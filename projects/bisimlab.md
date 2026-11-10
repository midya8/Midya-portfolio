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
