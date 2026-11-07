# SpecLab

Speculative decoding built from scratch in pure Python: output verified identical to target-only decoding on the tested configurations, with verification rounds counted exactly.

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

Bounds worth stating: greedy decoding only - the speculative sampling rejection rule is future work. Draft and target are n-gram toy models sharing structure, as real pairs do; no LLM-scale acceptance claim is made. Round savings are a modeled count: wall-clock gains in real deployments come from memory-bandwidth effects this project does not benchmark, and this implementation's actual scoring work is reported alongside the round count. Draft evaluations are reported separately as the real cost of speculation.

## Links

- Repository: [midya8/speclab](https://github.com/midya8/speclab)
