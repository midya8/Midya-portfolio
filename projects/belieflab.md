# BeliefLab: pay to observe, then act

[Source and full method notes](https://github.com/midya8/belieflab)

BeliefLab solves small, supplied POMDPs with two hidden states and two possible observations. It uses exact rational arithmetic to compare observation-based plans with the best fixed action sequence, trace a chosen policy tree and bound discounted infinite-horizon value. Python 3.10+, standard library only. It does not learn a model or approximate beliefs on a grid.

## Start with the question

| Question | Command | What it returns |
| --- | --- | --- |
| Is observing worth its cost? | `python -m belieflab demo` | A two-step sensing example and its exact policy envelope. |
| What does feedback add? | `python -m belieflab feedback-demo` | The optimized contingent and fixed-sequence values over every belief. |
| What does this particular tree earn? | `python -m belieflab policy-demo` | Branch probability masses, reward contributions and fixed-tree regret. |
| How far is a finite value from the discounted optimum? | `python -m belieflab residual-demo` | Global Bellman residual bounds and an infinite-value bracket. |

## A case where observing pays

The sensing fixture has two fixed hidden states. Either exploit action earns +1 in its matching state and -1 in the other. Probe costs 1/10 and reports the state correctly with probability 9/10. The initial belief is uniform; the horizon is two actions with discount one.

Starting with either exploit action gives a best total reward of zero. Starting with probe gives `-1/10 + 4/5 = 7/10`: use the observation to choose the second action. Every root action is compared over the same two-action horizon. A one-action decision would skip probe because its immediate reward is negative.

For belief `b = P(state 0)`, the two-step optimum is `max(2*(1-2*b), 7/10, 2*(2*b-1))`. Probe is optimal on `[13/40,27/40]`, including boundary ties. The figure joins exact envelope breakpoints, not samples from a belief grid.

![Exact sensing envelope and policy witnesses](https://raw.githubusercontent.com/midya8/belieflab/70920bfd9ecf2b0ef6a89397954836cb236e4c2a/assets/belief-audit.svg)

## Compare feedback with an optimized baseline

A fixed sequence commits all actions before observations arrive. BeliefLab checks every such sequence for the same model, discount and horizon, including every reward and sensing cost. It does not weaken the baseline to a myopic choice or one hand-picked sequence.

For the sensing fixture, all nine two-step sequences are checked. The best fixed-sequence value is `2*abs(2*b-1)`. At the uniform prior its value is zero, versus 7/10 with feedback. The gap has maximum 7/10 and exact uniform-belief integral 49/400. That integral is geometric area, not expected deployment gain. A separate uninformative-emission control has zero gap everywhere.

![Contingent and fixed-sequence envelopes with their exact gap](https://raw.githubusercontent.com/midya8/belieflab/70920bfd9ecf2b0ef6a89397954836cb236e4c2a/assets/feedback-audit.svg)

## Follow one policy tree

`evaluate_policy` follows a supplied tree without optimizing its actions. Every history has an unconditional state mass and reach probability; reachable histories also have a conditional belief. Impossible histories keep null conditional values rather than invented posteriors.

For the probe tree, the return is `-1/10 + (1/2)*(4/5) + (1/2)*(4/5) = 7/10`. Each branch contributes 2/5 unconditionally, not its conditional reward of 4/5. A separate backward alpha-vector evaluation must agree exactly with the forward sum.

`audit_policy` compares that fixed tree with the optimized contingent envelope. The probe tree is optimal on `[13/40,27/40]` but loses 13/10 at either certain-state prior. A tree optimal at one prior need not be optimal everywhere. A fixed exploit tree is also different from the optimized open-loop envelope, whose best sequence can change with the prior.

![Branch masses, reward contributions and fixed-policy optimality intervals](https://raw.githubusercontent.com/midya8/belieflab/70920bfd9ecf2b0ef6a89397954836cb236e4c2a/assets/policy-audit.svg)

## Bound value without claiming an infinite policy

`certify_discounted` builds through horizon `H+1` for `H` in `0..3`, with discount strictly below one. It finds the global signed minimum and maximum of `T V_H - V_H` over every belief. Dividing these bounds by `1-discount` gives shifts that bracket the infinite-horizon optimal value.

For the declared perfect-probe fixture at horizon three, the uniform-prior finite value is 13/20, the residual range is `[31/600,1/8]` and the certified infinite-value interval is `[113/150,9/10]`. Its analytic infinite value is 9/10. The raw residual alone is not a value-error bound.

![Signed residuals and the discounted infinite-value bracket](https://raw.githubusercontent.com/midya8/belieflab/70920bfd9ecf2b0ef6a89397954836cb236e4c2a/assets/discounted-certificate.svg)

## Reproduce it

```sh
python -m unittest discover -s tests -v
PYTHONPATH=. python examples/render_audit.py --check
PYTHONPATH=. python examples/render_feedback.py --check
PYTHONPATH=. python examples/render_policy.py --check
PYTHONPATH=. python examples/render_residual.py --check
python -m pip install .
belieflab demo
```

The 86 tests include independent complete policy-tree and state-path references, all-belief crossing-cell checks, fixed-policy mass accounting, signed residual controls, strict input rejection and exact figure regeneration. The wheel contains ten modules; both installed CLI entry points reproduce the source commands outside the source tree.

## Scope and limits

Models have two hidden states, two observations, one to three actions, horizon zero to four and zero terminal value. Strict rational inputs, simplex checks and candidate preflight reject unsupported requests without a partial result. Candidate counts do not bound rational bit costs, time or RAM.

Pruning preserves values, not every tied policy tree. Root-action ties are computed separately before pruning. The discounted certificate bounds optimal value; it does not return an evaluated infinite-horizon controller or certify action optimality, model truth or real-world safety. No transition, reward or observation learning is included.

[README: commands, validation and test coverage](https://github.com/midya8/belieflab#readme) · [DESIGN: backup, tie and signed-bound contracts](https://github.com/midya8/belieflab/blob/main/DESIGN.md)
