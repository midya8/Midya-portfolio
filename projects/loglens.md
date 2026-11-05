# loglens — case study

Dependency-free access-log analysis for incident work: point it at an nginx/Apache combined log or structured JSON logs and get the numbers that matter in the first five minutes of an incident — error rate, status distribution, hottest paths, hottest failing paths, and the source IPs behind 5xxs. Standard library only, CLI plus importable library, 241 unit tests with CI across Python 3.10–3.13.

- Repo: [midya8/loglens](https://github.com/midya8/loglens)

## The constraint that shaped the build

During an incident nobody wants to remember `awk` incantations. The log file already contains the answer to "what broke, when, and for whom" — the problem is getting at it fast, while the incident is still happening, without learning a query language or standing up a log pipeline first. The goal here was a tool that turns a log file into a one-screen summary in a single command, and whose functions are importable so the same analysis can run inside bigger tooling.

## Decisions

- **The headline answers first.** A single invocation leads with the numbers that matter in the first five minutes — error rate, status distribution, hottest paths, hottest failing paths, and the source IPs behind 5xxs — and only then narrows into timelines, latency tables, and per-client breakdowns, so the first screen already says what broke.
- **Format auto-detected per line.** Format detection is per line (`--format auto`, the default), so a file that switches between combined and JSON lines parses both, and a single format can be forced with `--format` — the tool adapts to the log, not the other way around.
- **Two formats, one record.** The combined-format and JSON parsers both emit the same `LogRecord`, so the statistics code never cares about the source format — every later feature works on either kind of log without a second implementation.
- **Unparseable lines are skipped, not fatal.** Real log files are mixed and partially corrupt, so a line that cannot be parsed is skipped rather than aborting the run — a damaged line never costs the analysis of the thousands of good ones around it.
- **Filters scope every statistic.** `--since`/`--until` scope every statistic to an incident window, `--status 5xx,404` scopes to exact codes and classes, and `--path-prefix /api` scopes to a service's surface — so narrowing to a failing slice never leaves stray numbers computed over the full log.
- **A timeline shows when it started.** `--timeline` buckets requests and 5xxs per minute (or any bucket size) so the incident's start is visible, and spike buckets only flag when both the error rate and the count clear a threshold — a single error in a quiet minute never reads as a spike.
- **Percentiles, not averages.** `--latency` reports p50/p95/p99 and the slowest requests, and `--latency-dist` shows the latency shape over fixed millisecond buckets — a p95 of 400ms reads differently when the mass sits at 250–500ms versus a long tail past 1s, and the average would hide both.
- **Apdex: one number for how it felt.** `--apdex SECONDS` computes the Apdex user-satisfaction score at threshold T — requests within T satisfied, within 4T tolerating, beyond 4T frustrated — plus a per-path table worst-first, so the endpoint dragging the score down leads; `--min-apdex 0.94` turns it into a pipeline gate, and a log with no durations fails the gate rather than passing unmeasured.
- **A pipeline gate, not just a report.** `--max-error-rate 0.05` exits 1 when the 5xx rate breaches the threshold, so loglens drops into CI or a cron health check against a fresh log slice — the same command that investigates an incident also guards against the next one.
- **Before/after around a deploy.** `--split-at` compares the windows on either side of a deploy or alert — error-rate delta, newly failing paths, and paths that recovered — and `--vs baseline.log` answers "did this release make things worse?" across two whole logs, with the paths carrying the biggest error-count increases ranked as regressions.
- **The failing-path status pivot.** `--path-status` answers "are the /api/checkout 5xxs actually 502s from the upstream?" — the failing endpoints (4xx+5xx) ranked worst-first, each with its per-status-code counts and total volume, so the next question is about the upstream, not the log.
- **Per-path and per-client tables.** `--by-path` ranks endpoints by error count — or by volume or p95 latency — with volume, error rate, and p95 latency, so the path causing the pain leads; `--by-ip` gives the same table per source IP, answering "is one client retry-storming us?", and `--by-hour` buckets the window by UTC hour of day, so a daily pattern stands out in a multi-day log.
- **Methods, agents, and referers behind the 5xxs.** `--methods` answers "is the spike on writes or reads?", `--agents` ranks user agents overall and behind 5xxs — the fast answer to "is this spike a bot or real users?" — and `--referers` does the same for referers, answering "which page were users on when it broke?"
- **Bytes are bandwidth answers.** `--by-size` turns the bytes column into bandwidth: total bytes served, mean and largest response, and the paths ranked by bytes moved with their share of the total — because the most requested path is not always the one moving the megabytes.
- **The exact requests, not just the aggregates.** `--errors` lists the failing requests themselves — timestamp, client, method, path, status, duration — capped by `--top` with a "+N more" note, so the path from "the rate spiked" to the exact requests that failed is one flag.
- **The report is the incident document.** `--report "Title"` renders the findings as a Markdown document — window, rates, failing paths, source IPs, the methods behind the 5xxs, a per-path breakdown table, latency, and the incident window with its error peak — ready to paste into an incident doc or ticket, not a separate chore after the analysis.
- **JSON output for tooling.** `--json` emits the whole summary — counts, rates, top-N, latency, timeline — as JSON, so dashboards and scripts can consume it without scraping text.
- **CLI plus importable library.** Each analysis works two ways: as a command you run by hand, and as a library you import into automation — the same error-rate and top-path math that answers a question in the terminal can run inside bigger tooling without being rewritten.

## Testing and compatibility

241 unit tests, with CI across Python 3.10–3.13.

## Worked example: the first five minutes of a 5xx spike

The commands below are the real loglens CLI, taken from the project's own usage docs. One question leads to the next — summary, timeline, failing slice, failing paths, the requests themselves, the deploy that preceded it, the report — and every step is the same tool, not a new setup:

```bash
python -m loglens examples/access.log
# one-screen summary: error rate, status distribution, hottest paths,
# hottest failing paths, and the source IPs behind the 5xxs

python -m loglens examples/access.log --timeline --bucket 60
# per-minute timeline: when the incident started, and which minutes spiked

python -m loglens app.log --status 5xx --path-prefix /api
# API errors only — every statistic scoped to the failing slice

python -m loglens app.log --path-status
# the failing endpoints ranked worst-first, with per-status-code counts:
# are the /api/checkout 5xxs actually 502s from the upstream?

python -m loglens app.log --errors
# the failing requests themselves — timestamp, client, method, path,
# status, duration — capped by --top with a "+N more" note

python -m loglens app.log --split-at 2026-10-31T22:00:00Z
# before/after the deploy: error-rate delta, newly failing paths,
# and paths that recovered

python -m loglens app.log --report "Checkout 5xx spike"
# the findings as a Markdown incident report, ready to paste
# into the incident doc or ticket

python -m loglens app.log --max-error-rate 0.05
# exit 1 above a 5% 5xx rate — the same check, as a pipeline gate
```

The same analysis is importable as a library (`from loglens.parse import parse_lines`, `from loglens.stats import error_rate, top_paths, top_error_ips`), so an ad-hoc question in the terminal and a scheduled check share one implementation.

## What it demonstrates

Incident tooling that starts from the question, not the query language: one command, the headline answers first, and the same analysis importable into bigger tooling. The report is what the tool produces, not a chore after the work — and a log file you already have is enough to answer what broke, when, and for whom.

## Links

- Repo: [midya8/loglens](https://github.com/midya8/loglens)
