# VariLab: inference objectives, curvature and compatible decisions

[Source repository](https://github.com/midya8/varilab)

VariLab compares inference questions on supplied Ising models: approximate a joint distribution, inspect curvature, condition on evidence or choose a compatible joint MAP assignment. Each calculation exposes its arithmetic and work limits. Fields and couplings are inputs, not learned parameters.

## A better objective can give worse marginal means

Two spins have zero fields and coupling `J=3`. The target favors aligned states, almost equally split between `(-1,-1)` and `(1,1)`. Exact means are zero; exact cross-covariance is `tanh(3)=0.995055`. Three product-distribution runs change only the initial means, using the same ascending sequential coordinate order, 100-sweep cap and `1e-12` sweep-change tolerance.

| Start | Final spin means | ELBO | Reverse KL | Maximum mean error | Stop rule |
|---|---|---:|---:|---:|---|
| Zero | `(0,0)` | 1.386294 | 2.309329 | 0.000000 | Met, 1 sweep |
| Positive `.1` | `(.994902,.994902)` | 3.005027 | 0.690596 | 0.994902 | Met, 7 sweeps |
| Negative `-.1` | `(-.994902,-.994902)` | 3.005027 | 0.690596 | 0.994902 | Met, 7 sweeps |

The higher-ELBO runs have lower reverse KL but worse marginal means. All product approximations miss the target's nonzero cross-covariance. The symmetric run stops with zero coordinate residual and gradient, yet it is not an ELBO maximum: a small joint positive perturbation raises the objective. A stopping rule alone does not certify local/global optimality or useful marginals.

The separate no-edge control is exactly representable by the product family: means match `tanh(fields)` to floating precision. Its `max_mean_error <= 1e-6` gate passes; the positive-start coupled gate fails. Both directions are asserted and displayed. The targets, coupling and starts were directly specified without seed, parameter or checkpoint search. This is a constructed counterexample, not an empirical method ranking.

## A curvature certificate, not an optimizer claim

The `curvature(model, means)` API and strict CLI return the analytic ELBO Hessian at supplied interior means using exact fractions of the compiled binary-float inputs. Symmetric congruence returns `T`, block-diagonal `D`, exact positive/negative/zero eigenvalue counts and signed rational directions with quadratic forms; the independently checked identity is `T^T H T = D`. A nonzero diagonal uses a scalar pivot, an all-zero diagonal with an off-diagonal entry uses a 2x2 pivot, and a zero remainder records nullity. No numerical eigenvalue threshold is used.

At `J=3,m=0`, inertia is `(1,1,0)` and direction `(3,1)` has exact positive form `8`, so the coordinate fixed point is a saddle. At the existing broken-symmetry fitted point, inertia is `(0,2,0)`. At `J=1,m=0`, it is `(0,1,1)`; the immediately adjacent representable couplings below and above 1 have `(0,2,0)` and `(1,1,0)`. The fixture uses those direct neighbors, not a search. The figure embeds complete rational certificates and plots all counts on one scale. Inertia preserves signs, not eigenvalue magnitudes.

The returned gradient is floating point; negative-definite curvature does not establish exact stationarity or a maximum. Singular points receive no higher-order verdict. This is curvature at represented inputs, not an interval enclosure or uncertainty calibration. It uses cubic rational-operation work and quadratic storage for at most 12 spins, with variable integer bit costs and no runtime guarantee. The finite-state reference remains floating point and is not silently rebranded as rational arithmetic.

```sh
python -m varilab curvature-demo
python -m varilab curvature examples/coupled.json --means '[0,0]'
PYTHONPATH=. python examples/render_curvature.py --check
```

## What to run

| Question | API | Arithmetic and cap |
|---|---|---|
| Full state reference or product approximation | `exact`, `mean_field`, `compare` | Floating enumeration/coordinate ascent, 12 spins |
| Hessian sign counts | `curvature` | Rational congruence at represented interior means, 12 spins |
| Condition an acyclic model | `forest` | Floating sum-product, 128 spins |
| Compatible forest MAP and tie counts | `forest_map` | Rational max-sum, 128 spins |
| Bounded cyclic conditional query | `elimination_plan`, `eliminate` | Symbolic preflight, floating log-sum-exp, 64 spins |
| Cyclic joint MAP and tie counts | `cyclic_map` | Same preflight, rational max-sum/traceback, 64 spins |

```sh
python -m varilab demo
python -m varilab exact examples/coupled.json
python -m varilab compare examples/coupled.json --initial '[0.1,0.1]'
python -m unittest discover -s tests -v
for name in audit curvature forest map elimination cyclic_map; do
  PYTHONPATH=. python examples/render_$name.py --check
done
```

A standalone wheel contains nine runtime modules. All 15 CLI modes and console
entry points match the source checkout outside the source directory. The runtime
and tests use only Python's standard library. No API, GPU, network, external data
or model download is needed.

## The boundary of the claim

For the finite-state reference, "exact" means every finite state is enumerated using floating-point log-sum-exp, not exact rational/outward-rounded arithmetic. Target probability underflow retains finite logs; product zero masses have null log probability. Tiny rounding errors in normalization, KL or covariance remain possible. `tanh` can saturate at endpoints.

Enumeration, mean-field and curvature models have 1..12 spins (forest allows 1..128), finite fields/weights with magnitude at most 100 and strictly indexed nonduplicate edges. JSON files are capped at 256 KiB. Reference work `2**n*(n+edges+n*n)` is capped at 786,432; requested fitting work `sweeps*n*(n+edges)` is capped at 500,000, with at most 1,000 sweeps. Errors do not return partial results. These counts are operational limits, not timing promises.

There is no arbitrary-dimensional exact inference, likelihood fitting, parameter learning, richer variational family, stochastic optimizer, convergence proof or calibrated uncertainty claim. Standard ELBO/KL and coordinate-ascent principles follow [Blei, Kucukelbir and McAuliffe (2017), sections 2.2-2.4](https://www.cs.columbia.edu/~blei/papers/BleiKucukelbirMcAuliffe2017.pdf). The Ising reduction, code, supplied synthetic examples, independent test references and figures are original implementations. [Derivation and accounting](https://github.com/midya8/varilab/blob/main/DESIGN.md).

The congruence/inertia principle follows [Nick Higham (2022)](https://nhigham.com/2022/12/06/what-is-the-inertia-of-a-matrix/); implementation, exact certificates and boundary fixtures are independent.

For portable regeneration, the curvature figure fixes the captured broken-symmetry binary means to `0.9949015284526289`. It includes the complete rational certificate but omits the separate libm-dependent float gradient diagnostic; that diagnostic remains in the API. No curvature values are rounded for sign decisions.


## Evidence-aware inference without a full joint table

`forest(model, evidence=[{'i':0,'spin':1}])` adds exact two-pass log sum-product for acyclic supplied Ising graphs up to 128 spins. Outputs include every conditional singleton marginal, every stored edge's four-state joint/moment/covariance, root/component log partitions, all directed messages and dependency sets, unconditional log partition and evidence probability/log probability. Cycles (including zero-weight cycles) and invalid/duplicate evidence are rejected before messages. Disconnected forests, isolated nodes and complete observations are supported. Clamped impossible states have probability zero and null logs; underflowed possible events retain finite logs. The existing enumeration, mean-field and curvature paths retain their 12-spin caps.

A direct four-node zero-field J=2 chain has prior means zero. Observing its first spin as +1 gives means `(1,0.964028,0.929349,0.895918)`, analytically `tanh(2)^distance`, with evidence probability 0.5. An endpoint >0.8 gate passes with evidence and fails without it: different queries, not a method benchmark. A direct 128-node chain returns 254 directed messages without enumerating its state table. No timing claim is made. Cavity recomputation and serialized dependencies give `O(n+sum degree^2)` work/output, bounded by the 128-spin cap; this implementation does not claim linear complexity. Conditioning is not causal intervention and the graph is not learned.

The forest SVG uses small-chain analytic values rounded to 12 decimals for
portable geometry; full float messages remain in the demo. This does not make
floating messages rational certificates. Sum-product follows [Zemel and Urtasun, CSC412 exact inference lectures (2016)](https://www.cs.toronto.edu/~duvenaud/courses/csc412/lectures/05-exactInference.pdf); implementation and test references are independent.

```sh
python -m varilab forest-demo
python -m varilab forest examples/coupled.json --evidence '[{"i":0,"spin":1}]'
PYTHONPATH=. python examples/render_forest.py --check
```


## A compatible joint decision, with exact tie counts

`forest_map` and `map` / `map-demo` add max-sum decoding with exact fractions of compiled binary-float potentials, not original decimal text. They return a compatible optimal assignment and separately recomputed score, exact maximizing count/uniqueness, component scores/counts, singleton constrained global optimum scores/counts/gaps, all directed message scores/counts/source-spin choices and full parent-conditioned traceback. Forbidden clamped states have null score/gap and zero count; no tolerance decides a tie. Validation, cycle rejection and 128-spin topology are shared with sum-product, whose ordinary probability arithmetic is unchanged.

Directly constructed h=(1/4,63/256), J=-2 has two unique ordinary marginal modes +1, with P(+1) about 0.506550 and 0.502723. Their joint (+1,+1) scores -385/256. The unique joint MAP (+1,-1) scores 513/256, exact gap 449/128=3.5078125. Both demo gates are asserted: compatible decoding reaches the optimum; independent marginal modes do not. This distinguishes decision questions rather than ranking algorithms. A separate symmetric zero-field J=-2 example has two global optima: all local max-marginals permit either spin, but independent first choices (-1,-1) are incompatible. Stored parent-conditioned traceback chooses (-1,+1), an actual optimum. The deterministic local first-compatible tie rule is not a global lexicographic or relabel-invariant witness rule.

A 128-isolated-spin fixture counts exactly 2^128 maximizing assignments without enumeration. Recomputed cavities plus serialized dependencies cost O(n+sum degree^2) rational/count operations and output entries; variable integer bit costs matter, and no timing claim is made. Singleton scores/counts include other disconnected components. Scores are not probabilities; this forest MAP path makes no parameter learning, top-k or causal claim. The fourth SVG plots both signed scores on one zero scale and embeds complete rational scores/counts/traceback certificates; only ordinary marginal-probability labels are rounded to 12 decimals for portability.

Max-sum and backtracking follow [University of Washington CSE515 max-product lecture (2020)](https://courses.cs.washington.edu/courses/cse515/20wi/maxprod.pdf); code, rational multiplicity accounting, fixtures and independent test references are original.

```sh
python -m varilab map-demo
python -m varilab map examples/coupled.json --evidence '[{"i":0,"spin":1}]'
PYTHONPATH=. python examples/render_map.py --check
```


## Cyclic queries without hiding intermediate-factor cost

`elimination_plan` symbolically plans scopes and exact table-work counters before numeric factor allocation. `eliminate` executes accepted plans for supplied Ising graphs including cycles, up to 64 spins and 8 unobserved query indices, with disjoint hard evidence and either an exact supplied nonquery elimination permutation or deterministic min-fill (missing neighbor edges, then degree, then index). It returns the evidence-restricted log partition, normalized conditional joint query table, every produced factor's complete log values, final unnormalized values and matching planned/executed counters. The rightmost sorted query index changes fastest. This is float log-sum-exp, not rational arithmetic or normalized evidence probability.

The directly specified 16-node zero-field star with J=1/2 exposes order dependence on the same partition query. Hub first needs 65,536 bucket assignments and is refused before numeric tables; min-fill peaks at 4 and matches analytic log Z 12.892072. A separate 64-node cycle answers joint query [0,1] at peak 8, with log Z 52.048748 and adjacent moment 0.462117 matching independent transfer-matrix formulas. Both resource gates are asserted. A refused order is not an impossible graph, and min-fill is a heuristic rather than an optimal-treewidth proof or speed benchmark.

Fixed caps are 4,096 peak assignments (including larger initial/final tables), 250,000 scalar factor-entry reads and 65,536 total initial/intermediate/final output entries. The plan exposes every input factor ID, bag, output scope and step counter. Constants from evidence are retained; zero-weight stored edges remain conservatively in symbolic scopes. Rejected plans remain inspectable, but execution returns no partial inference. Counters exclude set/index/transcendental/Python-object costs and are not seconds, FLOPs or memory bytes. Query probabilities may underflow while retaining finite log probabilities. The sum-product path does not perform MAP. Neither path claims arbitrary-factor, learned, causal or unbounded inference.

The cyclic sum-product SVG embeds complete symbolic metadata and rounds float
display labels to 12 decimals; full numerical traces remain in the demo. Variable elimination and scope accounting follow [Zemel and Urtasun, CSC412 exact inference lecture (2016)](https://www.cs.toronto.edu/~duvenaud/courses/csc412/lectures/05-exactInference.pdf); code, explicit resource contract, fixtures and independent references are original.

```sh
python -m varilab elimination-demo
python -m varilab plan examples/coupled.json --query '[1]'
python -m varilab eliminate examples/coupled.json --query '[1]' --evidence '[{"i":0,"spin":1}]'
PYTHONPATH=. python examples/render_elimination.py --check
```


## Cyclic decisions need compatible separator choices

![Triangle local-choice failure and exact odd-ring MAP certificate](https://raw.githubusercontent.com/midya8/varilab/main/assets/cyclic-map-audit.svg)

```sh
python -m varilab cyclic-map-demo
python -m varilab cyclic-map examples/coupled.json --query '[1]' --evidence '[{"i":0,"spin":1}]'
PYTHONPATH=. python examples/render_cyclic_map.py --check
```

`cyclic_map(model, query=..., evidence=..., order=...)` uses the existing 64-spin symbolic planner and all three table-work caps, but performs exact rational max-sum rather than float log-sum-exp. Each factor cell carries a best score, an integer count of compatible maximizing eliminated assignments, and all maximizing eliminated spins. A query row gives the full-graph optimum score/count conditional on that query state, its exact gap, and whether it reaches the global optimum. Final maximization includes query spins too. This is **joint MAP, not marginal MAP**: no variable is summed out, and scores/counts are not probabilities. Fractions represent the compiled binary-float inputs, not the original decimal strings.

The directly specified zero-field triangle has all three couplings -1. Every singleton permits both spins in a global optimum, but independent first choices (-1,-1,-1) score -3. Compatible reverse traceback reaches score +1, a gap of 4; there are six global optima, not a unique answer. A separate 63-spin odd ring with the same couplings has exact score 61 and 126 optima, matching the independent formula n-2 and 2*n: pick one unsatisfied edge and a global spin flip. Its peak is 8 bucket assignments. The 16-star order-control demo still rejects hub-first and accepts min-fill; both gate directions are asserted. Graphs, couplings and orders are directly specified, not searched or timed.

The result includes the complete symbolic plan, every produced rational score/count/choice table, a chosen query state, reverse traceback with actual separator context, the full compatible assignment and separately recomputed score. Equal scores use rational equality, never a tolerance. Ties pick the first sorted query state, then first compatible stored spin in reverse elimination order. The witness is deterministic for that plan, **not globally lexicographic or order-invariant**. Counts include disconnected components and eliminated-variable multiplicities. The planner's counters still count table-cell reads/outputs, not scalar arithmetic operations: rational numerator/denominator and count bit lengths, choice arrays, traceback, serialization and object overhead cost more. No time, RAM-byte, optimal-treewidth, learning or causal claim follows.

MAP elimination and traceback follow [University of Washington CSE515 max-product lecture (2020)](https://courses.cs.washington.edu/courses/cse515/20wi/maxprod.pdf); rational multiplicity accounting, implementation, fixtures and independent tests are original.


## Checks and limits

The current suite has **183 tests and six reproducible SVGs**. Independent
references include direct exponentials on 216 three-spin targets, an inertia
oracle over 729 symmetric matrices, 324 enumerated conditioned forest cases,
972 Fraction enumerations for each MAP path and 432 cyclic
model/evidence/query/order combinations. Tests reconstruct per-update objectives,
messages, factor scopes, score/count tables and compatible traceback. They check
resource boundaries before numeric allocation, underflow/subnormal cases,
validation, deterministic outputs, isolation and strict CLI behavior.

All six figures regenerate from demo data. Tests inspect plotted values,
geometry and complete metadata, and reject changed fixtures. These are finite
implementation checks, not all-input proofs, speed benchmarks or a ranking of
inference methods. Rational certificates concern represented binary-float
inputs, not decimal intentions or uncertain data. Scores/counts are not
probabilities; conditioning is not intervention; cyclic joint MAP is not
marginal MAP. A rejected plan is a resource refusal, not an impossible query.
