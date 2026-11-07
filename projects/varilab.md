# VariLab: optimizing the bound is not recovering every marginal

[Source repository](https://github.com/midya8/varilab)

Mean-field variational inference is an optimization problem, but a better objective does not mean every requested statistic is better. VariLab makes that distinction inspectable for tiny supplied Ising distributions where every target state can be enumerated.

## The result that stays uncomfortable

Two spins have zero fields and coupling `J=3`. The target favors aligned states, almost equally split between `(-1,-1)` and `(1,1)`. Exact means are zero; exact cross-covariance is `tanh(3)=0.995055`. Three product-distribution runs change only the initial means, using the same ascending sequential coordinate order, 100-sweep cap and `1e-12` sweep-change tolerance.

| Start | Final spin means | ELBO | Reverse KL | Maximum mean error | Stop rule |
|---|---|---:|---:|---:|---|
| Zero | `(0,0)` | 1.386294 | 2.309329 | 0.000000 | Met, 1 sweep |
| Positive `.1` | `(.994902,.994902)` | 3.005027 | 0.690596 | 0.994902 | Met, 7 sweeps |
| Negative `-.1` | `(-.994902,-.994902)` | 3.005027 | 0.690596 | 0.994902 | Met, 7 sweeps |

The higher-ELBO runs have lower reverse KL but worse marginal means. All product approximations miss the target's nonzero cross-covariance. The symmetric run stops with zero coordinate residual and gradient, yet it is not an ELBO maximum: a small joint positive perturbation raises the objective. A stopping rule alone does not certify local/global optimality or useful marginals.

The separate no-edge control is exactly representable by the product family: means match `tanh(fields)` to floating precision. Its `max_mean_error <= 1e-6` gate passes; the positive-start coupled gate fails. Both directions are asserted and displayed. The targets, coupling and starts were directly specified without seed, parameter or checkpoint search. This is a constructed counterexample, not an empirical method ranking.

## A curvature certificate, not an optimizer claim

The new `curvature(model, means)` API and strict CLI return the analytic ELBO Hessian at supplied interior means using exact fractions of the compiled binary-float inputs. Symmetric congruence returns `T`, block-diagonal `D`, exact positive/negative/zero eigenvalue counts and signed rational directions with quadratic forms; the independently checked identity is `T^T H T = D`. A nonzero diagonal uses a scalar pivot, an all-zero diagonal with an off-diagonal entry uses a 2x2 pivot, and a zero remainder records nullity. No numerical eigenvalue threshold is used.

At `J=3,m=0`, inertia is `(1,1,0)` and direction `(3,1)` has exact positive form `8`, so the coordinate fixed point is a saddle. At the existing broken-symmetry fitted point, inertia is `(0,2,0)`. At `J=1,m=0`, it is `(0,1,1)`; the immediately adjacent representable couplings below and above 1 have `(0,2,0)` and `(1,1,0)`. The fixture uses those direct neighbors, not a search. The figure embeds complete rational certificates and plots all counts on one scale. Inertia preserves signs, not eigenvalue magnitudes.

The returned gradient is floating point; negative-definite curvature does not establish exact stationarity or a maximum. Singular points receive no higher-order verdict. This is curvature at represented inputs, not an interval enclosure or uncertainty calibration. It uses cubic rational-operation work and quadratic storage for at most 12 spins, with variable integer bit costs and no runtime guarantee. The finite-state reference remains floating point and is not silently rebranded as rational arithmetic.

```sh
python -m varilab curvature-demo
python -m varilab curvature examples/coupled.json --means '[0,0]'
PYTHONPATH=. python examples/render_curvature.py --check
```

## What is implemented

- Full finite support in log space, with probabilities/log probabilities, log partition, means, second moments and covariance.
- Product-Bernoulli ELBO, entropy, expected log potential and analytic interior gradients.
- Sequential coordinate updates `m_i=tanh(h_i+sum_j J_ij*m_j)`, with explicit coordinate order, every update snapshot, recomputed objective, sweep-change stopping status and final coordinate residual.
- Independently summed `KL(q || p)` from complete product state probabilities, compared with `log_partition - ELBO`.
- Strict versioned JSON model/API/CLI, bounded work, an offline demo and a reproducible SVG containing the complete model, state probabilities, settings and histories.

This is inference for supplied target distributions, not fitting parameters or learning a posterior from data. The product family cannot represent arbitrary dependence, even if the optimizer improves its own objective. Synchronous/Jacobi updates are not implemented or treated as equivalent.

## Why the checks matter

58 tests include analytic independent/two-spin references, direct exponentials on 216 three-spin models, every pair moment, product-state ELBO and KL reconstructions, finite differences for every gradient coordinate, exhaustive one-coordinate objective scans and every-update ascent checks. They also cover full history reconstruction/copy isolation, symmetry and coordinate-label/order equivalence, the nonmaximum stopping example, lost covariance, saturated point masses, retained finite logs for underflowed target probabilities, strict validation and actual/reference work boundaries. 20 added curvature tests cover a 729-matrix independent inertia oracle, exact reconstruction and signed witnesses, finite-difference Hessians, permutations, singular/zero/2x2 pivots, near-endpoint and full-size models, validation and CLI equality. Four added figure tests verify all 15 inertia bars and complete certificates. Six original CLI tests and four original figure tests cover outputs/errors and every displayed bar/value.

A standalone wheel contains all four runtime modules and produces the same demo outside the source directory. The runtime and tests use only Python's standard library. No API, GPU, network, external data or model download is needed.

```sh
python -m varilab demo
python -m varilab exact examples/coupled.json
python -m varilab compare examples/coupled.json --initial '[0.1,0.1]'
python -m unittest discover -s tests -v
PYTHONPATH=. python examples/render_audit.py --check
```

## The boundary of the claim

"Exact" means every finite state is enumerated using floating-point log-sum-exp, not exact rational/outward-rounded arithmetic. Target probability underflow retains finite logs; product zero masses have null log probability. Tiny rounding errors in normalization, KL or covariance remain possible. `tanh` can saturate at endpoints.

Models have 1..12 spins, finite fields/weights with magnitude at most 100 and strictly indexed nonduplicate edges. JSON files are capped at 256 KiB. Reference work `2**n*(n+edges+n*n)` is capped at 786,432; requested fitting work `sweeps*n*(n+edges)` is capped at 500,000, with at most 1,000 sweeps. Errors do not return partial results. These counts are operational limits, not timing promises.

There is no arbitrary-dimensional exact inference, observation conditioning, parameter learning, richer variational family, stochastic optimizer, convergence proof or calibrated uncertainty claim. Standard ELBO/KL and coordinate-ascent principles follow [Blei, Kucukelbir and McAuliffe (2017), sections 2.2-2.4](https://www.cs.columbia.edu/~blei/papers/BleiKucukelbirMcAuliffe2017.pdf). The Ising reduction, code, supplied synthetic examples, independent test references and figures are original implementations. [Derivation and accounting](https://github.com/midya8/varilab/blob/main/DESIGN.md).

The congruence/inertia principle follows [Nick Higham (2022)](https://nhigham.com/2022/12/06/what-is-the-inertia-of-a-matrix/); implementation, exact certificates and boundary fixtures are independent.
