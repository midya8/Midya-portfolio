# EvalForge - case study

Local-first LLM/agent evaluation with complete paired comparison evidence.

- [Source](https://github.com/midya8/evalforge)
- [Editable paired inspector](https://midya8.github.io/evalforge/)
- [Evidence contract and prior work](https://github.com/midya8/evalforge/blob/main/EVIDENCE.md)
- [Original README](https://github.com/midya8/evalforge/blob/main/docs/original-readme.md)

## The average changed. Did the tasks?

A whole-run mean can fall while every matched task improves: the candidate may add hard tasks and omit easy ones. Original comparison also silently collapsed duplicate ids and trusted stored summaries. EvalForge now validates result rows, rejects duplicate ids and recomputes all-task and matched-task summaries separately. Equal ids remain supplied evidence, not proof that task definitions or scorers match.

The original per-task binary64 gate is preserved: a score drop beyond tolerance, a lost pass or a missing baseline task fails. Added tasks do not fail it. Every matched task now retains its complete normalized baseline/candidate record, delta, margin, pass-loss/score-drop flags and classification; native result-level metadata is retained too. Persistent failed/error tasks may pass a comparison if they do not regress. A comparison PASS is not an absolute evaluation-quality verdict.

## Read every witness

An independent JavaScript engine recomputes edited result lists. The fixed 0..1 dumbbell chart adapts to narrow screens; baseline rings and candidate dots remain distinct when equal. All paired rows, missing/added records, raw output/error/check/tag/latency/attempt evidence, pass cells and null assignments remain inspectable. Editing hides stale results and disables export until recomputed. Export is the complete current report, not a reference fixture. Model output is displayed as text.

Two bounded arithmetic controls expose the entire calculation:

- Paired sign flips enumerate every assignment of nonzero .001-score differences, each signed contribution and sum, with inclusive absolute two-sided tails. Zero differences are factored out, not silently dropped from coverage.
- Exact McNemar exposes the four paired pass-status cells and every binomial count, with the doubled lower tail capped at one. It tests binary pass marginals, not score means.

No pairs is undefined; all ties give p=1, not equivalence. Independent/exchangeable pairs, task selection, changed scorers, dependence and repeated benchmark searches limit interpretation. No significance threshold, multiplicity correction or automatic inference gate is added. These are established methods made inspectable, not a new statistical method or evidence of model superiority.

## The original harness is still there

Standard-library Python executes stdin/stdout command adapters with retries, timeout and bounded workers. Deterministic exact/contains/regex/JSON/subset/token-F1/numeric/length checks write durable JSON plus HTML/JUnit/Markdown/SARIF reports. Task structural validation runs first; check-specific validation occurs during scoring. The command is trusted local code, not a sandbox. Invalid run gate/runtime options now fail before execution.

All 68 original tests, task data, mock adapter and demo are byte-preserved and fingerprinted. The original README, actual original six-task mock run and HTML report remain visible; the current renderer reproduces that HTML byte-for-byte. Controlled replacement outputs are clearly labelled, not misrepresented as new adapter/model runs. The mock is synthetic, not an AI benchmark.

## Verification

- 92 Python tests on 3.10-3.13, including all 780 short integer difference vectors against separate brute-force signs, small pass tables, 200 seeded original-gate references, malformed rows, duplicate ids, stale summaries and metadata retention.
- 24 complete retained reports independently compared at all 11,808 numeric and 2,691 other scalar leaves.
- Actual Chrome verifies 53 paired rows, 564 sign assignments, 118 displayed full records, 47 binomial rows, all chart dots/pass cells, export/invalidation and 320/390/1280 containment.
- Fresh public source plus an isolated installed wheel outside the checkout checks nine module origins, all retained reports and audit/mock-adapter/compare CLI with HTML/JUnit/Markdown/SARIF outputs.

The inspector is bounded to 12 rows per side/eight matched pairs and a .001 score/drop grid; native comparison is not. Retained timings are one local execution, not a latency benchmark. Same-environment regeneration is not cross-platform determinism. No API key, paid API or hosted model call is used.
