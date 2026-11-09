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
