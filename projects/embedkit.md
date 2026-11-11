# EmbedKit: inside the sampled step

EmbedKit now audits the noise behind its negatives. The unchanged sampler excludes positive context and earlier negatives, retries20 times, then returns the first eligible sorted word. Native Fraction and independent browser BigInt count exact53-bit proposal intervals and propagate every reachable bounded subset state, with finite retry versus unlimited conditional rejection on the same proposals.

## Exact finite retry sampler audit

61 Python tests retain all53 prior tests and40 original trainer tests. Eight Node/actual-Chrome tests retain all4 prior tests;33 complete reports agree on2,085 exact rational strings and3,682 numeric values, with maximum normalized decimal-display delta2.22e-16. Independent enumeration checks10,844 small-grid random tuples and289 unlimited-conditional ordered paths. Scripted calls exercise1,659 actual original-sampler grid boundaries plus success/retry/fallback consumption. All195 witness states,20 responsive views and2 trusted downloads are checked. A fresh10-module installed package reproduces original training/19 old step reports and all33 sampler reports through both new entrypoints.

Source feature/PR/main checks and Pages deployment were verified before this showcase update. Exact probabilities assume independent uniform-grid proposals, not a true-IID claim about deterministic PRNG output or an exact fixed-seed joint law. Multi-draw audits are bounded to8 words; the unchanged32-word synthetic corpus is one draw only. Final subset TV is not ordered-sequence TV, and inclusion weights do not imply expected changing-vector SGD updates. Expected fallback events are not probability of any fallback. Undefined unlimited rejection at zero eligible mass stays undefined. No training-quality, speed, generalization or new-algorithm claim.

The constructed default counts are a:1, b:1, z:1,000,000 with positive context z excluded. Under independent53-bit grid proposals and20 attempts, fallback probability is0.9987359285, selection of sorted-first a is0.9993679643 and selection of b is0.0006320357. Unlimited rejection gives about0.5 each on the same stored-threshold proposal. The tiny a/b asymmetry comes from exact grid endpoints, not an imposed equality. This is a stress case, not a natural-language benchmark.

For excluded proposal mass e, the geometric factor G is the sum of e^t for t=0..A-1. Each eligible word receives its proposal mass times G; the sorted first eligible word additionally receives e^A. Expected random calls equal G. A subset-mask dynamic program sums all ordered paths reaching each subset, then applies the same state-dependent transition. It returns every state/outgoing law, exact interval counts, final inclusion, expected fallback events, expected proposals and final subset total variation. Selecting all eligible words can give final-subset TV zero even while intermediate laws differ.

Stored binary64 thresholds are inputs. Count witnesses read the unchanged original closure, preserving its count^0.75 construction and rounding. Strict comparisons use exact ceil(D*threshold) endpoints, with the last word receiving residual grid mass because the last stored threshold is not tested. Repeated thresholds and zero proposal masses are supported. At e=1 finite retry returns afterA draws but unlimited rejection never returns, so the comparator is undefined, not uniform.

The editable independent page supports exclusions, retry and grid counterfactuals, state/layer selection, full exact report and input exports. Edits clear prior output and disable downloads; duplicate keys, nonfinite values, infeasible draw counts and out-of-bound shapes are rejected. Bounds are2..32 words for zero/one draw, at most8 words for complete multi-draw laws,1..53 bits and1..20 attempts. Original32-word counts retain all1,658 tokens; named controls cover skew, balance, center eligibility, duplicate thresholds and zero eligible mass. Twenty-four seeded tables supplement the controls without replacing originals.

[Live sampler audit](https://midya8.github.io/embedkit/sampler.html) · [Source PR3](https://github.com/midya8/embedkit/pull/3) · [Math and eight-source ledger](https://github.com/midya8/embedkit/blob/main/SAMPLER.md)

The earlier sampled-step evidence follows. Its53-test/four-browser-test counts describe the retained release, not the combined61/eight suite.

## From objective to update

Independent editable SGNS objective and gradient inspector: every sampled event, 1,593 coordinate finite differences, real sequential replay versus a frozen simultaneous step, and visible clamp/order effects. Twelve original pairs capture 72 actual calls; seven labeled controls expose repetition, conflicting labels, saturation and overshoot. Full 300-sentence corpus and all 32 trained vectors retained; browser recomputes all 992 cosine neighbors. 53 Python tests and four Node/actual-Chrome tests compare 19 complete reports. Original 40 tests, trainer and gates remain unchanged.

The frozen objective is a sum of stable softplus terms. Repeated output rows accumulate gradients; input and output roles are separate tables even if their word names match. Every analytic gradient coordinate is compared with a central difference, and every sequential event exposes pre/post vectors, raw/clipped logits, true logistic factor and original update factor.

The unchanged trainer applies the positive event and each negative in order, with a ±15 logit clamp. A simultaneous step on the frozen summed gradient is a different policy. Both final losses are evaluated on the same fixed event list. The constructed overshoot control increases simultaneous loss from 16.0007 to 47.9464 at lr=2. Neither update is claimed to guarantee descent.

## Original model, not a selected projection

All original source, corpus generator, 300 sentences, 32-word vocabulary, 512 trained input-vector coordinates and 24 topic-evaluation words remain. At dimension 16, 30 epochs and seed 7, original coherence is 1.0000 and separation margin 0.6033. The browser computes all 31 neighbors of any of the 32 words. Full corpus, vectors and fixture inputs can be downloaded; no synthetic two-dimensional picture replaces the model.

The original sampler uses unigram^0.75 base weights with positive-context and already-drawn exclusions, a vocabulary-size cap and a first-eligible fallback after twenty rejected draws. Its actual sequential draw law is not IID base-weight sampling. Repeated negatives and contradictory labels are constructed editor controls, not sampler outputs.

## Verification

- 53 Python tests on 3.10-3.13, including all 40 unchanged originals.
- Four Node/real-Chrome tests compare 19 complete reports with 28,107 numeric values, all 1,593 finite-difference coordinates, all fixture/output-row selectors, all 992 neighbors, invalid-state clearing, three JSON exports, keyboard controls and 320/390/1280 layouts.
- Read-only trace capture checks all 72 real event returns. Capture arithmetic is exact on CPython 3.10; supported-runtime replay uses 1e-13 coordinate tolerance. The inspector uses explicit sequential binary64 reductions; the original trainer keeps its runtime's sum behavior.
- Isolated installation outside the checkout imports eight modules, retrains the entire original model, verifies all reports and captures and runs three CLI commands. Full original demo and both gate sides remain.
- Public branch source, current native main, CI and deployment are checked independently. Witness archives retain all fields, each below 164KB.

## Limits and attribution

Fixed sampled logistic losses are not expected-noise losses or calibrated word probabilities. Finite differences are diagnostics, not proofs. When saturated, clamping changes the update factor from the true logistic gradient. The small synthetic topics are separated by construction; coherence 1.0 is not a natural-language benchmark. No speed, generalization or new-algorithm claim is made. SGNS and its derivatives are attributed to standard prior work in STEP.md.

## Links

- [Source](https://github.com/midya8/embedkit)
- [Implementation PR #2](https://github.com/midya8/embedkit/pull/2)
- [Live inspector](https://midya8.github.io/embedkit/)
- [Math, tolerances and sources](https://github.com/midya8/embedkit/blob/main/STEP.md)
