# DenoiseLab: reconstruct pixels, then inspect the edits

DenoiseLab reconstructs hidden pixels in small UCI digit images with manual NumPy backpropagation. It compares the network with PCA and nearest-neighbor controls that use only visible values. Independent scalar JavaScript runs the same models in the browser, without an API or pretrained weights.

The controls matter. At 16 scattered missing pixels, PCA and nearest neighbor both beat the network on the original test set. At 32 missing pixels, the network has lower measured error. At 48, the three are close. The table below keeps every result visible rather than presenting one mask as a general ranking.

## Choose an inspector

| Question | Live page | What it checks |
| --- | --- | --- |
| What is reconstructed from this mask? | [Reconstruction](https://midya8.github.io/denoiselab/) | Neural, PCA, neighbor and mean predictions |
| Does a local derivative predict a finite edit? | [Input response](https://midya8.github.io/denoiselab/response.html) | Actual edits, neural/PCA Jacobians and residuals |
| Where does the nearest neighbor switch? | [One-pixel path](https://midya8.github.io/denoiselab/path.html) | Exact rational intervals and endpoint ties |
| Which neighbor wins when two values move? | [Two-pixel cells](https://midya8.github.io/denoiselab/plane.html) | Exact area, segment, point and empty cells |

The edit inspectors use the original fits. They do not improve test scores or make a fixed coordinate slice a general robustness guarantee. The two-pixel map retains all 3,062 original fitting-row coefficients. A separate source-matched verifier checks supporting halfplanes, maximal lower-dimensional cells and empty-cell infeasibility proofs without rerunning clipping. Boundary queries check every original row and retain complete ties. [Geometry, proof and limits](https://github.com/midya8/denoiselab/blob/main/PLANE.md).

The current checks pass 52 Python and fourteen Node/real-Chrome tests. Geometry checks include independent boundary-pair enumeration of 238 small-source cells and 2,110 rational queries, forty cross-language maps, 160 browser queries and 30,720 actual canvas colors. Installed reproduction covers ten modules, nine commands and the full refit/evaluation. Exact rational ties and binary64 inference have different numerical contracts.

## Measured official test audit

Mean squared error **only on missing pixels**, averaged across all 1,797
original test digits. Pixel units are normalized from [0,16] to [0,1]. All
methods copy visible pixels unchanged; scoring all pixels would dilute the
error by the missing fraction.

| Pattern | Neural | PCA ridge | Neighbor | Pixel mean |
|---|---:|---:|---:|---:|
| 16 scattered pixels | 0.0353774 | 0.0317004 | 0.0312412 | 0.0727401 |
| 32 scattered pixels | 0.0340515 | 0.0410443 | 0.0363968 | 0.0735652 |
| 48 scattered pixels | 0.0546866 | 0.0547961 | 0.0549125 | 0.0733333 |
| 4-by-4 block / 16 pixels | 0.0649021 | 0.0723497 | 0.0650337 | 0.1011151 |

The training corruption hides exactly 32 randomly selected pixels per image,
refreshed on every presentation. All four evaluation patterns were fixed before
the test loader ran. Different counts and blocks are disclosed shifts, not
post-test tuning. One seed and one mask per image/case; no repeated-sample
confidence interval, robust recovery certificate or causal geometry claim.

## Models and protocol

- Official UCI 3,823 training / 1,797 test split stays intact. A deterministic
  class-stratified feature-hash split yields 3,062 fitting / 761 validation rows.
  No exact feature duplicates cross partitions; near duplicates are not excluded.
- Network input: 64 erased values plus 64 missing flags. Tanh widths 64, 16,
  64, then 64 sigmoid outputs. **14,544 learned parameters**. All derivatives
  are written out, including hidden-only MSE and weight L2. Adam is explicit.
- Epoch candidates 10, 30, 60; minimum validation hidden-pixel MSE selects 60.
  Validation error falls from 0.1797185 at initialization to 0.0320862.
- PCA fits mean/SVD basis using only fitting rows. Rank 8/16/32 and ridge
  .001/.01/.1/1 are selected on the same validation masks. Rank 16, ridge .1
  wins, also the bottleneck-rank-matched control. Inference solves coefficients
  from **observed coordinates only**, with ridge and output clipping. It is not
  a deliberately weak zero-filled orthogonal projection.
- Nearest neighbor uses squared error on visible pixels only, lowest fitting
  index on ties. Labels are used for the split, never fitting or prediction.
- Selected models, complete selection history, immutable evaluation plan,
  original source hashes, every per-image test score and first-ten predictions
  are saved as finite JSON. No pickle.

[Protocol, equations and sources](https://github.com/midya8/denoiselab/blob/main/METHOD.md) gives equations, derivatives, seeds, provenance,
floating-point scope and limits. The denoising objective follows established
Vincent et al. work, not a new algorithm. No source experiment is claimed as
reproduced.

## Run offline

Python 3.10+, NumPy 2.2.6. No other runtime dependency.

```sh
pip install -e .
python -m denoiselab demo > /tmp/denoise-report.json
python -m denoiselab train --output /tmp/denoise-refit
python -m denoiselab evaluate --output /tmp/denoise-refit
python -m denoiselab predict --model denoiselab/artifacts/network.json --input examples/predict.json
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -m unittest discover -s tests -v
python examples/export_browser.py --check
python examples/render_audit.py --check
node --test tests/*.cjs
bash examples/demo.sh
```

`demo` reads the full saved report. `train` never loads test rows. `evaluate`
checks selected model/protocol/plan hashes before loading test data. `predict`
erases hidden positions before inference even if the supplied array contains
target values. The CLI exits 2 for invalid JSON or inputs.

## Verification

**52 Python tests** include 200 full-parameter finite differences against a
separate objective, a separate augmented least-squares PCA solve, nearest/tie
controls, exact data hashes and no duplicate features, full refit with a test
loader prohibition, full test re-evaluation, validation-only selection,
tampering refusal, CLI paths, SVG pixels/values and complete report metadata.

**Fourteen Node/real-Chrome tests** compare independent JavaScript inference with
Python on all 40 public test/mask examples, verify hidden-target erasure and
visible-pixel identity, check a tiny analytic ridge solve, and exercise actual
browser masks, keyboard controls, copy denial/success, downloads and responsive
320/390/1280 layouts. The phone audit table stacks into labeled cards; it does
not hide core values behind horizontal scrolling.

CI also builds a wheel and runs all ten modules and nine CLI commands from
outside the checkout, refitting and evaluating the installed package. Floating
training is checked with explicit tolerances, not claimed bitwise portable
across BLAS implementations. Exported files are exact from committed artifacts.

## Attribution and limits

Data: Alpaydin, E. & Kaynak, C. (1998), [Optical Recognition of Handwritten
Digits](https://archive.ics.uci.edu/dataset/80/optical+recognition+of+handwritten+digits),
UCI, DOI [10.24432/C50P49](https://doi.org/10.24432/C50P49), CC BY 4.0.
Original numeric files and manifest are retained from the same verified source
archive used by DigitLab. Rendered inputs and reconstructions are adaptations;
no endorsement is implied. Code is MIT; data terms are separate in
[the data notice](https://github.com/midya8/denoiselab/blob/main/denoiselab/data/LICENSE.md).

One historical dataset, small images, one model/seed/budget, fixed artificial
missingness, no individual writer IDs. Masked reconstruction error does not
establish semantic preservation, calibrated uncertainty, image generation,
clinical restoration or behavior on naturally missing observations. This is a
standalone reconstruction experiment, not DigitLab's classifier/attack study
or LatentLab's synthetic variational density model.

## Fixed-mask response (v0.2)

The original manual-gradient training and strong observed-pixel controls are retained. Input response is separately derived from fixed parameters: full chain-rule matrices through three tanh layers and sigmoid, and an observed-only linear-system derivative for PCA. Actual edited reconstructions remain separate from local tangent predictions. Saturated PCA rows have zero local response; nonconstant clipping-boundary rows are null rather than an invented derivative. Nearest-neighbor response retains old/new retrieved indices and a frozen-original-neighbor image, with a scalar switch control.

Complete unbounded tangents and residuals can be copied or downloaded; only the rendered image clamps them. Missingness flags remain discrete. No hidden accuracy score or refit is performed. [Equations, independent checks and source ledger](https://github.com/midya8/denoiselab/blob/main/RESPONSE.md).
