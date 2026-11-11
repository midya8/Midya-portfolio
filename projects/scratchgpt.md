# ScratchGPT

A NumPy GPT with exact continuation and actual activation rematerialization: original-block upstream VJPs, full-gradient controls and an independent full-backward browser engine.

[Live optimizer replay](https://midya8.github.io/scratchgpt/) · [Source](https://github.com/midya8/scratchgpt) · [Continuation contract](https://github.com/midya8/scratchgpt/blob/master/CONTINUATION.md)

## Problem

A training checkpoint is not just a bag of weights. The previous trainer saved parameters, Adam moments and the update clock but re-created both random generators on restart. It also did not bind saved state to the text or numerical options. A restart could silently change the next batch and future training trajectory.

## Implementation

The original reverse-mode autograd engine and pre-LN character transformer remain intact: learned token/position embeddings, causal multi-head attention, GELU MLPs, residual paths and a language-model head. The historical 419,328-parameter, two-layer/four-head Shakespeare checkpoint, text, loss records and sample are preserved, not retrained or used for a new speed claim.

The v0.2 continuation checkpoint saves:

- Complete named float32 parameters, Adam m/v buffers, update clock, beta values, epsilon and LR.
- Both full PCG64 train/evaluation states, including cached uint32 information.
- Text SHA-256, character count, sorted vocabulary and split identity; dimensions, seed, batch, base LR, warmup, clipping and evaluation settings.
- Scheduled history, last loss and a runtime fingerprint.

The no-pickle loader checks the complete artifact before returning a new training object. It refuses legacy resume, changed data/options/environment, unknown fields, invalid RNG state, mismatched clocks/history/shapes/dtypes, nonfinite values, negative second moments, duplicate ZIP members and excessive archive size. Atomic continuation saves use a same-directory temporary file, flush/fsync and replacement; serialization/replace failures leave the previous checkpoint intact. Terminal validation uses a cloned RNG and does not alter future scheduled history.

## A complete small-run witness

The offline replay is a **separate 1,056-parameter synthetic model**, not the shipped Shakespeare fit. It retains all 12 updates, every gradient/parameter/moment coordinate, before/after batches and logits, and all 13 stop boundaries. Each fit is continued to update 12.

| Arm | Controlled omission | Result |
| --- | --- | --- |
| Exact continuation | None | 13/13 complete final states identical within the same environment |
| Legacy RNG reset | Train and evaluation RNG state | Final weights differ at all 11 interior boundaries |
| Missing Adam memory | m/v only, clock retained | Final weights differ at all 11 interior boundaries |
| Evaluation RNG reset only | Evaluation generator | Training weights unchanged; future scheduled history changes |

At boundary 4 the maximum final weight difference is about 0.01715618 for RNG reset and 0.02066660 for missing moments. Boundaries 0 and 12 are retained controls. The legacy arm isolates RNG loss rather than reproducing the old extra terminal-history row. This is one small-run counterexample, not a general ranking of state importance.

Scalar JavaScript independently recomputes the Adam equation and full transformer forward pass from the selected update's weights. Editable contexts and before/after states expose all logits/probabilities; scalar gradient/LR/beta/epsilon edits show a one-coordinate hypothetical. Full update and inference JSON downloads retain the evidence. The browser does not calculate gradients or train.

## Verification

- **70 Python tests** on 3.10, 3.11, 3.12 and 3.13, retaining all **11 original tests** and original model/autograd/optimizer/data sources.
- All 13 exact restart boundaries compare full parameters, buffers, both RNGs and history, not just final loss. A separate-process CLI test compares 12 updates with 4+8, including terminal previews.
- Independent scalar Adam checks **38,016** p/m/v values, maximum absolute native/reference error about **5.933e-8**; an independent forward checks **2,592** logits, maximum error about **3.031e-8**. Its objective also supplies central finite differences for three coordinates of every parameter tensor.
- **Three Node/actual-Chrome tests** cover every scalar update, independent forward/loss references, causality and invalid domains. Chrome inspects **101,376 coordinate-table cells**, **468 coordinate views**, **72 before/after inference views**, both exports, invalidation and 320/390/1280 layouts.
- Fresh-public-source tests and replay regeneration, plus an installed wheel outside the checkout: five import origins, all 13 boundaries, separate-process resume and sampling the original Shakespeare checkpoint.
- Six CI jobs: four Python versions, browser and installed-package reproduction. GitHub Pages serves the offline workbench.

Original checkpoint SHA-256: `3de6a1626e4489a2e0bc867fc58fe66d323ac6c527bb3af7be662b49510a817e`.

## Limits and attribution

Exactness is scoped to uninterrupted/resumed runs in the same numerical environment. Python/NumPy build, platform/machine and thread settings are recorded; a matching fingerprint is necessary, not proof that every runtime detail is identical. Cross-version regeneration and browser/native comparisons use tolerances, not universal bitwise promises. Atomic replacement is not a guarantee against every filesystem/power-loss failure. Hashes bind identity, not trust or licensing; the loader does not authenticate arbitrary checkpoint provenance.

Historical Shakespeare loss/timing numbers remain historical. The synthetic replay is not a text-quality benchmark; edited optimizer scalars are not newly trained trajectories. No speed, GPU, generalization or new-algorithm claim is made.

Educational implementation and this continuation/replay by Midya Rahmani. Adam, transformers and RNG checkpointing are prior work. [Source notes](https://github.com/midya8/scratchgpt/blob/master/CONTINUATION.md#sources-and-attribution) cover the Adam/transformer papers, NumPy RNG/NPZ contracts, checkpoint components and Python file-replacement semantics.

### 0.3: real activation rematerialization and full browser backward

[Full-backward workbench](https://midya8.github.io/scratchgpt/remat.html) · [Execution/measurement contract](https://github.com/midya8/scratchgpt/blob/master/REMATERIALIZATION.md) · [Implementation PR #4](https://github.com/midya8/scratchgpt/pull/4)

An opt-in native path executes groups of original NumPy transformer blocks, discards their interior graph and recomputes those blocks during backward. Fresh private leaves take the actual upstream vector-Jacobian product, then add boundary-input and parameter contributions to the outer graph. It does not replace the original Tensor.backward, GPT forward, optimizer, trainer or durable exact-continuation schema. Mutation/replacement guards, fresh-graph single-use semantics, shared outer paths, existing gradient contributions and actual GC-visible disposal of forward interiors are tested. Only deterministic dropout=0 and first-order derivatives are supported; tied parameters inside a region are rejected.

A separate float64 scalar JavaScript autograd engine implements the complete small GPT: token/position embeddings, layer norms, causal multi-head QKV attention, residuals, GELU MLP, logits, CE, reverse differentiation and region recomputation. This new browser page computes actual gradients rather than replaying stored native gradients. The existing continuation page remains its separate optimizer/forward replay. Tokens, targets, grouping, one-step SGD rate and every named weight are editable through a bounded CLI-compatible JSON input. Stale results and downloads clear on edit; actual input/report downloads retain all coordinates.

111 Python tests retain all 70 prior tests byte-for-byte. Thirty seeded shape/batch/head/width/layer controls use nonuniform upstream derivatives; all grouping choices, five-step original Adam trajectories and an independent all-parameter float64 forward/finite-difference oracle check the VJPs. Every one of the historical Shakespeare checkpoint's 419,328 parameter gradients is checked against original eager backward for both block groupings. The checkpoint is not retrained or rebenchmarked.

Eighteen complete native witnesses contain 15,184 parameter positions, including eager controls and weights after three real original Adam steps. Eight Node/actual-Chrome tests retain all three prior tests. Independent native/browser comparisons check 61,888 numeric fields; an all-88-parameter scalar finite-difference control checks browser derivatives. Actual Chrome verifies all reports, 106,288 parameter-table cells, 1,206 coordinate selections, 54 layouts, trusted-input invalidation and two actual downloads with native CLI replay. Installed-wheel reproduction outside the checkout checks both new CLI routes, every native witness and the full trained-checkpoint gradients. Original continuation regeneration and installed continuation/sample checks remain intact.

Observed diagnostics are graph-reachable logical Tensor.data elements or separate browser scalar nodes, not allocator bytes, process RSS, peak memory, complete backward storage or speed. Native parameter/mask nodes, closure arrays, gradients, audit copies and Python/BLAS buffers are excluded; views count per Tensor even if allocations alias. The browser has a different graph granularity, so its counts are not equated with native counts. Bigger regions trade fewer retained boundaries for larger temporary recomputation graphs. The full audit itself stores reference outputs and gradients.

Fresh public source and all 14 deployed assets are byte-checked; 54 local/public and 54 public/deployed screenshot pairs match without masks. Feature, PR and main pass all six CI jobs; Pages and deployed original/new browser suites pass. These checks establish this bounded implementation, not a GPU kernel, optimal schedule, training-speed/process-memory reduction, new method, new trajectory or generalization gain. Standard activation checkpointing/rematerialization, transformers and reverse-mode differentiation are credited in the contract.
