# DigitLab: real digits, stronger baseline, bounded attacks

Real UCI digit training in NumPy with manual gradients and a frozen official-test audit. On 1,797 test digits, exact 1NN gets 1,760 correct, the tanh MLP 1,734 and linear softmax 1,698, all using the same 3,062 fitting examples. At normalized L-infinity radius 0.1, MLP correct counts fall to 898 under FGSM and 768 under a 20-step/three-start PGD candidate pool, versus 1,708 under one seeded random-sign control. 30 tests include 201 independent gradient probes, full refit without test-loader access, strict JSON inference and saved-report reproduction. The official train/test files retain original hashes and CC BY 4.0 attribution. Continuous input attacks, not imperceptibility, certified robustness or an adaptive 1NN ranking.

![Frozen official-test audit and selected digit adaptations](https://raw.githubusercontent.com/midya8/digitlab/a5f2da5e9e6732ace852f7af39bb73bf6afbd66c/assets/digit-audit.svg)

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



## Reproduce and inspect

- [Code and offline commands](https://github.com/midya8/digitlab)
- [Full protocol, equations, source attribution and limits](https://github.com/midya8/digitlab/blob/main/METHOD.md)
- [Every prediction and confusion matrix](https://github.com/midya8/digitlab/blob/main/digitlab/artifacts/report.json)
- [Dataset license and original hashes](https://github.com/midya8/digitlab/blob/main/digitlab/data/LICENSE.md)

Code is MIT; UCI data and adapted digit images are CC BY 4.0. Established FGSM, PGD, softmax, tanh, momentum and nearest-neighbor methods are not claimed inventions.
