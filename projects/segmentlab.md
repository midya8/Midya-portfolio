# SegmentLab

**A confident segmentation is not evidence that an event occurred.** SegmentLab is a dependency-free Python implementation of exact offline Bayesian Gaussian changepoint inference. It retains the full finite-partition evidence and marginals, not only one best cut list.

[Repository and runnable examples](https://github.com/midya8/segmentlab) · [Technical reference](https://github.com/midya8/segmentlab/blob/main/DESIGN.md)

## The problem

A single outlier can look like a short, high-confidence segment when the assumed noise is too small. Thresholded marginal peaks also hide whether cuts occur together, and the most probable whole partition need not minimize expected boundary mistakes.

The project makes these distinctions inspectable: model assumptions, prior normalization, the full joint partition law, numerical work and the decision loss remain explicit. It does not label real-world events or claim calibrated cuts.

## What I built

- Conjugate Gaussian interval evidence with centered rolling mean/M2 statistics, avoiding repeated interval rescans.
- Count-capped forward/backward log sums, explicitly normalized admissible Bernoulli-gap priors, all interval/boundary/count marginals and complete MAP backtrace.
- Pointwise latent-mean uncertainty including within-segment and between-partition components, excluding future observation noise.
- Seeded complete-partition backward draws plus conditional Gaussian segment means, with finite-RNG limits stated.
- Exact requested-pair cut inclusion queries that allow other cuts, finite log probabilities and distinct impossible-event/undefined-conditional flags.
- Full discrete partition entropy, conditioned-prior KL and dependence of the entire cut vector, rather than an independent-cut entropy shortcut.
- Constrained minimum expected false/missed boundary-loss decisions, with MAP and infeasible-threshold comparisons kept separate.
- Strict JSON commands,104 tests, independent exhaustive tiny references and two regenerable SVGs with all plotted values retained.

## Selected results, and what they mean

| Development example | Result | Interpretation |
|---|---|---|
| Same isolated outlier, two supplied noise scales | sigma.15: MAP `[12,13]`, probability.960218; sigma2: MAP `[]`, probability.648223 | Model confidence can isolate contamination; this is not a noise-model quality ranking |
| Six zeros, count cap2 | cuts2/4 each have marginal mass.011658220257; joint mass0 | Multiplying marginals invents a structurally forbidden event |
| Selected seven-point decision fixture | no-cut boundary-risk optimum.680000591; MAP `[3]` risk.869071786 | MAP and additive-boundary loss answer different questions; neither number is observed accuracy |
| Four-point uncertainty fixture | posterior entropy1.029013408 > prior entropy.836308115; KL.166962288 | KL is not prior entropy minus posterior entropy |
|10,000 joint draws, seed19 | K4 has exact mass.000115427 and zero sampled visits | Zero visits do not imply zero posterior mass |

Every input, setting, fixture-selection provenance, conditional direction and raw numerical qualification is preserved in the [technical reference](https://github.com/midya8/segmentlab/blob/main/DESIGN.md) and runnable audit JSON. These are selected development cases, not untouched-test performance, causal effects or real-data calibration.

[Known-shift and noise-assumption figure](https://github.com/midya8/segmentlab/blob/main/assets/partition-audit.svg) · [Complete-path versus marginal-average figure](https://github.com/midya8/segmentlab/blob/main/assets/joint-draw-audit.svg)

## Same-design replicate mixtures

New replicate observations integrate partition and segment-mean uncertainty, then add fresh noise. In a selected five-point outlier fixture, a moment-matched Gaussian overstates density at2 by1.54 nats. This is a shape comparison using all fitted observations, not forecasting, leave-one-out evaluation, anomaly p-values or calibrated coverage. The [technical reference](https://github.com/midya8/segmentlab/blob/main/DESIGN.md#same-design-replicate-predictive-mixtures) preserves inputs, two-prior results and quantile residuals.

## Run it locally

```sh
python -m unittest discover -s tests -v
python -m segmentlab --help
python -m segmentlab infer examples/sequence.json
python -m segmentlab sample examples/sequence.json --draws 4 --seed 23
python -m segmentlab joint examples/sequence.json --pairs '[[1,3],[2,4]]'
python -m segmentlab information examples/sequence.json
python -m segmentlab decide examples/sequence.json --false-cut-cost 1 --missed-cut-cost 1
python -m segmentlab predictive examples/sequence.json --queries '[[2,0.0],[3,1.0]]'
```

The repo README has the complete seven-field example payload and reproducible audit commands. Model commands share a strict schema; Python APIs also offer defaults. CLI options and errors are tested. CI uses Python3.10..3.13 and byte-checks both generated figures.

## Design choices and limits

All observations in a segment are conditionally independent Normal(mean,sigma²), with supplied known sigma and independent Normal mean priors. The Bernoulli interior-gap prior is conditioned on minimum segment length and count cap; its normalizer is included in evidence. Means are integrated out for the discrete partition law. No prior or noise hyperparameter is learned.

Inference is offline: future observations inform earlier cuts and means. Full marginals use `O(N²*K²)` work, bounded to120 observations and12 requested segments; feature-specific work and output bounds are documented. Results are finite sums in floating point, not symbolic arithmetic or formal numerical certificates. Tiny masses can underflow and finite arithmetic can affect near ties.

No online alert, forecast, credible-band coverage, robust-outlier model, event attribution, causality or model-misspecification guarantee is claimed. Relative decision costs are supplied loss units, not money. Lower entropy, higher KL and lower chosen-loss risk do not establish real-world correctness.

Independent implementation inspired by Fearnhead's independent-segment recursions, with a different explicit conditioned prior/count recurrence. No copied code, reproduced paper experiments, pruning or paper-sampler replication. Attribution and derivations remain in the linked reference. MIT licensed.
