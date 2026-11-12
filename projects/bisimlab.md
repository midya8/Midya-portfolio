# BisimLab

Compare small protocol models under strong bisimulation, exact finite traces, hidden-action semantics and divergence-preserving branching. Inspect the evidence for each answer. The current suite has 32 Python and 12 Node/actual-Chrome tests; earlier counts below describe their release stages, not separate current totals.

### BisimLab: same traces, different choices

[Source](https://github.com/midya8/bisimlab) · [Interactive inspector](https://midya8.github.io/bisimlab/) · [Method](https://github.com/midya8/bisimlab/blob/main/METHOD.md)

Two states can allow the same finite action sequences but disagree about when a choice remains available. The original inspector shows every strong-bisimulation refinement, failed left/right step match, distinguishing Hennessy-Milner formula, truth set and quotient edge. A separate paired-subset search checks finite trace equality, rather than sampling paths.

The original nine Python tests remain in the current suite. They include all 512 three-state/one-action graphs against relation enumeration and 100 seeded graphs. The original three Node/actual-Chrome tests compare 593 complete reports and every control record at 320/390/1280 pixels. A native partition-signature checker replays reports without calling the generator; installed checks run both CLI entry points outside the checkout.

All labels are visible in this original mode, even a label named `tau`. Hidden-action modes have separate contracts below. The supplied model has one to six states; state names are not observations. No probabilities, source extraction, policy guarantee, new algorithm or formal proof. Established theory and inspected sources are credited in the method.

### BisimLab: complete trace-product replay

[Interactive trace product](https://midya8.github.io/bisimlab/traces.html) · [Source and exact semantics](https://github.com/midya8/bisimlab/blob/main/TRACES.md)

For a pair of states, inspect the entire reachable product of their possible successor sets. The graph keeps every action edge after a mismatch, including the both-empty sink. BFS discovery words, layers, mismatch nodes and a shortest distinguishing path remain visible. Equal finite traces still do not imply branching equivalence.

The v0.2 checks compare 4,715 complete reports across Python bitmasks, independent JavaScript sets and a separate explicit-subset checker. Its 17 Python tests include all earlier tests, exhaustive unary three-state graphs across every ordered pair, direct word enumeration, seeded cases and forged closure/provenance rejection. Six Node/actual-Chrome tests include all earlier browser checks, every control record, export and stale-result clearing at 320/390/1280 pixels. Installed checks replay six original and seven trace controls through two entry points and check six import origins.

This mode uses one to six states with all actions visible. Exact subset exploration is exponential within that cap, not a scalable solver. The contract credits subset determinisation and product language equivalence; it makes no new-algorithm claim.

## BisimLab: silence can hide a choice

[Silent-action inspector](https://midya8.github.io/bisimlab/silent.html) · [Exact contract](https://github.com/midya8/bisimlab/blob/main/SILENT.md) · [Reviewed change](https://github.com/midya8/bisimlab/pull/3)

Explicitly hiding labels can produce different answers under strong, branching and weak bisimilarity. Inspect each fixed-point round, removed pair, attack and finite response path. Branching matching preserves the choice at the matched step; weak matching may lose it. The default contrast reconstructs and credits Bisping Example 6.3.

This v0.3 mode is divergence-insensitive and unrooted. Its separate silent-cycle witnesses do not turn it into a divergence-preserving check: a silent loop and a deadlock may still be equivalent. No termination, fairness, liveness or deployed-agent guarantee follows. The separate v0.4 mode below checks a different divergence obligation.

Historical v0.3 coverage includes 23 Python and nine Node/Chrome tests, retaining earlier checks. Independent generation, path/set replay and candidate-relation oracles agree with JavaScript on 1,154 reports: 8,461 rounds, 4,014 removed pairs and 8,166 response records. The optional unmodified mCRL2 ltscompare 202507.0 comparison covers 350 systems and 5,652 pair-semantics comparisons. Installed checks replay six base, seven trace and ten silent controls through four entry points, check eight module origins and reject 20 forgeries.

Actual Chrome checks 30 silent reports at 320/390/1280 pixels, 294 rounds, 498 removed-pair selections, 960 attacks, 414 responses and ten native-verified downloads, plus 18-loop graph geometry. These are fixture coverage counts, not a proof or speed benchmark.

## BisimLab 0.4: the loop must stay inside

[Explicit-divergence inspector](https://midya8.github.io/bisimlab/divergence.html) · [Source](https://github.com/midya8/bisimlab) · [Exact contract and sources](https://github.com/midya8/bisimlab/blob/main/DIVERGENCE.md) · [Reviewed change](https://github.com/midya8/bisimlab/pull/4)

Both states can loop forever and still disagree about where the loop is possible. This mode compares ordinary branching equivalence with unrooted divergence-preserving branching equivalence. It enumerates every set partition and retains each state's internal reachability, exit signatures, nonempty-cycle lassos and failed same-block obligations. These are exhaustive candidates, not fixed-point rounds.

The six-state opening control reconstructs and credits Luttik 2020 Example 3/Figure 1. Both states are globally divergent, but only one can diverge while staying in the class where the visible action remains available. A global cycle flag misses the distinction. Earlier strong, trace and divergence-insensitive modes keep their separate meanings.

The current suite passes 32 Python and 12 Node/Chrome tests. A simple-path/block-insertion verifier has no generator imports; a separate relational attack/response oracle uses matrix cycle closure. All 220 declared non-input primitive-leaf mutations are rejected. Python/JavaScript agree on 1,157 complete reports containing 8,720 partitions, 37,743 state records and 19,346 failures. The pinned unmodified mCRL2 comparison covers 353 systems and 3,672 unordered-pair/semantics comparisons, not every witness field. A fresh isolated wheel retains all prior controls and entry points, adds 13 divergence controls through two new entry points, checks three new module origins and rejects 26 forgeries.

Actual Chrome checks 39 reports at 1280/390/320 pixels, 843 candidate selections, 4,467 state rows, 2,955 failure rows and 13 trusted completed downloads verified by the native checker. The v0.4 release also checked 47 complete unmasked visual states after deployment. Wide exact tables scroll inside the page.

Bounds are one to six states, zero to three labels, 18 unique edges and at most 203 partitions. A report checks only the supplied finite model, not its correspondence to a program. Shared theory, schema and canonicalization remain common assumptions. This is bounded educational model checking, not a new algorithm, scalable engine, learned model, benchmark, formal proof or real-agent safety/liveness guarantee.
