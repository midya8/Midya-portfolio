# CalibrLab: confidence calibration from scratch, measured end to end

A model can be accurate and still be wrong about how sure it is - and for anything downstream of a probability (thresholds, triage, abstention), that matters as much as accuracy. CalibrLab implements the measurement and the simplest principled repair in dependency-free Python: ECE/MCE/Brier/NLL metrics, a per-bin reliability table, and temperature scaling fit on validation data only, all measured on a fixture designed to be overconfident.

## The fixture

Six Gaussian classes in 16 dimensions (noise 0.6) so real uncertainty exists. A one-hidden-layer MLP (hand-derived backprop, finite-difference verified) trains on 20 samples per class - few enough that it memorizes: train accuracy 1.0000, test 0.5563, and its top confidence bin averages 0.9735 confidence at 0.6602 accuracy. ECE before repair: 0.2765.

## The repair, with its exact guarantee

Temperature scaling divides the logits by one scalar T fit by grid search on the VALIDATION split's NLL - the test split never influences T. The method's one guarantee is exact: positive scaling preserves argmax, so accuracy cannot move. The gates assert drift == 0 bit-for-bit.

## Measured results (checked-in fixture, pinned in tests)



## What's honest about it

- The oracle row fits T on test and is labeled unattainable: it quantifies what the validation fit leaves on the table (NLL 1.1984 vs 1.2060 - a gap of 0.0076), it is never a fit target.
- After scaling, most bins skew mildly UNDER-confident: one scalar cannot match a per-bin curve. MCE stays at 0.1216 because small bins are noisy. Both are reported in the README, not smoothed over.
- Gates are deterministic regression checks on this fixture's primary artifact (overconfidence before, calibrated after, exact invariance) - not general proofs, and no arm is gated to stay weak.

## Engineering notes

- The MLP's gradients are derived in code and finite-difference verified (max error < 1e-6 in the suite).
- 16 tests separate three concerns: metric unit tests (perfect calibration scores zero, NLL of uniform is log k, argmax invariance under T), gradient verification, and deterministic fixture regression (run twice, same numbers).
- CI runs the suite on Python 3.10-3.13 plus an offline demo asserting both gate sides: the achievable set passes and an impossible ECE reduction (0.9) fails.

Repo: [midya8/calibrlab](https://github.com/midya8/calibrlab)
