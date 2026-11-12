# EvalForge - case study

EvalForge runs command adapters against supplied checks and compares saved task results. Its browser inspectors let you edit paired results or a clustered candidate family, then inspect the complete calculation. A passing comparison means the configured regression rule passed, not that a model is good.

- [Source and CLI](https://github.com/midya8/evalforge)
- [Paired inspector](https://midya8.github.io/evalforge/)
- [Family inspector](https://midya8.github.io/evalforge/family.html)

## Compare the same tasks

A whole-run mean can fall while every matched task improves if the candidate adds hard tasks or omits easy ones. EvalForge validates result rows and computes all-task and matched-task summaries separately. It rejects duplicate IDs rather than silently collapsing them and does not trust stored summary scores.

The original per-task rule remains: a score drop beyond tolerance, a lost pass or a missing baseline task fails. Added tasks do not fail it. Persistent failed or errored tasks can pass a comparison if they do not regress. Equal IDs do not establish matching task definitions, matching scorers or independent samples.

The paired inspector retains each complete normalized baseline/candidate record, delta, gate margin and decision. A fixed 0..1 chart keeps equal scores distinct. Editing hides stale results and disables export until recomputed. Export contains the current report; model output is displayed as text.

Two bounded arithmetic controls show every term:

- Paired sign flips enumerate all assignments of nonzero .001-score differences and inclusive absolute two-sided tails. Zero differences are factored out.
- Exact McNemar shows all four pass-status cells, binomial counts and the doubled lower tail capped at one. It tests binary pass marginals, not mean scores.

No pairs is undefined. All ties give p=1, not equivalence. Task selection, dependence, changed scorers and repeated benchmark searches limit interpretation. These established methods do not supply a superiority verdict or change the regression gate.

[Paired contract, provenance and prior work](https://github.com/midya8/evalforge/blob/main/EVIDENCE.md)

## One sign per declared cluster

The separate family audit gives each supplied cluster one sign shared across every candidate. Its default candidate has raw absolute-sum tail 1/4 and family-maximum tail 1/2. Repeated-row controls change the declared flip unit without changing observed task-weighted sums.

The inspector accepts at most four candidates, 12 common tasks and eight clusters, with integer score ticks 0..1000. Zero blocks and ties keep full multiplicity; empty evidence stays undefined. Every assignment, contribution and maximum remains inspectable.

Supplied cluster labels do not prove independence, joint symmetry or randomization. Marginal symmetry is not enough for the joint maximum. Complete-joint-null orbit arithmetic does not provide universal strong-FWER protection under arbitrary partial nulls, prove model superiority or establish equivalence.

[Family contract and credited sources](https://github.com/midya8/evalforge/blob/main/FAMILY.md)

## Local execution and reports

The standard-library harness sends prompts to command adapters on stdin and reads answers from stdout. Exact, contains, regex, JSON/subset, token-F1, numeric and length checks produce JSON, HTML, JUnit, Markdown and SARIF reports. Retries, timeouts and bounded workers remain supported. Structural task validation runs first; check-specific validation happens during scoring. Invalid runtime and gate options fail before adapter execution.

Adapters and task checks run locally with the caller's permissions. EvalForge does not sandbox them. Review unfamiliar programs before running them.

All 68 original tests, task data, mock adapter and demo are retained and fingerprinted. The original six-task mock run and HTML report remain visible; the current renderer reproduces that HTML exactly. The mock is synthetic, not an AI benchmark. Supplied scores are not authenticated or rescored by the inspector.

```sh
python -m evalforge validate examples/tasks.jsonl
python -m evalforge run --tasks examples/tasks.jsonl \
  --cmd "python examples/mock_model.py" --out run.json --fail-under 1
python -m evalforge audit --spec examples/audit.json --json audit.json
python -m evalforge.family_cli --input examples/family.json
```

## Reproduction checks

The current suite has 102 Python tests and seven Node/actual-Chrome tests. It retains the earlier 92-test paired suite and all 68 original tests. CI covers Python 3.10-3.13 and actual Chrome. These checks use fixed synthetic controls and the offline mock, not paid APIs or hosted model calls.

Paired checks compare all 780 short integer-difference vectors with a separate sign enumeration, test small pass tables and compare 200 seeded original-gate references. Independent JavaScript agrees on 24 complete reports. Chrome checks all pairs, full records, assignments, binomial rows, chart dots, stale/export behavior and 320/390/1280px containment.

Family checks compare 150 seeded matrices and all 729 small two-column controls with independent original-task relabeling. Native aggregation/bit masks and browser Cartesian signs/original-task sums agree on 24 reports, 118 task rows, 73 cluster rows, 506 assignments and 10,474 candidate-by-cluster contributions. Chrome checks displayed rows, geometry, invalidation and both exports.

```sh
python -m unittest discover -s tests -q
npm test
bash tools/wheel_smoke.sh
bash tools/family_wheel_smoke.sh
```

Isolated installed-wheel checks run outside the checkout. The original suite checks nine module origins, retained reports, the mock adapter and report formats. The family suite reproduces all 24 reports through API, module and console entry points. Same-environment evidence regeneration is byte-identical, not a promise across platforms. Retained timings are one local execution, not a latency benchmark.
