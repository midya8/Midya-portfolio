# CompileLab

CompileLab builds small reduced ordered binary decision diagrams and shows how variable order changes their shape. A separate projection view lists the hidden completions behind each retained assignment, keeping logical existence distinct from summed mass.

[Workbench](https://midya8.github.io/compilelab/) · [Source](https://github.com/midya8/compilelab) · [Reviewed implementation](https://github.com/midya8/compilelab/pull/1) · [Exact contract](https://github.com/midya8/compilelab/blob/main/CONTRACT.md)

## One Boolean function, every order

The default control is `(x0 iff x2) and (x1 iff x3)`. Its four full models have weighted mass 1/4 when every literal weighs 1/2. Across all 24 variable orders, the ordinary noncomplemented reduced ordered BDD has 6 to 9 reachable nonterminals. A five-variable multiplexer control spans 7 to 13 nonterminals over all 120 orders while retaining 16 full models and mass 1/2. Node sizes exclude terminals and are not timing or memory measurements.

Choose any order and see its actual graph, all complete assignment paths, every low-first full-tree reduction step and every reachable node's suffix count and mass. Equal children remove a redundant test; equal variable/low/high triples merge. Canonical means unique up to graph isomorphism for a fixed variable order, not across orders. Node IDs are deterministic presentation labels with separate spaces for original, conditioned and projected diagrams.

## Count the declared universe, not only the support

A declared variable that does not occur in the formula remains part of the original assignment space. A skipped Boolean variable contributes two choices to an unweighted count, but `(w_false + w_true)` to weighted mass. Every edge's audit includes gap variables between its test and child, and the root total includes variables skipped before the root. A terminal true represents one empty-suffix assignment, not one assignment over all remaining declared variables.

Conditioning pins the specified values and removes those variables from the free diagram universe. Its diagram mass excludes the pinned literals; the separately named full evidence-event mass includes them. Exact nonnegative rational arithmetic avoids silently rounding these distinctions. Zero-weight Boolean models remain logical models. Arbitrary literal weights need not be normalized and do not imply learned independence or calibrated probability.

## Existential projection is not arithmetic marginalization

For `x0 OR x1`, keep only x0. Retained assignment 0 has one satisfying hidden completion, while retained assignment 1 has two. There are three full models but two projected retained models. With every literal weighted 1/2, full mass is 3/4 while retained-only projected mass is 1. The two fiber completion masses are 1/4 and 1/2, while both projected retained masses are 1/2. These are different counting spaces, not inconsistent estimates.

Every retained row exposes all satisfying evidence-compatible full extensions, their weights, their count and the lexicographically first full witness. Full witness strings always follow x0..x(n-1), not the chosen BDD order. A zero-mass extension still establishes existential truth. Keep-empty, all-pinned, unsatisfied-evidence, no-model, empty-universe-true and empty-universe-false controls retain their exact meanings; an empty assignment is not no assignment.

## Separate construction, checking and reference

The native generator uses Shannon recursion, a unique triple table and graph dynamic programming. A separate checker imports strict input validation only. It enumerates CNF truth with bitmasks, groups residual truth vectors rather than calling the recursive builder, and directly enumerates suffix assignments for each node/edge mass instead of using the producer's recurrence. Every truth row, trace decision, graph, atlas tie, fiber, witness and summary is reconstructed. Canonical JSON comparison retains boolean/integer distinctions. This is independent implementation, not a formally verified theorem.

JavaScript is a separate row-partition implementation with BigInt rational arithmetic. Its browser replay regenerates with the same engine and is labeled accordingly. Downloads become independently checked only after the native CLI accepts them. A report verifies consistency with its embedded input, not input provenance or real-world suitability.

The optional actual BSD-licensed dd 0.6.0 library builds formulas from the input CNF rather than consuming our graph. It checks complete original/projected model sets, original/conditioned/projected counts and exact original/event/projected masses from its own models. Its complemented-edge representation has different structural size conventions, so raw node counts are intentionally not compared. No library code is vendored. The reference needs Python 3.11+; the dependency-free core supports Python 3.10+.

## Reproduce and check

From a source checkout, using Python 3.10+:

```sh
git clone https://github.com/midya8/compilelab.git
cd compilelab
python -m venv .venv
. .venv/bin/activate
python -m pip install .
python -m compilelab docs/example.json --output evidence.json
python -m compilelab evidence.json --verify
python -m unittest discover -s tests -v
python -m tools.check_assets
python -m tools.check_installed
npm test
```

The Node tests need Node 22+ and Chrome. The wheel check installs into a temporary
environment, checks module origins, then reproduces all twelve controls through
both entry points outside the checkout. Altered reports must fail verification.
The optional dd comparison needs a separate Python 3.11+ environment and
`dd==0.6.0`; it is not a core dependency.

Native tests cover the exhaustive two-variable clause/keep class, seeded inputs,
complete cross-language reports and altered outputs. The exhaustive class includes
the empty clause and signed non-tautological clauses; it is not all syntactically
possible CNFs. Seeded inputs use at most four variables, while developed controls
cover the five-variable boundary. Many random CNFs are constant. These are bounded
checks, not a large-graph benchmark or a claim about learning or generalization.

Actual Chrome checks compare displayed graphs, assignment paths, projection
extensions and order atlases with native reports at four widths. They select all
120 orders of the five-variable control and replay completed downloads through
native Python. Invalid edits must clear stale results and disable export.

The original [evidence ledger](https://github.com/midya8/compilelab/blob/main/EVIDENCE.md)
retains the individual test counts and optional historical reference results.
The documentation batch reran the core, browser, installed and deployed checks;
it did not rerun the optional dd comparison. No empirical learning, timing or
real-agent claim follows from these fixtures.

## Scope and prior work

At most five variables, ten clauses, ten signed literals per clause, exact nonnegative rational literal weights with numerator/denominator at most 1,000 and full permutation atlas at most 120 orders. Ordinary noncomplemented ROBDDs only. No dynamic-order heuristic, general d-DNNF compiler, arbitrary symbolic-scale guarantee, formal proof, probability calibration, new Boolean algorithm or real-agent benchmark.

[Bryant 1986](https://www.cs.cmu.edu/~bryant/pubdir/ieeetc86.pdf) grounds ordered reduction, fixed-order canonicity and order sensitivity. [Darwiche/Marquis 2002](https://www.cs.cmu.edu/afs/cs/project/jair/pub/volume17/darwiche02a.pdf) places Boolean decision diagrams within AI knowledge compilation and its query/size tradeoffs. [Bryant/Tan/Heule 2025](https://www.cs.cmu.edu/~bryant/pubdir/sat25.pdf) already certifies projected compilation with formally verified checkers; this bounded replay does not claim those guarantees. Official [dd documentation](https://github.com/tulip-control/dd/blob/main/doc.md), [implementation](https://github.com/tulip-control/dd/blob/main/dd/autoref.py) and [README](https://github.com/tulip-control/dd/blob/main/README.md) establish actual library semantics. [Northeastern weighted-inference material](https://www.khoury.northeastern.edu/home/sholtzen/assets/teaching/CS7480-23-slides/lec-7.pdf), [Berkeley Boolean-function lectures](https://people.eecs.berkeley.edu/~keutzer/classes/244fa2005/lectures/12-1-BooleanFunctions.pdf) and [TU Graz BDD notes](https://www.isec.tugraz.at/wp-content/uploads/2020/07/mc08-bdds.pdf) support literal-product sums, cofactors and existential OR abstraction. Full dated/source-type ledger in source SOURCES.md.

Existing FactorLab studies dense-factor elimination order and mixed sum/max inference; ProvLab studies relational provenance. CompileLab instead audits reduced Boolean graph structure, skipped-variable counting universes and existential-extension fibers. Classical theory, original bounded implementation and controls, not a claim to invent knowledge compilation.
