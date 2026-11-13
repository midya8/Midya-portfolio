# SubmodLab: greedy selection and cardinality rounding

[Source](https://github.com/midya8/submodlab) · [Live inspector](https://midya8.github.io/submodlab/) · [Method and sources](https://github.com/midya8/submodlab/blob/main/METHOD.md)

## Subset-selection checks

Subset selection is often described as picking the most useful or diverse data. Those descriptions can hide the objective, overlap, theorem assumptions and the gap between a greedy solution and an exact optimum. SubmodLab compares greedy selection with exhaustive optima on small supplied objectives. The supplied similarities are inputs, not learned meanings.

## Discrete inspector

- Nonnegative rectangular facility-location matrices and weighted-coverage special cases.
- Complete finite set-function tables, including deliberately invalid assumptions.
- Every subset value and optimum tie under an at-most-k cardinality limit.
- Updated greedy with complete candidates and deterministic lowest-index ties, versus singleton top-k ranking.
- Every monotonicity edge and local diminishing-return inequality, with complete violation lists.
- Exact finite-k approximation factor and proof-derived prefix upper-bound certificates only when all assumptions pass.
- Independent BigInt browser engine, editable inputs, signed subset chart and complete JSON export.

## Controls

The default six-row coverage control has three selectable items and k=2. Greedy uniquely starts with item 0 covering four rows, then adds one row: value 5. Items 1 and 2 cover all six rows: exact optimum 6. Its actual ratio is 5/6; the finite-k worst-case factor is 3/4. Neither number is a claim that greedy is optimal.

A separate duplicate-representative matrix [[5,5,0],[0,0,4]] makes singleton top-k choose duplicate representatives for value 5. Updated greedy chooses complementary items for value 9, also the exact optimum. This comparison is descriptive, not a causal learned-mechanism result.

A monotone synergy table gives greedy 3 versus optimum 10 and fails submodularity. A submodular but nonmonotone table makes exactly-k greedy end at 0 while at-most-k optimum is 2. Both withhold theorem and bound fields. Zero/all budget, all-zero optimum ties, fractional values, modular additivity and seeded rectangular controls remain present.

## Prefix upper bounds use k

For any visited prefix A, an optimal set need not contain A. Monotonicity and diminishing returns bound its value by f(A) plus the k largest nonnegative remaining gains, capped by f(V). Taking the minimum bound over every visited prefix gives the final upper bound. Substituting k-|A| would incorrectly certify 5 below the default control's true optimum 6. The actual greedy/OPT ratio and greedy/upper-bound certificate are distinct fields.

## Verification

The original discrete release checked 24 Python tests on 3.10-3.13. They include 120 independently enumerated facility controls, 100 arbitrary-table full lattice/nested-set comparisons, 40 positive-scale controls, 30 facility/table equivalence controls and 60 all-subset prefix-bound controls. These are controls within tests, not separate test methods.

24 complete native/BigInt reports match 16,426 exact leaves. Actual Chrome verifies 360 subset rows/bars and 2,056 full records: 360 subsets, 33 greedy steps and their candidate tables, 57 prefixes, 812 edges and 794 diminishing-return witnesses. Summary selections, assumption failures, certificates, export, stale/invalid behavior and 320/390/1280 containment are checked. Isolated installed-wheel reproduction verifies all reports, console CLI and four module origins outside checkout.

## Boundaries and prior work

At most six selectable items, 64 subsets and eight represented facility rows. Exact rational strings, no learned embeddings, API calls, cost/knapsack or matroid constraints, lazy/stochastic greedy, runtime benchmark, downstream quality metric or new theorem. Exhaustive enumeration is exponential, not a scalable optimizer.

Native JSON rejects duplicate keys and bounds input to 32KiB. Browser JSON.parse retains the last duplicate key and bounds input to 32,768 characters. These parser differences are explicit.

Established theory is credited to Nemhauser, Wolsey and Fisher; definitions and proof are cross-checked against Krause and Golovin's survey, Submodlib objective documentation and the Isabelle Archive of Formal Proofs. METHOD.md records exact links and documentation shorthand conflicts. This implementation is not formally verified. Implementation, independent checks and original synthetic controls by Midya Rahmani; no external code, figures, datasets or weights copied.

## Exact expectation and deterministic cardinality rounding

The separate rounding inspector shows the exact multilinear extension, every excluded-item gradient and excluded-pair Hessian context, independent-product count probabilities and both endpoints of every deterministic cardinality swap. A two-item half-probability control has expected count 1 yet exceeds budget 1 with probability 1/4; its duplicate-coverage expectation 3/4 rounds to a singleton worth 1. Nonmonotone submodular controls are accepted, while synergy and wrong total probability mass refuse rounding. The extension adds nine Python tests (33 total), 21 reports matching 10,682 exact native/BigInt leaves, independent product/derivative/path oracles, full-record Chrome checks and installed reproduction. This is bounded deterministic rounding, not continuous optimization, randomized marginal preservation, a general matroid method or a learned-quality claim.

[Live rounding inspector](https://midya8.github.io/submodlab/rounding.html) · [Rounding method and sources](https://github.com/midya8/submodlab/blob/main/ROUNDING.md)
