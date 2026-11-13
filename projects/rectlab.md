# RectLab

RectLab covers the ones in a small binary matrix with all-one rectangles. It computes minimum overlapping covers, disjoint partitions, maximal-only covers and fooling-set lower bounds, with exact counts and selectable optimal factor sets.

The current suite has 18 Python and 6 Node/Chrome tests. Python checks complete reports for every 3×3 binary matrix; separate browser code checks the finite corpus. Installed commands and a numerical SciPy reference are checked separately. These are bounded synthetic examples, not learned data or a scale benchmark.

[Live inspector](https://midya8.github.io/rectlab/) · [Source](https://github.com/midya8/rectlab) · [Reviewed implementation](https://github.com/midya8/rectlab/pull/1) · [Exact method](https://github.com/midya8/rectlab/blob/main/docs/method.md)

## Indexed optimal sets and factor membership

The launch version computed exact counts but displayed only the first cover in each family. Version 0.2 adds random access by canonical zero-based decimal index, plus every factor's exact optimum inclusion count. The certificate retains the first witness for deterministic replay while the UI can inspect any index, with native previous/next and direct entry. This is access by index, not a random sampler.

The default still has 68 unrestricted optimal covers. R0 appears in exactly one, while R12 appears in 40. Restricting to maximal factors makes R0 ineligible and changes R12's count to nine out of thirteen. No default factor is mandatory. In the unique-cover overlap control, all three selected factors are mandatory. These statements are about an explicitly counted finite family, not learned explanation likelihoods, uncertainty about the matrix or causal necessity.

Membership is relative to the selected family: mandatory means in every optimum, optional means some but not all, never optimal means none. Ineligible nonmaximal factors have zero incidence in maximal-only mode and are labeled separately. Summing all factor inclusion counts yields family count times minimum factor count. The empty input has one empty optimal set and no mandatory factors.

The generator propagates counts of optimal prefixes over the skip/take DP graph. A take edge contributes prefix count times exact suffix count to its factor. Shared states combine prefix multiplicities without identifying distinct sets. The checker instead forces each factor, then counts residual k-1-factor covers by inclusion-exclusion. For partitions it uses the independent residual partition recursion, only accepting residual optimum k-1. It reconstructs every inclusion vector and classification rather than trusting a displayed summary.

Lexicographic rank/unrank uses take-before-skip blocks of fixed-cardinality factor sets. Unrank subtracts whole exact suffix counts; rank adds blocks skipped by the selected factor list. No complete family is materialized by production access. Tests separately enumerate all optimum sets for every 3×3 matrix and developed control, checking order, bijection, reconstruction and each factor's membership. Indices are canonical unsigned decimal strings up to 100 digits and must be below the exact count; factor lists must be sorted distinct integer IDs and actually optimal. Invalid browser indices report rejection while preserving the last valid witness. Boundary buttons stop rather than wrap.

Schema `rectlab/2` includes the full census. Old schema 1 certificates are rejected rather than silently treated as if they carried new fields. Regenerate using their embedded input. The low-level rank/select methods take a generated or verified report; public input-based helpers compute their own report. This remains a bounded exact tool, not a new ranking algorithm, statistical sampler or certificate-authenticity system.

## Fooling-set lower-bound gap

The default synthetic 4×4 matrix is `0101 / 1101 / 1110 / 1011`, read row by row. Its 11 positive cells admit 41 nonempty all-one rectangles. Every cover needs at least four rectangles, but the maximum fooling-set size is only three. The gap is real: a valid largest fooling set does not certify the minimum cover size here.

The unrestricted optimum has 68 unordered minimum covers. Restricting factors to maximal rectangles leaves the size at four and reduces the count to 13. Both counts are correct for different candidate families. The interface states which family is selected, exposes its full factor membership census and can reconstruct any optimum by index. Its certificate keeps the first set as a deterministic canonical witness.

## Overlap changes the optimization problem

The developed overlap control is `1011 / 1100 / 1110 / 0001`. Its unique minimum cover has three rectangles. Every disjoint partition needs four. Its ordinary arithmetic rank is also four, which is why that rank is displayed as a contrast rather than used as a Boolean-rank lower bound.

B and C are binary factors. Their Boolean product uses OR over componentwise AND. Their ordinary product records coverage multiplicity instead. Amber cells in the multiplicity grid show overlap; thresholding positive multiplicities recovers the input. XOR is not used. Switching to the partition witness removes overlap at the price of a fourth factor.

## Maximal rectangles do not preserve the census

Any legal rectangle can be enlarged to a maximal one. Enlarging every rectangle of a minimum cover cannot increase its size. If fewer factors survived, the original cover was not minimum. This proves that an optimum exists using maximal factors. It does not preserve all optimum factorizations or their count.

RectLab lists every legal rectangle, marks maximal ones and computes the unrestricted and maximal-only counts separately. Concepts and closures are established adjacent mathematics, not renamed as a new discovery. ConceptLab owns the portfolio's concept-lattice and implication exploration; this project instead studies the exact cover/partition/counting distinction.

## Complete fooling-set evidence

Positive cells are numbered in row-major order. Every subset is classified. A fooling set contains no pair that fits in one legal rectangle. Two selected cells fail that test when both cross cells are positive; same-row and same-column pairs are correctly rejected too.

Each rejected subset carries its first obstructing pair. Every maximum witness is selectable and highlighted on the input grid. A maximum witness proves only the reported lower bound. Empty input has size zero and exactly one empty witness. The certificate includes the complete subset census, not only selected positive examples.

## Producer and independent verifier

The Python producer scans row/column subsets to generate candidates, then runs ordered skip/take dynamic programming over covered-cell masks. It stores minimum size, exact integer count and the lexicographically first optimal witness. Candidate reuse and factor permutations do not inflate counts. Partitions require disjoint masks. Zero matrices have one empty cover, not zero explanations.

The checker imports schema helpers only. It rediscovers legal rectangles from subsets of positive cells: a subset is a rectangle when its size equals the product of its distinct row and column counts. Inclusion-exclusion counts k-factor covers directly from candidate avoidance counts. Exact suffix counts reconstruct a lexicographic witness. A separate first-uncovered-cell recursion checks partitions without counting permutations. Determinant minors check arithmetic rank independently of the producer's rational elimination.

The checker reconstructs the entire report from the included input and rejects extra, missing, reordered, mistyped or forged fields. A bounded cache stores serialized expected reports keyed by the strictly validated matrix. This avoids repeating exponential work for many certificates for the same input; it does not make certificates authentic, signed, private or independent of their embedded inputs.

A separate JavaScript engine uses BigInt counts and exact rational row operations. Browser replay uses that same engine and is explicitly labeled same-engine. Downloaded certificates are independently checked with Python. Input edits clear stale reports and disable downloads until recomputation. Invalid matrices cannot silently leave an old result looking current.

## Numerical reference and its limits

SciPy 1.15.3/HiGHS receives fresh binary-variable models built directly from raw input cell subsets. Cover constraints require each positive cell to occur at least once; partition constraints require exactly once. A separate maximum-fooling-set model forbids choosing compatible pairs. All 159 nonempty models match exact objectives, and returned integer witnesses are checked against the raw matrix.

This is a floating-point MILP reference with numerical solver tolerances, not proof of exactness, independent optimum counts or a runtime benchmark. The exact native checker provides different bounded evidence. Established libraries and theory are credited rather than presented as a new algorithm.

## Reproduced evidence

| Check | Observed result |
|---|---|
| Python suite | 18 tests |
| Exhaustive tiny class | All 512 binary 3×3 matrices: complete independent reports plus every optimal set/order/rank and membership in all three families |
| Python/JavaScript corpus | 64 complete reports: nine developed controls and 55 seeded inputs |
| Retained evidence | 964 legal rectangles; 24,575 fooling-subset audits |
| Primitive tampering | All 170 primitive noninput fields in a three-positive-cell certificate forged individually and rejected per engine |
| Structural tampering | Extra/missing fields, reversed lists, invalid input types and Boolean-for-integer substitutions |
| Actual SciPy reference | 159 input-built cover/partition/fooling MILP models over 53 nonempty inputs |
| Installed wheel | Six site-packages module origins; nine controls; two CLI entrypoints; 18 forgery failures; 54 select/rank pairs |
| Actual Chrome | 36 control-width views at 1440/768/390/320; 108 witness-family selections; 520 optimal-set inspections; 2,988 membership rows; 192 maximum-fooling selections |
| Trusted browser transfers | Nine input and nine certificate downloads; certificates checked natively; one native upload/replay; trusted next/previous/index entry |

The exhaustive class is all 3×3 binary matrices, not every accepted 5×5 input. Seeded matrices vary dimensions and sparsity. Developed controls include lower-bound and partition gaps, census restrictions, solid rectangles, diagonal structure, empty input, unused rows and the twelve-one boundary. These are bounded checks, not statistical claims, learned data or a causal ablation.

## Publication

The original v0.2 publication checked all 30 source files and five executable browser assets, alongside hosted CI, Pages and deployed Chrome behavior. The current README-only review preserves all 29 other files. Deployed behavior checks cover all nine controls, three factor families, indexed selections, membership rows, input invalidation and trusted JSON transfers. Source tests, numerical reference checks and deployment checks provide different evidence; none is a claim of large-scale performance.

## Scope and sources

At most five rows, five columns and twelve positive cells. Every rectangle is nonempty; counts concern distinct unordered rectangle sets, not ordered matrix-factor columns or duplicate factors. The deterministic certificate retains index 0, but every optimum in each cover family is accessible by index, with a complete factor inclusion census. All maximum fooling witnesses are present. The UI and certificate explain this boundary.

No noisy or approximate factorization, missing-data completion, neural training, real-user permission inference, production role mining, deterministic communication protocol, scale advantage, new lower bound or formal-verification claim. Python CLI rejects duplicate JSON keys; browser JSON parsing does not promise that check. Certificates validate the embedded matrix, not the truth of a claimed real-world relation.

[Skiena's combinatorial generation lecture](https://www3.cs.stonybrook.edu/%7Eskiena/392/brazil/lecture3.pdf) grounds count-guided rank/unrank; [Python's itertools documentation](https://docs.python.org/3/library/itertools.html) grounds explicit combination test oracles. Existing ranking theory is credited, not claimed as new. The [IJCAI survey](https://ijcai.org/proceedings/2020/685) grounds Boolean OR factors and biclique equivalence. [Theis](https://arxiv.org/abs/0708.1174) grounds fooling-set lower bounds. [Pourmoradnasseri and Theis](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v24i2p37/pdf/) supplies rectangle-cover and conflict-graph definitions. [Bun's university notes](https://cs-people.bu.edu/mbun/courses/591_F19/notes/lec2.pdf) distinguish cover and partition. [Konecny's FCA tutorial](https://www.kde.cs.uni-kassel.de/icfca2023/assets/slides/Konecny.pdf) and the [binary factorization tutorial](https://cs.uef.fi/~pauli/bmf_tutorial/material.html) acknowledge existing related work. [SciPy's documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.milp.html) grounds the optional numerical reference. Original bounded implementation and synthetic controls; no third-party code, figures, dataset or weights copied.
