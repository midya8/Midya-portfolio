# BellmanLab

[Repository](https://github.com/midya 8/bellmanlab)

Exact rational planning for small fully specified discounted MDPs. The model is supplied, not learned from samples. Dependency-free Python 3.10+, strict JSON CLI, a reproducible SVG and an isolated-wheel demo.

![Bellman residual versus certified and actual value error](https://raw.githubusercontent.com/midya 8/bellmanlab/main/assets/bellman-audit.svg)

## A stopping rule that checks the right quantity

A directly specified one-state self-loop pays 1/100 each step at discount 99/100. Its exact value is one. From value zero, the Bellman residual is 1/100, but the actual value error and certified upper bound are both one. Testing the raw residual against a value-error tolerance 1/10 passes the wrong gate. The contraction certificate divides the residual by 1-discount, so the correct gate fails. Synchronous exact value iteration first meets the certified tolerance after 230 sweeps. The full initial-plus 230-audit history is returned; the demo asserts initially passing raw residual, failing certified error and finally passing certified error.

The SVG puts all three quantities on one linear scale with a shared zero and a visible tolerance line. Its metadata contains exact initial/final certificates, six declared checkpoints 0,1,10,100,229,230 and the full separate policy-iteration trace. Full histories remain in the CLI/API; no rational stopping decision is rounded.

## Evaluation is different from optimality

Exact policy evaluation solves `(I-discount*P_policy)v=reward_policy` with rational Gauss-Jordan elimination and checks every policy equation afterward. Residual zero for those equations does not certify that the policy is optimal. A separate full Bellman audit checks all actions, returns every greedy tie and computes the value-error bound.

A separate three-state fixture pays 1 immediately and terminates, or pays 0 then reaches a state paying 1/5 forever. At discount 9/10, immediate action gives start value 1; exact policy improvement chooses delayed return and reaches 9/5. This uses one complete supplied model, not different training data or a comparison of online learning algorithms.

Policy iteration retains an old action on an exact greedy tie and changes only for strict improvement. Every policy, value, action table, proposed improvement and stability flag is recorded. Stable means optimal, not unique. Hitting the evaluation cap returns the last evaluated policy with `optimal=false`, not a proposed policy that has never been evaluated. Value-iteration caps likewise do not masquerade as convergence. Audit representatives choose the first greedy index, without a unique-policy claim.

## Independent checks and resource contract

34 tests include 243 two-state stochastic models with all four deterministic policies independently evaluated by two-by-two Cramer formulas:972 exact policy evaluations. Policy iteration matches the per-state optimal envelope across policies. Each value-iteration checkpoint's actual error is compared with its certified bound. Tests also reconstruct every synchronous backup and full Q/tie table; check near-one-discount geometric-series values and a16-state delayed chain; cover zero discount, negative rewards, tiny exact advantages, old-action tie retention, monotone policy values, caps, final-audit read counters, pivoting, strict schema/rational/transition validation, denominator limits, isolation and every CLI command. Four SVG tests verify complete declared metadata, every bar/tolerance coordinate, regeneration and changed-history rejection. A four-module wheel reproduces the demo outside the source directory.

Inputs use explicit integers or rational pairs, not floats or decimal strings. Transition rows sum exactly to one. Scope is 16 states, eight actions per state,64 actions and 512 stored transition entries total; rewards have magnitude<=100. Input components and the model/initial-value denominator LCM have stated 1,000,000 caps. Value iteration permits 256 sweeps and policy iteration 64 evaluations. Stored zero-probability entries remain counted. Planned/executed transition-entry reads include every full Bellman audit, even the final residual check; counts exclude rational bit complexity, validation, serialization and object overhead. No wall-time, FLOP or RAM-byte guarantee follows.

```sh
python -m bellmanlab demo
python -m bellmanlab audit examples/residual.json --values '[0]'
python -m bellmanlab evaluate examples/delayed.json --policy '[0,0,0]'
python -m bellmanlab value examples/residual.json --sweeps 256 --tolerance '[1,10]'
python -m bellmanlab policy examples/delayed.json
python -m unittest discover -s tests -v
PYTHONPATH=. python examples/render_audit.py --check
```

Dynamic programming and policy improvement follow [Sutton and Barto, Chapter 4 lecture slides](https://people.montefiore.uliege.be/lwh/AIA/Dynamic-programming-Sutton.pdf). Implementation, exact schema/certificates, direct fixtures, independent tests and figure are original. No external dataset or model is bundled. MIT licensed; no API key, network, paid service, GPU or download is needed.

Only finite, fully observed, discounted supplied models are supported. The certificate bounds value error, not greedy-policy loss or statistical uncertainty. No learned environment, online RL, sample-efficiency, partial-observability, undiscounted guarantee or real-world control-safety claim is made. Exact arithmetic cannot validate the supplied model's fit to the world.
