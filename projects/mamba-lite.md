# mamba-lite

A Mamba-style selective SSM built on a hand-written NumPy reverse-mode autograd engine, trained twice on the same task with selectivity on and off.

[Source](https://github.com/midya8/mamba-lite)

## Problem

Modern state-space models credit their performance to input-dependent dynamics, but most public code ships the claim with the model. This repo isolates it: the smallest training task that only selective dynamics can solve, and the same architecture with the selection mechanism removed. Selective copy is that task. Eight random tokens appear early in the sequence, a separator follows, then up to twelve filler tokens and an EMIT token. The model echoes the first block after EMIT. Nothing in the filler says what to copy, so the answer lives entirely in the recurrent state, and the model has to decide when to stop holding and start emitting.

## Implementation

- A reverse-mode autograd engine written from scratch: add, mul, matmul, exp, log, sigmoid, softplus, silu, sum, reshape, gather, slice, stack, a fused cross-entropy, and a causal depthwise conv. Each op carries a finite-difference check in the tests.
- The block follows the Mamba recipe: RMSNorm pre-norm, input projection, causal conv, SiLU gate, the scan `h_t = exp(dt_t * A) * h_{t-1} + dt_t * B_t * x_t` unrolled over time in float64, output projection, residual.
- The fixed-rate variant removes input dependence by tying dt to a learned bias and fixing B and C per layer, which makes the recurrence an LTI system. Everything else about training is identical.
- A chunked training driver checkpoints every 100 steps so long runs can resume after a timeout.

## Measured results and limits

After 1800 steps each, evaluated on 256 held-out samples: the selective model reaches 0.996 token accuracy and 0.969 full-sequence accuracy. The fixed-rate variant plateaus at 0.427 token accuracy and never completes a sequence. Training takes about fifteen minutes on a laptop CPU.

Limits worth naming: one seed per arm, a two-block d=64 model, a synthetic task with a known answer, and generation that recomputes the prefix at each step. The unrolled scan trades memory for clarity. Nothing here claims anything about larger models, long contexts, or wall-clock speed.

## Files

`src/mambalite/autograd.py` (engine), `src/mambalite/ssm.py` (model), `src/mambalite/data.py` (task), `train.py` and `train_driver.py` (training), `tests/` (gradient checks, a plain-loop reference implementation, generation consistency), `assets/` (checkpoints, learning curve, results JSON).
