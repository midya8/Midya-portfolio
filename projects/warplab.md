# WarpLab: soft-DTW paths, lengths and inverse response

[Alignment inspector](https://midya8.github.io/warplab/) · [Length atlas](https://midya8.github.io/warplab/lengths.html) · [Inverse response](https://midya8.github.io/warplab/inverse.html) · [Source](https://github.com/midya8/warplab)

WarpLab makes a small soft-DTW calculation inspectable down to individual cells, edges and complete paths. Dependency-free scalar Python and browser JavaScript compute the same reports. Separate exhaustive oracles check them without calling the dynamic program or inverse solver. The mathematics is established; the work here is the implementation, experiment interface and independent checks.

## Choose the question

| Question | Calculation | Contract |
| --- | --- | --- |
| Which alignments carry probability, and how does the score change? | Gibbs cell occupancies, joint edge flows, sequence/temperature gradients and signed cost Hessian-vector products | [Alignment](https://github.com/midya8/warplab/blob/main/CONTRACT.md) |
| What changes when each visited cell pays a penalty? | Every legal length's conditional law, exact path counts and hard minima, then the penalized mixture | [Length atlas](https://github.com/midya8/warplab/blob/main/LENGTHS.md) |
| Can a penalty in [-4,4] attain a target expected length? | Finite endpoint reachability, bisection trace, sampled length laws and actual residual | [Inverse response](https://github.com/midya8/warplab/blob/main/INVERSE.md) |

Positive penalty favors shorter paths; negative penalty rewards longer paths. This changes the objective, not alignment quality. A width stop and a small mean residual are different outcomes. Neither is an interval-arithmetic certificate or proof of a unique parameter.

## Alignment, cell by cell

Stable prefix/suffix log messages recover every occupancy and joint edge probability. Directional expectation messages give cost Hessian-vector products without autodiff or a materialized Hessian. Path-incidence covariance and finite differences independently check their sign, values and symmetry.

The hard control reports the minimum, exact tie count and lexicographically first minimum path. Python Fraction and JavaScript BigInt compare exact sums of binary64 local costs, not tolerance-defined ties or ideal real-number input arithmetic. The browser provides cost/occupancy/Hessian layers, row/column selectors, edge inspection and a complete-path slider.

| Control | What to look for |
| --- | --- |
| Three zeros against themselves, temperature one | 13 equal-cost paths; raw score `-log(13)`, not zero |
| One-row grid | One legal path; entropy and cost Hessian are zero |
| Seven zeros against seven zeros | All 8,989 paths tie; score `-log(8989)` at temperature one |
| Same sequences at 0.05 and 8 | Different path distributions, not an accuracy comparison |
| Large costs, low temperature | Finite report even when tiny probabilities underflow to zero |
| Signed cost perturbation | Occupancy response follows negative path-incidence covariance |

## Separate length before mixing

Length-resolved log messages expose exact path counts, conditional occupancies and edges, hard minima/ties and conditional coordinate/temperature gradients. Length includes both endpoints. A per-visited-cell penalty changes the length mixture but leaves each conditional law unchanged.

The atlas reports the entropy chain rule, expected-length penalty gradient and negative length-variance curvature. Its independent oracle groups complete paths by length and checks the penalized law directly, without using the length-message generator.

## Invert the response without hiding failures

The inverse report accepts a target in [1,13] and first checks the response at penalties -4 and +4. Unreachable targets, single-length unidentifiability and numerical flattening stay distinct. Each bisection step retains the pre-update bracket, mean, centered variance, derivative and complete length law. The selected point is the evaluated point with smallest absolute residual, not necessarily the final midpoint.

Absolute mean tolerance and pre-update penalty-width tolerance are both 1e-9, with at most 40 midpoint evaluations. One control deliberately stops on width while missing mean tolerance. Unreachable targets retain a diagnostic response, not a solution. A separate complete-path oracle evaluates every witness penalty and checks the trace, status and selection without calling the solver or length dynamic program. Binary64 replay can disagree at adversarial branch boundaries; those reports fail verification.

## Reproduce and check

```sh
python -m pip install .
python -m unittest discover -s tests -v
npm test
bash tools/check_wheel.sh
```

Node 22+ and installed Chrome are required for the browser tests. The Python package has no runtime dependencies. The wheel check creates a fresh environment and runs module and console commands outside the checkout for eight alignment, eight length and nine inverse controls. CLI input is capped at 4 MiB; malformed, duplicate-key, nonfinite, unknown-field and out-of-bounds requests fail without replacing an existing output.

The current source passes 37 Python tests and 12 Node tests including actual Chrome. CI covers Python 3.10-3.13 and Node 22/Chrome. Cross-language checks compare 168 alignment reports, 98 length atlases and 36 inverse reports; both implementations are checked against independent exhaustive paths. Tests cover conservation, soft-min bounds, transpose/scaling, sequence/temperature/cost finite differences, Hessian symmetry, monotonicity, forged reports and generator-disabled verification.

Local and deployed Chrome checks at 320, 390 and 1280 pixels cover 396 cell selections, 576 complete-path selections and 72 layer changes for alignment; 81 length selections, 1,740 cell inspections and 72 penalty changes for the atlas; and 438 inverse witness selections. Row/column controls, export and stale/error clearing are checked. All 15 deployed assets match verified source bytes; all 75 unmasked control screenshots match locally rendered pages pixel for pixel. A separate trusted-download check retrieves all 25 control reports locally and live, matches each to browser runtime and independently verifies every report.

[Alignment implementation](https://github.com/midya8/warplab/pull/1) · [Length extension](https://github.com/midya8/warplab/pull/2) · [Inverse extension](https://github.com/midya8/warplab/pull/3) · [Calculation guide review](https://github.com/midya8/warplab/pull/4)

## Mathematical boundaries

Inputs are scalar synthetic sequences of length 1..7 with values -8..8, temperature 0.05..8 and signed cost directions -4..4. At most 8,989 paths are admitted. Larger requests fail rather than being truncated. Base dynamic messages are O(nm). With K=n+m-1, length-resolved messages take O(nmK), and conditional cell/edge convolutions take O(nmK²). The inverse solver currently uses that full atlas preprocessing, then O(K) work per response evaluation. Exhaustive enumeration is exponential and deliberately bounded.

Raw soft-DTW can be negative and is not a metric. Occupancy sums to expected path length, not one, and is not a normalized transport coupling. Edge probabilities are joint traversal probabilities, not conditional transitions. Hessian products use independent cost coordinates, not sequence coordinates. Binary64 rounding and probability underflow remain; numerical verification is not a formal proof.

The self-corrected divergence is absent. The 2021 primary paper proves nonnegativity under ground-cost-specific assumptions; for plain squared Euclidean cost it proves stationarity at equality and describes nonnegativity as conjectural. WarpLab does not broaden that theorem from teaching/library summaries or claim a later resolution.

This is not a learned model, dataset benchmark, speed claim, accuracy comparison or new alignment algorithm. Unlike CTC, there is no blank/label emission model; unlike optimal transport, there are no coupling marginal constraints. No private data or paid APIs are involved.

## Credit

[Cuturi & Blondel, ICML 2017](https://proceedings.mlr.press/v70/cuturi17a.html) introduced soft-DTW and differentiable alignment. [Blondel, Mensch & Vert, AISTATS 2021](https://proceedings.mlr.press/v130/blondel21a.html) develops expected-alignment derivatives, Hessian products and cost-dependent divergence results. WarpLab's scalar implementation, verifier, experiment interface and reproduction tests are original; the underlying mathematics is credited, not presented as new.
