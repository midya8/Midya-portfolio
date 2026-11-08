# InfluenceLab: differentiate a weight, then actually delete the row

[Source repository](https://github.com/midya8/influencelab) · [Model and solver](https://github.com/midya8/influencelab/blob/main/DESIGN.md) · [Full report](https://github.com/midya8/influencelab/blob/main/examples/demo.json)

![Influence and actual deletion audit](https://raw.githubusercontent.com/midya8/influencelab/main/assets/influence-audit.svg)

Convex logistic influence functions with safeguarded Newton fits, full Hessian/Cholesky and convergence witnesses, and independently checked sample-weight derivatives. Actual finite-deletion refits show query-loss change +0.305655 versus the local prediction +0.203204 on one developed row. Separate retained-mean normalization and damped-inverse controls expose changed objectives and approximation limits. Strict JSON CLI, installed-wheel parity, a reproducible SVG and 26 tests. Small supplied-model sensitivity, not causal attribution, a deep-model benchmark or an unlearning guarantee.

## Why this exists

A sample-weight derivative answers a local question at a fitted model. Deleting a whole row is a finite perturbation; renormalizing the remaining rows changes how ridge competes with data loss. Those distinctions should be visible, not lost behind one influence ranking.

InfluenceLab fits small fully regularized binary logistic models with Newton steps, unjittered Cholesky solves, Armijo backtracking and an explicit numerical convergence requirement. It reports the full Hessian, Cholesky factors, parameter directions, query-loss derivatives, adjoint agreement, solve residuals and all refit histories. There is no implicit intercept: a supplied constant column is regularized too.

## Measured fixture, not a benchmark

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

26 tests cover scalar fit against a separate monotone bisection optimizer; primitive and full-objective finite differences; every parameter weight derivative against perturbed converged refits on the fixture and three seeded systems up to six parameters; independent 2D inverse and adjoint solves; curvature sum-of-squares; strong-convexity error diagnostics; actual deletion and normalization equivalence; local quadratic remainder behavior; orthogonal-coordinate/permutation/label-complement checks; duplicate/zero features; explicit nonconvergence and safeguarded backtracking; strict JSON and stable extreme logits.

Three of those tests inspect every chart cell/position and the complete compressed JSON metadata, including hidden refit-Hessian tampering. The four-module wheel reproduces both demo and caller JSON outside checkout. CI covers Python 3.10-3.13 and the reproducible SVG.

## Limits and credit

This is an original small implementation of standard influence-function mathematics, not a new explanation algorithm. [Koh and Liang (2017), Section 2.1](https://proceedings.mlr.press/v70/koh17a.html) supplies the standard inverse-Hessian derivative; this API uses unit sample weights inside the original-N average, hence the explicit `1/N`. [Basu, Pope and Feizi](https://arxiv.org/abs/2006.14651) discusses deep-model fragility; this project stays in positive-ridge convex logistic regression and does not reproduce those experiments.

The fixture was developed during implementation. Finite deletion is a converged floating-point reference, not symbolic arithmetic. No causal attribution, bad-label detection guarantee, privacy deletion, machine-unlearning guarantee, neural-network scalability or confidence interval. No paid APIs, runtime dependencies or private datasets. MIT licensed.
