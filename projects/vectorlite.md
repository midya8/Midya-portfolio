# VectorLite

**A signature is not a neighbor.** A finite random-hyperplane retrieval inspector with exact candidate, probability and evaluation-protocol witnesses.

[Live inspector](https://midya8.github.io/vectorlite/) · [Source](https://github.com/midya8/vectorlite) · [Numerical/probability contract](https://github.com/midya8/vectorlite/blob/main/METHOD.md)

## Problem

A signature stores signs, not distances. A candidate filter can miss the exact best vector, and a self-query benchmark can reward finding the query itself. Candidate counts can also be mistaken for speed, even when an implementation scans every signature.

VectorLite makes those boundaries visible. The original dependency-free exact cosine/L2 and Gaussian-plane LSH library remains, with its original 12-vector corpus, demo, 31 tests and self-inclusive mean recall@3 of 1.0. Its original README is retained as historical context. The new contract corrects the earlier suggestion that lowering the sharing threshold can reduce recall for the same fixed index and score/id ordering.

## Implementation

### Finite geometry, not a screenshot of results

The working browser independently computes from editable vectors, query and actual exported planes. It shows normalized 2D directions without inventing a projection for higher-dimensional data, all dot products and bits, each vector's shared-bit count, every admitted/missed canonical exact neighbor and every threshold from 0 through the bit count. Input edits hide stale results until recomputation. Complete JSON export retains the witness.

The Gaussian-plane stream is generated in Python. JavaScript replays the actual planes rather than claiming a cross-language PRNG match. Explicit plane editing is supported, with probability references labeled as ideal iid-isotropic rebuild expectations, not conditional probabilities for arbitrary fixed planes.

### Stable arithmetic and honest ranking

Cosine scales each vector before normalization, avoiding the original direct-square overflow/underflow. `[1e300,1e300]` versus `[1e300,0]`, and their `1e-300` counterparts, now return approximately `sqrt(.5)`. Finite/dimension checks, unique ids and copied inputs prevent silent invalid scores or set-recall collapse. L2 uses stable distance arithmetic and rejects an unrepresentable result.

Zero vectors retain cosine 0 and all-positive bits, but their angular probabilities are undefined, not silently set to one half. Signs use unrounded dots with `>=0` mapped to bit 1. Display rounding does not set signatures or gates. Mean recall is no longer rounded before gate comparison. Approximate L2, which was previously silently treated as cosine, now fails clearly.

### Complete threshold and probability witnesses

For a fixed query, planes, k and score/id order, an admitted canonical exact top-k item must survive exact candidate rescoring: fewer than k corpus items precede it in the full ordering. Recall is therefore the fraction of ground-truth ids admitted. Lowering threshold creates nested candidates and cannot lower that recall. This says nothing about changing seeds or bit counts, semantic ties or another retrieval implementation.

For a nonzero pair, a random isotropic plane agrees with probability `p=1-theta/pi`. Across independent planes, shared bits follow a binomial distribution. VectorLite computes each threshold's marginal admission tail, expected candidate count and expected canonical recall. Candidate events share planes and can be correlated; no binomial law for total candidate count is claimed. The half-angle `atan2` identity stabilizes angular endpoints. Zero-vector theory is shown as undefined.

### Keep the protocol next to the number

- Original `self-inclusive` remains the default benchmark.
- `--exclude-self` removes the query id from both exact and approximate rankings, labeled `leave-one-id-out`. Duplicate vectors may remain; this is not held-out evaluation.
- `--queries` runs `external-supplied` vectors. Providing a file does not establish an independent split or relevance quality.

Two original synthetic vectors, the same query, 8 planes, seed 0 and strict threshold produce recall **1 with self included, 0 with its id excluded**. That control isolates an id-exclusion difference on this fixture, not general method performance.

## Verification

- **50 Python tests on 3.10-3.13**, including all 31 original tests unchanged; six original files including corpus/demo/tests remain byte-identical, and original README is preserved byte-exact.
- **Independent references:** 120 cosine pairs checked with 90-digit Decimal arithmetic, rational binomial tails, exhaustive 8-bit sign patterns, full-circle angular geometry and 1,200 seeded Gaussian rebuilds.
- **35 retained audits**, including original 8D data, synthetic 2D/5D controls, exact sign boundaries, zero vectors and self-exclusion pair. They regenerate byte-for-byte in the tested environments.
- **Independent scalar JavaScript:** 20,784 numerical fields across 643 threshold rows. Actual Chrome verifies all 332 vector rows, 643 threshold rows and 5,856 projection rows, invalidation, bad input, one JSON export and 320/390/1280 containment.
- **Installed distribution:** wheel imported outside checkout with six module origins, all 35 full audits, audit CLI and original-query CLI. Original offline demo and both gate sides remain.

## Bounds

This is an O(N) signature scan, not a bucketed/sublinear or production-scale ANN index. Candidate rescoring fractions are not latency or operation totals. Canonical score/id ties are a declared ground truth, not human relevance judgments. Near-zero projections and near-tied scores remain floating-point sensitive; same-environment reproducibility is not universal determinism.

The audit is deliberately bounded to 64 items, 16 dimensions, 128 bits and a 128KiB strict JSON spec. Probability theory assumes ideal independent isotropic nonzero planes and is not conditional on displayed fixed or edited arbitrary planes. The 1,200-rebuild check is a sanity control, not a confidence interval. These vectors are synthetic, not learned embeddings or a retrieval-quality benchmark. No speed, model-quality, confidence-interval or new-algorithm claim is made.

## Attribution and links

Random-hyperplane LSH is prior work. The [method contract](https://github.com/midya8/vectorlite/blob/main/METHOD.md) links Charikar's primary paper, UCSD geometry notes, SciPy's binomial definition, scikit-learn self-neighbor semantics, Python numerical documentation and ANN-Benchmarks as broader context. No benchmark code/data was copied. Implementation, original synthetic fixtures and audit by Midya Rahmani.

- [Repository](https://github.com/midya8/vectorlite)
- [Live geometry and recall inspector](https://midya8.github.io/vectorlite/)
- [Method and limitations](https://github.com/midya8/vectorlite/blob/main/METHOD.md)
- [Original historical README](https://github.com/midya8/vectorlite/blob/main/docs/original-readme.md)
