# AttnLens

Causal multi-head self-attention trained from scratch in pure Python, with gradient verification and attention-pattern analysis.

## Problem

Attention weights get quoted constantly as if they were explanations, but few projects train attention themselves or check what a head actually learned. The cleanest measurable case is recall: "the token that followed this marker earlier". One layer cannot solve it cleanly - the key token's own content does not say it followed a marker - but two layers can, which makes success and failure both visible in the weights. This is the shape of what larger-model literature calls an induction head; here the evidence is direct measurement on a small task, not circuit-level analysis of a large model.

## Approach

- **The mechanism, no dependencies** - token embeddings plus fixed sinusoidal positions, two residual blocks of causal multi-head self-attention (Q/K/V projections, scaled dot-product scores, masked softmax), an output projection and cross-entropy loss at the final position.
- **Hand-derived backpropagation** - gradients for embeddings, per-head Q/K/V, both output projections and the residual chain are derived manually; the test suite checks every parameter group against finite differences (to ~1e-11) on the suite's fixture model (two layers, dim 4, two heads).
- **A task with structure to find** - each sequence hides one key after a marker at a varying position and asks for it at the end. One seeded RNG drives initialization and the fresh training samples generated each epoch, so a config and seed reproduce the run bit for bit.
- **Analysis, not vibes** - per-head mean entropy, previous-token mass, and recall attention (the query position's weight on the key token), with text heatmaps and terminal/JSON/Markdown reports. `--max-final-loss`, `--min-accuracy` and `--min-recall-attention` turn training quality into CI gates. Optimization uses global-norm gradient clipping: without it, training was observed to diverge in the tested configurations.

## Verification

- 46 unit tests cover softmax stability, positional encodings, causal masking, attention row normalization, residual structure, finite-difference gradient checks for every parameter group on the fixture model, SGD loss decrease, gradient clipping behavior, dataset structure and determinism, head statistics, report formats, the CLI including both gate sides, and pinned trained quality (>= 95% accuracy, >= 0.7 recall attention at 100 seeded epochs on the checked-in configuration).
- `bash examples/demo.sh` runs fully offline: trains, verifies that the top head's query row concentrates on the key token (0.80-0.91 weight on the checked-in seed), asserts report contents, and confirms an impossible gate fails.
- CI runs the same suite across Python 3.10-3.13.

Bounds worth stating: a two-layer model on a synthetic recall task demonstrates the mechanism, manual backpropagation and pattern analysis - not language modeling at scale. The task is designed so one layer struggles and two suffice; that gap is the demonstration. The measured recall attention shows what these heads learned on this task and configuration; it is an observation consistent with induction-head behavior, not proof of the same circuit, and not an explanation method for larger models.

## Links

- Repository: [midya8/attnlens](https://github.com/midya8/attnlens)
