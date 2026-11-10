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
