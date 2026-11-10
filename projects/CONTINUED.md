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


### DFALab: active learning with exact counterexamples

[Live inspector](https://midya8.github.io/dfalab/) | [Source and contract](https://github.com/midya8/dfalab/blob/main/CONTRACT.md) | [Case study](dfalab.md)

Ask membership questions, repair an observation table, then break a wrong conjecture with a shortest counterexample. Classic Angluin L* is replayed with every experiment, closure/consistency witness and complete reachable-product equivalence check. The final DFA has access words and pair-separating suffixes proving minimality. Independent Python/JavaScript reports and a separate certificate checker are tested against exhaustive tiny teachers and a pair-marking oracle. Exact equivalence relies on the supplied finite synthetic teacher, not random tests of a real service; no new algorithm or query-efficiency claim.

### DFALab: bounded conformance, not an unrestricted test-pass claim

[Live W-method inspector](https://midya8.github.io/dfalab/conformance.html) | [Construction, assumptions and sources](https://github.com/midya8/dfalab/blob/main/CONFORMANCE.md) | [Source](https://github.com/midya8/dfalab)

The classic DFA W-method now has a complete experiment inspector: every state-cover word, middle word, distinguishing suffix, canonical factor and acceptance path. It separates four claims: finite suite agreement, the supplied candidate's reachable-state bound, a bounded equivalence certificate and a separate exact graph audit. A faulty extra-state candidate passes when its bound is understated; increasing the bound exposes the fault. Tests do not infer a hidden service's state count.

An independent verifier reconstructs all factor combinations and checks every output and witness without calling the generator. Six added native tests include 52,488 exhaustive reference/candidate cases; 131 full native/browser-engine reports are cross-checked. Actual Chrome audits 3,444 test selections and 141 probes across eleven controls and three widths. Four Python versions, seven Node/Chrome checks and installed two-family reproduction preserve the original L* learning page and schema. These are synthetic fixture checks, not production-protocol benchmarks or a new theorem. The method is credited to Vasilevskii and Chow; the precise DFA theorem and reset/state-bound assumptions are documented.

### DFALab: exhaustive finite fault atlas and exact test-subset selection

[Live fault atlas](https://midya8.github.io/dfalab/fault-atlas.html) | [Exact domain, cost and sources](https://github.com/midya8/dfalab/blob/main/FAULT_ATLAS.md) | [Source](https://github.com/midya8/dfalab)

Enumerate every complete labeled implementation in a tiny unary/binary state domain, distinguish equivalent survivors from real faults, and inspect every acceptance-matrix row. Every subset of the constructed W-suite is checked under test-count then letter-count cost. All minima, escaping faults and chosen-test deletion witnesses are retained. Irredundancy is not confused with minimum cardinality; label/unreachable-state duplicates are not counted as unique languages or bug frequencies.

An independent native verifier reconstructs the complete machine domain and every subset result. Tests cover all 60 tiny minimal references with a separate equivalence oracle. Eleven complete cross-engine atlas reports match; actual Chrome audits 6,996 candidate selections and 804 subset selections across eight controls and three widths. All eighteen native checks on four Python versions, ten Node/Chrome checks and installed three-family reproduction preserve active learning and bounded conformance. Optimization is restricted to subsets of the generated W-suite, not globally shortest tests or real-world protocol coverage. Classic W-method and set-cover ideas are explicitly credited.


### SynthLab: counterexample-guided bit-vector program synthesis


**Fits the examples. Fails the function.** A learner chooses the cheapest grammar expression fitting known examples; an exact finite verifier returns the first wrong input. Inspect every iteration, eliminated candidate, complete truth table and evaluation tree. Full-domain semantic signatures safely deduplicate programs without using the target; a separate verifier enumerates every raw ordered grammar tree to check bounded completeness and canonical minimum cost.

Ten synthetic controls separate example agreement, exact finite correctness and minimum AST-node cost inside the explicit grammar. Eight native tests run on Python3.10-3.13, including512 Boolean target/grammar pairs and2764 raw trees at each of three widths; four Node/actual-Chrome tests audit30 reports,90 iterations,903 candidate signatures and3420 expression probes. Installed module+console reproduction runs outside the checkout. Classical CEGIS/enumeration credited. No novel algorithm, unbounded synthesis, cvc5 integration or production-code benchmark claim.

[Live inspector](https://midya8.github.io/synthlab/) · [Source](https://github.com/midya8/synthlab) · [Grammar, proof boundary and sources](https://github.com/midya8/synthlab/blob/main/CONTRACT.md)

#### Exact finite teaching-set atlas

**A correct program need not be uniquely identified.** The teaching inspector separates CEGIS correctness from eliminating every rival function. For realizable 1-bit and 2-bit targets it checks every input subset, reports all minimum-cardinality teaching sets and seed-constrained minima, and provides row-deletion rival witnesses. A separate direct-intersection verifier checks the complete atlas, including the embedded raw-AST synthesis certificate.

The two-bit XOR control has 132 distinct rival functions and 65,536 input subsets. CEGIS stops correctly with four examples but leaves three rivals; the atlas finds 182 four-row teaching sets. Same number of examples does not mean the same identifying power. Five teaching controls add seven native tests and three Node/Chrome checks, bringing the project to 15 native tests on Python 3.10-3.13 and seven Node/Chrome checks. Chrome audits 15 teaching reports, 1,203 subset selections and 597 rival truth selections; installed module and console reproduction runs outside the checkout.

[Teaching inspector](https://midya8.github.io/synthlab/teaching.html) · [Teaching contract and sources](https://github.com/midya8/synthlab/blob/main/TEACHING.md) · [Reviewed implementation](https://github.com/midya8/synthlab/pull/2)

Finite target-specific identification, not class-wide teaching dimension or PAC learning. Classical teaching-set/minimum-cover ideas credited to Goldman and Kearns; word-valued labels use explicit equality. No new teaching algorithm claim.

#### Exact adaptive query policies

**Let the answer choose the next question.** The adaptive inspector solves the smallest worst-case number of further input queries needed to identify any function still fitting the initial observations. It audits every nonempty version space, every query's label partition, all tied minimax rows, a canonical policy and every possible target path. A separate verifier checks the complete recurrence and the underlying raw-tree synthesis certificate.

A full seeded two-bit grammar leaves ten functions after two known observations. Two further adaptive queries suffice, while every fixed passive separating set needs three rows. Immediate split balance is not the same objective: across all balanced tie resolutions, policies need two or three further queries. Neither an easier hand-selected class nor an unlucky chosen baseline tie is used.

Seven additional native tests bring the project to 22 on Python 3.10-3.13; five additional Node/Chrome checks bring it to 12. The adaptive tests compare 541 complete native/JavaScript reports with independent verification. Actual Chrome audits 15 adaptive reports, 1,583 version-space selections, 111 query partitions, 306 answer branches, 84 target traces and 105 passive mask selections. Installed module+console reproduction includes all three certificate families outside the checkout.

[Adaptive inspector](https://midya8.github.io/synthlab/adaptive.html) · [Exact adaptive contract and sources](https://github.com/midya8/synthlab/blob/main/ADAPTIVE.md) · [Reviewed implementation](https://github.com/midya8/synthlab/pull/3)

At most ten functions after separately counted initial observations, exact noiseless labels and unit query cost. Future answers are simulated from supplied tables, not a live oracle. Classical decision-tree dynamic programming and generalized binary search credited. No expected-cost, PAC or novel-algorithm claim.

## WarpLab: inspectable differentiable alignment

Soft-DTW without the black box: scalar Python and browser JavaScript expose every Gibbs cell occupancy and joint edge flow, sequence/temperature gradients, and cost Hessian-vector products. A separate exhaustive path oracle checks every report field against all legal alignments.

- Stable log-space messages and directional expectation messages, no autodiff dependency. Cost curvature is checked against negative path-incidence covariance and finite differences.
- Eight synthetic controls include negative self-scores, a single legal path, low-temperature underflow and a 7 by 7 grid where all 8,989 paths tie. Hard ties compare exact rational sums of binary64 local costs, not a fuzzy tolerance.
- Strict JSON certificates, atomic CLI output and fresh installed module/console reproduction. Python 3.10-3.13 CI; 168 complete cross-language reports; real Chrome checks at 320/390/1280 pixels, including cell/edge inspection, complete paths, accessible row/column controls, export and error clearing.

[Live alignment inspector](https://midya8.github.io/warplab/) · [Source and reproduction](https://github.com/midya8/warplab) · [Mathematical contract](https://github.com/midya8/warplab/blob/main/CONTRACT.md) · [Reviewed implementation](https://github.com/midya8/warplab/pull/1)

Raw soft-DTW is not a metric and can be negative. Occupancy sums to expected path length, not one; it is not a transport coupling. Hessian products are in independent cost coordinates. Lengths are bounded to 1..7; synthetic controls are not accuracy or speed benchmarks. Established soft-DTW and differentiable-DP mathematics credited to Cuturi/Blondel and Blondel/Mensch/Vert. No novel-algorithm or ground-cost-independent divergence theorem claim.

### Path-length atlas

[Live length atlas](https://midya8.github.io/warplab/lengths.html) · [Length contract](https://github.com/midya8/warplab/blob/main/LENGTHS.md) · [Reviewed extension](https://github.com/midya8/warplab/pull/2)

Separate every legal visited-cell count before mixing paths. Length-resolved log messages expose exact path counts, conditional occupancies and joint edge flows, hard minima/ties, and conditional coordinate/temperature gradients. An explicit per-visited-cell penalty changes the mixture, not the conditional laws. Inspect the entropy decomposition, expected-length gradient and negative length-variance curvature.

The extension adds 98 independently verified complete cross-language atlases. Merged main passes 27 Python tests on each Python 3.10-3.13 and nine Node/Chrome tests, plus installed module/console reproduction for eight base and eight length controls. Live Chrome checks 81 length selections, 1,740 row/column cell inspections, 72 penalty changes and 96 complete reports at 320/390/1280 pixels. All ten deployed assets are source-exact; all 48 screenshots across both inspectors match verified main pixel for pixel.

Length includes both endpoints. Positive penalty favors shorter paths, negative penalty rewards longer paths: this is a changed objective, not an accuracy improvement. The independent oracle groups complete paths and checks the penalized law directly; it does not trust the length-message generator. Synthetic grids remain bounded to 1..7 samples, with at most 8,989 paths. No new-algorithm or benchmark claim.

### Inverse expected-length response

[Live inverse inspector](https://midya8.github.io/warplab/inverse.html) · [Inverse contract](https://github.com/midya8/warplab/blob/main/INVERSE.md) · [Reviewed extension](https://github.com/midya8/warplab/pull/3)

Choose a target expected visited-cell count and inspect whether penalty -4..4 can reach it. The full numerical bisection witness exposes every bracket, response, centered length variance and probability law. Finite-range failures, single-length unidentifiability and numerical flattening stay distinct. A narrow-bracket control deliberately misses the mean-residual tolerance, making the difference between stopping rules visible.

A separate complete-path oracle directly evaluates every witness penalty and checks the trace, status and selected response without calling the solver or length dynamic program. Merged main passes 37 Python tests on each Python 3.10-3.13 and 12 Node/Chrome tests. Tests include 36 complete cross-language inverse reports, derivative finite differences, random interior targets, generator-disabled verification and forged witnesses. Fresh installed module/console reproduction covers eight base, eight length and nine inverse controls. Live inverse Chrome checks 438 witness selections over 27 complete reports at 320/390/1280; all 15 deployed assets are source-exact, and all 75 screenshots across the three inspectors match verified main pixel for pixel.

This is bounded numerical evidence, not interval arithmetic or a unique-parameter certificate. A width stop does not promise a 1e-9 mean residual; unreachable targets show a diagnostic response, not a solution. Binary64 rounding can disagree at adversarial branch boundaries, in which case verification fails. No learned model, benchmark or new-algorithm claim.

## HingeLab: a boundary is not always an adversary

[Live inspector](https://midya8.github.io/hingelab/) · [Source](https://github.com/midya8/hingelab) · [Reviewed implementation](https://github.com/midya8/hingelab/pull/1) · [Case study](hingelab.md)

Follow every rational affine region of a small ReLU network. Inspect hidden activation masks, exact decision roots and the full opposite-class set, including open endpoints and isolated ties. The report separates an attained nearest adversary from an unattained distance infimum and checks the actual closed-ball radius. A paired control keeps margin(x) = x fixed and changes only the reference side: the class-1 tie makes radius one robust on one side and nonrobust on the other.

Forward interval splitting is checked by an independent complete activation-mask enumerator that never calls the generator. Python Fraction and browser BigInt engines agree on 144 complete reports. Merged main passes 12 tests on each Python 3.10-3.13, including 200 seeded two-layer networks, generator-disabled verification and forged evidence. Four Node/Chrome tests and fresh installed module/console reproduction cover all eight controls. Live Chrome checks 54 region selections over 24 reports at 320/390/1280, export, stale clearing and invalid input. All five deployed assets are source-exact, and all 24 main/deployed screenshots match pixel for pixel.

This is exact only for the declared small rational, one-dimensional contract, with a fixed class-1 tie convention and explicit domain. SVG coordinates are rounded for display, never used as evidence. No trained model, model import, high-dimensional certificate, benchmark or new-algorithm claim. Established exact line-restriction and verification work is attributed; a downloaded browser report is independently checked only when the Python checker accepts it.

## HingeLab: every reference, one exact radius

[Live reference atlas](https://midya8.github.io/hingelab/reference.html) · [Source](https://github.com/midya8/hingelab) · [Reviewed implementation](https://github.com/midya8/hingelab/pull/2)

Compute the entire robust-reference set, not one sampled point. Exact class-component erosion keeps strict versus closed endpoints, isolated ties and domain-edge clipping. A nested tent's class-1 interval [-1/2, 1/2] at radius 1/2 shrinks to the robust singleton {0}; at 513/1024 it disappears. Its zero interval length never erases its existence. The exact robust-length fraction is not accuracy or a data probability.

A separate activation-mask/critical-atom checker exhausts every boundary/root and radius-shifted transition, without the reference generator or its erosion/union routines. Merged main passes 20 tests on each Python 3.10-3.13 and seven Node/Chrome tests. Evidence includes 160 new seeded networks with point agreement/radius monotonicity, 200 new complete exact Python/BigInt reference reports, 144 preserved base reports, generator-disabled and forged-type checks, and an additional 972-case tiny-network/domain/radius sweep. Fresh installed module/console reproduction covers eight base plus eight reference controls. Live Chrome checks 47 robust-component selections over 28 reference reports, plus 24 base reports, at 320/390/1280. All nine deployed assets match main, and all 52 main/deployed screenshots match pixel for pixel, including singleton, empty, above-threshold and zero-radius states.

The original bounded rational one-dimensional contract and class-1 ties are unchanged. The closed ball is intersected with the declared domain. Established piecewise-affine analysis and set erosion, not a new algorithm, trained/imported model, high-dimensional certificate, sampled-grid proof or benchmark. Browser evidence becomes independently checked only after Python accepts its download.

## HingeLab: every radius, exact

[Live all-radius profile](https://midya8.github.io/hingelab/radius.html) · [Source](https://github.com/midya8/hingelab) · [Radius-profile case study](hingelab.md#radius-profile-extension)

Exact piecewise-linear robust interval length for every radius in [0,32],
class-wise and total existence sets with strict/closed extinction endpoints,
and the first radius at most a requested length fraction. Zero length is not
empty: margin x on [-2,2] retains a robust singleton at radius 2. A separate
mask/atom checker reconstructs the complete profile from candidate collision
radii and opposite-class closed-ball intersection, without importing the
profile/reference generator or erosion/union code. Full exact JSON export.

44 source files verified on merged main `4b1ceacf5ffeeb25ed8052c48053a926e91dd047`.
26 Python tests on each of 3.10-3.13; ten Node/Chrome tests; 104 new complete
cross-language profile reports plus 200 reference and 144 base reports; fresh
installed reproduction for eight controls in each report family. Live Chrome
checks 28 radius, 28 reference and 24 base reports. All 13 deployed assets are
source-exact; all 80 native/feature/main/deployed screenshots match without
masks and final phone/desktop/conditional pixels were inspected. Feature, PR,
main CI and Pages all green. [Merged PR](https://github.com/midya8/hingelab/pull/3).

Deliberately bounded scalar rational ReLU networks, closed balls clipped to the
declared domain and class-1 ties. Established set erosion, not a new algorithm,
training/import, high-dimensional certificate, accuracy/probability estimate,
benchmark or scaling claim. Browser evidence requires independent Python
acceptance. [Exact contract and finite-partition proof](https://github.com/midya8/hingelab/blob/main/RADIUS.md).


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
## CPNetLab: a ranking is not an entailed preference

[Live workbench](https://midya8.github.io/cpnetlab/) · [Source and reproduction](https://github.com/midya8/cpnetlab) · [Contract and limits](https://github.com/midya8/cpnetlab/blob/main/CONTRACT.md) · [Prior-work ledger](https://github.com/midya8/cpnetlab/blob/main/SOURCES.md)

Complete, supplied binary CP-nets define legal single-variable improvements, not a universal score. CPNetLab enumerates every outcome and improving flip, finds shortest paths or closed no-path cuts, counts every compatible strict ranking, and supplies two actual opposite rankings when a pair is incomparable. Incomparable does not mean indifferent.

- **One legal flip can violate more rows.** In a four-variable fanout, `0000 → 1000` is an improving flip while violated rows rise from 1 to 3. All 2,304 compatible strict rankings still put the target above the start. Counting violated rows is not the preference semantics.
- **Dependency cycles and inconsistency are different.** A matching two-variable dependency cycle permits four strict rankings. Reversing one table produces the actual improving cycle `00 → 01 → 11 → 10 → 00`, zero strict rankings, and no vacuous dominance verdict.
- **Many rankings need not settle a pair.** Two independent consistent cycles admit exactly 101,977,088 rankings while leaving `0000` and `1111` incomparable. The UI displays a complete ranking for each direction.

A separate Python checker rebuilds the entire evidence report using Hamming-one pairs, Floyd-Warshall and suffix-removal counting, rather than the generator's conditional-row flips, breadth-first paths and prefix-ideal counting. Shared validation and binary encoding are disclosed. Python and JavaScript agree on all eight controls, 61 outcomes and 100 edges. Browser JSON is independently checked only after the Python verifier accepts it, not merely because export worked.

Reproduction covers all 36 two-variable networks and 576 ordered queries against all permutations; five three-variable fixtures against all 40,320 permutations each; 160 seeded additional networks; strict evidence forgeries; Python 3.10-3.13; and installed-wheel execution outside the checkout through module and console commands. Actual Chrome checks 24 reports at three widths, all 689 ordered control comparisons, every rendered conditional row, path, ranking witness and no-path cut, all eight evidence exports, and stale/invalid/cycle recovery. Final source, CI, deployment assets, behavior and pixels were checked before this showcase was published.

**Exact scope:** zero to four variables and at most 16 outcomes; complete strict binary local tables. No learned human preferences, local ties, missing rows, constraints, cardinal utility, partial-model semantics or scalable-solver claim. CP-net theory and graph/counting methods are established prior work; these are developed synthetic controls, not human-choice measurements or a new algorithm.


## CPNetLab row subsets: minimal is not minimum

[Live whole-row atlas](https://midya8.github.io/cpnetlab/scopes.html) · [Source](https://github.com/midya8/cpnetlab) · [Contract](https://github.com/midya8/cpnetlab/blob/main/ROW-SUBSETS.md)

Enumerate every whole conditional-row subset, not one convenient explanation.
Eight developed controls cover 865 subset graphs with actual improving paths,
inconsistency cycles and compatible strict-ranking witnesses. The default
256-subset control has two minimal conflicts and six irreducible withdrawals:
three remove one row, three remove two. A separate control has two-row and four-row
minimal path supports. Minimal does not mean minimum; neither means the right
human preference to abandon.

The independent Python checker labels Hamming-one pairs, uses Floyd-Warshall
paths and checks all proper candidate subsets. It reconstructs every mask and
all four antichains without importing either analyzer. Shared strict input
validation/outcome encoding is disclosed. Browser JSON is independently checked
only after Python accepts it. Whole-row withdrawal removes all justified flips,
not an arbitrary single edge. All outcomes and the supplied model remain intact.
This is bounded what-if constraint evidence, not automatic preference revision,
indifference, extended partial-model semantics, learned preferences or a new
algorithm. At most eight rows, sixteen outcomes and 256 subsets.

Release checks: 14 Python tests on 3.10-3.13; six combined Node/actual-Chrome tests;
all 576 ordered two-variable query atlases (6,400 subset records); all 400
two-variable masks against every possible total order; 91 accepted seeded row
atlases; installed 0.2.0 wheel outside the checkout through both CLI entry points
for both eight-control families; forged-evidence rejection. Actual deployed Chrome
selects all 865 masks, all 46 antichain buttons, every row toggle and all eight
exports, with stale/invalid/row-limit recovery and eight controls at three widths.
The original complete-model checks remain green. Feature/PR/main CI and Pages
passed; 37 source files, all 11 live assets and the root page match, with 28
main/feature and 28 main/deployed unmasked pixel matches.


## EpistemLab: true when said, false after heard

[Live workbench](https://midya8.github.io/epistemlab/) · [Source](https://github.com/midya8/epistemlab) · [Evidence contract](https://github.com/midya8/epistemlab/blob/main/CONTRACT.md) · [Prior work](https://github.com/midya8/epistemlab/blob/main/SOURCES.md)

A public announcement can be truthful and make its own content false. EpistemLab
shows every world removed, every surviving information block, and the newly
evaluated truth set of every subformula. In the default two-world experiment,
"p, but agent a does not know p" retains one world and becomes false there.
The fact remains true; the ignorance does not.

Eight developed controls also separate everybody's knowledge from common
knowledge with an actual two-agent failure chain; show distributed knowledge
that neither agent has alone; inspect disconnected common-knowledge components;
and follow three observers through an 8 → 7 → 4 → 1 world sequence. Repeated
updates and eliminated focus worlds are explicit. Empty is not false: pointed
query values are null when the focus no longer exists.

The Python generator uses recursive pointwise semantics and breadth-first paths.
A separate verifier rebuilds the complete report with truth-set algebra,
descending fixed points, block intersections and Floyd-Warshall distances.
Shared strict input validation is disclosed. JavaScript reproduces the complete
control reports; browser exports count as independently checked only after the
Python verifier accepts them. Every modal obligation includes all reachable
worlds, canonical shortest paths and an actual shortest failure witness when one
exists. No model, backend, or paid API is called.

Release checks: seven Python tests on 3.10-3.13, four Node/actual-Chrome tests,
all 200 three-world/two-agent partition-and-valuation models, 120 seeded nested
requests, strict malformed/forged-evidence rejection, and an installed 0.1.0
wheel outside the checkout through both module and console entry points. Actual
Chrome checks 24 responsive reports, 51 round snapshots, 383 formula/world
selections, 142 modal obligations, eight exports and stale/invalid/empty recovery.
Feature, PR, main CI and Pages passed. All 27 source files and seven deployed
assets plus the root page match; 30 feature/main and 30 main/live screenshots
match without masks. Final deployed desktop, phone and edge-state pixels were
inspected before publication.

**Exact scope:** finite supplied S5 models, at most 16 worlds, five atoms, three
agents, six queries and four sequential global truthful restrictions. No beliefs,
probabilities, language-to-knowledge inference, real-person knowledge claims,
arbitrary public-announcement quantification, or new-algorithm claim. Truth loss
is evidence for this supplied model and update, not a proof that a formula fails
in every model. Sources distinguish these model-specific checks from general
announcement-validity questions.


## EpistemLab disclosures: a restriction is not an announcement

[Live disclosure atlas](https://midya8.github.io/epistemlab/disclosures.html) · [Source](https://github.com/midya8/epistemlab) · [Exact contract](https://github.com/midya8/epistemlab/blob/main/DISCLOSURES.md)

Enumerate every retained-world subset, but count only actual Boolean-definable
announcements over the supplied atoms as solutions. An arbitrary what-if
restriction can split worlds with identical atomic facts. No Boolean formula
over those atoms can do that. The atlas supplies a retained/removed pair with the
same valuation as an explicit obstruction, or complete defining DNF cubes when
the restriction is expressible.

Eight developed controls cover 324 restrictions and 25 separate knowledge goals.
The default goal has two inclusion-maximal successful disclosures retaining two
and three worlds; only the latter is maximum-retained. Another control has two
successful diagnostic restrictions and no Boolean solution. A stronger truthful
Boolean disclosure can also destroy an ignorance goal. The search checks all
proper supersets, not just one-bit neighbours: a direct regression has successful
masks 1 and 7 with failing intermediate masks 3 and 5.

A separate Python checker enumerates world combinations and unions of valuation
classes, then uses independent truth-set/fixed-point/Floyd semantics for every
restriction. It rebuilds every defining cube, obstruction, post-update query
truth set, frontier and stronger-disclosure loss witness without importing the
atlas generator. Shared strict model parsing is disclosed. Browser exports count
as independently checked only after the Python verifier accepts them. The UI also
shows the complete restricted model and actual modal obligation paths. A removed
focus has null pointed answers; inspecting another surviving world never turns
it into an answer about the eliminated focus.

Release checks: 14 Python tests on 3.10-3.13; nine Node/actual-Chrome tests; all
200 small-model atlases/1,600 restriction records against every one-atom Boolean
truth function; 45 nested-goal atlases; malformed and forged-evidence rejection;
and installed 0.2.0 wheel reproduction outside the checkout through both CLI
entry points for both eight-control families. Deployed atlas Chrome checks 24
responsive reports, 972 mask selections, 75 goal selections, 204 frontier/witness
buttons, 2,596 subformula selections including 1,170 modal obligations, 87 world
toggles, eight exports and stale/invalid/prior-anchor/empty recovery. Original
sequential-update checks remain green. Feature/PR/main CI and Pages passed; all
39 source files and 12 deployed assets plus root match, with 60 feature/main and
60 main/live unmasked screenshot matches across both surfaces. Actual desktop,
phone, obstruction, goal-loss and empty-state pixels were inspected.

**Exact scope:** at most eight supplied worlds, five fixed atoms, three S5 agents,
six separately evaluated goals, no prior announcements, and one Boolean
restriction. No fresh atoms, epistemic-announcement search, speaker-knowledge
requirement, arbitrary-announcement logic, general planning, shortest-formula
claim or privacy guarantee. Counting retained worlds is a finite combinatorial
objective, not probability or real information leakage. These are established
semantic and truth-table methods with explicit finite evidence, not a new
algorithm or a claim about real people's knowledge.


## StableLab: support is not grounding

[Live workbench](https://midya8.github.io/stablelab/) · [Source](https://github.com/midya8/stablelab) · [Exact contract](https://github.com/midya8/stablelab/blob/main/CONTRACT.md) · [Prior-work ledger](https://github.com/midya8/stablelab/blob/main/SOURCES.md)

A model can be supported and minimal, yet still not stable. StableLab makes the
missing foundation visible. Enumerate every candidate interpretation of a tiny
normal logic program, inspect the actual Gelfond-Lifschitz reduct, and follow
its synchronous derivation rounds from the empty set. See every original rule's
truth test, every support, every proper-subset classical model and every
nonempty unfounded subset with all rule-level obligations.

The program `p <- not p; p <- q; q <- p` has exactly one classical model,
`{p,q}`. It is both supported and minimal. But its candidate reduct contains
only a positive cycle and derives nothing, so there is no stable model. Other
controls separate even and odd default cycles, constraint filtering, a fact
that grounds four derivation layers, exceptions to defaults, one empty stable
model versus no model, and 16 stable alternatives among 256 candidates. Ten
developed synthetic controls contain 300 candidates in total. When no stable
model exists, brave and skeptical answers are explicitly null here, rather than
presenting vacuous universal truth as evidence.

The separate Python checker does not call the generator. It enumerates every
reduct model and proper candidate subset to test stability, intersects models of
the definite reduct for its least closure, reconstructs rounds by bounded proof
heights, and independently checks every unfounded subset. Shared strict input
validation is disclosed. Browser exports become independently checked only
when `stablelab verify evidence.json` accepts them.

Release evidence: nine Python tests on 3.10/3.11/3.12/3.13; four Node/actual-Chrome
tests; all 1,177 two-atom programs through two signed-body rules/constraints;
200 seeded three-atom programs; forged-evidence rejection; and installed 0.1.0
wheel reproduction outside the checkout through both CLI entry points on all
ten controls. An optional external clingo 5.8.3 comparison agreed on stable-model
families for 1,387 programs. That finite check does not validate the UI/proof
evidence or prove general solver compatibility.

Actual deployed Chrome checks 30 responsive reports, all 900 candidate selections,
6,537 unfounded subset selections and 16,605 rule obligations, 1,926 closure
rounds, every displayed rule/reduct/support/query verdict, ten exports accepted
by Python, stale/invalid input and recovery. All 27 native/fresh feature/main
source files match, as do six deployed assets plus root. All 31 feature/main and
31 main/live unmasked screenshot pairs match. Desktop and phone pixels, circular
support, stable alternatives, seeded closure, empty/no-model cases and error
states were inspected. Feature/PR/main CI and Pages are green; PR1 merged
normally after all final checks passed.

**Exact scope:** at most eight declared propositional atoms and 32 normal rules
or headless constraints. Facts and default negation, not a full ASP language.
No variables or variable grounding, function symbols, classical negation,
disjunction, choice rules, aggregates, optimization, well-founded semantics or
clingo text compatibility. Established finite enumeration and semantic methods,
not a new algorithm or a scalable solver. Synthetic programs, not real agents'
beliefs. Model counts are not probabilities.

## StableLab: safe replacement, not matching answers

Equal stable models today does not make a rule module safe to swap. StableLab 0.2.0 now checks every SE pair and produces an actual rule context when two finite modules differ, including controls with equal classical **and** stable families but unequal SE sets.

[Live safe-replacement inspector](https://midya8.github.io/stablelab/equivalence.html) · [Source](https://github.com/midya8/stablelab) · [Contract and reproduction](https://github.com/midya8/stablelab/blob/main/EQUIVALENCE.md) · [Merged PR #2](https://github.com/midya8/stablelab/pull/2)

- Complete `X ⊆ Y` atlas: up to five atoms, 243 pairs, 24 normal rules per side. Every original/reduct obligation is visible; every difference supplies a concrete facts/cycle context with both augmented stable families and full candidate evidence.
- Independent three-valued Python reconstruction and proper-subset context model checks, not another call to the generator. Shared strict parsers and the base evidence verifier are disclosed. Eleven controls include an actual two-edge positive cycle gadget, safe transitive-edge removal, redundant rules, contextual inconsistency and empty vocabulary.
- Reproduced from final feature and main: 16 Python tests on 3.10–3.13; eight Node/Chrome tests; installed 0.2.0 wheel, both CLI entry points, all 11 comparison controls and forged-verdict rejection. Optional clingo 5.8.3 agrees on 5,184 base and 3,514 augmented families across 2,592 comparisons.
- Actual deployed Chrome checks 33 comparison reports at desktop/390/320 widths, all 993 displayed pairs and 9,012 rule obligations, 24 context displays and 11 downloaded reports independently verified in Python. Final feature/main and main/live each match on 65 unmasked screenshots across the base and comparison inspectors. All 11 deployed assets plus root match final main exactly. Feature/PR/main CI and Pages are green.

The strong-equivalence claim is restricted to finite normal-rule contexts over the same declared vocabulary. No arbitrary ASP syntax, fresh-atom context UI, update-semantics preservation, scalable-solver or new-theory claim. Published SE-model foundations and the cycle specialization are credited in [SOURCES.md](https://github.com/midya8/stablelab/blob/main/SOURCES.md). The original eight-atom reduct inspector remains available.


## StableLab: every input, not every rule

A rule module can agree under every added set of facts and still fail under a new rule. StableLab 0.3.0 makes that distinction inspectable: ordinary, uniform and strong equivalence are separate promises, not interchangeable labels.

[Live fact-input inspector](https://midya8.github.io/stablelab/uniform.html) · [Source](https://github.com/midya8/stablelab) · [Contract and reproduction](https://github.com/midya8/stablelab/blob/main/UNIFORM.md) · [Feature PR #3](https://github.com/midya8/stablelab/pull/3) · [Download-readiness regression #4](https://github.com/midya8/stablelab/pull/4)

- Every positive fact subset over the declared vocabulary, with both augmented stable families and every candidate's original rules, reduct and closure. The smallest separator is minimum-cardinality only after **all** smaller inputs agree; equal-size ties use the lowest bitmask. Ten controls reach minimum fact counts 0/1/2/3/4, empty vocabulary and the complete 32-input table.
- The complete UE-pair atlas retains diagonal and maximal proper SE pairs, exposes every disqualifying proper extension and checks that UE equality agrees with the full input table. The credited Eiter/Fink Example 2 agrees under all eight fact inputs but fails under the displayed rule context.
- A separate Python checker reconstructs context candidates through definite-model intersections and proper-subset reduct tests without calling either generator. Shared parsers, checked comparison evidence and the base verifier are disclosed. The JavaScript engine is a portable generator, not another independent solver.
- Final feature/main reproduction: 22 Python tests on 3.10/3.11/3.12/3.13; eleven Node/actual-Chrome tests; installed 0.3.0 wheel outside the checkout, both CLI entry points, all 10 base/11 comparison/10 uniform controls and forged-report rejection. Optional clingo 5.8.3 agrees on 20,978 augmented stable families across 10,489 fact contexts and 2,511 comparisons. This finite check is not a general solver proof.
- Actual deployed Chrome checks 30 uniform reports at desktop/390/320 widths, every one of 255 fact selections, 4,539 candidate selections, 41,343 displayed rule obligations and 1,290 UE-pair selections, plus ten exports accepted by Python. Both earlier inspectors also pass. All 56 native/fresh source files and 16 deployed assets plus root match; 96 feature/main and 96 main/live unmasked screenshots match exactly. Main CI and Pages are green. Desktop/phone overview, fact/candidate details and UE/contract pixels were inspected.

A main-only CI failure exposed a test-harness race: a download path could exist before its bytes finished writing. The preserved failure led to a delayed/partial-write regression and transport-readiness checks across all three inspectors. Parsing, full evidence equality and independent verification still run once; semantic failures are not retried.

**Exact scope:** at most five declared propositional atoms and 24 normal rules per side, including constraints. Added inputs are positive facts over that same vocabulary. Established finite semantics, not new theory, an update-semantics guarantee or a scalable solver. No disjunction, variables, aggregates, classical negation, fresh-atom context UI or broader ASP syntax. [Published foundations and credit](https://github.com/midya8/stablelab/blob/main/SOURCES.md). The original reduct and strong-equivalence inspectors remain available.
