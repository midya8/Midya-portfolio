# RatingLab

Observed-only rating factorization with manual NumPy alternating ridge solves, per-block decrease accounting, normal-equation residuals and full gradients. All eleven fits remain inspectable. A separately validation-selected bias-only control slightly beats the selected factors on test RMSE (.656176 versus .656457); all eight factor fits exhaust their stationarity budget. Twenty-three Python and five Node/real-Chrome tests include 60 independent exact rational ridge references, eleven fresh refits, test-label poisoning and 12,771 scalar/native predictions. The browser recomputes arbitrary indexed pairs and shared factor rotations, exposing why coordinate products are not causal preferences. Seven-module/six-command installed wheel. CC BY 4.0 historical UCI ratings, MIT code. Missing pairs are not negatives, and observed-rating RMSE is not top-N relevance, missing-pair accuracy or calibrated certainty.

## Why this project exists

A sparse rating matrix is not a dense matrix with zeros filled in. Rating 0 is an actual observation here. Fitting an unobserved pair as zero would invent evidence. This project keeps the observed-edge objective visible and derives every joint bias-and-factor block as a regularized linear system with the training mean fixed.

The sum-squared objective applies the regularizer once per parameter, not once per observation. Each user and item update checks its local objective decrease; half-pass accounting must telescope to the global objective. Full gradients are separate from the residual of the last solved block. An all-zero-factor stationary control has objective 4 while an explicit feasible factorization has objective .4: a zero gradient is not a global-minimum certificate.

## Evaluation without hiding the stronger control

Only the overall rating in 1,161 distinct user-item pairs from 138 users and 130 items is modeled. The frozen observed-edge split has 696 training, 232 validation and 233 test rows. All held-out entities happen to be warm. Eight rank-2/rank-4 factor fits use two penalties and two seeds. A separate bias-only family selects among three penalties with the same validation RMSE rule. Test rows are evaluated only after both selections, without refitting.

The selected factor fit has test RMSE .656456774; selected bias-only .656175974; training mean .758069714. The bias control stays visible even though it slightly wins. This is one historical split, not a significance or general-superiority claim. Source rows have no timestamps, so the split is not chronological. Synthetic cold-entity tests do not establish measured cold-start performance.

## Independent checks and editable inference

Sixty exact Fraction Gaussian-elimination references check ridge solutions. Finite differences check every coordinate of a tiny complete model gradient. All eleven saved candidates are fitted again; poisoning every test label must leave fitting, histories and selection unchanged. Independent scalar JavaScript checks 12,771 predictions against native references. Real Chrome exercises eleven models, 33 visible pairs, physical keyboard rotation, normal matrices, invalid-input recovery, clipboard success/failure, a JSON Blob download and 320/390/1280-pixel layouts.

A shared orthogonal rotation preserves predictions and regularization while changing coordinate products. Those products are algebraic terms, not identified tastes, semantic attributes or causal importance. The browser's 130-item strip keeps missing observations empty and does not pretend to be a validated recommendation ranking.

The installed wheel reproduces all seven package modules, six commands, eleven fits and both full audits outside the source checkout. Only the licensed rating CSV is bundled; consumer profiles, restaurant locations, names and demographics are not used. Source identifiers become stable indices, not features. MovieLens was considered but not redistributed because of its license terms.

- [Repository](https://github.com/midya8/ratinglab)
- [Live inspector](https://midya8.github.io/ratinglab/)
- [Objective, equations, protocol and limits](https://github.com/midya8/ratinglab/blob/main/METHOD.md)
- [Original UCI dataset](https://archive.ics.uci.edu/dataset/232/restaurant+consumer+data)
