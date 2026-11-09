# Diagnoselab: all conflicts, all minimal repairs

[Live inspector](https://midya8.github.io/diagnoselab/) · [Source](https://github.com/midya8/diagnoselab) · [Full method and attributed sources](https://github.com/midya8/diagnoselab/blob/main/METHOD.md)

## Why one conflict is not enough

Given fixed hard CNF and removable soft clauses, enumerate every relative minimal unsatisfiable subset (MUS) and every minimal correction set (MCS). A repair must hit every core, not merely one. Inclusion-minimal does not mean minimum cardinality or minimum cost. The default control contrasts one removal at cost 5 with two removals costing 2. Inconsistent hard background gives an empty relative core and no soft repair.

## Inspectable evidence

- Original dependency-free Python implementation and separate BigInt JavaScript implementation, exact rational arithmetic.
- All soft subsets, separate exhaustive truth-table models and deterministic DPLL search traces. Every node retains partial assignments, first-unit reasons, residual clauses, satisfied IDs, branches, conflict IDs and model completion.
- All MUS member-deletion model lists; all MCS reinsertion UNSAT references and unique-hit core witnesses.
- Every candidate's intersections with both families, checking minimal-hitting-set duality in both directions, including empty-family/empty-core boundaries.
- Every cardinality/cost tie and both deletion-order runs. Duplicate identities, tautologies, empty clauses and unused variables remain explicit.
- Editable local browser input, complete report export and stale/invalid clearing.

## Checks actually run

17 Python test functions on Python 3.10, 3.11, 3.12 and 3.13. Independent checks include 180 all-proper-subset family oracles, 80 complete-trace controls, positive-cost scaling, clause permutation, literal order/repetition and variable complementation, validation/no mutation and invalid CLI output preservation.

Four Node/actual-Chrome tests compare all 18 retained reports on 74,292 exact scalar leaves and add 90 independent truth-mask controls. Actual browser inspection covers 827 subset outcomes, 1,301 complete DPLL node records, 20 cores, 52 repairs, 304 truth rows, all family/duality/truth/subset tables, every selected repair and node record, export and 320/390/1280 containment. An isolated installed wheel reproduces all 18 reports outside the checkout, verifies four module origins and compares console/module CLI output. These system counts are not test-function counts or performance measurements.

## Honest scope

Six Boolean variables, at most eight hard and eight removable clauses. All subsets and assignments are enumerated. This is established DPLL and MUS/MCS theory with attributed sources, not a novel/scalable SAT or MaxSAT algorithm. No external solver code or dataset copied. Synthetic clauses are supplied assumptions, not verified facts. Costs are supplied removal preferences, not failure probabilities. Restored consistency is not causal or physical diagnosis and establishes no real-world action is safe. Search traces are tested computational witnesses, not DRAT/LRAT exports or machine-checked proofs. Native/browser JSON parser differences are documented in the method. No paid service, model or API.

Original implementation, independent checks and synthetic controls: Midya Rahmani.
