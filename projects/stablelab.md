# StableLab

Finite answer-set evidence for normal logic programs.

## StableLab: support is not grounding

[Live workbench](https://midya8.github.io/stablelab/) · [Source](https://github.com/midya8/stablelab) · [Exact contract](https://github.com/midya8/stablelab/blob/main/CONTRACT.md) · [Prior-work ledger](https://github.com/midya8/stablelab/blob/main/SOURCES.md)

A model can be supported and minimal, yet still not stable. StableLab makes the
missing foundation visible. Enumerate every candidate interpretation of a tiny
normal logic program, inspect the actual Gelfond-Lifschitz reduct, and follow
its synchronous derivation rounds from the empty set. See every original rule's
truth test, every support, every proper-subset classical model and every
nonempty unfounded subset with all rule-level obligations.

The program `p <- not p; p <- q; q <- p` has exactly one classical model,
`{p,q}`. It is both supported and minimal. But its candidate reduct contains
only a positive cycle and derives nothing, so there is no stable model. Other
controls separate even and odd default cycles, constraint filtering, a fact
that grounds four derivation layers, exceptions to defaults, one empty stable
model versus no model, and 16 stable alternatives among 256 candidates. Ten
developed synthetic controls contain 300 candidates in total. When no stable
model exists, brave and skeptical answers are explicitly null here, rather than
presenting vacuous universal truth as evidence.

The separate Python checker does not call the generator. It enumerates every
reduct model and proper candidate subset to test stability, intersects models of
the definite reduct for its least closure, reconstructs rounds by bounded proof
heights, and independently checks every unfounded subset. Shared strict input
validation is disclosed. Browser exports become independently checked only
when `stablelab verify evidence.json` accepts them.

Release evidence: nine Python tests on 3.10/3.11/3.12/3.13; four Node/actual-Chrome
tests; all 1,177 two-atom programs through two signed-body rules/constraints;
200 seeded three-atom programs; forged-evidence rejection; and installed 0.1.0
wheel reproduction outside the checkout through both CLI entry points on all
ten controls. An optional external clingo 5.8.3 comparison agreed on stable-model
families for 1,387 programs. That finite check does not validate the UI/proof
evidence or prove general solver compatibility.

Actual deployed Chrome checks 30 responsive reports, all 900 candidate selections,
6,537 unfounded subset selections and 16,605 rule obligations, 1,926 closure
rounds, every displayed rule/reduct/support/query verdict, ten exports accepted
by Python, stale/invalid input and recovery. All 27 native/fresh feature/main
source files match, as do six deployed assets plus root. All 31 feature/main and
31 main/live unmasked screenshot pairs match. Desktop and phone pixels, circular
support, stable alternatives, seeded closure, empty/no-model cases and error
states were inspected. Feature/PR/main CI and Pages are green; PR1 merged
normally after all final checks passed.

**Exact scope:** at most eight declared propositional atoms and 32 normal rules
or headless constraints. Facts and default negation, not a full ASP language.
No variables or variable grounding, function symbols, classical negation,
disjunction, choice rules, aggregates, optimization, well-founded semantics or
clingo text compatibility. Established finite enumeration and semantic methods,
not a new algorithm or a scalable solver. Synthetic programs, not real agents'
beliefs. Model counts are not probabilities.
