# EmbedKit: inspect word-vector updates and sampling

EmbedKit trains word vectors from scratch in Python, then opens up the two parts that are easy to hide: the sampled weight update and the negative-sampling policy. The browser inspectors let you edit inputs, replay events and check the full reports against the native implementation.

The sampler's fallback can dominate its proposal weights. In a deliberately skewed table with counts a:1, b:1 and z:1,000,000, excluding z makes the sampler choose sorted-first a about 99.94% of the time. Unlimited rejection gives roughly 50% to each eligible word on the same stored proposal. That is a constructed policy stress case, not a language-quality result.

## Where to start

| Question | Open or run | What it shows |
| --- | --- | --- |
| What changes during one sampled update? | [Step inspector](https://midya8.github.io/embedkit/) | Every gradient coordinate and event, with a separate frozen simultaneous-step control |
| How do retries and fallback change negative selection? | [Sampler audit](https://midya8.github.io/embedkit/sampler.html) | Exact bounded subset laws under independent uniform-grid proposals |
| Do the original embeddings separate these topics? | `nearest`, `evaluate` | Neighbor coherence on the unchanged synthetic corpus, not a natural-language benchmark |
| Can I reproduce a browser report outside the checkout? | `inspect`, `embedkit-sampler`, `examples/verify_wheel.sh` | Native report replay and isolated-package checks |

The current suite has 61 Python tests and eight Node/real-Chrome tests. Counts for the earlier sampled-step release below describe that retained stage, not the combined suite.

## Check the finite-retry sampling policy

61 Python tests retain all 53 prior tests and 40 original trainer tests. Eight Node/actual-Chrome tests retain all 4 prior tests; 33 complete reports agree on 2,085 exact rational strings and 3,682 numeric values, with maximum normalized decimal-display delta 2.22e-16. Independent enumeration checks 10,844 small-grid random tuples and 289 unlimited-conditional ordered paths. Scripted calls exercise 1,659 actual original-sampler grid boundaries plus success/retry/fallback consumption. All 195 witness states, 20 responsive views and 2 trusted downloads are checked. A fresh 10-module installed package reproduces original training / 19 old step reports and all 33 sampler reports through both new entrypoints.

The current native main, hosted checks and deployed browser assets were checked independently. Exact probabilities assume independent uniform-grid proposals, not a true-IID claim about deterministic PRNG output or an exact fixed-seed joint law. Multi-draw audits are bounded to 8 words; the unchanged 32-word synthetic corpus is one draw only. Final subset TV is not ordered-sequence TV, and inclusion weights do not imply expected changing-vector SGD updates. Expected fallback events are not probability of any fallback. Undefined unlimited rejection at zero eligible mass stays undefined. No training-quality, speed, generalization or new-algorithm claim.

The constructed default counts are a:1, b:1, z:1,000,000 with positive context z excluded. Under independent 53-bit grid proposals and 20 attempts, fallback probability is 0.9987359285, selection of sorted-first a is 0.9993679643 and selection of b is 0.0006320357. Unlimited rejection gives about 0.5 each on the same stored-threshold proposal. The tiny a/b asymmetry comes from exact grid endpoints, not an imposed equality. This is a stress case, not a natural-language benchmark.

For excluded proposal mass e, the geometric factor G is the sum of e^t for t=0..A-1. Each eligible word receives its proposal mass times G; the sorted first eligible word additionally receives e^A. Expected random calls equal G. A subset-mask dynamic program sums all ordered paths reaching each subset, then applies the same state-dependent transition. It returns every state/outgoing law, exact interval counts, final inclusion, expected fallback events, expected proposals and final subset total variation. Selecting all eligible words can give final-subset TV zero even while intermediate laws differ.

Stored binary64 thresholds are inputs. Count witnesses read the unchanged original closure, preserving its count^0.75 construction and rounding. Strict comparisons use exact ceil(D*threshold) endpoints, with the last word receiving residual grid mass because the last stored threshold is not tested. Repeated thresholds and zero proposal masses are supported. At e=1 finite retry returns after A draws but unlimited rejection never returns, so the comparator is undefined, not uniform.

The editable independent page supports exclusions, retry and grid counterfactuals, state/layer selection, full exact report and input exports. Edits clear prior output and disable downloads; duplicate keys, nonfinite values, infeasible draw counts and out-of-bound shapes are rejected. Bounds are 2..32 words for zero/one draw, at most 8 words for complete multi-draw laws, 1..53 bits and 1..20 attempts. Original 32-word counts retain all 1,658 tokens; named controls cover skew, balance, center eligibility, duplicate thresholds and zero eligible mass. Twenty-four seeded tables supplement the controls without replacing originals.

[Live sampler audit](https://midya8.github.io/embedkit/sampler.html) · [Source PR3](https://github.com/midya8/embedkit/pull/3) · [Math and eight-source ledger](https://github.com/midya8/embedkit/blob/main/SAMPLER.md)

The earlier sampled-step evidence follows. Its 53-test/four-browser-test counts describe the retained release, not the combined 61/eight suite.

## Follow one sampled update

Independent editable SGNS objective and gradient inspector: every sampled event, 1,593 coordinate finite differences, real sequential replay versus a frozen simultaneous step, and visible clamp/order effects. Twelve original pairs capture 72 actual calls; seven labeled controls expose repetition, conflicting labels, saturation and overshoot. Full 300-sentence corpus and all 32 trained vectors retained; browser recomputes all 992 cosine neighbors. 53 Python tests and four Node/actual-Chrome tests compare 19 complete reports. Original 40 tests, trainer and gates remain unchanged.

The frozen objective is a sum of stable softplus terms. Repeated output rows accumulate gradients; input and output roles are separate tables even if their word names match. Every analytic gradient coordinate is compared with a central difference, and every sequential event exposes pre/post vectors, raw/clipped logits, true logistic factor and original update factor.

The unchanged trainer applies the positive event and each negative in order, with a ±15 logit clamp. A simultaneous step on the frozen summed gradient is a different policy. Both final losses are evaluated on the same fixed event list. The constructed overshoot control increases simultaneous loss from 16.0007 to 47.9464 at lr=2. Neither update is claimed to guarantee descent.

## Inspect the full trained model

All original source, corpus generator, 300 sentences, 32-word vocabulary, 512 trained input-vector coordinates and 24 topic-evaluation words remain. At dimension 16, 30 epochs and seed 7, original coherence is 1.0000 and separation margin 0.6033. The browser computes all 31 neighbors of any of the 32 words. Full corpus, vectors and fixture inputs can be downloaded; no synthetic two-dimensional picture replaces the model.

The original sampler uses unigram^0.75 base weights with positive-context and already-drawn exclusions, a vocabulary-size cap and a first-eligible fallback after twenty rejected draws. Its actual sequential draw law is not IID base-weight sampling. Repeated negatives and contradictory labels are constructed editor controls, not sampler outputs.

## Reproduce the sampled-step checks

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
