# SynthLab: synthesis, teaching sets and adaptive queries

[Source](https://github.com/midya8/synthlab) · [Live inspector](https://midya8.github.io/synthlab/) · [Grammar and sources](https://github.com/midya8/synthlab/blob/main/CONTRACT.md)

## Finite program synthesis

SynthLab searches for tiny unsigned bit-vector expressions. A learner selects the cheapest expression fitting its known examples. A finite verifier checks the complete supplied target table and returns the first wrong input. The inspector shows every iteration, eliminated candidate, truth table and evaluation tree.

The grammar has constants 0/1, variables x/y and selected add/and/neg/not/xor operators. It supports 1..3-bit values and at most five AST nodes. Every terminal and operator node costs one, including repeated subtrees. This is a grammar-relative cost, not runtime or code size in another language. Bitwise complement differs from modular negation; a missing operator or too-small cost bound can exclude a solution without proving that no program exists.

The generator retains the minimum-cost, then ASCII-prefix-smallest expression for each full-domain output signature. This equivalence is safe for the declared pure, total, compositional operations. The frontier does not use the target values or known examples. A separate verifier enumerates every raw ordered grammar tree, without semantic pruning or calls to the generator's evaluator, frontier or text printer. It checks bounded completeness, canonical minimum cost and the full counterexample replay. Exhaustion proves absence only in the declared grammar and bound.

The original eight native tests include 512 Boolean target/grammar pairs and all 2,764 largest-grammar raw trees at each of three bit widths. Eighty complete Python/browser-engine reports match and independently verify. Actual Chrome checks 30 reports, 90 iterations, 903 candidate signatures and 3,420 expression probes at 320/390/1280, including export and stale-state clearing. Installed module/console reproduction runs outside the checkout.

## Correctness versus teaching

A correct candidate need not be the only function fitting the examples. The teaching inspector checks every input subset for representable 1..2-bit targets. It retains all minimum teaching sets, seed-preserving minima and row-deletion rival witnesses. A separate verifier uses direct disagreement-set intersections to check the complete atlas and the embedded raw-tree synthesis certificate.

The two-bit XOR control has 132 rival functions and 65,536 input subsets. CEGIS stops correctly with four examples but leaves three rivals. The atlas finds 182 four-row teaching sets. Equal example counts do not imply equal identifying power. The quantity is a target-specific teaching minimum, not class-wide teaching dimension or a generalization guarantee. Seed-preserving extensions and unrestricted minima are separate problems.

The teaching release added seven native tests and three Node/Chrome checks. Chrome checks 15 teaching reports, 1,203 subset selections and 597 rival selections. Installed module/console reproduction covers this certificate family too.

[Teaching inspector](https://midya8.github.io/synthlab/teaching.html) · [Teaching contract and sources](https://github.com/midya8/synthlab/blob/main/TEACHING.md)

## Exact adaptive identification

The adaptive inspector finds the minimum worst-case number of further input queries needed to identify any function fitting the initial observations. It checks every nonempty version space, every label partition, all minimax ties, a canonical policy and every possible target path. Initial observations are counted separately. The entire consistent class is retained, with a cap of ten functions; larger classes are rejected rather than trimmed to make the task easier.

A full seeded two-bit grammar leaves ten functions after two observations. Two further adaptive queries suffice. Every fixed passive separating set needs three rows. Immediate split balance is a different objective: complete balanced-policy tie choices require two or three further queries. The comparison includes the best and worst balanced tie resolutions, not one unlucky baseline tie.

Seven further native tests bring the current suite to 22; five further Node/Chrome checks bring it to twelve. Adaptive tests compare 541 complete native/JavaScript reports with independent verification. Chrome checks 15 adaptive reports, 1,583 version-space selections, 111 query partitions, 306 answer branches, 84 target traces and 105 passive-mask selections. Installed module/console reproduction covers all three certificate families outside checkout.

[Adaptive inspector](https://midya8.github.io/synthlab/adaptive.html) · [Adaptive contract and sources](https://github.com/midya8/synthlab/blob/main/ADAPTIVE.md)

## Boundaries and prior work

All targets and future query answers come from supplied finite tables, not a hidden service. Labels are exact and noiseless; queries have unit cost. There is no prior, expected-cost objective, PAC result, unknown-service guarantee, production-code benchmark or unbounded synthesis claim. Equivalent expressions are one semantic function, not distinct source programs. CLI certificates use strict parsing and atomic output. No API key, runtime dependency, private data or paid service is needed.

Classical CEGIS is credited to Solar-Lezama and colleagues. Grammar-guided enumeration, semantic equivalence, Goldman and Kearns's teaching-set/minimum-cover ideas and decision-tree dynamic programming are established work. SynthLab is an original bounded implementation and inspector, not SKETCH, cvc5, an e-graph implementation or a new algorithm.
