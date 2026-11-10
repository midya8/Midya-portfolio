# ShapleyLab: exact attribution for an explicit reference game

[Public repository](https://github.com/midya8/shapleylab)

Dependency-free Python scalar callback API/JSON CLI, 49 Python tests plus four Node/actual-Chrome tests, offline demo and Python 3.10-3.13 CI. Standard formula, no new theory.


## Boundary

A local explanation is a choice of score function, point and reference game.
ShapleyLab enumerates the empirical-background replacement game. It does not
learn a model or infer feature causality. The CLI evaluates only an explicitly
serialized polynomial scorer; the Python API can wrap any deterministic finite
scalar predictor. No network requests, dynamic imports or model downloads.

## Joint replacement semantics

For each mask, replace excluded coordinates using one complete background row,
then average scores over rows. This preserves dependence among missing features
but breaks fixed/missing dependence. It is not conditional imputation and does
not factor the empirical background into independent coordinate marginals.
For product score with background (0,0)/(1,1), v(empty)=0.5, not 0.25.

## Exact enumeration

For d features, store 2**d coalition values by integer bit mask. Each feature's
Shapley value averages its marginal increment using weight
`1 / (d * choose(d-1, |S|))`. An independent factorial ordering implementation in
tests checks dimensions 1-6. In exact mode, no Monte Carlo or regression approximation occurs.
The full mask invokes the score once instead of B times. Every other mask uses
all B rows, so calls equal `(2**d - 1)*B + 1`. The callback must be deterministic;
we do not spend extra calls trying to prove determinism. Counts are not walltime.

## Numerical behavior

Check finite coordinates and scalar outputs. Average by fsum of contributions
divided by B, avoiding an overflowing raw sum. When all background outputs are
identical, return that float unchanged, preserving equality to the single full
mask score. Attribution increments/means and the efficiency residual must remain
finite or fail. Do not renormalize attributions or allocate numerical residuals
to arbitrary features. Exact refers to coalition enumeration, not symbolic
arithmetic or unknown population attribution.

## Work limits

Individual mode rejects dimensions outside 1-12. Group mode accepts up to
64 raw features partitioned into at most 12 atomic groups. Both reject background
sizes outside 1-1000 and budgets outside 1-1000000. Default call budget 200000. Validate budget before invoking the
callback. Lists are copied where output could otherwise alias input; callbacks
receive immutable tuples. A malicious or stateful callback is outside the model
contract and cannot be made safe by an attribution algorithm.

## Counterexamples are part of the demo

Product at x=(2,3,99) yields [3,3,0] relative to zero background but [2,3,0]
relative to a background with the first two coordinates one. Prediction remains
6; baseline changes from 0 to 1. A different background asks a different question.
For squared difference with diagonal binary background and diagonal target,
coalitions [0,0.5,0.5,0] yield zero attribution and zero residual while singleton
hybrids are off the observed manifold. Passing efficiency is not manifold proof.
The sigmoid polynomial is hand-specified, not trained or accuracy-benchmarked.

## Atomic feature groups

Optional `groups` are an explicit, disjoint, exhaustive partition of raw feature
indices. Every feature in a group switches together between target and the same
background row. `explain_groups` applies the ordinary Shapley formula to these
groups as atomic players; it does not compute individual values then add them.

```python
from shapleylab import explain_groups

result = explain_groups(
    lambda row: row[0] * row[1] * row[2],
    point=[1, 1, 1], background=[[0, 0, 0]],
    feature_names=["a", "b", "c"],
    groups=[{"name": "ab", "features": [0, 1]},
            {"name": "c", "features": [2]}],
)
assert result["group_names"] == ["ab", "c"]
assert result["attributions"] == [0.5, 0.5]
```

The ungrouped three-way product gives `[1/3, 1/3, 1/3]`. Summing the first two
individual values gives 2/3, **not** the grouped value 1/2. Grouping changes the
coalition game and the question; no arbitrary credit split back to members is
reported. This mode is not an Owen-value allocation within groups.

The same optional `groups` key is accepted by the JSON CLI:

```sh
python -m shapleylab explain --input examples/grouped.json
```

In group mode, `attributions` align with `group_names`, not `feature_names`.
`feature_names` retains the raw coordinate order; `group_feature_indices` records
the partition; `attribution_unit` explicitly identifies atomic groups. Coalition
mask bit j includes all members of group j. Names must be distinct, groups
nonempty, indices valid integers, with every feature covered exactly once.

Up to 64 raw features and 12 groups, still at most 1000 background rows and the
same call budget. Replace d by group count G in `(2**G - 1)*B + 1`. The three-way
fixture uses 4 calls instead of 8 because its game has 2 players instead of 3;
this is not an equal-question speed benchmark. A tested 64-feature/eight-group
sum uses 256 calls with one background row, returning eight values of 8.

Grouping a known correlated block prevents hybrids that split that block. It
does not preserve dependencies across different groups, infer groups for you,
make reference rows representative, or establish conditional/causal validity.
Singleton groups recover the original individual-feature game; one group
receives prediction minus baseline. Group ordering changes output order only.

Source for the grouping concept and distinction from post-grouped sums:
[Jullum, Redelmeier and Aas, groupShapley (2021)](https://ar5iv.labs.arxiv.org/html/2106.12228).
ShapleyLab retains its declared empirical replacement contribution function;
it does not implement that paper's conditional-distribution estimation or claim
new grouping theory.

## Optional permutation approximation

Exact mode remains the default and is preferable for small games. For up to
64 individual features, `explain_sampled` instead samples independent uniform
feature orderings with an isolated seeded RNG. For each ordering, it adds every
feature in sequence and records that feature's marginal score increment. The
mean increment is its estimated attribution. Every visited coalition is still
averaged over **all** background rows; backgrounds are not subsampled.

```python
from shapleylab import explain_sampled

result = explain_sampled(
    lambda row: row[0] * row[1] * row[2],
    point=[1, 1, 1], background=[[0, 0, 0]],
    feature_names=["a", "b", "c"], permutations=2, seed=0,
)
assert result["attributions"] == [0.5, 0.5, 0.0]
assert result["monte_carlo_standard_errors"][2] == 0.0
# Exact third attribution is 1/3, despite zero observed Monte Carlo error.
```

```sh
python -m shapleylab explain --input examples/product.json --permutations 64 --seed 0
```

Sampled output has `method=independent_permutation_monte_carlo`, P/seed, per-feature
MC standard errors, cached coalition count, actual score calls and a preflight
upper call bound. No complete coalition-value array is reported in sampled mode.
Sampled grouped mode is not implemented and is rejected, not silently ignored.
P must be 2-10000 (default API 256), seed an integer in [0, 2**32). Exact CLI mode
rejects a nondefault seed without `--permutations`.

The diagnostic is sample SD of per-permutation increments divided by sqrt(P).
It describes permutation randomness for this **fixed** model/point/background,
not model-training uncertainty, background representativeness or confidence in
feature importance. No confidence intervals, adaptive stopping, antithetic
pairing or convergence certificate. Zero observed MC error at small P can miss
a nonzero exact attribution, as the executable example shows. Each ordering
telescopes to prediction minus baseline, so efficiency can pass while individual
allocations remain wrong.

On the three-way product, P=2/seed 0 gives `[0.5, 0.5, 0]`, standard errors
`[0.5, 0.5, 0]`, six calls. P=4096/seed 0 gives
`[0.3220215, 0.3415527, 0.3364258]`, standard errors about
`[0.0073017, 0.0074108, 0.0073835]`, eight calls with caching. Exact is
`[1/3, 1/3, 1/3]`. These are fixed development examples, not a guarantee that
more samples always improve a realized estimate. Even when all eight coalition
values enter the cache, sampled output still averages the drawn increments;
it does not silently switch to the exact coalition-weight formula. Prefer exact
mode when that game fits its budget.

For d features and B rows, at most `min(2**d, 2 + P*(d-1))` unique masks are visited.
The preflight upper call bound is `(max_masks - 1)*B + 1`, accounting for the
single full-mask call. A bound exceeding the budget rejects before any callback;
this can be conservative because orderings can share masks. A tested 64-feature
sum with P=32/seed 4 uses 2002 calls (upper bound 2018), producing 64 unit
attributions and zero MC errors since every linear marginal is constant. This
is a call count for a constructed score, not a walltime or quality benchmark.

Standard permutation-sampling idea:
[Captum Shapley Value Sampling documentation](https://captum.ai/api/shapley_value_sampling.html).
Independent educational implementation, no Captum dependency. This mode is not
SHAP's forward/reverse antithetic PermutationExplainer or a new estimator.

## Source credit

The standard formula and masking distinction are documented at:

- https://arxiv.org/abs/1705.07874
- https://shap.readthedocs.io/en/stable/generated/shap.LinearExplainer.html
- https://selfexplainml.github.io/PiML-Toolbox/_build/html/guides/explain/shap.html

Independent educational implementation. No new explanation theorem, conditional
SHAP, TreeSHAP, causal identification or efficiency advantage is claimed.


### Live replacement and permutation ledger (v0.2)

[Live inspector](https://midya8.github.io/shapleylab/) exposes every background
replacement row, coalition value, weighted predecessor term and complete small
player ordering. Native audits log actual calls to the original exact engine;
cached paths add no score evaluations. The independent browser recomputes seven
fixed public synthetic games under bounded target edits, not a user callback.
Atomic grouped credits remain distinct from post-summed individual credits.

49 Python tests plus four Node/actual-Chrome tests check 95 coordinate edits,
128 Fraction games, 64 independent BigInt product games, all 44 original
coalitions, 18 players and 30 orderings. Installed 11-module/four-command
reproduction retains original exact/grouped/sampled modes and all prior demo
reports. Signed zero-centered bars, hybrid provenance, invalid-state clearing
and JSON witnesses are checked at 320/390/1280 widths.

The original diagonal-reference squared-difference game still assigns zero
credits through unrealistic singleton hybrids. The P=2 sample still assigns
zero estimated error to a wrong dummy-looking credit. Efficiency alone validates
neither. No new model, training, causal attribution, representative-background,
confidence or explanation-quality claim.
[Derivation, six sources and limits](https://github.com/midya8/shapleylab/blob/main/LEDGER.md).


## ShapleyLab 0.3: Together changes the share

The same three-way product can assign `[1/3, 1/3, 1/3]` to individual features, `[1/2, 1/2]` to two atomic groups, and `[1/4, 1/4, 1/2]` to Owen members when `a,b` must arrive together. One score and background, different allowed orders. Equal splitting and post-summing ordinary credits are not the same rule.

The two-level Owen mode keeps every background-replacement evaluation, member coefficient, quotient-group marginal and complete admissible ordering. Its native checker imports no generator and independently replays the declared synthetic score and full allocation report. The independent browser computes permutation-count weights, lets you edit the supplied model and partition, and downloads evidence that the native CLI can verify.

[Live editable inspector](https://midya8.github.io/shapleylab/owen.html) · [Source and installed reproduction](https://github.com/midya8/shapleylab) · [Method, sources and boundaries](https://github.com/midya8/shapleylab/blob/main/OWEN.md) · [Reviewed change](https://github.com/midya8/shapleylab/pull/2)

72 Python tests include 556 signed game/partition cases checked across 50,362 independent Fraction orderings, 14,668 unanimity-support/partition cases and separate primitive-mutation checks. 132 complete native/JavaScript reports agree, plus 206 broad-magnitude, half-even, subnormal and cancellation reports independently native-verify. An original BigInt binary64-unit summation helper fixes a pre-release double-rounding failure without widening tolerance. Actual Chrome checks all 12 original controls at 320/390/1280, 12 trusted completed native-verified downloads, and raw/sigmoid six-feature/32-background requests with 2017 evaluations and 720 paths each. Fresh installed-wheel checks preserve all 95 prior edit archives and original modes. All 24 feature/PR checks, 12 main checks and three Pages jobs passed. All ten deployed assets and the original root match public source; all 45 deployed browser states match the tested unmasked pixels.

Established coalitional-value theory, original supplied synthetic controls, no new allocation theorem or measured explanation-quality result. Standalone supplied tables support up to eight features; full declared-score/browser reports up to six features and 32 background rows. Computed float leaves compare at disclosed absolute/relative `1e-12`; integer metadata remain exact. Replay is not authentication or a global error bound. A supplied partition does not validate a background or prevent off-reference within-block hybrids. No arbitrary nested hierarchy, conditional/causal effect, learned grouping, paid API or private data.
