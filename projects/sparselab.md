# SparseLab

[Public repository](https://github.com/midya8/sparselab) · [Equations and limits](https://github.com/midya8/sparselab/blob/main/DESIGN.md) · [Full numerical report](https://github.com/midya8/sparselab/blob/main/examples/demo.json)

## The question

Sparse coefficients are easy to display as a feature ranking. But a sparse selected support may be a coordinate-descent tie choice rather than an identified property of the fitted prediction. SparseLab separates the supplied convex optimization problem, numerical optimality checks and coefficient ambiguity.

## The implementation

Dependency-free Python 3.10+ cyclic coordinate descent for `||y-X beta||^2/(2N) + lambda*||beta||_1`. Every supplied column is penalized. There is no hidden intercept, standardization, centering or ridge term. Partial residuals are recomputed, avoiding accumulated incremental-residual drift.

Every sweep reports primal loss/penalty, an interior scaled-residual feasible dual witness, all correlations, stable gap decomposition, direct primal-minus-dual difference, all KKT residuals and support. Both absolute gap and maximum KKT residual must reach tolerance; a sweep limit stays an explicit nonconvergence result. Descending regularization paths retain all fit histories and the actual warm starts.

A separate exact-rational active/sign enumerator tests all `3^p` patterns for up to five columns. It solves nonsingular active normal equations with rational elimination and checks every KKT condition exactly. It counts skipped singular patterns and returns valid nonsingular-support optima, not every point in a continuum. Fractions represent the validated binary64 inputs exactly.

![Orthogonal coefficient path, duplicate ambiguity and convergence controls](https://raw.githubusercontent.com/midya8/sparselab/main/assets/sparsity-audit.svg)

## What the developed controls show

| Control | Verified result | Limit of the claim |
|---|---|---|
| Four-row orthogonal design, six dyadic penalties | Coefficients match closed-form soft thresholds of `[2,-3/4,1/8]`; lambda_max=2 | Mathematical control, not held-out accuracy |
| Duplicate columns, lambda=1/4 | Forward `[7/4,0,-1/2]`, reverse `[0,7/4,-1/2]`, midpoint `[7/8,7/8,-1/2]`: objective `5/8`, identical predictions, zero KKT residual | Unique predictions do not identify coefficients or a causal selected feature |
| Correlated columns, lambda=1/8 | One sweep gap `0.330882353`, max KKT `0.176470588`; 18 sweeps reach objective `19/68` | Same objective/data/order/initialization; one run is explicitly truncated, not a competitive baseline |

The duplicate-column exact oracle finds both sparse witnesses. Convexity makes every mixture optimal, including the denser midpoint. No ridge term is added to hide the ambiguity. The correlated exact oracle independently agrees with `[0,33/17]` and objective `19/68`.

## Verification and reuse

28 tests: 25 behavior/CLI checks and three SVG checks. Independent scalar/orthogonal formulas, ten seeded exact-rational comparisons, full five-column enumeration, duplicate convex mixtures, weak duality, all primal/dual equations, monotone sweep histories, warm/cold agreement, explicit path failure propagation, sign/row/column symmetries, row replication, scale/penalty equivalence, zero columns, strict malformed JSON, nonmutation and RNG isolation.

All 18 coefficient plot points and polyline geometry, 23 table cells with their coordinates, full embedded compressed report metadata, hidden intermediate-history tampering and byte-exact SVG regeneration are tested. CI targets Python 3.10-3.13 and requires the five-module wheel to reproduce both complete CLI JSON outputs outside the source tree.

```bash
python -m sparselab demo
python -m sparselab path examples/input.json
python -m unittest discover -s tests -v
python examples/render_figure.py --check
```

## Boundaries and attribution

Small dense fits only: <=128 rows, <=12 columns; exact oracle <=32 rows, <=5 columns. Positive lambda, bounded finite inputs and a minimum nonzero-column norm. Output retains full history and can be larger than input. Floating-point dual/KKT checks are not outward-rounded mathematical certificates and do not give coefficient error bounds in rank-deficient problems. The exact oracle is exponential, not a large-scale solver.

Standard coordinate descent/soft thresholding and warm paths follow [Friedman, Hastie and Tibshirani](https://pmc.ncbi.nlm.nih.gov/articles/PMC2929880/); standard KKT and dual geometry are covered by [Ryan Tibshirani's coordinate descent notes](https://www.stat.cmu.edu/~ryantibs/convexopt/lectures/coord-desc.pdf). Original implementation and developed mathematical controls, no new algorithm claim. No external dataset, paid API, speed superiority, cross-validation, held-out prediction result, causal feature importance or statistical/post-selection inference. MIT license.
