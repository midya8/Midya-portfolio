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
