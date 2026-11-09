# More AI portfolio projects

[Full project index](README.md)


## ConceptLab: exact concepts and implication witnesses

[Live inspector](https://midya8.github.io/conceptlab/) | [Source](https://github.com/midya8/conceptlab) | [Method and prior work](https://github.com/midya8/conceptlab/blob/main/METHOD.md)

A bounded knowledge-representation workbench for formal concept analysis. Independent Python and JavaScript enumerate every formal concept, cover, meet/join, attribute closure and object derivation. Inspect canonical implications, pseudo-intent decisions, NextClosure pivots, forward rule traces and rule-removal countermodels. Every implication query retains supporting and counterexample rows; an empty premise extent means vacuous validity and null confidence, not evidence.

Fourteen original controls include duplicate rows, zero support, empty universes, strict joins, nonminimal pseudo-intents and multi-rule closure. The retained suite covers 194 attribute subsets, 390 object subsets, 69 concepts, 30 canonical rules, 635 ordered lattice operations and 5,762 implication queries. Independent set-based checks cover all 689 contexts with zero to three objects/attributes plus 100 seeded larger contexts per engine. Native CLI, installed wheel and actual-Chrome checks accompany the interactive inspector.

Finite exact teaching/audit tool: at most six attributes and eight objects. Not learned prediction, fuzzy concept analysis, noisy-data inference, causality or a scalable mining system. Existing FCA theory and software are attributed; no new algorithm is claimed.

[ConceptLab case study](conceptlab.md)


### ConceptLab incomplete-context completions

[Live completion inspector](https://midya8.github.io/conceptlab/partial.html) | [Semantics and sources](https://github.com/midya8/conceptlab/blob/main/PARTIAL.md)

Unknown is not false. Enumerate every compatible binary completion of a three-valued table. Inspect certain, contingent and impossible implications, all object counterexamples, exact defined row-confidence bounds and endpoint ties, with zero-support completions kept separate. Intersect goals in one shared completion and retain every inclusion-minimal impossible goal set with deletion witnesses.

Original controls expose two traps: both extreme fill-ins can pass while an intermediate world refutes an implication, and separately possible goals can be jointly impossible. Overlapping-premise tautologies, empty universes, duplicate objects and all 64 worlds of six unknowns remain explicit. Twelve controls cover 86 completions, 438 implication queries, 4,634 query/completion witness rows and 63 goal subsets.

Independent Python and JavaScript engines, 17 native tests on four Python versions, six Node/Chrome tests and 26 installed-wheel reports preserve the complete-context workbench. Every retained UI record, export and invalid-input clearing is checked; all controls are layout-tested at 320/390/1280. Limits: four attributes, four objects, six unknown cells. Completion counts are not probabilities; confidence bounds describe supplied rows, not unseen data. No imputation, causal claim, graded possibility model, incomplete-context basis or new algorithm is claimed.


### STRIPSLab exact planning and relaxation witnesses

[Live inspector](https://midya8.github.io/stripslab/) · [Source](https://github.com/midya8/stripslab) · [Method and prior work](https://github.com/midya8/stripslab/blob/main/METHOD.md)

An original bounded classical-AI planning lab: audit every state and every blocked/applicable action, compare exact real and delete-relaxed shortest-plan families, and inspect h-max/h-add fixed-point rounds and tied fact achievers. Strict controls expose shared-effect double counting, relaxed solvability hiding real dead ends, restoration costs, all shortest-order ties and unreachable cyclic prerequisites. Python bitsets/reverse BFS and independent JavaScript sets/Bellman sweeps reproduce the same complete reports.

Six facts, eight grounded positive-precondition unit-cost actions. No PDDL parser, real-world execution, scalable-planner claim or new planning algorithm. Fourteen original synthetic tasks; eight Python tests, three Node/Chrome tests and isolated wheel reproduction of all fourteen full reports. Established STRIPS and heuristic-planning work is attributed with inspected-source limits.

[STRIPSLab case study](https://github.com/midya8/Midya-portfolio/blob/main/projects/stripslab.md)
