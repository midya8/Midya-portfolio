# EmbedKit

Train word embeddings from scratch with pure-Python SGNS, then evaluate how well they separate topics.

## Problem

Embeddings sit under retrieval, RAG and semantic search, but in most projects they arrive pre-trained and opaque. Showing you understand them means training them: implementing the skip-gram objective, negative sampling and the evaluation loop that tells you whether the vectors learned anything.

## Approach

- **SGNS with no dependencies** - for each (center, context) pair, plain sigmoid-gradient SGD pushes the center vector toward the context vector and away from k negatives, with the dot product clamped for numerical stability. Dimension, window, negative count, learning rate and epochs are all parameters.
- **Unigram^0.75 negative sampling** - the classic Word2Vec smoothing of the frequency distribution, drawn by binary search over a cumulative table.
- **Deterministic by construction** - weight initialization, epoch shuffling and negative draws all come from a single seeded RNG, so the same corpus and seed reproduce the same vectors bit for bit - which is what makes quality numbers testable.
- **Coherence evaluation** - given labeled topic clusters, each word is scored by the fraction of its k nearest neighbors in the same cluster, plus a separation margin between mean intra-cluster and inter-cluster similarity. `--min-coherence` and `--min-margin` turn embedding quality into a CI gate, and terminal, JSON and Markdown reports carry the results.

## Verification

- 40 unit tests cover tokenization, the Embeddings API (similarity symmetry, self-exclusion, lexicographic tie-breaks, zero-vector handling), negative sampling, training determinism, `min_count` filtering and parameter validation, trained-quality assertions on the checked-in corpus (same-topic similarity beats cross-topic, 90%+ neighbor purity), coherence and separation math including error cases, all three report formats, and the CLI end to end including both sides of every gate.
- `bash examples/demo.sh` runs fully offline: trains on the checked-in three-topic corpus (regenerated deterministically by `examples/data/gen_corpus.py`), shows same-topic neighbors, passes the quality gates, asserts report contents, and confirms an impossible gate fails.
- CI runs the same suite across Python 3.10-3.13.

Bounds worth stating: this is SGNS on a small synthetic corpus - it demonstrates the training mechanics and the evaluation loop, it does not produce embeddings comparable to models trained on large natural corpora. The demo corpus is well separated by construction, so coherence 1.0 there shows the objective learns the structure it is given, not that the method solves topic modeling. For a classical non-neural baseline on real text, PPMI + SVD over a co-occurrence matrix is the usual alternative.

## Links

- Repository: [midya8/embedkit](https://github.com/midya8/embedkit)
