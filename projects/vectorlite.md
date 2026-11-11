# VectorLite

VectorLite now has actual reusable block buckets. An optional backend partitions fixed binary signatures into r+1 disjoint blocks, unions exact-key postings and verifies full Hamming distance before unchanged cosine/id rescoring. The original signature scan remains the default and reference.

[Live inspector](https://midya8.github.io/vectorlite/) · [Source](https://github.com/midya8/vectorlite) · [Numerical/probability contract](https://github.com/midya8/vectorlite/blob/main/METHOD.md)

## Actual optional block-bucket backend (v0.3)

59 Python tests retain all50 prior tests;8 Node/actual-Chrome tests retain all3 prior tests. Independent native and BigInt small-cube oracles each cover5,376 query/radius/mode comparisons. Another480 random excluded-query checks,360 random cosine rankings and105 original-spec backend rankings agree with scans. All34 full reports,1,908 selected Chrome rows,24 responsive views and2 trusted JSON exports are checked. An installed8-module wheel reproduces all35 old audits,34 new reports and both new CLI entrypoints.

A constructed512-row24-bit/radius2 control needs3 lookups,11 posting visits and9 full Hamming checks versus512 scan checks. A dense duplicate control would visit1,536 postings; auto instead scans after3 lookups. These are structural counts, not elapsed time, measured RAM or total operations. The fallback rule is a heuristic, not a general sublinear guarantee. Exact signature filtering is still approximate cosine retrieval, not semantic relevance. The r+1 exact-block method is a credited specialization of established multi-index hashing, not a new algorithm.

For radius r<bits, any code with at most r changed bits must share at least one of r+1 disjoint nonempty blocks. Each block has a real key-to-row-position posting table. Candidate union is only a superset: duplicates are removed by row index, exclusions apply before the full XOR/popcount check, and surviving ids receive the unchanged cosine score/id order. Duplicate signatures keep distinct positions. This is exact relative to the old threshold filter, not exact cosine nearest neighbors.

`HammingBuckets` copies signatures and supports repeated lookups at a fixed radius. `BucketLSHIndex` copies vectors/ids and retains the original hyperplanes and stable arithmetic. `scan`, forced `blocks` and `auto` modes expose key lookup count, posting-length sum, references visited, unique candidates, excluded entries, full checks and cosine rescores. The auto rule probes lengths without traversing postings and scans when their sum is at least N. All-radius and declared block-cap cases skip building tables entirely. Index construction still stores N times the number of blocks posting references; sparse query checks do not erase build, memory, union/sort or reporting costs.

The separate BigInt browser receives only input signatures, builds its own Map postings and shows partitions, occupied keys, query bucket lengths, all checked/admitted/rejected rows and per-row XOR/matching blocks. Changing input or policy hides stale output and disables exports. Strict input rejects duplicate keys, invalid hex, unknown keys and bad exclusions. JSON input/report exports replay native exactly, with no numeric tolerance. CLI/browser limits are128 bits,1,024 rows,128KiB; the generic native signature API allows up to4,096 bits and a maximum64-block declared cap. No online insertion/removal or in-place threshold change is implemented.

The original12-vector corpus,35 reports, scan, projections and original geometry browser engine remain unchanged. An additional original-corpus signature control XORs every code with the first query signature; this preserves Hamming distances, not a new embedding or cosine-quality evaluation. Sparse and dense constructed tables are both visible, alongside cap/all-radius, empty table, exclusions, false candidates and24 seeded tables. Source feature/PR/main checks and Pages deployment were verified before this showcase update;46 public files and12 live assets matched source.24 local/public and24 public/deployed unmasked pixel pairs matched exactly.

[Live block buckets](https://midya8.github.io/vectorlite/buckets.html) · [Algorithm, costs and source ledger](https://github.com/midya8/vectorlite/blob/main/BUCKETS.md) · [Source PR4](https://github.com/midya8/vectorlite/pull/4)

The earlier geometry/probability release follows. Its50-test and six-module installed evidence describes that retained release; the combined suite has59 tests and8 checked module origins. Its O(N) scan limitation still describes the original default, not a claim that the optional sparse query always traverses all codes.

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

The original default is an O(N) signature scan. The optional block backend above adds a real index but makes no general sublinear or production-scale ANN claim. Candidate rescoring fractions are not latency or operation totals. Canonical score/id ties are a declared ground truth, not human relevance judgments. Near-zero projections and near-tied scores remain floating-point sensitive; same-environment reproducibility is not universal determinism.

The audit is deliberately bounded to 64 items, 16 dimensions, 128 bits and a 128KiB strict JSON spec. Probability theory assumes ideal independent isotropic nonzero planes and is not conditional on displayed fixed or edited arbitrary planes. The 1,200-rebuild check is a sanity control, not a confidence interval. These vectors are synthetic, not learned embeddings or a retrieval-quality benchmark. No speed, model-quality, confidence-interval or new-algorithm claim is made.

## Attribution and links

Random-hyperplane LSH is prior work. The [method contract](https://github.com/midya8/vectorlite/blob/main/METHOD.md) links Charikar's primary paper, UCSD geometry notes, SciPy's binomial definition, scikit-learn self-neighbor semantics, Python numerical documentation and ANN-Benchmarks as broader context. No benchmark code/data was copied. Implementation, original synthetic fixtures and audit by Midya Rahmani.

- [Repository](https://github.com/midya8/vectorlite)
- [Live geometry and recall inspector](https://midya8.github.io/vectorlite/)
- [Method and limitations](https://github.com/midya8/vectorlite/blob/main/METHOD.md)
- [Original historical README](https://github.com/midya8/vectorlite/blob/main/docs/original-readme.md)
