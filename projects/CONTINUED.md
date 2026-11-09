# More AI portfolio projects

[Full project index](README.md)


## ConceptLab: exact concepts and implication witnesses

[Live inspector](https://midya8.github.io/conceptlab/) | [Source](https://github.com/midya8/conceptlab) | [Method and prior work](https://github.com/midya8/conceptlab/blob/main/METHOD.md)

A bounded knowledge-representation workbench for formal concept analysis. Independent Python and JavaScript enumerate every formal concept, cover, meet/join, attribute closure and object derivation. Inspect canonical implications, pseudo-intent decisions, NextClosure pivots, forward rule traces and rule-removal countermodels. Every implication query retains supporting and counterexample rows; an empty premise extent means vacuous validity and null confidence, not evidence.

Fourteen original controls include duplicate rows, zero support, empty universes, strict joins, nonminimal pseudo-intents and multi-rule closure. The retained suite covers 194 attribute subsets, 390 object subsets, 69 concepts, 30 canonical rules, 635 ordered lattice operations and 5,762 implication queries. Independent set-based checks cover all 689 contexts with zero to three objects/attributes plus 100 seeded larger contexts per engine. Native CLI, installed wheel and actual-Chrome checks accompany the interactive inspector.

Finite exact teaching/audit tool: at most six attributes and eight objects. Not learned prediction, fuzzy concept analysis, noisy-data inference, causality or a scalable mining system. Existing FCA theory and software are attributed; no new algorithm is claimed.

[ConceptLab case study](conceptlab.md)


### ConceptLab incomplete-context completions

[Live completion inspector](https://midya8.github.io/conceptlab/partial.html) | [Semantics and sources](https://github.com/midya8/conceptlab/blob/main/PARTIAL.md)

Unknown is not false. Enumerate every compatible binary completion of a three-valued table. Inspect certain, contingent and impossible implications, all object counterexamples, exact defined row-confidence bounds and endpoint ties, with zero-support completions kept separate. Intersect goals in one shared completion and retain every inclusion-minimal impossible goal set with deletion witnesses.

Original controls expose two traps: both extreme fill-ins can pass while an intermediate world refutes an implication, and separately possible goals can be jointly impossible. Overlapping-premise tautologies, empty universes, duplicate objects and all 64 worlds of six unknowns remain explicit. Twelve controls cover 86 completions, 438 implication queries, 4,634 query/completion witness rows and 63 goal subsets.

Independent Python and JavaScript engines, 17 native tests on four Python versions, six Node/Chrome tests and 26 installed-wheel reports preserve the complete-context workbench. Every retained UI record, export and invalid-input clearing is checked; all controls are layout-tested at 320/390/1280. Limits: four attributes, four objects, six unknown cells. Completion counts are not probabilities; confidence bounds describe supplied rows, not unseen data. No imputation, causal claim, graded possibility model, incomplete-context basis or new algorithm is claimed.


### STRIPSLab exact planning and relaxation witnesses

[Live inspector](https://midya8.github.io/stripslab/) · [Source](https://github.com/midya8/stripslab) · [Method and prior work](https://github.com/midya8/stripslab/blob/main/METHOD.md)

An original bounded classical-AI planning lab: audit every state and every blocked/applicable action, compare exact real and delete-relaxed shortest-plan families, and inspect h-max/h-add fixed-point rounds and tied fact achievers. Strict controls expose shared-effect double counting, relaxed solvability hiding real dead ends, restoration costs, all shortest-order ties and unreachable cyclic prerequisites. Python bitsets/reverse BFS and independent JavaScript sets/Bellman sweeps reproduce the same complete reports.

Six facts, eight grounded positive-precondition unit-cost actions. No PDDL parser, real-world execution, scalable-planner claim or new planning algorithm. Fourteen original synthetic tasks; eight Python tests, three Node/Chrome tests and isolated wheel reproduction of all fourteen full reports. Established STRIPS and heuristic-planning work is attributed with inspected-source limits.

[STRIPSLab case study](https://github.com/midya8/Midya-portfolio/blob/main/projects/stripslab.md)


### STRIPSLab search witnesses: an actual suboptimal h-add plan

[Inspect four complete search runs](https://midya8.github.io/stripslab/search.html) · [Search policy and reproducible evidence](https://github.com/midya8/stripslab/blob/main/SEARCH.md)

The new A*/best-first inspector exposes every selected frontier, strict cost improvement, applicable action decision and returned plan. A controlled task returns cost 3 with h-add versus exact cost 2 under the disclosed tie and goal-pop policy. Zero, h-max and exact h-plus return cost 2. Includes admissibility/consistency diagnostics, unsolvable exhaustion, strict CLI certificates, an independently implemented browser engine, and a separate synthetic reopening test. Full-state precomputation is explicit: this is a bounded audit, not a planner speedup or new algorithm claim.


### STRIPSLab availability: used does not mean necessary

[Live action-availability inspector](https://midya8.github.io/stripslab/sensitivity.html) | [Exact source and policy](https://github.com/midya8/stripslab/blob/main/SENSITIVITY.md)

Disable every static action subset. Keep every exact counterfactual distance, shortest-plan count, original action ID, representative and optimal edge. Separate an action used by one representative from one required by every optimal plan or every valid plan. Retain all inclusion-minimal sufficient sets and all solvability/optimality cuts, with independently checked minimal-hitting-set duals.

The original duplicate-shortcut control leaves a longer detour when both shortcuts are removed: optimality fails before solvability does. Eighteen controls retain 466 scenarios, 21,731 state rows and 408 optimal edges. Python BFS and independent JavaScript distance sweeps agree on 118 complete reports covering 2,515 scenarios; independent native set-transition and all-proper-subset oracles cover another 80 seeded tasks. Seventeen native tests, nine Node/Chrome tests and 47 isolated installed reports preserve all earlier modes. Browser checks every retained scenario at 320/390/1280.

Six facts/eight unit-cost grounded actions maximum. Static deterministic re-planning, not failure probabilities, timed outages, a scalable landmark extractor, real-world reliability or a new algorithm. [Implementation, boundaries and inspected sources](https://github.com/midya8/stripslab/blob/main/SENSITIVITY.md).


## UnifyLab: a binding is not a solution

[Live finite-term inspector](https://midya8.github.io/unifylab/) | [Source](https://github.com/midya8/unifylab) | [Method and inspected sources](https://github.com/midya8/unifylab/blob/main/METHOD.md)

An original bounded classical-AI unification lab. Keep every equation rewrite, composed earlier binding, exact constructor clash and zero-based occurs-check cycle path. A normalized simultaneous substitution is applied to every original equation. Alias reversal is not automatically a cycle, and a resource limit never means non-unifiability.

Independent Python and JavaScript engines reproduce 167 complete reports and 270 rewrites. A separate native certificate checker reconstructs local rules without calling the solver; a third lazy-environment oracle tests controls, 600 seeded systems and all 64 term-pool pairs. Seventeen controls retain 38 rewrites, including actual state/result expansion limits. Twelve native tests on Python 3.10-3.13, three Node/Chrome tests and seventeen isolated installed reports through two CLIs in solve/verify modes. Every retained browser step, equation, binding, witness, export and invalid edit is checked, with layouts at 320/390/1280.

Established finite-tree unification, not new theory. Six variables/eight equations, 96 input nodes, 4,096-node state/result budgets and 256 rewrites. No rational trees, higher-order/AC unification, resolution prover, linear-time or benchmark-win claim. Most-generality follows the established rewrite/solved-form theory; bounded ground-factorization tests are not a universal proof. [UnifyLab case study](https://github.com/midya8/Midya-portfolio/blob/main/projects/unifylab.md).


## UnifyLab: minimal equation conflicts and deletion repairs

[Live subset inspector](https://midya8.github.io/unifylab/cores.html) · [Source](https://github.com/midya8/unifylab) · [Method and inspected sources](https://github.com/midya8/unifylab/blob/main/SUBSETS.md)

Test every indexed subset, keep duplicate equation identities, and distinguish an inclusion-minimal conflict from a smallest conflict. Confirmed deletion repairs list indices to REMOVE and failing single restorations. The default control has independent duplicate/cycle conflicts and repairs of different sizes. A resource limit stays unresolved: no inferred status, false inconsistency, complete-frontier or minimum-size claim. Any selected subsystem opens its detailed rewrite trace.

Eight synthetic controls cover 371 subsets, including all 256 masks at the eight-equation bound, real state/result limits and a known clash beside an unknown expansion. Independent Python/JavaScript engines match 108 full audits and 1,032 subset summaries. Nineteen native tests pass on Python 3.10-3.13; six Node/Chrome tests. Native tests use a third lazy-binding oracle, all proper subsets and independent minimal hitting-set enumeration. Actual Chrome checks every control/subset/neighbor at 320/390/1280, five linked rewrite reproductions, export and invalid-state clearing. Installed wheels reproduce seventeen base reports and eight subset audits through both entry points outside the checkout.

Established finite-tree and constraint-diagnosis concepts, not a new scalable MUS/MCS algorithm. At most 256 independent bounded solves; the aggregate is not an independently verified rewrite certificate. Eight inspected sources distinguish minimal from minimum, conflict from repair, and unifiability semantics from resource limits. No model, API, paid service or private dataset.


## UnifyLab: repeated differences, shared variables

[Ground generalization inspector](https://midya8.github.io/unifylab/generalize.html) · [Method and inspected sources](https://github.com/midya8/unifylab/blob/main/GENERALIZATION.md) · [Source](https://github.com/midya8/unifylab)

Finite ground-term anti-unification: keep common constructors and give the same ordered disagreement pair the same variable. Inspect fresh/reuse records, two substitution maps and exact reconstructions. The independent native checker rejects coherent overgeneralization even when both inputs reconstruct. Python and independently written JavaScript agree on 209 reports; nine synthetic controls expose 43 node records. Original solver and subset inspectors retained.

27 native tests, nine Node/Chrome tests, installed wheel checks through both CLI entry points and responsive 320/390/1280 inspection. Established syntactic anti-unification, not a new algorithm, semantic clone detector or code repair model. Ground finite trees only; the checker validates the canonical trace, not arbitrary renamed certificates or a formal proof.


## HornLab: a circle is not a proof

[Live inspector](https://midya8.github.io/hornlab/) · [Source and tests](https://github.com/midya8/hornlab) · [Method and sources](https://github.com/midya8/hornlab/blob/main/METHOD.md)

Bounded positive propositional Horn inference with synchronous derivation rounds and every indexed rule decision. Compare the least model with every classical and supported model: a supported circular assignment need not have a derivation. Inspect an atomic countermodel for each non-entailed query and every inclusion-minimal initial-fact support, including its deletion failures and all seed subsets. Not entailed does not mean classically false.

Independent Python bitsets and JavaScript sets match 210 full reports; a separate native set/truth-table checker replays the complete report. Ten original controls, exhaustive two-atom programs, seeded tests, installed-wheel reproduction and actual Chrome record checks. Six atoms/eight rules, no negation or variables; established semantics, not a new algorithm or production rule engine.


## HornLab: every route, every break

[Rule-deletion inspector](https://midya8.github.io/hornlab/rules.html) · [Method and primary sources](https://github.com/midya8/hornlab/blob/main/RULES.md) · [Source](https://github.com/midya8/hornlab)

Keep initial facts fixed and inspect all indexed-rule subsets, synchronous closures, every minimal rule support and every minimal deletion set. One broken route need not break the goal. Each support retains one-rule removal failures; each deletion retains restoration successes. Both minimal-hitting-set dualities and every support/deletion intersection are explicit, including empty-support and already-absent boundary cases.

Eighteen native tests retain all originals, with all 1,024 two-atom programs and 150 seeded rule lattices. Independent Python/JavaScript match 131 audits covering 5,304 subsets. Eleven browser controls expose 305 subsets, 35 queries, 36 supports, 27 deletion sets and 36 intersections, all record-checked at 320/390/1280. A separate native set/truth-table checker validates the complete lattice without calling the generator. Installed-wheel reproduction checks both inspectors through both CLI entry points. Established bounded monotone explanation, not causal attribution, ontology translation, a new algorithm or formal proof.


### BisimLab: same traces, different choices

[Source](https://github.com/midya8/bisimlab) · [Interactive inspector](https://midya8.github.io/bisimlab/) · [Method](https://github.com/midya8/bisimlab/blob/main/METHOD.md)

Finite agent-protocol equivalence from scratch: every strong-bisimulation refinement, every failed left/right step match, executable Hennessy-Milner witness DAGs, truth sets and a quotient graph. The default original control has equal finite trace languages but loses a choice after the same action; exact paired-subset BFS checks trace equality separately from branching equivalence. A native partition-signature checker never calls the generator, and independent JavaScript matches full reports. Nine native tests include all 512 three-state/one-action graphs against relation enumeration and 100 seeded graphs; three Node/actual-Chrome tests include 593 complete cross-engine reports and every control record at 320/390/1280. Installed-wheel checks cover both CLI entry points outside checkout. One to six states, all labels visible: no silent abstraction, probabilities, policy guarantee, source extraction, new algorithm or formal-proof claim. Established theory and seven inspected sources are attributed in the method.


### BisimLab: complete trace-product replay

[Interactive trace product](https://midya8.github.io/bisimlab/traces.html) | [Source and exact semantics](https://github.com/midya8/bisimlab/blob/main/TRACES.md)

The second inspector retains the entire reachable product of two states' possible successor sets, including every action edge after a mismatch and the both-empty sink. Inspect canonical BFS discovery words, layers, all possibility-mismatch nodes and a shortest distinguishing path. Equal finite traces still do not imply branching equivalence.

Python bitmasks, independent JavaScript sets and a separate native checker based on explicit subset tables agree on 4,715 trace reports. Seventeen native tests include exhaustive unary three-state graphs across every ordered pair, direct word enumeration, seeded multi-action cases and forged closure/provenance checks. Six Node/actual-Chrome tests cover every control record, export and invalid-input clearing at 320/390/1280px. Installed-wheel checks cover six original and seven trace controls, two CLI entry points and six import origins. One to six states, all actions visible; exponential and bounded, with no silent actions, model/API dependency, scalable-solver or new-algorithm claim. Established subset determinisation and product language equivalence are attributed in the source ledger.


### ShieldLab: a safe next step can still lose

[Source](https://github.com/midya8/shieldlab) | [Interactive inspector](https://midya8.github.io/shieldlab/) | [Exact method and seven-source ledger](https://github.com/midya8/shieldlab/blob/main/METHOD.md)

An exact tiny safety-game inspector for hand-written agent protocols. Every synchronous fixed-point obligation, winning controller move, losing rank and branching invariant/counterstrategy graph is visible. Changing only who controls a state flips the result: one-step-safe actions need not preserve safety forever. Independent bitmask Python and explicit-set JavaScript, plus a separate dual-attractor and exhaustive positional-policy checker.

Eight native tests include all 21,952 three-state graph/ownership/safety combinations and 150 seeded larger arenas. Three Node/actual-Chrome tests compare 643 complete reports and all six controls at 320/390/1280. Installed wheels replay both CLI entry points outside checkout. Finite total perfect-information model only: no runtime shield, LLM guarantee, liveness, timing, probability, new algorithm or formal proof. Dead ends are rejected; safe waiting need not mean progress.

### BuchiLab: a winning state is not a winning policy

[Interactive inspector](https://midya8.github.io/buchilab/) | [Source](https://github.com/midya8/buchilab) | [Method and seven-source ledger](https://github.com/midya8/buchilab/blob/main/METHOD.md)

Tiny finite adversarial repeated-goal games with every nested greatest/least fixed-point obligation, progress rank, complete positional controller policy and reachable cyclic non-goal SCC visible. Idle can stay inside the winning region forever and still lose: rank-guided progress and per-policy audits show why. A separate checker replays with sets/Floyd reachability and every joint-policy eventual lasso, without calling the generator. Nine native tests include 21,952 exhaustive three-state games; three Node/actual-Chrome tests compare 331 complete Python/JavaScript reports and every control record at 320/390/1280. Installed wheels replay seven original controls through both CLIs outside checkout. No fairness assumption, learned abstraction, deployed shield, general LTL compiler, formal proof or real-agent guarantee. Rank-permitted actions are sufficient, not all winning policies.

### BuchiLab: repeat the actual failure

[Action-level lasso inspector](https://midya8.github.io/buchilab/lassos.html) | [Exact witness contract](https://github.com/midya8/buchilab/blob/main/LASSOS.md)

A reachable bad component now becomes an exact action-labelled prefix once and nonempty non-goal cycle forever, for every failing fixed controller policy/root. Empty prefixes, self-loops, multiedge cycles, unreachable bad components and duplicate-target action choices are explicit. BFS generation is independently checked with bounded simple walks and the joint-policy lasso oracle. Original v1 reports and original tests stay intact: 16 native tests across four Python versions and five Node/actual-Chrome tests, including 314 complete witness-report comparisons and every record in ten controls at 320/390/1280. Installed wheels replay both report families outside checkout. Input-order anchor, shortest prefix/cycle individually, not globally shortest lasso. These are per-policy counterexamples, not one environment strategy defeating every controller policy or a real-agent guarantee.

## HallLab: distinct is a global promise

[Live inspector](https://midya8.github.io/halllab/) · [Source](https://github.com/midya8/halllab) · [Method and six-source ledger](https://github.com/midya8/halllab/blob/main/METHOD.md)

Tiny constraint-based AI assignment, with every supported variable/value backed by a complete injective assignment and every rejected edge explained by a forced-residual Hall obstruction. A full synchronous pairwise-AC baseline makes the global bottleneck visible. Exact matching/counting, independent exhaustive native checker, separate JavaScript assignment engine, editable graphs, all tight/deficient subsets and every propagation round.

12 native tests include 8,777 exhaustive domain graphs; 682 complete cross-engine reports; actual Chrome checks every control edge/subset/round at 320/390/1280. Fresh installed CLI replay. Original synthetic controls, no learned model or paid API. At most six variables/eight values, one constraint: not an optimized Régin SCC propagator, scalability benchmark or whole-CSP solver.


### HallLab: local support is not a shared solution

[Overlapping-scope inspector](https://midya8.github.io/halllab/overlaps.html) · [Exact overlap contract and sources](https://github.com/midya8/halllab/blob/main/OVERLAPS.md) · [Source](https://github.com/midya8/halllab)

Repeat full local all-different propagation to a synchronous fixed point, then compare it with exact common-assignment support across overlapping scopes. A two-color triangle keeps every local value but has no joint assignment. A satisfiable triangle keeps local values that never occur in a common solution. Inspect each round, original-variable mappings, scope-only witnesses, full common witnesses and exhaustive rejection bins.

Separate native API/module CLI, independent report checker and JavaScript engine. Eight new native tests and three new Node/Chrome tests preserve the original test sources. Full cross-engine checks cover 621 overlap reports; nine browser controls run at 320/390/1280 widths. Installed-wheel checks run outside the checkout. Tiny exact reference: six variables, eight values, six scopes, at most 262144 full tuples. Classic consistency theory, not a scalable CP solver or a new algorithm.


### HallLab: every minimal conflict, every minimal removal

[Live conflict inspector](https://midya8.github.io/halllab/conflicts.html) · [Exact contract and seven-source ledger](https://github.com/midya8/halllab/blob/main/CONFLICTS.md) · [Source](https://github.com/midya8/halllab)

All inclusion-minimal conflicting all-different scope sets and all inclusion-minimal scope-removal repairs, with complete single-deletion witnesses, common kept-network assignments and contained conflicts for every restoration. The default diamond has a size-one and four size-two minimal removals: minimal is not minimum. Inspect every active subset and the hitting-set intersections that explain why a repair must break every conflict. Domains stay fixed; an empty-domain background has no scope-removal repair.

Independent native histogram generation, per-subset product verification and recursive JavaScript search. 28 native tests, nine Node/actual-Chrome tests; 621 cross-engine reports and 4413 active subsets. Installed wheel reproduces all three report families outside checkout. Prior implementations/tests retained. All browser controls/proofs checked at 320/390/1280. Tiny exact relations, not a scalable MUS/MCS solver, weighted optimizer or a new duality theorem.


## STNLab - temporal bounds with attainable schedules

[Live inspector](https://midya8.github.io/stnlab/) · [Source](https://github.com/midya8/stnlab) · [Method and source ledger](https://github.com/midya8/stnlab/blob/main/METHOD.md) · [Case study](https://github.com/midya8/Midya-portfolio/blob/main/projects/stnlab.md)

For tiny hand-written AI plans, inspect every implied time difference: a tight path plus a complete schedule attaining the bound, or an explicit ray proving it unbounded. Negative cycles show exactly why no schedule exists, even away from the anchor. Removing one edge returns an alternate implication path or a complete separating schedule. Eleven editable controls include duplicate edges, zero cycles, free components and a chain with bound 100.

Native Floyd-Warshall/Bellman-Ford generation, independent permutation/edge-product verification and recursive browser search agree. Nine native tests cover exhaustive tiny graphs, seeded networks and strict CLI rejection; real Chrome checks all proof panels at three widths. Six points and twelve constraints, real-valued times, no resource capacity, uncertain durations or execution guarantee. Classic temporal-network theory, not a new optimization algorithm.


## STNLab insertion sensitivity

One proposed temporal constraint, an exact consistency threshold and every changed implied bound. [Source](https://github.com/midya8/stnlab) · [Insertion inspector](https://midya8.github.io/stnlab/insertions.html) · [Contract and source ledger](https://github.com/midya8/stnlab/blob/main/INSERTIONS.md).

Native old-matrix one-edge closure is checked against independent full recomputation. Inspect the old return path, a complete schedule at the feasibility boundary, a candidate-first negative cycle, or a still-unbounded anchored ray. All finite post-insertion bounds include attaining schedules; 41 integer weights are separate alternatives, not accumulated changes.

Ten new synthetic controls include exact-boundary feasibility, a missing return path, a pre-inconsistent base, duplicate/self-loop cases, a six-point threshold outside the input window and a 12-edge base plus candidate. The original inspector remains intact. Seventeen Python tests, six Node/real-Chrome tests and installed-wheel checks cover both families. This is bounded classical temporal reasoning, not event execution, uncertainty handling, a new algorithm or a scalable verifier.


### STNLab existential projection

[Interactive projection lab](https://midya8.github.io/stnlab/projection.html) | [Source](https://github.com/midya8/stnlab) | [Exact contract](https://github.com/midya8/stnlab/blob/main/PROJECTION.md)

Hide time points without losing the bounds their paths imply. STNLab restricts the closed network to retained original IDs, lifts jointly feasible retained assignments into full original schedules, and exposes retained assignments that naive edge deletion wrongly permits. Each finite projected bound has an original path and a full attaining schedule; unbounded pairs have anchored rays. Hidden negative cycles remain impossible.

Independent Fourier-Motzkin elimination, path enumeration and pinned-cycle checks audit the result. Native Python and separate browser recomputation agree across 12 projection controls, with installed CLI reproduction and real Chrome proof-panel tests at 320, 390 and 1280 pixels. Classical STN analysis over real-valued time points, not a new algorithm, calendar executor or uncertainty model.


## STNLab complete conflicts and repairs

[Live conflict/repair inspector](https://midya8.github.io/stnlab/conflicts.html) | [Source](https://github.com/midya8/stnlab) | [Exact contract and sources](https://github.com/midya8/stnlab/blob/main/CONFLICTS.md)

Enumerate every inclusion-minimal temporal conflict and every inclusion-minimal correction set. Replay negative cycles, conflict-deletion schedules, repaired schedules and restoration contradictions. An independent native verifier checks complete hitting-set duality; a separate JavaScript engine powers the inspector. Minimal is explicitly distinct from minimum-cardinality.

Validation: 31 native tests on Python 3.10-3.13, 12 Node/Chrome tests, 316 cross-engine reports, exhaustive tiny networks and installed-wheel reproduction for all four STNLab families. Chrome visits every control proof at 320/390/1280. Includes duplicate edges, disconnected conflicts, self-loops, empty repairs and the 12-edge boundary. Classical duality applied to bounded STNs, not a new-theory or scalable-solver claim.


## EUFLab: ground equality with evidence

[Live proof and countermodel inspector](https://midya8.github.io/euflab/) | [Source and reproduction](https://github.com/midya8/euflab) | [Semantics and six-source ledger](https://github.com/midya8/euflab/blob/main/METHOD.md)

Functions preserve equality, not difference. EUFLab exposes ground congruence proof DAGs, every contradicted disequality and a total finite interpretation for consistent inputs. Inspect non-injectivity, cyclic values, duplicate syntax, ordered arguments and inconsistent-premise boundaries. Native union-find/proof forests, separate browser relation saturation, independent proof/model verification and exhaustive set-partition references make the claims inspectable.

Validation: 9 native tests on Python 3.10-3.13; 156 cross-engine reports; 251 query selections at each of 320, 390 and 1280 pixels; installed-wheel generation and verification through both entry points. Bounded ground conjunctions only, not quantified logic, arithmetic, SMT-LIB parsing or a production SMT solver. No model service or paid API.


## EUFLab finite-model atlas

[Live finite-model atlas](https://midya8.github.io/euflab/atlas.html) | [Source and reproduction](https://github.com/midya8/euflab) | [Exact atlas contract](https://github.com/midya8/euflab/blob/main/ATLAS.md)

The most separated quotient is not necessarily the smallest model. EUFLab now enumerates every compatible term-equality pattern, finds minimum domain size, and classifies each pair as forced equal, forced different or flexible. Explore total model witnesses, unary backward difference, binary disjunctions, odd-cycle coloring and all 4,140 eight-name patterns. Counts are equality patterns, not full interpretations; extra unnamed domain elements remain possible.

Independent restricted-growth, explicit-block and subset-cover enumerators. Validation preserves the original nine native tests: 16 native tests on Python 3.10-3.13, six Node/Chrome tests, 76 complete cross-engine atlas reports, installed-wheel reproduction of both inspector families, and all 4,317 admitted control patterns at 320/390/1280 pixels. Exhaustive ground-conjunction search, capped at eight terms; no scalability or new-algorithm claim.


## EUFLab domain-cap debugger

[Live bounded-domain debugger](https://midya8.github.io/euflab/cardinality.html) | [Source and reproduction](https://github.com/midya8/euflab) | [Exact diagnosis contract](https://github.com/midya8/euflab/blob/main/CARDINALITY.md)

Too few values? Find every cause. With the domain cap held fixed, enumerate every inclusion-minimal assertion conflict and deletion repair. Separate intrinsic inconsistency from cap-only conflicts, inspect every assertion subset, and replay total models for repairs or one-literal core relaxations. Duplicate occurrences retain their identities; minimal repairs need not have minimum size. A three-cycle shows why explicit difference-edge coloring alone misses functional constraints.

Validation: 23 native tests on Python 3.10-3.13, nine Node/Chrome tests, 269 complete cross-engine reports, independent labeled-assignment and hitting-set references, and installed-wheel reproduction of all three inspector families. Chrome audits 379 subset selections, 36 core-relaxation actions, 29 repair actions and 104 cap changes at each of 320/390/1280 pixels. Eight terms, eight assertion occurrences, ground conjunctions only. Complete bounded enumeration, not a new algorithm or scalability claim.


## EUFLab costed repair planner

[Live planner](https://midya8.github.io/euflab/planner.html) · [Source and exact contract](https://github.com/midya8/euflab/blob/main/PLANNER.md)

Protect what cannot change, price what can. The fourth EUFLab inspector enumerates every permitted deletion set, every cost-only optimum and a separate cost/count Pareto frontier. Protected intrinsic or cap-only cores explain infeasibility. Each plan includes a total minimum-domain model with kept, protected and omitted assertion truth rows.

Zero-cost nonminimal ties are preserved, not silently filtered to minimal repairs. Deleting does not mean negating; the live control shows an omitted equality that still holds. Costs never override protection. Fourteen synthetic controls cover different-size/same-cost optima, two-coordinate tradeoffs, duplicate occurrences, hard obstructions and function-driven cardinality.

Native and browser engines agree on 358 complete reports. Independent labeled-domain references check graph/protection policies and functional DAGs; an independent certificate verifier rebuilds models and checks all masks/objectives. Python 3.10-3.13, installed module/console reproduction and actual Chrome phone/desktop checks. Eight terms/eight assertions, ground one-sort conjunctions; no general MaxSMT, new-algorithm or scalability claim. Nothing is actually edited.


### EUFLab exact repair-cost sensitivity

[Live sensitivity inspector](https://midya8.github.io/euflab/sensitivity.html) | [Source and certificate contract](https://github.com/midya8/euflab/blob/main/SENSITIVITY.md)

Vary one assertion deletion cost over every integer from 0 to 1,000,000. The certificate gives exact keep/delete intervals, breakpoint ties and every optimum mask, including zero-cost nonminimal repairs. An independent native verifier rebuilds all affine plan-cost lines; the browser inspector audits replacement costs, regret and total models without treating omitted assertions as negated. Hard protections and blocked policies remain explicit. This is bounded exhaustive analysis, not an industrial-scale solver or simultaneous multi-cost robustness guarantee.
