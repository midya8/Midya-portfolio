# DPPLab: every finite subset, exactly

[Source](https://github.com/midya8/dpplab) · [Live inspector](https://midya8.github.io/dpplab/) · [Method and sources](https://github.com/midya8/dpplab/blob/main/METHOD.md)

Exact-rational finite DPP subset laws with every determinant, inclusion-kernel witness, Schur include/exclude conditioning and fixed-total-size contrast. Dependency-free Python and independent BigInt JavaScript agree on 24 complete reports / 4,050 exact leaves; 24 Python tests on 3.10-3.13 and actual-Chrome full-record/geometry checks. Duplicate-item controls separate zero co-occurrence from equal-marginal independence. Established bounded L-ensembles, not learned relevance, a scalable sampler or a downstream quality result.

## The control

L = [[4,4,0],[4,4,0],[0,0,1]] gives normalizer 18. Items 0 and 1 each have inclusion probability 4/9, but their joint inclusion is zero, versus 16/81 under independent equal marginals. Item 2 is independent with probability 1/2. Mean size is 25/18 and variance 113/324. This demonstrates supplied mathematical repulsion, not semantic diversity measured on a corpus.

## The implementation

Native Fraction elimination and Gauss-Jordan inversion compute every subset weight, normalizer, inclusion kernel and Schur residual. Independent BigInt JavaScript instead uses permutation determinants and adjugate inverses. The interface retains all exact fractions, every selected atom, all mode ties, item/cardinality laws and full matrix records; SVG uses decimal conversion only for geometry.

Include/exclude conditions are separate from optional fixed total size k. Residual kernels condition only on include/exclude; a highlighted warning prevents treating them as fixed-k kernels. Identity L with k=1 gives zero probability to the pair, even though its event-only inclusion determinant is 1/4. Impossible events return null laws, not a silently repaired answer.

## Independent evidence

- 24 Python tests on 3.10-3.13, including 120 determinant references, 50 inverse identities, 140 full Gram-kernel oracles, 100 conditioning oracles, 40 fixed-k scale controls and 20 sign-conjugation controls.
- 24 complete retained reports match all 4,050 exact native/BigInt leaves.
- Actual Chrome verifies 252 subset rows and full records, 786 matrix cells, 84 pair rows, 504 bar fraction/geometry witnesses, all selected laws, modes and matrix records, invalid/stale states and JSON export.
- Isolated installed-wheel reproduction checks all reports, console CLI and four module origins outside the checkout.
- Actual 320/390/1280 pixels and viewport containment checked; complete records wrap within mobile reading width, with supplemental wide tables explicitly scrollable.

## Contract and limits

One to five real-symmetric PSD likelihood-kernel items, at most 32 subsets. Every principal minor is checked exactly; singular valid kernels are kept. Input rational strings have length and reduced numerator/denominator bounds. Native strict JSON rejects duplicate keys; browser JSON.parse keeps the last duplicate. This parser difference is explicit, not hidden behind numerical agreement.

No model, embeddings, dataset, paid API, sampler, learned kernel, search/relevance benchmark, scale claim or novel DPP algorithm. Primary Kulesza/Taskar identities, official DPPy definitions/properties, independent MIT notes and the University of Toronto PSD criterion are linked in METHOD.md. Implementation and original synthetic controls by Midya Rahmani; no external code, figures, datasets or weights copied.
