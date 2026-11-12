# ConceptLab

ConceptLab inspects the concepts and implication rules of small object-attribute tables. Python integer masks and browser JavaScript sets compute independent reports. Three modes separate a complete table, explicit unknown cells and observations checked against a supplied expert table. No model, API or private data is used.

| Question | Inspector | Method |
| --- | --- | --- |
| Which concepts and implications hold in a complete table? | [Binary context](https://midya8.github.io/conceptlab/) | [Definitions and sources](https://github.com/midya8/conceptlab/blob/main/METHOD.md) |
| What can change when unknown cells are filled in? | [Completions](https://midya8.github.io/conceptlab/partial.html) | [Completion semantics](https://github.com/midya8/conceptlab/blob/main/PARTIAL.md) |
| Which observed rules survive counterexamples from the supplied domain? | [Attribute exploration](https://midya8.github.io/conceptlab/exploration.html) | [Exploration protocol](https://github.com/midya8/conceptlab/blob/main/EXPLORATION.md) |

[Source](https://github.com/midya8/conceptlab)

## Complete contexts

Inspect every attribute closure, object derivation, formal concept, cover and pairwise meet/join. Pseudo-intent decisions, canonical implications, forward-rule traces, rule-removal countermodels and NextClosure pivots retain their intermediate records. A join can contain more objects than the raw union. A pseudo-intent need not be a minimal nonclosed set.

Implication queries list every supporting and counterexample row. An empty premise extent gives vacuous validity and null confidence, not evidence. Missing incidence is false in this mode; it is not an unknown cell. The canonical-basis theorem concerns minimum implication count, not minimum total premise/conclusion literal count.

Fourteen synthetic controls include duplicate rows, empty universes, unsupported premises, strict joins and multi-rule closure. Independent set checks cover all 689 contexts with zero to three objects and attributes, plus seeded larger contexts. The method retains individual query, lattice and witness counts. Limits are six attributes and eight objects.

## Unknown-cell completions

Enumerate every compatible binary completion of a 0/1/null table. An implication can be certain, contingent or impossible. Confidence endpoints retain all ties, while undefined zero-support completions stay separate. Goals share one completion: separately possible goals can be jointly impossible. Every inclusion-minimal impossible goal set retains its one-goal-deletion witnesses.

Controls show why checking only the all-false and all-true fill-ins is insufficient. Twelve controls include all 64 worlds of six unknown cells, overlapping-premise tautologies, duplicate objects and empty universes. Python and JavaScript compare complete reports against independent exhaustive references. Limits are four attributes, four objects, six unknown cells and four goals. Completion counts are not probabilities, and confidence bounds do not estimate unseen data.

## Attribute exploration

An implication can fit every observed row and still fail in the supplied domain. The simulator asks the strongest observed implication for a premise, retains every expert-table counterexample, reveals the lowest-ID refutation and retries that premise. Accepted implications change the next lectic pivot. Every seed, earlier-coordinate disagreement and derivation round remains inspectable.

A separate Python checker reconstructs theory closure by intersecting all satisfying models, checks pivots against exhaustive lectic successors and checks the canonical basis through an independent recursive pseudo-intent characterization. It does not call either generator. The final audit compares accepted-knowledge, full-expert and final-observed closure for every attribute subset. Some rows can stay unseen without losing the supplied table's implication theory.

Twelve controls include repeated rejection, implication chains, unsupported premises, duplicate row identities and sufficient-but-not-exhaustive observations. Exhaustive small inputs and seeded inputs are compared across both engines. Limits are five attributes and eight supplied objects. This is a simulated exact expert, not a human, language model or claim about external domain truth.

## Reproduce and check

From a checkout, using Python 3.10+:

```sh
git clone https://github.com/midya8/conceptlab.git
cd conceptlab
python -m venv .venv
. .venv/bin/activate
python -m pip install .
python -m conceptlab examples/demo.json -o audit.json
python -m conceptlab --partial examples/partial.json -o completions.json
python -m conceptlab --exploration examples/exploration.json -o exploration.json
python -m conceptlab --verify-exploration exploration.json
python -m unittest discover -s tests -v
npm test
sh tools/wheel_smoke.sh
```

The Node tests need Node 22+ and Chrome/Chromium. The wheel script also needs uv. It installs into a temporary environment and runs outside the checkout, checks all six module origins, reproduces the complete/partial/exploration controls through both entry points and rejects altered exploration reports through both verifier entry points.

The documentation review reran all 24 Python tests and eleven Node/actual-Chrome tests on fresh baseline, revised, published and merged source. Hosted CI checks Python 3.10 through 3.13. Deployed Chrome tests exercise all three inspectors at 320/390/1280, compare displayed records with native reports, replay exploration downloads through the independent verifier and check that invalid edits clear stale results and disable export.

The exploration method records the earlier optional concepts 0.9.2 comparison, including its empty-axis exclusions. That historical comparison was not rerun for this documentation review and does not validate the exploration scheduler.

## Scope and prior work

This implements established formal concept analysis, NextClosure and attribute exploration. The method files credit the inspected research, teaching and software sources and state what was implemented independently. No external FCA code, datasets, examples, benchmarks or optimized algorithms were copied. No affiliation with the credited projects is claimed.

These are bounded teaching and audit tools, not new algorithms, scalable mining systems, learned predictions, missing-data estimates or causal evidence. No fuzzy/noisy expert, live human expert, background theory, minimum-question guarantee or statistical generalization is claimed. Zero-object and zero-attribute contexts explicitly extend the set formulas beyond texts that assume nonempty universes.
