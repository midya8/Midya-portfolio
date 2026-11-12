# GameLab: exact zero-sum payoff audits

[Public source](https://github.com/midya8/gamelab) · Python 3.10+ · standard library only · MIT

![Exact minimax and degeneracy audit](https://raw.githubusercontent.com/midya8/gamelab/refs/heads/main/assets/minimax-audit.svg)

## Problem

GameLab solves supplied zero-sum payoff tables with at most four actions per player. It reports exact security witnesses, every optimal strategy vertex and the exploitability of a chosen policy pair. A fixed matrix and a full Cartesian payoff box use separate audits.

A score table can be cyclic. A single average payoff can look balanced even when both policies are exploitable, and an exact game value need not identify one optimal randomized policy. These audits expose those differences; they do not infer payoff tables from agent behavior.

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

The original 37 fixed-matrix tests, retained in the current total of 53, cover all 81 ternary 2x2 matrices against an independent one-dimensional envelope oracle, independent permutation determinants and every basis residual on four controls, optimal-vertex cross-pairs and convex mixtures, coordinate attaining witnesses, all 81 grid strategy pairs, affine/permutation/negative-transpose invariances, perturbation cases, 4x4 capacity and strict input failures. Four SVG tests bind 23 cells, four range segments/eight endpoints, complete compressed report metadata, hidden-basis tampering and exact regeneration. The original five-module installed checks match all four fixed-matrix CLI JSON outputs outside checkout. The interval extension below adds a sixth module and two commands. CI runs Python 3.10-3.13 plus a package-parity job.

## Scope and attribution

Only 1..4 actions per side; exact bounded inputs; no runtime dependency or network call. Developed numerical fixtures are not held-out tournaments or evidence of real-agent strength. No general-sum, hidden-information, extensive-form, correlated-equilibrium, learned-opponent, payoff-estimation, scalable-solver or new-algorithm claim. Exact elimination can grow expensive with large rational components.

The project implements established minimax, LP duality and polytope geometry. Six consulted sources, the full proof, schemas, orientation differences and uncertainty boundaries are recorded in the source repository's DESIGN.md. The README links the complete developed JSON audit and the reproducible figure generator.


## Shared-table interval support extension

![Shared-table interval audit](https://raw.githubusercontent.com/midya8/gamelab/refs/heads/main/assets/interval-audit.svg)

A fixed policy pair faces one unknown payoff table, not two independently selected adverse tables. `interval_audit` computes the exact worst joint deviation gap over a supplied full Cartesian entrywise interval box. For every pure reply pair, it constructs the signed coefficient of every entry before maximizing, retains endpoint choices and contributions, and returns an attaining matrix with a direct best-reply audit. It also reports each player's separately maximized unilateral gain and the conservatism of their sum.

In the developed shared-entry control, only A[0,0] varies in [0,2], all other entries are one and both policies choose action zero. Row worst deviation requires entry zero; column worst requires entry two. The exact shared worst gap is one, while their incompatible separate maxima sum to two. The game value stays one throughout, and the separate robust-security pair is an equilibrium for every allowed table.

For a full 2x2 unit box with uniform fixed policies, shared worst gap is 1/2 versus separate worst-regret sum one. For a one-action game with sole payoff [-50,50], value-range width is 100 but every policy pair's gap is zero. Payoff uncertainty is not the same as incentive to deviate.

Complete endpoint game solves certify the attainable game-value extrema v(L) and v(U). The lower-game row policy and upper-game column policy separately optimize worst security and guarantee pair gap at most v(U)-v(L); a signed audit can be tighter. This construction does not claim to minimize worst joint gap over policies. Individual unilateral deviations are not confused with individual security exploitability as the game value varies.

The current 53-test suite includes all 16 zero/one-width boxes on a nonconstant 2x2 base, each at nine fixed policy pairs, against independent exhaustive endpoint enumeration; every candidate support contribution/attainment; corner game values and robust security; shared-entry and singleton cancellation; affine, zero-width, rectangular and 4x4 controls; strict schemas and no mutation. Three added SVG tests bind all 29 numbers, complete metadata, hidden-coefficient tampering and exact regeneration. The original 37 tests and four original full CLI outputs remain unchanged; the six-module wheel matches all six full outputs outside checkout.

The box is deterministic supplied data, not a statistical confidence region or an independence assumption. No coupled-budget/ellipsoid uncertainty, sampling coverage, payoff estimation, empirical strength or new theorem is claimed. The implementation applies established box support functions; the source INTERVALS.md gives proofs, complete schema and Li-Ding-Floudas, Gorissen-den Hertog and Bertsimas-den Hertog-Pauphilet attribution.
