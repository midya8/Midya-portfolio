# UnifyLab

Finite first-order unification with complete equation rewrites, composed substitutions and independently checked certificates.



## A binding is not a solution

[Live finite-term inspector](https://midya8.github.io/unifylab/) | [Source](https://github.com/midya8/unifylab) | [Method and inspected sources](https://github.com/midya8/unifylab/blob/main/METHOD.md)

An original bounded classical-AI unification lab. Keep every equation rewrite, composed earlier binding, exact constructor clash and zero-based occurs-check cycle path. A normalized simultaneous substitution is applied to every original equation. Alias reversal is not automatically a cycle, and a resource limit never means non-unifiability.

Independent Python and JavaScript engines reproduce 167 complete reports and 270 rewrites. A separate native certificate checker reconstructs local rules without calling the solver; a third lazy-environment oracle tests controls, 600 seeded systems and all 64 term-pool pairs. Seventeen controls retain 38 rewrites, including actual state/result expansion limits. Twelve native tests on Python 3.10-3.13, three Node/Chrome tests and seventeen isolated installed reports through two CLIs in solve/verify modes. Every retained browser step, equation, binding, witness, export and invalid edit is checked, with layouts at 320/390/1280.

Established finite-tree unification, not new theory. Six variables/eight equations, 96 input nodes, 4,096-node state/result budgets and 256 rewrites. No rational trees, higher-order/AC unification, resolution prover, linear-time or benchmark-win claim. Most-generality follows the established rewrite/solved-form theory; bounded ground-factorization tests are not a universal proof.


## What makes the evidence inspectable

Each record retains full before/after pending systems and binding maps. Delete/orient/decompose/eliminate/occurs/clash rules have deterministic first-equation and left-to-right child order. Failure leaves the terminal state unchanged. A limit preserves a completed prefix and claims no unifier or non-unifiability.

The native checker independently validates the record, including resource-bound termination and final idempotence/equality, without invoking solve. It is an executable checker, not a cryptographic signature or proof-assistant extraction. The browser's narrower result checks are explicitly distinguished from it. CLI output is atomic after valid computation; native parsing rejects duplicate keys while browser JSON.parse uses the last duplicate key, disclosed in the page.

## Reproduce

```sh
python -m unittest discover -s tests -v
npm test
bash tools/wheel_smoke.sh
python -m unifylab examples/equations.json -o certificate.json
python -m unifylab --verify certificate.json
```

No runtime dependencies, paid API, model, private dataset or account. Six inspected source groups span Martelli/Montanari, Oxford rewrite theory, Norvig's binding-list correction, SWI-Prolog finite/rational-tree semantics, Dresden substitution/complexity notes and an independent explanatory article. METHOD.md identifies inspected coverage and excluded algorithms/examples.


## UnifyLab: minimal equation conflicts and deletion repairs

[Live subset inspector](https://midya8.github.io/unifylab/cores.html) · [Source](https://github.com/midya8/unifylab) · [Method and inspected sources](https://github.com/midya8/unifylab/blob/main/SUBSETS.md)

Test every indexed subset, keep duplicate equation identities, and distinguish an inclusion-minimal conflict from a smallest conflict. Confirmed deletion repairs list indices to REMOVE and failing single restorations. The default control has independent duplicate/cycle conflicts and repairs of different sizes. A resource limit stays unresolved: no inferred status, false inconsistency, complete-frontier or minimum-size claim. Any selected subsystem opens its detailed rewrite trace.

Eight synthetic controls cover 371 subsets, including all 256 masks at the eight-equation bound, real state/result limits and a known clash beside an unknown expansion. Independent Python/JavaScript engines match 108 full audits and 1,032 subset summaries. Nineteen native tests pass on Python 3.10-3.13; six Node/Chrome tests. Native tests use a third lazy-binding oracle, all proper subsets and independent minimal hitting-set enumeration. Actual Chrome checks every control/subset/neighbor at 320/390/1280, five linked rewrite reproductions, export and invalid-state clearing. Installed wheels reproduce seventeen base reports and eight subset audits through both entry points outside the checkout.

Established finite-tree and constraint-diagnosis concepts, not a new scalable MUS/MCS algorithm. At most 256 independent bounded solves; the aggregate is not an independently verified rewrite certificate. Eight inspected sources distinguish minimal from minimum, conflict from repair, and unifiability semantics from resource limits. No model, API, paid service or private dataset.
