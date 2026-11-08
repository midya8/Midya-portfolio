# DistillLab: knowledge distillation from scratch, measured against matched control arms

A small model trained on a teacher's soft outputs often beats the same model trained on hard labels - the classic explanation is "dark knowledge": the teacher's per-sample class-similarity structure. DistillLab implements the whole pipeline in dependency-free Python and, more importantly, measures the gain against matched control arms instead of repeating the explanation: a pseudo-label arm trained on the teacher's argmax, a uniform-smoothing arm, and a permuted-target control.

## The fixture

Eight classes arranged on a ring in 32 dimensions: each class center blends its own random unit direction with its predecessor's, so neighboring classes are genuinely similar. The teacher (hidden 64, 2632 params) trains on 100 samples per class. Students (hidden 6, 254 params - about 10x smaller) train on only 10 per class: the low-data regime where distillation is supposed to matter.

## The loss, by hand

```
L = alpha * T^2 * CE(softmax(z_student / T), softmax(z_teacher / T)) + (1 - alpha) * CE(softmax(z_student), onehot)
dL/dz = alpha * T * (p_s^T - p_t^T) + (1 - alpha) * (p_s - onehot)
```

The T^2 prefactor restores the gradient scale that dividing logits by T removes; one factor of T survives the chain rule. Every parameter gradient is finite-difference verified in the test suite.

## Matched arms, different target conventions

Identical student seeds, capacity, learning rate and epoch budget. Target conventions differ; the original mismatched-target arm uses T=3 while the main distilled arm uses T=4:

- **direct**: one-hot labels.
- **distill**: teacher soft targets at T=4 blended with the label (alpha=0.95).
- **pseudo**: the teacher's argmax predictions as hard labels on the same inputs - input-specific teacher signal with no distribution content.
- **smoothing**: one-hot labels smoothed 0.1 toward uniform - input-INDEPENDENT softening.
- **control**: teacher soft targets for *different, deterministically permuted inputs* - the same marginal distribution of target vectors, zero input-specific information.

## Measured results (checked-in fixture, pinned in tests)

| arm | test accuracy | train accuracy |
|---|---|---|
| direct | 0.6813 | 1.0000 |
| pseudo-labels (teacher argmax) | 0.7094 | 0.7875 |
| **distilled (soft targets, T=4)** | **0.7469** | 0.8000 |
| uniform label smoothing | 0.6781 | 1.0000 |
| control (permuted targets) | 0.1250 | - |
| T=1 ablation | 0.7219 | - |

Teacher: 0.8344. Distillation gain: **+0.0656** over direct at identical budget, measured against the control arms on this fixture:

- **Pseudo-labels exceed direct by +0.0281** - training on the teacher's own argmax predictions already helps here.
- **Distillation exceeds pseudo-labels by a further +0.0375** - consistent with the classic dark-knowledge explanation, but soft-vs-argmax also changes target confidence and the optimization problem, so this comparison alone does not isolate why. The suite pins the arm ordering from below as fixture regression.
- **One uniform-smoothing setting**: eps=0.1 scores 0.6781, below direct on this fixture. This does not rule out other smoothing settings or identify the mechanism behind the distillation difference.
- **Not input-mismatched signal**: the permuted-target control sits at exactly chance (1/8 = 0.1250). Reported, not gated: it is a comparison between matched arms, and if it ever moved the README numbers would move with it.
- **A smaller measured train-test gap**: direct memorizes (train 1.0000, gap 0.3187); distilled does not (train 0.8000, gap 0.0531).
- **The student genuinely imitates**: KL(teacher || student) drops from 1.0932 (direct) to 0.9563 (distilled).
- **Temperature helps, modestly here**: T=1 soft-target distillation already beats direct (not the separate hard argmax arm), T=4 adds +0.0250 over T=1. The suite pins the direction and the README says the effect is modest on this fixture.

## Gates

```bash
python -m distilllab gates --min-teacher-acc 0.80 --min-distill-gain 0.04
```

The gates are deterministic regression checks on the primary arms (teacher strength, distillation gain, arm ordering); the control arms are reported as comparisons, not gated. The demo also asserts an impossible gain (0.5) fails.

## Scope

Small synthetic classification, not language-model logit distillation; capacity gaps in production are larger and the hard-label term is often dropped. The gain here is a few accuracy points - a descriptive comparison under controlled synthetic conditions, not a production-scale result. 24 Python tests plus four Node/actual-Chrome tests, fully offline, CI across Python 3.10-3.13.

- Repo: [midya8/distilllab](https://github.com/midya8/distilllab)

## v0.2: one gradient, 254 moving parts

[Live student-update inspector](https://midya8.github.io/distilllab/) · [Equations, schema and numerical limits](https://github.com/midya8/distilllab/blob/main/STEP.md)

Select any original trained student arm or its original initialization, one of the 80 student-training rows, temperature, soft weight and step size. Independent Python and browser evaluators expose hard/soft class derivatives, every simultaneous parameter update, hidden activations, stable CE/entropy/KL terms and all original 80 training/320 test predictions. Full input/report JSON is available. Each entered state starts from its chosen frozen model; test labels never enter the gradient.

A supplied two-hidden-unit control makes the finite-step limitation visible: selected-row loss rises from 1.3466 to 3.6897 at eta=2 although the local directional derivative is negative. This arithmetic counterexample is separate from the original trained models. A lower local loss is not a generalization, calibration, causal-mechanism or deployment guarantee.

24 Python tests retain all original 12 tests. Four Node/actual-Chrome tests check 36 complete native/browser witnesses with 8,900 parameter records and 14,001 evaluation positions. Independent checks include 160 70-digit Decimal logit controls, 80 uniform-class controls, every-parameter finite differences on the original initialization and overshoot network, and 21 original backprop/update states. Installed wheel reproduction rebuilds the original teacher and six student fits, full data/logits/report and all witnesses outside checkout, importing seven modules and running all four commands.

The new inspector uses stable, unclipped logit-space objectives. Original helper functions clamp probabilities at 1e-12 while their gradient formula is the ordinary unclipped derivative; the distinction below that floor is explicit, and original source/training/results are retained. T changes target entropy and objective scale, so loss values across different T do not rank generalization. The wording above narrows older mechanism claims without changing any recorded result: soft-vs-argmax and a single smoothing setting do not isolate causal components. Standard distillation and backpropagation are attributed to six sources in STEP.md, not claimed as a new method.
