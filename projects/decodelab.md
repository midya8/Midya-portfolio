# DecodeLab

Decoding strategies for language models, from scratch, with measured generation quality.

## Problem

Every language-model pipeline picks a decoding strategy - greedy, sampling at some temperature, top-k, top-p, beam search - and most pick by vibe. The choice changes output length, diversity and degeneracy, but without a controlled distribution and reproducible sampling there is no way to attribute a difference in output to the strategy rather than to luck.

## Approach

DecodeLab controls everything except the strategy:

- **An exact distribution** - an add-k smoothed n-gram model whose next-token probabilities come straight from corpus counts. Every token has defined probability mass, unseen contexts included, so strategies decode against ground truth.
- **Deterministic decoding** - greedy resolves ties by corpus frequency then lexicographic order; beam search ranks by total log probability with deterministic ordering. Samplers take an explicit seed: same seed, same corpus, same text.
- **Quality as metrics** - distinct-1 and distinct-2 (n-gram diversity), repetition rate (immediate self-repeats) and unigram entropy, computed per strategy and reported side by side in terminal, JSON and Markdown.
- **CI gates** - `--min-distinct-2` and `--max-repetition` fail the pipeline when a decoding change pushes generation below policy, so the tradeoff is enforced rather than documented.

## Verification

- 36 unit tests cover tokenization, model smoothing and normalization including unseen contexts, every strategy's determinism and filtering behavior, all metrics, all three report formats, and the CLI end to end including both sides of both gates.
- `bash examples/demo.sh` runs fully offline over a small AI-themed corpus: greedy output asserted exactly, seeded sampling asserted reproducible, a five-strategy comparison with JSON and Markdown reports, and both sides of the quality gate.
- CI runs the same suite across Python 3.10-3.13.

Bounds worth stating: the n-gram model is a stand-in that gives the strategies a real, exact distribution to work against - it demonstrates decoding behavior, not modern language-model quality. Metrics like distinct-n and repetition rate catch degenerate repetition, not factual correctness or coherence.

## Links

- Repository: [midya8/decodelab](https://github.com/midya8/decodelab)
