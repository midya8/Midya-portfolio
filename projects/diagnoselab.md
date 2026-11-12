# Diagnoselab: consistency repairs and their consequences

[Live inspector](https://midya8.github.io/diagnoselab/) · [Source](https://github.com/midya8/diagnoselab) · [Full method and attributed sources](https://github.com/midya8/diagnoselab/blob/main/METHOD.md)

Diagnoselab checks which removable clauses restore consistency to a small propositional formula, then asks what follows under the selected repairs. The consistency and query inspectors answer different questions. Both use exact arithmetic and retain the counterexamples and search traces behind the result.

## Finding every minimal repair

Given fixed hard CNF and removable soft clauses, enumerate every relative minimal unsatisfiable subset (MUS) and every minimal correction set (MCS). A repair must hit every core, not merely one. Inclusion-minimal does not mean minimum cardinality or minimum cost. The default control contrasts one removal at cost 5 with two removals costing 2. Inconsistent hard background gives an empty relative core and no soft repair.

## What the consistency inspector shows

- Original dependency-free Python implementation and separate BigInt JavaScript implementation, exact rational arithmetic.
- All soft subsets, separate exhaustive truth-table models and deterministic DPLL search traces. Every node retains partial assignments, first-unit reasons, residual clauses, satisfied IDs, branches, conflict IDs and model completion.
- All MUS member-deletion model lists; all MCS reinsertion UNSAT references and unique-hit core witnesses.
- Every candidate's intersections with both families, checking minimal-hitting-set duality in both directions, including empty-family/empty-core boundaries.
- Every cardinality/cost tie and both deletion-order runs. Duplicate identities, tautologies, empty clauses and unused variables remain explicit.
- Editable local browser input, complete report export and stale/invalid clearing.

## Consistency checks

The original consistency workflow has 17 Python test functions, retained in the current suite of 24. CI covers Python 3.10, 3.11, 3.12 and 3.13. Independent checks include 180 all-proper-subset family oracles, 80 complete-trace controls, positive-cost scaling, clause permutation, literal order/repetition and variable complementation, validation/no mutation and invalid CLI output preservation.

Four original Node/actual-Chrome tests, retained in the current suite of eight, compare all 18 retained reports on 74,292 exact scalar leaves and add 90 independent truth-mask controls. Actual browser inspection covers 827 subset outcomes, 1,301 complete DPLL node records, 20 cores, 52 repairs, 304 truth rows, all family/duality/truth/subset tables, every selected repair and node record, export and 320/390/1280 containment. An isolated installed wheel reproduces all 18 reports outside the checkout, checks the four original module origins and compares console/module CLI output. The consequence extension adds a fifth module origin and 26 reports to that installed check. These system counts are not test-function counts or performance measurements.

## Limits

Six Boolean variables, at most eight hard and eight removable clauses. All subsets and assignments are enumerated. This is established DPLL and MUS/MCS theory with attributed sources, not a novel/scalable SAT or MaxSAT algorithm. No external solver code or dataset copied. Synthetic clauses are supplied assumptions, not verified facts. Costs are supplied removal preferences, not failure probabilities. Restored consistency is not causal or physical diagnosis and establishes no real-world action is safe. Search traces are tested computational witnesses, not DRAT/LRAT exports or machine-checked proofs. Native/browser JSON parser differences are documented in the method. No paid service, model or API.

Original implementation, independent checks and synthetic controls: Midya Rahmani.

## Consequences under each repair policy

[Live query inspector](https://midya8.github.io/diagnoselab/consequences.html) · [Method/sources](https://github.com/midya8/diagnoselab/blob/main/CONSEQUENCES.md)

The query inspector distinguishes every/some repair from every/some surviving model, with all tied minimum-cost/cardinality policies, complete countermodels and negated-query DPLL traces. Shared-clause intersection is a separate baseline with strict counterexamples. No-repair families are inapplicable, not vacuous certainty. 26 consequence reports (16,165 scalar leaves), 67 repairs, 78 policy records and 151 full DPLL nodes including intersection baselines; 24 Python/eight Node-Chrome tests preserve all originals. Installed-wheel reproduction and mobile/table/export checks. Finite propositional reasoning, not a database/DL engine or probability claim.

Query inspection adds a distinct reasoning task after consistency restoration. Every-repair entailment can differ from both possible-in-every-repair and intersection-baseline entailment. Original two- and three-way controls expose these gaps. Every repaired formula retains full truth-table query witnesses and the full deterministic search tree of the formula conjoined with query negation. Empty and tautological queries, duplicated literals, hard inconsistency and tied policy families have explicit controls. Chrome checks 78 policy records, 67 repairs, 70 selectable per-repair search nodes, 462 literal rows, complete policy JSON (including intersection search trees), all tables/export/stale/invalid clearing at 320/390/1280. Native independent replay covers all 151 nodes. Four additional inspected sources are attributed in the linked method, with exact limits. No claim of formal certification, real fault diagnosis, scalable solver or novelty.
