# InfluenceLab: local influence and deletion refits

[Source repository](https://github.com/midya8/influencelab) · [Model and solver](https://github.com/midya8/influencelab/blob/main/DESIGN.md) · [Full report](https://github.com/midya8/influencelab/blob/main/examples/demo.json)

![Influence and actual deletion audit](https://raw.githubusercontent.com/midya8/influencelab/main/assets/influence-audit.svg)

InfluenceLab fits a small regularized logistic model and compares local sample-weight derivatives with converged deletion refits. Its deletion paths refit at every grid node, so the numerical integral can be checked against the endpoint loss change. The seven-row development fixture shows where a frozen first-order prediction fails, including a sign reversal when all rows are deleted.
## What the derivative measures

A sample-weight derivative answers a local question at a fitted model. Deleting a whole row is a finite perturbation; renormalizing the remaining rows changes how ridge competes with data loss. Those distinctions should be visible, not lost behind one influence ranking.

InfluenceLab fits small fully regularized binary logistic models with Newton steps, unjittered Cholesky solves, Armijo backtracking and an explicit numerical convergence requirement. It reports the full Hessian, Cholesky factors, parameter directions, query-loss derivatives, adjoint agreement, solve residuals and all refit histories. There is no implicit intercept: a supplied constant column is regularized too.

## Development fixture results

Seven synthetic rows, query `(1,2)` with label 1, ridge 0.1 and original normalizer 7 give theta approximately `(-0.275488,0.220249)` and query loss `0.614042`. For row 5:

| Operation | Query-loss change |
|---|---:|
| Linear fixed-N deletion prediction | +0.203204 |
| Actual fixed-N numerical refit | +0.305655 |
| Actual retained-row mean, same ridge | +0.317231 |
| Damped inverse, delta 0.5, same base fit | +0.119499 |

The linear-minus-fixed-N-refit error is `-0.102451`. The full report keeps all seven rows, not just the highlighted example. All 15 base/deletion numerical fits have max absolute gradient at most `8.197e-11`, and undamped influence solves have max residual `5.551e-17`. Residuals measure numerical equations, not statistical uncertainty or deletion accuracy.

Fixed-N deletion equals retained-mean deletion with ridge multiplied by `N/(N-1)`. It does not equal retained-mean deletion with unchanged ridge. Adding 0.5 to the inverse Hessian is also not refitting a ridge-0.6 model: the original optimum and gradients stay fixed.

## Independent checks

The original 26 tests cover scalar fit against a separate monotone bisection optimizer; primitive and full-objective finite differences; every parameter weight derivative against perturbed converged refits on the fixture and three seeded systems up to six parameters; independent 2D inverse and adjoint solves; curvature sum-of-squares; strong-convexity error diagnostics; actual deletion and normalization equivalence; local quadratic remainder behavior; orthogonal-coordinate/permutation/label-complement checks; duplicate/zero features; explicit nonconvergence and safeguarded backtracking; strict JSON and stable extreme logits.

Three of those tests inspect every chart cell/position and the complete compressed JSON metadata, including hidden refit-Hessian tampering. The current five-module wheel reproduces all four demo/caller reports outside checkout. CI covers Python 3.10-3.13 and both reproducible SVGs.

## Finite-deletion path extension

![Refitted finite deletion paths](https://raw.githubusercontent.com/midya8/influencelab/main/assets/deletion-paths.svg)

`trace_deletion` continuously lowers selected weights from 1 to 0 while holding original N and ridge fixed. At each of 17 grid nodes it refits from zero, solves the current implicit parameter derivative and evaluates the query-loss derivative. Coarse Simpson/trapezoid levels reuse the fine-grid fits. [Derivation and input contract](https://github.com/midya8/influencelab/blob/main/PATHS.md) and [complete path reports](https://github.com/midya8/influencelab/blob/main/examples/path-demo.json) keep all 51 fits across the three groups, full Hessians/Cholesky/history, every derivative and every solve residual.

| Selected rows | First-order loss delta | Actual endpoint delta | Simpson 16 delta | Integral minus endpoint |
|---|---:|---:|---:|---:|
| 5 | +0.203204 | +0.305655 | +0.305655349 | +1.381e-7 |
| 5,6 | -0.149822 | -0.357507 | -0.357502140 | +4.825e-6 |
| All seven | -0.004253 | +0.079105 | +0.079849431 | +7.442e-4 |

The all-row endpoint has theta zero and query loss log(2), reversing the base prediction's sign. Its sharp derivative tail leaves a visible Simpson 16 gap around 0.000744. A small successive quadrature difference is not an error certificate, and monotone error reduction is not promised for arbitrary inputs. These are numerical refits and quadrature, not exact arithmetic.

Rows 5 and 6 have a joint endpoint change -0.357507, while their separate finite-deletion changes sum to -0.142898. At the base point, the group derivative *is* the sum of individual derivatives. Finite group nonadditivity is not a causal interaction claim.

14 new behavior tests check quadrature against independent polynomial integrals, interior parameter/query derivatives against perturbed refits, all-node equations and convergence, local sum identities, direct grouped endpoints, sign reversal/nonadditivity, grid fit reuse, symmetry and strict API/CLI. Three SVG tests check summary/convergence cells, all 51 polyline points, full metadata and hidden interior-Hessian tampering. All 43 tests pass; the five-module wheel reproduces all four complete JSON reports outside checkout and both SVGs regenerate byte-exactly. The original demo and figure are unchanged. This uses repeated retraining as a small reference, not a scalable deletion or unlearning method.

## Scope and attribution

This is an original small implementation of standard influence-function mathematics, not a new explanation algorithm. [Koh and Liang (2017), Section 2.1](https://proceedings.mlr.press/v70/koh17a.html) supplies the standard inverse-Hessian derivative; this API uses unit sample weights inside the original-N average, hence the explicit `1/N`. [Basu, Pope and Feizi](https://arxiv.org/abs/2006.14651) discusses deep-model fragility; this project stays in positive-ridge convex logistic regression and does not reproduce those experiments.

The fixture was developed during implementation. Finite deletion is a converged floating-point reference, not symbolic arithmetic. No causal attribution, bad-label detection guarantee, privacy deletion, machine-unlearning guarantee, neural-network scalability or confidence interval. No paid APIs, runtime dependencies or private datasets. MIT licensed.
