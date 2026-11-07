# QuantLab

Post-training int8 quantization built from scratch in pure Python, with measured accuracy and size trade-offs.

## Problem

Every edge-deployment story ends at "then we quantize to int8", but the trade-off is usually asserted from vendor benchmarks rather than measured. QuantLab builds symmetric int8 quantization itself - per-tensor and per-channel - and measures the two things that matter: what the smaller storage costs in task accuracy on a model trained inside the repo, and where the reconstruction error actually concentrates.

## Approach

- **Real quantization, no libraries** - symmetric int8 (scale = absmax/127, zero maps to zero), per-tensor or per-channel scales, dequantization, and byte-exact size accounting: params x 4 vs params + 4 per scale.
- **A trained fixture model** - a perceptron-trained linear classifier over hashed features on a deterministic synthetic dataset (one seed reproduces the run bit for bit), small enough that the int8 accuracy cost is measured exactly on held-out data.
- **Error located, not just averaged** - a controlled study boosts one matrix row x100 and shows per-tensor's single scale crushing every other row (small-row SNR 9.25 dB) while per-channel holds 48.39 dB: a measured 39.14 dB gain, the case per-channel exists for.
- **Gates, both sides** - `--max-accuracy-drop`, `--min-ratio` and `--min-snr-gain` fail CI when trade-offs regress; the demo proves an impossible gate fails.

## Verification

- 28 unit tests cover quantization range and round-trip error, zero handling, scale counts, size accounting, dataset and training determinism, fixture accuracy parity between fp32 and int8, both sides of the magnitude study, and every CLI gate.
- Fixture results: fp32 test accuracy 0.9833, per-channel int8 0.9833 (measured drop 0.0000), storage 768 B to 204 B (3.765x); magnitude study: +39.14 dB small-row SNR for per-channel.
- `bash examples/demo.sh` runs fully offline: both commands with their gates plus a negative control.
- CI runs the same suite across Python 3.10-3.13.

Bounds worth stating: int8 storage is simulated with Python ints proven in range, and size accounting is byte arithmetic rather than a serialized format. Post-training quantization only - no quantization-aware training, int4, or activation quantization. The fixture model is tiny so the measurement is exact; real models show non-zero drops and nothing here claims otherwise.

## Links

- Repository: [midya8/quantlab](https://github.com/midya8/quantlab)
