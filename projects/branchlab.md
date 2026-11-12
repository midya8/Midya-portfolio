# BranchLab

Inspect small supplied graphs under ordinary and explicit fair-path CTL. The path convention is visible, and every answer has replayable finite-model evidence. The current suite has 29 Python and seven Node/actual-Chrome tests.

## BranchLab: always possible is not inevitable

[Live workbench](https://midya8.github.io/branchlab/) | [Source](https://github.com/midya8/branchlab) | [Method and limits](https://github.com/midya8/branchlab/blob/main/METHOD.md)

Check a CTL formula on a supplied state graph, then inspect the evidence. In the opening model, `AG EF p` holds while `AF p` fails: a goal remains reachable everywhere, but an infinite wait is still allowed. This original mode uses ordinary infinite paths. The separate fair-path mode below uses explicit justice sets instead.

Twelve original controls separate nested path quantifiers, different existential witnesses, strong-until failure, time-zero success and finite versus lasso counterexamples. Python and browser JavaScript expose every unique subformula's truth set, synchronous least/greatest rounds, all-state obligations and the complete `2^n` subset-image atlas. A native checker derives truth by enumerating all fixed points and reconstructs every typed certificate field. It separately enumerates finite prefixes and first-repeat lassos. One trace is shown only when it is valid evidence for the selected claim; other claims require branching certificates.

The original 15 Python tests remain in the current 29-test suite. They cover all 144 two-state graph/labelling cases and a direct path/lasso oracle on 2,744 three-state cases. The optional pyModelChecking 1.3.4 ordinary comparison agrees on 212 requests and 3,630 subformula truth sets. Complete browser/native records agree on 276 requests. Actual Chrome checks 36 control/width reports, 192 subformulas, 558 state selections, 237 rounds, 1,110 subset rows and 12 completed exports replayed natively. Fresh installed-wheel checks run both CLI entry points outside the checkout, replay all 12 ordinary controls, check five module origins and reject 20 forged CLI reports.

Bounds are one to six total states, four atomic propositions and eight formula roots. Strong until includes time zero. No fairness, probability, action or controller is inferred in this mode. This is classical bounded CTL, not symbolic scale, LTL/CTL*, verified AI agents or new theory. Runtime needs no paid API or external package. The optional GPL test reference is separate and is not vendored; the method credits established theory and inspected sources.

## BranchLab 0.2: a fair path must meet them all

[Fair-path inspector](https://midya8.github.io/branchlab/fair.html) | [Source](https://github.com/midya8/branchlab) | [Exact convention and sources](https://github.com/midya8/branchlab/blob/main/FAIRNESS.md)

A path must meet every supplied justice set infinitely often on the same execution. The fair-CTL inspector compares ordinary and fair truth at every subformula. Inspect each induced region, recurrent component, justice intersection, backward round and replayable finite-prefix/closed-walk witness. The four-state opening control needs the repeated walk `s0 → s1 → s0 → s2 → s0` to meet both justice sets. Neither first simple cycle is enough. A trap can retain a local atom while having no fair continuation.

The current suite passes 29 Python and seven Node/actual-Chrome tests, retaining the original ordinary workflows. Native Tarjan generation, a separate Boolean-closure/recurrent-subset checker and a browser Kosaraju engine agree on 278 full reports: 2,808 regions, 4,135 subformulas and 2,643 fair lassos. All 519 changed non-input primitive leaves of one certificate are rejected. The optional NetworkX 3.4.2 comparison checks those regions, 4,632 components and all lassos as a graph reference, not a full fair-CTL oracle. The pyModelChecking ordinary comparison remains separate. Three pinned-version counterexamples explain why its fairness route is excluded.

Actual Chrome checks 36 fair reports at 1280/390/320 pixels: 216 regions, 612 region/start selections, 465 subformula selections, 390 witness rows and 2,628 graph edges. Twelve trusted completed downloads are replayed by the native checker. Fresh installed wheels retain the ordinary checks, add nine module-origin checks, replay 12 fair controls through both entry points, and reject 24 forged CLI reports with atomic output preservation plus 24 direct forgeries. These are fixture coverage counts, not a proof or speed benchmark.

Bounds are one to six total states and zero to four state-based justice sets. Atoms and Boolean operators remain local; temporal operators quantify over fair paths. Universal truth without a fair continuation is displayed as vacuous, not progress. Fair EG restricts to the operand region before testing recurrence: intersecting ordinary EG with globally fair states is unsound. An empty justice set excludes every path; no justice constraints recovers ordinary CTL.

These are generalized-Buchi execution assumptions, not strong/compassion fairness or an implemented scheduler. The engines share a written contract and strict schema; the checker also reuses separately implemented ordinary-CTL replay. Sources use different Boolean conventions, so the chosen convention and contrast are documented rather than blended. No new theory, scalable symbolic solver or real-agent safety/liveness guarantee is claimed.
