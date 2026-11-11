# MoeLab: the batch decides

Exact finite capacity dispatch for supplied mixture-of-experts gate tables retains the entire optimal assignment family, not just one greedy route. Every capacity-state edge, optimal count, Hall bottleneck and attainable scalar-update error extreme is independently replayed; original sparse training and routing-seam audits remain intact.

## The batch decides: capacity is not independent routing

[Exact capacity inspector](https://midya8.github.io/moelab/capacity.html) · [Proof, schema, sources and limits](https://github.com/midya8/moelab/blob/main/CAPACITY.md)

The objective is explicit: maximize dispatched tokens first, then the sum of their original gate probabilities. Each token can receive one eligible expert or skip its expert update; the token is not deleted. Capacities and eligibility are supplied, including empty eligibility and eligible zero gates. Four full-strength controls compare input-order/confidence-order top-choice/drop and best-available rerouting. Confidence-first best-available keeps `51/100` gate mass on one control versus global `49/50`; on another it exactly matches the optimum. Coverage first can retain less gate mass while dispatching more tokens. No equal-load or task-quality objective is smuggled into that ordering.

A Fraction dynamic program records all reachable capacity states and every feasible transition. Its root's optimal-edge DAG represents every optimal dispatch. Exact completion and marginal counts retain ties without distinguishing identical buffer slots. All token subsets expose capacitated Hall deficiencies; total spare capacity alone need not prevent skipped updates. An independent Cartesian-product verifier never imports the producer and reconstructs every report leaf, state, edge, family count and bottleneck. The independent browser BigInt engine matches the complete report, not a rounded summary.

Gate mass is not task quality. One two-token control has two routing optima with the same dispatched count and gate mass but scalar-update MSE **0 and 25**. Minimum and maximum MSE over the entire routing-optimal family have attained assignment witnesses. Targets are used only for this secondary audit; they never select the routing-optimal family. Outputs are original gate times supplied scalar expert value, without post-routing gate renormalization. This is neither an end-to-end residual-stream loss nor a model-quality result.

Fourteen controls include three bridges from the original frozen aux/no-aux/initialization models and the first six original training rows. Captured binary64 gate/output bytes carry provenance, reproduce numerically at `1e-12` across Python versions, and undergo explicitly labeled exact rational row normalization. All **53 Python/nine Node tests** pass, including 225 probability pairs, 1,024 eligibility/capacity cases, 125 full native/BigInt reports, tiny gates, permutations and every-leaf tampering. Actual Chrome checks 98 dispatch displays, 1,085 exact gate/support cells, all 813 capacity states, 42 layouts and two real JSON downloads with native verification. Both original and new isolated installed-wheel gates pass. At most seven tokens/four experts; no new algorithm, production router, gradients through allocation, new training gain, causal-masking guarantee or measured GPU speed. Original data, checkpoints, training, earlier route inspector and results are retained.

## Earlier sparse-training and routing-seam audit, preserved

A mixture-of-experts layer routes each input to one (or a few) specialized sub-models instead of running one dense network over everything. MoeLab implements the whole mechanism in dependency-free Python - router, experts, sparse training objective, load-balancing term - and treats routing behavior as something to measure, not assume.

## The fixture

Four input regimes on well-separated cluster centers, each with its own linear input-target map: the sign and scale of the relationship flips per regime. A single *linear* map cannot represent the data by construction; whether a nonlinear dense model catches up is an empirical question, which the measured baseline answers for this configuration. The baseline is a one-hidden-layer tanh MLP with slightly *more* parameters than the mixture (145 vs 136), trained with its own hand-derived backprop.

## Sparse training, gradients by hand

The trained prediction is Switch-style: `y = g_top(x) * expert_top(x)` - the router softmax scores every expert, the top expert answers, and its output is weighted by its own gate probability. The selected route is held fixed during differentiation. Gradients flow through the gate probability and chosen expert on that branch, away from routing boundaries:

```
dL/dw_e   = s * g_e * x              (s = 2(y - t))
dL/dz_k   = s * y_e * g_e * (delta_ek - g_k),   z = R x + c
aux       = E * sum_k g_k^2
d aux/dR_ej = 2 E x_j g_e (g_e - S2),   S2 = sum_k g_k^2
```

Every gradient is finite-difference verified in the test suite, task and aux terms separately.

## Measured results (checked-in fixture, pinned in tests)

| metric | MoE (136 params) | dense MLP (145 params) |
|---|---|---|
| test MSE | 0.0303 | 0.1853 |

- **Routing purity 1.0000**: each regime routes to exactly one expert across the whole test set.
- **Usage shares exactly [0.25, 0.25, 0.25, 0.25]**.
- **Soft evaluation costs 0.6291 vs 0.0303 sparse** - the objective is sparse, the observed comparison does not isolate the cause. The suite pins this inversion.

## The aux-loss finding nobody puts in the README

Load-balancing auxiliary losses exist to stop expert collapse. On this symmetric fixture, collapse never happens: max expert share is 0.25 with the aux term and 0.25 without, and dropping the term fits slightly *better* (0.0015 vs 0.0303). MoeLab reports that instead of selling the term - the fixture is the wrong place to justify it; the standard motivation, imbalanced expert traffic in production serving, is untested here because the fixture is symmetric by construction.

## Gates

```bash
python -m moelab gates --max-mse 0.06 --min-purity 0.95 --max-expert-share 0.26
```

The gates are deterministic regression checks on the mixture itself - fit, routing purity, usage shares - and the demo asserts an impossible purity bar fails. The baseline comparison is reported as measured numbers, not gated: if a stronger baseline ever closes the gap, the honest outcome is to update the numbers, not to fail the baseline.

## Scope

Experts and router are linear, the fixture is synthetic, and routing is top-1 with fixed-branch derivatives - real MoE layers route tokens inside transformers. The transferable mechanics are the measured ones here: sparse gating with gate-probability weighting, specialization as a measurable property, and load balance as a measured distribution. 39 Python tests and five substantive Node/actual-Chrome tests, with original nine tests preserved, fully offline inference, and seven-job CI across Python 3.10-3.13, demo, browser and installed wheel.

- Repo: [midya8/moelab](https://github.com/midya8/moelab)


## v0.2: follow the routing seam

[Interactive inspector](https://midya8.github.io/moelab/) · [Equations, input schema, sources and limits](https://github.com/midya8/moelab/blob/main/ROUTES.md)

An affine router gives an inspectable geometry: along x(lambda) = origin + lambda(destination - origin), each logit and expert output is an affine function. The new Python Fraction evaluator and independent browser BigInt evaluator enumerate all pair crossings, exact point ties and open cells, retaining crossings that do not change the upper-envelope winner. Choose any pair of the original 240 training examples, any of three original model states, or eight arithmetic controls. Every original train/test row remains visible in its original position, with no target-based filtering.

- Retained-probability output is g_e h_e, not a renormalized top-1 weight of one. Both neighboring limits and the exact point's chosen branch are shown. A route can change with zero jump; a triple-tie point can differ from both limits.
- Fixed-branch derivative is g_e [v_e + h_e(b_e - sum_j g_j b_j)]. It does not differentiate argmax or claim smoothness through a seam.
- Mathematical geometry uses exact rational extensions of finite binary64 inputs. Actual rounded path, dot products, softmax and probability-argmax inference are reported separately. A smallest-subnormal control proves their owners can disagree. Output values remain numerical approximations, not exact-real certificates.
- The original implementation's mean per-example E sum p², its old prose's E sum(mean p)² and Switch's E sum fP are different statistics. Uniform ties make all three equal one while all rows go to expert 0. All three are reported; original training is unchanged.

32 complete witnesses cover 8,176 evaluation and 2,080 path display positions. Native/browser comparisons require exact rational and discrete records and 1e-12 numeric tolerance. Additional checks include 80 independent integer geometries, 160 independent 70-digit Decimal prediction/derivative controls, branch finite differences, all 240 destination choices, all 340 row positions, strict JSON, exports, invalid-input non-revival and 320/390/1280 layouts. The installed wheel imports seven modules, runs all four commands outside the checkout, retrains aux/no-aux/dense models, compares full data/models/report at 1e-11 for runtime/libm portability, and reproduces all frozen witnesses. Freshly retrained rational fractions are kept distinct from the frozen model.

The older no-aux text said 0.0010; the original report regenerates to 0.0014970307791088836, which rounds to 0.0015. This corrects the prose, not the model. Original MSEs, purity, shares, dense model, trainer, data, tests and gate thresholds are retained. No token capacity, dropping, transformer, measured serving cost, robustness radius, causal mechanism or generalization result is claimed. The 65-point display curve does not discover boundaries and may miss sub-grid intervals; exact tables preserve them. Standard methods are attributed, not presented as a new algorithm.
