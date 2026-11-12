# MatchLab: stable matching and supplied costs

MatchLab enumerates strict complete two-sided stable matchings on small synthetic profiles. It shows every pairing, blocking-pair test, deferred-acceptance proposal state and stable-lattice operation. Supplied assignment costs are separate from preference rankings: inspect what each side can attain and which assignment minimizes the chosen costs.

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

## What each checker covers

The Python generator enumerates bijections, builds rank lookup arrays and constructs lattice joins/meets from coordinatewise A-better/A-worse partners. The native replay checker does not import the generator: it enumerates independently, uses direct preference-list indexing, tracks proposals through per-proposer partners, and finds joins/meets by exhaustive search over the full family's upper/lower bounds. It checks exact types, values, order and completeness, including every optimum tie. Shared schema validation remains a common trust surface.

JavaScript independently enumerates full assignments and searches lattice bounds. Full native/browser report parity is useful but cannot exclude a shared specification error. Native tests also cover all 16 complete two-by-two ordinal profiles, arbitrary free-proposer schedules, side reversal, participant relabeling, positive affine cost changes, receiver improvement, proposal nonrepetition, lattice laws, opposite-side order, ties and negative costs.

The optional input-built SciPy/HiGHS reference creates binary assignment variables, row/column bijection constraints and a no-blocking inequality for each pair. It independently solves unconstrained and stable cost objectives and rescores/checks its returned assignment from the original input. It does not verify every optimum tie, lattice operation or cap; exhaustive replay covers those obligations. It is a numerical reference at tolerance `1e-8`, not an exact solver certificate or scalability benchmark.

## Run and check

The native suite covers complete finite reports, forged evidence, side reversal,
relabeling and lattice laws. Cross-engine checks compare the full Python and
JavaScript reports. Chrome tests select matching, proposal, lattice and cost-cap
states at desktop and mobile widths, then download reports and check them with
the native verifier. The wheel check imports outside the source tree and runs
both CLI entrypoints, including forged-report rejection.

```sh
python -m venv .venv
. .venv/bin/activate
python -m pip install .
matchlab demo > report.json
matchlab verify report.json
python -m unittest discover -s tests -v
node --test tests/test_engine.cjs tests/test_browser.cjs
python tools/check_assets.py
python tools/check_installed.py
```

Node 22+ and Chrome (or `CHROME_BIN`) are needed for browser tests. To run the
optional input-built integer reference in the active environment:

```sh
python -m pip install scipy==1.15.3
python tools/check_milp.py
```

The test output reports the finite corpus and numerical tolerance. These checks
do not establish the truth of supplied preferences or the social suitability of
an assignment. [README review](https://github.com/midya8/matchlab/pull/2) ·
[Main checks](https://github.com/midya8/matchlab/actions/runs/43236650962) ·
[Pages deployment](https://github.com/midya8/matchlab/actions/runs/43236649201).

## Scope and prior work

Equal sides of size one to five; strict complete rankings; all pairs acceptable; one partner per participant. Input costs are signed integers -1000..1000. No ties, unacceptable partners, capacities, unmatched participants or learned preferences. Enumeration and exhaustive replay add factorial/output-size work. No scalable market-allocation service is claimed.

Gale-Shapley deferred acceptance, proposer optimality and the stable lattice are classical and attributed in [SOURCES.md](https://github.com/midya8/matchlab/blob/main/SOURCES.md). Existing matching software is acknowledged. The original contribution is the implementation, synthetic controls, evidence format, independent replay and inspectable UI, not a new algorithm, fairness result or strategy-proofness claim for both sides. Developed profiles are not held-out evaluation. There is no backend, paid API, analytics or external font dependency. A self-consistent report certifies its included arithmetic, not the intended provenance of the input.
