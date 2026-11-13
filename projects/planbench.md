# PlanBench

Exact finite retry-risk analysis for supplied agent DAGs. Inspect the joint plan-success, completion-time and cost law, including exhausted retries, skip cascades and shared ancestors. A cheap failed run can satisfy a budget by skipping the work: within-limit probability is not successful-completion probability. The original seeded simulator stays unchanged.

## Retry risk and completion law

39 Python tests retain all 29 originals; four Node/actual-Chrome tests compare 28 complete Fraction/BigInt reports, 260 terminal histories, 177 joint atoms, 778 selected step rows, 24 responsive views and native-replayed trusted exports. An independent Bernoulli-bit/completion-event oracle checks 65 seeded DAGs and retry boundaries. An installed wheel reproduces both new CLI entrypoints and original validate/simulate gates outside the checkout.

At most six steps and two retries each. Failure rates, fixed durations and costs are declared, not learned. Calls fail independently; unlimited workers and immediate retries exclude resource contention, backoff, timeouts and correlated outages. Exact rational laws are not production reliability, empirical confidence or a new scheduling algorithm. Original float/seed behavior is preserved, not reinterpreted as a rational seed-equivalence guarantee.

## Exact outcome witnesses

A half-failing prerequisite followed by a five-time-unit dependent step has probability 1/2 of fitting time1/cost1, but zero probability of succeeding within those limits. For two independent half-failing parallel steps with one retry each, expected makespan is 7/4 rather than the maximum individual expected duration 3/2. A shared ancestor is sampled once, not separately per path.

Native code branches only on executed terminal outcomes. The independent browser enumerates all potential terminal assignments, schedules completion events and sums unused skipped-step outcomes. Complete histories retain final-attempt starts, dependency-ready times, costs and unconditional/conditional summaries. Zero-success conditional expectations stay undefined. No live tools are run.

[Live retry-risk inspector](https://midya8.github.io/planbench/) · [Source](https://github.com/midya8/planbench) · [Exact model and sources](https://github.com/midya8/planbench/blob/main/RISK.md)

## Original seeded simulation retained

# PlanBench

Validate and simulate agent task plans before they run.

## Validation and simulation

The original validator checks plan structure and declared input production. The
simulator follows one seeded sequence of failures with supplied durations, costs
and retry limits. Neither runs real tools or learns their latency or reliability.
The separate exact-risk API above enumerates all positive-probability histories
within its bounds.

## Original simulator

PlanBench treats a plan as a DAG of tool calls and checks it twice:

- **Semantic validation** - beyond JSON shape: duplicate step ids, unknown tools, unknown or self dependencies, cycles (Kahn's algorithm), and `requires` inputs that no dependency's tool produces. Findings are severity-ranked: structural blockers are high, unproduced inputs are medium.
- **Deterministic parallel simulation** - a discrete-event simulator runs steps as soon as their dependencies succeed, in parallel where the DAG allows it. Tool calls fail independently with the tool's declared failure rate, drawn from a seeded RNG: the same plan, registry and seed always produce the same trace. Steps retry within `max_retries`; when attempts are exhausted the step fails and its dependents are skipped, visibly.
- **Plan-shape metrics** - makespan from the event trace, total cost including retry cost, critical path by summed duration, and parallelism (total work over critical path): how much concurrency the DAG actually offers.
- **CI gates** - `--require-success`, `--max-makespan`, `--max-cost` and `--max-findings` fail the pipeline when a plan stops meeting policy.

## Verification

- The original 29 unit tests cover loader validation, every finding kind, topological ordering including cycles, sequential and parallel timing, seeded determinism, retry exhaustion with skip cascades, cost accumulation, metrics, all three report formats, and the CLI end to end including both sides of every gate.
- `bash examples/demo.sh` runs fully offline: a research-agent plan with flaky tools simulates green (retries exercised, real concurrency asserted), a broken plan is rejected with findings, and both gate sides are exercised.
- The current 39-test Python suite includes those originals and the exact-risk checks. Four Node/actual-Chrome tests check the browser. CI runs Python 3.10-3.13.

Bounds worth stating: durations and failure rates are declared in the fixtures, not learned from real executions - the simulation measures what a plan would do under those assumptions, it does not predict real-world latency. Validation checks structure and producibility, not whether a tool call would actually succeed.

## Links

- Repository: [midya8/planbench](https://github.com/midya8/planbench)
