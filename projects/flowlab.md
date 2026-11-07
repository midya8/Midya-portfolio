# FlowLab: exact model density is not an exact fit

Affine-coupling normalizing flow from scratch: exact 2-D model log density, explicit inverse sampling, bounded log scales and handwritten likelihood gradients. A 200-parameter flow gives test NLL2.188408 on a disclosed banana-shaped development fixture, vs train-fitted full-covariance Gaussian2.907770 and untrained flow2.896854; known generating density2.151426 is report-only. Test roundtrip/logdet residual max1.78e-15 is an implementation audit, not a global error bound. Sample residuals/outliers remain visible. 29 tests, strict artifacts and offline train/score/gradient/sample CLI. No exact-fit, image, anomaly-detection or general ranking claim.

[Source repository](https://github.com/midya8/flowlab) · [Design contracts](https://github.com/midya8/flowlab/blob/main/DESIGN.md)

![Shared-axis density and sample audit](https://raw.githubusercontent.com/midya8/flowlab/main/assets/flow-audit.svg)

## Why this project

Invertible layers let one model score observed data and generate samples with the same weights. This project makes the Jacobian sign, inverse arithmetic, train-only baseline and gap to the known generator inspectable. Exact likelihood computation describes the fitted model, not the unknown data distribution.

## Model and numerical contract

Four alternating affine-coupling layers map data x to standard-normal latent z. Each layer keeps one coordinate a and transforms the other b:

```
y_a = x_a
y_b = x_b * exp(s(x_a)) + t(x_a)
log_abs_det = s(x_a)
x_b = (y_b - t(y_a)) * exp(-s(y_a))
log p_X(x) = log p_Z(f(x)) + sum(log_abs_det)
```

A shared 1 -> tanh(12) -> 2 conditioner produces raw scale and shift. Scale is bounded as `tanh(raw_scale)` by default; translations and data are not clipped. Masks alternate which coordinate is held fixed. The demo has 200 learned parameters, manual backpropagation and minibatch Adam. Sampling draws standard-normal latents and applies inverse layers in reverse order, returning samples from the **fitted model**, not guaranteed samples from the true distribution.

The log density is the analytic change-of-variables density of this invertible model, evaluated with ordinary floating-point arithmetic. "Exact" does not mean an exact fit, exact arithmetic, globally optimized training or certified numerical accuracy for arbitrary extreme inputs. Nonfinite states/densities fail rather than being clipped. [DESIGN.md](https://github.com/midya8/flowlab/blob/main/DESIGN.md) spells out gradients, schema, bounds and limitations.

## Measured development fixture

Independent u,v ~ N(0,1), then `x=u`, `y=0.5*v+0.6*(u*u-1)`. This is a smooth banana-shaped density with a known reference likelihood. 1,024 training points (seed53), 512 fresh test points (seed59); flow seed11, training-draw seed12, 2,000 updates, batch32, learning rate0.003. Final checkpoint, no validation or test-based selection. No architecture, schedule or seed sweep was run. The data and outputs were inspected during development, so this is not an untouched benchmark.

| Density | Train NLL, nats/2-D point | Test NLL, nats/2-D point |
| --- | ---: | ---: |
| Trained flow | 2.146052 | 2.188408 |
| Same untrained flow | 2.811894 | 2.896854 |
| Train-fitted full-covariance Gaussian | 2.808904 | 2.907770 |
| Known generating density, report-only reference | 2.136111 | 2.151426 |

The Gaussian fits both means and the complete 2x2 maximum-likelihood covariance on training data only. It is not an intentionally unfit standard-normal control. The untrained flow uses the same initial parameters. These are descriptive fixture comparisons, not a causal decomposition or a general model ranking.

All 256-sample arms use sample seed19 except the fresh generator reference (seed61). Trained/generated curve-residual second moments are **0.293054 / 0.244743**; untrained/Gaussian are **1.720324 / 1.714797**. Fractions with absolute residual <=1 are **91.41% / 93.36% / 55.86% / 55.86%** in that order. The known population residual second moment is 0.25. These are sample summaries, not calibrated probability coverage or a full distribution test. Raw points and means are in demo JSON.

Across 512 test points, the maximum forward/inverse reconstruction or opposing-logdet residual is **1.7763568394002505e-15** on the development run. That is an implementation audit on those inputs, not a global error bound. The trained model remains worse than the known generating density on this test set; likelihood fidelity and sample fidelity are different checks.

## Audits

29 tests include every parameter of tiny one/two/three-layer flows by central finite differences, an independent finite-difference full Jacobian determinant, both inverse directions, constant-affine density, logdet sign, standard-normal identity, midpoint density integration of a small near-identity model, strict serialization, bounds, no mutation and CLI. The quadrature test is a finite-grid sanity check, not a general normalization proof; the bijective change-of-variables construction supplies the model's mathematical normalization.

CI tests Python3.10-3.13, trains the actual fixture and checks both reproduced SVGs on3.11. Figures use shared axes and expose outside-plot counts rather than silently dropping outliers.

## Limits

Only continuous 2-D points, 1-8 layers and hidden width1-32. No image model, dequantization, multiscale architecture, batch normalization, residual conditioner, classifier, out-of-distribution detector or production guarantee. Bounded scales limit per-layer dilation but do not bound translation, all input derivatives or every composite condition number. Artifacts save inference weights/settings, not optimizer state, and do not support exact training resume. No privacy or anomaly-detection claim. Density values may exceed1; densities are not discrete point probabilities and NLL units depend on coordinate units.

## Source credit

Independent educational implementation of **Dinh, Sohl-Dickstein and Bengio (2017), [Density estimation using Real NVP](https://arxiv.org/pdf/1605.08803v3.pdf)**, especially change of variables Eq.2-3, affine coupling/inverse Eq.4-9 and alternating couplings Section3.5. Source read for mathematics; no copied code or pretrained weights. The paper's image architecture and benchmark results are not reproduced here.

MIT license.

## Reproduce

```sh
python -m unittest discover -s tests -v
python -m flowlab demo > /tmp/flow-demo.json
python examples/render_demo.py /tmp/flow-demo.json --check
python examples/render_score.py /tmp/flow-demo.json --check
```

The train/score/gradient/sample CLI accepts bounded continuous 2-D data. No external runtime dependency or network access is needed.

## Score vectors: the base term is not enough

![Shared-scale input gradient decomposition](https://raw.githubusercontent.com/midya8/flowlab/main/assets/score-audit.svg)

The new `gradient` CLI and `Flow.input_score` API return fitted log density, the full input score, normal-base pullback and log-Jacobian gradient. For `log p_X=log p_Z(f(x))+L(x)`, the full score is `J_f^T(-f(x))+grad L`. With fixed trained weights on a fixed9x9 grid (x=-2..2,y=-1..3,spacing.5), central differences at epsilon1e-5 give max coordinate error **1.1904095487125232e-9**. Omitting the volume term raises the max coordinate discrepancy to **0.6605454933292365**. Both gates run in the demo; all original training, likelihood and sample outputs are unchanged.

The figure uses the same axes and vector gain across all components, with a disclosed length cap and capped counts; raw vectors and finite-difference values remain in JSON. Tests check both coordinates and both components across1/2/3/8 layers plus independent standard-normal, constant-affine and variable-scale formulas. CLI accepts1-256 rows and rejects nonfinite vectors.

These are implementation audits, not global error bounds, feature importance, causal effects or a comparison of learning mechanisms. A score vector is the local derivative of fitted log density in these coordinate units, not a probability or an out-of-distribution detector. No gradient-ascent trajectories, mode finder or score-based sampler is claimed. Likelihood gradients and true data quality remain different questions.
