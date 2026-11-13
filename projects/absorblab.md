# AbsorbLab

Inspect a small supplied Markov chain in three ways: where it ends, which states can be grouped and what changes when probability moves within one row.

[First-hit inspector](https://midya8.github.io/absorblab/) · [Strong-lumping inspector](https://midya8.github.io/absorblab/lumping.html) · [Row-response inspector](https://midya8.github.io/absorblab/response.html) · [Source and reproduction](https://github.com/midya8/absorblab)

## A vanishing exit is not its limit

The row-response default has a self-loop and a goal edge, each with probability `1/2`. Moving mass from the loop to the goal changes the waiting time. As long as the goal edge stays positive, eventual success is one. When the last exit disappears, success becomes zero. The interior limit is still one; it is not the endpoint answer.

A retry control has success `(1/4+t)/(1/2+t)`, so its response has curvature rather than a flat baseline. The inspector shows the exact rational curves and derivatives, solves endpoints separately and counts success-conditioned visits and directed edges. Terminal outgoing edges are excluded from that traffic; zero-success conditioning stays undefined. The plot joins sampled points, while the displayed formula defines the interior response.

## Conditioning selects paths

The first-hit control starts with equal direct and risky branches. Given eventual success, those branches become `4/5` direct and `1/5` risky. Mean time given success is `6/5`, while unconditional time to stopped success is infinite. Removing failure edges locally leaves the original equal choice unchanged, so it does not explain this global selection.

The inspector exposes success, failure and never-terminal probabilities, conditional moments, closed-cycle witnesses, Doob-conditioned transitions and finite-horizon mass. First success or failure stops the run, including terminal roots at time zero. A closed nonterminal class can prevent either hit forever. Conditioning is selection, not an intervention that improves the original chain.

## Equal now can split next

Strong lumping asks whether states can share a block without changing block-transition probabilities. In the six-state control, equal immediate goal mass hides a second-round split: `s0` and `s1` separate after their successors do, while noncontiguous `s0` and `s5` remain merged. Every representative of a final block agrees, so the quotient needs no averaging.

The inspector shows refinement rounds, split witnesses, every set partition and the cell-by-cell identity `PC=CQ`. It uses the original transition matrix, including terminal outgoing edges, rather than substituting first-hit stopped rows. Observation tags and terminal status are part of the contract. "Exact" means rational arithmetic here, not the distinct conditional notion of exact lumpability.

## What is checked

The current suite has **42 Python tests and 11 Node tests**, including actual Chrome for all three inspectors. Python uses standard-library fractions; the browser uses separately written BigInt engines. Fresh installed wheels check fourteen module origins outside the checkout and run all twelve controls for each workflow through both console and module entrypoints. First-hit CLI checks reject twenty forgeries; lumping and response each reject 24 CLI and 24 direct-checker forgeries, with atomic output preservation on CLI failure.

| Workflow | Native/browser complete-report comparisons | Actual Chrome coverage |
| --- | --- | --- |
| First hit | 213 reports: twelve controls, 81 two-state cases and 120 seeded chains. | 36 control/width reports, every state/horizon/support/elimination selection and twelve completed downloads replayed natively. |
| Strong lumping | 527 reports, 6,448 partitions and 4,038 quotient cells. | 36 reports, every refinement/pair/partition/forecast selection and twelve completed downloads replayed natively. |
| Row response | 146 reports, 1,909 samples, 61,255 conditional edge cells and 15,435 derivative pairs. | 36 control reports, 1,293 root/sample views, twelve completed downloads replayed natively and twelve dense six-state views. |

The replay checkers use different support or algebra calculations, but share the schema and some helpers. Cross-implementation agreement is finite descriptive evidence, not a proof or a performance benchmark. The first-hit tests also cover all 9,261 three-state uniform nonempty-support/status cases, all 729 deterministic three-state/status cases, 120 acyclic chains checked by a separate full-path moment oracle and field-by-field certificate mutations.

All three optional SymPy 1.14.0 references were invoked. First hit checks 682 probability pairs and 351 conditional moment triplets on 213 inputs, using Boolean transitive closure and an independently formed conditioned chain. Lumping checks 527 requests, all partition mass matrices and 2,038 matrix-power identities, but imports the native generator and test corpus. Response checks 928 symbolic success/failure curves and 10,290 derivative pairs on 146 requests, using the reported transient indices. The latter two are algebra references, not independent support analyses or complete-report replay.

## Scope and sources

The input is a supplied chain with one to six states, up to six positive rational transitions per row and a horizon of 0-12. The row-response interior has fixed positive support; each endpoint is a separate chain. Finite forecasts do not truncate eventual quantities, and restricted visits do not assert finite lifetime in closed nonterminal classes.

This is an educational implementation, checker and set of controls built on established finite Markov, Doob-transform, strong-lumpability and rank-one inverse methods. It does not learn probabilities, estimate a real model, optimize policies, perform causal interventions, synthesize general parameters or guarantee real-agent behavior. The math is credited rather than claimed as new theory. The engines share a written specification; none is a theorem prover.

[First-hit method and sources](https://github.com/midya8/absorblab/blob/main/METHOD.md) · [Lumping method and sources](https://github.com/midya8/absorblab/blob/main/LUMPING.md) · [Response method and sources](https://github.com/midya8/absorblab/blob/main/RESPONSE.md)
