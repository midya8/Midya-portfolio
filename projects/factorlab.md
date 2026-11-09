# FactorLab: sum is not max

[Source](https://github.com/midya8/factorlab) · [Live inspector](https://midya8.github.io/factorlab/) · [Method and sources](https://github.com/midya8/factorlab/blob/main/METHOD.md)

## Why this exists

A graph alone does not tell you what inference question was answered. Summing hidden variables, maximizing a joint assignment and maximizing a marginal decision can produce different answers. An elimination order can change the question when sum and max are mixed, or change allocated table size while preserving the answer when they are not.

## What it implements

- Nonnegative rational binary factors with explicit little-endian scope indexing.
- Evidence restriction, scalar factors and injected units for variables absent from all factors.
- Every joined product with source-factor indices and values.
- Every two-branch reduction with all max ties and complete generated factors.
- Primal graph, per-step fill edges and induced width, without numerical sparsity shortcuts.
- Complete structural census of up to 120 orders and replay in the browser.
- Independent exhaustive joint weights, partition, marginal-MAP masses and all optimal ties.
- Editable independent BigInt inference, full current JSON export and stale/error clearing.

## The retained counterexample

The factor on scope [0,1] has little-endian values [6,5,0,5]. With x0 as the MAP decision and x1 hidden, summing first gives x0 masses [6,10]. The optimum is x0=1 with probability 10/16=5/8. Maximizing x0 first instead computes max(6,5)+max(0,5)=11, an upper bound that is not an attainable marginal-MAP mass.

The joint mode is x0=0,x1=0 with weight 6. Projecting it onto x0 picks the wrong marginal decision. These are different questions, not a numerical instability or an alleged learned mechanism.

A separate five-variable star has identical all-sum partition for hub-first and leaves-first schedules. Their dense joined-table counts are 62 and 18, with induced widths 4 and 1. This is an exact allocation comparison, not wall-clock speed or process-memory evidence. Observed hub, zero mass, disconnected factors, absent variables, exact ties, all-observed inputs and ten seeded cyclic controls remain present.

## Verification

24 Python tests pass on 3.10-3.13. They include 160 dense scalar references, 100 full current-factor-product references, all orders on 20 random four-variable graphs for all-sum/all-max/mixed queries, 40 rescaling controls and an independent adjacency-set census. Controls inside tests are not separate test methods.

24 complete native/BigInt reports match 23,114 exact leaves. Actual Chrome checks 1,939 complete selected records: 325 joint, 406 joined products, 203 reductions, 75 steps, 69 sliced factors and 861 census records. It also checks 21 fill edges, 75 bars, all tables/summaries, SVG geometry/colors, order replay, export, invalid/stale clearing and 320/390/1280 containment. Installed-wheel reproduction verifies all reports, both CLI routes and four module origins outside checkout.

## Boundaries and prior work

At most five binary variables, ten factors and 32 full assignments. Exhaustive reference/census work is exponential. Nonnegative multiplication supports the max distributivity used here; negative factors are rejected. Sum-before-max is sufficient, not necessary: disconnected or tied factors can make an interleaving agree. Matching a tiny reference is not a universal ordering rule. Invalid schedules return bounds, not assignments or posterior probabilities.

Zero evidence mass leaves probabilities null. Inputs are arbitrary potentials: an evidence-restricted partition is not P(e) without the full unconditioned normalizer. Conceptual operation counts exclude rational bit growth, reference enumeration and browser overhead. Minimum census width concerns the evidence-sliced primal graph, not constrained marginal-MAP width.

Native JSON rejects duplicate keys, floating-point index tokens and inputs beyond 32KiB UTF-8. Browser JSON.parse keeps the last duplicate key, accepts integer-valued numeric tokens such as 1.0, and bounds 32,768 characters. Potential arithmetic is exact in both.

Established variable elimination and mixed-query theory is credited to Peyrard et al.; Liu and Ihler; Urtasun and Hazan; MIT 6.438; Gormley; and Lee, Marinescu, Dechter and Ihler. METHOD.md records exact sources and normalized-model/typography qualifications. No belief propagation, variational inference, anytime search, learned predictor, new algorithm or formal verification is claimed. Implementation, independent checks and original synthetic controls by Midya Rahmani; no external source code, figures, data or weights copied.
