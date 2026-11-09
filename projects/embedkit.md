# EmbedKit: inside the sampled step

Train word embeddings from scratch with dependency-free Python SGNS, then inspect what one sampled step actually does in an independently implemented browser.

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
