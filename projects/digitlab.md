# DigitLab: train digit models, then audit what they do

DigitLab trains a linear model and a small tanh network from scratch in NumPy, with manual gradients. Compare them with a nearest-neighbor baseline, edit digits in the browser, and inspect separate exact proofs for the fixed linear model. The nearest-neighbor baseline wins the clean test comparison: 1,760 of 1,797 correct, versus 1,734 for the network and 1,698 for the linear model, all using the same 3,062 fitting examples.

## Where to start

| Question | Open or run | What to keep in mind |
| --- | --- | --- |
| How do edits change a prediction or attribution? | [Model inspector](https://midya8.github.io/digitlab/) | Floating inference and reference-relative contributions, not a certificate |
| How do the trained models compare? | `demo`, `train`, `evaluate` | One frozen split, with the stronger same-fit baseline retained |
| Is every input in a clipped box classified correctly? | `box-audit` | An exact proof for the stored linear coefficients, not the nonlinear network |
| Where can linear-model error first occur? | `radius-audit` | The error-radius infimum may not be attained |

At normalized radius 0.1, the network has 898 correct test predictions under FGSM and 768 under the finite PGD candidate pool. Those searches do not prove robustness, label preservation or imperceptibility. Input attacks are continuous, not restricted to valid integer-count handwriting.

The current suite has 78 Python tests and six Node/real-Chrome tests. Historical counts below describe the checks added at each stage.

![Frozen official-test audit and selected digit adaptations](https://raw.githubusercontent.com/midya8/digitlab/a5f2da5e9e6732ace852f7af39bb73bf6afbd66c/assets/digit-audit.svg)

## Inspect reference-relative contributions

A [live model inspector](https://midya8.github.io/digitlab/) now adds baseline-relative class-logit Integrated Gradients for the unchanged UCI digit models. Choose the class and zero or fit-only mean reference, inspect all 64 signed contributions and their logit-sum residual, and keep the attack label separate. An algebraic tanh specialization is checked against independent 128-node quadrature on 40 reference vectors; all 7,188 official model/reference/row cases are finite. 78 Python tests and six Node/real-Chrome tests include 106 attribution reference vectors plus the existing 52 inference/gradient cases. Four reproducible audit figures, ten-module/ten-CLI wheel checks, and mobile/keyboard/touch controls. Established attribution, not a new method, causal importance, explanation quality or a certificate. The stronger same-fit 1NN clean result, exact linear box/radius proofs and original data/models remain visible.

![Finite attribution checks and baseline-relative signed digit maps](https://github.com/midya8/digitlab/raw/24112893ca7560c364e79c328464dd5c5b68e7c6/assets/attribution-audit.svg)

Both references are explicit: all-zero block counts and the frozen mean of only
3,062 fitting rows, never the validation or official test rows. The explained
quantity is a selected class logit, not a softmax probability. The page displays
the input and reference logits, their difference, contribution sum and floating
residual, with all 64 signed coordinates available as text. Neither reference
is presumed neutral, realistic or causally meaningful.

Independent Gauss-Legendre path integration checks individual coordinates on
40 fixed reference vectors, rather than checking completeness alone. The saved
maximum coordinate difference is 3.56e-15, and the maximum sum residual across
7,188 official cases is 1.07e-14. These are finite numerical checks, not exact
proofs, explanation-quality metrics or evidence of model trustworthiness.
Changing the baseline changes both the path and the question. The added
ATTRIBUTION.md documents the derivation, established sources, controls and
limits; the fourth SVG includes the complete saved report as metadata.

## Edit inputs without a prediction server

A [live model inspector](https://midya8.github.io/digitlab/) runs manual JavaScript inference and input gradients for the unchanged, from-scratch UCI digit models. Paint with mouse/touch/keyboard, inspect all ten scores and compute clipped FGSM without an upload or prediction service. Editing clears the attack label. 64 Python tests and four Node/real-Chrome tests include 52 independent NumPy reference cases and mobile/keyboard/touch checks. The stronger same-fit 1NN clean result stays visible. Separate exact linear box/radius proofs retain all 1,797 official rows and boundary-attainment distinctions; they do not certify this floating demo or the nonlinear MLP. Original data/models/reports and CC BY 4.0 attribution are preserved.

[Open the live demo](https://midya8.github.io/digitlab/), or clone the repository
and open `docs/index.html` with no runtime install. Ten first-per-label official
examples are explicitly not representative. The page makes no accuracy promise
for edited drawings. Softmax scores are not calibrated confidence. FGSM keeps
its result separate from the original grid, requires an explicit loss label
after an edit, and does not certify human-label preservation or imperceptibility.
The exact rational proofs below are not executed by the page.

Model/sample exports remain byte-exact. Floating NumPy reference regeneration
uses explicit finite absolute tolerances, with roundoff acceptance and material
corruption/nonfinite/discrete-change rejection controls. CI installs stable
Chrome for Testing explicitly instead of assuming a runner's preinstalled
browser works. A real browser checks 320/390/1280px layout, keyboard painting,
touch dragging, both models, attack bounds, clear and restore.

Ordinary static-host requests contact GitHub Pages, which logs IP addresses for
security; prediction/input data is not uploaded. Use the local files to avoid
host contact. [Browser protocol and privacy](https://github.com/midya8/digitlab/blob/main/WEB.md).

## Check the first possible linear-model error

Real UCI digit training in NumPy with a stronger same-fit 1NN baseline and frozen official-test models. Exact linear audits retain all 64,692 box margins. v0.3 solves all 1,797 clipped adversarial-radius infima: 99 clean errors, 796 positive attained thresholds and 902 positive unattained infima. Lowest-index ties determine whether the boundary itself is an error; all 7,188 old box decisions agree. 59 tests include 201 gradient probes, two independent 144-case vertex references, 160 Fraction row references, 100 official-boundary checks and three full-report figures. Nine-module/eight-CLI wheel reproduction. Original datasets, models and old reports preserved, with CC BY 4.0 data attribution. Exact real affine proofs, not all floating executions, nonlinear MLP verification, imperceptibility or adaptive 1NN ranking.

![Exact radius and boundary-attainment evidence](https://raw.githubusercontent.com/midya8/digitlab/5c2fcdad50ec3c1fbefb69a94537607013c0601b/assets/radius-audit.svg)

The event solver follows exact affine-margin slopes until pixels clip, solves each first zero algebraically and combines all competitors with tie-aware attainment. The first attained example is row 6 (true 6, competitor 4); the first unattained example is row 0 (true 0, competitor 9). Their zero-margin boundary predictions are evaluated exactly and are not asserted to agree with floating evaluation on a mathematical tie. An error witness for an unattained threshold lies strictly beyond it, not at it. These first-category examples are diagnostic, not a representative sample.

[Full threshold proof, controls and sources](https://github.com/midya8/digitlab/blob/main/RADIUS.md).

## Prove linear-model correctness inside a box

Real UCI digit training in NumPy with manual gradients, a stronger same-fit 1NN clean baseline and a frozen official-test audit. v0.2 adds exact real affine-box correctness for the fixed linear model: 1,698 / 1,495 / 1,028 / 23 of 1,797 test rows at radii 0 / 1/20 / 1/10 / 1/5. Attained witnesses expose 14 and 10 saved PGD survivors at the latter two radii. All 64,692 margins and 7,188 witness decisions are retained. 45 tests include 201 gradient probes, 144 all-vertex certificates, 160 independent Fraction row references, two full-report figures and six-mode/eight-module wheel parity. Original source data, models and finite-attack report are preserved. CC BY 4.0 data attribution. Certificates concern the real affine function of loaded binary64 coefficients, not all floating executions or the nonlinear MLP; no imperceptibility or adaptive 1NN ranking claim.

![Exact affine-box proof and missed-PGD witnesses](https://raw.githubusercontent.com/midya8/digitlab/562e23c333c85051959b32f6e5ba8cd3926679f0/assets/box-audit.svg)

The method minimizes each true-label-versus-competitor affine margin at its valid coordinate endpoints. Every competitor is tested, with strict positivity only when a lower class index would win a tie. A clipping control separates minimum 1 on the valid [0,3/10] domain from the invalid un-clipped result -1; a zero-margin tie control is correct for label 0 but fails for label 1. All clean and 7,188 selected witness predictions agree with NumPy, a finite check rather than an all-domain floating error bound. No training, original evaluation choices or original report changed.

[Full proof, exact coefficients, tie/clipping controls and sources](https://github.com/midya8/digitlab/blob/main/BOX.md).

## Protocol and implementation



This is UCI Optical Recognition of Handwritten Digits, **not MNIST**. Each input
is 64 block counts in 0..16, normalized by the fixed metadata scale 16. The
original 3,823-row training file and separate 1,797-row test file are bundled
with SHA-256 checks and [CC BY 4.0 attribution](https://github.com/midya8/digitlab/blob/main/digitlab/data/LICENSE.md).
UCI reports 30 training writers and a different 13 test writers. Numeric files
have no individual writer IDs, so that assertion is source-reported, not
independently verified here.

Only the official training file is partitioned: within each class, sort feature
SHA-256 hashes and hold out the first floor(20%) rows. That gives **3,062 fitting
rows and 761 validation rows**. All official test rows remain separate. Exact
feature-hash overlap is zero across all three partitions; this does not rule
out similar handwriting or prove writer-disjoint validation.

The fixed protocol, fitting/validation indices and checkpoint choices are
saved. Both models train for 80 epochs using seeded shuffled minibatch SGD
with momentum, checking epochs 10, 20, 40 and 80. Selection minimizes validation
NLL, not test performance or validation accuracy. Both select epoch 80. The MLP
has *higher* validation accuracy at epoch 40, but that was not the declared
selection criterion. Test examples were first parsed after model selection and
all attack settings were fixed. Subsequent unchanged re-evaluations check
reproduction; no test-driven hyperparameter or seed selection is performed.

## The baseline wins on clean digits

| Classifier, all on the same 3,062 fitting rows | Official test correct | Accuracy | Test NLL |
|---|---:|---:|---:|
| Exact Euclidean 1NN | 1,760 / 1,797 | 97.94% | Not a probability model |
| Linear softmax, 650 parameters | 1,698 / 1,797 | 94.49% | 0.16906 |
| Tanh MLP, 2,410 parameters | 1,734 / 1,797 | 96.49% | 0.12096 |

1NN uses exact squared Euclidean distances with earliest fitting-row index on
exact ties. It has no tuned `k`, feature scaling fit or hidden all-training-data
advantage. It stores the same fitting examples used by both trained models.
These are descriptive results on one historical benchmark and fixed protocol,
not superiority or SOTA claims. Test confusion matrices and every prediction
are included in the [complete report](https://github.com/midya8/digitlab/blob/main/digitlab/artifacts/report.json).

## Better clean accuracy does not certify input robustness

White-box attacks know the selected model and true labels. Pixels stay in
[0,1], with L-infinity radius epsilon around each original input. Normalized
**epsilon 0.1 corresponds to 1.6 original 0..16 block-count units**. The continuous
attack domain is not restricted to valid integer-count handwriting. No human
label-preservation, imperceptibility or real-world OCR threat claim is made.

At epsilon 0.1 on the MLP:

- Clean: 1,734 / 1,797 correct.
- One fixed random-sign control: 1,708 / 1,797 correct.
- FGSM: 898 / 1,797 correct, fooling 836 of the 1,734 initially correct rows.
- PGD candidate pool: 768 / 1,797 correct, fooling 966 of those initially correct rows.

PGD uses 20 projected steps and three seeded random starts, step size epsilon/4.
The per-row candidate pool includes clean input, FGSM, every start and every
iterate. It prefers any misclassification, then larger true-label cross entropy
among equally successful candidates. This explicit pool cannot lose a clean or
FGSM misclassification, but it is still a finite attack, **not a certificate or
optimal attack**. Surviving these attacks is not proof of robustness. Attacks
are also reported at other fixed-in-advance radii, including zero-radius identity.
A single seeded random-sign draw is a descriptive control, not a confidence
interval or isolated causal mechanism estimate.

1NN gets 1,678 correct on the MLP's epsilon-0.1 PGD images. That is **transfer**,
not an adaptive attack on 1NN. Do not rank model robustness from that comparison.
The six shown image pairs are explicitly selected: first three initially
correct attack successes, then first three survivors, at MLP PGD epsilon 0.1.
They are not a representative test sample.



## Reproduce the checks

- [Code and offline commands](https://github.com/midya8/digitlab)
- [Full protocol, equations, source attribution and limits](https://github.com/midya8/digitlab/blob/main/METHOD.md)
- [Every prediction and confusion matrix](https://github.com/midya8/digitlab/blob/main/digitlab/artifacts/report.json)
- [Dataset license and original hashes](https://github.com/midya8/digitlab/blob/main/digitlab/data/LICENSE.md)

Code is MIT; UCI data and adapted digit images are CC BY 4.0. Established FGSM, PGD, softmax, tanh, momentum and nearest-neighbor methods are not claimed inventions.
