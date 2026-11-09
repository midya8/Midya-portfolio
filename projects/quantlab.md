# QuantLab

Weight-only int8 quantization from scratch, with real packed files and an independent editable browser inspector.

## Problem

An analytic byte count is not a file, and a small coefficient error does not guarantee an unchanged decision. QuantLab follows the complete path: source weight, integer code, stored IEEE scale, reconstructed weight, signed logit-error contribution and fixed-input decision margin.

## Implementation

- QLB1 is a bounded educational binary format: 24-byte versioned little-endian header, IEEE binary32/64 scales, row-major signed int8 codes and CRC32. Independent Python and JavaScript parsers reject malformed lengths, counts, dimensions, reserved codes, nonfinite scales and corrupt checksums. CRC32 detects accidental corruption, not authenticity.
- The browser independently quantizes and dequantizes editable matrices, exposes every coefficient and logit, imports real QLB1 files and exports the binary, input, full report and complete original fixture archive. Invalid edited input clears results and disables exports until valid input is applied.
- Python Fraction and browser BigInt dyadics independently compute exact logits for the represented-real maps and pairwise sufficient margin bounds, including the first-index tie rule. Full rational witnesses are available. Runtime binary64 predictions are reported separately.
- The original quantizer, model, analysis, all 27 original tests, 120 training examples, 60 test examples, eight-row magnitude study and CLI gates remain unchanged. Constructed prediction-flip and tie-collapse examples are labeled controls, not trained-model results.

## Measured results

The original source model and all four storage choices retain 59/60 accuracy on the checked-in synthetic test fixture. No test examples are filtered out. The original magnitude study still reports small-row SNR 9.25 dB with one tensor scale versus 48.39 dB with row scales, a 39.14 dB difference.

| Original 192 weights | Actual QLB1 file | Compared with 768 conceptual raw fp32 bytes |
|---|---:|---:|
| Row scales, binary32 | 232 B | 3.3103x |
| Row scales, binary64 | 244 B | 3.1475x |
| Tensor scale, binary32 | 224 B | 3.4286x |
| Tensor scale, binary64 | 228 B | 3.3684x |

The earlier 204 B row-scale figure is analytic payload accounting, not a serialized file. The original Python weights and inference are binary64; fp32 is only a conceptual byte comparator.

## Verification

- 39 Python tests on 3.10-3.13, including the 27 unchanged original tests. The earlier documentation's count of 28 was incorrect.
- Four Node/actual-Chrome tests compare 52 full independent reports, 59,004 numeric values, every packed byte and every exact rational string. They cover all 60 test selectors, every fixture/mode/precision combination, malformed input, binary import/export, keyboard operation and 320/390/1280-pixel layouts.
- Isolated installed-wheel reproduction outside the checkout imports seven modules, retrains the complete original fixture, verifies all 52 reports and runs six CLI commands. The original offline demo and both sides of its gates remain.
- Public source is checked against the tested files; main CI and Pages deployment are checked independently.

## Scope

Exact bounds apply to fixed represented-real linear maps, not floating-point accumulation, uncertain inputs, unseen accuracy or deployment. The synthetic classifier uses hashed count features and perceptron updates, not an LLM. The browser performs dequantized scalar inference, not integer matmul. No speedup, RAM reduction, complete checkpoint, authentication or ONNX/GGUF compatibility is claimed. Symmetric absmax quantization, ties-to-even rounding and triangle-inequality error bounds are standard methods, with sources and the full byte contract in FORMAT.md.

## Links

- Repository: [midya8/quantlab](https://github.com/midya8/quantlab)
- Reviewed implementation: [PR #2](https://github.com/midya8/quantlab/pull/2)
- Live inspector: [QuantLab](https://midya8.github.io/quantlab/)
