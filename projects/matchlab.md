# MatchLab: stable is not cost-optimal

**No pair wants to leave together. That does not select the cheapest stable assignment.**

MatchLab is an exact finite two-sided preference workbench for AI allocation and multi-agent reasoning teaching profiles. Inspect every complete pairing, strict blocking-pair test, deferred-acceptance proposal state, attainable stable partner and stable-lattice operation. An explicitly separate supplied assignment-cost matrix exposes where stability and optimization answer different questions.

[Live inspector](https://midya8.github.io/matchlab/) · [Source](https://github.com/midya8/matchlab) · [Method and attributed theory](https://github.com/midya8/matchlab/blob/main/METHOD.md) · [Reviewed change](https://github.com/midya8/matchlab/pull/1)

## Optimal for which side?

In the original default profile A rankings are `1>2>0`, `0>2>1`, `2>1>0`. B rankings are `2>0>1`, `1>2>0`, `1>0>2`. Rows of the supplied cost matrix are `(6,0,0)`, `(6,3,2)`, `(1,7,11)`. These numbers are a separate assignment objective, not preference ranks converted to utilities.

| Matching ID | A-to-B assignment | Supplied cost | Blocking pairs | Role |
|---|---|---:|---:|---|
| 3 | `(1,2,0)` | 3 | 1 | Unique unconstrained cost minimum |
| 4 | `(2,0,1)` | 13 | 0 | Unique cheapest stable assignment |
| 1 | `(0,2,1)` | 15 | 0 | B-proposing stable extreme |
| 2 | `(1,0,2)` | 17 | 0 | A-proposing stable extreme |

The unconstrained minimum is blocked by `(A2,B1)`: each strictly prefers the other to its assigned partner. The stability premium for requiring no blocking pair is **10**, but running either side's deferred acceptance does not select the cost-13 stable assignment. Every A participant weakly prefers the A-proposing extreme within the stable family; every B participant has the reverse interest. There is no claim that either side's optimum makes both sides better off.

Another original four-by-four control has four stable assignments with an incomparable diamond lattice. Matchings 1 and 6 are incomparable; their A-oriented join is 0 and meet is 7. The stable family need not be a single chain.

## Every temporary holding is inspectable

The lowest-ID free proposer tries its next receiver. A receiver keeps its best proposal so far; a held proposer can be displaced later. Both sides' full traces show previous holdings, acceptance, rejected proposer, receiver holdings, next cursors, free IDs and partial A-to-B assignment. Partial assignments always use A-to-B orientation, including when B proposes.

The inspector retains the full assignment census and all n-squared pair tests per assignment. Select any pairing to see assigned edges and dashed blocking edges, each participant's candidate/current ranks and both strict comparisons. Select either proposal trace, any stable-lattice operand pair or any integer blocker-count cap. Stable partner lists retain every attainable partner in that participant's own preference order.

The cost/blocker-count frontier keeps every tied nondominated assignment. Cap zero recovers the stable cost minimum; the maximum cap recovers the unconstrained one. The relaxation is something to inspect, not a recommendation to tolerate departures. Ordinal rank sums and worst ranks are descriptive indices, not cardinal utilities or an implicit policy. Input edits clear old evidence and disable stale exports; narrow-screen tables scroll internally.

## Checks with different obligations

The Python generator enumerates bijections, builds rank lookup arrays and constructs lattice joins/meets from coordinatewise A-better/A-worse partners. The native replay checker does not import the generator: it enumerates independently, uses direct preference-list indexing, tracks proposals through per-proposer partners, and finds joins/meets by exhaustive search over the full family's upper/lower bounds. It checks exact types, values, order and completeness, including every optimum tie. Shared schema validation remains a common trust surface.

JavaScript independently enumerates full assignments and searches lattice bounds. Full native/browser report parity is useful but cannot exclude a shared specification error. Native tests also cover all 16 complete two-by-two ordinal profiles, arbitrary free-proposer schedules, side reversal, participant relabeling, positive affine cost changes, receiver improvement, proposal nonrepetition, lattice laws, opposite-side order, ties and negative costs.

The optional input-built SciPy/HiGHS reference creates binary assignment variables, row/column bijection constraints and a no-blocking inequality for each pair. It independently solves unconstrained and stable cost objectives and rescores/checks its returned assignment from the original input. It does not verify every optimum tie, lattice operation or cap; exhaustive replay covers those obligations. It is a numerical reference at tolerance `1e-8`, not an exact solver certificate or scalability benchmark.

## Reproduced evidence

| Check | Developed scope |
|---|---|
| Native Python | 20 tests; 76 complete reports: 16 developed controls plus 12 seeded profiles per size 1..5 |
| Exact report evidence | 2,219 assignments; 49,295 pair witnesses; 113 stable assignments; 217 lattice operations; 715 proposal states |
| Mutation rejection | 1,372 changed derived primitives across three controls, all rejected |
| Cross-engine | Two Node tests; full 76-report Python/JavaScript parity and strict input handling |
| Independent integer reference | 152 input-built HiGHS solves; 1,774 constraint rows; zero observed objective error |
| Installed reproduction | Six module origins outside source; 16 controls; both CLI entrypoints; 32 forged reports rejected |
| Actual Chrome | 48 responsive views; 1,149 selected assignments; 23,793 pair rows |
| Interactive state oracle | 453 proposal states; 243 lattice-operation selections; 450 blocker-cap selections |
| Download replay | 16 exact reports downloaded by trusted mouse click and independently verified natively |

```sh
python -m pip install .
matchlab demo > report.json
matchlab verify report.json
python -m unittest discover -s tests -v
node --test tests/test_engine.cjs tests/test_browser.cjs
python tools/check_installed.py
python tools/check_milp.py
```

Publication verified at main `03d9549d21565f50b49320bff645152d40446d7d`. [PR #1](https://github.com/midya8/matchlab/pull/1) merged after all six latest feature/PR jobs passed. [Main CI](https://github.com/midya8/matchlab/actions/runs/42889633488) and [Pages deployment](https://github.com/midya8/matchlab/actions/runs/42889689979) passed for that exact main. All 44 public files match tested source; all five deployed assets match byte-for-byte. The full deployed Chrome workflow passes, including independent download replay; all 31 captures match inspected local pixels. These gates identify this released implementation, not the truth of supplied preferences or social suitability of an assignment.

## Scope and prior work

Equal sides of size one to five; strict complete rankings; all pairs acceptable; one partner per participant. Input costs are signed integers -1000..1000. No ties, unacceptable partners, capacities, unmatched participants or learned preferences. Enumeration and exhaustive replay add factorial/output-size work. No scalable market-allocation service is claimed.

Gale-Shapley deferred acceptance, proposer optimality and the stable lattice are classical and attributed in [SOURCES.md](https://github.com/midya8/matchlab/blob/main/SOURCES.md). Existing matching software is acknowledged. The original contribution is the implementation, synthetic controls, evidence format, independent replay and inspectable UI, not a new algorithm, fairness result or strategy-proofness claim for both sides. Developed profiles are not held-out evaluation. There is no backend, paid API, analytics or external font dependency. A self-consistent report certifies its included arithmetic, not the intended provenance of the input.
