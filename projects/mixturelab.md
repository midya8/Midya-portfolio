# MixtureLab

Manual Gaussian-mixture EM on real, licensed chemistry. Likelihood is not identity.

- [Repository and reproduction](https://github.com/midya8/mixturelab)
- [Live 13-feature density inspector](https://midya8.github.io/mixturelab/)
- [Derivation, frozen protocol and source ledger](https://github.com/midya8/mixturelab/blob/main/METHOD.md)

## The engineering question

Can a complete density-estimation implementation expose what each optimization step did, preserve a real holdout, and show why better likelihood does not identify true categories?

The estimator owns log-space E-steps, weighted means/scatters, full and diagonal constrained covariance M-steps, restart selection, validation selection and all artifacts. NumPy supplies linear algebra, not a mixture estimator. No model API, sklearn estimator or private dataset.

## Experiment

UCI Wine, Aeberhard & Forina (1992), 178 chemical analyses and 13 features. Original files and SHA256 checks are bundled under CC BY 4.0. The loader strips the cultivar target before returning features; no labels enter splitting, fitting or scoring.

A new fixed label-free split uses 106 training, 36 validation and 36 test rows, not an official UCI benchmark split. Scaling is training-only. Both covariance families, k in {1,2,3,5}, and three fixed seeds yield 24 fits. The covariance floor 0.05 is fixed in squared standardized units. Training likelihood chooses each restart; validation NLL chooses the configuration; test scores open afterward, without a validation refit. All candidates stay visible.

| Model | Train NLL | Validation NLL | Test NLL |
| --- | ---: | ---: | ---: |
| Diagonal k=5, seed 11, validation pick | 13.40992 | 13.45753 | 15.34782 |
| Full k=1, seed 11, fitted Gaussian control | 14.40496 | 14.99046 | 15.72686 |
| Full k=5, seed 23, best training configuration | 10.20168 | 17.95955 | 18.47913 |

Mean negative natural log density in standardized 13D coordinates, lower is better. More capacity improves training density here while worsening test density. This one small historical split does not show general superiority or statistical significance.

## The audit that matters

With a fixed covariance constraint C >= 0.05I, the full-covariance M-step clips weighted scatter eigenvalues. Adding 0.05I is a different operation and generally does not solve that subproblem. The method derives the precision-space KKT conditions and checks them numerically on 100 random scatters, with 40 independent analytic 2D clipping references.

Every EM update keeps the old posterior and records:

`mean likelihood gain = complete-data Q gain + posterior KL`.

All initial/final models, complete scalar histories, and final before/after transition witnesses are retained. All 24 fits meet the stated likelihood-increment tolerance. That is not a stationary-point test or a global optimum certificate. Zero numerical component mass fails explicitly, with no hidden reseeding.

## Actual browser inference

A separate scalar JavaScript Cholesky implementation recomputes density and every component responsibility for arbitrary edited 13-feature vectors. Training-only PCA supplies a view, not the fit. Its ellipses are 90% probability contours of the model's 2D Gaussian marginals, not full-dimensional decision regions or measured coverage.

The far-input control shows how a nearly certain within-model posterior can accompany very low density. The page includes all eight model choices, all 24 restart summaries, complete current-fit trajectory, JSON witness copy/download and clear invalid-input errors.

## Verification and limits

36 Python tests and eight Node/real-Chrome tests cover independent scalar/2D Gaussian likelihoods, weighted moments, precision-space KKT checks, analytic covariance clipping, EM identities, holdout-poisoning isolation, original-unit density transformations, all eight models x 178 source rows (1,424 native/browser evaluations), every responsibility, edited inputs, physical keyboard behavior, copy/download and 320/390/1280 layouts. A built wheel imports ten modules and runs all five CLI commands outside the checkout, including all 24 fresh fits and saved/fresh audits. Numerical reproduction uses tolerances, not promised bitwise eigenvectors.

The controls show unconstrained covariance collapse, label permutation, duplicate-component nonidentifiability and additive versus constrained covariance updates. They are supplied mathematical controls, not causal component ablations on the chemistry. The saved audit checks histories as scalar identities and the final transition; it does not authenticate model origin or replay every historical parameter state.

No cultivar prediction, wine-quality score, calibrated uncertainty, identified latent cause, global mixture optimum, floor/split sensitivity guarantee or population-wide conclusion. Standard EM and constrained optimization, original implementation. Code MIT; data CC BY 4.0; no endorsement.

## Fixed-model geometry extension (v0.2)

[Live gradient, curvature and ascent inspector](https://midya8.github.io/mixturelab/geometry.html) · [Derivative and search derivation](https://github.com/midya8/mixturelab/blob/main/GEOMETRY.md)

The new page computes all 13 input-score coordinates, the complete 13x13 Hessian, the kx13 component-posterior Jacobian and original-unit transforms. These are fixed-model input derivatives, not parameter training or causal feature importance. A chosen finite coordinate change is compared with first- and second-order predictions.

A normalized-gradient line search accepts only an actual log-density gain at least 0.0001 times step length times gradient norm. It retains every accepted point and stops explicitly on norm, budget or line-search exhaustion. Eight traces use the same already-public input at budget 128: the four diagonal models and full k=1 reach the norm criterion; full k=2,3,5 remain budget-exhausted. No mode is certified.

Two equally weighted unit Gaussians at -2 and +2 have zero input gradient and curvature +3 at zero. The routine stops there at a strict minimum, visibly demonstrating why its norm rule is not a mode certificate. A perturbed start moves away; a single Gaussian and duplicate-component controls check closed forms.

Independent checks include 312 all-coordinate finite-difference probes, every posterior-Jacobian and Hessian column, 50 scalar directional second differences, affine/rotation/permutation checks, 40 complete native/browser geometry cases and eight trace references. New tests also recreate only the two new reference artifacts byte-for-byte, enforce CLI row/budget/number types and exercise all browser budgets, keyboard input, invalid exports, copy failure/success, real downloaded JSON and expanded mobile/desktop layouts. The final suite has 36 Python and eight Node/real-Chrome tests. The installed wheel imports ten modules and runs all seven commands outside checkout, including all 24 fresh fits and audits.

All original models, experiment report, source data, split, scales, browser references, browser dataset and score figure remain byte-for-byte unchanged. The extension does not tune against test results, guarantee chemically plausible inputs, claim calibrated confidence or certify global/local modes. A technical secondary source has a matrix-form softmax typo; the derivation explicitly records it and uses the correct elementwise chain rule instead.
