# DFALab: active learning, bounded conformance and finite faults

[Live inspector](https://midya8.github.io/dfalab/) | [Repository](https://github.com/midya8/dfalab) | [Contract and sources](https://github.com/midya8/dfalab/blob/main/CONTRACT.md)

## Three questions

DFALab learns a minimal deterministic finite automaton from a supplied finite teacher using Dana Angluin's L* algorithm. Replay each membership query, observation-table repair, conjecture and shortest counterexample. Separate inspectors build a bounded W-method conformance suite and find its best test subsets within a tiny, fully enumerated fault domain.

A closed and consistent table can still propose the wrong language. Passing a finite suite can still hide a fault outside its state bound. Removing redundant tests does not by itself prove a minimum suite. Each inspector keeps the evidence for its own claim separate.

## Learning from a finite teacher

An original implementation of Dana Angluin's classic L* learner asks globally cached membership queries, repairs observation-table closure and consistency, and processes all prefixes of each exact counterexample. Every cell, teacher-side query path, repair witness and conjecture is replayable. Each equivalence query includes the complete reachable target/hypothesis product, all outputs and all edges. Its first mismatch is a shortest shortlex counterexample. No mismatch proves all-word language equivalence for the supplied finite teacher.

The final DFA has shortest access words and a shortest distinguishing suffix for every state pair, proving reachable-state minimality. This does not prove minimum query count. Native Python and browser JavaScript generate matching reports. An independent native verifier replays the whole certificate without calling the generators, using separate shortest-access fixed points. A separate pair-marking oracle checks language equivalence and minimal state counts.

## Use the learning inspector

Choose a synthetic teacher or edit up to six states and three letters. Replay every table, query, repair, hypothesis, product graph and final pair distinction. Try words against the learned machine or export an offline-checkable certificate. The standard even/even parity language is attributed to Angluin; other fixtures cover delayed acceptance, unreachable accepting states, nonzero starts and multiple counterexamples.

## Learning checks

The original eight native learning tests are retained in the current suite of eighteen. CI runs Python 3.10-3.13. Learning checks include all 17,496 three-state binary teachers, all 648 three-state unary teachers and all 128 two-state binary teachers, with every start and accepting set. Seeded larger teachers, disabled-generator verification, forged reports and strict atomic CLI caps add separate checks. The original four learning Node/Chrome checks compare 189 complete reports and replay 93 table selections, 45 conjectures and 411 new-query rows over 320/390/1280 pixels. Installed module/console generation and verification reproduce all nine controls outside checkout.

## Scope and attribution

These are complete deterministic finite synthetic teachers, not real-world protocol benchmarks, noisy observations, timed automata or unknown services. Exact equivalence is available because the target DFA is supplied. Random testing cannot inherit that guarantee. Acceptance concerns the whole word, not a safety promise for every prefix. L* and its theoretical guarantees belong to Angluin (1987); no algorithmic novelty, query-efficiency win or industrial scalability is claimed. No model, paid API or private data is needed.

MIT licensed. Full references, certificate semantics and reproduction commands are in the contract.

## Bounded conformance

[Live W-method inspector](https://midya8.github.io/dfalab/conformance.html) | [Construction, assumptions and sources](https://github.com/midya8/dfalab/blob/main/CONFORMANCE.md) | [Source](https://github.com/midya8/dfalab)

The classic DFA W-method inspector shows every state-cover word, middle word, distinguishing suffix, canonical factor and acceptance path. It separates four claims: finite suite agreement, the supplied candidate's reachable-state bound, a bounded equivalence certificate and a separate exact graph audit. A faulty extra-state candidate passes when its bound is understated; increasing the bound exposes the fault. Tests do not infer a hidden service's state count.

An independent verifier reconstructs all factor combinations and checks every output and witness without calling the generator. Six added native tests include 52,488 exhaustive reference/candidate cases; 131 full native/browser-engine reports are cross-checked. Actual Chrome audits 3,444 test selections and 141 probes across eleven controls and three widths. At this stage the suite had fourteen native tests, seven Node/Chrome checks and installed two-family reproduction. The current suite retains these checks and adds the fault-atlas checks below. The original L* learning page and schema are preserved. These are synthetic fixture checks, not production-protocol benchmarks or a new theorem. The method is credited to Vasilevskii and Chow; the precise DFA theorem and reset/state-bound assumptions are documented.

## Finite fault atlas

[Live fault atlas](https://midya8.github.io/dfalab/fault-atlas.html) | [Exact domain, cost and sources](https://github.com/midya8/dfalab/blob/main/FAULT_ATLAS.md) | [Source](https://github.com/midya8/dfalab)

Enumerate every complete labeled implementation in a tiny unary/binary state domain, distinguish equivalent survivors from real faults, and inspect every acceptance-matrix row. Every subset of the constructed W-suite is checked under test-count then letter-count cost. All minima, escaping faults and chosen-test deletion witnesses are retained. Irredundancy is not confused with minimum cardinality; label/unreachable-state duplicates are not counted as unique languages or bug frequencies.

An independent native verifier reconstructs the complete machine domain and every subset result. Tests cover all 60 tiny minimal references with a separate equivalence oracle. Eleven complete cross-engine atlas reports match; actual Chrome audits 6,996 candidate selections and 804 subset selections across eight controls and three widths. All eighteen native checks on four Python versions, ten Node/Chrome checks and installed three-family reproduction preserve active learning and bounded conformance. Optimization is restricted to subsets of the generated W-suite, not globally shortest tests or real-world protocol coverage. Classic W-method and set-cover ideas are explicitly credited.
