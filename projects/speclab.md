# SpecLab

Speculative decoding built from scratch in pure Python: proven-identical output with measured evaluation savings.

## Problem

Speculative decoding is usually sold with a speedup number and an equivalence footnote. SpecLab builds the mechanism itself - draft proposes, target verifies - and treats both halves as things to prove: the output must equal target-only decoding exactly, and the savings must be counted rather than estimated.

## Approach

- **Exact models** - draft and target are character-level n-grams over one deterministic corpus; the target's greedy choice comes straight from counts, so verification is ground truth, not an approximation.
- **Batched verification, honestly counted** - the whole drafted block scores in one pass counted as exactly one target evaluation; the counting contract is asserted in tests on both sides (naive = one eval per token, block = one eval per block).
- **Equivalence as a theorem tested broadly** - greedy speculative construction emits only target-confirmed or target-chosen tokens; the suite verifies exact equality across four draft/target configurations, three generation lengths, and gamma 1/2/4/8.
- **Acceptance measured, failure mode included** - a mismatched order-2/order-3 pair drops acceptance to 0.03 with savings nearly gone; pinned in the suite so measurement is demonstrably real.

## Verification

- 16 unit tests cover equivalence across configs and gammas, the evaluation-counting contracts, acceptance bounds and consistency, pinned fixture numbers, determinism, both sides of every CLI gate, and the low-acceptance negative control.
- Fixture results (8 prompts x 60 tokens, gamma=4): identical output on every prompt, mean acceptance 0.800, 122 vs 480 target evaluations - a 74.6% measured saving.
- `bash examples/demo.sh` runs fully offline and asserts both gate sides; CI runs the suite across Python 3.10-3.13.

Bounds worth stating: greedy decoding only - the speculative sampling rejection rule is future work. Draft and target are n-gram toy models sharing structure, as real pairs do; no LLM-scale acceptance claim is made. Savings are counted in target evaluations, not wall-clock: the latency argument is memory bandwidth, which this project counts rather than benchmarks. Draft evaluations are reported separately as the real cost of speculation.

## Links

- Repository: [midya8/speclab](https://github.com/midya8/speclab)
