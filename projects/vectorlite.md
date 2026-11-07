# VectorLite

Exact and approximate kNN vector search from scratch, with measured recall.

## Problem

Vector search demos usually show an index returning results, not how wrong those results are. Approximate nearest-neighbor indexes trade recall for speed, and the size of that tradeoff depends on the data, the seed and the configuration. Without an exact baseline to compare against, "approximate" is a promise nobody checked.

## Approach

VectorLite keeps the exact baseline next to the approximation and measures the gap:

- **Exact kNN** - brute-force cosine and L2 search over every vector with score-then-id tie-breaking, so results are deterministic and ground truth is always available at small and medium scale. It is O(n) per query by design: it exists to be correct, not fast.
- **Random-hyperplane LSH** - each vector hashes to a bit signature from seeded random hyperplanes; candidates are the vectors sharing enough signature bits with the query, rescored exactly before ranking. The same seed and data rebuild the identical index bit for bit, so results are reproducible and testable.
- **Recall as a first-class metric** - `benchmark` self-queries every vector through both indexes and reports mean recall@k of the approximate index against the exact one, with per-query detail in the JSON report.
- **A CI gate** - `--min-recall` fails the pipeline when an approximation change (fewer bits, a different seed, a lower sharing threshold) drops recall below policy, so the tradeoff is enforced rather than documented.

Vectors are JSONL, one `{"id": "...", "vector": [...]}` object per line, loaded with validation: uniform dimensions, finite numbers, duplicate-id rejection.

## Verification

- 31 unit tests cover vector math, JSONL loading validation, exact ordering and tie-breaking, LSH build determinism and seed sensitivity, signature-bit similarity, recall metrics, and the CLI end to end including both sides of the recall gate.
- `bash examples/demo.sh` runs fully offline over a clustered 12-vector dataset: an exact query, a benchmark asserting mean recall@3 of 0.9 or better, and both sides of the gate.
- CI runs the same suite across Python 3.10-3.13.

Bounds worth stating: random-hyperplane LSH approximates cosine similarity only (the L2 metric is exact-search only), and measured recall is a property of the dataset, seed and configuration under test - it is evidence, not a guarantee for other data. Both indexes are in-memory and single-machine; this is a correctness-first reference and evaluation harness, not a production-scale index.

## Links

- Repository: [midya8/vectorlite](https://github.com/midya8/vectorlite)
