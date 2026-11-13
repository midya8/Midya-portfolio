# STRIPSLab: real plans, relaxed plans and action availability

[Live inspector](https://midya8.github.io/stripslab/) · [Source](https://github.com/midya8/stripslab) · [Method and sources](https://github.com/midya8/stripslab/blob/main/METHOD.md) · [Merged implementation](https://github.com/midya8/stripslab/pull/1)

## What it checks

STRIPSLab compares real and delete-relaxed plans in a fully disclosed state space: zero to six Boolean facts, positive initial/goal/precondition sets, and at most eight positional unit-cost actions. Each action has add and delete sets. The real successor deletes then adds; the relaxed successor only adds. Facts absent from a state are false, not unknown.

The export retains every one of the 2^m states, including unreachable states. Each state retains every blocked/applicable action, missing preconditions, actual added/removed facts, real/relaxed successors, exact remaining goal distances, all shortest suffix choices, decimal-string sequence counts and one representative replay. Initial-state reachability is reported separately. Initial optimal-plan edges retain every shortest tie, not one favorable path.

## Where the approximation fails

- A shared effect achieves two goals in one real action, while h-add counts it twice.
- A consumable resource permits either goal but not both. The relaxed graph finds a plan; the real graph has no plan.
- A restoration action makes the real optimum three steps versus two relaxed steps.
- Independent goals expose h-max's lower estimate, while independent action orders retain six shortest sequences.
- Empty goals, zero facts, duplicate action identities, no-ops, cyclic prerequisites, reachable traps and a six-fact chain test boundaries.

Synchronous h-max and h-add fact-cost propagation retains every round, the final unchanged round and all tied best fact achievers. Exact h-plus comes from the full relaxed state graph, not either propagation estimate. Local achiever ties are not claimed to be complete relaxed plans.

## Reproduce the results

The original Python implementation uses bitsets and reverse BFS. Independently written JavaScript uses sets and all-state Bellman sweeps. Native reference tests use set transitions, Floyd-Warshall, bounded walk counting at the independently determined shortest length and a recursive derivation-tree cost oracle. A different JavaScript seeded task bank compares whole reports. Chrome checks every retained UI record across all fourteen tasks, controls, export and invalid-input clearing at 320/390/1280 widths.

The current suite has 17 Python tests and 9 Node/Chrome tests across all three modes. The isolated installed wheel reproduces 14 base, 15 search and 18 availability reports, checks five installed module origins and runs both CLI entry points in all three modes. Fresh source checkouts pass the native, browser and installed-package checks. The original base release had eight Python tests and three Node/Chrome tests.

## Scope and prior work

Established STRIPS and heuristic-planning theory, with original bounded implementations and synthetic tasks. No PDDL parsing or grounding, negative preconditions, conditional effects, non-unit costs, concurrency, probabilistic outcomes, partial observability, safety guarantee, scalable-planner or benchmark-win claim. Seven inspected sources, including Bonet/Geffner, Haslum/Geffner, planning textbooks/course notes and planner documentation, are attributed in METHOD.md with source coverage and implementation differences. No planner code or published benchmark is copied.


## Search: a suboptimal h-add plan

[Inspect four complete search runs](https://midya8.github.io/stripslab/search.html) · [Search policy and reproducible evidence](https://github.com/midya8/stripslab/blob/main/SEARCH.md)

The A*/best-first inspector exposes every selected frontier, strict cost improvement, applicable action decision and returned plan. A controlled task returns cost 3 with h-add versus exact cost 2 under the disclosed tie and goal-pop policy. Zero, h-max and exact h-plus return cost 2. Includes admissibility/consistency diagnostics, unsolvable exhaustion, strict CLI certificates, an independently implemented browser engine, and a separate synthetic reopening test. Full-state precomputation is explicit: this is a bounded audit, not a planner speedup or new algorithm claim.


## Action availability: used does not mean necessary

[Live action-availability inspector](https://midya8.github.io/stripslab/sensitivity.html) | [Exact source and policy](https://github.com/midya8/stripslab/blob/main/SENSITIVITY.md)

Disable every static action subset. Keep every exact counterfactual distance, shortest-plan count, original action ID, representative and optimal edge. Separate an action used by one representative from one required by every optimal plan or every valid plan. Retain all inclusion-minimal sufficient sets and all solvability/optimality cuts, with independently checked minimal-hitting-set duals.

The original duplicate-shortcut control leaves a longer detour when both shortcuts are removed: optimality fails before solvability does. Eighteen controls retain 466 scenarios, 21,731 state rows and 408 optimal edges. Python BFS and independent JavaScript distance sweeps agree on 118 complete reports covering 2,515 scenarios; independent native set-transition and all-proper-subset oracles cover another 80 seeded tasks. Seventeen native tests, nine Node/Chrome tests and 47 isolated installed reports preserve all earlier modes. Browser checks every retained scenario at 320/390/1280.

Six facts/eight unit-cost grounded actions maximum. Static deterministic re-planning, not failure probabilities, timed outages, a scalable landmark extractor, real-world reliability or a new algorithm. [Implementation, boundaries and inspected sources](https://github.com/midya8/stripslab/blob/main/SENSITIVITY.md).
