# MoeLab: mixture-of-experts from scratch, routing measured

A mixture-of-experts layer routes each input to one (or a few) specialized sub-models instead of running one dense network over everything. MoeLab implements the whole mechanism in dependency-free Python - router, experts, sparse training objective, load-balancing term - and treats routing behavior as something to measure, not assume.

## The fixture

Four input regimes on well-separated cluster centers, each with its own linear input-target map: the sign and scale of the relationship flips per regime. A single *linear* map cannot represent the data by construction; whether a nonlinear dense model catches up is an empirical question, which the measured baseline answers for this configuration. The baseline is a one-hidden-layer tanh MLP with slightly *more* parameters than the mixture (145 vs 136), trained with its own hand-derived backprop.

## Sparse training, gradients by hand

The trained prediction is Switch-style: `y = g_top(x) * expert_top(x)` - the router softmax scores every expert, the top expert answers, and its output is weighted by its own gate probability. The argmax choice is straight-through; gradients flow through the gate probability and the chosen expert:

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
- **Soft evaluation costs 0.6291 vs 0.0303 sparse** - the objective is sparse, so averaging specialized experts actively hurts. The suite pins this inversion.

## The aux-loss finding nobody puts in the README

Load-balancing auxiliary losses exist to stop expert collapse. On this symmetric fixture, collapse never happens: max expert share is 0.25 with the aux term and 0.25 without, and dropping the term fits slightly *better* (0.0010 vs 0.0303). MoeLab reports that instead of selling the term - the fixture is the wrong place to justify it; the standard motivation, imbalanced expert traffic in production serving, is untested here because the fixture is symmetric by construction.

## Gates

```bash
python -m moelab gates --max-mse 0.06 --min-purity 0.95 --max-expert-share 0.26
```

The gates are deterministic regression checks on the mixture itself - fit, routing purity, usage shares - and the demo asserts an impossible purity bar fails. The baseline comparison is reported as measured numbers, not gated: if a stronger baseline ever closes the gap, the honest outcome is to update the numbers, not to fail the baseline.

## Scope

Experts and router are linear, the fixture is synthetic, and routing is top-1 with straight-through gradients - real MoE layers route tokens inside transformers. The transferable mechanics are the measured ones here: sparse gating with gate-probability weighting, specialization as a measurable property, and load balance as a measured distribution. 9 unit tests, fully offline, CI across Python 3.10-3.13.

- Repo: [midya8/moelab](https://github.com/midya8/moelab)
