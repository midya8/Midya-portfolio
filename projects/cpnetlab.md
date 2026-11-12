# CPNetLab: what follows from the preference rows?

CPNetLab takes a small supplied binary CP-net and lists its legal single-variable improving flips. It computes reachability paths, inconsistency cycles, compatible strict rankings and witnesses for incomparable outcomes. A separate whole-row analysis asks which conditional statements support a path or conflict, and which withdrawals restore consistency. These are supplied qualitative preferences, not learned human tastes or cardinal scores.

[Complete-model inspector](https://midya8.github.io/cpnetlab/) · [Whole-row inspector](https://midya8.github.io/cpnetlab/scopes.html) · [Public source](https://github.com/midya8/cpnetlab)

## Two questions, two reports

| Question | Commands | What the report means |
| --- | --- | --- |
| What follows from the complete supplied model? | `analyze`, `verify` | Every outcome and improving flip, shortest positive-length paths, cycles, ranking counts and opposite ranking witnesses for incomparable pairs |
| Which whole rows suffice, conflict or can be withdrawn? | `scopes`, `verify-scopes` | Every row subset, actual path/cycle/ranking witnesses, all inclusion-minimal supports, conflicts and consistency-restoring withdrawals |

A compatible ranking is one possible total order, not an entailed preference. Incomparability is not indifference. A withdrawn row removes every flip it justifies, not one convenient edge. All outcomes and the original supplied model remain intact.

## A local improvement is not a score increase

In the four-variable fanout control, `0000 → 1000` is a legal improving flip even though the number of violated rows rises from one to three. All 2,304 compatible strict rankings put the target above the start. Counting violated rows does not implement the preference semantics.

Dependency cycles and inconsistency also differ. One two-variable dependency cycle permits four compatible rankings and two locally unimprovable outcomes. Reversing a preference table creates the actual improving cycle `00 → 01 → 11 → 10 → 00`, with zero compatible rankings. The inspector shows the cycle rather than making a vacuous preference verdict.

Two independent consistent cycles admit 101,977,088 compatible rankings while leaving `0000` and `1111` incomparable. A complete ranking witness for each direction makes that distinction inspectable.

## Minimal does not mean minimum

The whole-row inspector enumerates every subset of at most eight conditional rows. Across eight developed controls there are 865 subset graphs, with actual paths, cycles and ranking witnesses. It lists all minimal supports, conflicts and withdrawals, rather than choosing a repair for the user.

The default eight-row control has 256 subsets, two minimal conflicts and six irreducible withdrawals: three remove one row, three remove two. A separate control has two-row and four-row minimal path supports. Inclusion-minimal means no proper subset works. Minimum means the smallest cardinality. Neither identifies the human preference that should be abandoned.

These are counterfactual constraint graphs, not automatic preference revision or extended partial-model semantics. Reachability can still be reported in an inconsistent row-subset graph, without calling it an entailed strict preference.

## Reproduce and check

Python 3.10+ has no runtime dependencies. Node 22+ and Chrome are needed for browser tests.

```sh
git clone https://github.com/midya8/cpnetlab.git
cd cpnetlab
python -m pip install .
python -m cpnetlab analyze docs/example.json > evidence.json
python -m cpnetlab verify evidence.json
cpnetlab scopes docs/example.json > rows.json
cpnetlab verify-scopes rows.json
python -m unittest discover -s tests -v
node --test --test-concurrency=1 tests/test_engine.mjs tests/test_scopes.mjs tests/test_browser.cjs tests/test_scopes_browser.cjs
bash tools/check_wheel.sh
python -m http.server --directory docs 8000
```

Python builds flips from conditional rows, uses breadth-first paths and prefix-ideal ranking counts. The independent checker instead compares Hamming-one outcome pairs, uses Floyd-Warshall and suffix-removal counting, and reconstructs the complete report without importing either analyzer. For row subsets it checks all proper candidate subsets and all four antichains. Shared strict input validation and binary encoding are disclosed. JavaScript uses exact BigInt ranking counts, but is not a separate verifier. Browser JSON is independently checked only after the Python verifier accepts it.

The documentation review ran fresh baseline, revised, published and merged source: each passed 14 Python and six Node/actual-Chrome tests. Each isolated wheel checked eight complete-model and eight row-subset controls outside the checkout through module and console analyzers/verifiers, including forged-evidence rejection. The full six-test suite also passed against both deployed inspectors; all 11 live assets matched source bytes.

The complete-model checks include all 36 two-variable networks and 576 ordered queries, five three-variable fixtures against all 40,320 permutations each, and 160 seeded additional networks. Row checks include all 576 ordered two-variable query atlases with 6,400 subset records, all 400 two-variable masks against every total order, and 91 accepted seeded atlases. Actual Chrome checks all 689 ordered complete-model control queries and all 865 row masks, antichain buttons, exports and stale/invalid recovery at three widths.

## Scope and prior work

Complete models have zero to four binary variables, complete strict local tables, no self parents and at most 16 outcomes. The row atlas additionally allows at most eight complete conditional rows and 256 subsets. No local ties, missing rows, learned preferences, cardinal utility, constraints, uncertainty, recommendation-quality or scalable-solver claim. Inconsistent complete models have no compatible strict ranking; the tool does not turn that into a vacuous preference verdict.

CP-net theory, graph search, linear-extension counting and minimal-conflict/correction-set concepts are established prior work. The controls are developed synthetic examples, not measured human choices or a new algorithm. The [complete-model contract](https://github.com/midya8/cpnetlab/blob/main/CONTRACT.md), [row-subset contract](https://github.com/midya8/cpnetlab/blob/main/ROW-SUBSETS.md) and [source ledger](https://github.com/midya8/cpnetlab/blob/main/SOURCES.md) record the definitions, attribution and limits.
