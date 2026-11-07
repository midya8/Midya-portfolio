# PlanBench

Validate and simulate agent task plans before they run.

## Problem

Agent plans fail in boring ways that are cheap to catch before execution: a step calls a tool that does not exist, waits on an input nobody produces, or sits in a dependency cycle. And plans that look fine on paper miss their budgets once real tool latency, failures and retries are accounted for. Reviewing a plan by eye catches neither reliably.

## Approach

PlanBench treats a plan as a DAG of tool calls and checks it twice:

- **Semantic validation** - beyond JSON shape: duplicate step ids, unknown tools, unknown or self dependencies, cycles (Kahn's algorithm), and `requires` inputs that no dependency's tool produces. Findings are severity-ranked: structural blockers are high, unproduced inputs are medium.
- **Deterministic parallel simulation** - a discrete-event simulator runs steps as soon as their dependencies succeed, in parallel where the DAG allows it. Tool calls fail independently with the tool's declared failure rate, drawn from a seeded RNG: the same plan, registry and seed always produce the same trace. Steps retry within `max_retries`; when attempts are exhausted the step fails and its dependents are skipped, visibly.
- **Plan-shape metrics** - makespan from the event trace, total cost including retry cost, critical path by summed duration, and parallelism (total work over critical path): how much concurrency the DAG actually offers.
- **CI gates** - `--require-success`, `--max-makespan`, `--max-cost` and `--max-findings` fail the pipeline when a plan stops meeting policy.

## Verification

- 29 unit tests cover loader validation, every finding kind, topological ordering including cycles, sequential and parallel timing, seeded determinism, retry exhaustion with skip cascades, cost accumulation, metrics, all three report formats, and the CLI end to end including both sides of every gate.
- `bash examples/demo.sh` runs fully offline: a research-agent plan with flaky tools simulates green (retries exercised, real concurrency asserted), a broken plan is rejected with findings, and both gate sides are exercised.
- CI runs the same suite across Python 3.10-3.13.

Bounds worth stating: durations and failure rates are declared in the fixtures, not learned from real executions - the simulation measures what a plan would do under those assumptions, it does not predict real-world latency. Validation checks structure and producibility, not whether a tool call would actually succeed.

## Links

- Repository: [midya8/planbench](https://github.com/midya8/planbench)
