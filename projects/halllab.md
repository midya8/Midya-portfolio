# HallLab: exact all-different support

HallLab computes which variable/value pairs belong to complete assignments in supplied tiny domains. Every retained variable/value has a complete injective assignment. Every pruned edge has a forced-residual Hall obstruction. Compare against full synchronous pairwise arc consistency, not a weakened one-pass baseline.

[Interactive inspector](https://midya8.github.io/halllab/) · [Exact method, boundaries and six-source ledger](https://github.com/midya8/halllab/blob/main/METHOD.md)

```json
{"values":3,"domains":[[0,1],[0,1],[0,1,2]]}
```

Two variables reserve `{v0,v1}`. Pairwise disequalities leave all seven edges; global support leaves five, forcing x2 to v2. Each rejected edge explains the residual variable group with fewer available values than variables. A second control has three variables sharing two values: every binary constraint has support but no full assignment exists.

## Run and audit

```sh
python -m halllab input.json --output report.json
python -m halllab report.json --verify
python -m unittest discover -s tests -v
npm test                      # Node 22 + actual Chrome
bash tools/check_wheel.sh      # installed outside checkout, both CLI entry points
python -m http.server 8000 --directory docs
```

Or `pip install .`, then `halllab input.json`. Python 3.10+, no runtime dependencies; build requires pip/setuptools. Browser runs an independent exhaustive JavaScript engine, never an API or packaged native output.

```python
from halllab import analyze, verify
report = analyze({"values": 3, "domains": [[0, 1], [0, 1], [0, 1, 2]]})
assert report["filtered"] == [[0, 1], [0, 1], [2]]
assert verify(report)  # exhaustive independent oracle, no matching calls
```

## What the one-scope inspector shows

- Maximum-cardinality matching, canonical ties and exact complete-assignment count.
- All original edges with either first full support assignment or first forced-residual deficient subset.
- Every original tight/deficient Hall subset; tight is not impossible.
- Original, pairwise fixed-point and globally supported domains; every synchronous binary-AC round.
- Original synthetic controls for hidden Hall bottlenecks, noninterval domains, surplus values, reassignment, symmetric supports, empty domain/scope, cascade and full 48-edge scope.
- Strict bounded JSON CLI, atomic output and exact report verification. Edits/invalid input clear stale browser reports.

The original 12 native tests, retained in the current 36-test suite, cover 8,777 exhaustive domain graphs and 120 seeded larger inputs; 682 full Python/JS report comparisons; Chrome replays every edge/subset/round at three widths. Fresh installed reproduction and CI span Python 3.10-3.13. [METHOD.md](https://github.com/midya8/halllab/blob/main/METHOD.md) gives actual counts, semantics and source attribution.

## Limits before interpretation

At most six variables/eight values; one all-different relation, not a complete constraint solver. Classic matching/Hall theory, not a new AI algorithm. Native repeated DFS matching queries plus bitmask counting versus independent exhaustive native checker and JavaScript assignment recursion. The original one-scope implementation does not use Régin SCC, Hopcroft-Karp, Choco or NetworkX; the separate alternating workflow and optional Choco reference are described below. No scalability benchmark, learned model, real assignment deployment or whole-CSP guarantee. A full match for one constraint does not ensure a shared solution for several constraints. MIT license.


## Overlapping scopes: local support is not a joint solution

[Overlapping-scope inspector](https://midya8.github.io/halllab/overlaps.html) · [Exact overlap contract and sources](https://github.com/midya8/halllab/blob/main/OVERLAPS.md) · [Source](https://github.com/midya8/halllab)

Repeat full local all-different propagation to a synchronous fixed point, then compare it with exact common-assignment support across overlapping scopes. A two-color triangle keeps every local value but has no joint assignment. A satisfiable triangle keeps local values that never occur in a common solution. Inspect each round, original-variable mappings, scope-only witnesses, full common witnesses and exhaustive rejection bins.

Separate native API/module CLI, independent report checker and JavaScript engine. Eight new native tests and three new Node/Chrome tests preserve the original test sources. Full cross-engine checks cover 621 overlap reports; nine browser controls run at 320/390/1280 widths. Installed-wheel checks run outside the checkout. Tiny exact reference: six variables, eight values, six scopes, at most 262144 full tuples. Classic consistency theory, not a scalable CP solver or a new algorithm.


## Conflicts and minimal removals

[Live conflict inspector](https://midya8.github.io/halllab/conflicts.html) · [Exact contract and seven-source ledger](https://github.com/midya8/halllab/blob/main/CONFLICTS.md) · [Source](https://github.com/midya8/halllab)

All inclusion-minimal conflicting all-different scope sets and all inclusion-minimal scope-removal repairs, with complete single-deletion witnesses, common kept-network assignments and contained conflicts for every restoration. The default diamond has a size-one and four size-two minimal removals: minimal is not minimum. Inspect every active subset and the hitting-set intersections that explain why a repair must break every conflict. Domains stay fixed; an empty-domain background has no scope-removal repair.

Independent native histogram generation, per-subset product verification and recursive JavaScript search. The first three report families had 28 native tests and nine Node/actual-Chrome tests, retained in the current suite; 621 cross-engine reports and 4413 active subsets. Installed wheel reproduces all three report families outside checkout. Prior implementations/tests retained. All browser controls/proofs checked at 320/390/1280. Tiny exact relations, not a scalable MUS/MCS solver, weighted optimizer or a new duality theorem.


## Alternating support: spare values and cycles

One variable and two values produce three singleton alternating SCCs, but both domain edges have support. HallLab's fourth inspector follows a free value through an even alternating path, flips its edges, and shows the resulting full assignment. Compare cycle support, tight Hall pruning, isolated values, empty scope and impossible partial matchings. Every original edge has a directed arc and either an explicit full matching or a forced-residual Hall obstruction. Dummy-node SCCs expose the equivalent characterization without hiding where the spare value starts.

The native generator uses augmenting matching, Tarjan SCCs and free-root reachability; a separate checker uses exhaustive partial tuples and Floyd closure, while the browser independently uses assignment recursion and BFS classes. All 5,058 tiny domain graphs, 120 seeded bound-wide cases, 821 complete cross-language reports and 136 primitive forgeries are checked. Actual pinned Choco4.10.18 AC_REGIN propagation agrees over 821 cases, with real FC/NEQS/AC calibration. Thirty-six Python tests and 12 Node/Chrome tests preserve all previous tests; a fresh installed wheel checks both new entrypoints and atomic failure behavior.

The deployed inspector replays all 12 controls at 1280/390/320, every edge certificate, reach layer, SCC and flip step, with trusted completed JSON downloads and narrow-screen rightmost-scroll checks. Fresh public source reproduction, installed entrypoints, CI, deployed assets and phone/desktop workflow screenshots were checked. This is classical bounded all-different theory on at most six variables and eight values, not a new algorithm, production incremental solver, learned model, scale benchmark or whole-CSP guarantee. The earlier matching/Hall, overlapping-scope and conflict/removal workflows remain separate.

[Live alternating inspector](https://midya8.github.io/halllab/alternating.html) · [Source](https://github.com/midya8/halllab) · [Exact contract and eight-source ledger](https://github.com/midya8/halllab/blob/main/ALTERNATING.md) · [Pull request](https://github.com/midya8/halllab/pull/4)
