# CredalLab: do these probabilities share a world?

**Each probability can look valid. Their joint model can still be impossible.**

CredalLab is a small, exact inspector for finite probability knowledge bases. Give it explicit worlds, unconditional interval assessments and an event query. It checks whether one joint distribution can satisfy every assessment, returns sharp attainable bounds when it can, and exports independently replayable primal/dual certificates.

It is an original implementation of classical finite probabilistic satisfiability and linear optimization, not a new inference theorem, learned probability model, credal network, calibration benchmark or production safety system.

## Version 0.2: survives every duel, never wins the menu

[Decision inspector](https://midya8.github.io/credallab/decisions.html) · [Decision semantics and sources](https://github.com/midya8/credallab/blob/main/DECISIONS.md) · [Reviewed change](https://github.com/midya8/credallab/pull/2)

The exact menu `(3,0), (0,3), (1,1)` separates five classical criteria. The third action can defend against each pure rival at a different belief, yet no one common belief makes it best. It remains strict pairwise maximal and interval-undominated, and is the unique pure-action maximin choice. Its best shared-belief margin is exactly `-1/2` at belief `(1/2,1/2)`. A fixed 50/50 mixture of its rivals has utility `3/2` in both worlds and excludes it by `1/2` everywhere.

A separate interior-only tie control changes the third action to `(3/2,3/2)`: it is E-admissible only at the half/half belief, not at an original credal vertex. The implementation solves the menu-intersection margin LP with a free-below margin variable, rather than checking only the original probability vertices.

The inspector reports E-admissible, strict pairwise maximal, interval-undominated, pure-action maximin and maximax sets. Select every action's common belief, expected utilities, exclusion-mixture weights and world payoffs; replay every range, ordered-pair, margin and projected-mixture primal/dual certificate. A standalone native checker validates supplied evidence without loading the solver or generator, and accepts alternative attaining witnesses. Editing clears old output and disables stale downloads.

The convention is explicit: **no pointwise-admissibility prefilter**, strictly positive robust advantage for dominance, all ties retained including zero-mass boundaries. Some older presentations apply a pointwise prefilter; the project follows the strict-only definitions in [Nakharutai, Troffaes and Caiado (2019)](https://arxiv.org/html/1906.12215). Randomized rivals are exclusion certificates, not all mixed optimal actions, a mixed maximin solver or advice to randomize. No criterion is selected for the user.

| Additional decision evidence | Developed scope |
|---|---|
| Native | 15 added tests, 31 total with original probability tests |
| Exact parity | 96 complete Python/BigInt decision reports, 75 feasible menus, 56 excluded actions |
| Report forgery rejection | 824 primitive decision modifications across three controls |
| Independent floating reference | 1,420 input-built HiGHS LPs, largest absolute error `2.220446049250313e-16`, tolerance `1e-8` |
| Installed decision wheel | 10 module origins outside source, 16 controls, both entry points, 32 CLI forgeries rejected |
| Actual Chrome | 48 responsive views, 129 action selections, 855 certificate selections, 2,784 independent inequality rows, 1,884 variable rows, 16 downloaded reports natively checked |

The original 120-report probability checks, 505 primitive mutations, 690 reference LPs and original browser/installed checks still pass. All six combined Node/Chrome tests pass. These are finite development controls, not held-out experiments or formal verification. Parsing and mathematical construction are shared by the generator and native checker; independent input-built LPs and visible-row reconstruction reduce but do not remove that common failure surface.

Decision inputs are limited to six worlds/actions and six assessments with separate 20,000 candidate-basis limits. Utilities use bounded exact signed rationals on one common state-independent scale. CLI model input is capped at 64 KiB and certificate reports at 8 MiB; untrusted API reports need caller size limits. No learned utility, conditional decision, sequential policy, scalable algorithm or real-world validation is claimed. See the decision document for the full derivation, source-convention differences and failure surfaces.

```sh
credallab decisions examples/decisions/maximal_never_best.json > decisions.json
credallab verify-decisions decisions.json
python tools/check_decisions_installed.py
python tools/check_decisions_highs.py
node --test --test-concurrency=1 tests/test_decisions.cjs tests/test_decision_browser.cjs
```

Version 0.2 publication verified: [PR #2](https://github.com/midya8/credallab/pull/2) merged after all 12 feature/PR checks. [Merged-main CI](https://github.com/midya8/credallab/actions/runs/42878413289) and [Pages](https://github.com/midya8/credallab/actions/runs/42878411009) passed. All 76 public files match checked source at `3a51c42958a1bddafdf2e42f236fe927f5b2772d`; all ten deployed assets match that source. Both complete deployed Chrome workflows pass: 44 decision captures and 35 updated probability captures match inspected local pixels. Downloaded reports are independently replayed natively. These deployment checks establish this published version, not the truth of supplied utilities or beliefs.

## The default probability counterexample

Consider three binary variables A, B, C and the events A≠B, A≠C and B≠C. Every binary assignment satisfies either zero or two of these events, never all three. Group assignments with the same event memberships into four worlds:

| World | Binary assignments | A≠B | A≠C | B≠C |
|---|---|---:|---:|---:|
| 0 | 000, 111 | 0 | 0 | 0 |
| 1 | 001, 110 | 0 | 1 | 1 |
| 2 | 010, 101 | 1 | 0 | 1 |
| 3 | 011, 100 | 1 | 1 | 0 |

The teaching control uses the three event sets `{1,2}`, `{1,3}`, `{2,3}`. These are the same three pairwise-disagreement events in a reordered column order. Requiring each probability to be one is impossible: their indicator sum is at most two, while the requested expectation sum is three. The minimum common interval relaxation is exactly `1/3`.

Lower each required probability to `2/3` and the unique grouped distribution becomes `(0, 1/3, 1/3, 1/3)`. The logical world universe matters as much as the numerical bounds. Grouping preserves these supplied event memberships, not arbitrary queries about A, B or C.

[Live inspector](https://midya8.github.io/credallab/) · [Source](https://github.com/midya8/credallab) · [Reviewed change](https://github.com/midya8/credallab/pull/1)

Version 0.1.0 is merged. All 12 feature/PR checks, merged-main checks and Pages deployment passed. All 43 public source files match the checked tree. Five deployed assets match merged source; all 35 deployed responsive/control/certificate captures match the inspected local pixels. The deployed browser repeats all 48 control-width views, 288 certificate selections and 16 downloaded-report replays. These are finite developed checks, not formal verification or held-out evaluation.

## Run it

Python 3.10+, no runtime dependencies:

```sh
python -m pip install .
credallab run examples/triangle_impossible.json > report.json
credallab verify report.json
python -m credallab demo > demo.json
```

A browser version lives in `docs/`. Serve it locally with `python -m http.server --directory docs 8000`. JavaScript BigInt rational arithmetic reproduces the complete Python reports. There is no backend, external font, analytics, paid API or network inference call. Loading the static site retrieves its own assets and teaching controls.

```python
from credallab import analyze, verify
model = {
    "version": 1, "worlds": 4,
    "constraints": [
        {"event": [0, 1], "lower": [1, 2], "upper": [1, 2]},
        {"event": [0, 2], "lower": [1, 2], "upper": [1, 2]},
    ],
    "query": {"event": [0], "given": [0, 1, 2, 3]},
}
report = analyze(model)
assert verify(report)
assert report["bounds"]["event"]["lower"]["value"] == [0, 1]
assert report["bounds"]["event"]["upper"]["value"] == [1, 2]
```

Those two half-probability marginals do not justify an independence guess of `1/4` for their intersection.

## What the evidence contains

- A common-slack consistency LP, with an attaining distribution and dual certificate. A strictly positive minimum slack proves the original assessments impossible.
- Exact event and given-event minima and maxima, with attaining distributions.
- Conditional bounds only over compatible distributions with positive conditioning mass. A separate given-event range distinguishes "can vanish" from "forced zero". No posterior is invented for a forced-zero event.
- Every primal inequality, its evaluated slack, every nonnegative dual multiplier, and every dual coefficient in the browser.
- A standalone native certificate checker that imports schema validation only. It checks equations on the supplied witness, not equality with a regenerated preferred answer. Alternative valid witnesses are accepted.
- Editing clears old results and disables download until a fresh successful check.

## Reproduction

```sh
python -m unittest discover -s tests -v
node --test --test-concurrency=1 tests/test_engine.cjs tests/test_browser.cjs
python tools/check_installed.py
python -m pip install scipy==1.15.3
python tools/check_highs.py
```

The browser test requires Chrome and Node 22+; set `CHROME_BIN` if needed. `CREDAL_SCREEN_DIR=/tmp/credal-captures` saves the inspected states.

Developed checks, not held-out evaluation:

| Check | Scope |
|---|---|
| Native tests | 16 tests, including world permutation, duplicate assessments, tightening, strict types, alternate witnesses, import independence and CLI failures |
| Complete report agreement | 120 developed cases: 78 feasible, 42 infeasible, 69 with defined positive-mass conditional bounds |
| Certificate mutations | 505 primitive modifications rejected across three developed reports |
| Independent floating reference | 690 rebuilt HiGHS LPs, including 138 Charnes-Cooper conditional LPs; tolerance `1e-8` |
| Installed wheel | Six module origins outside checkout, 16 controls, two CLI entry points, 32 tampered CLI reports rejected |
| Actual Chrome | 48 control-width views, 288 certificate selections, 1,671 inequality rows, 897 witness-variable rows and 16 downloaded reports independently replayed |

These counts describe a finite development grid. They do not establish correctness for every input, large-scale performance, empirical usefulness or formal verification. The floating reference independently rebuilds the mathematical programs from inputs, but uses the same stated problem convention. The native checker shares parsing and matrix construction with the generator, so bugs in that common layer can affect both.

## Limits and attribution

Inputs allow 1-6 explicit worlds and at most six interval assessments, with a further 20,000 phase-I candidate-basis limit. Rational input components and denominator LCM are bounded. This is deliberately an inspectable exponential enumerator, not a scalable LP engine. All constraints are unconditional; only the query can be conditional. See [METHOD.md](https://github.com/midya8/credallab/blob/main/METHOD.md) for exact signs, schema, endpoints, failure modes and sources.

Classical foundations: [probabilistic satisfiability and coherence survey](https://isipta99.sipta.org/proc/041.pdf), [overlapping marginal compatibility](https://ar5iv.labs.arxiv.org/html/1112.4788), [LP duality notes](https://web.stanford.edu/class/ee364a/lectures/duality.pdf), [linear-fractional programming notes](http://www.seas.ucla.edu/~vandenbe/ee236a/lectures/lfp.pdf), [Python Fraction](https://docs.python.org/3/library/fractions.html), and [SciPy HiGHS](https://docs.scipy.org/doc/scipy/reference/optimize.linprog-highs.html).

MIT license. Teaching controls and code are original to this project. The classical mathematics is attributed, not claimed as an invention.
