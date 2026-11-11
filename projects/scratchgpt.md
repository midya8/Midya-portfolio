# ScratchGPT

A small NumPy GPT with three inspectable execution paths: exact training continuation, block recomputation during backward and cached inference that rebuilds when the learned-position window moves.

[Cache workbench](https://midya8.github.io/scratchgpt/cache.html) · [Source](https://github.com/midya8/scratchgpt) · [Continuation replay](https://midya8.github.io/scratchgpt/) · [Rematerialization](https://midya8.github.io/scratchgpt/remat.html)

## What changed

The original repository includes a reverse-mode autograd engine, pre-LN causal transformer and a 419,328-parameter character model trained on TinyShakespeare. The later work keeps that checkpoint, loss log, sample, default GPT forward, trainer and sampler intact. Each execution change is tested against the original code rather than treated as correct because its output looks plausible.

### A restart must preserve the next update

A training checkpoint now saves named float32 parameters, Adam m/v buffers and clock, both PCG64 train/evaluation states, text identity, vocabulary, dimensions, numerical options, scheduled history and runtime metadata. The bounded no-pickle loader rejects inconsistent, malformed or incompatible state before returning a training object. Atomic save replacement preserves the previous checkpoint when serialization or replacement fails; it is not a guarantee against every power or filesystem failure.

A separate 1,056-parameter synthetic run retains all 12 updates and all 13 stop boundaries. Complete continuation reaches the same final state at every boundary in the same environment. Resetting train/evaluation RNG or dropping Adam moments changes weights at all 11 interior boundaries. Resetting only evaluation RNG changes future validation history, not training weights. Stops at zero and 12 remain controls.

The browser independently recomputes Adam arithmetic and transformer forwards from the recorded weights. It does not train on that page. The reference checks cover 38,016 optimizer values and 2,592 logits. A separate-process installed CLI checks uninterrupted versus 4+8 updates.

[Continuation contract](https://github.com/midya8/scratchgpt/blob/master/CONTINUATION.md)

### Activation rematerialization: rebuild the derivative

The optional rematerialization path groups original transformer blocks, keeps their boundaries and discards the forward interior graph. Backward rebuilds those blocks with the actual upstream vector-Jacobian product (VJP), then adds input and parameter contributions to the outer graph. It does not replace the original `Tensor.backward` or turn itself on in the trainer.

A separate float64 scalar-autograd browser model computes the complete tiny GPT and both backward paths. Tokens, targets, grouping, one-step SGD rate and every named weight are editable. Eighteen complete native controls cover 15,184 parameter positions. Every one of the shipped checkpoint's 419,328 parameter gradients is checked for both block groupings without retraining it.

The diagnostics count reachable logical Tensor.data elements or browser scalar nodes. These are different granularities, neither peak memory nor speed. Only deterministic dropout-zero, first-order derivatives with unchanged inputs and weights are supported. The audit also checks fanout, existing gradient contributions, mutation rejection and actual disposal of discarded interiors.

[Rematerialization contract](https://github.com/midya8/scratchgpt/blob/master/REMATERIALIZATION.md)

### Reuse KV states only while their context stays valid

The inference path takes a copied, read-only float32 weight snapshot. Prefill computes the causal context; append projects only new token rows and uses a right-aligned mask for multi-token chunks. A low-level append refuses overflow. Rolling advance rebuilds every layer of the entire final window whenever cropping shifts learned absolute positions. Dropping old KV slots alone is included as a deliberately wrong control, not attributed to another library.

The independent float64 browser model exposes all context tokens, rebased positions, masks, logits and paged K/V coordinates. Complete editable inputs and reports download as JSON; the input runs in the native CLI against the original GPT. Edits clear stale results. A native-witness label appears only for an exact complete-input match.

Eight full controls contain 43 chunk steps, 685 cached logits and 3,256 K/V coordinates. Chrome checks every displayed coordinate and mask, 24 control/viewport combinations, trusted input changes, valid and invalid imports, two real downloads and native replay of the downloaded input. The controls are tiny synthetic models, some after three original Adam updates, not the Shakespeare checkpoint.

The archived timing run uses the unchanged original checkpoint, 48 teacher-forced steps, two warmups and seven retained timed repeats. Only NumPy full versus NumPy cached isolates caching from removing autograd graph construction. Full/cached median factors are 8.287x, 10.722x, 1.407x and 0.994x for prompt lengths 4, 16, 48 and 64. At full context, caching rebuilds every step and loses slightly: 253.230 ms cached versus 251.783 ms full. The CPU model was not recorded. These are local timings, not a decoding-throughput or hardware comparison.

[Cache contract and complete timing record](https://github.com/midya8/scratchgpt/blob/master/CACHE.md) · [Implementation PR #5](https://github.com/midya8/scratchgpt/pull/5)

## Current checks

- 158 Python tests on 3.10-3.13 and 13 Node/Chrome tests retain all prior tests. No old numerical tolerance or test was weakened.
- Fresh public source is compared byte-for-byte with the reviewed files. Native controls regenerate from their complete inputs.
- Installed wheels run outside the checkout. Checks cover original continuation/sample routes, all rematerialization controls and full trained-checkpoint gradients, both cache-audit CLI routes, the benchmark CLI and 80 original-checkpoint inference steps through 16 window rebuilds.
- CI tests the four Python versions, browser behavior and installed reproduction. Pages deployment and current live behavior are verified separately from a successful source merge.

## Limits

Exact continuation is limited to the same validated numerical environment; matching metadata is necessary, not proof that every runtime detail agrees. Float32 native and float64 browser results use tolerances, not universal bitwise promises. Cache matrix-vector/matrix-matrix shapes can round differently. The new shipped-checkpoint cache test uses a `1e-5` absolute logit bound and `3e-6` softmax total-variation bound. Close distributions can still produce different sampled tokens near an RNG threshold. The original sampler is unchanged.

KV bytes are resident native ndarray payload, excluding weights, token history, temporaries, allocator/Python/BLAS storage and audit references. They are not peak memory or RSS. Matrix-row and score-cell counters describe executed shapes, not FLOPs or wall time. Snapshot weights do not track later training.

No new model training, generalization gain, attention algorithm, GPU kernel, optimal checkpoint schedule or production inference server is claimed. Transformers, Adam, activation checkpointing and KV caching are established techniques, with source notes in each contract. The original checkpoint's SHA-256 remains `3de6a1626e4489a2e0bc867fc58fe66d323ac6c527bb3af7be662b49510a817e`.
