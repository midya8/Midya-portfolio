# CalibrLab: confidence calibration from scratch, measured end to end

A model can be accurate and still be wrong about how sure it is - and for anything downstream of a probability (thresholds, triage, abstention), that matters as much as accuracy. CalibrLab implements the measurement and the simplest principled repair in dependency-free Python: ECE/MCE/Brier/NLL metrics, a per-bin reliability table, and temperature scaling fit on validation data only, all measured on a fixture designed to be overconfident.

## The fixture

Six Gaussian classes in 16 dimensions (noise 0.6) so real uncertainty exists. A one-hidden-layer MLP (hand-derived backprop, finite-difference verified) trains on 20 samples per class - few enough that it memorizes: train accuracy 1.0000, test 0.5563, and its top confidence bin averages 0.9735 confidence at 0.6602 accuracy. ECE before repair: 0.2765.

## The repair, with its exact guarantee

Temperature scaling divides the logits by one scalar T fit by grid search on the VALIDATION split's NLL - the test split never influences T. The method's one guarantee is exact: positive scaling preserves argmax, so accuracy cannot move. The gates assert drift == 0 bit-for-bit.

## Measured results (checked-in fixture, pinned in tests)

```
CalibrLab evaluation (checked-in fixture, 6 classes x dim 16, noise 0.6)

Train accuracy:                 1.0000   (overfit by design)
Test accuracy:                  0.5563

Uncalibrated (T=1) vs temperature-scaled (T fit on validation):
  ECE:    0.2765 -> 0.0651   (reduction +0.2114)
  MCE:    0.3487 -> 0.1216
  Brier:  0.7149 -> 0.5964
  NLL:    2.0030 -> 1.2060
  Accuracy drift from scaling: 0.000000   (exactly 0 by construction)

Fitted temperature (validation):  T = 3.85   (val NLL 1.3118)
Oracle temperature (on test):     T = 3.30   (test NLL 1.1984)
The oracle row is an unattainable reference: fitting on test would leak.

Reliability before:
  confidence    n    mean_conf  accuracy
  --------------------------------------------
  [0.0, 0.1)    0
  [0.1, 0.2)    0
  [0.2, 0.3)    1    0.2675     0.0000  OVER
  [0.3, 0.4)    8    0.3662     0.2500  OVER
  [0.4, 0.5)   28    0.4656     0.3929  OVER
  [0.5, 0.6)   37    0.5471     0.4324  OVER
  [0.6, 0.7)   46    0.6387     0.4130  OVER
  [0.7, 0.8)   34    0.7423     0.4412  OVER
  [0.8, 0.9)   70    0.8487     0.5000  OVER
  [0.9, 1.0)  256    0.9735     0.6602  OVER

Reliability after:
  confidence    n    mean_conf  accuracy
  --------------------------------------------
  [0.0, 0.1)    0
  [0.1, 0.2)    0
  [0.2, 0.3)   26    0.2631     0.1923  OVER
  [0.3, 0.4)  112    0.3486     0.4107  under
  [0.4, 0.5)  130    0.4471     0.5308  under
  [0.5, 0.6)   96    0.5467     0.5833  under
  [0.6, 0.7)   51    0.6431     0.7647  under
  [0.7, 0.8)   47    0.7446     0.7660  under
  [0.8, 0.9)   17    0.8369     0.8824  under
  [0.9, 1.0)    1    0.9073     1.0000  under
```

## What's honest about it

- The oracle row fits T on test and is labeled unattainable: it quantifies what the validation fit leaves on the table (NLL 1.1984 vs 1.2060 - a gap of 0.0076), it is never a fit target.
- After scaling, most bins skew mildly UNDER-confident: one scalar cannot match a per-bin curve. MCE stays at 0.1216 because small bins are noisy. Both are reported in the README, not smoothed over.
- Gates are deterministic regression checks on this fixture's primary artifact (overconfidence before, calibrated after, exact invariance) - not general proofs, and no arm is gated to stay weak.

## Engineering notes

