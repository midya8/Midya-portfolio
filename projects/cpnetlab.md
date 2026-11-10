# CPNetLab

Exact finite qualitative preferences. Supplied tables, not learned human tastes.

## CPNetLab: a ranking is not an entailed preference

[Live workbench](https://midya8.github.io/cpnetlab/) · [Source and reproduction](https://github.com/midya8/cpnetlab) · [Contract and limits](https://github.com/midya8/cpnetlab/blob/main/CONTRACT.md) · [Prior-work ledger](https://github.com/midya8/cpnetlab/blob/main/SOURCES.md)

Complete, supplied binary CP-nets define legal single-variable improvements, not a universal score. CPNetLab enumerates every outcome and improving flip, finds shortest paths or closed no-path cuts, counts every compatible strict ranking, and supplies two actual opposite rankings when a pair is incomparable. Incomparable does not mean indifferent.

- **One legal flip can violate more rows.** In a four-variable fanout, `0000 → 1000` is an improving flip while violated rows rise from 1 to 3. All 2,304 compatible strict rankings still put the target above the start. Counting violated rows is not the preference semantics.
- **Dependency cycles and inconsistency are different.** A matching two-variable dependency cycle permits four strict rankings. Reversing one table produces the actual improving cycle `00 → 01 → 11 → 10 → 00`, zero strict rankings, and no vacuous dominance verdict.
- **Many rankings need not settle a pair.** Two independent consistent cycles admit exactly 101,977,088 rankings while leaving `0000` and `1111` incomparable. The UI displays a complete ranking for each direction.

A separate Python checker rebuilds the entire evidence report using Hamming-one pairs, Floyd-Warshall and suffix-removal counting, rather than the generator's conditional-row flips, breadth-first paths and prefix-ideal counting. Shared validation and binary encoding are disclosed. Python and JavaScript agree on all eight controls, 61 outcomes and 100 edges. Browser JSON is independently checked only after the Python verifier accepts it, not merely because export worked.

Reproduction covers all 36 two-variable networks and 576 ordered queries against all permutations; five three-variable fixtures against all 40,320 permutations each; 160 seeded additional networks; strict evidence forgeries; Python 3.10-3.13; and installed-wheel execution outside the checkout through module and console commands. Actual Chrome checks 24 reports at three widths, all 689 ordered control comparisons, every rendered conditional row, path, ranking witness and no-path cut, all eight evidence exports, and stale/invalid/cycle recovery. Final source, CI, deployment assets, behavior and pixels were checked before this showcase was published.

**Exact scope:** zero to four variables and at most 16 outcomes; complete strict binary local tables. No learned human preferences, local ties, missing rows, constraints, cardinal utility, partial-model semantics or scalable-solver claim. CP-net theory and graph/counting methods are established prior work; these are developed synthetic controls, not human-choice measurements or a new algorithm.


## CPNetLab row subsets: minimal is not minimum

[Live whole-row atlas](https://midya8.github.io/cpnetlab/scopes.html) · [Source](https://github.com/midya8/cpnetlab) · [Contract](https://github.com/midya8/cpnetlab/blob/main/ROW-SUBSETS.md)

Enumerate every whole conditional-row subset, not one convenient explanation.
Eight developed controls cover 865 subset graphs with actual improving paths,
inconsistency cycles and compatible strict-ranking witnesses. The default
256-subset control has two minimal conflicts and six irreducible withdrawals:
three remove one row, three remove two. A separate control has two-row and four-row
minimal path supports. Minimal does not mean minimum; neither means the right
human preference to abandon.

The independent Python checker labels Hamming-one pairs, uses Floyd-Warshall
paths and checks all proper candidate subsets. It reconstructs every mask and
all four antichains without importing either analyzer. Shared strict input
validation/outcome encoding is disclosed. Browser JSON is independently checked
only after Python accepts it. Whole-row withdrawal removes all justified flips,
not an arbitrary single edge. All outcomes and the supplied model remain intact.
This is bounded what-if constraint evidence, not automatic preference revision,
indifference, extended partial-model semantics, learned preferences or a new
algorithm. At most eight rows, sixteen outcomes and 256 subsets.

Release checks: 14 Python tests on 3.10-3.13; six combined Node/actual-Chrome tests;
all 576 ordered two-variable query atlases (6,400 subset records); all 400
two-variable masks against every possible total order; 91 accepted seeded row
atlases; installed 0.2.0 wheel outside the checkout through both CLI entry points
for both eight-control families; forged-evidence rejection. Actual deployed Chrome
selects all 865 masks, all 46 antichain buttons, every row toggle and all eight
exports, with stale/invalid/row-limit recovery and eight controls at three widths.
The original complete-model checks remain green. Feature/PR/main CI and Pages
passed; 37 source files, all 11 live assets and the root page match, with 28
main/feature and 28 main/deployed unmasked pixel matches.
