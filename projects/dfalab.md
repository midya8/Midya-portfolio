# DFALab: learn the missing distinction

[Live inspector](https://midya8.github.io/dfalab/) | [Repository](https://github.com/midya8/dfalab) | [Contract and sources](https://github.com/midya8/dfalab/blob/main/CONTRACT.md)

## The problem

A finite sample can make two protocol states look identical. A closed and consistent observation table can still propose the wrong language. What experiment distinguishes the states, and what evidence justifies stopping?

## The implementation

An original implementation of Dana Angluin's classic L* learner asks globally cached membership queries, repairs observation-table closure and consistency, and processes all prefixes of each exact counterexample. Every cell, teacher-side query path, repair witness and conjecture is replayable. Each equivalence query includes the complete reachable target/hypothesis product, all outputs and all edges. Its first mismatch is a shortest shortlex counterexample. No mismatch proves all-word language equivalence for the supplied finite teacher.

The final DFA has shortest access words and a shortest distinguishing suffix for every state pair, proving reachable-state minimality. This does not prove minimum query count. Native Python and browser JavaScript generate matching reports. An independent native verifier replays the whole certificate without calling the generators, using separate shortest-access fixed points. A separate pair-marking oracle checks language equivalence and minimal state counts.

## Working inspector

Choose a synthetic teacher or edit up to six states and three letters. Replay every table, query, repair, hypothesis, product graph and final pair distinction. Try words against the learned machine or export an offline-checkable certificate. The standard even/even parity language is attributed to Angluin; other fixtures cover delayed acceptance, unreachable accepting states, nonzero starts and multiple counterexamples.

## Validation

Eight native tests run on Python 3.10-3.13, including all 17,496 three-state binary teachers, all 648 three-state unary teachers and all 128 two-state binary teachers, with every start and accepting set. Seeded larger teachers, disabled-generator verification, forged reports and strict atomic CLI caps add separate checks. Four Node/Chrome tests compare 189 complete reports and replay 93 table selections, 45 conjectures and 411 new-query rows over 320/390/1280 pixels. Installed module/console generation and verification reproduce all nine controls outside checkout.

## Honest scope

These are complete deterministic finite synthetic teachers, not real-world protocol benchmarks, noisy observations, timed automata or unknown services. Exact equivalence is available because the target DFA is supplied. Random testing cannot inherit that guarantee. Acceptance concerns the whole word, not a safety promise for every prefix. L* and its theoretical guarantees belong to Angluin (1987); no algorithmic novelty, query-efficiency win or industrial scalability is claimed. No model, paid API or private data is needed.

MIT licensed. Full references, certificate semantics and reproduction commands are in the contract.

### DFALab: bounded conformance, not an unrestricted test-pass claim

[Live W-method inspector](https://midya8.github.io/dfalab/conformance.html) | [Construction, assumptions and sources](https://github.com/midya8/dfalab/blob/main/CONFORMANCE.md) | [Source](https://github.com/midya8/dfalab)

The classic DFA W-method now has a complete experiment inspector: every state-cover word, middle word, distinguishing suffix, canonical factor and acceptance path. It separates four claims: finite suite agreement, the supplied candidate's reachable-state bound, a bounded equivalence certificate and a separate exact graph audit. A faulty extra-state candidate passes when its bound is understated; increasing the bound exposes the fault. Tests do not infer a hidden service's state count.

An independent verifier reconstructs all factor combinations and checks every output and witness without calling the generator. Six added native tests include 52,488 exhaustive reference/candidate cases; 131 full native/browser-engine reports are cross-checked. Actual Chrome audits 3,444 test selections and 141 probes across eleven controls and three widths. Four Python versions, seven Node/Chrome checks and installed two-family reproduction preserve the original L* learning page and schema. These are synthetic fixture checks, not production-protocol benchmarks or a new theorem. The method is credited to Vasilevskii and Chow; the precise DFA theorem and reset/state-bound assumptions are documented.
