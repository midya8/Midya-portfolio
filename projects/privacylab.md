# PrivacyLab

[Repository](https://github.com/midya8/privacylab) · [Equations and limits](https://github.com/midya8/privacylab/blob/main/DESIGN.md) · [Complete exact report](https://github.com/midya8/privacylab/blob/main/examples/demo.json)

## What it does

PrivacyLab audits supplied finite probability tables against explicit neighboring-secret edges. It computes the smallest delta at an exact multiplicative factor t=exp(epsilon), with every directed-pair event witness and full rational arithmetic. Factor 3 means epsilon ln(3), not epsilon 3. The code does not learn a mechanism from private data or infer which datasets are neighbors.

![Exact finite-channel privacy audits and shared-coin joint-release failure](https://raw.githubusercontent.com/midya8/privacylab/main/assets/privacy-audit.svg)

## The failure worth making visible

Individually private-looking releases need not compose when their randomness is shared incorrectly. In the developed bit-secret control, Z is zero with probability 3/4 and the releases are A=secret XOR Z and B=Z. A alone has pure privacy factor 3 and B alone factor 1, but A XOR B recovers the secret exactly. The joint distributions have disjoint supports and delta 1 for every finite factor. Conditioning on A=0 makes B deterministically 0 versus 1, exposing the missing conditional-mechanism premise. This is a counterexample to reasoning from marginals, not to a DP composition theorem.

| Developed channel | Minimal pure factor | delta at factor 1 | delta at factor 3 | delta at factor 9 |
| --- | --- | --- | --- | --- |
| Randomized response, truthful probability 3/4 | 3 | 1/2 | 0 | 0 |
| Two independent releases | 9 | 1/2 | 3/8 | 0 |
| Vote with a fresh fair tie-break | 3 | 1/2 | 0 | 0 |
| Parity only | 1 | 0 | 0 | 0 |
| Shared coin: first marginal | 3 | 1/2 | 0 | 0 |
| Shared coin: second marginal | 1 | 0 | 0 | 0 |
| Shared coin: joint release | infinite | 1 | 1 | 1 |

Independent-product construction explicitly assumes fresh independent randomness conditional on the secret. Stochastic postprocessing uses one row-stochastic kernel unchanged for every secret, with fresh randomness. In the developed example the vote is exactly the original randomized-response channel, and parity is secret-independent with distribution [5/8,3/8]. More privacy is not a utility claim, and those helpers cannot verify that an outside program satisfies their randomness assumptions.

## Exact arithmetic and inspectable witnesses

For each listed undirected edge, both directed pairs are audited. At factor t the maximum over every event E of P(E)-tQ(E) is exactly the sum of positive P_k-tQ_k terms. Reports keep every term, probability ratio or explicit support mismatch, strict-positive attaining event and its P/Q masses, all zero-excess ties, singular mass, every worst pair and finite pure-factor witnesses. All-zeros outputs are distinct from positive mass over zero comparison probability. Unlisted secret pairs remain visible rather than silently covered.

Inputs are exact integers, unsigned decimal/fraction strings or API Fraction values; floats/bools are rejected. Rows sum exactly to 1 without renormalization. Work limits are 8 secrets, 64 outputs, 28 undirected edges,512-bit rational components and 100000-byte CLI input. Product artifacts preserve an explicit output-pair mapping and fail if output/rational limits would be exceeded. Point queries are not interpolated into an unverified full privacy curve.

## Verification and reproduction

29 tests reconstruct all demo terms/events and compare 24 seeded channels against exhaustive all 16-event searches per directed pair at four factors. A 10^-100 singular support leak remains exact. Minimal pure witnesses, profile monotonicity/convexity, omitted adjacency, permutations, full capacity, exact parsing, strict error paths and nonmutation/RNG state are covered. Transform tests check every product probability, exact binomial count channels through four randomized-response releases, 24 seeded stochastic-kernel contractions, shared-coin reconstruction/conditional failure, identity/constant/permutation kernels, alignment and limits. The SVG checks all 36 exact cells/coordinates, full report metadata, hidden attaining-event tampering and byte-exact regeneration. A five-module wheel matches both complete CLI JSON outputs outside checkout; CI covers Python 3.10-3.13 and package parity.

```sh
python -m privacylab demo
python -m privacylab audit examples/input.json
python -m unittest discover -s tests -v
python examples/render_figure.py --check
```

## Scope and attribution

Established DP and hockey-stick arithmetic, not a new privacy theorem. Sources include Dwork/Roth's [Algorithmic Foundations](https://homepage.divms.uiowa.edu/~sriram/5980/spring17/privacybook.pdf), [modern privacy accounting notes](https://arxiv.org/pdf/2210.00597) and Google Research's [accounting overview](https://research.google/blog/differential-privacy-accounting-by-connecting-the-dots/). No trained-model certification, secure sampler, real-data adjacency proof, DP-SGD accountant, advanced composition implementation, population-fact secrecy or privacy-utility optimum. Exactness concerns the supplied finite table and listed edges, not a deployed mechanism. Delta is not a per-person leak probability.

## Exact adaptive transcript extension

Version 0.2 adds full finite history-conditioned mechanism trees. At every node the caller supplies the next-output distribution given the secret and the entire transcript. All histories are required, including impossible ones. Fixed round factors multiply to T; they are not adaptively selected epsilon parameters. The code unfolds the exact joint channel and compares its actual hockey-stick delta with three auditable upper bounds.

![Exact adaptive transcript bounds and branch-weighted killed mass](https://raw.githubusercontent.com/midya8/privacylab/main/assets/adaptive-transcripts.svg)

For each directed neighbor pair, a substochastic kernel clips each local probability to `min(K_P, t_i*K_Q)`. Good mass flows down the tree without normalization. Every incoming mass, local delta, removed mass, child mass and leaf domination slack is retained. Leaf mass g is below both P and TQ; the telescoping deficit `1-sum(g)` therefore bounds the actual joint delta. The maximum directional deficit is at most `1-product_i(1-d_i)`, where each d_i is the worst conditional delta across all histories and listed directions, which is at most the clamped additive sum.

| Developed tree | T | Actual delta | Clipped bound | Uniform bound | Additive bound |
|---|---:|---:|---:|---:|---:|
| Independent pure randomized response | 9 | 0 | 0 | 0 | 0 |
| Adaptive randomized response or constant | 3 | 3/8 | 1/2 | 1/2 | 1/2 |
| Independent response at factor one | 1 | 1/2 | 3/4 | 3/4 | 1 |
| Fair branch, reveal on one side | 1 | 1/2 | 1/2 | 1 | 1 |
| Reveal only on an impossible history | 1 | 0 | 0 | 1 | 1 |
| Shared coin, actual conditional laws | 3 | 1 | 1 | 1 | 1 |

The fair branch charges conditional delta 1 only to incoming mass 1/2. A revealing but impossible node still has its conditional audit, yet incurs zero killed mass. The shared-coin joint from the original project is reproduced exactly by its true conditional laws: after A, B=A XOR secret is deterministic and revealing. Its marginal privacy cannot substitute for that conditional guarantee. A clipping bound can also be strictly looser than the actual profile, as the independent factor-one row shows.

### Verification of the extension

46 tests retain the original 29 and add 14 adaptive behavior plus three SVG tests. Twenty-four seeded three-round, three-secret trees use independent recursive path enumeration and exhaustive all-256-event searches per directed pair. Tests reconstruct conditional events and every flow/leaf inequality; compare the shared-coin joint with the original static report and independent trees with static products; exercise six rounds, 64 leaves, eight secrets and all 28 edges; and cover null histories, unary rounds, permutations, omitted adjacency, tiny exact mass, computed-rational limits and strict CLI errors. All 36 new figure cells/coordinates, both diagram edges, complete report metadata, hidden-witness tampering and regeneration are checked. Both figures regenerate byte-exactly; the six-module installed wheel matches all four complete CLI JSON outputs outside checkout. CI covers Python 3.10-3.13 and packaging.

```sh
python -m privacylab adaptive-demo
python -m privacylab adaptive examples/adaptive-input.json
python -m unittest discover -s tests -v
python examples/render_adaptive.py --check
```

[Full adaptive proof and contract](https://github.com/midya8/privacylab/blob/main/ADAPTIVE.md) · [Complete adaptive report](https://github.com/midya8/privacylab/blob/main/examples/adaptive-demo.json)

Limits are six rounds, eight outcomes per round, 64 transcripts, 128 conditional nodes and 512-bit constructed probability/flow components. The supplied kernels must really be the intended conditional laws; the code cannot verify an external sampler, randomness or real-data adjacency. Long canonical output fractions may require API Fraction values to resubmit under the 160-character input-string cap. The CLI has a separate 100000-byte input cap. This is established DP composition/subdistribution reasoning, not a new theorem, privacy filter, odometer, unbounded interaction, adaptive-parameter accountant, advanced/optimal composition implementation or training guarantee. Sources: [Dwork and Roth, section 3.5](https://homepage.divms.uiowa.edu/~sriram/5980/spring17/privacybook.pdf) and [fully adaptive composition context](https://arxiv.org/html/2203.05481v3); no filters or odometers from that paper are implemented.
