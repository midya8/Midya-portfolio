# ParetoLab: the compromise a weighted sum misses

**Nondominated does not mean selected by any positive weighted sum.** ParetoLab makes finite biobjective AI planning inspectable: every additive DAG path, exact scalarization interval, optimizer tie, epsilon threshold and Pareto-label pruning witness. Supplied costs, not learned preferences.

[Live inspector](https://midya8.github.io/paretolab/) · [Source](https://github.com/midya8/paretolab) · [Reviewed change](https://github.com/midya8/paretolab/pull/1)

## Three paths, one missing compromise

The developed default has three parallel choices: `(0,12)`, `(7,7)`, `(12,0)`. All minimize two supplied costs. All three are nondominated. For the middle choice to minimize `t*cost1 + (1-t)*cost2` against both extremes, it needs `t >= 7/12` and `t <= 5/12`. The intersection is empty. No finer weight grid can repair that.

Set a hard second-cost ceiling of7 instead and `(7,7)` is the lexicographic optimum. This is the classical unsupported-efficient-point phenomenon, illustrated with an original teaching control, not a new theorem or an empirical claim about AI agents.

## Hard constraints and expectations are different problems

Allow random selection of a complete path before execution and bound only expected second cost. Probabilities7/12 and5/12 on the two extreme paths yield expected costs `(5,7)`, two below the deterministic first cost. But the first extreme violates the realized ceiling with probability7/12. The inspector shows that probability, rather than calling the mixture safe.

Every optimal basic singleton/two-path witness is retained. This does not enumerate the continuum of distributions in an optimal face. It is a whole-path lottery, not a per-step stationary randomized policy, discounted occupancy controller or chance constraint.

## Every weight, every tie

Against each rival path, the weighted-score comparison is an exact linear inequality in`t`. Reduced rational half-lines intersect with`[0,1]`; their endpoints define point cells and open intervals with constant optimizer identities. The midpoint is a witness, not a grid approximation.

Positive-weight support means optimal for some`0<t<1`. Closed support includes endpoints separately. A dominated path may minimize at`t=0` or1 because one objective is ignored; it is never promoted to the Pareto frontier. A nondominated collinear point optimal at a single interior weight does count as supported. Equal-cost edge sequences keep separate path IDs.

Raw objective units are used, with no automatic normalization. Positive rescaling preserves existence of support but moves weight breakpoints. The tests verify an exact weight reparametrization, not only unchanged frontier membership.

## Prune labels without losing tradeoffs

The reverse-node dynamic program extends every nondominated child suffix along every outgoing edge. Each local candidate has its own dominators and kept/discarded flag. Strictly dominated suffixes can be pruned because adding the same prefix preserves dominance; equal-cost identities remain.

The complete full-path census remains separate from that local trace. It includes extensions of already-pruned child suffixes, which are absent from a node's local candidate table. Both the local evidence and complete suffix counts are visible.

## Independent replay, not self-approval

The Python checker imports input validation only. Forward path enumeration replaces reverse suffix construction. A complete objective-line arrangement replaces the producer's support clipping as its classification cross-check. Independently classified complete child paths reconstruct local labels. Separate2x2 determinants reconstruct mixture probabilities. Full canonical comparison rejects altered leaves, shapes, ordering, types and rational spelling.

The browser replay changes census traversal but shares evidence construction. It is not labeled an independent checker. Shared definitions, parser rules and tie conventions can still share mistakes across languages. Exported consistency establishes arithmetic relative to the included input, not the provenance or practical suitability of those costs.

## Bounded reproduction

| Check | Observed result |
|---|---|
| Python suite |20 tests |
| Exhaustive small universe |729 ordered three-path profiles over all9 vectors in0..2 |
| Complete native/browser parity |52 reports;101 paths;176 weight cells;130 thresholds |
| Primitive tampering |579 rejected forgeries per engine |
| Input-built numeric reference |556 HiGHS graph-MILP/probability-LP solves;2,403 rows; maximum objective error8.9e-16 at1e-8 tolerance, SciPy1.15.3 |
| Installed wheel |6 module origins;12 controls;2 entrypoints;24 CLI forgeries |
| Actual Chrome |48 responsive views;220 path selections;208 weight cells;180 budget states;324 label rows |
| Native downloads |12 inputs and12 certificates; each certificate independently replayed by Python |

The graph reference builds binary arc-flow constraints from original input, not expected path answers. Its LP separately checks expected-cost optima and lexicographic ties. It checks objective values, not every optimizer identity or report field. The729-profile audit checks that the finite epsilon sweep recovers exactly the deterministic frontier. Twelve controls are developed,40 DAGs are seeded, neither is held-out empirical planning evaluation.

## Publication status

Source PR1 merged after all six latest feature/PR jobs passed. Current main `c88f08ac58174f84b34215f8cd9c84afff19b559` retains the initial commit, full feature history and merge. All31 public files match checked local source. [Merged-main checks](https://github.com/midya8/paretolab/actions/runs/42915096408) and [Pages deployment](https://github.com/midya8/paretolab/actions/runs/42915096516) passed. Five deployed assets are byte-exact. The full48-view/24-native-download Chrome workflow passed against the live site, including independent Python replay. Of40 unmasked captures,39 are pixel-identical; the remaining768px hero differs at18 border-antialias pixels by at most2/255 per channel. Both actual images were inspected with no content/layout difference. Live desktop hero, phone budget, weight atlas and320px label trace were inspected directly. These checks identify this implementation, not the validity of supplied costs.

## Scope and established work

2..7 topologically ordered nodes, at most12 forward arcs, two additive nonnegative integer costs0..20 and at most64 complete suffix paths per node. Parallel arcs and disconnected graphs are valid. No cycles, model learning, general multiobjective RL, real routing, practical safety, scalable solve or new-algorithm claim. The tool cannot validate supplied costs.

[Bergman et al.](https://arxiv.org/html/1802.08637) ground network-based discrete multiobjective optimization; [Demeyer et al.](https://backoffice.biblio.ugent.be/download/4410352/4410359) ground Pareto path labels; [Roijers et al.](https://www.fransoliehoek.net/docs/Roijers15JAIR.pdf) connect linear/Pareto coverage and expected mixtures to AI decisions. Existing [pymoo](https://pymoo.org/mcdm/) and [discopt](https://kitchingroup.cheme.cmu.edu/discopt/autoapi/discopt/mo/scalarization/index.html) are credited, not claimed to be outperformed. The full six-source ledger is in the repository.

The portfolio's BellmanLab already studies discounted expected-cost occupancy control; MatchLab includes assignment/blocker frontiers. This project is specifically the additive DAG path-support audit, not a claim that Pareto frontiers or mixtures are new portfolio ideas.
