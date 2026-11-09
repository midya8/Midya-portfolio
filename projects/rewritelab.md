# RewriteLab

## RewriteLab: a shortcut can need a larger detour

[Live inspector](https://midya8.github.io/rewritelab/) · [Source and reproduction](https://github.com/midya8/rewritelab) · [Merged PR](https://github.com/midya8/rewritelab/pull/1)

An exact, deliberately small arithmetic-optimization lab for inspecting the boundary between rewrite reachability and algebraic equivalence. Enumerate the whole bounded rewrite graph, inspect a shortest proof for every reachable tree, then compare it with every polynomial-equivalent tree in the same finite grammar.

- **A blocked shortcut:** `x*(1+1)` has two reachable five-node-budget terms costing 5, while `x+x` costs 3. Seven nodes unlock a three-rewrite distributive bridge to the cheaper term.
- **A limit that remains:** `(1+1)*(1+1)` with multiplication cost 8 has one reachable term costing 14 at seven nodes. The separate complete semantic census contains six terms and an addition-only optimum costing 7.
- **Independent evidence:** separate rule-template/grammar enumeration checks every proof edge, outgoing closure and shortest-distance inequality. Exact evaluation on a 5-by-5 grid proves polynomial identity for this degree-bounded grammar; it is not empirical sampling. The generator instead uses polynomial coefficient maps.
- **Inspect it all:** eight controls, all reachable proofs and semantic candidates, tree/distance views, positive occurrence costs, stale-state clearing and JSON evidence export.

Finite ordered binary trees over `0,1,x,y,+,*`, bounded to 3, 5 or 7 nodes: 36, 548 or 10,788 grammar terms. Bidirectional commutativity, associativity, identities, zero annihilation and distribution/factoring act at every subtree. Reverse zero can introduce any fitting grammar term, not just a source variable. Larger and non-improving intermediate terms are retained if they fit.

This is an explicit bounded rewrite graph, not an e-graph, tensor engine, floating-point compiler proof, learned policy, runtime-speedup result or novel optimization algorithm. Exact rational algebra need not preserve IEEE floating-point behavior. The seven-node cap is a real exponential-enumeration limit; no claim applies beyond the stated grammar, rules and budget.

Verified release: 25 exact public source files; 11 Python tests on 3.10-3.13; three Node/actual-Chrome tests; 72 complete cross-language reports with 111,316 proof rows and 111,342 semantic rows; a fresh installed wheel with eight complete module/console controls and forged-report rejection. Live Chrome checks 26 reports, all 3,612 proof and 3,630 semantic selections, eight controls at 320/390/1280 widths, blocked/detour/weighted/three-node states, export and errors. All five deployed assets match main. Feature, PR, main and Pages checks pass. [Exact contract](https://github.com/midya8/rewritelab/blob/main/CONTRACT.md) and [primary sources and distinctions](https://github.com/midya8/rewritelab/blob/main/SOURCES.md) state what was checked and what was not.

## Why it belongs in an AI portfolio

Algebraic rewrites and cost-guided extraction are part of AI compiler and tensor-graph optimization. This lab isolates one inspectable question without pretending to run a tensor compiler: can a cheap equivalent expression fit the grammar but remain unreachable because its rewrite bridge is too large? The source notes distinguish this explicit finite graph from equality-saturation systems such as egg/TENSAT and from TASO, Herbie and Alive2.


## RewriteLab budget barriers: when fitting is not reaching

[Live budget-barrier atlas](https://midya8.github.io/rewritelab/barriers.html) · [Source](https://github.com/midya8/rewritelab) · [Exact filtration contract](https://github.com/midya8/rewritelab/blob/main/BARRIERS.md) · [Merged change](https://github.com/midya8/rewritelab/pull/2)

The atlas retains every 3/5/7-node closure through the chosen cap and every
polynomial-equivalent candidate. It separates the first budget that fits both
source and target from the first budget that admits a rewrite proof. Each
blocked lower level has a complete closure obstruction, and each first-reachable
level has a shortest proof within that level. Source-too-large and
target-too-large are not mislabeled as blocked.

For `x*(1+1) -> x+x`, first fitting is 5, first reachable is 7, extra budget is
2 and shortest distance is 3. Thirteen of its 213 cap-7 semantic candidates
need a larger bridge. The weighted constant product is still a counter-control:
five of six candidates remain unreached through seven nodes. Leaf `x` first
has allowed budget 3, but its zero-step path has actual peak 1. Null means
not reached through the cap, not impossible at every larger budget.

Independent verification first checks every nested full closure with separate
generic rule templates and exact 25-point degree-bounded signatures, then
independently enumerates candidates and budget labels. It imports no atlas
generator, forward search or coefficient maps; the syntax/size/cost contract
and base independent verifier are shared. A test-only heap directly minimizes
peak-node labels through the independent template graph for all semantic
candidates of six sources.

Fresh public feature/main reproduction: 35 files source-exact; 20 tests on
Python 3.10-3.13; six Node/actual-Chrome tests; installed eight controls per
family through module and console outside the checkout, with forgeries rejected.
36 complete Python/JS atlases compare 13,016 candidate rows and 13,745 nested
proof rows. Chrome checks 25 atlases and every 3,844 candidate selection, all
five level states, three widths, export, cap changes and invalidation. Base
72 full cross-language reports and all base browser checks remain intact.
Feature/PR/main CI and Pages pass; nine deployed assets match main and 57
feature/main/live screenshots match without masks.

This is the least allowed budget in a fixed small grammar, not a new minimax
algorithm, e-graph, learned policy, tensor compiler or runtime benchmark. A
shortest proof at that budget need not be globally shortest across larger
budgets, and its peak need not equal the allowed budget. Reachable and semantic
optima each fall or stay fixed as the budget grows; their difference need not.
No result above the cap or IEEE floating-point equivalence is claimed.


## RewriteLab cost atlas: one graph, every cost tradeoff

[Live cost-weight atlas](https://midya8.github.io/rewritelab/weights.html) · [Source](https://github.com/midya8/rewritelab) · [Exact weight-box contract](https://github.com/midya8/rewritelab/blob/main/WEIGHTS.md) · [Merged change](https://github.com/midya8/rewritelab/pull/3)

A fixed rewrite graph can have different cheapest answers under different
operator costs. This atlas keeps all 512 positive integral (+, multiplication,
leaf) weight triples in 1..8. Every semantic expression is retained in an exact
operation-count group, together with its complete reachable subset. Every
outcome retains exact optimum ties and the cost gap. The accessible 8×8 slice
changes leaf cost without running another search; all optimum ties and group
members remain selectable.

For constant four, product vector (2 additions, 1 multiplication, 4 leaves)
competes with addition-only vector (3, 0, 4). They tie exactly when addition
and multiplication costs agree. There are 224 positive-gap triples, 288 with
zero gap and 64 ties. Each semantic group wins at 288 triples because ties
credit both, so win counts are not a probability partition. By contrast, the
five-node bridge source is strictly dominated by blocked `x+x` and has a gap
at all 512 triples. No crossover is invented for a dominated pair.

The independent checker validates a full unit-cost closure, counts canonical
syntax symbols separately from the generator's recursive tree traversal, and
rebuilds every group, reachable subset, weight outcome, tie, gap, dominator
and win count. Shared syntax and base independent closure checking are named
explicitly. All 512 ordinary optimize reports, including full expanded
expression ties, are cross-checked for both the constant crossover and the
blocked bridge. Strict positive-weight dominance is kept separate from zero
wins inside this finite box; absence of a box win is not a global impossibility.

Fresh public feature and main clones match all 45 source files and tracked
paths. There are 27 Python tests across 3.10-3.13 and nine Node/actual-Chrome
tests. Seventeen complete Python/JS weight reports compare 8,704 outcomes and
93 groups. Chrome checks 25 weight reports, all 4,096 outcome selections and
34,570 expression selections across eight controls and three widths, plus
current-weight export, invalid-selection recovery and stale clearing. Fresh
installed module and console reproduce eight controls each for all three
families outside the checkout and reject forgeries. Base and budget-barrier
checks remain intact. Feature/PR/main CI and Pages pass; all 13 live assets
match main and all 83 feature/main/live screenshots match without masks.

Costs count tree-node occurrences, not shared subexpressions or hardware
latency. This is an exhaustive integral weight box over a fixed seven-node
maximum grammar, not a continuous parameter-region analysis, learned policy,
e-graph, tensor engine, new algorithm or compiler-speed benchmark. The exact
rational identities are not IEEE floating-point transformation licenses.
Browser evidence is independently checked only after Python accepts its JSON.
## RewriteLab continuous regions: beyond a sampled cost grid

[Live explorer](https://midya8.github.io/rewritelab/regions.html) · [Source](https://github.com/midya8/rewritelab) · [Exact region contract](https://github.com/midya8/rewritelab/blob/main/REGIONS.md) · [Merged change](https://github.com/midya8/rewritelab/pull/4)

A finite cost grid cannot prove that an expression never wins elsewhere.
This extension computes complete optimum regions over every strictly positive
addition, multiplication and leaf-cost ratio. Normalizing their sum to one
turns the parameter space into a triangle. Each group's exact halfplanes yield
reduced rational vertices, with full expression memberships and reachable
subsets retained. Semantic and reachable optima have separate regions.

Closed geometry is not a positive-cost verdict. Empty, point, segment and area
regions retain their dimensions. A boundary-only winner is not obtainable at
strictly positive costs; an interior tie point or segment can be a real winner
despite zero area. Shared edges and vertices belong to every tied group. Area
is not a probability. The zero-cost boundary closes the diagram, not the
optimizer's request domain.

The generator uses exact rational polygon clipping. A separate checker instead
constructs feasible supporting-line intersections, counts canonical syntax
symbols and validates the complete nested unit-cost closure. It reconstructs
every group, vertex, dimension and positive-feasibility flag without importing
the generator, clipping or recursive count traversal. Shared syntax and base
independent closure checking are disclosed. JavaScript uses BigInt rational
arithmetic; float coordinates are only a display layer over exact vertex text.

Fresh public feature and main source match all 54 files and tracked paths.
Thirty-five Python tests pass on each of 3.10-3.13, alongside eight Node engine
and four actual-Chrome tests. Seventeen Python/JavaScript region reports agree
on 93 groups and 215 vertices. Independent tests cover all 36 three-node
sources, 500 random vector sets, exact degenerate/interior/boundary cases,
all eight controls at all 512 old grid points, 64 outside-grid positive points,
and forged geometry, types, closure and membership. Installed module and console
reproduce eight controls each in all four families outside the checkout and
reject forgeries.

Chrome checks 25 region reports, all 4,096 point selections and 34,570 expression
selections across eight controls and three widths, complete rational vertex
text, both diagrams per group, export, invalid recovery, stale clearing and
outside-grid prices. All previous inspector, barrier and weight-box checks are
retained. Feature/PR/main CI and Pages pass. All 16 deployed assets match main;
all 111 feature/main/live screenshots match exactly without masks.

The continuous cost domain does not enlarge the expression grammar: fixed
3/5/7-node budgets, rational identities and complete ordered trees still apply.
Costs count tree occurrences, not shared subexpressions or hardware latency.
No new algorithm, e-graph, learned costs, tensor engine, compiler-speed benchmark
or IEEE floating-point transformation license is claimed. Enumeration remains
exponential. Browser evidence is independently checked only after the Python
region checker accepts its complete JSON.
