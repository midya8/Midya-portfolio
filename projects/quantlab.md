# QuantLab: packed weights and integer-product audits

Two independent browser inspectors follow quantized weights through packed
files and fixed-input decision bounds, then add activation integer products
and partial sums. Exact rational reports expose weight and activation error
separately. The integer inspector ends with floating-point rescale, not
integer-only inference or a hardware benchmark.

## Activation integer dot products

The current suite has 47 Python tests, including all 39 earlier tests, and
seven Node/actual-Chrome tests. Independent floor/remainder rounding checks 240 seeded reports and all 519 signed half-unit controls. Python Fraction and independent browser BigInt dyadics agree on 72 complete reports with 6,848 products and all exact error strings. Actual NumPy 2.2.6 int32 matmul and cumsum check every accumulator and prefix. Seven Node/actual-Chrome tests cover 168 row selections, 20 responsive views, two trusted downloads replayed natively and stale-result rejection. A fresh isolated eight-module package reproduces original training, all 52 old reports and all 72 new reports, with both new CLI entrypoints. Original QLB1 bytes and 59/60 weight-only synthetic results remain unchanged.

The feature-stage publication checked all 53 merged files and ten deployed
assets against the tested source, with separate hosted CI and Pages gates.
Its deployed browser workflow and 20 local/deployed captures were checked
separately from the native tests. These checks are regression evidence, not
a deployment guarantee.

Integer products and prefixes are exact under the checked shape bound of 2,064,512. Final output rescaling uses binary64, not integer-only end-to-end inference. Fixed activation range is supplied, not calibrated. Exact fractions describe represented-real maps, not runtime summation or unseen accuracy. Error decomposition is order-dependent arithmetic, not causal attribution. No hardware speed, RAM, learned improvement, new algorithm or ONNX/TFLite compatibility claim. Established quantization literature is credited.

The default control uses `W=[[127,0],[0,127]]`, `x=[0.4,0.49]`, and activation range 127. Stored weight scales and activation scale are exactly 1. Original exact-real scores are 127 times the represented input values, with row 1 strictly larger. Quantized activations are `[0,0]`, so every product and accumulator is 0 and row 0 wins the tie. Weight error is exactly 0; activation error accounts for the whole score change. This is a constructed arithmetic control, not trained performance.

For each row, `a = W x`, `b = W_hat x` and `c = W_hat x_hat = s_w s_x sum(q_w q_x)`. Coordinate terms `(W_hat - W) x` sum to `b - a`; `W_hat (x_hat - x)` sum to `c - b`. Full rational strings and every contribution are exported. The source, weight-only and full exact-real winners remain separate from the binary64 runtime-rescale winner, with first-index tie handling. No sufficient floating-runtime certificate is claimed.

The supplied range produces `s_x = range / 127`, divided in binary64 and rounded to selected IEEE32/64 storage. Activation codes use exact represented-real `x / s_x` with nearest-even rounding and saturation to `[-127,127]`. Old weight codes retain their original binary64 quotient semantics and unchanged QLB1 file. The explicit endpoint flag tests `|x| > 127 * stored_scale`, not whether the rounded code is 127. Scale metadata can move the endpoint slightly. No calibration or test-set range optimization is performed.

Every accepted input has 2..8 rows and 1..128 features, finite nonboolean magnitudes at most 1,000,000 and a positive range. Unrepresentable positive scales fail explicitly. Since each product has magnitude at most 16,129, every prefix is at most `n * 16,129 <= 2,064,512`, well within signed int32. Native Python uses unbounded integers; browser Numbers are exact over these bounded integers. The additional actual NumPy int32 check is arithmetic evidence, not a kernel-speed benchmark.

The independent editable page has complete activation/product/prefix/error tables, exact report export and input export. Edits invalidate all prior output and disable downloads; duplicate keys and nonfinite input are rejected. Nine controls retain clipping, signed half-way ties, zeros, maximum shape, scale precision and three original trained examples. Neither original data nor candidates are filtered.

[Live activation audit](https://midya8.github.io/quantlab/integer.html) · [Source PR3](https://github.com/midya8/quantlab/pull/3) · [Method and seven-source ledger](https://github.com/midya8/quantlab/blob/main/INTEGER.md)

The earlier weight-only evidence follows. Its 39-test/four-browser-test counts describe the retained release, not the combined suite.

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

Exact bounds apply to fixed represented-real linear maps, not floating-point accumulation, uncertain inputs, unseen accuracy or deployment. The synthetic classifier uses hashed count features and perceptron updates, not an LLM. The weight-only browser performs dequantized scalar inference, not integer
matmul; the separate activation inspector above exposes bounded integer
products and floating-point rescale. No speedup, RAM reduction, complete checkpoint, authentication or ONNX/GGUF compatibility is claimed. Symmetric absmax quantization, ties-to-even rounding and triangle-inequality error bounds are standard methods, with sources and the full byte contract in FORMAT.md.

## Links

- Repository: [midya8/quantlab](https://github.com/midya8/quantlab)
- Reviewed implementation: [PR #2](https://github.com/midya8/quantlab/pull/2)
- Live inspector: [QuantLab](https://midya8.github.io/quantlab/)
