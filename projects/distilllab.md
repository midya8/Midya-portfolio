# DistillLab: compare student training, then inspect the gradients

DistillLab trains a teacher and smaller students in dependency-free Python, then opens up their gradients in two browser inspectors. On its synthetic fixture, the distilled student scores 0.7469 test accuracy, versus 0.6813 for direct labels and 0.7094 for teacher argmax labels. These are matched-arm results, not proof of what caused the difference.

## Where to start

| Question | Open or run | What to keep in mind |
| --- | --- | --- |
| How do the original training arms compare? | `evaluate`, `gates` | One synthetic fixture; the comparisons do not identify a causal mechanism |
| What happens in one student update? | [Step inspector](https://midya8.github.io/distilllab/) | Every parameter moves simultaneously from the same selected model |
| Can the same teacher confidence give different gradients? | [Target/rest inspector](https://midya8.github.io/distilllab/tail.html) | Four fixed-mass tail variants, not DKD training or a new trained arm |
| Can I replay a report outside the checkout? | `step-audit`, `distilllab-tail` | Native report checks and isolated-wheel reproduction |

The current suite has 36 Python tests and seven substantive Node/real-Chrome tests (eight runner entries including a helper). Counts below label the earlier retained release stages.

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

Small synthetic classification, not language-model logit distillation; capacity gaps in production are larger and the hard-label term is often dropped. The gain here is a few accuracy points - a descriptive comparison under controlled synthetic conditions, not a production-scale result. The earlier step-inspector release had 24 Python tests and four Node/actual-Chrome tests, fully offline, with CI across Python 3.10-3.13.

- Repo: [midya8/distilllab](https://github.com/midya8/distilllab)

## Follow one student update

[Live student-update inspector](https://midya8.github.io/distilllab/) · [Equations, schema and numerical limits](https://github.com/midya8/distilllab/blob/main/STEP.md)

Select any original trained student arm or its original initialization, one of the 80 student-training rows, temperature, soft weight and step size. Independent Python and browser evaluators expose hard/soft class derivatives, every simultaneous parameter update, hidden activations, stable CE/entropy/KL terms and all original 80 training/320 test predictions. Full input/report JSON is available. Each entered state starts from its chosen frozen model; test labels never enter the gradient.

A supplied two-hidden-unit control makes the finite-step limitation visible: selected-row loss rises from 1.3466 to 3.6897 at eta=2 although the local directional derivative is negative. This arithmetic counterexample is separate from the original trained models. A lower local loss is not a generalization, calibration, causal-mechanism or deployment guarantee.

24 Python tests retain all original 12 tests. Four Node/actual-Chrome tests check 36 complete native/browser witnesses with 8,900 parameter records and 14,001 evaluation positions. Independent checks include 160 70-digit Decimal logit controls, 80 uniform-class controls, every-parameter finite differences on the original initialization and overshoot network, and 21 original backprop/update states. Installed wheel reproduction rebuilds the original teacher and six student fits, full data/logits/report and all witnesses outside checkout, importing seven modules and running all four commands.

The new inspector uses stable, unclipped logit-space objectives. Original helper functions clamp probabilities at 1e-12 while their gradient formula is the ordinary unclipped derivative; the distinction below that floor is explicit, and original source/training/results are retained. T changes target entropy and objective scale, so loss values across different T do not rank generalization. The wording above narrows older mechanism claims without changing any recorded result: soft-vs-argmax and a single smoothing setting do not isolate causal components. Standard distillation and backpropagation are attributed to six sources in STEP.md, not claimed as a new method.


## Keep the confidence, change the tail

[Target/rest workbench](https://midya8.github.io/distilllab/tail.html) · [Equations and replay contract](https://github.com/midya8/distilllab/blob/main/TAIL.md)

The same supplied-label teacher target probability can produce different student gradients. The new workbench audits the established KL chain rule: binary target/rest KL plus teacher rest mass times conditional-tail KL. Four independent one-step variants keep target/rest mass at the selected temperature: original tail, uniform tail, a one-class cyclic rotation and a configured rotation/uniform mix. All begin from the same original student. Rotation preserves entropy in exact arithmetic, not class meaning or temperature-1 confidence. The target is the supplied training label, not necessarily the teacher's argmax.

Python computes analytic MLP backprop. The browser independently differentiates scalar tanh/logits/subset-logsumexp operations through reverse-mode automatic differentiation. Every class derivative, hard/binary/coupled-tail parameter component, full-class cross-check, simultaneous update and raw residual stays visible. Own-teacher and original-teacher KL changes use their respective correct before baselines. CE and KL differ by a fixed-teacher entropy offset, which can change between tail variants. True excluded-class normalization avoids both a finite minus-1000 mask and subtracting a rounded target probability from one. Saturation and underflow are exposed, not clamped into a proof.

36 Python tests retain all 24 earlier tests. Seven substantive Node/Chrome tests (eight runner entries) check 28 full witnesses, 112 variants, 21,724 parameter positions and 286,603 cross-runtime numeric fields. Independent checks include 2,368 centered finite-difference component checks, 40 80-digit Decimal controls, all seven archived states across all 80 training rows and 336 separately altered report leaves. Actual Chrome checks 84 input/width layouts, 24,012 class cells, 521,376 parameter cells, 65,172 coordinate selections and six completed downloads; three downloaded archives replay natively. Three further rightmost-scroll captures check narrow table access.

Installed wheels outside checkout check nine module origins, exact witness regeneration, both new CLI entrypoints, 56 valid archive replays and 56 rejected forgeries. The unchanged original wheel reproduction still rebuilds teacher/six student fits, all data/logits/report, 36 earlier witnesses and all four original commands. Bounded input and full report/replay schemas reject unknown fields, duplicate keys, nonfinite values and malformed shapes.

The decomposition is established work attributed to Zhao et al. (CVPR 2022) and standard KL algebra, not a new method. This is not a DKD training reproduction, held-out evidence or a causal explanation of the original accuracy gain. It adds no trained arm, test-label gradient or selected hyperparameter. All original trainer/model/data/report results and the earlier inspector remain attached and unchanged.
