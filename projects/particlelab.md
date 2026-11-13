# ParticleLab: particle filtering and missing uncertainty

ParticleLab estimates hidden scalar states from noisy observations. It retains the full particle histories so weight concentration, current-state diversity and early ancestry can be checked separately. Exact Kalman and RTS references show approximation errors under the supplied linear model.

[Repository](https://github.com/midya8/particlelab) · [Model and timing](https://github.com/midya8/particlelab#model-and-timing) · [Reviewed documentation](https://github.com/midya8/particlelab/pull/1)

## Equal weights can hide missing states

A particle filter can report equal weights and full effective sample size while carrying duplicate descendants of one badly placed initial particle. Weight ESS measures concentration of weights, not whether the state distribution has enough support.

## Filter and references

- Scalar bootstrap filter with a linear transition and identity or square observation function, known supplied Gaussian noise and a local seeded RNG.
- Log-domain likelihood weighting, adaptive systematic resampling, filtered versus carried summaries, and full particles/weights/log weights/parent mappings/root-label histories.
- Exact scalar linear-Gaussian Kalman reference with an explicit no-transition-at-t0 convention.
- Strict JSON CLI, 114 tests, five reproducible SVGs and CI on Python 3.10..3.13. Standard library only.

No roughening, state rejuvenation or parameter fitting is hidden in the filtering comparison. Separate retrospective genealogy and exact linear RTS commands are now available.

## Fixed development examples

The fixed twelve-point linear example uses 512 particles for all sixteen seeds 0..15. The mean of per-seed mean RMSEs versus the exact Kalman filter is **.0161016904**; the variance RMSE average is **.00794734279**. Seed 0 is plotted without selecting for fit. The example and smoke-check threshold were chosen during development, not held out. These are model-conditional approximation errors, not real-world accuracy or calibration.

A second fixture uses twenty zeros, a=1, process std=0, observation std=.1, initial mean=0/std=3, 32 particles and seed 0. At the end:

| Quantity | Resampling threshold fraction 1 | Resampling disabled | Exact reference |
|---|---:|---:|---:|
| Mean | -.2163600684 | -.2163533277 | 0 |
| Latent variance | 0 | .00000308085 | .000499972224 |
| Weight ESS | 32 | 1.00002950 | not applicable |
| Initial labels carried | 1 | 32 | not applicable |

Full ESS after resampling does not recover missing support. Keeping all labels without resampling is not enough either: almost all weight sits on one. With zero process noise neither method can create a missing state value. This is not a causal claim that resampling alone causes the failure, or a verdict about other proposals or particle budgets.

![Filtering, variance, ESS and ancestry](https://github.com/midya8/particlelab/raw/refs/heads/main/assets/particle-audit.svg)

[Reproducible figure source](https://github.com/midya8/particlelab/blob/main/assets/particle-audit.svg). All plotted means/variances, settings, seed errors and domains are retained in numeric SVG metadata; the polygons retain every moment-band vertex. Shading is mean +/- one SD, not calibrated coverage. Both success and failure checks run in the demo.

## Static square symmetry and sign loss

A restricted static square-observation reference has exact mean 0 and sign probability 1/2, but its modes can be near +/-2 with the mean deep in a density valley. A selected eight-particle run loses one sign while carried ESS is 8/8; the no-resampling comparison also has poor effective support. The analytic reference returns symmetry/modes/density ratios, not variance or evidence. [Derivation, assumptions and complete fixed-seed comparison](https://github.com/midya8/particlelab/blob/main/SYMMETRY.md).

## Retrospective paths and missing early uncertainty

A separate terminal-weighted genealogy smoother traces the retained parent maps, without drawing new paths or using the final resampled weights. The scalar linear RTS reference conditions on the complete observation sequence. A fixed 64-step dynamic fixture ends with 32 distinct current states but only one retained initial path: time-0 particle variance is 0 while exact smoothed variance is .009521314. Current process noise cannot recreate a discarded past path.

All sixteen inherited linear seeds 0..15 are retained; mean-of-seed smoothing mean/variance RMSEs versus RTS are .0299202464/.0137440904. These are development approximation errors, not a smoothing-versus-filtering ranking, independent posterior paths or calibrated coverage. [Index/weight derivation, figure, complete fixed results and limits](https://github.com/midya8/particlelab/blob/main/SMOOTHING.md).

## Backward simulation still depends on finite support

An optional sampler connects retained filtering states outside the parent maps, with separate seeded backward draws and a strict candidate-work cap. On the same fixed fixture, 512 draws reach two initial indices instead of one genealogical path. Their time-0 variance .022290238 is still over twice the exact .009521314. More path diversity is not calibrated uncertainty or recovered state support. Process std below 1e-4 is rejected; the deterministic-transition density is not fabricated. [Algorithm, comparison figure, numerical guards and limits](https://github.com/midya8/particlelab/blob/main/BACKWARD.md).

## Observation-conditioned proposals

An optional linear observation-conditioned Gaussian proposal exposes per-particle proposal moments and predictive importance weights, with exact initial predictive evidence and deterministic q=0 moves. Across all sixteen fixed seeds at N=32 on the inherited sequence, mean RMSE is similar (.082871/.081548 bootstrap/conditional), but conditional variance RMSE is worse (.037895 versus .035944). A more informative observation fixture has smaller conditional errors, not a general or causal ranking. Seed labels do not ensure paired identical random streams. [Derivation, all-seed figure, complete metrics and limits](https://github.com/midya8/particlelab/blob/main/PROPOSAL.md).

## Run it locally

```sh
python -m unittest discover -s tests -v
python -m particlelab demo > /tmp/particle-demo.json
python examples/render_demo.py /tmp/particle-demo.json --check
python -m particlelab filter examples/sequence.json --particles 512 --seed 0
python -m particlelab filter examples/sequence.json --ess-fraction 0
python -m particlelab kalman examples/sequence.json
python -m particlelab filter examples/sequence.json --particles 32 --proposal conditional
python -m particlelab smooth examples/sequence.json --particles 512 --seed 0
python -m particlelab rts examples/sequence.json
python -m particlelab backward examples/sequence.json --particles 32 --draws 512
```

The repository has the complete six-field payload, strict input/resource bounds, CLI options and output semantics. Tests include hand weights/moments/evidence, evidence from full products over static initial samples, revival of log mass after probability underflow, systematic-resampling boundaries/zero bins/offspring, exact Gaussian references, RNG/input isolation, ancestry mappings and all SVG coordinates.

## Reproduction and publication

The documentation review is merged in [PR #1](https://github.com/midya8/particlelab/pull/1), main `06832dbab58fa99e1e0573e904ea645ab07b8e20`. Fresh current, revised, published-head and merged-main checkouts each passed 114 Python tests and five byte-identical SVG regeneration checks. Installed-wheel checks verified seven module origins and ten complete CLI reports outside the checkout, using the same interpreter for the source and installed comparisons. All 43 published and main files matched the reviewed checkout; 41 tracked files were unchanged.

Both [head push checks](https://github.com/midya8/particlelab/actions/runs/43354899826) and [head PR checks](https://github.com/midya8/particlelab/actions/runs/43354953939) passed all five jobs. [Merged-main checks](https://github.com/midya8/particlelab/actions/runs/43355107329) passed five jobs. The main README and proposal derivation were inspected at full height, including figures and result tables. These checks verify implementation consistency, not real-world accuracy or calibrated uncertainty.

## Limits and attribution

A scalar supplied-parameter model, finite particles and floating point. The square branch has an analytic static symmetry/mode reference and a sign-support failure audit, not a dynamic nonlinear tracking benchmark. No convergence certificate, high-dimensional proposal, learned parameters, robustness, anomaly p-values or coverage guarantee. Evidence estimates are random; logs are not unbiased log-evidence estimates. No private or external dataset, paid API or GPU is used.

Independent implementation inspired by Gordon, Salmond and Smith's 1993 bootstrap-filter paper, Section 3. [Primary paper](https://people.bordeaux.inria.fr/pierre.delmoral/gordon-salmond-smith-1993.pdf). Uses its own fixtures and systematic/adaptive ESS resampling, not the paper's bearings-only experiments, roughening, prior editing or performance claims. No code or paper figures copied. Standard retained-history SIR smoothing and scalar RTS are independently implemented with [Särkkä and Svensson (2023), sections 12.2/15.1/15.2](https://users.aalto.fi/~ssarkka/pub/bfs_book_2023_online.pdf) as a technical reference. No source text/code/figures copied. MIT license.
