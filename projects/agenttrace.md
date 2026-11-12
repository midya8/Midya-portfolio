# AgentTrace - case study

AgentTrace reads local JSONL traces, checks their structure and reports recorded durations, tokens, costs and repeated tool/action signatures. A browser inspector separates duration sums from elapsed coverage. A second inspector tests a hypothetical fixed-interval retention policy. Neither inspector calls a model or measures real resource use.

- [Source and CLI](https://github.com/midya8/agenttrace)
- [Timing inspector](https://midya8.github.io/agenttrace/)
- [Fixed-interval policy inspector](https://midya8.github.io/agenttrace/capacity.html)

## Recorded time, not a critical path

Nested or overlapping steps can add up to more time than a run covers. The timing inspector keeps those quantities separate: step-duration sum, recorded span, busy interval union and peak recorded spans. Parent links supply context, not finish-to-start dependencies. A parent-path duration sum is not elapsed time or a causal critical path.

Missing timestamps stay unknown. Recorded gaps do not prove idle time, overlap does not prove wasted work, and peak spans do not count workers. The inspector cannot establish complete instrumentation or synchronized clocks.

Each supplied record remains inspectable alongside endpoints, interval segments, parent paths and relations, and percentile terms. The native parser rejects duplicate JSON keys and nonfinite numbers, reports invalid graphs, and handles deep graphs without recursive traversal. The browser uses a narrower documented input contract.

[Timing definitions, controls and prior work](https://github.com/midya8/agenttrace/blob/main/EVIDENCE.md)

## A separate fixed-interval policy

Given supplied intervals, drop penalties and an overlap cap, which subset has the least dropped penalty? At cap 1, two touching spans worth 6 each beat one enclosing span worth 9. Integer min-cost flow supplies a feasible assignment and a certificate with matching primal and dual bounds. The inspector shows every edge, residual reduced cost, residual arc and capacity-frontier choice.

The policy accepts at most 12 intervals, cap 0..4 and bounded integer endpoints and penalties. Half-open touching spans can share a hypothetical lane; zero-length points consume no capacity by convention. Primary penalty ties select the smallest retained input-order bitmask, not every primary optimum.

This does not delete trace records, infer real workers, establish dependency-safe cancellation, predict runtime or claim measured savings. The original analyzer and its gates are unchanged.

[Policy contract and credited sources](https://github.com/midya8/agenttrace/blob/main/CAPACITY.md)

## CLI and reports

Events identify a run, step, kind and name, with optional status, timestamps, duration, tokens, cost, payloads and a parent link. Validation reports malformed records and invalid references before their analysis is trusted. Repeated kind/name/input signatures flag possible loops; changed arguments form a different signature.

Analysis and baseline/candidate comparison can fail configured error, repetition, duration, cost and step-count gates. Reports include JSON, standalone escaped HTML, JUnit XML, Markdown and SARIF. These are checks on supplied records, not evidence that an agent's answers are correct. Trace payloads are data, never instructions.

```sh
python -m agenttrace validate examples/trace.jsonl
python -m agenttrace analyze examples/trace.jsonl --json analysis.json
python -m agenttrace compare examples/trace.jsonl examples/trace_candidate.jsonl \
  --max-new-errors 0 --max-p95-increase-ms 100 --max-cost-increase-pct 50
python -m agenttrace report examples/trace.jsonl --out report.html
python -m agenttrace.capacity_cli --input examples/capacity.json
```

## Reproduction checks

The current suite has 64 Python tests and seven Node/actual-Chrome tests. It retains the earlier 57 Python tests, including the original 33. CI covers Python 3.10-3.13 and actual Chrome. Fixed synthetic traces demonstrate the commands without a model or paid API; their timing and cost fields are not measurements of a real system.

Timing checks compare all 11,110 short interval lists with a separate unit-cell reference and compare 24 complete reports with an independent scalar JavaScript implementation. Chrome checks displayed records, tables, timeline geometry, export invalidation and 320/390/1280px containment.

Policy checks compare 250 seeded inputs at all five capacities with full-subset/unit-cell references. Another 120 larger controls check feasibility and certificates. Independent browser enumeration and shortest-path calculations agree with native reports on 24 controls. Browser exports replay through the native CLI.

```sh
python -m unittest discover -s tests -q
npm test
bash tools/wheel_smoke.sh
bash tools/capacity_wheel_smoke.sh
```

The isolated wheel checks run outside the checkout: the original suite verifies eleven module origins and all report formats; the policy suite checks all 24 reports through API, module and console entry points. Same-environment evidence regeneration is byte-identical, not a promise of identical output on every platform.
