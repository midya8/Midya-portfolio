# AttnLens

Actual blockwise online-softmax inference on trained checkpoints: inspect running maximum, normalizer, weighted values and the full residual stack against dense causal controls. Original from-scratch training and all-head interventions remain intact. Bounded score-buffer counts are not total memory or speed claims.

[Live intervention workbench](https://midya8.github.io/attnlens/) · [Source](https://github.com/midya8/attnlens) · [Exact intervention contract](https://github.com/midya8/attnlens/blob/main/INTERVENTIONS.md)

## Problem

A sharp attention map does not tell you how much the model's prediction depends on that head. AttnLens starts with a real, dependency-free two-layer trainer with manually derived gradients, then adds fixed-weight output interventions and an independent JavaScript computation of the same model. It also repairs a real numerical bug: a probability-clipped loss disagreed with its nonzero gradient on extreme targets.

## Implementation

- Token embeddings and sinusoidal positions feed two residual, two-head causal attention blocks and an output head. No autograd, pretrained model, MLP, normalization, dropout or API.
- Complete trained and same-seed initialization checkpoints are exported. The browser computes full inference from those weights, not prerecorded intermediate answers.
- Each intervention zeroes a selected head's result slice before the shared output projection, at every sequence position. Later layers recompute all Q/K/V, attention and residuals. The original same-layer attention pattern is still visible even when its result is muted.
- All 16 subsets of four heads are exposed, including unchanged and all-heads-off residual controls. The full 128-example original held-out split is evaluated for every subset and checkpoint, not a selected set of favorable heads.
- Eleven declared inputs include eight fixed-seed samples and three edge structures. The UI accepts valid edited sequences. All ten recalled-key changes, including the original as a no-op, and one change at each filler position test input sensitivity at fixed weights.
- The inspector shows full baseline/intervention logits, probabilities, every Q/K/V and attention row, head result slices, output projection, residuals and all source weights. Full model and audit JSON downloads are independently reproducible through a native CLI.

## Measured results and limits

The fixed seed-7 checkpoint (dim 8, 2 heads, 2 layers, 100 epochs × 64 samples, SGD 0.1) gets 128/128 original held-out examples correct at mean loss 0.000482558 nats. Muting all heads leaves embeddings, positions and the output head: 19/128 correct, loss 2.900797842. Every intermediate subset result is retained, including non-monotone effects.

These are descriptive results for one checkpoint, synthetic task and exact zero-vector replacement. Attention maps are not automatically explanations. Zero ablation can produce out-of-distribution activations and head effects need not add. Neither a one-layer performance gap, a classic induction circuit, seed robustness, production language modeling nor a training improvement is established.

## Numerical contract repair

The old loss used `-log(max(p_target, 1e-12))` while gradients remained `softmax - one_hot`. When the floor was active, reported loss was constant but the gradient nonzero. Stable log-sum-exp now gives the actual loss, including 2000 nats for logits `[1000, -1000]` with target 1, and agrees with extreme-logit finite differences. Original forward weights, optimizer, data, trainer configuration, 46 tests and demo/gates remain unchanged. Exported training traces are regenerated, not silently reused.

## Verification

- 59 Python tests pass on Python 3.10-3.13, retaining all 46 original tests. Added tests check no-op full forward equivalence, exact muted slices, all-off residual identity, downstream recomputation, causality, nonmutation, model validation, exhaustive subsets, matched edits, CLI exports and extreme numerical gradients.
- Complete weights, 100 training losses, original held-out examples, 32 aggregate subset results and fixture pins regenerate at normalized tolerance 1e-12 on all four Python versions without rewriting source data.
- Three Node/actual-Chrome tests compare 352 complete tensor reports, 22 full audits and 4096 held-out predictions. Node makes 590,268 native numeric comparisons. Chrome checks every displayed tensor and weight cell over 704 layer/head/row views, two full downloads, keyboard controls, stale-result clearing and 320/390/1280 layouts.
- A clean installed-wheel check outside the source tree confirms five installed module origins, checkpoint roundtrips, every fixture's exact original-forward equivalence, all subsets, audit CLI and both original CLI modes. Current public source is reproduced exactly.

Native/browser comparisons use normalized tolerance 1e-10. No cross-runtime bitwise, measured speed, GPU or memory claim.

## Prior work

Architecture, head interventions and induction-head ideas are prior work, not a new method. Six primary/official sources, including both sides of the attention-explanation debate, are linked in the [methods and attribution](https://github.com/midya8/attnlens/blob/main/INTERVENTIONS.md). This project is an educational implementation with a numerical repair, independent inference and a tested inspection surface.

### 0.3: actual blockwise online-softmax inference

[Online inference workbench](https://midya8.github.io/attnlens/online.html) · [Numerical and storage contract](https://github.com/midya8/attnlens/blob/main/ONLINE.md) · [Implementation PR #4](https://github.com/midya8/attnlens/pull/4)

An opt-in inference backend consumes causal key blocks on the actual trained and initialized checkpoints, carrying a running maximum, normalizer and weighted-value numerator into the real head projections and residual stack. Independent JavaScript computes full Q/K/V, every accumulator transition and all vocabulary logits against a separately computed dense causal control. Block size and forward/reverse order are editable; downloaded inputs and full audits replay through the installed native CLI.

The core observes one live score-list buffer, bounded by the selected block size, without constructing full score/probability matrices. This is a structural count, not process memory, bytes, speed or GPU IO. Q/K/V, head outputs and residual arrays remain. The debug trace, dense control and browser deliberately add quadratic audit storage; arithmetic work is still quadratic. Standard online normalization and blocked attention are prior work, not a new method, FlashAttention kernel, KV cache, linear attention or training backend.

76 Python tests retain the original 59 byte-for-byte. Independent 80-digit Decimal controls cover 648 exhaustive signed-value/ternary-score cases and 80 seeded Q/K/V sets; all 24 block sizes and both orders are checked on all 22 original checkpoint/fixture pairs, totaling 1,056 actual original-forward comparisons. Every structural buffer/work count, causal prefix and accumulator transition is checked, with overflow/underflow, equal-score means, invalid inputs and output preservation controls.

Six Node/actual-Chrome tests retain all four originals. The new native/JavaScript comparison covers 106 full-model and 80 standalone reports, 5,585 query rows, 11,254 accumulator states and 775,344 numeric fields. Actual Chrome checks 66 full native reports, every displayed tensor and state over 2,112 head/query views, 198 layouts and two real downloaded files replayed natively. Full public source, installed-wheel API/both new CLI paths, original training/intervention reproduction and deployed behavior are checked separately; screenshot comparisons do not substitute for numerical controls.

Binary64 block/order changes can alter rounding or near-tied predictions. The unchanged legacy engine uses a finite `-1e30` future sentinel, which can differ from exact causal skipping for extreme bounded custom weights. That counterexample is tested, and legacy error/prediction is reported separately rather than quietly rewriting old semantics. The original native modules, tests, checkpoint, intervention JavaScript/app/CSS and training remain unchanged; the original page only gains a link.
