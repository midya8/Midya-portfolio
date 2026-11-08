# GameLab: minimax value is unique, the strategy may not be

[Public source](https://github.com/midya8/gamelab) · Python 3.10+ · standard library only · MIT

![Exact minimax and degeneracy audit](https://raw.githubusercontent.com/midya8/gamelab/refs/heads/main/assets/minimax-audit.svg)

## Problem

A multi-agent score table can be cyclic. A single average payoff can look balanced even when both policies are exploitable. Even an exact game value need not identify one optimal randomized policy. GameLab makes those distinctions inspectable for a supplied small zero-sum matrix, rather than hiding degeneracy behind a single solver vector.

## Build

An exact-rational security-LP enumerator tries every active basis, at most 70 per player for a 4x4 table. Every singular/infeasible/feasible attempt retains rank, determinant, pivots, all slacks and violations. Feasible vertices merge duplicate bases, and all optimal vertices describe the full optimal face. The row player maximizes payoff; the column player minimizes it by solving the negative-transpose game. That internal column value has the opposite sign.

A deterministic equal average of distinct optimal vertices supplies one equilibrium with pure-action payoff, best-reply, probability, primal/dual and complementary-slackness witnesses. It is not a uniquely preferred or maximum-entropy policy. Coordinate extrema include attaining vertices; their ranges are not independent choices. A separate strategy audit returns both unilateral gains and both security losses, using the sum rather than half-sum exploitability convention.

The payoff-change audit retains both complete solutions, entry differences, every maximum-difference location and exact bound slacks. With epsilon the maximum entry change, value changes by at most epsilon and the old equilibrium pair has new gap at most two epsilon. These are deterministic supplied-table bounds, not confidence intervals.

## Developed controls

- Rock-paper-scissors has value zero and one-third mixed policies. Both fixed action-zero policies also yield payoff zero, but their unilateral gains sum to two. A zero observed payoff is not an equilibrium certificate.
- Duplicate rows in a 4x2 game give optimal row vertices `[0,1/2,1/2,0]` and `[1/2,0,1/2,0]`. Every convex combination is optimal. The fourth action is dominated. The representative `[1/4,1/4,1/2,0]` preserves the face rather than pretending it is unique.
- A constant 2x3 table has every policy optimal; singular and duplicate bases are expected. A nonzero game independently checks value `3/2` and row policy `[1/4,3/4]`.
- A two-row/one-column payoff flip of `10^-12` changes the unique optimal row from `[0,1]` to `[1,0]` with unchanged value. Strategies can be discontinuous even when values are stable. A separate near-bound control approaches the two-epsilon transfer-gap bound.

## Verification

37 tests cover all 81 ternary 2x2 matrices against an independent one-dimensional envelope oracle, independent permutation determinants and every basis residual on four controls, optimal-vertex cross-pairs and convex mixtures, coordinate attaining witnesses, all 81 grid strategy pairs, affine/permutation/negative-transpose invariances, perturbation cases, 4x4 capacity and strict input failures. Four SVG tests bind 23 cells, four range segments/eight endpoints, complete compressed report metadata, hidden-basis tampering and exact regeneration. The five-module installed wheel matches all four full CLI JSON outputs outside checkout. CI runs Python 3.10-3.13 plus a package-parity job.

## Scope and attribution

Only 1..4 actions per side; exact bounded inputs; no runtime dependency or network call. Developed numerical fixtures are not held-out tournaments or evidence of real-agent strength. No general-sum, hidden-information, extensive-form, correlated-equilibrium, learned-opponent, payoff-estimation, scalable-solver or new-algorithm claim. Exact elimination can grow expensive with large rational components.

The project implements established minimax, LP duality and polytope geometry. Six consulted sources, the full proof, schemas, orientation differences and uncertainty boundaries are recorded in the source repository's DESIGN.md. The README links the complete developed JSON audit and the reproducible figure generator.
