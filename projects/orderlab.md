# OrderLab: exact rank aggregation

OrderLab combines weighted complete rankings into a total order with the least pairwise disagreement. Compare every exact Kemeny optimum with an adjacent-swap local search, which can stop at a worse order. The browser shows each majority comparison, cycle, descent step and subset recurrence. Export the report and replay it independently from ballot inversions.

[Live inspector](https://midya8.github.io/orderlab/) · [Source](https://github.com/midya8/orderlab) · [Method and attributed theory](https://github.com/midya8/orderlab/blob/main/METHOD.md) · [Documentation review](https://github.com/midya8/orderlab/pull/2)

## Local cost, global cost and the pair bound

The developed default uses ballot `0>1>2` with weight 3, `1>2>0` with weight 2 and `2>0>1` with weight 2. Strict majority margins form the cycle `0>1>2>0`, with margins `3,3,1`.

Start at `1>2>0`: cost **10**. Its two adjacent swaps worsen cost by **3** and **1**, so strict descent stops immediately. Yet the unique global optimum `0>1>2` costs **8**. Choosing the cheaper direction independently for every pair gives a lower bound of **7**, but not a transitive order.

| Quantity | Exact value | Meaning |
|---|---:|---|
| Local endpoint cost | 10 | The declared start resists every adjacent swap |
| Global optimum | 8 | Minimum over all six total orders |
| Independent-pair lower bound | 7 | The sum of each pair's cheaper disagreement direction |
| Local/global gap | 2 | What the local stopping rule misses |
| Extra cost above pair bound | 1 | What one total order must pay beyond independent pairs |

The report calls the last quantity `cycle_tax`; it is not a cycle count or causal attribution to individual cycles. Weights are supplied multiplicities, not learned reliability. All tied optimal orders remain: the six-candidate all-tie control has 720 optima, not one ID-selected answer.

## Inspect any order or subset

Select any complete order to see each ballot's inversions and weighted cost, every pair's disagreement and lower-bound excess, and every adjacent neighbor's exact cost delta. The complete order census marks local, strict-local and global status independently. Select any subset to inspect all candidate-first transitions, minimum choices and complete restricted optimum counts. The empty subset has one empty order. Singleton local predicates hold vacuously.

The local policy takes the most negative adjacent delta, breaking equal improvements by the leftmost position. It never traverses zero-cost plateaus. That policy controls only the trace; it does not prefilter the global family.

Dense majority graphs retain all pairs and strict/tied directions. Four-or-more-candidate edge labels are omitted to prevent overlap; complete exact weight tables sit directly below. Editing input clears prior evidence and disables stale export. Tables scroll internally on small screens.

## Solver and checker paths

Python places the first candidate in each exact subset recurrence. JavaScript independently computes values by placing the last candidate and scores full orders directly from ballots. The native replay checker imports neither solver nor report generator: it enumerates every restricted permutation and sums ballot inversions directly. It checks types, omissions, complete tied families, transition rows, all neighbor deltas, strict cycles and the deterministic trace. Shared input validation remains a common trust surface.

An optional input-built binary linear-ordering formulation uses SciPy/HiGHS with every triangle constraint, explicit 0..1 bounds and integrality. It checks one optimum cost per non-singleton profile and decodes/rescores the returned order. This is a numerical reference at tolerance `1e-8`, not the exact all-family certificate.

## Reproduction checks

| Check | Developed scope |
|---|---|
| Native Python | 18 tests; 76 complete developed/seeded profiles |
| Exact report evidence | 10,427 full orders; 1,542 subsets; 3,883 transitions; 22 strict cycles |
| Mutation rejection | 1,100 changed derived primitives across three controls, all rejected |
| Cross-engine | Two Node tests; 76 complete JS/Python reports with native replay |
| Independent integer reference | 65 HiGHS solves; 422 triangle constraints; zero observed optimum cost discrepancy |
| Installed reproduction | Six module origins outside checkout; sixteen controls; both CLI entrypoints; 32 rejected tampered reports |
| Actual Chrome | 48 control-width views; 5,091 order selections; 846 subset selections |
| Visible row oracle | 12,861 ballot, 70,464 pair, 24,132 swap and 2,019 transition rows rebuilt from ballots |
| Download replay | Sixteen trusted-click exact reports verified natively |

```sh
python -m pip install .
orderlab demo > report.json
orderlab verify report.json
python -m unittest discover -s tests -v
node --test tests/test_engine.cjs tests/test_browser.cjs
python tools/check_installed.py
python tools/check_milp.py
```

The documentation review is published at main `4c9de871db767949470d4217265b4c58f1c48f6c` in [PR #2](https://github.com/midya8/orderlab/pull/2). Fresh checkouts of its head and merged main matched all 46 intended files and passed the Python, Node, actual-Chrome, installed-wheel and generated-asset checks. Both [head CI runs](https://github.com/midya8/orderlab/actions/runs/43349613439), [main CI](https://github.com/midya8/orderlab/actions/runs/43349781930) and [Pages deployment](https://github.com/midya8/orderlab/actions/runs/43349781506) passed. The five deployed assets match main, and the full deployed Chrome workflow passes, including independent download replay. All 35 deployed screenshots match the local captures; desktop and mobile review covers the local-gap, global-optimum, empty-subset, all-tie, invalid-input and horizontally scrolled table states. These checks cover the released implementation, not the truth or fairness of supplied preferences.

## Scope and prior work

One to six candidates, one to sixteen complete strict ballot rows, positive integer weights up to 1,000 and total weight up to 10,000. No tied or partial input rankings. Cost is bounded by 150,000 and order counts by 720, so the browser uses exact safe-integer arithmetic without a floating optimizer. Python has no runtime dependencies; the static inspector has no service, paid API, external font or analytics.

This is classical Kemeny aggregation, not Borda, a learned ranker, fairness model, real election recommendation, held-out evaluation or new theorem. The candidate-subset recurrence is credited to Betzler et al., Theorem 4; Dwork et al. establish the local/global distinction, and existing all-optimum/software work is acknowledged in [SOURCES.md](https://github.com/midya8/orderlab/blob/main/SOURCES.md). The implementation, controls, UI and evidence schema are original.

Subset values have `2^n` states, but full-order/cycle families and exhaustive replay add factorial/output-size work. No end-to-end scalability claim is made. A self-consistent report authenticates arithmetic for its included input, not the intended provenance of those ballots.
