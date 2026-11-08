# BellmanLab

[Repository](https://github.com/midya8/bellmanlab)

Exact rational planning for small fully specified discounted MDPs. The model is supplied, not learned from samples. Dependency-free Python 3.10+, strict JSON CLI, two reproducible SVGs and an isolated-wheel demo.

![Bellman residual versus certified and actual value error](https://raw.githubusercontent.com/midya8/bellmanlab/main/assets/bellman-audit.svg)

## A stopping rule that checks the right quantity

A directly specified one-state self-loop pays 1/100 each step at discount 99/100. Its exact value is one. From value zero, the Bellman residual is 1/100, but the actual value error and certified upper bound are both one. Testing the raw residual against a value-error tolerance 1/10 passes the wrong gate. The contraction certificate divides the residual by 1-discount, so the correct gate fails. Synchronous exact value iteration first meets the certified tolerance after 230 sweeps. The full initial-plus 230-audit history is returned; the demo asserts initially passing raw residual, failing certified error and finally passing certified error.

The SVG puts all three quantities on one linear scale with a shared zero and a visible tolerance line. Its metadata contains exact initial/final certificates, six declared checkpoints 0, 1, 10, 100, 229, 230 and the full separate policy-iteration trace. Full histories remain in the CLI/API; no rational stopping decision is rounded.

## Evaluation is different from optimality

Exact policy evaluation solves `(I-discount*P_policy)v=reward_policy` with rational Gauss-Jordan elimination and checks every policy equation afterward. Residual zero for those equations does not certify that the policy is optimal. A separate full Bellman audit checks all actions, returns every greedy tie and computes the value-error bound.

A separate three-state fixture pays 1 immediately and terminates, or pays 0 then reaches a state paying 1/5 forever. At discount 9/10, immediate action gives start value 1; exact policy improvement chooses delayed return and reaches 9/5. This uses one complete supplied model, not different training data or a comparison of online learning algorithms.

Policy iteration retains an old action on an exact greedy tie and changes only for strict improvement. Every policy, value, action table, proposed improvement and stability flag is recorded. Stable means optimal, not unique. Hitting the evaluation cap returns the last evaluated policy with `optimal=false`, not a proposed policy that has never been evaluated. Value-iteration caps likewise do not masquerade as convergence. Audit representatives choose the first greedy index, without a unique-policy claim.

## Independent checks and resource contract

The original 34 tests include 243 two-state stochastic models with all four deterministic policies independently evaluated by two-by-two Cramer formulas: 972 exact policy evaluations. Policy iteration matches the per-state optimal envelope across policies. Each value-iteration checkpoint's actual error is compared with its certified bound. Tests also reconstruct every synchronous backup and full Q/tie table; check near-one-discount geometric-series values and a 16-state delayed chain; cover zero discount, negative rewards, tiny exact advantages, old-action tie retention, monotone policy values, caps, final-audit read counters, pivoting, strict schema/rational/transition validation, denominator limits, isolation and every CLI command. Four SVG tests verify complete declared metadata, every bar/tolerance coordinate, regeneration and changed-history rejection. A six-module v0.2 wheel reproduces both demos outside the source directory.

Inputs use explicit integers or rational pairs, not floats or decimal strings. Transition rows sum exactly to one. Scope is 16 states, eight actions per state, 64 actions and 512 stored transition entries total; rewards have magnitude <=100. Input components and the model/initial-value denominator LCM have stated 1,000,000 caps. Value iteration permits 256 sweeps and policy iteration 64 evaluations. Stored zero-probability entries remain counted. Planned/executed transition-entry reads include every full Bellman audit, even the final residual check; counts exclude rational bit complexity, validation, serialization and object overhead. No wall-time, FLOP or RAM-byte guarantee follows.

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

## Finite-scenario rectangular robust planning

![Nominal and robust values, plus the difference between global and rectangular scenario uncertainty](https://raw.githubusercontent.com/midya8/bellmanlab/main/assets/robust-audit.svg)

`robust_audit` and `robust_value_iteration` accept `{"version":1,"scenarios":[model0,model1,...]}`. Each scenario is a complete ordinary model in the schema above. Scenarios must share the discount and the number of states/actions at every state. The set contains 1..8 scenarios and at most 2,048 stored transition entries across all scenarios; the combined normalized model-denominator LCM, including initial values when supplied, is capped at 1,000,000. Each scenario still obeys all ordinary limits. The existing 256 KiB JSON-file and 256-sweep caps apply.

**The scenario index is not one global model choice.** At each state/action nature may independently select any listed scenario's reward/transition row, after observing the action. This deliberately forms the `(state,action)`-rectangular closure of the listed models. Both rewards and transitions can vary. It does not solve an ambiguity set that couples one index across states, actions or time.

```python
from bellmanlab import robust_audit, robust_value_iteration
certificate = robust_audit(problem, values)
planning = robust_value_iteration(problem, sweeps=100, tolerance=[1,1000])
fixed_policy = robust_value_iteration(problem, policy=[0,0], sweeps=100)
```

For each state and action, the audit returns every exact scenario Q-value, the minimum across scenarios and every minimizing scenario index. It then maximizes these minima over actions, retaining every maximizing action. It returns the complete backed-up vector, sup residual and `residual/(1-discount)` value-error certificate. The full initial-plus-each-sweep audit history is kept. Without `policy`, the target is the robust optimal value. With a fixed deterministic `policy`, the backed-up vector selects that policy's worst-case action values: its certificate targets **only that policy's robust value**, even when another action is better. The audit still exposes all action Q-values and greedy ties, but zero fixed-policy residual does not establish optimality. Greedy-action representatives are not policy-loss certificates.

```sh
python -m bellmanlab robust-demo
python -m bellmanlab robust-audit examples/robust.json --values '[0]'
python -m bellmanlab robust-value examples/robust.json --sweeps 32 --tolerance '[1,1000000]'
python -m bellmanlab robust-value examples/robust.json --policy '[0]'
PYTHONPATH=. python examples/render_robust.py --check
```

Two directly specified controls make the modeling choice visible:

| Supplied fixture | Exact result |
|---|---|
| One state, discount 1/2, risky reward +2/5 or -2/5, safe reward +1/5 | The nominal risky value is 4/5. Its robust value is -4/5; the robust safe optimum is 2/5. The nominal policy loses 6/5 in robust value. |
| Two alternating states, discount 1/2, globally opposite reward vectors `[1,-1]` and `[-1,1]` | Keeping one global scenario fixed gives worst start value -2/3. The rectangular closure permits a negative row at both states and has value -2. They are different problems, not two solvers for the same uncertainty set. |

Exact fixed-point audits independently confirm the displayed rational values; the robust demo also returns certified finite-sweep runs. The second SVG uses signed common-zero bars, one linear scale per explicitly separated panel, with the full exact demo and every iteration checkpoint embedded in metadata. No parameter, seed or fixture search selects these examples.

54 total tests retain the 34 original checks and add 16 robust API/CLI tests plus four robust SVG tests. A new independent oracle enumerates four controller policies and four stationary adversary choices on each of 243 two-state/two-scenario models: 3,888 closed-form two-by-two Cramer evaluations. Per-policy minima and the controller maximum reproduce exact robust fixed points. Every returned checkpoint reconstructs all scenario Q-values, worst-case ties, greedy ties, synchronous vectors, residuals and bounds against the independent oracle. Tests distinguish a fixed-policy target from optimality, match the ordinary solver for singleton uncertainty, cover permutations/duplicates, signed rewards, zero discount, early stops/caps, zero-probability read accounting, aggregate entry and LCM boundaries, invalid schemas and JSON/CLI budgets. The SVG tests check every signed bar, both zero axes, complete exact metadata, regeneration and rejection of a changed undisplayed checkpoint.

Read counts include all stored scenario transition entries in every audit, including fixed-policy mode's all-action tables and the final residual audit. Planned `(sweeps+1)*aggregate_entries` is an upper bound; executed `number_of_audits*aggregate_entries` reflects stopping. These counts do not include rational bit costs, validation, comparisons, serialization or object overhead. They are not timing, FLOP or RAM measurements.

The rectangular robust-DP formulation is attributed to [Iyengar, Robust Dynamic Programming (2005)](https://pubsonline.informs.org/doi/10.1287/moor.1040.0129) and [Nilim and El Ghaoui, Robust Control of Markov Decision Processes with Uncertain Transition Matrices (2005)](https://people.eecs.berkeley.edu/~elghaoui/Pubs/RobMDP_OR2005.pdf). This finite scenario reward-and-transition contract, implementation, exact certificates, fixtures, tests and figures are original. No external code or dataset is copied. These are supplied ambiguity sets, not statistically learned confidence sets. Nothing certifies an unlisted environment or real-world control safety; there is no coupled-uncertainty solver, online RL, stochastic-policy search or greedy-policy-loss bound.
