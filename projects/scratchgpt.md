# ScratchGPT

A GPT built and trained from scratch in pure NumPy.

## Problem

Frameworks make it possible to train a transformer without understanding the code underneath. ScratchGPT keeps every core mechanism visible: tensors track operations, gradients move through hand-written backward rules, attention enforces causality, and the training loop updates a real model checkpoint.

## Approach

ScratchGPT implements a small reverse-mode autograd engine in about 400 lines of NumPy, then builds a pre-LN character-level GPT on top of it. The repository includes:

- broadcasting-aware backward rules for arithmetic, matrix multiplication, reductions, softmax, log-softmax, gather, layer norm and fused cross-entropy
- linear, embedding, layer-norm, causal multi-head self-attention, GELU MLP and residual block layers
- GPT-2 details such as learned positional embeddings, residual-path output scaling and no biases
- Adam with bias correction, learning-rate warmup, gradient-norm clipping, periodic evaluation and resumable checkpoints
- training and sampling CLIs for TinyShakespeare, including temperature and top-k sampling

The shipped configuration is deliberately small and reproducible on one CPU: 419,328 parameters, 2 layers, 4 heads, d_model 128, context length 64 and a 65-character vocabulary. The documented 3,000-step run reaches 1.83 nats/char validation loss in about 4.5 minutes on one CPU core.

## Verification

- 11 unit tests check every autograd operation against central finite differences, cover model forward and backward passes, require a short training run to reduce loss, and prove that position t cannot attend to position t+1.
- A fresh public clone at merge commit `031eeb1216c942b43c76b49eab68d6e6892f0a2b` passes editable install and the full test suite.
- GitHub Actions runs the same editable install and tests on Python 3.12; the packaging fix is green on the pull request and merged master run.
- The repository ships TinyShakespeare data, loss records, a trained checkpoint and sampled text so the results can be inspected and reproduced.

The model is intentionally tiny and the README does not oversell its prose quality. The value is that the autograd engine, attention block, optimizer and training loop are inspectable end to end with only NumPy.

## Links

- Repository: [midya8/scratchgpt](https://github.com/midya8/scratchgpt)
