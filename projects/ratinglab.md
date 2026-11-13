# RatingLab

RatingLab fits explicit ratings using NumPy alternating ridge solves. Only observed pairs enter the objective; zero is a real rating, not a missing value. The browser shows score terms, normal equations, objective histories and coordinate rotations for all eleven saved fits.

On the fixed test split, a separately validation-selected bias-only control has slightly lower RMSE than the selected factor model: .656176 versus .656457. All eight factor fits exhaust their numerical stationarity budget. Neither result is a claim about ranking quality, causal preferences or missing-pair accuracy.

The current suite has 37 Python and 14 Node/actual-Chrome tests. Checks include independent exact rational ridge references, eleven fresh fits, test-label poisoning, 12,771 scalar/native predictions and complete conditional-edit witnesses. The installed wheel imports ten modules and runs eight main CLI commands plus two single-row module commands outside checkout. The historical UCI ratings are CC BY 4.0; code is MIT.

The v0.2 conditional-response extension separates saved scores, a freshly re-solved unmodified ridge block and its finite rating edit or row deletion. It exposes leverage, the positive deletion denominator, query derivatives and all-opposite-index response curves. Sixty additional exact rational design systems, 2,784 direct deleted-block refits and 576 native/scalar-JavaScript witnesses check the formulas. Original factors and scores are unchanged. The mean and opposite factors remain frozen and retain information from the row: this is not full-model leave-one-out validation, causal influence, data unlearning or an uncertainty bound. [Conditional edit/deletion inspector](https://midya8.github.io/ratinglab/influence.html). [Derivation and limits](https://github.com/midya8/ratinglab/blob/main/INFLUENCE.md).

The v0.3 joint-batch inspector changes or removes multiple original training rows within one frozen block. Target edits add; joint deletions solve a coupled Schur system and generally differ from a sum of separate-original-baseline deletions. It shows the full source-bound problem, conservative positive-ridge bound, numerical condition/refusal checks and all-query joint/separate curves. Independent checks add 320 rational direct-system cases, 128 real augmented-least-squares cases and 320 complete native/browser Cholesky responses plus 4 controls. The current 37 Python/14 Node suite and installed-wheel checks include this extension. Original fits, scores and stronger bias control stay unchanged. This remains a conditional calculation, not full ALS retraining, cross-validation, causal attribution, uncertainty or data unlearning. [Joint batch inspector](https://midya8.github.io/ratinglab/batch.html). [Derivation and limits](https://github.com/midya8/ratinglab/blob/main/BATCH.md).

## Observed-only objective

A sparse rating matrix is not a dense matrix with zeros filled in. Rating 0 is an actual observation here. Fitting an unobserved pair as zero would invent evidence. This project keeps the observed-edge objective visible and derives every joint bias-and-factor block as a regularized linear system with the training mean fixed.

The sum-squared objective applies the regularizer once per parameter, not once per observation. Each user and item update checks its local objective decrease; half-pass accounting must telescope to the global objective. Full gradients are separate from the residual of the last solved block. An all-zero-factor stationary control has objective 4 while an explicit feasible factorization has objective .4: a zero gradient is not a global-minimum certificate.

## Fixed-split evaluation

Only the overall rating in 1,161 distinct user-item pairs from 138 users and 130 items is modeled. The frozen observed-edge split has 696 training, 232 validation and 233 test rows. All held-out entities happen to be warm. Eight rank-2/rank-4 factor fits use two penalties and two seeds. A separate bias-only family selects among three penalties with the same validation RMSE rule. Test rows are evaluated only after both selections, without refitting.

The selected factor fit has test RMSE .656456774; selected bias-only .656175974; training mean .758069714. The bias control stays visible even though it slightly wins. This is one historical split, not a significance or general-superiority claim. Source rows have no timestamps, so the split is not chronological. Synthetic cold-entity tests do not establish measured cold-start performance.

## Independent checks and browser inference

Sixty exact Fraction Gaussian-elimination references check ridge solutions. Finite differences check every coordinate of a tiny complete model gradient. All eleven saved candidates are fitted again; poisoning every test label must leave fitting, histories and selection unchanged. Independent scalar JavaScript checks 12,771 predictions against native references. Real Chrome exercises eleven models, 33 visible pairs, physical keyboard rotation, normal matrices, invalid-input recovery, clipboard success/failure, a JSON Blob download and 320/390/1280-pixel layouts.

A shared orthogonal rotation preserves predictions and regularization while changing coordinate products. Those products are algebraic terms, not identified tastes, semantic attributes or causal importance. The browser's 130-item strip keeps missing observations empty and does not pretend to be a validated recommendation ranking.

The installed wheel reproduces all ten modules including the package root, eight main CLI commands, two single-row module commands, eleven fits and both full audits outside the source checkout. Only the licensed rating CSV is bundled; consumer profiles, restaurant locations, names and demographics are not used. Source identifiers become stable indices, not features. MovieLens was considered but not redistributed because of its license terms.

- [Repository](https://github.com/midya8/ratinglab)
- [Live inspector](https://midya8.github.io/ratinglab/)
- [Objective, equations, protocol and limits](https://github.com/midya8/ratinglab/blob/main/METHOD.md)
- [Original UCI dataset](https://archive.ics.uci.edu/dataset/232/restaurant+consumer+data)


## Finite response with an explicit frozen boundary

The two conditional normal systems remain positive definite with λ > 0, including deletion of a block's sole observation. A target edit has exactly linear finite response within this quadratic problem. Sherman-Morrison gives a deletion update scaled by the original conditional residual and 1 − h. A bound 1 − h ≥ λ/(λ + ‖a‖²) follows from the deleted system's ridge floor. Numerical real-data readouts are not rational or interval certificates.

The saved user block may no longer be its conditional minimizer after the final item pass. That movement is reported separately before any edit. The inspector's three displayed scores prevent a changed conditioning baseline from being mislabeled as an observation's effect. A deleted-row residual is algebra, not a valid full-model cross-validation estimate: original opposite factors and training mean still encode the row. No original model, metric, split, source row or original figure is modified.