- The MLP's gradients are derived in code and finite-difference verified (max error < 1e-6 in the suite).
- 45 tests separate three concerns: metric unit tests (perfect calibration scores zero, NLL of uniform is log k, argmax invariance under T), gradient verification, and deterministic fixture regression (run twice, same numbers).
- CI runs the suite on Python 3.10-3.13 plus an offline demo asserting both gate sides: the achievable set passes and an impossible ECE reduction (0.9) fails.

Repo: [midya8/calibrlab](https://github.com/midya8/calibrlab)

## Beyond the fixture

`python -m calibrlab calibrate --input examples/logits.json` accepts caller-supplied
validation/test logits and emits a JSON calibration report without training
the synthetic model. Test labels never fit T; tests verify changing them does
not change T. Input errors exit 2 with no report. Split independence and common
class order remain the caller's responsibility.

### Numerical scoring

Temperature fitting and fixture/caller NLL reports use stable log-sum-exp
from logits without clipping. Regression cases cover wrong-class margin 1000,
extreme logits and large-temperature softmax; unrepresentable loss fails
explicitly instead of being silently capped. Published rounded fixture
metrics are unchanged.

## Paired bootstrap intervals

```bash
python -m calibrlab calibrate --input examples/logits.json --bootstrap 1000 --seed 13
```

The Python API accepts the same `bootstrap=1000, seed=13` options. The JSON
`bootstrap` object includes nominal 95% percentile intervals for accuracy,
ECE, MCE, Brier and NLL before/after plus paired after-minus-before deltas.
Each draw resamples identical test indices before and after. T stays fixed
at its original validation fit. The seeded local RNG does not change global
random state. Zero draws (the default) omit the object.

These are conditional IID test-row bootstrap intervals, not guaranteed
coverage or uncertainty from validation fitting/model training. Do not use
them unchanged for correlated/grouped rows. Tiny samples and binned ECE/MCE
can produce misleading or degenerate intervals; the two-row example is only
an interface demonstration. A negative loss/error delta means improvement,
but an interval is not a claim about a mechanism or future deployment.
Draws must be integers from 0 to 10000, with at most 2000000 sampled test rows.
Quantiles use linear interpolation of sorted bootstrap values.

## v0.2: inspect every score and confidence bin

[Live score ledger](https://midya8.github.io/calibrlab/) · [Equations/schema/limits](https://github.com/midya8/calibrlab/blob/main/LEDGER.md)

A native API/CLI and independent browser evaluator expose stable row logit NLL,
class Brier terms, every signed bin gap/ECE contribution, before-to-selected bin
migration and all fixed-temperature row deletions. Choose2..20bins or T0.1..20;
the validation fit remains the original191-point NLL grid, never a test fit.
A19-point descriptive path is separate from the optimizer. Full input/report
JSON can be copied/downloaded; input stays in the page.

Five public synthetic controls retain all240validation/480test logits and the
unchanged original report, the adverse caller example, uniform ties,
within-bin cancellation and singleton underflow. The latter controls are
shared-value arithmetic examples, not independent evaluation samples.

56Python tests (original45exact) and four Node/actual-Chrome tests verify95full
native/browser witnesses,9,367row/deletion records,55,328class Brier terms,
160independent70-digit Decimal games and80integer/uniform controls. Actual UI
checks visit all493positions/50bins. Installed wheel reproduction rebuilds
original full training/logits/report and all95witnesses outside checkout,
imports7modules and runs5commands.

Standard temperature scaling/proper losses, not a new calibration theorem.
ECE/MCE depend on bins, finite counts and only top-class probabilities; lower
NLL/Brier does not isolate calibration. Fixed-temperature deletion is not a
validation refit, causal effect or uncertainty interval. Positive scaling
preserves real-arithmetic argmax; binary64 rounding/underflow limits are
explicit. Original trainer/data/models/metrics/grid/bootstrap and original
results above are unchanged. The original rounded-NLL subtraction gives
.0076 oracle gap; unchanged full precision.007543134492483228 rounds to.0075
in the new ledger. No stronger deployment guarantee.
