# Correlab: the recommendation changes the deviation

[Public source](https://github.com/midya8/correlab) · Python 3.10+ · standard library only · MIT

![Exact joint-play obedience controls](https://raw.githubusercontent.com/midya8/correlab/refs/heads/main/assets/obedience-audit.svg)

## v0.2: what does the player observe?

![Exact private override-signal controls](https://raw.githubusercontent.com/midya8/correlab/refs/heads/main/assets/private-signals.svg)

A trusted executor retains the hidden baseline action. The player sees only a
supplied private signal and may pass or override, with the opponent left at its
baseline action. This is an explicit unilateral decision model, not CE of a
changed game. Every signal/action retains exact joint-cell contributions,
conditional gains, zero-mass nulls, all optimal choices and an attaining policy.
Identity signals recover full-swap gain; identical-row channels recover clipped
coarse gain. A supplied post-garbling retains both audits and a lifted optimal
coarse policy with exact nonnegative per-signal slacks summing to information loss.

All deterministic own-action partitions through four actions are audited
independently for each player, with every strict refinement relation. The
Bell counts are 1, 2, 5, 15. A developed cyclic control gives row gains
`0, 4/3, 5/3, 1, 2` for partitions `000, 001, 010, 011, 012`, showing that three
two-signal partitions can differ. The attributed Roth control yields
`0, 11/120, 11/60, 11/30` as C's reveal probability rises `0, 1/4, 1/2, 1`.

The v0.2 suite has 50 tests, including independent enumeration for 8,505
channel audits, 28 larger/rectangular four-signal controls up to 625 policies
per player, 243 supplied post-garbling lift certificates, and all 16 signal-alphabet size pairs checked by direct lift simulation. Three new SVG
tests bind 25 numeric cells, complete report metadata and hidden lift-term
tampering. All seven complete CLI outputs match an installed seven-module
wheel outside checkout. The original three CLI outputs and old SVG are unchanged.
Six additional source notes distinguish single-agent value from strategic welfare.

[Private-signal model, proofs and sources](https://github.com/midya8/correlab/blob/main/SIGNALS.md)

No simultaneous override outcome, global stochastic-channel optimization,
universal Blackwell-order search, privacy, learning or agent safety claim.

## The evaluation problem

Multi-agent evaluation can ask different questions before and after a player receives private advice. A joint play distribution may leave no profitable fixed-action deviation, yet still tell a player to take an action they would rather replace after seeing their recommendation. A single regret number can hide that distinction, the probability of the signal, or the effect of removing correlation.

Correlab audits supplied finite general-sum bimatrix games and exact joint laws. Both players maximize their own payoff table. It separates coarse fixed-action deviations, weighted one-pair internal deviations, unrestricted recommendation-dependent swap maps and conditional incentives. It does not search for an equilibrium or train an agent.

## Inspectable certificates

Every recommendation/action deviation retains all opponent-action probabilities, payoff differences and exact contributions. Each fixed deviation retains recommendation-wise gains. Full-swap optimization separates by recommendation: choose an action maximizing each row of weighted gains, then add the maxima. The report retains every optimal choice, the number of optimal maps, the lexicographically first attaining map and all its joint-cell contributions.

Conditional gains divide by the recommendation's positive probability; zero-probability recommendations return null. Each player's gains remain separate. The report also retains marginals, their product, exact product equality, total variation and an independently audited product control. Only a product law that is CCE is labeled a Nash product.

## Controls that expose misleading summaries

- Roth's explicitly attributed lecture-8 CCE-not-CE game has uniform diagonal play with expected payoff 3/10, best raw fixed gain -3/10 and clipped coarse epsilon zero. Recommendation C still permits conditional gain 11/10, weighted and full-swap gain 11/30.
- A developed coordination law pays 3/2 per player and is CE. Its product-marginals control pays 3/4 and has swap regret 1/4. The marginals are identical, but the joint law and incentive properties are not.
- A rare recommendation has mass 1/1000 and weighted gain 1/1000, while its conditional incentive is one.
- Three equally likely recommendations with row payoffs [0,0,1] have largest one-pair gain 1/3 but full-swap gain 2/3. An attaining map sends all recommendations to action 2.

## Finite histories, not learning claims

Realized joint actions produce exact prefix count laws. Independent sums of actual, fixed-action counterfactual and attaining-swap counterfactual payoffs certify that total regret equals prefix length times the corresponding empirical-law gain. Final empirical reports are order-invariant; prefixes and last-round laws need not be.

The developed six-round history finishes with an empirical CCE while the final action pair has coarse epsilon 11/10. This is a finite arithmetic identity and counterexample, not an implemented learner, no-regret guarantee, last-iterate theorem, concentration bound or evidence of agent strength.

## Original v0.1 verification and limits

33 tests cover all 81 ternary 2x2 row tables against all 35 quarter-grid joint laws, with a separately varied column table: 2,835 game/law cases checked by exhaustive action-map enumeration. Another 28 rectangular/larger controls enumerate up to 256 maps per player. All 256 length-four 2x2 histories are checked at three prefixes. Tests include player-specific affine transforms, transpose/player exchange, ties, zero signals, product Nash, negative raw coarse gains, replication, order, capacity, strict parsing and no input/RNG mutation.

Three SVG tests bind all 36 numeric cells, the full compressed report, hidden-term tampering and exact regeneration. The six-module installed wheel matches all three full CLI outputs outside checkout. CI runs Python 3.10-3.13 plus a package-parity job.

One to four actions per side, supplied exact payoff tables and joint laws, at most 1,000 realized rounds and 100 explicit checkpoints. Epsilon values are payoff incentives, not distance to an equilibrium set or statistical confidence. No scalable solver, adaptive algorithm, causal experiment, hidden-information/extensive-form game, real-agent benchmark or safety certification is claimed.

The source DESIGN.md provides proofs, complete schema and six consulted sources: Blum-Mansour, Bonn, Roth, Barakat, Charles University and Hart-Mas-Colell. It credits the adapted Roth fixture and records cost/payoff orientation differences plus source-text typos rather than silently inheriting them. Other controls are developed constructions, not external data.
