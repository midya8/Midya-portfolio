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

## StableLab: safe replacement, not matching answers

Equal stable models today does not make a rule module safe to swap. StableLab 0.2.0 now checks every SE pair and produces an actual rule context when two finite modules differ, including controls with equal classical **and** stable families but unequal SE sets.

[Live safe-replacement inspector](https://midya8.github.io/stablelab/equivalence.html) · [Source](https://github.com/midya8/stablelab) · [Contract and reproduction](https://github.com/midya8/stablelab/blob/main/EQUIVALENCE.md) · [Merged PR #2](https://github.com/midya8/stablelab/pull/2)

- Complete `X ⊆ Y` atlas: up to five atoms, 243 pairs, 24 normal rules per side. Every original/reduct obligation is visible; every difference supplies a concrete facts/cycle context with both augmented stable families and full candidate evidence.
- Independent three-valued Python reconstruction and proper-subset context model checks, not another call to the generator. Shared strict parsers and the base evidence verifier are disclosed. Eleven controls include an actual two-edge positive cycle gadget, safe transitive-edge removal, redundant rules, contextual inconsistency and empty vocabulary.
- Reproduced from final feature and main: 16 Python tests on 3.10–3.13; eight Node/Chrome tests; installed 0.2.0 wheel, both CLI entry points, all 11 comparison controls and forged-verdict rejection. Optional clingo 5.8.3 agrees on 5,184 base and 3,514 augmented families across 2,592 comparisons.
- Actual deployed Chrome checks 33 comparison reports at desktop/390/320 widths, all 993 displayed pairs and 9,012 rule obligations, 24 context displays and 11 downloaded reports independently verified in Python. Final feature/main and main/live each match on 65 unmasked screenshots across the base and comparison inspectors. All 11 deployed assets plus root match final main exactly. Feature/PR/main CI and Pages are green.

The strong-equivalence claim is restricted to finite normal-rule contexts over the same declared vocabulary. No arbitrary ASP syntax, fresh-atom context UI, update-semantics preservation, scalable-solver or new-theory claim. Published SE-model foundations and the cycle specialization are credited in [SOURCES.md](https://github.com/midya8/stablelab/blob/main/SOURCES.md). The original eight-atom reduct inspector remains available.
