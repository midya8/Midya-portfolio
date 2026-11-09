# WarpLab: inspectable differentiable alignment

[Live inspector](https://midya8.github.io/warplab/) · [Source](https://github.com/midya8/warplab) · [Mathematical contract](https://github.com/midya8/warplab/blob/main/CONTRACT.md) · [Reviewed implementation](https://github.com/midya8/warplab/pull/1)

## The engineering question

Can a differentiable alignment be explained cell by cell, then independently checked without trusting its dynamic program?

WarpLab is a bounded instrument for established soft-DTW mathematics. Local squared costs induce a Gibbs distribution over monotone right/down/diagonal paths. Stable prefix/suffix log messages expose every cell occupancy and joint edge flow. Directional expectation messages compute cost Hessian-vector products without an autodiff package or a materialized Hessian.

## What is implemented

- Dependency-free scalar Python package and matching browser JavaScript.
- Expected alignment, expected cost and visited-cell count; path entropy and temperature derivative; coordinate gradients.
- Signed independent-cost Hessian-vector products. A separate covariance computation and finite differences check their sign, values and symmetry.
- Hard minimum, exact hard-tie count and lexicographically first minimum path. Python Fraction and JavaScript BigInt compare exact sums of binary64 local costs, avoiding tolerance-defined ties.
- Deterministic complete-path enumeration, clickable cost/occupancy/Hessian layers, incoming/outgoing edge inspector and accessible row/column selectors.
- Versioned JSON export, strict input validation, 4 MiB CLI cap, atomic output and an independent exhaustive verifier.

## Controls with interpretable answers

| Control | Expected behavior |
| --- | --- |
| Three zeros against themselves, temperature one | 13 equal-cost paths; raw score `-log(13)`, not zero |
| One-row grid | One legal path; entropy and cost Hessian are zero |
| Seven zeros against seven zeros | All 8,989 legal paths tie; score `-log(8989)` at temperature one |
| Same stretched sequences at 0.05 versus 8 | Different path distributions, not a measured accuracy improvement |
| Large costs, low temperature | Finite report despite tiny probabilities underflowing to zero |
| Signed cost perturbation | Occupancy changes according to negative path-incidence covariance |

## Reproduction evidence

The merged implementation passed 15 Python tests on each of Python 3.10, 3.11, 3.12 and 3.13, plus five Node/Chrome tests. Tests compare 168 complete Python/JavaScript reports and verify both through independent exhaustive paths. Direct path-indicator sums reconstruct every occupancy and edge flow. Finite differences check sequence, temperature and cost-direction derivatives. Conservation, soft-min bounds, transpose/scaling, forged reports, input errors and atomic output are covered.

The installed wheel runs both module and console commands outside the checkout for all eight controls. Chrome at 320, 390 and 1280 pixels checks 24 complete reports, 396 cell selections, 576 complete-path selections and 72 layer changes, including hard-path selection, row/column controls, download and stale/error clearing. All five deployed assets are byte-identical to verified main; all 24 deployed control screenshots match main pixel for pixel.

## Mathematical boundaries

Inputs are scalar synthetic sequences of length 1..7 with values -8..8, temperature 0.05..8 and signed cost directions -4..4. The largest grid has 8,989 paths. Larger requests fail rather than silently truncating. The dynamic messages are O(nm), while path enumeration is exponential and deliberately bounded.

Raw soft-DTW can be negative and is not a metric. Cell occupancies sum to expected path length, not one, and are not a normalized transport coupling. Edge values are joint traversal probabilities, not conditional transitions. The Hessian product is with respect to independent cost entries, not sequence coordinates. Binary64 rounding and probability underflow remain numerical limitations.

The self-corrected divergence is absent. The 2021 primary paper's nonnegativity theorem has ground-cost-specific assumptions; for plain squared Euclidean cost it proves stationarity at equality and describes nonnegativity as conjectural. WarpLab does not broaden that theorem from library/teaching summaries or claim a later resolution.

No learned model, dataset benchmark, speed claim, accuracy comparison or novel-algorithm claim. No private data or paid APIs. Unlike CTC, there is no blank/label emission model; unlike optimal transport, there are no coupling marginal constraints.

## Credit and primary sources

[Cuturi & Blondel, ICML 2017](https://proceedings.mlr.press/v70/cuturi17a.html) introduced soft-DTW and its differentiable alignment. [Blondel, Mensch & Vert, AISTATS 2021](https://proceedings.mlr.press/v130/blondel21a.html) develops expected-alignment derivatives, Hessian products and cost-dependent divergence results. WarpLab's scalar implementation, verifier, experiment interface and reproduction tests are original; the underlying mathematics is credited, not presented as new.
