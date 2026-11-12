# BuchiLab: a winning state is not a winning policy

[Repeated-goal inspector](https://midya8.github.io/buchilab/) | [Action-lasso inspector](https://midya8.github.io/buchilab/lassos.html) | [Max-parity inspector](https://midya8.github.io/buchilab/parity.html) | [Source](https://github.com/midya8/buchilab)

An idle action can stay inside a winning region forever and still lose. BuchiLab shows why: reaching a goal once, returning to it forever and winning by the highest recurring priority are different objectives. Three separate inspectors expose the policies and counterexamples in small finite adversarial games. They implement established game theory, not a new solver or a real-agent safety guarantee.

## Returning to the goal

The original inspector exposes every nested greatest/least fixed-point update, synchronous predecessor obligation, progress rank, complete controller policy and reachable cyclic non-goal component. Idle can preserve the winning region without making progress. Rank-permitted actions are sufficient, not a catalog of all winning policies. Policy audits keep every environment move.

Seven original controls distinguish recurrence from one-time reachability, environment starvation from controller choice, full-graph components from non-goal induced cycles, and an empty controller policy from no policy. Input is bounded to six states and three moves per state. Final unchanged fixed-point rounds remain visible.

The generator uses bitmasks, Tarjan components and BFS. The native checker uses sets, Floyd reachability and exact eventual-lasso replay for every joint positional-policy pair without calling the generator. The browser uses its own sets and graph-search closure. Shared validation and written semantics remain shared; separate implementations are not separate theories.

## Replaying a failure

The action-lasso page turns each failing fixed controller policy/root into an exact action-labelled finite prefix followed by a nonempty non-goal cycle forever. Empty prefixes, self-loops, multiedge cycles, unreachable bad components and duplicate-target action choices remain distinct.

BFS generation is checked by bounded simple walks and the joint-policy lasso oracle. The input-order anchor is deterministic. The prefix and cycle are individually shortest for that anchor, not a globally shortest lasso. These are counterexamples to individual fixed policies, not one environment strategy defeating every possible controller policy. Original v1 reports and commands remain supported.

## The maximum that keeps returning

The separate max-parity page has two states where Even wins from both, yet its first complete policy loses. Waiting forever at priority 1 loses; repeatedly visiting priority 2 wins. A finite priority-7 prefix never overrides a recurring priority-0 cycle. Another control changes only ownership to expose an odd self-loop hidden inside an even-maximal component.

The page opens each classic Zielonka recursive subgame, both attractors, synchronous exists/all predecessor obligations and every original named move. Every complete policy retains all opponent moves, including choices outside its winning region. Threshold-induced components expose losing subcycles. Reachability is computed in the full retained graph, so a higher-priority finite prefix cannot hide a lower-priority recurring loss.

The checker uses set recursion, positive-length Floyd classes and every joint-policy root lasso. The browser uses sets, BFS classes and path replay, checking each fixed policy against the full joint atlas. Canonical strategies are the first complete policies winning the whole region, found by bounded enumeration. They are not presented as strategies directly synthesized by the recursive solver.

The game is finite, total, fully visible and turn-based, with one to six states, one or two moves per state and priorities 0 through 7. The largest joint atlas has 64 policy pairs and 384 root lassos, not 64 squared pairs. Sources use both minimum- and maximum-recurring conventions; this page uses maximum and records that choice in every report. The repeated-goal API and action-lasso workflow remain separate.

## What the checks cover

The current suite has 31 Python tests and nine Node/actual-Chrome tests. The original repeated-goal release had nine Python and three Node/Chrome tests; the lasso release brought those totals to sixteen and five. All are retained, with fifteen Python and four Node/Chrome parity tests added.

The original checks include 21,952 exhaustive three-state games and 331 complete native/browser reports. Action-lasso checks compare 314 complete reports and all records in ten controls. Parity checks compare 660 complete native/checker/browser reports: 576 exhaustive two-state arenas, 72 seeded arenas and twelve original controls. Each of 207 noninput primitive leaves is separately altered and rejected, with structural, type, order and truncation forgeries checked separately.

Actual Chrome covers the original controls and action-lasso controls at 320/390/1280. Parity checks cover 36 control/width reports, 117 recursive call selections, 126 attractor rounds, 333 predecessor rows, 114 policies, 309 policy-root selections, 273 threshold components, 327 joint-root lassos and 696 action steps. Twelve parity downloads use trusted mouse events and completed file bytes, then the native checker, not an intercepted Blob or patched anchor.

Fresh installed wheels check nine module origins under site-packages. The original seven goal controls run through two CLI entrypoints, ten action-lasso controls through the module CLI, and twelve parity controls through two entrypoints. Parity installed checks reject 24 direct and 48 atomic CLI forgeries outside checkout. CI covers Python 3.10-3.13 and actual Chrome. Counts describe this bounded corpus, not every six-state game or a formal proof.

## An external solver was actually run

Pinned Oink source `db336a53e6a1b2dc12ab89b58d1871fe565d0147`, with Lace `a091978dc4479fc3b9bc7af7dc77939ec8587c44`, was separately built and executed. Three solver families run 1,980 times and agree on 3,960 winning regions. Oink verifies all 660 supplied canonical strategy certificates, with a known-good and known-bad policy calibration. It does not choose those supplied policies for the certificate check.

The optional build uses isolated CMake 3.31.10. A pinned bundled cxxopts header omits `<cstdint>` and failed on the newer hosted compiler; the build explicitly preincludes that standard header without modifying the pinned sources. The original CI failure is retained. This external evidence checks winning regions and canonical strategies, not our JSON parser, trace ordering, attractor display or the underlying theorem. Oink is not a vendored runtime dependency.

## Contracts, credit and limits

[Original method and seven-source ledger](https://github.com/midya8/buchilab/blob/main/METHOD.md) | [Action-lasso contract](https://github.com/midya8/buchilab/blob/main/LASSOS.md) | [Parity method and inspected sources](https://github.com/midya8/buchilab/blob/main/PARITY.md)

The source records exact synchronous update rules, rank resets, policy ordering, strict input bounds, atomic output behavior and source conventions. Standard fixed-point, positional-game, Zielonka and component arguments are credited to their primary papers, academic notes and official tool documentation. Attribution is not endorsement.

Supplied graphs can omit real behavior or mislabel goals. There is no fairness assumption, dead-end totalization, stochastic/concurrent/partial-observation game, learned abstraction, temporal-logic compiler, deployed shield, strategy learning, scalable symbolic backend, new theory, machine-checked proof or real-agent guarantee. No paid API, private dataset or telemetry is used.
