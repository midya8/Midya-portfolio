# CalibrLab

Fit a temperature on validation logits, then inspect the result on a separate test split. The Python CLI and library report accuracy, ECE, MCE, Brier score, logit-space NLL, reliability bins and optional paired bootstrap intervals. Python uses only the standard library.

[Source and commands](https://github.com/midya8/calibrlab) | [Live score ledger](https://midya8.github.io/calibrlab/) | [Equations and input limits](https://github.com/midya8/calibrlab/blob/main/LEDGER.md)

## Two outcomes, not a promise of improvement

The included synthetic fixture trains a one-hidden-layer MLP on six Gaussian classes in 16 dimensions. It uses 20 training samples per class and reaches training accuracy 1.0000, with test accuracy 0.5563. That deliberately small training set produces an overconfident model.

A temperature selected by validation NLL improves the fixture's test scores:

| Measure | Before | After |
| --- | ---: | ---: |
| ECE | 0.2765 | 0.0651 |
| MCE | 0.3487 | 0.1216 |
| Brier | 0.7149 | 0.5964 |
| NLL | 2.0030 | 1.2060 |

The selected temperature is 3.85. The best temperature on the test grid is 3.30, with NLL 1.1984. That test-grid row is a reference, never a fit target. Subtracting the displayed rounded NLLs gives 0.0076; the unchanged full-precision gap is 0.007543134492483228, which rounds to 0.0075.

The caller example in `examples/logits.json` goes the other way: validation selects the upper grid boundary, T=10, and test NLL worsens from 0.0878 to 0.5762. Both examples are development controls. Neither establishes improvement on new data.

Positive scaling preserves argmax in real arithmetic. The fixture gates check exact accuracy invariance; binary64 rounding and underflow limits are described separately. One scalar cannot fix every confidence pattern, and it does not improve classification accuracy.

## Use separate validation and test logits

```sh
python -m calibrlab calibrate --input examples/logits.json
python -m calibrlab calibrate --input examples/logits.json --bootstrap 1000 --seed 13
```

Each split supplies logits and integer class labels, with a shared class order. Test labels never select T. Schema validation cannot detect leaked examples or a mismatched semantic class order, so split independence remains the caller's responsibility. Invalid input exits 2 without a JSON report.

Fitting and pipeline reports use stable log-sum-exp from logits, without a probability floor. A wrong-class margin of 1000 has NLL 1000, rather than a clipped loss near 27.6. Unrepresentable losses fail explicitly. The low-level probability-only NLL helper retains its documented floor and is not the fitting objective.

## What the bootstrap means

Optional nominal 95% percentile intervals resample identical test indices before and after scaling. They include paired after-minus-before deltas for accuracy, ECE, MCE, Brier and NLL. The validation-fitted T stays fixed.

These are conditional IID test-row intervals, not guaranteed coverage or uncertainty from fitting T or training the model. Tiny samples and binned ECE/MCE can give misleading or degenerate intervals. Correlated or grouped rows need a different resampling design. A negative loss delta describes this comparison, not a mechanism or a deployment guarantee.

## Inspect scores and bins

The live ledger and native score-audit command expose row logit NLL, per-class Brier terms, signed bin gaps, ECE contributions, bin migration and every fixed-temperature row deletion. Choose 2..20 bins or T in 0.1..20. The validation fit keeps the original 191-point NLL grid. A separate 19-point path displays validation/test NLL without recommending a test-selected temperature.

Five public synthetic controls include the original 240 validation / 480 test logits and report, the adverse caller example, uniform ties, within-bin cancellation and singleton underflow. The small arithmetic controls are shared-value examples, not independent evaluation samples. Inputs stay in the page; copy/download contains the full input and report.

ECE/MCE depend on binning, finite counts and top-class probabilities. NLL and Brier are proper losses, not calibration-only measures. Fixed-temperature deletion is not a validation refit, causal effect or uncertainty interval. These are standard formulas, not a new calibration method.

## Reproduce the checks

```sh
python -m unittest discover -s tests -v
node --test tests/*.cjs
bash examples/verify_wheel.sh
```

The 56 Python tests retain the earlier 45 metric, gradient, fixture and caller tests, then add score-ledger checks. Four Node/Chrome tests check independent native/browser arithmetic and actual UI behavior. The ledger evidence includes 95 full witnesses, 9,367 row/deletion records, 55,328 class Brier terms, 160 independent 70-digit Decimal games and 80 integer/uniform controls. UI checks visit all 493 positions and 50 bins.

An installed-wheel check rebuilds the original full training/logits/report and all 95 witnesses outside the checkout, imports seven modules and runs all five commands. CI runs Python 3.10-3.13 plus the demo, browser and package checks. These are regression and arithmetic checks, not evidence of calibration quality in a particular deployment.
