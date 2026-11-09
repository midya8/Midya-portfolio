# STRIPSLab: the price of ignoring delete effects

[Live inspector](https://midya8.github.io/stripslab/) · [Source](https://github.com/midya8/stripslab) · [Method and sources](https://github.com/midya8/stripslab/blob/main/METHOD.md) · [Merged implementation](https://github.com/midya8/stripslab/pull/1)

## What the lab audits

Classical AI planning with a tiny, fully disclosed state space: zero to six Boolean facts, positive initial/goal/precondition sets, and at most eight positional unit-cost actions. Each action has add and delete sets. The real successor deletes then adds; the relaxed successor only adds. Facts absent from a state are false, not unknown.

The export retains every one of the 2^m states, including unreachable states. Each state retains every blocked/applicable action, missing preconditions, actual added/removed facts, real/relaxed successors, exact remaining goal distances, all shortest suffix choices, decimal-string sequence counts and one representative replay. Initial-state reachability is reported separately. Initial optimal-plan edges retain every shortest tie, not one favorable path.

## Where the approximation fails

- A shared effect achieves two goals in one real action, while h-add counts it twice.
- A consumable resource permits either goal but not both. The relaxed graph finds a plan; the real graph has no plan.
- A restoration action makes the real optimum three steps versus two relaxed steps.
- Independent goals expose h-max's lower estimate, while independent action orders retain six shortest sequences.
- Empty goals, zero facts, duplicate action identities, no-ops, cyclic prerequisites, reachable traps and a six-fact chain test boundaries.

Synchronous h-max and h-add fact-cost propagation retains every round, the final unchanged round and all tied best fact achievers. Exact h-plus comes from the full relaxed state graph, not either propagation estimate. Local achiever ties are not claimed to be complete relaxed plans.

## Reproducibility

The original Python implementation uses bitsets and reverse BFS. Independently written JavaScript uses sets and all-state Bellman sweeps. Native reference tests use set transitions, Floyd-Warshall, bounded walk counting at the independently determined shortest length and a recursive derivation-tree cost oracle. A different JavaScript seeded task bank compares whole reports. Chrome checks every retained UI record across all fourteen tasks, controls, export and invalid-input clearing at 320/390/1280 widths.

Eight native tests pass on Python 3.10, 3.11, 3.12 and 3.13. Three Node/Chrome tests pass. A built wheel installed outside the checkout reproduces all fourteen reports, verifies three imported module origins and runs both CLI entry points. The fresh public checkout also passes native, browser and installed-package checks.

## Scope and prior work

Established STRIPS and heuristic-planning theory, with original bounded implementations and synthetic tasks. No PDDL parsing or grounding, negative preconditions, conditional effects, non-unit costs, concurrency, probabilistic outcomes, partial observability, safety guarantee, scalable-planner or benchmark-win claim. Seven inspected sources, including Bonet/Geffner, Haslum/Geffner, planning textbooks/course notes and planner documentation, are attributed in METHOD.md with source coverage and implementation differences. No planner code or published benchmark is copied.
