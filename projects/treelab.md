# TreeLab: pruning makes a smaller model, not the strongest model

From-scratch CART regression and weakest-link pruning on real UCI white-wine data. Exact feature copies stay together across 2,921 fitting, 1,008 validation and 969 test rows. The complete 290-state pruning path goes from 425 leaves to the root; validation selects 19 leaves without test targets. The stronger same-fit least-squares control stays visible: test RMSE 0.73422 versus selected-tree 0.77595 and grown-tree 0.88255. 40 tests include 40 independent split references, exact Fraction subtree oracles for 12 small trees, test-target mutation, full refit and strict JSON. Five-module/five-CLI installed-wheel reproduction, every test prediction and a data-checked audit SVG. Established greedy CART, not globally optimal tree learning, causal importance, wine-safety advice or an all-input certificate.

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
effects. No missing/categorical data, sample weights, ensembles or production
service is implemented. Out-of-range predictions are piecewise constant, with
no accuracy promise.

Data and derived figure/metrics: Cortez et al. (2009), UCI Wine Quality,
DOI 10.24432/C56S3T, CC BY 4.0. Code is MIT. CART, weakest-link pruning and least
squares are established methods, not claimed inventions. No endorsement implied.
