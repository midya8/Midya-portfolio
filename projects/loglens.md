# loglens — case study

Dependency-free access-log analysis for incident work: error rates, status distribution, hottest failing paths, and the source IPs behind 5xxs, plus incident timelines, latency percentiles, and Markdown incident reports.

- Repo: [midya8/loglens](https://github.com/midya8/loglens)

## The constraint that shaped the build

When something breaks in production, the first question is usually answerable from the access logs — but raw logs are the wrong shape for answering it. They are long, mixed-format, and full of healthy traffic. The goal here was a tool that turns a log file into an incident answer in one command: what broke, where, when, and whether it lines up with a deploy — without standing up a log platform first.

## Decisions

- **Standard library only, no dependencies.** Like sre-toolkit, loglens runs on Python alone, so it works in any environment, including one mid-incident, with nothing to install or keep current.
- **CLI plus importable library.** The same analysis runs by hand in a terminal or inside automation, so an ad-hoc investigation and a scheduled check share one implementation.
- **Per-line format auto-detection.** nginx/Apache combined and JSON logs are parsed with per-line auto-detection, so mixed or evolving log formats do not need a preprocessing step before analysis starts.
- **Answer the incident questions first.** Error rate, status distribution, hottest failing paths, and the source IPs behind 5xxs are the headline outputs — the numbers an incident responder reaches for before anything else.
- **Time as a first-class dimension.** Per-bucket incident timelines, time-window filtering, and before/after comparison around a deploy timestamp turn a flat log into a story: when the problem started, whether it spiked, and whether a release lines up with it.
- **Latency, not just errors.** p50/p95/p99 latency and per-path volume/error/latency tables — sortable by errors, volume, or p95 — catch the slow failures that never become 5xxs, and a 2xx/3xx/4xx/5xx status-class roll-up keeps the overall shape visible at a glance.
- **Filters that scope everything.** Status-code, class, and path-prefix filters apply to every statistic, so narrowing to the failing slice — say, only API errors with `--status 5xx --path-prefix /api` — does not leave stray numbers computed over the full log.
- **Triage behind the 5xxs.** Method, user-agent, and referer breakdowns behind server errors help separate a bad client, a bad referrer, or a bad deploy from a genuine backend failure.
- **A gate, not just a report.** `--max-error-rate 0.05` exits 1 when the 5xx rate breaches the threshold, so the same analysis drops into CI or a scheduled health check against a fresh log slice.
- **Reports as output, not an afterthought.** Markdown incident reports with per-path breakdowns, spike windows, and optional before/after deploy comparisons come out of the same tool that did the analysis, in a format that can be committed, reviewed, and searched.

## Testing and compatibility

142 unit tests, with CI across Python 3.10–3.13.

## Worked example: the first five minutes of a 5xx spike

The commands below are the real loglens CLI, taken from the project's own usage docs. One command answers the headline questions, then each follow-up narrows the picture without re-parsing anything by hand:

```bash
python -m loglens app.log
# one-screen summary: error rate, status distribution, hottest failing
# paths, and the source IPs behind the 5xxs

python -m loglens app.log --status 5xx --path-prefix /api
# same summary scoped to API errors only

python -m loglens app.log --timeline --bucket 60
# per-minute buckets of requests and 5xxs, with spike windows flagged,
# so the start of the incident is visible instead of guessed

python -m loglens app.log --split-at 2026-10-31T22:00:00Z
# before/after comparison around a deploy timestamp: did the release
# line up with the spike?

python -m loglens app.log --report "Checkout 5xx spike"
# the whole investigation as a Markdown incident report, ready to
# commit, review, and search
```

The same analysis is importable as a library (`from loglens.parse import parse_lines`), so an ad-hoc investigation and a scheduled check share one implementation.

## What it demonstrates

Building incident tooling that respects the moment it is used in: no platform to stand up, no dependencies to install, and answers — what broke, where, when, and whether a deploy is implicated — before decoration. The design favors the responder: one command, a clear picture, and a report that slots directly into the incident workflow.
