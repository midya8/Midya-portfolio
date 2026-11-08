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

## Exact Gap Safe screening extension

[Derivation and six controls](https://github.com/midya8/sparselab/blob/main/SCREENING.md) · [Full exact screening report](https://github.com/midya8/sparselab/blob/main/examples/screen-demo.json)

The original float solver and controls remain unchanged. `screen(X,y,coefficients,penalty)` now audits an arbitrary supplied iterate using exact rational arithmetic over the stored binary64 inputs. It constructs an exactly feasible residual-scaled dual vector, exact primal-dual gap G and sphere radius squared `2G/N`. For feature j, a positive exact margin `lambda-|X_j^T u|` and strict inequality `||X_j||^2*R_squared < margin^2` prove coefficient j zero in every optimizer. No rounded square root, tolerance decision or coordinate dropping is used.

![Exact Gap Safe certificates and limits](https://raw.githubusercontent.com/midya8/sparselab/main/assets/safe-screening.svg)

| Control | Exact gap | Exact outcome |
|---|---:|---|
| Loose zero iterate, lambda=1/4 | 14357/8192 | No feature certified |
| Near iterate with current beta_2=1/32 | 5/1024 | Feature 2 certified zero in every optimum; ball term 5/512 < squared margin 25/1024, slack 15/1024 |
| Exact interior zero, lambda=1/4 | 0 | Feature 2 certified |
| Exact boundary zero, lambda=1/8 | 0 | Feature 2 is zero, but radius=margin=0 fails the strict test |
| Duplicate-column optimum | 0 | Neither interchangeable copy is screened; either can carry a nonzero optimum coefficient |
| Loose iterate with a zero column | 73/32 | Zero column certified despite its nonzero current coefficient |

A separate equality control has ball term=squared margin=1/4 and must remain uncertified. These cases distinguish a sufficient screening certificate from current sparsity or a complete support detector. `not_certified` never means active, useful or causally relevant. Fractions describe the exact stored binary64 values, not ideal decimal values or unknown pre-rounding data.

The extension adds 14 behavior checks and 3 SVG checks, for 45 tests total. Every rational equation and exact ball is reconstructed independently; 24 additional seeded designs compare certified zeros with independent active/sign-oracle witnesses and check exact dual-optimum containment. Strict equality, boundary zeros, duplicates, general 128-row/12-column size, permutations, signs, scaling, row replication/N normalization, nonmutation/RNG and strict JSON CLI errors are checked. The new SVG checks 27 exact cells/coordinates, two squared-bound bars, full lossless report metadata and hidden-dual tampering. The six-module v0.2 wheel reproduces all four complete CLI JSON outputs outside checkout; both SVGs regenerate byte-exactly.

```bash
python -m sparselab screen-demo
python -m sparselab screen examples/screen-input.json
python examples/render_screening.py --check
```

Standard Gap Safe rules are due to Fercoq, Gramfort and Salmon, [Mind the duality gap: safer rules for the Lasso](https://proceedings.mlr.press/v37/fercoq15.html). This extension implements a strict rational sphere audit with explicit mean-loss normalization, not a new screening theorem, causal selector, statistical guarantee, complete zero detector or solver speedup. It does not upgrade the retained floating solver's numerical witnesses to interval certificates.


## Exact affine regularization branch extension

[Exact branch derivation and API](https://github.com/midya8/sparselab/blob/main/BRANCHES.md) · [complete report](https://github.com/midya8/sparselab/blob/main/examples/branch-demo.json)

A feature can leave the nonzero support as regularization falls, then return with the opposite sign. This extension verifies that behavior with exact affine KKT branches, not a dense grid of approximate fits. The caller supplies one weak sign pattern. Rational Gram solves give beta(lambda), and the complete selected-sign/inactive-correlation inequalities give its maximal closed nonnegative-lambda interval. Reports keep every half-line and tie, all affine coefficients/correlations, and exact endpoint/interior dual vectors with primal=dual. The entire interval claim comes from affine inequalities, not endpoint sampling alone.

![Five exact branches and a feature drop/re-entry](https://raw.githubusercontent.com/midya8/sparselab/main/assets/regularization-branches.svg)

The developed centered four-row fixture has columns a and 2a+b, response 2a-b, Gram [[1,2],[2,5]] and cross [2,3]. Its five supplied branches cover [3,infinity),[4/3,3],[1,4/3],[1/3,1],[0,1/3]. Feature1 enters positive at 3, feature 0 enters at 4/3, feature 1 leaves at 1 and re-enters negative at 1/3. Adjacent knots agree exactly in coefficients, predictions, objectives and dual vectors; the zero-penalty endpoint is [4,-1]. The positive-definite Gram makes this fixture's coefficient path unique, not a general uniqueness claim.

Selected signs are weak: boundary zeros are allowed and are not a recovered support. An infeasible pattern returns a noncertificate with its conflicting bounds; a zero-lambda singleton is a valid point without a strict-sign interior. Selecting both duplicate columns instead returns singular_active_gram, not a fabricated ridge solution or proof of infeasibility. Selecting either duplicate separately yields different coefficients and identical predictions. These controls keep algebra failure, empty intervals and nonunique models distinct.

62 tests retain 45 previous checks and add 14 branch behavior checks plus 3 SVG checks. Twelve seeded five-row/three-feature designs exercise all 27 sign patterns, reconstruct accepted endpoint/interior equations and compare dyadic in-interval points with the per-lambda enumeration oracle. Analytic closed forms, exact all-bound ties and just-outside violations, continuity/drop/re-entry, singular/empty/singleton/zero/unbounded cases, transformations/N normalization, binary64 semantics,128x12 capacity, no mutation/RNG and strict CLI errors are covered. Figure checks cover 20 cells/coordinates, both entire path geometries/all 10vertices, five knots, full exact report metadata and hidden singular-Gram tampering. Seven-module wheel parity reproduces all 6 complete CLI outputs outside checkout; all 3 SVGs regenerate byte-exactly. All earlier solver/oracle/demos/screening reports remain unchanged.

```bash
python -m sparselab branch-demo
python -m sparselab branch examples/branch-input.json
python examples/render_branches.py --check
```

Standard piecewise-linear LASSO methods: Efron, Hastie, Johnstone and Tibshirani's [Least Angle Regression](https://export.arxiv.org/pdf/math/0406456v2.pdf) and Rosset/Zhu's [discussion section 2](https://export.arxiv.org/pdf/math/0406470v1.pdf). This is one supplied-branch verifier, not a general LARS implementation, full-path guarantee, new theorem, causal selector or speed benchmark. Exact certificates apply to stored binary64-input rationals, not unknown pre-rounding data. The branch API shares a linear-solve helper with the per-lambda oracle, so equation reconstruction and analytic fixtures provide separate checks; it is not an independent linear-algebra comparison.
