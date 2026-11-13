# UnifyLab: equations, conflicts and ground-term generalization

[Source](https://github.com/midya8/unifylab) · [Live unifier](https://midya8.github.io/unifylab/) · [Method and sources](https://github.com/midya8/unifylab/blob/main/METHOD.md)

## Finite first-order unification

UnifyLab solves small equation systems over finite constructor trees. Each step retains the pending equations, earlier bindings and the change made by deleting, orienting, decomposing or eliminating an equation. Constructor clashes and occurs-check failures keep their witnesses. A successful result applies one normalized simultaneous substitution to every original equation.

Composition matters. If a variable already bound inside another term later gets a value, earlier bindings must change too. Reversing an alias is not automatically a cycle. The native engine eagerly composes replacements; a separate test oracle uses lazy bindings and symmetric dereferencing. A native certificate checker reconstructs local rewrites, resource limits and terminal claims without calling the solver. The separately written JavaScript engine reproduces complete reports. Browser equality/idempotence checks are narrower result checks, not this independent verifier.

Seventeen original controls retain 38 rewrites: eleven successes, four non-unifiable tasks and two actual resource-limit cases. Python/JavaScript agree on 167 complete reports containing 270 rewrites. Native tests also compare the lazy oracle on 600 seeded systems and all 64 ordered pairs from a small term pool. Bounded ground-factorization tests are regression evidence, not a universal proof of most-generality. That interpretation follows the established solution-preserving rewrite and solved-form theory; the deterministic policy chooses a presentation, not a uniquely printed MGU.

Input allows six variables, eight equations, 96 term nodes, depth six and arity two. Each composed state and the final applied-original result has a separate 4,096-node budget; at most 256 rewrites are retained. A limit keeps only the completed prefix and claims neither success nor non-unifiability. This expanded-tree implementation is not a compact-DAG or linear-time unifier.

## Equation conflicts and deletion repairs

[Subset inspector](https://midya8.github.io/unifylab/cores.html) · [Subset method and sources](https://github.com/midya8/unifylab/blob/main/SUBSETS.md)

Every indexed equation subset is solved independently. Duplicate equations keep separate identities. A confirmed inclusion-minimal conflict fails while each single deletion succeeds. A confirmed deletion repair lists indices to remove; restoring any removed equation must fail. Minimal does not mean smallest: the default control has conflicts and repairs of different sizes.

An unresolved resource limit is never treated as failure or inferred from a neighboring mask. Unknown required neighbors prevent frontier confirmation. Any unresolved mask withholds complete-frontier and minimum-cardinality claims, while separately confirmed conflicts can remain visible. For fully decided tables, tests independently enumerate all proper subsets and minimal hitting sets. Any selected subsystem opens its detailed rewrite trace with local indices; the subset inspector keeps the original indices.

Eight controls cover 371 subsets, including all 256 masks at the equation bound, real state/result expansion limits and a known clash beside an unresolved expansion. Independent Python/JavaScript implementations agree on 108 full audits and 1,032 subset summaries. Chrome checks every control/subset/neighbor at 320/390/1280 and five linked rewrite reproductions. At most 256 bounded solves are run. The aggregate summary is not an independently verified rewrite certificate or a scalable MUS/MCS algorithm.

## Ground-term generalization

[Generalization inspector](https://midya8.github.io/unifylab/generalize.html) · [Generalization method and sources](https://github.com/midya8/unifylab/blob/main/GENERALIZATION.md)

Unification finds a common instance. Anti-unification finds a common generalizer. This interface accepts two ground finite trees only, not variable-bearing equation inputs. It keeps common constructors and assigns the same variable to each repeated ordered disagreement pair. Reversed pairs remain distinct. Fresh/reuse records, both reconstruction maps and every postorder node are inspectable.

Reconstructing both inputs does not establish least-generality. A fresh variable at every differing position can reconstruct them while losing a shared equality. The native checker rejects that coherent but overly general trace. It uses an explicit obligation stack, structural pair-list search and a private instantiator rather than calling the generator or its memoized traversal. It accepts the canonical naming/record policy, not every renamed LGG certificate.

Python and JavaScript agree on 209 complete reports with 323 node records. Nine original controls expose 43 records. Native tests include 600 seeded ground pairs, all 64 small-pool pairs, field forgeries and bounded factorization against independently matched candidate patterns. These finite checks do not replace the first-order least-generality theorem.

## Run and check

```sh
python -m unittest discover -s tests -v
npm test
bash tools/wheel_smoke.sh
python -m unifylab examples/equations.json -o certificate.json
python -m unifylab --verify certificate.json
python -m unifylab --subsets examples/equations.json
python -m unifylab --generalize terms.json -o generalization.json
python -m unifylab --verify-generalization generalization.json
```

The current suite has 27 native tests and fifteen Node tests, including actual Chrome and six navigation-readiness checks. Browser tests inspect every retained rewrite/generalization node, subset boundary, export and invalid-state clearing, with layouts at 320/390/1280. Isolated wheel checks reproduce seventeen solves, eight subset audits and nine generalizations through module and console entry paths in all five modes outside the checkout, with six installed module origins.

Native parsing rejects duplicate keys, nonfinite constants and invalid UTF-8; output replacement is atomic after valid computation. Browser JSON.parse keeps the last duplicate key, disclosed in the pages. No runtime dependency, account, model, paid API or private dataset is required.

## Boundaries and prior work

Finite-tree syntactic unification, minimal conflict/correction sets and Plotkin/Reynolds anti-unification are established work. Martelli/Montanari's rewrite theory, Norvig's correction to faulty binding-list implementations and the cited constraint-diagnosis/generalization literature inform the scope. UnifyLab is an original bounded implementation, not a new theorem, optimized multiequation solver, resolution prover, semantic clone detector or code-repair model. No rational trees, higher-order/AC unification, semantic similarity, benchmark win, scalability or proof-assistant guarantee is claimed.
