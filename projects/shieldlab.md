# ShieldLab



### ShieldLab: a safe next step can still lose

[Source](https://github.com/midya8/shieldlab) | [Interactive inspector](https://midya8.github.io/shieldlab/) | [Exact method and seven-source ledger](https://github.com/midya8/shieldlab/blob/main/METHOD.md)

An exact tiny safety-game inspector for hand-written agent protocols. Every synchronous fixed-point obligation, winning controller move, losing rank and branching invariant/counterstrategy graph is visible. Changing only who controls a state flips the result: one-step-safe actions need not preserve safety forever. Independent bitmask Python and explicit-set JavaScript, plus a separate dual-attractor and exhaustive positional-policy checker.

Eight native tests include all 21,952 three-state graph/ownership/safety combinations and 150 seeded larger arenas. Three Node/actual-Chrome tests compare 643 complete reports and all six controls at 320/390/1280. Installed wheels replay both CLI entry points outside checkout. Finite total perfect-information model only: no runtime shield, LLM guarantee, liveness, timing, probability, new algorithm or formal proof. Dead ends are rejected; safe waiting need not mean progress.

## Why inspect the full game?

The fast action reaches a currently safe pending state, but the environment can force a leak on its next turn. Review stays in a closed safe region. Flip pending to controller ownership with no other graph change, and fast becomes winning. The inspector exposes both quantifiers and every round rather than presenting a single attractive trajectory.

Winning proof graphs fix a controller policy and retain every environment move. Losing proof graphs fix a rank-decreasing environment counterpolicy and retain every controller move, stopping at unsafe states. Ranks bound forced failure; canonical first choices are not promised optimal. A five-step forced chain, safe environment cycle, indefinite waiting and already-unsafe root make the boundaries explicit.

[PR and complete implementation history](https://github.com/midya8/shieldlab/pull/1). Original code and controls, dependency-free native runtime, no model API or private dataset. The method records standard safety-game theory, a conflicting dead-end convention, shielding abstraction requirements and the limits of this small model. Tests are evidence rather than proof.
