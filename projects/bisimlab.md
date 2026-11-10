# BisimLab

Original finite agent-protocol equivalence inspector.


### BisimLab: same traces, different choices

[Source](https://github.com/midya8/bisimlab) · [Interactive inspector](https://midya8.github.io/bisimlab/) · [Method](https://github.com/midya8/bisimlab/blob/main/METHOD.md)

Finite agent-protocol equivalence from scratch: every strong-bisimulation refinement, every failed left/right step match, executable Hennessy-Milner witness DAGs, truth sets and a quotient graph. The default original control has equal finite trace languages but loses a choice after the same action; exact paired-subset BFS checks trace equality separately from branching equivalence. A native partition-signature checker never calls the generator, and independent JavaScript matches full reports. Nine native tests include all 512 three-state/one-action graphs against relation enumeration and 100 seeded graphs; three Node/actual-Chrome tests include 593 complete cross-engine reports and every control record at 320/390/1280. Installed-wheel checks cover both CLI entry points outside checkout. One to six states, all labels visible: no silent abstraction, probabilities, policy guarantee, source extraction, new algorithm or formal-proof claim. Established theory and seven inspected sources are attributed in the method.


### BisimLab: complete trace-product replay

[Interactive trace product](https://midya8.github.io/bisimlab/traces.html) | [Source and exact semantics](https://github.com/midya8/bisimlab/blob/main/TRACES.md)

The second inspector retains the entire reachable product of two states' possible successor sets, including every action edge after a mismatch and the both-empty sink. Inspect canonical BFS discovery words, layers, all possibility-mismatch nodes and a shortest distinguishing path. Equal finite traces still do not imply branching equivalence.

Python bitmasks, independent JavaScript sets and a separate native checker based on explicit subset tables agree on 4,715 trace reports. Seventeen native tests include exhaustive unary three-state graphs across every ordered pair, direct word enumeration, seeded multi-action cases and forged closure/provenance checks. Six Node/actual-Chrome tests cover every control record, export and invalid-input clearing at 320/390/1280px. Installed-wheel checks cover six original and seven trace controls, two CLI entry points and six import origins. One to six states, all actions visible; exponential and bounded, with no silent actions, model/API dependency, scalable-solver or new-algorithm claim. Established subset determinisation and product language equivalence are attributed in the source ledger.


## BisimLab: silence can hide a choice

[Live silent-action inspector](https://midya8.github.io/bisimlab/silent.html) · [Source and exact contract](https://github.com/midya8/bisimlab/blob/main/SILENT.md) · [Reviewed change](https://github.com/midya8/bisimlab/pull/3)

Explicit hiding exposes three different answers: strong, branching and weak bisimilarity. This bounded inspector records every fixed-point round, removed pair, attack and canonical finite response skeleton, including the before-step requirement that weak matching can lose. Silent reachability and possible-divergence cycle witnesses are separate: no rooted or divergence-preserving semantics, fairness, liveness or deployed-agent guarantee is claimed. The default contrast reconstructs Bisping Example6.3 and is credited, not claimed as new.

Independent BFS generation, DFS/set replay and candidate-relation test oracles; full native/JS agreement on1,154 reports with8,461 rounds,4,014 removed pairs and8,166 response records. Optional unmodified mCRL2 ltscompare202507.0 agrees on350 systems/5,652 comparisons. All23 native tests pass on3.10-3.13, all9 Node/Chrome tests pass, and an installed wheel reproduces6 base/7 trace/10 silent controls outside the checkout through four entrypoints, checks eight module origins and rejects20 forged reports. Actual Chrome checks30 silent reports at320/390/1280,294 rounds,498 removed-pair selections,960 attacks,414 response records and10 independently verified downloads, plus18-loop graph geometry. These are bounded coverage counts, not a proof or speed benchmark.


## BisimLab0.4: the loop must stay inside

Two protocol states can both loop forever and still disagree about *where* that loop is possible. The new [explicit-divergence inspector](https://midya8.github.io/bisimlab/divergence.html) compares ordinary branching equivalence with unrooted divergence-preserving branching equivalence. It enumerates every set partition of a supplied finite protocol, retains every state's internal reachability, complete exit signatures, canonical nonempty-cycle lassos and every failed same-block obligation, then checks the coarsest valid partition explicitly. Earlier strong/modal, trace-product and divergence-insensitive workflows remain separate and unchanged.

The opening six-state example reconstructs and credits Luttik2020 Example3/Figure1. Both states are globally divergent, yet only one can diverge while staying in the class where the visible action remains available. A global cycle flag would miss the distinction. This is established theory, not a newly invented counterexample.

Independent checks include a simple-path/block-insertion verifier without generator imports, a direct relational attack/response oracle with matrix cycle closure, 220 individually rejected non-input leaf mutations, and 1,157 complete Python/JavaScript atlases containing 8,720 partitions, 37,743 state records and 19,346 failure records. Actual unmodified pinned mCRL2 agrees on 353 frameworks / 3,672 unordered-pair-semantics comparisons. All 32 Python tests and 12 Node/Chrome tests pass. A fresh isolated wheel retains all prior controls/entrypoints and reproduces 13 new controls through both new entrypoints, checks three new module origins and rejects 26 forged reports.

Actual Chrome checks 39 control-width reports at 1280/390/320, all 843 candidate selections, 4,467 state rows, 2,955 failure rows and 13 trusted completed JSON downloads verified by the native checker. Forty-seven complete unmasked visual states match the reviewed implementation after deployment. Wide exact tables deliberately scroll horizontally inside the page.

Bounds: 1..6 states, 0..3 labels and 18 unique edges, at most 203 partitions. This is exact bounded educational model checking, not a scalable verification engine, learned model, benchmark, formal proof or agent safety/liveness guarantee. A report certifies only the supplied finite model, not its correspondence to a program. Shared theory/schema/canonicalization remain common assumptions.

[Live inspector](https://midya8.github.io/bisimlab/divergence.html) · [Source](https://github.com/midya8/bisimlab) · [Exact contract and inspected foundations](https://github.com/midya8/bisimlab/blob/main/DIVERGENCE.md) · [Pull request](https://github.com/midya8/bisimlab/pull/4)
