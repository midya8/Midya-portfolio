# DistillLab: knowledge distillation from scratch, dark knowledge measured

A small model trained on a teacher's soft outputs often beats the same model trained on hard labels - the classic explanation is "dark knowledge": the teacher's per-sample class-similarity structure. DistillLab implements the whole pipeline in dependency-free Python and, more importantly, designs the experiment so that explanation is tested rather than repeated.

## The fixture

Eight classes arranged on a ring in 32 dimensions: each class center blends its own random unit direction with its predecessor's, so neighboring classes are genuinely similar. The teacher (hidden 64, 2632 params) trains on 100 samples per class. Students (hidden 6, 254 params - about 10x smaller) train on only 10 per class: the low-data regime where distillation is supposed to matter.

## The loss, by hand

```
L = alpha * T^2 * CE(softmax(z_student / T), softmax(z_teacher / T)) + (1 - alpha) * CE(softmax(z_student), onehot)
dL/dz = alpha * T * (p_s^T - p_t^T) + (1 - alpha) * (p_s - onehot)
```

The T^2 prefactor restores the gradient scale that dividing logits by T removes; one factor of T survives the chain rule. Every parameter gradient is finite-difference verified in the test suite.

## Three arms, one variable

Identical seeds, capacity, learning rate, and epoch budget; only the targets differ:

- **direct**: one-hot labels.
- **distill**: teacher soft targets at T=4 blended with the label (alpha=0.95).
- **control**: teacher soft targets for *different, deterministically permuted inputs* - the same marginal distribution of target vectors, zero input-specific information.

## Measured results (checked-in fixture, pinned in tests)

| metric | direct | distilled | control | T=1 ablation |
|---|---|---|---|---|
| test accuracy | 0.6813 | 0.7469 | 0.1250 | 0.7219 |
| train accuracy | 1.0000 | 0.8000 | - | - |

Teacher: 0.8344. Distillation gain: **+0.0656** over direct at identical budget.

- **The control is the point**: it lands at exactly chance (1/8 = 0.125), so the gain is input-specific teacher signal - dark knowledge - not the generic regularization of training on softer labels.
- **The mechanism is visible in the overfit gap**: direct memorizes (train 1.0000, gap 0.3187); distilled does not (train 0.8000, gap 0.0531).
- **The student genuinely imitates**: KL(teacher || student) drops from 1.0932 (direct) to 0.9563 (distilled).
- **Temperature helps, modestly here**: T=1 already beats direct (teacher argmax supervision), T=4 adds +0.0250. The suite pins the direction and the README says the effect is modest on this fixture - no inflated dark-knowledge claims.

## Gates

```bash
python -m distilllab gates --min-teacher-acc 0.80 --min-distill-gain 0.04 --max-control-acc 0.20
```

The control is gated from *above* - it is intentionally corrupted, and if it ever learns, the isolation claim fails with it. The demo also asserts an impossible gain (0.5) fails.

## Scope

Small synthetic classification, not language-model logit distillation; capacity gaps in production are larger and the hard-label term is often dropped. The gain here is a few accuracy points - a demonstration of the mechanism under controlled conditions, not a production-scale result. 11 unit tests, fully offline, CI across Python 3.10-3.13.

- Repo: [midya8/distilllab](https://github.com/midya8/distilllab)
