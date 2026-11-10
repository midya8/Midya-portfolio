# ConceptLab case study


## ConceptLab: exact concepts and implication witnesses

[Live inspector](https://midya8.github.io/conceptlab/) | [Source](https://github.com/midya8/conceptlab) | [Method and prior work](https://github.com/midya8/conceptlab/blob/main/METHOD.md)

A bounded knowledge-representation workbench for formal concept analysis. Independent Python and JavaScript enumerate every formal concept, cover, meet/join, attribute closure and object derivation. Inspect canonical implications, pseudo-intent decisions, NextClosure pivots, forward rule traces and rule-removal countermodels. Every implication query retains supporting and counterexample rows; an empty premise extent means vacuous validity and null confidence, not evidence.

Fourteen original controls include duplicate rows, zero support, empty universes, strict joins, nonminimal pseudo-intents and multi-rule closure. The retained suite covers 194 attribute subsets, 390 object subsets, 69 concepts, 30 canonical rules, 635 ordered lattice operations and 5,762 implication queries. Independent set-based checks cover all 689 contexts with zero to three objects/attributes plus 100 seeded larger contexts per engine. Native CLI, installed wheel and actual-Chrome checks accompany the interactive inspector.

Finite exact teaching/audit tool: at most six attributes and eight objects. Not learned prediction, fuzzy concept analysis, noisy-data inference, causality or a scalable mining system. Existing FCA theory and software are attributed; no new algorithm is claimed.

## Reproduction

Run `python -m unittest discover -s tests -v`, `npm test` and `bash tools/wheel_smoke.sh` from the source checkout. The wheel check runs outside the checkout, verifies all retained reports and installed module origins, and checks the console and module CLI. Python 3.10 through 3.13 are checked in CI. The browser checks every retained query, witness and report, JSON export, invalid-input clearing and 320/390/1280 layouts.

The method documents formulas, set conventions, input limits, implementation differences and prior sources. Zero-object and zero-attribute contexts explicitly extend the ordinary set formulas beyond texts that assume nonempty universes.


### ConceptLab incomplete-context completions

[Live completion inspector](https://midya8.github.io/conceptlab/partial.html) | [Semantics and sources](https://github.com/midya8/conceptlab/blob/main/PARTIAL.md)

Unknown is not false. Enumerate every compatible binary completion of a three-valued table. Inspect certain, contingent and impossible implications, all object counterexamples, exact defined row-confidence bounds and endpoint ties, with zero-support completions kept separate. Intersect goals in one shared completion and retain every inclusion-minimal impossible goal set with deletion witnesses.

Original controls expose two traps: both extreme fill-ins can pass while an intermediate world refutes an implication, and separately possible goals can be jointly impossible. Overlapping-premise tautologies, empty universes, duplicate objects and all 64 worlds of six unknowns remain explicit. Twelve controls cover 86 completions, 438 implication queries, 4,634 query/completion witness rows and 63 goal subsets.

Independent Python and JavaScript engines, 17 native tests on four Python versions, six Node/Chrome tests and 26 installed-wheel reports preserve the complete-context workbench. Every retained UI record, export and invalid-input clearing is checked; all controls are layout-tested at 320/390/1280. Limits: four attributes, four objects, six unknown cells. Completion counts are not probabilities; confidence bounds describe supplied rows, not unseen data. No imputation, causal claim, graded possibility model, incomplete-context basis or new algorithm is claimed.


### ConceptLab: a table is not an expert

[Live exact-expert exploration](https://midya8.github.io/conceptlab/exploration.html) | [Source](https://github.com/midya8/conceptlab) | [Protocol and inspected foundations](https://github.com/midya8/conceptlab/blob/main/EXPLORATION.md) | [Merged PR #3](https://github.com/midya8/conceptlab/pull/3)

An implication can fit every observed row and still fail in the supplied domain. This finite attribute-exploration simulator asks the strongest observed implication for a premise, retains every expert-table counterexample, reveals the lowest-ID refutation and retries the same premise. Accepted implications change the next lectic pivot; every seed, earlier-coordinate disagreement and derivation round remains inspectable. The expert is an explicitly supplied complete table, not a human or language model. Vacuous validity is not evidence about the world.

- A separate set-based Python checker reconstructs theory closure by intersecting all satisfying models, checks each pivot against exhaustive lectic successors, and checks the canonical basis through an independent recursive pseudo-intent characterization. It does not call either generator. The final audit compares accepted-knowledge, full-expert and final-observed closures for every attribute subset, with support IDs and all missing-attribute counterexamples. Some rows can remain unseen without losing the supplied table's implication theory.
- Fresh feature/main reproduction passes 24 native tests on Python 3.10/3.11/3.12/3.13 and all eleven Node/Chrome tests. All 6,654 small expert-family/initial-observation combinations are checked; Python and JavaScript agree across 6,966 reports and 64,658 events. The installed 0.3.0 wheel runs both entry points outside the checkout for fourteen complete-context, twelve partial-context and twelve exploration controls, with forged-export rejection.
- Optional concepts 0.9.2 agrees on 175,003 support/closure checks. It does not validate scheduling; 88 empty-axis requests are excluded from that package comparison and remain tested internally. Actual deployed Chrome checks 36 exploration reports at 1280/390/320, 273 events, 204 pivots, 294 premise obligations, 702 displayed derivation rounds and twelve downloaded exports accepted by the independent Python CLI. Both earlier inspectors pass their full behavior checks.
- All fifty native/fresh feature/main files and fourteen deployed assets plus root match exactly. Feature/PR/main CI and Pages are green. Forty new-inspector plus 21 targeted original-inspector/accepted-pivot screenshots match unmasked in feature/main and main/live comparisons. Phone rejection, narrow-phone lectic evidence, desktop accepted implication and both prior inspectors' new links were visually inspected.

Five attributes, eight supplied objects. Twelve original synthetic controls include repeated rejection, implication chains, empty contexts, unsupported premises, duplicate row identities and sufficient-but-not-exhaustive observations. Published FCA, NextClosure and attribute-exploration theory are credited; no new algorithm, minimum-question claim, live human expert, background theory, partial/noisy expert, statistical generalization or production scalability claim. Previous complete and partial inspectors are preserved.
