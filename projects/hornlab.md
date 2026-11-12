# HornLab

HornLab computes what follows from supplied positive definite-Horn rules and facts. Its three inspectors vary initial seeds, indexed rules or explicit fact transactions, and expose the complete bounded records. Circular local support is not a finite derivation.

[Inference inspector](https://midya8.github.io/hornlab/) · [Rule-deletion inspector](https://midya8.github.io/hornlab/rules.html) · [Fact-maintenance inspector](https://midya8.github.io/hornlab/updates.html) · [Source and tests](https://github.com/midya8/hornlab)

## Inference and initial-fact supports

Keep rules fixed. Inspect every synchronous closure round, indexed rule decision, classical satisfying assignment and supported-model flag. Each atom has its entailment result, first derivation round, tied first achievers and an actual countermodel when it is not entailed. Enumerating all subsets of the supplied initial facts gives every inclusion-minimal sufficient seed set and its deletion failures. Minimal does not mean smallest.

A satisfying assignment may include unjustified atoms. A supported assignment may justify atoms circularly. The least model captures positive entailment. Not entailed does not mean classically false: the all-true assignment satisfies every program in this scope.

## Rule supports and deletion sets

Keep initial facts fixed and vary the retained indexed rules. Inspect every subset and closure, every minimal rule support, every minimal deletion set and their removal/restoration boundaries. Both minimal-hitting-set dualities and every support/deletion intersection are explicit. One broken route need not break the goal. Rule deletion cannot remove an initial fact; an already absent atom has the empty deletion set.

## Explicit fact maintenance

Keep rules fixed and apply fact deletions and insertions. Inspect conservative overdeletion, surviving one-step derivations, restored/new delta insertion and every indexed rule obligation. Deleting explicit membership does not necessarily remove a consequence: another derivation may remain.

A deliberately weaker local-support pruning contrast can retain a cycle with no finite derivation. It starts each transaction from the same correct old closure, not from accumulated baseline errors. It is not the published Counting algorithm, DRedC or modern recursive counting methods. The positive, single-stratum delete/rederive specialization is credited to published work and does not claim its optimized no-repeated-inference bounds.

## Checks and reproduction

Separate native set/truth-table checkers replay the full reports without calling the generators. They share strict input validation. Inference checks model intersection and all proper seed subsets; rule audits reconstruct the complete rule lattice; updates reconstruct the maintenance trace and check every resulting least model by intersecting all definite-Horn models. Python/JavaScript parity is a separate check, not a replacement for independent verification.

The current checkout passes 26 Python and eight Node/Chrome tests. Native coverage includes all 1,024 two-atom program/initial-fact combinations, all 4,096 two-atom program/old-fact/new-fact transitions and seeded cases. Installed-wheel checks reproduce ten inference, eleven rule-audit and twelve update controls outside the checkout through both entry points, including forged-report rejection. Optional clingo 5.8.3 agrees on 11,381 positive-program stable families across 4,458 requests and 6,923 transactions.

Deployed Chrome checks all three inspectors at 320/390/1280. The rule controls expose 305 subsets, 35 queries, 36 supports, 27 deletion sets and 36 intersections. Update checks cover 36 reports, 81 transaction selections, 546 phase/round records, 1,491 displayed obligations and twelve downloaded exports independently accepted by Python. These are synthetic bounded controls, not an external benchmark.

```sh
python -m unittest discover -s tests -v
npm test
bash tools/wheel_smoke.sh
python -m hornlab examples/cycle.json -o report.json
python -m hornlab --verify report.json
```

Use `--rules` for rule audits or `--updates` for fact transactions, with `--verify` to check their exports. The installed `hornlab` command supports the same modes. No runtime dependency, external model, API, account or data download.

## Limits and sources

At most six atoms and eight indexed positive propositional rules; fact maintenance accepts at most eight transactions. No negation, variables, relation tuples, rule updates, full Datalog/Prolog or production performance claim. Duplicate indexed rules remain distinct. Empty-body rules may derive atoms without seed facts. Supports are relative to the selected input, not causal explanations or all proof trees.

Counts are exact finite enumeration, not probabilities or scalability evidence. Native checking is not a formal proof or signed certificate; JSON is unsigned, and the browser generator is not an independent verifier. Established semantics and algorithms, not new theory.

See the repository [inference contract](https://github.com/midya8/hornlab/blob/main/METHOD.md), [rule-audit contract](https://github.com/midya8/hornlab/blob/main/RULES.md) and [update contract](https://github.com/midya8/hornlab/blob/main/UPDATES.md) for schemas, validation limits, credited foundations and historical source notes. Those historical external citations were preserved, not freshly revalidated in this prose review.
