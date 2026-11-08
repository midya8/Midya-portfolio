# DenoiseLab: learned reconstruction with strong observed-pixel controls

Real masked-digit reconstruction with manual NumPy backprop, 14,544 learned parameters and independent scalar JavaScript inference. A local browser inspector recomputes the neural denoiser, observed-pixel PCA ridge solve, exact fitting-example neighbor and pixel mean when arbitrary pixels are erased. Validation-only selection preserves the official UCI holdout; all four fixed corruption cases and every per-image score remain visible. Nearest neighbor and PCA beat the neural net at 16 missing pixels; the network is lower at 32, with no universal ranking inferred. 27 Python tests plus four Node/real-Chrome tests cover 200 independent gradient probes, complete refit with test-loader prohibition, full evaluation reproduction, all 40 public inference examples and responsive keyboard/copy/download controls. Seven-module/four-CLI installed wheel. CC BY 4.0 data, MIT code; no uncertainty, causal, semantic-preservation or production-restoration claim.

[Open the live reconstruction inspector](https://midya8.github.io/denoiselab/).

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

**27 Python tests** include 200 full-parameter finite differences against a
separate objective, a separate augmented least-squares PCA solve, nearest/tie
controls, exact data hashes and no duplicate features, full refit with a test
loader prohibition, full test re-evaluation, validation-only selection,
tampering refusal, CLI paths, SVG pixels/values and complete report metadata.

**Four Node/real-Chrome tests** compare independent JavaScript inference with
Python on all 40 public test/mask examples, verify hidden-target erasure and
visible-pixel identity, check a tiny analytic ridge solve, and exercise actual
browser masks, keyboard controls, copy denial/success, downloads and responsive
320/390/1280 layouts. The phone audit table stacks into labeled cards; it does
not hide core values behind horizontal scrolling.

CI also builds a wheel and runs all seven modules and four CLI commands from
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
