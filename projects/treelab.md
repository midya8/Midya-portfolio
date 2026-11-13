# TreeLab: inspectable trees and bounded ensemble search

TreeLab fits regression trees in NumPy, saves their pruning paths and keeps stronger same-fit controls in the report. Its browser pages let you inspect frozen one-feature responses, find the closest allowed input for a single tree, and examine the bounds of an unfinished ensemble search. The model counterfactuals describe the predictor, not how to improve wine.

[Response explorer](https://midya8.github.io/treelab/) · [Single-tree counterfactuals](https://midya8.github.io/treelab/counterfactual.html) · [Ensemble search inspector](https://midya8.github.io/treelab/forest.html)

## Whole-ensemble search with a visible objective gap

A search state carries one common feature box and a current node in each of the 32 frozen trees. Forced branches propagate through all members. Projection onto a box gives an exact-rational weighted-L1 lower bound; descendant output ranges prune impossible target bands. A best-first queue compares those bounds with verified full-ensemble witnesses.

A completed search can prove optimality or infeasibility under its constraints. `budget_exhausted` means the frontier remains, with or without a known witness. It proves neither. Seeds must meet the constraints and pass native full-ensemble inference. The saved demo includes known one-axis target witnesses so an unfinished search does not conceal an easy incumbent.

All 36 requests cross original CSV rows 1, 8 and 11, output bands [6,7]/[7,8], all-feature versus alcohol-only policies, and 0/128/4096 expansion budgets. At row 1, target [6,7], alcohol-only finishes with output 6.05953621031746 and cost 0.36290323. The all-feature search at 4096 expansions remains unfinished with objective bounds [0.01838427, 0.36290323]. Alcohol-only target [7,8] is infeasible; all-feature search retains an expensive corner witness and a large gap. No outcome is dropped.

The ensemble inspector shows every status, exact rational bounds, full input, all 32 member outputs/leaf IDs, budget comparisons and source hashes. Exact objective bounds apply to stored binary64 costs and the single-input NumPy ensemble prediction route. They do not make training arithmetic exact or establish causal actionability, plausible chemistry, uncertainty coverage or scalability.

[Search method, proof scope and sources](https://github.com/midya8/treelab/blob/main/FOREST_SEARCH.md)

## Closest allowed input for one tree

For the unchanged 19-leaf CART, enumerate every leaf whose output lies in the requested closed band. Intersect the path with closed feature bounds and immutable inputs, then clamp the source into each feasible binary64 box. With positive weighted L1 costs, the cheapest projected witness is globally optimal for this stored single tree under those constraints.

Strict right branches use `nextafter`, not an arbitrary epsilon. Exact rational costs prevent rounded false ties and underflow from changing the answer. Exact-cost ties break by leaf ID. Every feasible leaf candidate is retained and independently re-routed.

The fixed 36 requests combine rows 1, 8 and 11, bands [6,7]/[7,8]/[9,9], and four policies: all features, alcohol only, alcohol immutable, and all features immutable. Domains and reciprocal-range weights come only from fitting rows. For row 1, reaching [7,8] changes fixed acidity, volatile acidity and alcohol, with output 7.647058823529412 and cost about 0.27508758. Alcohol alone cannot reach that band; no leaf outputs 9. These are properties of the predictor, not winemaking instructions or an ensemble optimum.

[Counterfactual method, CLI and limits](https://github.com/midya8/treelab/blob/main/COUNTERFACTUALS.md)

## One-feature response partitions

![Full alcohol response slices and all-feature attainable outputs](https://github.com/midya8/treelab/raw/refs/heads/main/assets/sweep-audit.svg)

The first three historical test rows, CSV indices 1, 8 and 11, all eleven features and both frozen models give 66 slices and 1,028 leaf segments. Domains use fitting-only min/max. Rows 1 and 8 are exact copies and retain identical curves. There is no refit or new accuracy result.

At non-axis splits, follow the branch compatible with the fixed row. At axis splits, intersect the leaf interval. Combine all members' boundaries and average their outputs on each common segment. Return attainable extrema with complete input witnesses. Left routing is `<=`; upper endpoints are inclusive. The first lower endpoint is inclusive and later ones are exclusive. Open lower witnesses use `math.nextafter`, including adjacent representable boundaries.

The first row's alcohol response has three CART segments and 50 ensemble segments. Outputs range from 5.31579 to 6.36283 for CART and 5.09926 to 6.54844 for bagging. They are model outputs on this one-axis domain, not confidence limits, causal improvements or joint-feature robustness bounds. Correlated inputs can make synthetic combinations implausible.

An opposite-stump control checks why separate member extrema are insufficient: each tree can reach 10, but their common-input mean is always 5. The analysis uses common partitions rather than adding independent extrema.

The response explorer displays every interval, member output/leaf, min/max witness and full input. Keyboard arrows, Previous/Next and the interval list offer alternate controls. Copy denial has an explicit fallback. All three browser pages display complete stored reports, with local JSON downloads and source hashes. No accounts, analytics, remote inference or uploads.

[Response method and finite-domain semantics](https://github.com/midya8/treelab/blob/main/SWEEPS.md) · [Explorer mechanics](https://github.com/midya8/treelab/blob/main/EXPLORER.md)

## Group-bootstrap bagging and OOB support

![Fixed prefix selection, OOB coverage and same-fit controls](https://github.com/midya8/treelab/raw/refs/heads/main/assets/bagging-audit.svg)

For each tree, draw 2,376 fitting-feature groups 2,376 times with replacement, then expand each drawn group with multiplicity. Grown members use minimum leaf size 5, depth limit 20 and all feature columns. Seed 20261108 and prefixes [1,4,16,32] are fixed before the run. Validation MSE selects 32 trees, without validation refitting. Expanded row counts range from 2,856 to 2,951; leaf size counts multiplicity.

OOB excludes an entire exact-feature group. Zero votes mean null. Prefixes 1/4/16/32 have 1,832/482/1/0 unsupported rows. Each OOB MSE uses its own supported subset and a row-dependent number of trees. It is not a fixed-set error curve or calibrated uncertainty interval. A four-row duplicate witness shows why row absence alone fails to exclude an in-bag copy; it does not estimate dataset-wide leakage.

All group draws, complete trees, fitting/validation/test member predictions and OOB vote counts are saved. The ensemble is deterministic gzip JSON with zero timestamp; compression changes storage, not predictions.

[Bagging implementation and assumptions](https://github.com/midya8/treelab/blob/main/BAGGING.md)

## Data, split and pruning

![Real-data controls, the full pruning path and one complete prediction route](https://github.com/midya8/treelab/raw/e9a7aed4d140d15233324045089f58d8152bf943/assets/tree-audit.svg)

The unmodified UCI white-wine CSV contains 4,898 rows, eleven physicochemical features and an ordinal expert score. The original names file, SHA-256 and data attribution are bundled. Quality is not a price, safety or causal target. There is no official train/test split.

Serialize feature values as binary64 `float.hex()` strings, hash each vector, sort the 3,961 groups and assign the first floor(60%) to fitting, the next through floor(80%) to validation and the rest to test. This yields 2,921/1,008/969 rows. Exact copies stay together, including conflicting targets in a synthetic control. The split is target-blind and source-row-order invariant. Exact-feature groups do not recover producer, batch or time independence; near copies remain possible.

Greedy CART scores every adjacent distinct feature boundary. Weakest-link pruning saves all 290 states from 425 leaves to one root, including normalized fitting SSE, alpha and removed nodes. Exact floating ties cut together; ancestor cuts subsume descendants. Node statistics use `math.fsum`. An earlier dot-product prototype gave 307 states; the saved protocol gives 290 with the same selected predictions and metrics.

Validation MSE selects 19 leaves at alpha 0.00365165, with no refit. All 969 test predictions and six first-row routes are saved. Test scoring follows selection. Changing test targets leaves fitting, pruning, validation scores and the selected model unchanged.

## Results on the fixed split

| Model on the same 2,921 fitting rows | Test RMSE | Test MAE |
|---|---:|---:|
| Fitting mean | 0.88943 | 0.67329 |
| Fitting median | 0.90235 | 0.64499 |
| Grown CART, 425 leaves | 0.88255 | 0.66363 |
| Validation-selected CART, 19 leaves | 0.77595 | 0.60758 |
| Ordinary least squares, 12 coefficients | 0.73422 | 0.57379 |
| Validation-selected group bagging, 32 trees | 0.70521 | 0.54568 |

Least squares beats the single tree and remains visible. It uses fitting-only centering/scaling and an intercept, solved with NumPy's least-squares routine, without a tuned ridge parameter. The bagging result uses the already-seen historical test set. These comparisons are descriptive, not fresh blind evaluation, statistical significance or causal isolation. Squared error treats ordinal scores as numeric; coefficients and tree leaves are not equivalent complexity units.

## Independent checks and offline reproduction

The suite has 101 Python tests and five Node/real-Chrome tests. Forty all-threshold stump references recompute SSEs directly. An exact `Fraction` oracle enumerates every subtree of twelve small fitted trees. Other checks cover pruning ties, validation ties, strict JSON, complete refits, all saved predictions and test-target mutation.

Response and counterfactual tests use independent leaf-box intersections or Cartesian-grid references, strict binary64 boundaries, exact-cost false ties, subnormal costs, opposite-stump controls and native witness re-scoring. Every saved response segment and all 36 single-tree and 36 ensemble requests are checked. Browser tests cover member displays, statuses, copy success/denial, downloads, keyboard controls, 320/390/1280px layouts and 44px controls.

The installed wheel exercises nine modules and nineteen CLI modes outside the checkout, including real-data refits and complete saved-report comparisons. NumPy 2.2.6 is pinned. Runtime fitting and analysis need no network service.

[Source, setup and CLI commands](https://github.com/midya8/treelab) · [Pruning method and sources](https://github.com/midya8/treelab/blob/main/METHOD.md)

## Scope and attribution

Greedy CART is not globally optimal tree learning. Pruning searches subtrees of one grown tree. Alpha has score-squared-per-leaf units because risk divides SSE by the root fitting-row count. Finite reference tests and exact floating ties are not all-input numerical certificates. Out-of-range inputs get piecewise-constant predictions without an accuracy promise. Missing/categorical values, user sample weights and production monitoring are unsupported.

A route explains how a model computes its output. A nearby model counterfactual does not establish an effective intervention, a plausible wine, distribution support or a guarantee under refitting. Independent feature bounds do not preserve joint chemistry constraints.

Code is MIT. Data and derived results: Cortez, Cerdeira, Almeida, Matos and Reis (2009), UCI Wine Quality, DOI 10.24432/C56S3T, CC BY 4.0. CART, pruning, bagging and counterfactual search are established methods, not claimed inventions. No endorsement is implied.
