# FireLab: balance is not an execution

**Token balance is not an executable resource plan.** FireLab separates a supplied firing-count equation, legal orderings of exactly that multiset and arbitrary goal reachability in an ordinary weighted Petri net. Original finite teaching controls, not a deployed agent or a new Petri-net algorithm.

[Live inspector](https://midya8.github.io/firelab/) · [Source](https://github.com/midya8/firelab) · [Reviewed implementation](https://github.com/midya8/firelab/pull/1)

## A catalyst can disappear from the equation, not the guard

Start with `(A,B,R)=(0,0,2)` and ask for `(0,1,1)`. Transition `t0: A+R -> A+B` has net effect `(0,+1,-1)`. Counts `(1,0,0)` balance exactly, but t0 cannot fire: there is no A token. Canceling the shared A term in the incidence matrix must not cancel its enabling guard.

Two helper transitions turn R into A and A back into R. The canonical shortest goal sequence is `t1 -> t0 -> t2`, length 3, with one shortest word. It reaches the same goal using counts the proposal omitted. Supplying all three counts makes that multiset executable. Remove the helpers and the balanced target becomes globally unreachable.

This makes three claims explicit:

1. Does this complete count vector land exactly at the specified goal?
2. Does any legal ordering execute exactly this vector, regardless of its endpoint?
3. Does any legal sequence reach the goal, using any counts?

Fixed-count failure is not a global impossibility proof. Neither a bounded count search nor a place invariant is silently presented as an unrestricted nonnegative-integer marking-equation solver.

## All ordinary markings and guards

Every transition preserves total tokens. The checked all-ones place invariant proves a finite ordinary state space, without adding artificial capacity constraints. Enumerate every nonnegative distribution of that total, not only initially reachable states. Every positional transition retains its exact missing-token deficits or successor. Shared pre/post arcs consume then produce; zero-arc transitions are enabled even at zero tokens.

Initial distances, all shortest-prefix counts, canonical shortest witnesses, reverse-goal distances and every optimal next-transition tie are retained. A goal is not made absorbing. A self-loop is not a deadlock; a transition unused by a chosen shortest plan is not necessarily dead. Every transition's reachable enabling states and shortest enabling prefix are visible. Duplicate transition IDs remain separate actions.

## Every partial firing multiset

For every subcount vector k, retain `m(k)=initial+Ck`, even if negative. Such algebraic rows are not ordinary markings. Each remaining transition has its own target row, guard deficits and enabled flag. Prefix counts enumerate legal words reaching this row using exactly k; suffix counts enumerate legal residual words starting at this marking. A suffix can exist without a legal prefix.

Repeated occurrences of an identical transition ID are indistinguishable. The boundary counts `(2,2,2,2)` on four enabled no-ops yield `8!/(2!^4)=2520` legal words, not 8! labeled permutations. Empty sequences count once at a valid marking. Canonical prefix/suffix words are lexicographically smallest ID words. A count-realizable multiset can still end at the wrong goal; its goal-reaching count stays zero.

## Independent replay and reference

The Python generator uses BFS/reverse BFS and forward/backward count-lattice dynamic programming. The separate checker imports input validation only, recursively distributes total tokens, simulates actual token bags, uses Floyd-Warshall/incoming-shortest recursion and explicitly enumerates legal multiset words for each prefix/residual. Every field is reconstructed and exact types compared. It does not call the generator.

JavaScript implements a second runtime with all-pairs distances and count-lattice DP. Its browser replay regenerates with that same engine, so is not called an independent checker. All engines share the written contract and controls; agreement can share semantic mistakes. Exported JSON is unsigned consistency evidence relative to its embedded input, not proof of that input's provenance or suitability.

An optional real PM4Py 2.7.23 reference constructs ordinary places, transitions and weighted arcs directly from each request. Actual classic enabling/execute checks every full-state transition. Separate traversal exhausts its complete initially reachable graph and goal distance without a timeout cutoff; actual firing semantics also counts the supplied multiset words. It does not consume our incidence or expected-edge answers. PM4Py remains optional and nonvendored; native/browser runtimes need no external model or paid API.

## Reproduced evidence

| Check | Observed result |
|---|---|
| Native suite | 18 tests; all 14 original controls |
| Exhaustive tiny class | 4,704 ordered two-transition / initial-marking / count cases |
| Additional native generation | 350 seeded requests, full independent replay |
| Python/JavaScript | 114 complete reports; 629 marking rows; 806 lattice rows |
| Changed output leaves | All 197 noninput primitive forgeries rejected per engine |
| Actual PM4Py 2.7.23 | 164 requests; 771 enabling states; 1,541 transition results; 2,834 accepted count words; full reachable graphs and goal distances |
| Outside-checkout wheel | 6 module origins; 14 controls through 2 entrypoints; 28 forged CLI failures |
| Actual Chrome | 56 views at 1440/768/390/320; 268 state selections; 664 move rows; 496 lattice rows; 1,016 remaining-count decisions |
| Download replay | 14 trusted completed report downloads, each independently accepted by native CLI |

The exhaustive class uses all 14 conservative two-place transitions whose pre/post total is 0..2, every ordered pair, all six initial markings of total 0..2, counts each 0..1 and goal equal to reversed initial vector: `196*6*4=4704`. Seeded and developed controls are disclosed, not held-out empirical agent evaluation. Reference agreement does not independently certify every field. CLI rejection emits no partial report; duplicate keys, decimals/constants, bool-as-int, oversized and invalid input are tested. Editing browser input clears stale tables and disables evidence export until a valid recomputation.

## Publication and pixels

PR1 merged only after all six latest feature/PR jobs passed. Main `97fb7a1cea00cbdfea79bf7458234120c2550d6c` retains initial `45dbb4c1e34f838bd381476926a9d4a2b6361d26` and full feature `077fc5739d0e3e8436cc9fa92424eed5f4897e21` history. All 32 public files byte-match tested source. [Merged-main checks](https://github.com/midya8/firelab/actions/runs/42923424730) and [Pages](https://github.com/midya8/firelab/actions/runs/42923424869) passed. All five deployed assets are byte-exact. The full 56-view/14-download Chrome workflow passes against the live site. Of 32 unmasked captures, 31 match exactly. The remaining 390px boundary-control state table differs in 165 pixels inside a header label, maximum channel difference 56/255; both actual images were inspected with no content or layout change. Live desktop hero, mobile verdicts, narrow-phone lattice guards and boundary-state evidence were inspected directly. This verifies this published implementation, not a real resource protocol.

## Scope and prior work

2-4 places, at most 4 transitions, integer arc entries 0-2, each transition strictly conserves token total, initial total 0-3; each supplied count 0-3 with sum at most 8. At most 20 markings and 81 subcount rows. Ordinary untimed interleaving only. No inhibitor/read extension, colors, timing, simultaneous steps, fairness, unbounded nets, broad invariant basis, scalable planner, new theorem, speed benchmark or real-agent guarantee.

[Bonet's Petri Nets for Planners](https://bonetblai.github.io/tutorials/icaps11-petri.pdf), [Cabasino/Giua/Seatzu's structural analysis](http://wpage.unina.it/detommas/dssc/cap11_12control.pdf) and [linear algebraic techniques](https://www.cse.iitb.ac.in/~akshayss/courses/cs735/desel-alg.pdf) ground the enabling/equation/invariant distinctions. [TINA](https://projects.laas.fr/tina/manuals/tina.html), its [primary tool paper](https://projects.laas.fr/tina/papers/ijpr_04.pdf), [PM4Py](https://processintelligence.solutions/pm4py/api/api.html) and the [Hamburg tool catalog](https://www.informatik.uni-hamburg.de/TGI/PetriNets/tools/db/tina.html) establish broad prior tooling. No older complexity summary, reduced-graph convention or license discrepancy is silently blended into a new claim. Full source coverage is in the repository's SOURCES.md.

Existing STRIPSLab studies Boolean delete relaxation and action availability; BranchLab/ShieldLab check supplied graphs. FireLab instead starts from integer-token guards and distinguishes net-effect counts from executable order and arbitrary goal reachability. It does not claim Petri nets or finite exhaustive planning are new portfolio ideas.
