# EUFLab

**Same output. Not the same input.** Proof-producing ground equality, congruence-derived contradictions and total finite countermodels.

[Live inspector](https://midya8.github.io/euflab/) · [Exact contract and six-source ledger](https://github.com/midya8/euflab/blob/main/METHOD.md)

- Native union-find and proof-forest paths; independent relational closure/certificate/model replay.
- Separate JavaScript relation engine. Every ordered equal pair has a proof DAG. Every non-entailed equality in a consistent input has a separating finite interpretation.
- Explicit controls for non-injectivity, cyclic values, duplicate syntax, ordered arguments, redundant assumptions, multiple disequality conflicts and inconsistency/vacuity.
- No dependencies at runtime. No model API, private data, account execution or new-algorithm claim.

## Run

Python 3.10+:

```sh
git clone https://github.com/midya8/euflab.git
cd euflab
python -m euflab docs/example.json --output report.json
python -m euflab report.json --verify
python -m unittest discover -s tests -v
bash tools/check_wheel.sh
```

Or install `python -m pip install .` and use `euflab`. Node 22+ and local Chrome run `npm test`. Open the demo via `python -m http.server --directory docs 8000` and visit http://localhost:8000. Browser edits run locally; native verification of downloaded reports runs offline.

Input is a subterm-closed ordered term DAG, not a string parser. IDs are original list positions:

```json
{"terms":[{"symbol":"a","args":[]},{"symbol":"b","args":[]},{"symbol":"f","args":[0]},{"symbol":"f","args":[1]}],"equalities":[[2,3]],"disequalities":[]}
```

This asserts f(a)=f(b). It does not imply a=b. The displayed total model assigns distinct values to a and b and the same output to f on both. Conversely, a=b implies f(a)=f(b). a=f(a) is legal because functions are not free constructors.

## Evidence and limits

Nine native tests include partition-enumeration references, 27 exhaustive constant conjunctions, 64 four-term assertion subsets plus all added disequality probes, 80 seeded DAGs, proof tampering and atomic CLI rejection. Two Node tests compare 156 semantic reports and native-check every browser proof DAG. Chrome tests all 251 ordered queries and every displayed proof/model row at 320/390/1280. Wheel reproduction runs 12 controls through both entry points outside checkout.

At most eight terms, arity at most two, eight equalities and eight disequalities. One uninterpreted sort; ground conjunctions only. Proofs are valid explanations, not shortest proofs or minimal cores. A separating model does not prove a universal inequality. Inconsistent inputs have no countermodel and entail everything classically, even if a pair is absent from positive closure. Classical congruence closure, not new theory, a scalable solver or a real-code verifier. See [METHOD.md](https://github.com/midya8/euflab/blob/main/METHOD.md).


## EUFLab: ground equality with evidence

[Live proof and countermodel inspector](https://midya8.github.io/euflab/) | [Source and reproduction](https://github.com/midya8/euflab) | [Semantics and six-source ledger](https://github.com/midya8/euflab/blob/main/METHOD.md)

Functions preserve equality, not difference. EUFLab exposes ground congruence proof DAGs, every contradicted disequality and a total finite interpretation for consistent inputs. Inspect non-injectivity, cyclic values, duplicate syntax, ordered arguments and inconsistent-premise boundaries. Native union-find/proof forests, separate browser relation saturation, independent proof/model verification and exhaustive set-partition references make the claims inspectable.

Validation: 9 native tests on Python 3.10-3.13; 156 cross-engine reports; 251 query selections at each of 320, 390 and 1280 pixels; installed-wheel generation and verification through both entry points. Bounded ground conjunctions only, not quantified logic, arithmetic, SMT-LIB parsing or a production SMT solver. No model service or paid API.


## EUFLab finite-model atlas

[Live finite-model atlas](https://midya8.github.io/euflab/atlas.html) | [Source and reproduction](https://github.com/midya8/euflab) | [Exact atlas contract](https://github.com/midya8/euflab/blob/main/ATLAS.md)

The most separated quotient is not necessarily the smallest model. EUFLab now enumerates every compatible term-equality pattern, finds minimum domain size, and classifies each pair as forced equal, forced different or flexible. Explore total model witnesses, unary backward difference, binary disjunctions, odd-cycle coloring and all 4,140 eight-name patterns. Counts are equality patterns, not full interpretations; extra unnamed domain elements remain possible.

Independent restricted-growth, explicit-block and subset-cover enumerators. Validation preserves the original nine native tests: 16 native tests on Python 3.10-3.13, six Node/Chrome tests, 76 complete cross-engine atlas reports, installed-wheel reproduction of both inspector families, and all 4,317 admitted control patterns at 320/390/1280 pixels. Exhaustive ground-conjunction search, capped at eight terms; no scalability or new-algorithm claim.
