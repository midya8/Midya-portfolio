# CompileLab: one function, many shapes

**A canonical diagram still depends on its variable order. A projected model is not a sum of hidden completions.** CompileLab makes both distinctions inspectable in a tiny exact Boolean knowledge-compilation workbench.

[Workbench](https://midya8.github.io/compilelab/) · [Source](https://github.com/midya8/compilelab) · [Reviewed implementation](https://github.com/midya8/compilelab/pull/1) · [Exact contract](https://github.com/midya8/compilelab/blob/main/CONTRACT.md)

## One Boolean function, every order

The developed default is `(x0 iff x2) and (x1 iff x3)`. Its four full models have weighted mass 1/4 when every literal weighs 1/2. Across all 24 variable orders, the ordinary noncomplemented reduced ordered BDD has 6 to 9 reachable nonterminals. A five-variable multiplexer control spans 7 to 13 nonterminals over all 120 orders while retaining 16 full models and mass 1/2. Node sizes exclude terminals and are not timing or memory measurements.

Choose any order and see its actual graph, all complete assignment paths, every low-first full-tree reduction step and every reachable node's suffix count and mass. Equal children remove a redundant test; equal variable/low/high triples merge. Canonical means unique up to graph isomorphism for a fixed variable order, not across orders. Node IDs are deterministic presentation labels with separate spaces for original, conditioned and projected diagrams.

## Count the declared universe, not only the support

A declared variable that does not occur in the formula remains part of the original assignment space. A skipped Boolean variable contributes two choices to an unweighted count, but `(w_false + w_true)` to weighted mass. Every edge's audit includes gap variables between its test and child, and the root total includes variables skipped before the root. A terminal true represents one empty-suffix assignment, not one assignment over all remaining declared variables.

Conditioning pins the specified values and removes those variables from the free diagram universe. Its diagram mass excludes the pinned literals; the separately named full evidence-event mass includes them. Exact nonnegative rational arithmetic avoids silently rounding these distinctions. Zero-weight Boolean models remain logical models. Arbitrary literal weights need not be normalized and do not imply learned independence or calibrated probability.

## Existential projection is not arithmetic marginalization

For `x0 OR x1`, keep only x0. Assignment0 has one satisfying hidden completion, while assignment1 has two. There are three full models but two projected retained models. With every literal weighted 1/2, full mass is 3/4 while retained-only projected mass is 1. The two fiber completion masses are 1/4 and 1/2, while both projected retained masses are 1/2. These are different counting spaces, not inconsistent estimates.

Every retained row exposes all satisfying evidence-compatible full extensions, their weights, their count and the lexicographically first full witness. Full witness strings always follow x0..x(n-1), not the chosen BDD order. A zero-mass extension still establishes existential truth. Keep-empty, all-pinned, unsatisfied-evidence, no-model, empty-universe-true and empty-universe-false controls retain their exact meanings; an empty assignment is not no assignment.

## Separate construction, checking and reference

The native generator uses Shannon recursion, a unique triple table and graph dynamic programming. A separate checker imports strict input validation only. It enumerates CNF truth with bitmasks, groups residual truth vectors rather than calling the recursive builder, and directly enumerates suffix assignments for each node/edge mass instead of using the producer's recurrence. Every truth row, trace decision, graph, atlas tie, fiber, witness and summary is reconstructed. Canonical JSON comparison retains boolean/integer distinctions. This is independent implementation, not a formally verified theorem.

JavaScript is a separate row-partition implementation with BigInt rational arithmetic. Its browser replay regenerates with the same engine and is labeled accordingly. Downloads become independently checked only after the native CLI accepts them. A report verifies consistency with its embedded input, not input provenance or real-world suitability.

The optional actual BSD-licensed dd 0.6.0 library builds formulas from the input CNF rather than consuming our graph. It checks complete original/projected model sets, original/conditioned/projected counts and exact original/event/projected masses from its own models. Its complemented-edge representation has different structural size conventions, so raw node counts are intentionally not compared. No library code is vendored. The reference needs Python 3.11+; the dependency-free core supports Python 3.10+.

## Reproduced evidence

| Check | Observed result |
|---|---|
| Native suite | 15 tests; all 12 developed controls |
| Exhaustive tiny class | 512 subsets of nine clauses × four keep subsets = 2,048 configurations |
| Seeded native inputs | 180, independently replayed |
| Native/JavaScript | 102 complete reports; 90 nonterminals; 1,394 trace rows |
| Changed output leaves | All 719 primitive noninput forgeries rejected per engine |
| Actual dd 0.6.0 reference | 574 CNFs; 340 full models; 175 projected assignments; complete sets/counts and exact masses |
| Outside-checkout wheel | Five site-packages module origins; 12 controls × two entry points; 24 forged CLI failures |
| Actual Chrome | 48 views at 1440/768/390/320; 144 diagrams; 924 assignment paths; 128 fiber selections; 160 extension rows |
| Order interaction | Every one of the five-variable control's 120 orders selected and checked |
| Download replay | 12 trusted completed JSON downloads independently accepted by native CLI |

The exhaustive class includes the empty clause and all signed non-tautological clauses over two variables; it is not all syntactically possible CNFs. Seeded inputs use at most four variables; developed controls cover the five-variable boundary. Many random CNFs are constant, so the 90 cross-language nonterminals are not a large graph benchmark. No empirical generalization, learning, timing or real-agent claim.

## Publication

PR1 merged normally after all eight latest feature/PR jobs passed. Main `61e066efdc27714844d18cf2950f2d21151b9aab` preserves initial `aa20d89f55a2bbdd51bf3810d009eb8263241651` and complete feature `8e2815793cdedba74ad9ee2d8fd55962e6709b6c` history. All 30 native public files byte-match tested source. [Merged-main checks](https://github.com/midya8/compilelab/actions/runs/42929615678) and [Pages](https://github.com/midya8/compilelab/actions/runs/42929615697) passed. Six deployed assets match source bytes. The complete deployed Chrome workflow passes all 48 views, 144 graphs, 924 assignment paths, 128 fibers, 160 extension rows, 120 boundary orders and 12 independently replayed downloads. All 64 unmasked local/live captures are pixel-identical. Actual desktop hero, phone zero-mass verdicts and narrow boundary graph inspected. Showcase publication remains a separate gate before the overall portfolio update is complete.

## Scope and prior work

At most five variables, ten clauses, ten signed literals per clause, exact nonnegative rational literal weights with numerator/denominator at most 1,000 and full permutation atlas at most 120 orders. Ordinary noncomplemented ROBDDs only. No dynamic-order heuristic, general d-DNNF compiler, arbitrary symbolic-scale guarantee, formal proof, probability calibration, new Boolean algorithm or real-agent benchmark.

[Bryant 1986](https://www.cs.cmu.edu/~bryant/pubdir/ieeetc86.pdf) grounds ordered reduction, fixed-order canonicity and order sensitivity. [Darwiche/Marquis 2002](https://www.cs.cmu.edu/afs/cs/project/jair/pub/volume17/darwiche02a.pdf) places Boolean decision diagrams within AI knowledge compilation and its query/size tradeoffs. [Bryant/Tan/Heule 2025](https://www.cs.cmu.edu/~bryant/pubdir/sat25.pdf) already certifies projected compilation with formally verified checkers; this bounded replay does not claim those guarantees. Official [dd documentation](https://github.com/tulip-control/dd/blob/main/doc.md), [implementation](https://github.com/tulip-control/dd/blob/main/dd/autoref.py) and [README](https://github.com/tulip-control/dd/blob/main/README.md) establish actual library semantics. [Northeastern weighted-inference material](https://www.khoury.northeastern.edu/home/sholtzen/assets/teaching/CS7480-23-slides/lec-7.pdf), [Berkeley Boolean-function lectures](https://people.eecs.berkeley.edu/~keutzer/classes/244fa2005/lectures/12-1-BooleanFunctions.pdf) and [TU Graz BDD notes](https://www.isec.tugraz.at/wp-content/uploads/2020/07/mc08-bdds.pdf) support literal-product sums, cofactors and existential OR abstraction. Full dated/source-type ledger in source SOURCES.md.

Existing FactorLab studies dense-factor elimination order and mixed sum/max inference; ProvLab studies relational provenance. CompileLab instead audits reduced Boolean graph structure, skipped-variable counting universes and existential-extension fibers. Classical theory, original bounded implementation and controls, not a claim to invent knowledge compilation.
