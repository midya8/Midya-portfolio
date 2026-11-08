# TreeLab: inspectable learners and constrained counterfactual geometry

A [live constrained counterfactual explorer](https://midya8.github.io/treelab/counterfactual.html) exposes multi-feature closest-leaf search for a frozen CART, alongside the [live one-axis response explorer](https://midya8.github.io/treelab/). Positive weighted L1, immutable inputs and fitting-only bounds give a closest feasible binary64 witness, every target-leaf candidate and exact rational costs. Strict thresholds use representable successors; infeasible requests remain visible across all 36 fixed cases. 87 Python tests and four Node/real-Chrome tests include an independent exhaustive grid oracle, false rounded ties, subnormal costs, full witness checks and responsive browser controls. Eight-module/sixteen-CLI installed-wheel checks retain all original data, models, historical controls and three audits. Established model counterfactual geometry, not causal recourse, plausible chemistry, ensemble optimality or new accuracy.

## v0.5: constrained multi-feature model counterfactuals

Find the closest input reaching a closed output band in the unchanged selected
CART, subject to closed feature bounds, immutable indices and positive weighted
L1 costs. Enumerate every target-output leaf, intersect its path with constraints
and clamp the source into each feasible binary64 box. Strict right branches use
nextafter, never an arbitrary epsilon. Exact rational costs prevent false rounded
ties and underflow; exact ties break by leaf ID. Every candidate is re-routed.

The fixed demo retains 36 requests: original test rows 1, 8, 11; target bands
[6,7], [7,8], [9,9]; all features, alcohol only, fixed alcohol, all fixed.
Fitting-only min/max and reciprocal-range weights. No new fitting or scoring.
For row 1, reaching [7,8] changes fixed acidity, volatile acidity and alcohol,
with output 7.647058823529412 and cost about 0.27508758. Alcohol alone cannot
reach that band under the same bounds. [9,9] has no target-output leaf.
These are facts about one predictor, not instructions for improving wine.

The [live browser page](https://midya8.github.io/treelab/counterfactual.html) displays every frozen request,
feature delta, feasible candidate, full input/box/path and exact cost; copy and
local download include the complete request. Report and model SHA-256 provenance.
87 Python tests and four Node/real-Chrome tests, eight modules and sixteen CLI
modes. Independent Cartesian-grid optimum checks, exact/false ties, subnormal
costs, immutable/directional bounds, all real witnesses and mobile controls.

[Counterfactual method, CLI, proof scope and attribution](https://github.com/midya8/treelab/blob/main/COUNTERFACTUALS.md)

This is a global weighted-L1 optimum over finite binary64 inputs for one stored
CART under independent box constraints. It is not causal recourse, plausible
chemistry, a feasible path, a bagging-ensemble optimum, calibrated uncertainty
or a guarantee for outcomes in reality. All previous models/reports/figures
remain unchanged; the one-axis explorer remains available below.

## v0.4: a live, frozen response explorer

[Open the live explorer](https://midya8.github.io/treelab/). The page bundles the
complete source report and its SHA-256, without recomputing or rounding its
intervals, witnesses or member outputs. No API calls, accounts, analytics,
remote inference or uploads. It starts with row 1 / 32-tree ensemble / alcohol.

Choose row, model and feature; inspect the full responsive step curve, exact
interval inclusion, every member output/leaf ID and attainable min/max with
complete input witnesses. The slider supports keyboard arrows; Previous/Next
and a full interval list offer alternatives. Copy and local JSON download
retain source row, model, feature, domain and interpretation warning. Denied
clipboard access produces an explicit fallback rather than a false success.

72 Python tests and three Node/real-Chrome tests include every one of the
66 UI slice selections and 1,028 segment witnesses/member displays, extrema,
keyboard movement, copy success/denial, download names and expanded disclosures
at 320/390/1280px. Chart labels reflow for phones instead of shrinking desktop
text. The live site passes the same real-Chrome checks and byte-for-byte
comparison of all five code/data/style files. CI also keeps Python 3.10-3.13
and installed-wheel seven-module/thirteen-CLI reproduction.

All prior data/models/reports and three audit figures are unchanged. This is
an interactive view of stored model-response geometry, not new inference,
a new accuracy result, causality, calibrated uncertainty, realistic-wine
guarantees or joint-feature robustness.

[Explorer mechanics and verification](https://github.com/midya8/treelab/blob/main/EXPLORER.md)

## v0.3: exact one-feature response partitions

![Full alcohol response slices and all-feature attainable outputs](https://github.com/midya8/treelab/raw/refs/heads/main/assets/sweep-audit.svg)

The first three historical test rows, original CSV indices 1, 8 and 11, all
eleven features and both frozen models give 66 slices and 1,028 leaf segments.
Domains use fitting-only min/max. No fitting or new held-out accuracy claim.
Rows 1 and 8 are exact copies and retain identical curves, rather than being
filtered for a more varied-looking demonstration.

At non-axis splits, follow only the branch compatible with the fixed row. At
axis splits, intersect the leaf's interval. Combine all members' boundaries,
average outputs on each common segment, and return attainable extrema with
complete input witnesses. Left routing is <=; upper endpoints are inclusive.
The first lower endpoint is inclusive, later ones are exclusive. Open lower
witnesses use math.nextafter, never an arbitrary epsilon. Singleton thresholds
and adjacent representable values remain correct.

For the first test row, the complete alcohol slice has 3 selected-CART leaf
segments and 50 ensemble segments. Model outputs range from 5.31579 to 6.36283
for CART and 5.09926 to 6.54844 for bagging. These are model responses on a
one-axis domain, not uncertainty intervals, causal improvements, possible-wine
guarantees or multifeature robustness bounds. Correlated inputs may make
synthetic feature combinations implausible.

An opposite-stump control shows why member extrema are insufficient: each
member can separately reach 10, but their mean is always 5. The implementation
uses common-axis leaf intersections, not the sum of separate extrema.

70 tests include direct checks of all real-data segment boundaries, member
leaf IDs and predictions, independent multidimensional leaf-box intersections,
random small trees/ensembles, zero-width domains, repeated axes, nextafter
boundaries, strict JSON/CLI and a no-refit complete report rerun. The installed
wheel exercises seven modules and all thirteen CLI modes. The audit SVG retains
its complete displayed curves/table data and regeneration checks.

[Response method, finite-domain semantics and sources](https://github.com/midya8/treelab/blob/main/SWEEPS.md)

## v0.2: group-bootstrap bagging

![Fixed prefix selection, OOB coverage and preserved same-fit controls](https://github.com/midya8/treelab/raw/refs/heads/main/assets/bagging-audit.svg)

Draw 2,376 fitting-feature groups 2,376 times with replacement for each tree,
then expand every drawn group with multiplicity. Grown members keep minimum
leaf size 5 and depth limit 20, with all feature columns available. Seed
20261108 and the prefix grid [1,4,16,32] are fixed before the run. Validation MSE
alone selects 32 trees, with no validation refit. Bootstrap expanded row counts
vary from 2,856 to 2,951. Leaf size counts multiplicity, not unique source rows.

OOB excludes a row's entire exact-feature group. Zero votes mean null. Prefixes
1/4/16/32 have 1,832/482/1/0 unsupported rows. Each prefix's OOB MSE is on its
own supported subset with a row-dependent number of trees; it is not a
fixed-set error curve or calibrated uncertainty interval. A four-row duplicate
witness demonstrates why row absence alone does not exclude an in-bag copy.
This witness does not estimate real-data leakage magnitude.

The 32-tree ensemble has test RMSE 0.705212 and MAE 0.545678 across 969 rows,
versus same-fit least squares 0.734217/0.573791 and selected CART
0.775952/0.607582. These are descriptive results on the reused historical test,
not a fresh blind benchmark, statistical significance or causal isolation.
Exact feature groups do not recover producer/batch identity.

The complete ensemble JSON, all group draws and fitting/validation/test member
outputs, per-row OOB votes and test predictions are saved. 57 tests and a
six-module/ten-CLI installed-wheel check cover full reproduction, independent
traversal, group multiplicity, missing support, corruption guards and test-target
mutation. The original v0.1 data/models/report and audit figure are unchanged.

[Bagging implementation, assumptions and sources](https://github.com/midya8/treelab/blob/main/BAGGING.md)

## Original v0.1 pruning audit, preserved

![Real-data controls, the full pruning path and one complete prediction route](https://github.com/midya8/treelab/raw/e9a7aed4d140d15233324045089f58d8152bf943/assets/tree-audit.svg)

## Protocol fixed before held-out evaluation

The original UCI white-wine CSV is bundled without modification with its
SHA-256, original names file and CC BY 4.0 attribution. The 4,898 rows contain
11 physicochemical features and an ordinal expert score. They are not a price,
safety or causal target. There is no official train/test split.

Serialize parsed feature values as binary64 float.hex strings, hash each vector,
sort the 3,961 unique groups and assign the first floor(60%) groups to fitting,
the next through floor(80%) to validation and the rest to test. This is target-
blind, source-row-order invariant and exact-feature-group disjoint. Target
conflicts would remain together, as a synthetic conflict control verifies.
Near copies, unrecorded production batches and time-forward shift remain open.

Fit CART with minimum leaf size 5 and maximum depth 20. Greedy squared-error
splits use every adjacent distinct feature boundary; left branches use <=.
Weakest-link pruning saves every state's normalized fitting SSE, alpha, leaf
count and removed node IDs. Exact floating ties cut together, with ancestor
cuts subsuming their descendants. Node statistics use math.fsum for reduction
portability. The earlier dot-product prototype gave 307 states; final stable
statistics give 290 with the same selected predictions and test metrics.

Validation MSE alone selects 19 leaves at alpha 0.00365165. There is no refit.
All 969 test predictions, the complete grown/selected model JSON and six first-
test-row prediction routes are saved. The test is evaluated only after fitting,
pruning and validation selection. Changing all test targets leaves the fitting,
pruning path, validation scores, selected index and selected model unchanged.

## Keep the stronger control

| Model on the same 2,921 fitting rows | Test RMSE / score units | Test MAE / score units |
|---|---:|---:|
| Fitting mean | 0.88943 | 0.67329 |
| Fitting median | 0.90235 | 0.64499 |
| Grown CART, 425 leaves | 0.88255 | 0.66363 |
| Validation-selected CART, 19 leaves | 0.77595 | 0.60758 |
| Ordinary least squares, 12 coefficients | **0.73422** | **0.57379** |

The linear control uses fitting-only centering/scaling and an intercept, solved
with NumPy's least-squares routine. No tuned ridge parameter. Squared error
treats the ordinal scores as numeric. Complexity units differ, and this single
historical split does not establish significance, future accuracy, a causal
benefit of pruning or superiority over other model families.

## Independent checks, not self-agreement alone

Forty all-threshold stump references recompute candidate SSEs directly. Every
subtree of 12 small depth-three fitted trees is enumerated with exact Fraction
risks from training rows. Production path and explicit-alpha prune objectives
are checked at breakpoints, interval interiors, zero and a large alpha. Separate
controls cover simultaneous weakest links, boundary inclusivity, adjacent
binary64 threshold fallback, validation-score ties and target-scale alpha units.

Full refit and report reproduction, all saved test predictions, group overlap,
test-target mutation, linear normal equations, strict JSON corruption and
complete SVG metadata/series/metrics are checked. The wheel is installed outside
the checkout and exercises all five modules and all five CLI modes: demo, audit,
fit, prune and predict. Prediction returns the complete branching route.

## What this does not claim

Greedy CART is not globally optimal tree learning. Weakest-link pruning searches
subtrees of one grown tree, not every possible partition. Alpha is score-squared
per leaf because SSE is divided by the root fitting count. Binary64 arithmetic,
finite oracles and exact floating tie rules are not exact all-input certificates.
A route explains this model's computation, not feature causality or deletion
effects. The original single-tree v0.1 has no missing/categorical data, sample weights, ensembles or production
service is implemented. Out-of-range predictions are piecewise constant, with
no accuracy promise.

Data and derived figure/metrics: Cortez et al. (2009), UCI Wine Quality,
DOI 10.24432/C56S3T, CC BY 4.0. Code is MIT. CART, weakest-link pruning and least
squares are established methods, not claimed inventions. No endorsement implied.

The complete frozen ensemble is bundled as deterministic `bagging-model.json.gz`
(gzip of the full JSON, zero timestamp). CLI model loading accepts `.json.gz`
as well as plain JSON. This changes storage only, not trees, draws or predictions.
