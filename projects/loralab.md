# LoRALab: same model, different factor-SGD step

[Interactive inspector](https://midya8.github.io/loralab/) · [Source and reproduction](https://github.com/midya8/loralab)

LoRALab implements low-rank adaptation in dependency-free Python, then exposes a less obvious distinction: equivalent factor coordinates can represent the same model but take different ordinary SGD steps. The browser and Python evaluators are independent. This is an arithmetic diagnostic on a synthetic classifier, not a new optimizer or an LLM benchmark.

## Change coordinates, not the experiment

For a frozen base and factors, `W' = W + BA`. An invertible change `B' = BC`, `A' = C^-1 A` preserves `BA` in real arithmetic. Ordinary Euclidean factor SGD is invariant to orthogonal changes of basis, but general scaling and shear need not preserve its next merged model.

The inspector computes full logits, probabilities, factor gradients and before/after matrices. It retains the finite-step second-order term:

`delta(BA) = -eta_A BB^T G - eta_B GA^T A + eta_A eta_B G(BA)^T G`

For scalar `C = cI`, the compensated rates `eta_A' = eta/c^2` and `eta_B' = eta*c^2` reproduce the original next merged model in real arithmetic. This is a coordinate identity, not a recommendation to use one scale or a proposed optimizer. The page shows all 31 sampled scales, including worse steps, rather than selecting a winner.

At original width 2, epoch 30, the first training example, learning rate 0.1 and scale 4, before-step logit residual is 0. The ordinary next-matrix difference is 0.0056767304; scalar compensation gives residual 0 in this binary64 calculation. These are descriptive residuals, not numerical certificates or causal explanations of retention.

## Every original epoch boundary stays attached

All 31 epoch boundaries at widths 1, 2, 4 and 8 remain inspectable: 124 states with full factors, norms, online-update counts and train/test metrics. These are not all 14,400 individual online updates. The diagnostic first-example or mean-batch step is not a retrained original online epoch. Custom finite-classifier JSON and full matrix gauges are supported with strict shape, finite-value and operational inversion bounds. Inputs, complete reports and the full archive can be downloaded.

## Original results, including adverse retention

The unchanged seeded hashed-bag-of-words classifier has three outputs and 128 features. A disjoint-vocabulary shift lowers base B accuracy from A accuracy 1.0000 to B accuracy 0.4444.

| Original method | B accuracy | A retention | Trainable parameters | Share of full baseline |
|---|---:|---:|---:|---:|
| No adaptation | 0.4444 | 1.0000 | 0 additional | - |
| Factor width 1 | 0.9333 | 0.7333 | 131 | 33.9% |
| Factor width 2 | 1.0000 | 0.7556 | 262 | 67.7% |
| Factor width 4 | 1.0000 | 0.7778 | 524 | 135.4% |
| Factor width 8 | 1.0000 | 0.7778 | 1048 | 270.8% |
| Full fine-tuning | 1.0000 | 0.9556 | 387 | 100.0% |

Width 2 matches full fine-tuning's B accuracy with 67.7% of its trainable parameters, but retains less A accuracy: 0.7556 versus 0.9556. Widths 4 and 8 cost more parameters than the full baseline. Factor width is not measured matrix rank: three output rows cap `rank(BA)` at three. Adapters freeze the base bias; the original full baseline trains it. These original design choices and results are preserved, not normalized away.

The original merge-back check still measures a nonzero maximum logit difference of about 1.07e-14, below its unchanged 1e-12 gate. Exact algebra does not imply exact floating-point reassociation.

## Verification and installed reproduction

- 31 Python tests across Python 3.10-3.13, including all 14 unchanged original tests, finite differences of every factor coordinate, randomized controls and independent 80-digit Decimal finite-step checks.
- Four Node/actual-Chrome tests compare 54 complete reports containing 591,615 numeric values, all retained states, full matrix controls, strict invalid-state behavior, keyboard, report/input/archive exports and responsive layouts.
- An isolated installed wheel imports all eight implementation modules, exercises all four commands and reconstructs the original data, base, factors, states and report outside the source checkout. Frozen reports use 1e-12 comparison tolerance; original retraining across runtimes allows 1e-11 for libm differences. Original gates are unchanged.
- Seven CI jobs cover four Python versions, the original demo, browser checks and installed-package reproduction.

## Limits and attribution

Synthetic hashed bag-of-words discards token order and can collide. The diagnostic uses true stable mean cross-entropy; original training logs add 1e-12 inside the probability logarithm. Neither finite-case equality nor an operational inverse estimate is an outward-rounded certificate, convergence guarantee or deployment-quality result. There is no claim about transformers, Adam, unseen tasks or the cause of retention loss.

Standard identities are attributed to [LoRA](https://arxiv.org/html/2106.09685v2) and [fixed-rank factorization geometry](https://arxiv.org/html/1209.0430v2). [LoRA+](https://arxiv.org/html/2402.12354) and LoRA-RITE provide context; neither optimizer is implemented here. Full derivations, schemas and scope are in `COORDINATES.md` in the source.
