# sre-toolkit: error budgets, alert rules and incident records

A dependency-free Python CLI and library for error-budget math, supplied-sample burn rules, keyword alert triage and incident documents. The tools run on local records; they are not a monitoring service or an incident-response platform.

- Repo: [midya8/sre-toolkit](https://github.com/midya8/sre-toolkit)

## What the commands do

| Command | Result |
|---|---|
| `budget`, `downtime` | Budget consumed, burn rate, remaining bad events and allowed downtime |
| `burn` | Evaluate supplied long/short-window samples, suggest a policy template or replay timestamped buckets |
| `triage` | Keyword severity, deduplicated occurrence counts, optional inhibition, silences and service-to-owner routes |
| `report` | SLO snapshot tables, optional fleet summary and worst-first sorting |
| `postmortem` | Markdown or JSON incident records with timestamp-derived response metrics |
| `metrics` | Mean, median and nearest-rank p90 TTD/TTR, service/severity/week breakdowns and open action items |
| `slo-doc` | Markdown or JSON SLO definitions |

The library and CLI share the same math. Python's standard library is the only runtime dependency. That keeps local use simple; it does not make the tools suitable for every production environment without review.

## Alert rules and their limits

The default page rule requires burn of at least 14.4x on both the 1h and 5m windows. The ticket rule requires 6x on both the 6h and 30m windows. Requiring both windows filters some short spikes, but does not guarantee that a brief spike cannot page. Custom rules and `burn --suggest` provide policy inputs, not a validated policy for a particular service.

`burn --replay` evaluates trailing windows at supplied bucket ticks and reports firing intervals. It does not connect to telemetry or send pages. The supplied records, bucket resolution and rule choices determine the replay's scope.

Triage uses keywords and explicit rules. Repeated alerts retain their occurrence counts; silenced alerts remain visible with reasons. Inhibition suppresses lower-severity symptoms on a service with an active critical alert. Routes assign owners using an explicit default. These operations organize records; they do not identify an incident's cause or prove which alert deserves attention.

A budget-exhaustion projection assumes the current burn rate continues. It is not a forecast. Incident response-time summaries skip records without parseable timestamps, so the input coverage matters when comparing aggregates.

## Run the examples

From a repository checkout:

```bash
python -m sre_toolkit budget --slo 0.999 --total 10000 --bad 5 --window-days 30
python -m sre_toolkit burn examples/burn-samples.json
python -m sre_toolkit burn examples/burn-replay.json --replay
python -m sre_toolkit triage examples/alerts.json --inhibit
python -m sre_toolkit triage examples/alerts.json --routes examples/routes.json --by-owner
python -m sre_toolkit report examples/slo-snapshots.json --worst-first
python -m sre_toolkit postmortem examples/incident.json
python -m sre_toolkit metrics examples/incidents.json --json
python -m sre_toolkit metrics examples/incidents.json --action-items
```

Exit status 1 has command-specific meaning: an exhausted budget in `budget` or `report`, a critical firing rule in `burn` (including replay), or stale open actions in `metrics --action-items`. Not every command is a health gate. Read the command's output contract before using it in automation.

## Reproducible checks

The documentation review changes README and the opening docstring in `burn_alerts.py`, not executable code, tests or fixtures. A fresh public checkout passes 254 Python tests and compilation. The parsed burn-alert module is identical outside that docstring. Nineteen CLI comparisons against the original public base preserve stdout, stderr and exit status, including failing budget and burn gates.

A copied package runs outside the checkout: all nine module origins resolve to that copy, and the same nineteen CLI comparisons pass there. CI covers Python 3.10-3.13. There is no package-build or Pages deployment for this repository.

```bash
python -m unittest discover -s tests -v
python -m compileall -q sre_toolkit tests
```

These checks support behavior preservation on the tested inputs. They do not measure operational alert quality, incident outcomes or the suitability of a policy for a real service.
