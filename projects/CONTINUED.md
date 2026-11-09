# More AI portfolio projects

[Full project index](README.md)


## ConceptLab: exact concepts and implication witnesses

[Live inspector](https://midya8.github.io/conceptlab/) | [Source](https://github.com/midya8/conceptlab) | [Method and prior work](https://github.com/midya8/conceptlab/blob/main/METHOD.md)

A bounded knowledge-representation workbench for formal concept analysis. Independent Python and JavaScript enumerate every formal concept, cover, meet/join, attribute closure and object derivation. Inspect canonical implications, pseudo-intent decisions, NextClosure pivots, forward rule traces and rule-removal countermodels. Every implication query retains supporting and counterexample rows; an empty premise extent means vacuous validity and null confidence, not evidence.

Fourteen original controls include duplicate rows, zero support, empty universes, strict joins, nonminimal pseudo-intents and multi-rule closure. The retained suite covers 194 attribute subsets, 390 object subsets, 69 concepts, 30 canonical rules, 635 ordered lattice operations and 5,762 implication queries. Independent set-based checks cover all 689 contexts with zero to three objects/attributes plus 100 seeded larger contexts per engine. Native CLI, installed wheel and actual-Chrome checks accompany the interactive inspector.

Finite exact teaching/audit tool: at most six attributes and eight objects. Not learned prediction, fuzzy concept analysis, noisy-data inference, causality or a scalable mining system. Existing FCA theory and software are attributed; no new algorithm is claimed.

[ConceptLab case study](conceptlab.md)
