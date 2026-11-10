# HornLab


## HornLab: a circle is not a proof

[Live inspector](https://midya8.github.io/hornlab/) · [Source and tests](https://github.com/midya8/hornlab) · [Method and sources](https://github.com/midya8/hornlab/blob/main/METHOD.md)

Bounded positive propositional Horn inference with synchronous derivation rounds and every indexed rule decision. Compare the least model with every classical and supported model: a supported circular assignment need not have a derivation. Inspect an atomic countermodel for each non-entailed query and every inclusion-minimal initial-fact support, including its deletion failures and all seed subsets. Not entailed does not mean classically false.

Independent Python bitsets and JavaScript sets match 210 full reports; a separate native set/truth-table checker replays the complete report. Ten original controls, exhaustive two-atom programs, seeded tests, installed-wheel reproduction and actual Chrome record checks. Six atoms/eight rules, no negation or variables; established semantics, not a new algorithm or production rule engine.

## Method boundaries

Facts are fixed seeds. Empty-body rules can derive atoms with empty seed support. Duplicate indexed rules remain distinct achievers. Synchronous closure does not chain through a new atom until the next round. Models satisfy all implications; support is a separate equality test and may admit unsupported-by-derivation cycles. Minimal supports are relative only to the given initial facts with rules held fixed.

The native checker uses explicit sets, enumerates every truth assignment and tests all proper seed subsets, separate from the bitset generator and its immediate-deletion test. They share validation. This is bounded exhaustive evidence, not a formal proof or a signed certificate. JSON export is unsigned, and the browser generator is not an independent verifier.

## Reproduce

```sh
python -m unittest discover -s tests -v
npm test
bash tools/wheel_smoke.sh
python -m hornlab examples/cycle.json --output /tmp/horn.json
python -m hornlab --verify /tmp/horn.json
```

See the repository METHOD.md for six inspected sources, exact schema, the ten controls and validation limits. No external model, API or paid service.


## HornLab: every route, every break

[Rule-deletion inspector](https://midya8.github.io/hornlab/rules.html) · [Method and primary sources](https://github.com/midya8/hornlab/blob/main/RULES.md) · [Source](https://github.com/midya8/hornlab)

Keep initial facts fixed and inspect all indexed-rule subsets, synchronous closures, every minimal rule support and every minimal deletion set. One broken route need not break the goal. Each support retains one-rule removal failures; each deletion retains restoration successes. Both minimal-hitting-set dualities and every support/deletion intersection are explicit, including empty-support and already-absent boundary cases.

Eighteen native tests retain all originals, with all 1,024 two-atom programs and 150 seeded rule lattices. Independent Python/JavaScript match 131 audits covering 5,304 subsets. Eleven browser controls expose 305 subsets, 35 queries, 36 supports, 27 deletion sets and 36 intersections, all record-checked at 320/390/1280. A separate native set/truth-table checker validates the complete lattice without calling the generator. Installed-wheel reproduction checks both inspectors through both CLI entry points. Established bounded monotone explanation, not causal attribution, ontology translation, a new algorithm or formal proof.


## HornLab: deletion has a derivation debt

Removing a fact can leave a cycle with positive local support and no finite derivation. HornLab 0.3.0 now maintains explicit fact transactions with a complete delete/rederive trace, then shows exactly where a deliberately weaker local-support pruning check goes wrong.

[Live fact-maintenance inspector](https://midya8.github.io/hornlab/updates.html) · [Source](https://github.com/midya8/hornlab) · [Exact contract and credited foundations](https://github.com/midya8/hornlab/blob/main/UPDATES.md) · [Merged PR #3](https://github.com/midya8/hornlab/pull/3)

- Conservative overdeletion, surviving one-step derivations and restored/new delta insertion, with every transaction, round, indexed rule obligation and lost/gained/restored atom. Explicit facts can also be inferred; deleting their explicit status does not necessarily delete their consequence. Twelve developed controls include alternate routes, conjunction, cycles, empty-body rules, duplicates, mixed updates, no-ops and empty vocabulary.
- A separate set-based checker reconstructs the full trace and checks each resulting least model by intersecting all definite-Horn models, without calling the generator. Shared strict validation is disclosed. Python/JavaScript parity covers 212 complete requests and 1,627 transactions; it is not substituted for the independent checker.
- Final feature/main reproduction passes 26 Python tests on 3.10/3.11/3.12/3.13 and eight Node/Chrome tests. Exhaustive tests cover all 4,096 two-atom program/old-fact/new-fact transitions plus 350 seeded eight-step sequences, full-field/type forgeries and atomic CLI failures. Installed 0.3.0 wheel checks run outside the checkout through both entry points for 10 base, 11 rule-audit and 12 update controls, including rejection of forged updates.
- Optional clingo 5.8.3 agrees on 11,381 positive-program stable families across 4,458 requests and 6,923 transactions. Actual deployed Chrome checks 36 new reports at 1280/390/320, 81 transaction selections, 546 phase/round records, 1,491 displayed obligations and twelve downloaded exports independently accepted by Python. Both earlier inspectors also pass their full checks.
- All 49 native/fresh feature/main source files and fourteen deployed assets plus root match exactly. Feature/PR/main CI and Pages are green. All 43 update-inspector plus twelve targeted earlier-inspector screenshots match unmasked in both feature/main and main/live comparisons. Phone overview, narrow-phone cyclic retention, desktop rederivation and both earlier inspectors' new links were visually inspected.

The local contrast counts explicit membership plus currently firing indexed rules, not finite proof trees. It starts each transaction from the same correct old closure and is explicitly **not** the published Counting algorithm, DRedC or modern recursive counting methods. The positive, single-stratum delete/rederive specialization is credited to published work and does not claim its optimized no-repeated-inference bounds. Six atoms, eight fixed positive rules, at most eight fact transactions. No negation, relation tuples, variables, rule updates, full Datalog, new theory or production performance claim. The original inference and rule-deletion inspectors remain available.
