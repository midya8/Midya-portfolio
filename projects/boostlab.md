# BoostLab: fitted is not selected

[Training-path inspector](https://midya8.github.io/boostlab/) | [Source](https://github.com/midya8/boostlab) | [Method](https://github.com/midya8/boostlab/blob/main/DESIGN.md) | [Path derivation and reproduction](https://github.com/midya8/boostlab/blob/main/PATH.md)

The stump model fits 80 trees, but validation keeps the zero-tree constant. Its last checkpoint has better test accuracy and worse test logloss. BoostLab keeps both results visible, along with every intermediate prefix. It is a dependency-free Python implementation of binary gradient boosting, with mean-residual leaves by default and optional capped, L2-regularized Newton leaves. It implements established methods, not new boosting theory.

## How fitting and selection differ

Only training rows and labels determine the half-count-smoothed intercept, residuals, splits and leaves. The model predicts a logit and applies a stable sigmoid. Bernoulli loss uses softplus minus `y*z`, not clipped-probability logloss. The residual `y-sigmoid(z)` is checked by central finite differences at both labels and multiple logits.

Each round fits a greedy residual-SSE tree and adds it at a fixed rate. Stable feature sorting and prefix sums test distinct-value boundaries, with `min_leaf` on both sides. The first exactly tied gain wins; improvement must exceed `1e-14`. A threshold is the lower observed value, including adjacent binary64 values. Constant targets return their identical float; constant features or too few rows produce a mean leaf. Local greedy choices do not optimize a global tree.

Validation chooses the earliest prefix improving logloss by more than `1e-12`, including round zero. Patience stops fitting after that many rounds without such an improvement. Changing validation labels can change the chosen prefix or stopping point, but not the shared fitted prefix. The API accepts no test data; the demo reports test metrics afterward. This separation does not make a caller's feature pipeline, split or tuning leakage-free. The selected model, last fitted model and complete loss history are returned separately.

## What Newton mode changes

Default leaves are mean residuals in `[-1,1]`. With `leaf_mode="newton"`, a leaf instead uses `sum(y-p)/(sum(p*(1-p))+L2)`, followed by an unshrunk-step cap. Probabilities come from the start of the round. The tree still uses residual-SSE splits, not Hessian-gain splits. There is no line search or exact likelihood optimization.

L2 must be finite in `[0,1000000]` (default 0); the cap is in `(0,10]` (default 3). Nondefault L2 or cap is rejected in mean mode. A zero denominator returns zero with a diagnostic count. Comparing the numerator with cap times denominator before dividing avoids infinite intermediates for subnormal Hessians. Cap hits are counted. Tests cover sigmoid Hessians by finite differences, leaf arithmetic, regularization, caps, zero denominators and subnormal denominators. A cap is a training choice, not a convergence guarantee.

## The original development fixture

Seed 7 generates 256/128/512 training/validation/test rows. Two coordinates are uniform in `[-2,2]`; the label is the sign of their product, independently flipped with probability 0.05. All three arms use 80 rounds, rate 0.5, `min_leaf=5` and patience 80. The original draft used patience 12; it was changed to 80 to expose the full checkpoint, not to select on test scores. The fixture was inspected during development and is not an untouched final benchmark.

| Arm and checkpoint | Trees / nodes | Test accuracy | Test logloss |
| --- | --- | --- | --- |
| Mean depth 1, selected constant | 0 / 0 | .4980 | .7060 |
| Mean depth 1, last fitted | 80 / 240 | .6367 | .7366 |
| Mean depth 2, selected and last | 80 / 556 | .8906 | .3400 |
| Newton depth 2, selected | 35 / 237 | .900390625 | .3341242425 |
| Newton depth 2, last fitted | 80 / 538 | .8984375 | .3468631810 |

Mean depth-2 training/validation losses are .2487/.3457. The Newton arm uses L2=1 and cap 3, with selected training/validation losses .1776606433/.3379099355. No leaf clips or has a zero denominator. This setting was not selected by a Newton grid search, but the development fixture had already been seen. Equal rounds do not mean equal node capacity. Newton changes regularization and capping as well as leaf arithmetic; this comparison does not isolate their causal effects, establish a general model ranking or supply a production-performance benchmark.

## Inspect every fitted prefix

The v0.2 page retains all 80 trees and 81 prefixes for each arm, including those validation rejects. An inspected prefix is separate from the original selection. The page shows selected and last-fitted logits for the same editable input, every included or omitted tree route, and complete exportable model/path JSON. Editing either coordinate clears the original historical fixture label. There is no fitting, selection, model API or upload on the page.

All 243 arm/prefix metric states retain training, validation and report-only test loss/accuracy. The loss chart uses a shared zero-based axis across arms and prefixes. These fixed-fixture metrics do not change when the input changes. The input's logit chart includes zero and uses its own sign-aware scale. Algebraic tree terms are neither feature importance nor causal attribution; sigmoid output is not calibrated confidence.

Fitting updates logits incrementally. The archive follows existing inference: `initial + rate*math.fsum(leaves)`. The browser uses compensated scalar summation. Independent checks agree within numerical tolerances, not bit-for-bit or as exact real arithmetic. Near-zero threshold labels can depend on rounding. The path display does not turn an inspected development fixture into external evaluation or supply confidence intervals.

## Reproduce and check

The current suite has 36 Python tests and five Node/actual-Chrome tests. All 29 original Python tests remain. Independent Fraction sums and a recursive scalar checker cover 4,860 original sample/prefix states, 1,458 edited states, 78 complete routes and all 243 metric states. Actual Chrome checks every original state, 180 UI configurations, physical keyboard input, invalid/stale witness refusal, clipboard failures and success, and real JSON Blob downloads. Tests cover 320/390/1280 layouts and expanded mobile routes/JSON.

A fresh installed wheel imports all seven modules, executes all five main commands and reproduces the three original 80-round fits, histories and witnesses outside checkout. The source's reproduction instructions run the same exporter API and installed checks. CI covers Python 3.10-3.13. These are bounded fixture and implementation checks, not a scalability or calibrated-coverage result.

## Model format and limits

Prediction still accepts `boostlab_v1` unchanged. Newton artifacts use `boostlab_v2` with leaf mode, L2 and cap; strict schemas check leaf values against that cap rather than `[-1,1]`. Both store ordered feature names, the initial logit, rate and recursive trees. Prediction validates schemas, finite scalars, feature indices, leaf ranges, depth and tree count. JSON round trips preserve tested predictions. Inputs become binary64, so large integer distinctions can disappear. NaN/Infinity and silent normalization are rejected.

Bounds: 1-16 features, 1-2000 rows per request/split, 1-200 rounds, depth 1-3, `min_leaf` 1-1000, patience 1-200 and rate `(0,1]`. There are no missing-value, categorical, weighted, stochastic, multiclass or histogram modes. No dynamic code, remote model download, networking or automatic deployment is part of prediction. This is not a compatible clone of gbm, sklearn or XGBoost.

## Credit

[Friedman, 2001](https://doi.org/10.1214/aos/1013203451) supplies the gradient-boosting reference. The [gbm guide](https://gbm-developers.github.io/gbm/articles/gbm.html) describes the Bernoulli Newton ratio used here with explicit L2 and a cap. Residual-SSE splits and a fixed rate remain simplifications, not the full source algorithms. The path notes credit their additional established references. Original educational code; attribution is not endorsement. No paid dependency, private data or telemetry.
