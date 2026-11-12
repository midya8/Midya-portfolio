# loglens

Standard-library analysis of nginx / Apache combined logs and structured JSON logs. It reports recorded request counts, status codes, paths, latency, response sizes and client metadata. CLI and importable functions share the same parsers and statistics. Python 3.10+.

## Start with the question

| Question | Flags |
| --- | --- |
| Which recorded requests failed? | `--errors`, `--path-status`, `--by-path` |
| When did recorded 5xx rates rise? | `--timeline`, `--spikes`, `--bucket` |
| How do two recorded windows differ? | `--split-at`, `--vs` |
| What durations and sizes are available? | `--latency`, `--latency-dist`, `--apdex`, `--by-size` |
| Which client metadata recur? | `--by-ip`, `--methods`, `--agents`, `--referers` |

Filters select time bounds, status codes and path prefixes. `--json` emits a summary for scripts; `--report` emits Markdown. Review client addresses, paths, query strings and other log content before sharing either output.

## What the measurements mean

The combined and JSON parsers produce the same `LogRecord`. Auto-detection happens per line, so mixed files can be read. Unparseable lines are skipped rather than stopping the run. That keeps valid records usable but can bias every statistic when missing or malformed records are not representative.

A timeline buckets recorded requests and 5xx responses. Spike thresholds flag buckets by count and rate. Neither establishes the real incident start, cause or duration. Timestamp parsing has its own coverage; naive timestamps are treated as UTC. Source logs need an independently checked capture window and timezone.

Before/after and baseline comparisons describe recorded differences. They do not isolate a release's effect from traffic mix, collection changes or other concurrent changes. A path-status table counts statuses by path; a 502 alone does not identify which upstream caused it.

Latency and Apdex use records carrying durations. The configured Apdex threshold divides those samples into satisfied, tolerating and frustrated duration bands; its weighted score is not measured human satisfaction. Source IPs, user agents and referers are recorded metadata, not person identity, proof of a retrying process or bot classification. Response-size totals describe recorded response bytes, not complete network traffic.

## Exit-code gates

`--max-error-rate` exits 1 when the selected records' 5xx rate exceeds the chosen threshold. `--min-apdex` checks the duration-based score and requires `--apdex`; no timed samples fail that gate rather than passing unmeasured. A gate evaluates the supplied log, not service availability or log freshness. Choose a window and verify collection coverage before using it in automation.

## Reproduce a local report

The repository includes small example logs. These commands need no remote service:

```bash
python -m loglens examples/json.log --format json --latency --json
python -m loglens examples/access-agents.log --agents --referers --methods --json
python -m loglens examples/access.log --vs examples/access-baseline.log --json
```

The error-rate control below is expected to exit 1 because the sample includes 5xx records and the threshold is zero:

```bash
python -m loglens examples/access.log --max-error-rate 0 --json
```

## Verification

241 tests cover parsing, mixed and corrupt input, statistics, timeline buckets, spike windows, durations, Apdex, filters, comparisons, reports and CLI flags and gates. CI runs Python 3.10-3.13.

```bash
python -m unittest discover -s tests -v
python -m compileall -q loglens
```

A fresh public checkout passes the suite and compile check. A copied module was also checked outside the checkout: nine imported module paths resolve to that copy, and all four CLI commands above return the expected exit codes and parseable JSON. This is functional verification on local examples, not a performance benchmark or a production-readiness claim. There is no package build configuration or hosted app in the repository.

## Links

- Repo: [midya8/loglens](https://github.com/midya8/loglens)
