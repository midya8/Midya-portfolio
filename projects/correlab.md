# Correlab: what does the player know?

Correlab audits a supplied joint play distribution in a small two-player general-sum game. It computes exact rational gains for fixed-action, recommendation-conditioned and full-swap deviations. A separate private-signal model lets a player pass or override through a trusted executor. No model is trained, and no equilibrium is searched for.

[Public source](https://github.com/midya8/correlab) · Python 3.10+ · standard library only · MIT

| Question | Command | Information model |
| --- | --- | --- |
| Is a supplied law obedient? | `audit` | The player sees its own recommendation. Fixed-action, weighted one-pair, full-swap and conditional gains stay separate. |
| What holds for a realized history? | `history` | The same model applied to empirical prefix laws, with actual and counterfactual payoff totals. |
| What can a private signal reveal? | `signals` | The player sees a supplied signal, not its hidden baseline action, then passes or overrides. |
| What changes under a supplied post-garbling? | `garble` | A coarser signal, with a lifted coarse policy and nonnegative per-signal slacks. |
| What do deterministic partitions reveal? | `partitions` | Own-action partitions through four actions, with every strict refinement relation. |

## Own-recommendation audits

![Exact joint-play obedience controls](https://raw.githubusercontent.com/midya8/correlab/refs/heads/main/assets/obedience-audit.svg)

Both players maximize their own payoff table. Each recommendation/action deviation retains every opponent-action probability, payoff difference and exact contribution. Full-swap optimization separates by recommendation: choose an action maximizing each row of weighted gains, then add the maxima. Reports keep every optimal choice, the number of optimal maps, the lexicographically first attaining map and all its joint-cell contributions.

Conditional gains divide by positive recommendation mass; zero-mass recommendations return null. Each player's gains remain separate. The report also audits the product of the supplied marginals and retains exact product equality and total variation. Only a product law that is CCE is labeled a Nash product.

The controls separate claims that a single regret number can hide:

- Roth's attributed lecture-8 law has uniform diagonal play, payoff 3/10, best raw fixed gain -3/10 and clipped coarse epsilon zero. Recommendation C still permits conditional gain 11/10 and weighted/full-swap gain 11/30.
- A developed coordination law pays 3/2 and is CE. Its product-marginals control pays 3/4 and has swap regret 1/4, despite identical player marginals.
- A recommendation with mass 1/1000 has weighted gain 1/1000 and conditional gain one.
- Three equally likely recommendations with row payoffs [0,0,1] have largest one-pair gain 1/3 and full-swap gain 2/3. An attaining map sends every recommendation to action 2.

[Definitions, proof, schema and source notes](https://github.com/midya8/correlab/blob/main/DESIGN.md)

## Private pass-or-override signals

![Exact private override-signal controls](https://raw.githubusercontent.com/midya8/correlab/refs/heads/main/assets/private-signals.svg)

A trusted executor keeps the baseline action hidden. The player sees only a supplied private signal, then passes or overrides; the opponent stays at its baseline action. This is a unilateral decision problem, not CE of a changed game or a simultaneous-override model.

Every signal/action retains exact joint-cell contributions, conditional gains, zero-mass nulls, ties and an attaining policy. Identity signals recover full-swap gain; identical-row channels recover clipped coarse gain. A supplied post-garbling keeps both audits and a lifted optimal coarse policy. Its nonnegative per-signal slacks sum to the information loss.

The deterministic own-action partition counts are 1, 2, 5 and 15 for one through four actions. All partitions are audited independently for each player, including every strict refinement relation. A developed cyclic control gives gains `0, 4/3, 5/3, 1, 2` for partitions `000, 001, 010, 011, 012`: the three two-signal partitions have different values. The Roth control gives gains `0, 11/120, 11/60, 11/30` as C's reveal probability rises `0, 1/4, 1/2, 1`.

[Private-signal model, proofs and sources](https://github.com/midya8/correlab/blob/main/SIGNALS.md)

## Histories are not learning guarantees

Realized joint actions produce exact prefix count laws. Independent sums of actual, fixed-action counterfactual and attaining-swap counterfactual payoffs check that total regret equals prefix length times the corresponding empirical-law gain. Final empirical reports are order-invariant; prefixes and last-round laws need not be.

A developed six-round history finishes with an empirical CCE while its last joint action has coarse epsilon 11/10. This is a finite arithmetic identity and counterexample, not an implemented learner, no-regret guarantee, last-iterate theorem or concentration bound.

## Reproduce and check

From a checkout, using Python 3.10+:

```sh
git clone https://github.com/midya8/correlab.git
cd correlab
python -m correlab demo
python -m correlab audit examples/audit-input.json
python -m correlab history examples/history-input.json
python -m correlab signal-demo
python -m correlab signals examples/signals-input.json
python -m correlab garble examples/garble-input.json
python -m correlab partitions examples/partitions-input.json
python -m unittest discover -s tests -v
python examples/render_demo.py --check
python examples/render_signals.py --check
```

The documentation review ran all 50 tests and both figure checks on fresh baseline, revised, published and merged source. Fresh isolated wheels verified seven module origins, all seven complete CLI reports byte-for-byte, both saved demos and all 50 tests outside the checkout. Hosted CI checks Python 3.10 through 3.13 plus wheel parity.

The suite enumerates 2,835 original game/law cases against independent action maps, 28 rectangular/larger controls up to 256 maps per player, and all 256 length-four 2x2 histories at three prefixes. The private-signal checks enumerate 8,505 channel audits, 28 four-signal controls up to 625 policies per player and 243 post-garbling lift certificates. All 16 signal-alphabet size pairs are checked by direct lift simulation. Figure tests bind 36 obedience cells and 25 signal cells, full compressed reports, hidden-term tampering and exact regeneration.

## Scope and prior work

Inputs are supplied finite bimatrix games, exact joint laws, signal channels or realized histories. Limits are one to four actions per side, 1,000 realized rounds and 100 explicit checkpoints. Epsilon values are payoff incentives, not distance to an equilibrium set or statistical confidence. No adaptive learner, scalable equilibrium solver, causal experiment, hidden-information/extensive-form game solver, universal channel-order search, global stochastic-channel optimization, privacy, real-agent strength or safety certification is claimed.

The method files cite and reconcile established definitions from Blum-Mansour, Bonn, Roth, Barakat, Charles University and Hart-Mas-Colell. They credit the adapted Roth fixture and record cost/payoff orientation differences and source-text typos. Other controls are developed constructions, not external data. The separate signal source notes distinguish single-agent information value from strategic welfare.
