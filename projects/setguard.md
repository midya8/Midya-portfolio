# SetGuard

[Public repository](https://github.com/midya8/setguard) · [Live rank ledger](https://midya8.github.io/setguard/)

SetGuard turns a fixed classifier's probabilities and separate calibration labels into prediction sets. Save the fitted thresholds as JSON, predict without labels and inspect every score/rank/inclusion decision. It implements standard split conformal prediction, not a new algorithm.

| Question | Read | Boundary |
| --- | --- | --- |
| Why is this label included? | [Inclusion ledger](https://midya8.github.io/setguard/) | A deterministic witness does not validate a deployment. |
| What changes with one threshold per class? | [Classwise mode](#optional-label-conditional-mode) | The target is label-conditional, not input-conditional or fixed-split coverage. |
| What does the rank count prove? | [Rank diagnostic](#rank-diagnostic) | The arithmetic cannot check exchangeability or model/calibration independence. |

41 Python and four Node/actual-Chrome tests and offline CI on Python 3.10-3.13 cover rank corrections, ties,
empty/all-label sets, schema/artifact failures, class order and the demo.

## Inclusion ledger (0.2)

A native score/rank/inclusion ledger and independent no-API browser now make the existing method inspectable. Five fixed public synthetic cases show pooled/classwise thresholds, every equality tie, absent-label infinity boundaries, each unlabeled candidate's inclusion/exclusion reason, 19 sampled alpha points and each held-position rank check. No candidate labels are fitted. The original three empirical arms, probabilities, calibration data and scores remain unchanged.

The browser's native-compatible JSON retains exact input, rank/threshold artifacts and decisions. Python uses Fraction decimal ranks; JavaScript independently uses BigInt rationals. Scores are still binary64 numbers. The point path is descriptive, not alpha optimization; the deletion ledger is deterministic rank arithmetic, not uncertainty or an exchangeability test.

41 Python and four Node/actual-Chrome tests check 95 case/alpha witnesses, 160 independent Fraction games, 80 integer-grid games, 4,199 pooled positions, 8,341 pooled/classwise deletion records and 2,736 candidate-label decisions. UI switching checks all 20 candidate rows and 22 groups. An installed wheel reproduces the original demo and 95 witnesses outside the checkout, imports six modules and executes six CLI commands. Earlier release checks inspected desktop/mobile pixels and tested keyboard controls and JSON exports.

[Rank ledger equations and numerical limits](https://github.com/midya8/setguard/blob/main/LEDGER.md) · [Merged implementation PR](https://github.com/midya8/setguard/pull/1)

## Separation of concerns

`core.py` owns probability/schema validation, corrected-rank fitting, artifact
validation, unlabeled prediction and empirical diagnostics. `demo.py` has a
fixed seeded probability generator and no training loop. `cli.py` is JSON I/O.
Only `fit` sees calibration labels; `predict` rejects a labels field.

## Finite sample correction and ties

For n calibration scores, k=ceil((n+1)(1-alpha)). The k-th smallest is used
without interpolation, with an all-label sentinel when k=n+1. Alpha's decimal
representation is converted to a Fraction before the ceiling. The exact score
comparison is repeated at prediction; no subtraction-based p threshold rewrite
introduces another floating boundary. Scores still use machine precision.
All equal scores are included at the threshold, making ties conservative.
There is no randomized upper-coverage claim. Empty sets remain empty.

## Artifact contract

Version 1 method `split-conformal-1-minus-p`. Class names and order are explicit
and required to match at inference. Null threshold means all labels; serialized
Infinity is avoided. Artifact schema/rank/boundary consistency is validated,
but the artifact does not contain signed provenance or prove the threshold came
from the stated calibration rows. An altered but structurally valid threshold
can change behavior. Store artifacts with your model version and data lineage.

## Demonstration and counterexample

200 calibration rows (seed11), 2000 test rows (seed29). Underlying class
probabilities come from normalized Gamma(.7,1) draws. Labels are sampled from
that vector; the predictor cubes and renormalizes it. Calibration and test
are independent seeded samples of this same design. Target .9, observed
coverage .9235, mean size3.017, argmax accuracy .496. No benchmark superiority
is claimed. The shifted arm deliberately sets truth to the least-probable
class with the identical test probability rows. Coverage .076 is a boundary
example of violating exchangeability, not a measured general drift rate.

## Rank diagnostic

Leave each score position out once, threshold the others, count inclusion.
For every finite multiset, the count is at least k among n+1 positions.
The demo distinct-score sequence covers 19/21; exhaustive tests cover 243
five-position sequences with tied scores at five alpha values. This audit
checks deterministic rank mechanics. It cannot establish exchangeability,
training/calibration independence or a population guarantee from one dataset.

## Statistical scope

The standard lower bound is marginal over calibration and future test data
under exchangeability and a predictor fixed independently of calibration.
It is not conditional on a particular calibration split, class or input.
Empirical test coverage can fall below target. Tuning alpha/score/model after
inspecting calibration/test data invalidates a naive application of the bound.
No protected-attribute, drift or time-series coverage claim is made. Classwise mode is only conditioned on the true label, not arbitrary protected groups. Set size
reflects a tradeoff and can reach all classes; large sets may be unhelpful.

## Sources

- https://arxiv.org/html/2107.07511 (Angelopoulos and Bates, Section1, AppendixD)
- https://androma.org/theorems/17354 (rank boundary and tied-score lower bound)

## Optional label-conditional mode

```bash
python -m setguard fit --input examples/calibration.json --alpha 0.1 --mode classwise > classwise.json
```

API: `fit(calibration, alpha=.1, mode="classwise")`. Pooled mode stays the
default and keeps its version-1 artifacts. Classwise mode uses a version-2
artifact with `class_counts`, `ranks` and `thresholds` in class-name order.
Each threshold uses only calibration rows whose true label is that class.
Absent classes, or classes with too few rows for the requested rank, get a
null threshold and are always included. There is no pooled fallback.

This standard classwise/Mondrian construction targets label-conditional
coverage under exchangeability within each label and a predictor fixed
independently of calibration. It averages over calibration/test randomness;
it does not promise every realized class rate exceeds the target, input-
conditional coverage, fixed-calibration coverage or validity under shift.
Class names/order alone cannot verify these assumptions. Rare classes can
make sets much larger or force inclusion on every row.

On the same development fixture, class counts are [43,37,50,35,35]. Classwise
empirical coverage is 0.9285 and mean size 3.1095 (pooled: 0.9235 and 3.017).
Class d's realized coverage is only 0.8859, below the 0.9 target. This finite
split does not prove or refute the procedure's population coverage theorem,
and is not evidence that classwise mode always improves coverage or size.

Reference: [Class-Conditional Conformal Prediction with Many Classes](https://www.stat.berkeley.edu/~ryantibs/papers/classconf.pdf),
description of standard/classwise and Mondrian methods. This repository uses
the standard classwise construction, not that paper's clustered method.
