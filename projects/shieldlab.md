# ShieldLab



### ShieldLab: a safe next step can still lose

[Source](https://github.com/midya8/shieldlab) | [Interactive inspector](https://midya8.github.io/shieldlab/) | [Exact method and seven-source ledger](https://github.com/midya8/shieldlab/blob/main/METHOD.md)

An exact tiny safety-game inspector for hand-written agent protocols. Every synchronous fixed-point obligation, winning controller move, losing rank and branching invariant/counterstrategy graph is visible. Changing only who controls a state flips the result: one-step-safe actions need not preserve safety forever. Independent bitmask Python and explicit-set JavaScript, plus a separate dual-attractor and exhaustive positional-policy checker.

Eight native tests include all 21,952 three-state graph/ownership/safety combinations and 150 seeded larger arenas. Three Node/actual-Chrome tests compare 643 complete reports and all six controls at 320/390/1280. Installed wheels replay both CLI entry points outside checkout. Finite total perfect-information model only: no runtime shield, LLM guarantee, liveness, timing, probability, new algorithm or formal proof. Dead ends are rejected; safe waiting need not mean progress.

## Why inspect the full game?

The fast action reaches a currently safe pending state, but the environment can force a leak on its next turn. Review stays in a closed safe region. Flip pending to controller ownership with no other graph change, and fast becomes winning. The inspector exposes both quantifiers and every round rather than presenting a single attractive trajectory.

Winning proof graphs fix a controller policy and retain every environment move. Losing proof graphs fix a rank-decreasing environment counterpolicy and retain every controller move, stopping at unsafe states. Ranks bound forced failure; canonical first choices are not promised optimal. A five-step forced chain, safe environment cycle, indefinite waiting and already-unsafe root make the boundaries explicit.

[PR and complete implementation history](https://github.com/midya8/shieldlab/pull/1). Original code and controls, dependency-free native runtime, no model API or private dataset. The method records standard safety-game theory, a conflicting dead-end convention, shielding abstraction requirements and the limits of this small model. Tests are evidence rather than proof.

## ShieldLab: safe waiting is not arrival

ShieldLab now separates safe waiting from forced arrival. A finite reach-before-unsafe inspector exposes every synchronous attractor obligation, exact minimum worst-case first-goal bound and complete ranked strategy or target-avoiding counterstrategy. Every original move and every positional controller assignment remains inspectable: a winning successor can still stall, while a slower fixed policy can still win. [Live first-goal inspector](https://midya8.github.io/shieldlab/reachavoid.html), [source and reproduction](https://github.com/midya8/shieldlab), [contract and eight-source ledger](https://github.com/midya8/shieldlab/blob/main/REACHAVOID.md), [reviewed change](https://github.com/midya8/shieldlab/pull/2).

All 24 native tests pass on Python 3.10-3.13, preserving all 8 original tests. Independent deterministic strategy-pair simulation checks 324 two-state and 32,928 three-state cases; 120 seeded larger cases and the 729-policy boundary have full replay. All six Node/Chrome tests pass, including 457 complete native/JavaScript reports, 1,329 policies and 6,291 root outcomes. Actual Chrome drills every policy/root across 12 controls at 320/390/1280 and verifies 12 event-confirmed downloaded reports through the native CLI. Fresh installed wheels on each Python version reproduce 6 original and 12 new reports through two entrypoints, check 8 module origins and reject 20 forged CLI records. Feature/PR, main and Pages checks are green; all 38 native files match fresh public source and deployed assets/behavior/pixels are verified.

Terminal safe goals stop the play on first hit; empty targets lose and unsafe roots fail immediately. No fairness assumption forces the environment to cooperate. Safety-until-goal treats success as absorbing and is not necessarily the original nonterminal infinite-safety objective. Complete assignments include unreachable active controller decisions but exclude irrelevant goal/unsafe actions. The original safety engine, checker, controls and tests keep their semantics. Established finite-game theory and original bounded controls are credited, not presented as a new theorem, external-solver benchmark, scalable solver, learned runtime shield, probabilistic guarantee or proof about real software.
