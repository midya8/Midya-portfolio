# SpecLab

Speculative decoding built from scratch in pure Python: output verified identical to target-only decoding on the tested configurations, with verification rounds counted exactly.

## v0.2: exact stochastic probability laws

![Exact finite sampling audit](https://raw.githubusercontent.com/midya8/speclab/refs/heads/main/assets/stochastic-audit.svg)

A new independent finite-table engine samples draft tokens, accepts with
`min(1,p/q)`, and replaces the first rejected token with the normalized positive
residual. Full proposal/acceptance/rejection/bonus certificates support complete
sequence laws and joint sequence/count laws; a separate procedural sampler uses
exact integer RNG tickets. The original greedy n-gram path below is unchanged.

The corrected four-token law has exact TV zero; using the target directly as a
rejection fallback instead has TV `141/1024` on the prefix-dependent fixture.
Its expected `75/32` modeled verification rounds require `179/32` target positions
and `13/4` draft calls. Identical and disjoint-support controls retain honest
boundary behavior, including speculative overhead. Assigned parallel-round and
position-score costs are hypothetical, not measured latency or FLOPs.

34 tests cover both paths, including all 2,187 binary prefix-table pairs against
an independent kernel oracle, all 225 ternary quarter-grid distribution pairs,
36 vocabulary/horizon/lookahead configurations, and **every procedural RNG
ticket** for all 25 binary quarter-grid pairs at horizon 2. Both output and cost
laws match the analytical engine. The figure binds all 96 data cells and full
witness metadata. Five CI jobs cover Python 3.10-3.13, saved full JSON/SVG parity,
and all five CLI modes from an installed ten-module wheel outside checkout.

Supplied finite tables only: vocabulary 1..3, horizon 1..4, gamma 1..3. No EOS,
real model, GPU kernel or throughput benchmark. Same probability law does not
mean identical output under a shared seed. [Proof, schema, source distinctions
and counting contract](https://github.com/midya8/speclab/blob/main/STOCHASTIC.md).

## Original greedy n-gram implementation

## Problem

Speculative decoding is usually sold with a speedup number and an equivalence footnote. SpecLab builds the mechanism itself - draft proposes, target verifies - and treats both halves carefully: equivalence is an algorithm invariant of the greedy construction plus finite tests of this implementation, and the savings are a clearly-labeled modeled count, not a benchmark.

## Approach

- **Exact models** - draft and target are character-level n-grams over one deterministic corpus; the target's greedy choice comes straight from counts, so verification is ground truth, not an approximation.
- **Equivalence: invariant plus verification** - the ideal greedy construction emits only tokens the target greedily confirms or chooses itself, so it equals target-only greedy decoding; the checked-in implementation is verified against that invariant across four draft/target configurations, three generation lengths, and gamma 1/2/4/8.
- **Verification rounds, honestly labeled** - each drafted block counts as one modeled verification round (the batched pass a real deployment runs); the actual sequential scoring calls inside each round are counted separately and both numbers are reported.
- **Acceptance measured, failure mode included** - a mismatched order-2/order-3 pair drops acceptance to 0.03 with savings nearly gone; pinned in the suite so measurement is demonstrably real.

## Verification

- 14 unit tests cover implementation equivalence across configs and gammas, both counting contracts, acceptance bounds and consistency, pinned fixture numbers (including actual scoring work), determinism, both sides of every CLI gate, and the low-acceptance negative control.
- Fixture results (8 prompts x 60 tokens, gamma=4): identical output on every prompt, mean acceptance 0.800, 122 vs 480 verification rounds - a 74.6% modeled reduction; actual sequential scoring work 510 vs 480 calls, reported plainly.
- `bash examples/demo.sh` runs fully offline and asserts both gate sides; CI runs the suite across Python 3.10-3.13.

Bounds of this original path: greedy decoding only. The separate v0.2 finite-table stochastic sampler above does not change this n-gram evaluation. Draft and target are n-gram toy models sharing structure, as real pairs do; no LLM-scale acceptance claim is made. Round savings are a modeled count: wall-clock gains in real deployments come from memory-bandwidth effects this project does not benchmark, and this implementation's actual scoring work is reported alongside the round count. Draft evaluations are reported separately as the real cost of speculation.

## Links

- Repository: [midya8/speclab](https://github.com/midya8/speclab)
