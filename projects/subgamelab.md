# SubgameLab: complete plans and subgame checks

SubgameLab checks small, supplied two-player sequential games with exact rational arithmetic. It compares root one-node stability, full-player pure Nash equilibrium and subgame perfection, retaining off-path choices and tied contingent plans.

[Live inspector](https://midya8.github.io/subgamelab/) · [Source](https://github.com/midya8/subgamelab) · [Reviewed implementation](https://github.com/midya8/subgamelab/pull/1) · [Exact contract](https://github.com/midya8/subgamelab/blob/main/CONTRACT.md)

## Empty threats and root Nash

In the developed default, P1 chooses action 0 for payoff (1, 4), or action 1 to P2. P2's action 0 gives (-1, 0), while action 1 gives (3, 2). Complete plans 00 and 11 are pure Nash: against P2's fight action 0, P1 does not want to enter, and P2's unreached action cannot improve its root payoff. But if P2's node is actually reached, changing its action gains 2. Only 11 is subgame perfect. This is a developed variant of the classical entry-deterrence pattern, not a newly discovered phenomenon or market recommendation.

Every profile exposes each node's continuation payoff pair and root reach, every local root/continuation gain, and every full-player alternative in each subgame. Choose a plan, continuation node and player to see the complete witness. A valid certificate checks the arithmetic of included payoffs, not their truth or any real person's rationality.

## One-node root stability can miss a joint change

The same-player control gives P1 payoff 1 by stopping at the root, 0 by entering then stopping, and 3 by entering then continuing. Plan 00 is stable against changing either node alone at the root. Changing both nodes gains 2, so it is not Nash. The browser explicitly calls the weaker property root one-node stability.

This does not contradict the finite one-deviation principle. That principle requires continuation optimality at every player node, including unreached ones. Checking only reach-weighted root gains is a different condition. We compare full-player alternatives at every subtree directly rather than use that shortcut.

## Zero-reach subgames

A chance control reaches terminal (2, 2) with probability 1. Its probability 0 branch lets P2 choose (0, 0) or (0, 5). Both complete plans are root Nash and have identical root outcomes. Only the latter satisfies subgame perfection. Subtree values are evaluated from the subtree root; there is no division by its zero reach probability.

Rational chance, terminal-only, one-player-only, all-tied and maximum-six-decision controls remain present. Chance probabilities are supplied exact distributions, not learned uncertainty or calibrated agent behavior.

## Tied continuation plans

In a tied P2 continuation, both actions give P2 payoff 3, while P1 receives 1 or 4. P1's outside option is 2. Depending on the retained P2 continuation, P1 should stop or enter. Both subgame-perfect plans survive. The all-zero three-decision control retains all 8 complete plans.

Backward induction combines every pair of child-subgame equilibrium plans before selecting every maximizing current action. It never takes coordinatewise maxima from incompatible continuation plans. Unchosen child plans remain in the evidence. Deterministic IDs are lexicographic complete action assignments, not merged normal-form outcome classes.

## Independent replay

Native generation uses reverse dynamic evaluation and child-plan Cartesian products. The independent verifier imports validation only: it enumerates terminal paths, multiplies chance/choice indicators, sums exact terminal payoffs and enumerates every full unilateral assignment in every subtree. It reconstructs the complete report and each node's equilibrium-plan correspondence without using generator recurrence or backward induction. Strict recursive comparison rejects extra, missing, reordered, mistyped or forged evidence.

The separate JavaScript engine uses BigInt rational arithmetic and matches every complete report. Its browser replay uses that same engine and is explicitly not an independent verifier. Trusted browser downloads are checked by the independent native CLI.

Optional actual Nashpy 0.0.43 builds a fresh normal-form payoff matrix for each subtree directly from input paths, then checks every pure strategy pair with its best-response API. Matrices are not built from expected output. Exact rational matrix entries are scaled to integers; the largest absolute scaled entry is 18 and every nonzero payoff difference is at least 1 in this corpus. Nashpy uses NumPy isclose, so this is supplemental numerical reference evidence, not exact certification. Gambit was researched but its local build did not finish; no Gambit validation is claimed.

## Verification

| Check | Observed result |
|---|---|
| Python suite | 14 tests |
| Exhaustive tiny class | All 2,916 two-decision games: four player-owner patterns × 729 ternary six-payoff assignments |
| Complete Python/BigInt reports | 65: ten developed controls and 55 seeded trees |
| Retained report content | 1,233 profiles; 12,820 subgame/player audits; 48,250 full-player alternatives |
| Primitive certificate tampering | 317 noninput forgeries rejected per engine |
| Actual Nashpy reference | 533 input-built subtree matrices; 2,353 pure-pair checks; all 1,233 profile classifications |
| Installed wheel | Five site-packages module origins; ten controls; two entrypoints; 20 CLI forgery failures |
| Actual Chrome | 40 views at 1440/768/390/320; 388 plan selections; 1,209 continuation selections; 2,837 alternative rows |
| Trusted completed downloads | Ten inputs and ten certificates; certificates independently replayed by native CLI |

The exhaustive class fixes a particular two-decision chain topology, not all finite trees. Seeded trees vary shape and repeated player ownership, with some chance roots. Developed controls cover the six-decision/two-chance boundaries. Counts are bounded reproduction evidence, not statistical generalization, timing measurements or real-agent strength.

## Original implementation

The original [PR1](https://github.com/midya8/subgamelab/pull/1) merged after all 12 latest feature/PR jobs passed. Its merge `63cea0d5493f98c88a8cd9eedc38fe29110b5784` retains initial commit `e476b84101157f0917e6f1c1f3524e53ca75b3a1` and feature `0585e52f79b161645830f05dd0fd963530b1db96`. All 27 public files match the tested source. [Merged-main checks](https://github.com/midya8/subgamelab/actions/runs/42934221670) and [Pages deployment](https://github.com/midya8/subgamelab/actions/runs/42934221719) passed. Five live assets match merged source, the complete deployed Chrome workflow passes, and all 48 unmasked deployed captures match local pixels. Actual desktop hero, phone chance-zero verdicts and 320 px boundary witness tables were inspected.

## Scope and credited theory

Two players, at most six binary player decisions, two binary chance nodes and 17 nodes. Complete pure contingent plans; singleton information sets; exact canonical rational inputs with absolute numerator/denominator at most 1,000. No hidden information, mixed-equilibrium enumeration, imperfect recall, CFR, learning, preference inference, formal verification, new theorem, scalable solver or real-market advice. Native duplicate JSON keys are rejected; browser JSON.parse keeps the last. Stale edits clear evidence and disable downloads; tables/tree scroll inside bounded mobile regions.

[Osborne's textbook chapter](https://www.economics.utoronto.ca/osborne/igt/igtChapter5.pdf), [Tamuz's notes](https://tamuz.caltech.edu/teaching/ps172/lectures.pdf), [MIT refinement lectures](https://ocw.mit.edu/courses/14.126-game-theory-spring-2024/mit14_126_s24_lecture_2_refinements.pdf) and [Maryland's game-tree lecture](https://www.cs.umd.edu/~hajiagha/474GT15/Lecture12122013.pdf) ground the finite model and continuation requirements. [Knight's educational chapter](https://vknight.org/gtb/chapters/subgame-perfection/), [Gambit's algorithms](https://gambitproject.readthedocs.io/en/stable/algorithms.html) and [Nashpy's best-response API](https://nashpy.readthedocs.io/en/stable/how-to/check-best-responses.html) acknowledge existing teaching and software. Subgame perfection is classical Selten theory, not our invention. Full source ledger and API distinctions are in SOURCES.md.

GameLab studies zero-sum matrices; Correlab studies one-shot advice/obedience; AuctionLab studies allocation incentives. SubgameLab instead audits sequential contingent plans, full-player versus root-local deviations and credibility in every finite perfect-information subtree. Original bounded implementation and developed controls by Midya Rahmani; no external code, figures, datasets or weights copied.
