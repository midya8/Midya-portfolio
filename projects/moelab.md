# MoeLab: the batch decides

A pure-Python mixture-of-experts model with separate inspectors for exact finite capacity dispatch and routing boundaries. The original sparse trainer, dense baseline, frozen models, 340 data rows and measured results stay intact.

[Capacity inspector](https://midya8.github.io/moelab/capacity.html) · [Route inspector](https://midya8.github.io/moelab/) · [Source](https://github.com/midya8/moelab)

## Exact capacity dispatch

The supplied table defines rational gate probabilities, eligibility and expert capacities. Each token receives one eligible expert or skips its expert update; skipping does not delete the token. First maximize dispatched tokens, then their retained gate mass. This objective does not optimize equal loads or task quality.

Four greedy controls share the same input-order/confidence-order and top-choice/drop/best-available rules on every input. Confidence-first best-available retains `51/100` gate mass on one control versus the global `49/50`; on another it matches the optimum. Maximizing coverage can retain less gate mass while dispatching more tokens. Controls are not required to lose.

A Fraction dynamic program keeps every reachable capacity state, feasible edge, optimal suffix count and optimal assignment marginal. Its optimal-edge DAG represents the whole globally optimal family. Hall bottleneck witnesses enumerate every token subset and its eligibility-induced slot deficit. Spare total capacity alone need not prevent skipped updates.

An independent Cartesian-product verifier never imports the producer. It reconstructs the complete assignment family and every report leaf, state, edge, count and bottleneck. The separate browser BigInt engine also matches complete reports, not rounded summaries.

## Gate mass is not task quality

Two routing optima can have the same dispatched count and retained gate mass but scalar-update MSE **0 and 25**. The report gives attained minimum and maximum error witnesses over the entire routing-optimal family. Targets never select that family; they enter only this secondary audit. Updates use the original gate times the supplied scalar expert value, without post-routing gate renormalization. This is not an end-to-end residual-stream loss or a model-quality result.

Fourteen controls include three bridges from the original aux/no-aux/initialization models and the first six training rows. Captured binary64 gate/output bytes carry provenance and reproduce numerically at `1e-12`. Gates then undergo explicitly labeled exact rational row normalization; the dispatch calculation is not claimed to reproduce the original rounded inference exactly.

[Capacity objective, proof, complete schema, sources and limits](https://github.com/midya8/moelab/blob/main/CAPACITY.md)

## Sparse training and measured results

Four synthetic input regimes use different linear target maps. A single linear map cannot represent the construction. The comparison is a trained one-hidden-layer tanh MLP with 145 parameters against the mixture's 136, under the recorded optimizer budget. A wider or better-tuned dense model may close the measured gap.

Training predicts `y = g_e h_e`, where `g` is the router softmax, `h_e` is a linear expert and `e` is the lowest-index maximum gate. Hold that branch fixed. With `s = 2(y - target)`:

```
dL/dW_ej = s g_e x_j
dL/dz_k = s h_e g_e (delta_ek - g_k)
aux = E sum_k g_k^2
```

These ordinary branch derivatives are checked by finite differences away from routing boundaries. They do not differentiate argmax or use a soft backward surrogate. The module, evaluation and test docstrings now describe the implementation; training arithmetic and all test assertions are unchanged.

| Frozen fixture metric | Value |
|---|---:|
| Sparse MoE test MSE | 0.0303 |
| Dense MLP test MSE | 0.1853 |
| Soft-evaluation MoE test MSE | 0.6291 |
| No-aux MoE test MSE | 0.0015 |
| Worst-regime routing purity | 1.0000 |
| Expert usage shares | [0.25, 0.25, 0.25, 0.25] |

Soft evaluation is worse here, but this comparison does not isolate a cause. The symmetric fixture balances itself with or without the auxiliary penalty, and no-aux fits better. It does not test the penalty under imbalanced traffic. The frozen no-aux value is 0.0014970307791088836; an earlier 0.0010 was a prose error, not a changed training result. Gates pin the mixture's own fit, purity and usage, not a requirement that a baseline lose.

[Implemented training equations](https://github.com/midya8/moelab/blob/main/DESIGN.md)

## Follow the routing seam

Along an affine input path, router logits and expert outputs are affine functions. Python Fraction and browser BigInt engines enumerate every pair crossing, exact point tie and open cell, including nonwinning crossings, persistent winners and sub-grid intervals. Choose any pair of the 240 original training examples, three original model states or eight arithmetic controls. All 340 train/test positions remain inspectable.

The selected gate probability stays in the output. Both one-sided limits and the tie point are reported: a route can change with zero jump, and a triple-tie point can differ from both limits. Fixed-branch derivatives remain distinct from differentiation through a seam. Exact rational geometry and rounded binary64 inference are separate; a smallest-subnormal control shows their selected experts can disagree. The 65-point plot does not discover boundaries and can miss thin cells; the exact table preserves them.

The mean per-example `E sum p^2`, squared batch-mean gates `E sum(mean p)^2` and Switch's `E sum fP` are different statistics. All three can equal one while every tied row chooses expert 0. A low penalty is not a traffic guarantee.

[Route equations, schema, sources and limits](https://github.com/midya8/moelab/blob/main/ROUTES.md)

## Reproduction and limits

All **53 Python and nine Node/Chrome tests** retain the earlier nine original tests and the 39-Python/five-Node route suite. Capacity checks include 225 probability pairs, 1,024 eligibility/capacity cases, 125 complete native/BigInt reports, tiny gates, permutation invariants, every-leaf tampering and task-error extrema. Actual Chrome checks 98 dispatch displays, 1,085 gate/support cells, all 813 capacity states, 42 layouts and two real JSON downloads with native verification.

The route evidence includes 32 complete witnesses, 8,176 evaluation positions, 2,080 path display positions, 80 independent integer geometries and 160 independent 70-digit Decimal controls. Chrome checks all destination choices and evaluation positions, exports, invalid-state clearing and 320/390/1280 layouts. Both outside-checkout wheel scripts pass: the original retrains aux/no-aux/dense models and compares full data/models/report at `1e-11`, keeping regenerated rational fractions distinct from frozen models; the capacity wheel imports ten modules and independently replays all 14 controls. CI covers Python 3.10-3.13, demo, browser and installed packages.

Capacity dispatch is limited to supplied rational tables with at most seven tokens/four experts. Experts and router are linear; the data are small and synthetic. These are established methods with attributed sources, not a new routing algorithm, production router, gradients through allocation, new training gain, robustness or causal guarantee, calibrated uncertainty, generalization result or measured GPU/serving speed.
