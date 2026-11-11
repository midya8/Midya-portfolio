# RectLab: a cover is not a partition

**A perfect reconstruction does not settle how its factors should be counted.** This finite Boolean factorization inspector separates minimum overlapping covers, minimum disjoint partitions, maximal-only factor restrictions and fooling-set lower bounds. Inspect the factors, not only the headline rank.

[Live inspector](https://midya8.github.io/rectlab/) · [Source](https://github.com/midya8/rectlab) · [Reviewed implementation](https://github.com/midya8/rectlab/pull/1) · [Exact method](https://github.com/midya8/rectlab/blob/main/docs/method.md)

## A lower bound can stop short

The default synthetic 4×4 matrix is `0101 / 1101 / 1110 / 1011`, read row by row. Its 11 positive cells admit 41 nonempty all-one rectangles. Every cover needs at least four rectangles, but the maximum fooling-set size is only three. The gap is real: a valid largest fooling set does not certify the minimum cover size here.

The unrestricted optimum has 68 unordered minimum covers. Restricting factors to maximal rectangles leaves the size at four and reduces the count to 13. Both counts are correct for different candidate families. The interface states which family is selected and displays its lexicographically first optimal factor-id set, not a truncated list presented as every optimum.

## Overlap changes the optimization problem

The developed overlap control is `1011 / 1100 / 1110 / 0001`. Its unique minimum cover has three rectangles. Every disjoint partition needs four. Its ordinary arithmetic rank is also four, which is why that rank is displayed as a contrast rather than used as a Boolean-rank lower bound.

B and C are binary factors. Their Boolean product uses OR over componentwise AND. Their ordinary product records coverage multiplicity instead. Amber cells in the multiplicity grid show overlap; thresholding positive multiplicities recovers the input. XOR is not used. Switching to the partition witness removes overlap at the price of a fourth factor.

## Maximal rectangles do not preserve the census

Any legal rectangle can be enlarged to a maximal one. Enlarging every rectangle of a minimum cover cannot increase its size. If fewer factors survived, the original cover was not minimum. This proves that an optimum exists using maximal factors. It does not preserve all optimum factorizations or their count.

RectLab lists every legal rectangle, marks maximal ones and computes the unrestricted and maximal-only counts separately. Concepts and closures are established adjacent mathematics, not renamed as a new discovery. ConceptLab owns the portfolio's concept-lattice and implication exploration; this project instead studies the exact cover/partition/counting distinction.

## Complete fooling-set evidence

Positive cells are numbered in row-major order. Every subset is classified. A fooling set contains no pair that fits in one legal rectangle. Two selected cells fail that test when both cross cells are positive; same-row and same-column pairs are correctly rejected too.

Each rejected subset carries its first obstructing pair. Every maximum witness is selectable and highlighted on the input grid. A maximum witness proves only the reported lower bound. Empty input has size zero and exactly one empty witness. The certificate includes the complete subset census, not only selected positive examples.

## Two constructions, independent checking

The Python producer scans row/column subsets to generate candidates, then runs ordered skip/take dynamic programming over covered-cell masks. It stores minimum size, exact integer count and the lexicographically first optimal witness. Candidate reuse and factor permutations do not inflate counts. Partitions require disjoint masks. Zero matrices have one empty cover, not zero explanations.

The checker imports schema helpers only. It rediscovers legal rectangles from subsets of positive cells: a subset is a rectangle when its size equals the product of its distinct row and column counts. Inclusion-exclusion counts k-factor covers directly from candidate avoidance counts. Exact suffix counts reconstruct a lexicographic witness. A separate first-uncovered-cell recursion checks partitions without counting permutations. Determinant minors check arithmetic rank independently of the producer's rational elimination.

The checker reconstructs the entire report from the included input and rejects extra, missing, reordered, mistyped or forged fields. A bounded cache stores serialized expected reports keyed by the strictly validated matrix. This avoids repeating exponential work for many certificates for the same input; it does not make certificates authentic, signed, private or independent of their embedded inputs.

A separate JavaScript engine uses BigInt counts and exact rational row operations. Browser replay uses that same engine and is explicitly labeled same-engine. Downloaded certificates are independently checked with Python. Input edits clear stale reports and disable downloads until recomputation. Invalid matrices cannot silently leave an old result looking current.

## Actual third-party reference, with its limit

SciPy 1.15.3/HiGHS receives fresh binary-variable models built directly from raw input cell subsets. Cover constraints require each positive cell to occur at least once; partition constraints require exactly once. A separate maximum-fooling-set model forbids choosing compatible pairs. All 159 nonempty models match exact objectives, and returned integer witnesses are checked against the raw matrix.

This is a floating-point MILP reference with numerical solver tolerances, not proof of exactness, independent optimum counts or a runtime benchmark. The exact native checker provides different bounded evidence. Established libraries and theory are credited rather than presented as a new algorithm.

## Reproduced evidence

| Check | Observed result |
|---|---|
| Python suite | 12 tests |
| Exhaustive tiny class | All 512 binary 3×3 matrices, complete reports compared with independent reconstruction |
| Python/JavaScript corpus | 64 complete reports: nine developed controls and 55 seeded inputs |
| Retained evidence | 964 legal rectangles; 24,575 fooling-subset audits |
| Primitive tampering | All 140 primitive noninput fields in a three-positive-cell certificate forged individually and rejected per engine |
| Structural tampering | Extra/missing fields, reversed lists, invalid input types and Boolean-for-integer substitutions |
| Actual SciPy reference | 159 input-built cover/partition/fooling MILP models over 53 nonempty inputs |
| Installed wheel | Five site-packages module origins; nine controls; two CLI entrypoints; 18 forgery failures |
| Actual Chrome | 36 control-width views at 1440/768/390/320; 108 witness-family selections; 192 maximum-fooling selections |
| Trusted browser transfers | Nine input and nine certificate downloads; certificates checked natively; one native upload/replay |

The exhaustive class is all 3×3 binary matrices, not every accepted 5×5 input. Seeded matrices vary dimensions and sparsity. Developed controls include lower-bound and partition gaps, census restrictions, solid rectangles, diagonal structure, empty input, unused rows and the twelve-one boundary. These are bounded checks, not statistical claims, learned data or a causal ablation.

## Publication

PR1 merged after all 10 latest feature/PR jobs passed. All 28 public source files match the checked implementation, and the public checkout reproduces the native/browser and isolated installed-package checks. Merged-main CI and Pages passed. Five live assets match merged source; the complete deployed Chrome workflow passes, and all 36 unmasked captures match local pixels. Actual desktop, phone and narrow layouts were inspected. Portfolio/profile publication and visual checks remain pending until separately observed.

## Scope and sources

At most five rows, five columns and twelve positive cells. Every rectangle is nonempty; counts concern distinct unordered rectangle sets, not ordered matrix-factor columns or duplicate factors. Only one optimum witness per cover family is shown, although exact counts cover the entire family. All maximum fooling witnesses are present. The UI and certificate explain this boundary.

No noisy or approximate factorization, missing-data completion, neural training, real-user permission inference, production role mining, deterministic communication protocol, scale advantage, new lower bound or formal-verification claim. Python CLI rejects duplicate JSON keys; browser JSON parsing does not promise that check. Certificates validate the embedded matrix, not the truth of a claimed real-world relation.

The [IJCAI survey](https://ijcai.org/proceedings/2020/685) grounds Boolean OR factors and biclique equivalence. [Theis](https://arxiv.org/abs/0708.1174) grounds fooling-set lower bounds. [Pourmoradnasseri and Theis](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v24i2p37/pdf/) supplies rectangle-cover and conflict-graph definitions. [Bun's university notes](https://cs-people.bu.edu/mbun/courses/591_F19/notes/lec2.pdf) distinguish cover and partition. [Konecny's FCA tutorial](https://www.kde.cs.uni-kassel.de/icfca2023/assets/slides/Konecny.pdf) and the [binary factorization tutorial](https://cs.uef.fi/~pauli/bmf_tutorial/material.html) acknowledge existing related work. [SciPy's documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.milp.html) grounds the optional numerical reference. Original bounded implementation and synthetic controls; no third-party code, figures, dataset or weights copied.
