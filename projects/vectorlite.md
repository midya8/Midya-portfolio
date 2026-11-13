# VectorLite: exact-code filtering, approximate vector search

VectorLite ranks supplied vectors by cosine or negative L2 distance. Its
random-hyperplane path filters candidates before cosine rescoring. The default
scans every signature; an optional fixed-radius backend reuses block postings.
Both have finite browser inspectors, with each projection, lookup and rejected
candidate available to inspect.

[Signature inspector](https://midya8.github.io/vectorlite/) · [Block-bucket inspector](https://midya8.github.io/vectorlite/buckets.html) · [Source](https://github.com/midya8/vectorlite)

## Choose a retrieval path

| Question | API | Boundary |
|---|---|---|
| Rank every supplied vector | `ExactIndex` | Floating cosine or negative L2, then ID ties |
| Filter by shared hyperplane bits | `LSHIndex` | Scan every signature; cosine-rescore admitted candidates |
| Reuse signature posting tables | `HammingBuckets`, `BucketLSHIndex` | Exact Hamming-radius filtering, not exact cosine neighbors |
| Inspect projections and every threshold | `vectorlite.audit.audit` | 64 items, 16 dimensions, 128 bits, 128 KiB JSON |
| Inspect block lookups and checked rows | `vectorlite.bucket_cli` | 1,024 rows, 128 bits, 128 KiB JSON |

```sh
python -m vectorlite query --vectors examples/data/vectors.jsonl \
  --query '0.9,0.1,0,0,0.1,0,0,0.1' -k 3
python -m vectorlite audit --spec examples/audit.json --json report.json
python -m unittest discover -s tests -v
bash examples/demo.sh
python scripts/build_audit.py
python scripts/build_buckets.py
node --test --test-concurrency=1 tests/engine.cjs tests/test_browser.cjs \
  tests/test_buckets.cjs tests/test_buckets_browser.cjs
bash scripts/wheel_smoke.sh
```

Runtime and tests use Python's standard library. The independent browser
engines use scalar JavaScript and BigInt. No model API, training, network or
embedding download is required to run the calculations.

## A signature is not a neighbor

The signature inspector recomputes from editable vectors, query and actual
exported planes. It shows normalized 2D directions without inventing a
projection for higher-dimensional data, every dot product and bit, shared-bit
counts, admitted and missed canonical exact neighbors, and every threshold
from zero through the bit count. Edits hide stale results until recomputation.

Python generates the Gaussian-plane stream. JavaScript replays the actual
planes rather than claiming a cross-language PRNG match. Explicit plane editing
is supported. Scan JSON export matches the current browser report; native
reports additionally carry `schema`, `plane_source` and `theory_contract`
metadata. Numerical/witness fields are independently compared with stated
floating tolerance, not advertised as byte-identical cross-language arithmetic.

Cosine scales vectors before normalization, avoiding direct-square overflow and
underflow. The `1e300` and `1e-300` versions of `[1,1]` versus `[1,0]` both give
approximately `sqrt(.5)`. Finite/dimension checks, unique IDs and copied inputs
prevent silent invalid scores or set-recall collapse. L2 uses stable distance
arithmetic and rejects unrepresentable results. Zero vectors retain cosine zero
and all-positive bits, but have undefined angular theory. Unrounded dots set
bits using `>=0`; full-precision means drive recall gates. Approximate L2 fails
rather than silently using cosine.

## Fixed-index recall and random-plane expectations

For fixed query, planes, k and score/ID ordering, lowering the shared-bit
threshold gives nested candidate sets. An admitted canonical exact top-k item
survives exact candidate rescoring, so canonical recall cannot fall. This does
not imply that more bits, a new seed or another tie policy improves recall.
Canonical ID ties are a declared ground truth, not human relevance.

For a nonzero pair, an ideal random isotropic plane agrees with probability
`p = 1 - theta/pi`. Independent planes give a binomial shared-bit count. The
inspector shows marginal admission tails, expected candidate count and expected
canonical recall over ideal iid rebuilds. These are not conditional probabilities
for the displayed fixed or edited planes. Candidate events share planes and may
be correlated; there is no binomial claim for their aggregate count. A half-angle
`atan2` identity stabilizes angular endpoints.

The original synthetic corpus retains self-inclusive mean recall@3 of 1.0.
`--exclude-self` removes the query ID from exact and approximate rankings;
duplicate vectors may remain. A two-vector control changes recall from 1 to 0
when only self exclusion changes. `--queries` accepts external supplied vectors.
Neither alternative establishes an independent held-out relevance evaluation.

## Reusable blocks, including the case where scanning wins

At radius `r < bits`, at most r changed bits cannot touch every one of `r+1`
disjoint nonempty blocks. Each true radius neighbor therefore shares an exact
block. Real key-to-row-position tables retrieve posting lists, union and
deduplicate positions, apply exclusions and check full XOR/popcount distance.
A block match is necessary, not sufficient. Duplicate signatures retain distinct
positions; surviving vectors get the unchanged cosine/ID order.

`HammingBuckets` copies signatures for repeated fixed-radius queries.
`BucketLSHIndex` also copies vectors/IDs and retains the original hyperplanes and
arithmetic. `scan`, forced `blocks` and `auto` expose lookups, posting-length
sum, visits, unique candidates, exclusions, full checks and cosine rescores.
Auto probes lengths without traversing lists and scans when their sum is at
least N. Radius covering all bits and declared block-cap cases skip table
construction and fall back even in forced-block mode.

A constructed 512-row, 24-bit/radius-2 control uses three lookups, 11 posting
visits and nine full Hamming checks instead of 512 scan checks. Dense duplicates
would visit 1,536 postings; auto instead scans after three lookups. These are
structural counts, not time, measured RAM or total operations. Building tables
still stores N times the number of blocks posting references. Union, sorting,
reporting and construction costs do not disappear. The heuristic is not a
general sublinear guarantee.

The separate BigInt browser builds its own Map postings from supplied
signatures. It exposes partitions, occupied keys, lookup lengths, every checked
row, XOR and matching blocks. Input/report downloads reproduce native reports
exactly. Edits hide stale output and disable exports. Strict parsing rejects
duplicate/unknown keys, invalid hex and bad exclusions. The generic native API
allows up to 4,096 bits and a declared cap of at most 64 blocks; the bounded
CLI/browser has the smaller limits in the table. Changing radius requires a
rebuild. Online insert/delete is not implemented.

The original 12-vector corpus remains. An additional control XORs its signatures
with the first query code, preserving Hamming distances without creating a new
embedding or quality benchmark. Sparse/dense tables, exclusions, false
candidates, empty tables, cap/all-radius fallbacks and 24 seeded tables are
available to inspect.

## Checks and limits

The current suite has **59 Python tests and eight Node/Chrome tests**.

- Numerical references include 90-digit Decimal cosine calculations, rational
  binomial tails, exhaustive sign patterns, full-circle geometry and 1,200
  seeded Gaussian rebuilds. Finite checks do not prove ideal PRNG behavior.
- The 35 scan audits contain 643 threshold rows and 20,784 numerical fields
  checked in independent JavaScript. Chrome checks 332 vector rows, 643 threshold
  rows and 5,856 projection rows, invalidation, errors and responsive containment.
- Each language checks 5,376 small-cube query/radius/mode comparisons. Other
  controls cover 480 random excluded-query cases, 360 cosine rankings and 105
  original-spec backend rankings. All 34 bucket reports match native exactly;
  Chrome checks 1,908 selected rows, 24 responsive views and trusted downloads.
- An installed wheel is checked outside the checkout through eight named import
  origins, all 35 scan audits, 105 original-spec rankings, 34 bucket reports,
  original query/audit commands and both bucket CLI entry points. Eight checked
  origins is not a claim that the package contains only eight Python files.

Near-zero projections and near-tied scores remain floating-point sensitive.
Synthetic vectors are not learned embeddings or human relevance labels.
Same-environment reproduction is not universal determinism. No latency,
measured-RAM, production-scale, semantic-relevance, recall-gain, model-quality or
new-algorithm claim follows.

## Method credit

Random-hyperplane LSH and multi-index hashing are established methods. The block
backend is a credited exact-block specialization, not a new algorithm.
[METHOD.md](https://github.com/midya8/vectorlite/blob/main/METHOD.md) and
[BUCKETS.md](https://github.com/midya8/vectorlite/blob/main/BUCKETS.md) retain the
contracts, source ledger and limitations. The original README is preserved
[as history](https://github.com/midya8/vectorlite/blob/main/docs/original-readme.md),
including older claims; it is not the current contract. No benchmark code or data
was copied. Implementation and original synthetic controls are by Midya Rahmani.
