# BisimLab

Original finite agent-protocol equivalence inspector.


### BisimLab: same traces, different choices

[Source](https://github.com/midya8/bisimlab) · [Interactive inspector](https://midya8.github.io/bisimlab/) · [Method](https://github.com/midya8/bisimlab/blob/main/METHOD.md)

Finite agent-protocol equivalence from scratch: every strong-bisimulation refinement, every failed left/right step match, executable Hennessy-Milner witness DAGs, truth sets and a quotient graph. The default original control has equal finite trace languages but loses a choice after the same action; exact paired-subset BFS checks trace equality separately from branching equivalence. A native partition-signature checker never calls the generator, and independent JavaScript matches full reports. Nine native tests include all 512 three-state/one-action graphs against relation enumeration and 100 seeded graphs; three Node/actual-Chrome tests include 593 complete cross-engine reports and every control record at 320/390/1280. Installed-wheel checks cover both CLI entry points outside checkout. One to six states, all labels visible: no silent abstraction, probabilities, policy guarantee, source extraction, new algorithm or formal-proof claim. Established theory and seven inspected sources are attributed in the method.
