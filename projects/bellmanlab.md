# BellmanLab

[Repository](https://github.com/midya8/bellmanlab)

Exact rational planning for small fully specified discounted MDPs. The model is supplied, not learned from samples. Dependency-free Python 3.10+, strict JSON CLI, three reproducible SVGs and an isolated-wheel demo.

![Bellman residual versus certified and actual value error](https://raw.githubusercontent.com/midya8/bellmanlab/main/assets/bellman-audit.svg)

## A stopping rule that checks the right quantity

A directly specified one-state self-loop pays 1/100 each step at discount 99/100. Its exact value is one. From value zero, the Bellman residual is 1/100, but the actual value error and certified upper bound are both one. Testing the raw residual against a value-error tolerance 1/10 passes the wrong gate. The contraction certificate divides the residual by 1-discount, so the correct gate fails. Synchronous exact value iteration first meets the certified tolerance after 230 sweeps. The full initial-plus 230-audit history is returned; the demo asserts initially passing raw residual, failing certified error and finally passing certified error.

The SVG puts all three quantities on one linear scale with a shared zero and a visible tolerance line. Its metadata contains exact initial/final certificates, six declared checkpoints 0, 1, 10, 100, 229, 230 and the full separate policy-iteration trace. Full histories remain in the CLI/API; no rational stopping decision is rounded.

## Evaluation is different from optimality

Exact policy evaluation solves `(I-discount*P_policy)v=reward_policy` with rational Gauss-Jordan elimination and checks every policy equation afterward. Residual zero for those equations does not certify that the policy is optimal. A separate full Bellman audit checks all actions, returns every greedy tie and computes the value-error bound.

A separate three-state fixture pays 1 immediately and terminates, or pays 0 then reaches a state paying 1/5 forever. At discount 9/10, immediate action gives start value 1; exact policy improvement chooses delayed return and reaches 9/5. This uses one complete supplied model, not different training data or a comparison of online learning algorithms.

Policy iteration retains an old action on an exact greedy tie and changes only for strict improvement. Every policy, value, action table, proposed improvement and stability flag is recorded. Stable means optimal, not unique. Hitting the evaluation cap returns the last evaluated policy with `optimal=false`, not a proposed policy that has never been evaluated. Value-iteration caps likewise do not masquerade as convergence. Audit representatives choose the first greedy index, without a unique-policy claim.

## Independent checks and resource contract

The original 34 tests include 243 two-state stochastic models with all four deterministic policies independently evaluated by two-by-two Cramer formulas: 972 exact policy evaluations. Policy iteration matches the per-state optimal envelope across policies. Each value-iteration checkpoint's actual error is compared with its certified bound. Tests also reconstruct every synchronous backup and full Q/tie table; check near-one-discount geometric-series values and a 16-state delayed chain; cover zero discount, negative rewards, tiny exact advantages, old-action tie retention, monotone policy values, caps, final-audit read counters, pivoting, strict schema/rational/transition validation, denominator limits, isolation and every CLI command. Four SVG tests verify complete declared metadata, every bar/tolerance coordinate, regeneration and changed-history rejection. An eight-module v0.3 wheel reproduces the policy demo outside the source directory.

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

The v0.2 foundation has 54 tests, retaining the 34 original checks and adding 16 robust API/CLI tests plus four robust SVG tests. A new independent oracle enumerates four controller policies and four stationary adversary choices on each of 243 two-state/two-scenario models: 3,888 closed-form two-by-two Cramer evaluations. Per-policy minima and the controller maximum reproduce exact robust fixed points. Every returned checkpoint reconstructs all scenario Q-values, worst-case ties, greedy ties, synchronous vectors, residuals and bounds against the independent oracle. Tests distinguish a fixed-policy target from optimality, match the ordinary solver for singleton uncertainty, cover permutations/duplicates, signed rewards, zero discount, early stops/caps, zero-probability read accounting, aggregate entry and LCM boundaries, invalid schemas and JSON/CLI budgets. The SVG tests check every signed bar, both zero axes, complete exact metadata, regeneration and rejection of a changed undisplayed checkpoint.

Read counts include all stored scenario transition entries in every audit, including fixed-policy mode's all-action tables and the final residual audit. Planned `(sweeps+1)*aggregate_entries` is an upper bound; executed `number_of_audits*aggregate_entries` reflects stopping. These counts do not include rational bit costs, validation, comparisons, serialization or object overhead. They are not timing, FLOP or RAM measurements.

The rectangular robust-DP formulation is attributed to [Iyengar, Robust Dynamic Programming (2005)](https://pubsonline.informs.org/doi/10.1287/moor.1040.0129) and [Nilim and El Ghaoui, Robust Control of Markov Decision Processes with Uncertain Transition Matrices (2005)](https://people.eecs.berkeley.edu/~elghaoui/Pubs/RobMDP_OR2005.pdf). This finite scenario reward-and-transition contract, implementation, exact certificates, fixtures, tests and figures are original. No external code or dataset is copied. These are supplied ambiguity sets, not statistically learned confidence sets. Nothing certifies an unlisted environment or real-world control safety; there is no coupled-uncertainty solver, online RL, stochastic-policy search or greedy-policy-loss bound.

## Exact nested controller and adversary policy iteration

![Evaluated versus proposed controller and nature policies under separate caps](https://raw.githubusercontent.com/midya8/bellmanlab/main/assets/robust-policy-audit.svg)

`robust_evaluate_policy(problem, policy, initial_nature=None, iterations=64)` solves the supplied controller's worst-case value by exact adversary policy iteration. Each nature policy selects one scenario row per state for the controller's action. The solver uses the existing rational Gauss-Jordan evaluator, checks every linear equation, audits all scenario values, and changes nature only for a strict minimizing improvement. It retains the current scenario on every exact tie. A stable nature policy has zero fixed-controller robust residual and gives the exact robust value.

`robust_policy_iteration(problem, initial=None, iterations=64, nature_iterations=64)` nests that evaluation inside controller improvement. **The controller is never improved from an unfinished inner solve.** Once nature stabilizes, the controller keeps its action if it is among the robust greedy ties; otherwise it selects the first maximizing action. Exact nature values decrease during the inner solve; exact controller robust values increase during outer improvement. Every evaluated controller/nature policy, solved value, all-scenario Q/tie audit, separate proposed policy and stability flag remains in the nested history. The return includes the number of controller evaluations and total nature evaluations; it does not label those as FLOPs or time.

```sh
python -m bellmanlab robust-policy-demo
python -m bellmanlab robust-evaluate examples/robust.json --policy '[0]'
python -m bellmanlab robust-evaluate examples/robust.json --policy '[0]' --iterations 1
python -m bellmanlab robust-policy examples/robust.json
python -m bellmanlab robust-policy examples/robust.json --iterations 1
python -m bellmanlab robust-policy examples/robust.json --nature-iterations 1
PYTHONPATH=. python examples/render_robust_policy.py --check
```

The same prescribed one-state model exposes both independent caps:

| Run | Returned evaluated controller / nature | Returned value | Exact controller robust value? | Robust optimal? |
|---|---|---:|---|---|
| Inner nature cap 1 | `[0]` / `[0]` | 4/5 | No. This is an upper bound; the true risky robust value is -4/5. | No. Controller improvement is withheld. |
| Outer controller cap 1, completed inner solve | `[0]` / `[1]` | -4/5 | Yes | No. Proposed safe action `[1]` is stored separately, not passed off as evaluated. |
| Both policies stable | `[1]` / `[0]` | 2/5 | Yes | Yes. No uniqueness claim. Two controller evaluations and three nature evaluations. |

`exact=false` in fixed-policy evaluation means the returned value belongs to the last **evaluated stationary nature policy**. It is a componentwise upper bound on that controller's robust value, not an exact worst case. The returned fixed-policy residual certificate still bounds distance to the robust policy value. Outer output separately labels `policy_value_exact`, `optimal` and the termination reason. If nature hits its cap, `improved_policy` is null and outer improvement stops. If only the controller cap is hit, the last exact evaluated controller value is returned, with the proposed controller kept only in history. Both budgets require integers in 1..64; at most 4,096 exact nature evaluations can occur in one outer call. This is an operational limit, not a guarantee that the budgets suffice on every supported model or a bound on integer bit cost/RAM.

70 total tests add 12 exact nested-policy tests and four third-SVG tests to the retained 54 checks. On the same 243-model exhaustive grid, another independent enumeration of 3,888 controller/adversary Cramer solutions verifies every exact fixed-controller value, each returned nature witness, the final controller/nature pair, inner value decrease, outer value increase, minimizing/greedy tie sets, residual bounds and evaluation counters. Additional tests cover both cap failures, withheld outer improvement, retained controller/nature ties, negative rewards, tiny exact advantages, a 16-state chain, invalid policies/budgets, output isolation and CLI modes. Third-SVG tests check all 15 displayed result cells, full exact nested metadata, regeneration and changed-undisplayed-certificate rejection. The eight-module v0.3 wheel reproduces the policy demo outside the source tree. Both prior SVGs remain byte-reproducible.

This is exact supplied rectangular-model planning when stability is reached, not a new learning algorithm, statistical confidence set, coupled-uncertainty solver, unique-policy guarantee or real-world safety claim. Exact rational linear solves alone establish the value of their evaluated policy pair; the separate inner and outer stability checks establish the stronger robust-policy and optimality claims.


## BellmanLab0.4: a policy between policies

A budget can make every high-reward deterministic policy infeasible while a randomized stationary policy remains optimal. The live inspector exposes the whole cost/reward polygon, clipped feasible vertices, exact occupancy flow, a state-conditional policy and an independently checked primal-dual certificate. In the wait/exit control, half-and-half mixing of two deterministic policies produces local exit probability 1/3, not 1/2: mixing policies and randomizing actions are different operations. A separate one-state control attains reward 1 under budget 1/2 while the best feasible deterministic policy earns 0. Infeasible budgets return a checked minimum-cost lower bound, not a fabricated policy.

The new dependency-free Python API and CLI use exact fractions; a separate checker reconstructs the complete report with determinant/Cramer solves and gift wrapping rather than the generator's helpers. The browser uses BigInt rationals and a separately implemented engine. All 88 Python tests and four Node tests pass, retaining all 70 earlier tests and three reproducible SVGs. Across 861 exhaustive/seeded/control inputs, complete browser reports equal native output and 1,722 actual SciPy HiGHS LP solves agree within 1e-8; an extra full-bound report checks integers beyond JavaScript's safe range. An independent full-flow vertex oracle covers 28 cases, and 169 non-input primitive-leaf forgeries are rejected. A fresh isolated wheel reproduces the prior three demo families and the new API/CLI outside the source tree. Feature, PR, merged-main and Pages jobs are green.

The deployed five assets and root are byte-exact to merged source. Real Chrome checks 36 reports at 1280, 390 and 320 pixels, every policy/vertex selection in those controls, 12 completed JSON downloads verified by the native checker and 42 unmasked pixel states. This is classical normalized discounted occupancy-measure planning for one supplied expected-cost constraint, limited to four states and eight total actions. It is not a new algorithm, learned model, scale benchmark, per-trajectory safety guarantee or combination with the separate rectangular-robust planner. Shared theory/schema/tie conventions mean agreement is evidence, not a formal proof.

[Live occupancy inspector](https://midya8.github.io/bellmanlab/) · [Source](https://github.com/midya8/bellmanlab) · [Exact contract and source ledger](https://github.com/midya8/bellmanlab/blob/main/OCCUPANCY.md) · [Pull request](https://github.com/midya8/bellmanlab/pull/1)


## BellmanLab 0.5: two budgets, one policy

Two separately achievable budgets can still be impossible together. The new exact inspector keeps both expected costs visible and enumerates the full feasible occupancy vertices, not only their two-dimensional projection. One original three-action control needs a mixture of three deterministic policies: weights 5/12, 1/3 and 1/4 attain reward 3/2 under ceilings 1/3 and 1/4, while the best feasible deterministic policy earns zero. A different control has separately attainable ceilings but a checked joint infeasibility gap of 1/6. Visit rates reweight an initial policy mixture into local action probabilities; a feasible reward/cost projection alone is not a full policy witness.

The dependency-free Python generator returns every deterministic policy, every feasible full vertex, all optimal vertices, an exact full-occupancy mixture and a re-solved stationary policy. A separate checker uses Cramer/determinant solves and one-, two- and three-policy simplex intersections rather than generator helpers. Bellman action inequalities, two nonnegative multipliers and complementary slackness certify feasible optima; a weighted minimum-cost bound certifies joint impossibility. Valid alternative multiplier witnesses are accepted. An independent BigInt browser engine agrees on 822 complete reports, including a dense four-state case beyond JavaScript's safe integer range. Actual SciPy 1.15.3 HiGHS checks all 822 problems: 692 feasible and 130 infeasible, with worst reward error below 4.5e-10.

Reproduction retains the original and one-budget workflows: 103 Python tests, eight Node tests, 958 rejected non-input primitive-leaf mutations and isolated installed-wheel checks of both new CLI entrypoints. Actual deployed Chrome checks 36 control reports, 108 policy selections, 117 vertex selections, three extra dense reports and twelve trusted completed downloads replayed by the native checker at 1280/390/320 pixels. All ten deployed assets match merged source; 42 full unmasked captures match the inspected local rendering. Feature, pull-request, merged-main and Pages checks are green.

This is exact classical occupancy-measure planning for a supplied discounted MDP, limited to one-to-four states, eight total actions and exactly two expected-cost ceilings. Budgets are expectations under the supplied initial distribution, not trajectory caps or real-world safety guarantees. It is not learned, scalable, combined with the separate robust planner, or a new algorithm. Shared mathematical assumptions mean cross-checks are evidence rather than formal proof.

[Two-budget inspector](https://midya8.github.io/bellmanlab/coupled.html) · [Source](https://github.com/midya8/bellmanlab) · [Derivation, limits and source ledger](https://github.com/midya8/bellmanlab/blob/main/COUPLED.md) · [Reviewed change](https://github.com/midya8/bellmanlab/pull/2)
