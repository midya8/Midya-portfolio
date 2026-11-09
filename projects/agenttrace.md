# AgentTrace - case study

Local-first validation, analysis, and HTML, JUnit XML, Markdown and SARIF reporting for AI agent execution traces: read JSONL traces, check their structure, summarize every run, detect repeated tool/action loops, track failures, latency, tokens and cost, enforce CI-friendly gates, and render a standalone HTML timeline. Standard library only, CLI, 57 unit tests (all original 33 retained) with CI across Python 3.10-3.13.

- Repo: [midya8/agenttrace](https://github.com/midya8/agenttrace)

## Graph and timing evidence

Full-record graph/timing inspector: every endpoint, interval segment, parent path/relation, normalized record and p95 term. Independent Python/JavaScript recomputation and current JSON export. 57 Python tests retain all original 33 tests; 24 synthetic controls, 11,110 interval checks and an isolated installed-wheel reproduction. Parent links are not causal dependencies; recorded coverage/overlap is not CPU, idle, waste or utilization. No model/API call.

- [Live inspector](https://midya8.github.io/agenttrace/)
- [Definitions and controls](https://github.com/midya8/agenttrace/blob/main/EVIDENCE.md)

## The constraint that shaped the build

Agent frameworks are good at showing a friendly final answer and bad at preserving the operational truth of how it got there — which tool was called how many times, where the time went, what it cost, whether it looped. The goal was a tool that keeps that truth in a portable record: every LLM call, tool call, action, observation and error as one JSONL event, validated before it is trusted, and reviewable as a report without a server — without sending prompts or outputs anywhere.

## Decisions

- **One JSONL event per step.** Every event carries `run_id`, `step`, `kind` and `name` — kinds `llm`, `tool`, `action`, `observation`, `error`; statuses `ok`, `failed`, `cancelled`, `timeout` — with optional `duration_ms`, `tokens_input`, `tokens_output`, `cost_usd`, `input`/`output` payloads, and a `parent` link to a step in the same run (forward references allowed once resolved). A format agents and test harnesses can append to and Unix tools can inspect.
- **Validation first.** Malformed events, duplicate step IDs, unknown parents, negative numbers, unknown event types, and bad timestamps are reported before analysis is trusted — a corrupt trace never produces confident-looking numbers.
- **Loops are a signature, not a count.** Repeated signatures are detected from event kind, name, and normalized input payload, so retries with changed arguments do not count as the same loop — the gate fires on an agent stuck repeating itself, not on an agent retrying with different inputs.
- **Latency and cost are explicit.** Summaries carry p95 step latency, run depth, token totals, and cost alongside error counts — so "slow" and "expensive" are numbers in the same report as "failed", not impressions from watching a run.
- **Gates turn review into a script.** `--fail-on-error`, `--max-loop-repeat`, `--max-p95-ms`, `--max-cost-usd`, and `--max-steps` make trace review a command CI can run, with meaningful exit codes.
- **Compare against the run you trust.** Baseline/candidate comparison reports absolute and percentage deltas for runs, steps, errors, tool and LLM calls, repeated signatures, p95 latency, tokens, and cost — and exits 1 when a configured gate fails, so an agent change is protected in CI without calling a model.
- **The report is safe to archive, and fits CI.** A standalone HTML timeline with untrusted trace payloads escaped, no JavaScript, no external service — the run stays reviewable after the agent and its logs are gone. The same analysis also emits JUnit XML for CI test viewers, Markdown for native CI job summaries, and SARIF that maps validation and gate failures to code-scanning tools; the offline demo generates all four formats from the fixed local trace fixture without any model call.
- **The demo proves the loop without a model.** A fixed local trace fixture — a five-step baseline run and a slightly slower candidate — demonstrates validation, analysis, gates, and reporting fully offline; its timing and cost numbers are fixture data, not evidence about a real model.

## Testing and compatibility

57 unit tests (all original 33 retained), with CI across Python 3.10-3.13. The suite runs fully offline.

## Worked example: catching a looping agent

The commands below are the real AgentTrace CLI, taken from the project's own usage docs. Validate the trace, analyze it, gate it, compare a candidate against the baseline, then render the report:

```bash
python3 -m agenttrace validate examples/trace.jsonl
# structure first — malformed events, duplicate step IDs, unknown
# parents, and bad timestamps fail here, before any analysis

python3 -m agenttrace analyze examples/trace.jsonl --json analysis.json \
  --junit analysis.xml --markdown analysis.md
# run summaries, tool/LLM call counts, latency and cost rollups,
# run depth, and loop detection, as JSON for tooling — plus a JUnit
# report for CI test viewers and a Markdown summary for CI job
# summaries; the offline demo also generates the SARIF form

python3 -m agenttrace analyze examples/trace.jsonl \
  --fail-on-error \
  --max-loop-repeat 3 \
  --max-p95-ms 500 \
  --max-cost-usd 0.01 \
  --max-steps 10
# the same analysis as a gate — errored steps, a repeated
# tool/action signature, slow steps, or an over-budget run
# fails the command

python3 -m agenttrace compare examples/trace.jsonl examples/trace_candidate.jsonl \
  --max-new-errors 0 \
  --max-p95-increase-ms 100 \
  --max-cost-increase-pct 50 \
  --json compare.json
# candidate against baseline: new errors, p95 growth, and cost
# growth each have their own gate

python3 -m agenttrace report examples/trace.jsonl --out report.html
# a standalone HTML timeline, untrusted payloads escaped,
# reviewable without a server
```

## What it demonstrates

Agent runs as inspectable data: validate the record before trusting it, make loops, latency, and cost explicit numbers, and gate changes against a saved baseline — the same discipline as the evaluation harness, applied to the run itself rather than the output.

## Links

- Repo: [midya8/agenttrace](https://github.com/midya8/agenttrace)
