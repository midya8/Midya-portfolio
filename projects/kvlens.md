# KVLens

KV-cached incremental decoding built from scratch in pure Python, verified token-for-token against full recompute with measured FLOP savings.

## Problem

Every production LLM serving stack relies on KV caching: recompute attention over the whole prefix for each generated token and decoding is quadratic in sequence length; cache each position's keys and values once and each step is linear. Most projects assert this; few show the two paths side by side, prove they produce the same distribution, and measure the savings instead of quoting big-O. KVLens does all three with no dependencies.

## Approach

- **One attention block, two decode paths** - a tiny causal multi-head attention block (Q/K/V projections, masked scaled dot-product attention, output head) with seeded weights. The full path recomputes Q/K/V and attention over the entire prefix per new token; the cached path runs a batched prefill that computes each prompt position's K/V once, then one incremental step per generated token attending over the cache.
- **Bitwise equivalence by construction** - both paths run the same operations in the same order, so their final-position logits are bitwise identical. The equivalence sweep confirms a max absolute logit difference of exactly 0.0 across two model configurations and five prefix lengths, and the test suite checks greedy generations token for token across further configs.
- **Measured savings, not assumed** - a matmul FLOP counter inside both paths reports the counted cost of each run: 36.9% saved at 2 generated tokens growing to 90.8% at 32 on the default fixture. At 1 generated token the paths cost the same - prefill is the full forward - and the curve test pins that shape.

## Verification

- 28 unit tests cover model shapes and seeded determinism, cache growth, bitwise logit equality, greedy equivalence across configurations, cost ordering (cached never exceeds full), the savings-curve shape, and every CLI command including both sides of each gate.
- `bash examples/demo.sh` runs fully offline: generates 32 tokens down both paths with `--require-identical --min-savings 0.85`, runs the equivalence sweep, and prints the savings curve.
- CI runs the same suite plus both gates across Python 3.10-3.13.

Bounds worth stating: weights are seeded, not trained, so generated sequences are not meaningful language - the project verifies decoding machinery, not model quality. The counter covers matmul FLOPs only and the project makes no latency claim: the real reason KV caching is fast is memory bandwidth, which a pure-Python model cannot measure. One attention block, greedy decoding only, no cross-sequence batching or cache eviction.

## Links

- Repository: [midya8/kvlens](https://github.com/midya8/kvlens)
