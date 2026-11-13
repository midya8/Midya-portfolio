# ParetoLab: exact two-cost path planning

ParetoLab compares every path through a small forward graph with two supplied
additive costs. It separates the nondominated paths, the choices a weighted sum
can select, and the paths selected by a hard cost limit. Expected-cost lotteries
answer a different question and can violate the limit on a realized path.

The browser shows exact weight intervals, optimizer ties, epsilon thresholds and
Pareto-label pruning. Export a report and replay it with the Python checker.

[Live inspector](https://midya8.github.io/paretolab/) · [Source](https://github.com/midya8/paretolab) · [Reviewed change](https://github.com/midya8/paretolab/pull/2)

## Three paths, one missing compromise

The developed default has three parallel choices: `(0,12)`, `(7,7)`, `(12,0)`. All minimize two supplied costs. All three are nondominated. For the middle choice to minimize `t*cost1 + (1-t)*cost2` against both extremes, it needs `t >= 7/12` and `t <= 5/12`. The intersection is empty. No finer weight grid can repair that.

Set a hard second-cost ceiling of 7 instead and `(7,7)` is the lexicographic optimum. This is the classical unsupported-efficient-point phenomenon, illustrated with a hand-specified teaching control, not a new theorem or an empirical claim about AI agents.

## Hard constraints and expectations are different problems

Allow random selection of a complete path before execution and bound only expected second cost. Probabilities 7/12 and 5/12 on the two extreme paths yield expected costs `(5,7)`, two below the deterministic first cost. But the first extreme violates the realized ceiling with probability 7/12. The inspector shows that probability, rather than calling the mixture safe.

Every optimal basic singleton/two-path witness is retained. This does not enumerate the continuum of distributions in an optimal face. It is a whole-path lottery, not a per-step stationary randomized policy, discounted occupancy controller or chance constraint.

## Weight intervals and ties

Against each rival path, the weighted-score comparison is an exact linear inequality in `t`. Reduced rational half-lines intersect with `[0,1]`; their endpoints define point cells and open intervals with constant optimizer identities. The midpoint is a witness, not a grid approximation.

Positive-weight support means optimal for some `0<t<1`. Closed support includes endpoints separately. A dominated path may minimize at `t=0` or 1 because one objective is ignored; it is never promoted to the Pareto frontier. A nondominated collinear point optimal at a single interior weight does count as supported. Equal-cost edge sequences keep separate path IDs.

Raw objective units are used, with no automatic normalization. Positive rescaling preserves existence of support but moves weight breakpoints. The tests verify an exact weight reparametrization, not only unchanged frontier membership.

## Prune labels without losing tradeoffs

The reverse-node dynamic program extends every nondominated child suffix along every outgoing edge. Each local candidate has its own dominators and kept/discarded flag. Strictly dominated suffixes can be pruned because adding the same prefix preserves dominance; equal-cost identities remain.

The complete full-path census remains separate from that local trace. It includes extensions of already-pruned child suffixes, which are absent from a node's local candidate table. Both the local evidence and complete suffix counts are visible.

## Replay and its limits

The Python checker imports input validation only. Forward path enumeration replaces reverse suffix construction. A complete objective-line arrangement replaces the producer's support clipping as its classification cross-check. Independently classified complete child paths reconstruct local labels. Separate 2x2 determinants reconstruct mixture probabilities. Full canonical comparison rejects altered leaves, shapes, ordering, types and rational spelling.

The browser replay changes census traversal but shares evidence construction. It is not labeled an independent checker. Shared definitions, parser rules and tie conventions can still share mistakes across languages. Exported consistency establishes arithmetic relative to the included input, not the provenance or practical suitability of those costs.

## Reproduction checks

| Check | Observed result |
|---|---|
| Python suite | 20 tests |
| Exhaustive small universe | 729 ordered three-path profiles over all 9 vectors in 0..2 |
| Complete native/browser parity | 52 reports; 101 paths; 176 weight cells; 130 thresholds |
| Primitive tampering | 579 rejected forgeries per engine |
| Input-built numeric reference | 556 HiGHS graph-MILP/probability-LP solves; 2,403 rows; maximum objective error 8.9e-16 at 1e-8 tolerance, SciPy 1.15.3 |
| Installed wheel | 6 module origins; 12 controls; 2 entrypoints; 24 CLI forgeries |
| Actual Chrome | 48 responsive views; 220 path selections; 208 weight cells; 180 budget states; 324 label rows |
| Native downloads | 12 inputs and 12 certificates; each certificate independently replayed by Python |

The graph reference builds binary arc-flow constraints from original input, not expected path answers. Its LP separately checks expected-cost optima and lexicographic ties. It checks objective values, not every optimizer identity or report field. The 729-profile audit checks that the finite epsilon sweep recovers exactly the deterministic frontier. Twelve controls are developed, 40 DAGs are seeded, neither is held-out empirical planning evaluation.

## Publication status

The documentation review is published in [PR #2](https://github.com/midya8/paretolab/pull/2), main `3f0c8c45d8c8f79ef9cf83a89bac41beb2e5dde2`. Fresh checkouts of the head and merged main matched all 31 reviewed files and passed 20 Python tests, 4 Node/Chrome tests, installed-wheel reproduction and generated-asset checks. Both [head CI runs](https://github.com/midya8/paretolab/actions/runs/43352068342), [main checks](https://github.com/midya8/paretolab/actions/runs/43352218546) and [Pages deployment](https://github.com/midya8/paretolab/actions/runs/43352218579) passed. Five live assets match main. The full deployed Chrome workflow passed 48 views and 24 downloads with native certificate replay. Of 40 live screenshots, 39 match local pixels exactly; one 768px hero differs at 25 pixels, with no content or layout difference on inspection. Desktop/mobile review also covers the budget comparison and label-pruning table. These checks identify the implementation, not the validity of supplied costs.

## Scope and established work

2..7 topologically ordered nodes, at most 12 forward arcs, two additive nonnegative integer costs 0..20 and at most 64 complete suffix paths per node. Parallel arcs and disconnected graphs are valid. No cycles, model learning, general multiobjective RL, real routing, practical safety, scalable solve or new-algorithm claim. The tool cannot validate supplied costs.

[Bergman et al.](https://arxiv.org/html/1802.08637) ground network-based discrete multiobjective optimization; [Demeyer et al.](https://backoffice.biblio.ugent.be/download/4410352/4410359) ground Pareto path labels; [Roijers et al.](https://www.fransoliehoek.net/docs/Roijers15JAIR.pdf) connect linear/Pareto coverage and expected mixtures to AI decisions. Existing [pymoo](https://pymoo.org/mcdm/) and [discopt](https://kitchingroup.cheme.cmu.edu/discopt/autoapi/discopt/mo/scalarization/index.html) are credited, not claimed to be outperformed. The full six-source ledger is in the repository.

The portfolio's BellmanLab already studies discounted expected-cost occupancy control; MatchLab includes assignment/blocker frontiers. This project is specifically the additive DAG path-support audit, not a claim that Pareto frontiers or mixtures are new portfolio ideas.
