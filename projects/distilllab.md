# DistillLab: knowledge distillation from scratch, the gain decomposed

A small model trained on a teacher's soft outputs often beats the same model trained on hard labels - the classic explanation is "dark knowledge": the teacher's per-sample class-similarity structure. DistillLab implements the whole pipeline in dependency-free Python and, more importantly, decomposes the measured gain with matched control arms instead of repeating the explanation: pseudo-labels isolate the teacher's own predictions, a uniform-smoothing arm rules out input-independent softening, and a permuted-target control rules out input-mismatched teacher signal.

## The fixture

Eight classes arranged on a ring in 32 dimensions: each class center blends its own random unit direction with its predecessor's, so neighboring classes are genuinely similar. The teacher (hidden 64, 2632 params) trains on 100 samples per class. Students (hidden 6, 254 params - about 10x smaller) train on only 10 per class: the low-data regime where distillation is supposed to matter.

## The loss, by hand

```
L = alpha * T^2 * CE(softmax(z_student / T), softmax(z_teacher / T)) + (1 - alpha) * CE(softmax(z_student), onehot)
dL/dz = alpha * T * (p_s^T - p_t^T) + (1 - alpha) * (p_s - onehot)
```

The T^2 prefactor restores the gradient scale that dividing logits by T removes; one factor of T survives the chain rule. Every parameter gradient is finite-difference verified in the test suite.

## Five arms, one variable

Identical seeds, capacity, learning rate, and epoch budget; only the targets differ:

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

Teacher: 0.8344. Distillation gain: **+0.0656** over direct at identical budget, decomposed on this fixture:

- **Teacher-signal component: +0.0281** (pseudo-labels minus direct) - the teacher's own predictions already carry input-specific value.
- **Dark-knowledge component: +0.0375** (distilled minus pseudo-labels) - the non-target-class distribution content beyond those predictions, which is what the term dark knowledge refers to. The suite pins both components from below as fixture regression.
- **Not smoothing**: uniform label smoothing scores 0.6781, at or below direct - input-independent softening is not the mechanism.
- **Not input-mismatched signal**: the permuted-target control sits at exactly chance (1/8 = 0.1250). Reported, not gated: it is a comparison between matched arms, and if it ever moved the README numbers would move with it.
- **The mechanism is visible in the overfit gap**: direct memorizes (train 1.0000, gap 0.3187); distilled does not (train 0.8000, gap 0.0531).
- **The student genuinely imitates**: KL(teacher || student) drops from 1.0932 (direct) to 0.9563 (distilled).
- **Temperature helps, modestly here**: T=1 already beats direct (teacher argmax supervision), T=4 adds +0.0250 over T=1. The suite pins the direction and the README says the effect is modest on this fixture.

## Gates

```bash
python -m distilllab gates --min-teacher-acc 0.80 --min-distill-gain 0.04
```

The gates are deterministic regression checks on the primary arms (teacher strength, distillation gain, the two gain components); the control arms are reported as comparisons, not gated. The demo also asserts an impossible gain (0.5) fails.

## Scope

Small synthetic classification, not language-model logit distillation; capacity gaps in production are larger and the hard-label term is often dropped. The gain here is a few accuracy points - a demonstration of the mechanism under controlled conditions, not a production-scale result. 12 unit tests, fully offline, CI across Python 3.10-3.13.

- Repo: [midya8/distilllab](https://github.com/midya8/distilllab)
