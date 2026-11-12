# LoRALab

[Interactive inspector](https://midya8.github.io/loralab/) · [Source and reproduction](https://github.com/midya8/loralab)

LoRALab separates factor width, matrix rank, all-input softmax-equivalent rank and finite-probe agreement with exact rational factors, nonzero minors and independent verification. The original factor-coordinate SGD inspector and all 124 archived states remain intact. This is a linear-classifier audit, not a new algorithm, rounded-runtime certificate or LLM benchmark.

## Exact predictive rank, with witnesses

A separate exact-rational inspector distinguishes supplied width, matrix rank, the least rank of an all-input softmax-equivalent update, and finite-probe rank. For a fixed linear output map and bias, the all-input minimum is the rank of its class-row differences. Constructive factors prove the upper bound; a nonzero minor proves the matching lower bound. An independent native Bareiss verifier never calls the rank producer, and browser BigInt decodes the original binary64 factors as exact represented ratios.

All 124 original states remain attached. At every nonzero epoch, widths 4/8 have exact product rank 3 and class-difference rank 2; widths 1/2 retain ranks 1/2. Fewer algebraic scalar slots do not prove lower rational storage, runtime memory, inference speed or retained accuracy. Original training still used 524/1048 parameters at widths 4/8.

Finite-probe minimum rank is rank(D X^T), with an attaining extension, an explicit unseen-coordinate counterexample when it differs globally, and a nonzero probe-nullspace direction whenever probes fail to span feature space. Even a canonical extension that happens to equal D cannot make non-spanning probes complete.

Python, Node and actual-Chrome tests compare full native/browser reports at every archived boundary, reject altered factors and minors, and replay downloaded certificates through the independent native verifier. Exact controls include finite-probe blind directions and exhaustive small-matrix/minor checks. Both installed-wheel checks reproduce outside the source checkout. Exact arithmetic certifies a real probability function only; rounded probabilities, argmax, loss, future factor training and hidden layers are outside scope. Exact rank is not tolerance-based numerical rank.

[Exact inspector](https://midya8.github.io/loralab/rank.html) · [Proof, schema and reproduction](https://github.com/midya8/loralab/blob/main/PREDICTIVE_RANK.md). Standard softmax equivalence and rank facts are attributed to [Yang et al.](https://arxiv.org/abs/1711.03953), [LoRA](https://arxiv.org/abs/2106.09685) and [Nick Higham](https://nhigham.com/2021/02/23/matrix-rank-relations/), not presented as a new algorithm.

## Factor-coordinate updates

For a frozen base and factors, `W' = W + BA`. An invertible change `B' = BC`, `A' = C^-1 A` preserves `BA` in real arithmetic. Ordinary Euclidean factor SGD is invariant to orthogonal changes of basis, but general scaling and shear need not preserve its next merged model.

The inspector computes full logits, probabilities, factor gradients and before/after matrices. It retains the finite-step second-order term:

`delta(BA) = -eta_A BB^T G - eta_B GA^T A + eta_A eta_B G(BA)^T G`

For scalar `C = cI`, the compensated rates `eta_A' = eta/c^2` and `eta_B' = eta*c^2` reproduce the original next merged model in real arithmetic. This is a coordinate identity, not a recommendation to use one scale or a proposed optimizer. The page shows all 31 sampled scales, including worse steps, rather than selecting a winner.

At original width 2, epoch 30, the first training example, learning rate 0.1 and scale 4, before-step logit residual is 0. The ordinary next-matrix difference is 0.0056767304; scalar compensation gives residual 0 in this binary64 calculation. These are descriptive residuals, not numerical certificates or causal explanations of retention.

## Archived epoch boundaries

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

Width 2 matches full fine-tuning's B accuracy with 67.7% of its trainable parameters, but retains less A accuracy: 0.7556 versus 0.9556. Widths 4 and 8 cost more parameters than the full baseline. Factor width is not measured matrix rank: three output rows cap `rank(BA)` at three. Adapters freeze the base bias; the original full baseline trains it. The comparison keeps these original design choices.

The original merge-back check still measures a nonzero maximum logit difference of about 1.07e-14, below its unchanged 1e-12 gate. Exact algebra does not imply exact floating-point reassociation.

## Verification and installed reproduction

The Python checks cover training, finite differences of factor coordinates, randomized controls and independent 80-digit Decimal finite-step checks. Browser checks compare complete reports, strict invalid-state behavior, keyboard input, exports and responsive layouts. Original retraining across runtimes allows 1e-11 for libm differences; frozen reports use 1e-12. The original accuracy, retention, parameter and merge gates are unchanged.

From a source checkout:

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install .
python -m unittest discover -s tests
bash examples/demo.sh
node --test tests/test_coordinates.cjs tests/test_coordinates_browser.cjs \
    tests/test_rank.cjs tests/test_rank_browser.cjs
bash examples/verify_wheel.sh
bash examples/verify_rank_wheel.sh
```

The wheel scripts install into temporary environments and check packaged data, commands, original states and independent certificates outside the checkout. Web checks need Node 22+ and Chrome.

## Limits and attribution

Synthetic hashed bag-of-words discards token order and can collide. The diagnostic uses true stable mean cross-entropy; original training logs add 1e-12 inside the probability logarithm. Neither finite-case equality nor an operational inverse estimate is an outward-rounded certificate, convergence guarantee or deployment-quality result. There is no claim about transformers, Adam, unseen tasks or the cause of retention loss.

Standard identities are attributed to [LoRA](https://arxiv.org/html/2106.09685v2) and [fixed-rank factorization geometry](https://arxiv.org/html/1209.0430v2). [LoRA+](https://arxiv.org/html/2402.12354) and LoRA-RITE provide context; neither optimizer is implemented here. Full derivations, schemas and scope are in `COORDINATES.md` in the source.
