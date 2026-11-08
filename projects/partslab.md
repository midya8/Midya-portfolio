# PartsLab

**Add without subtracting.**

- Live: [editable nonnegative parts inspector](https://midya8.github.io/partslab/)
- Source: [midya8/partslab](https://github.com/midya8/partslab)
- Method: [equations, fixed protocol and primary sources](https://github.com/midya8/partslab/blob/main/METHOD.md)

## What it does

Manual NumPy nonnegative matrix factorization turns original 8x8 UCI digit pixels into nonnegative additive basis contributions. A scalar-JavaScript browser solves actual new nonnegative coefficients when you edit arbitrary pixels. It shows individual contributions, a separately rescaled basis view, numerical KKT status, unclipped reconstruction errors and signed PCA/SVD/mean controls. No model API, uploads, hidden labels or prerecorded arbitrary-input answers.

Six fits use all 3,823 original training images without labels: fixed ranks 8/16/32, seeds 11/23 and 100 outer / 3 inner coordinate sweeps. Within each rank, lowest reencoded training MSE selects a restart. All six histories and results remain public; no rank is selected. A frozen model/protocol hash is verified before evaluation opens the 1,797-row official test file. No holdout-based budget or seed tuning.

## What the stronger controls say

| Rank | Training-chosen seed | NMF test MSE | Centered PCA | Uncentered SVD |
|---:|---:|---:|---:|---:|
|8|23|0.0309683|0.0251267|0.0257206|
|16|23|0.0163996|0.0118776|0.0119639|
|32|11|0.0046791|0.0027689|0.0027681|

Training-mean MSE 0.0735163. Scores use raw unclipped reconstructions; display canvases alone clip. PCA has an extra training mean, so equal rank is not equal parameter count or compute. Both signed controls win at every fixed rank. This is not a claim of NMF superiority, digit recognition or perceptual quality.

## Where optimization stops

Every scalar coordinate step minimizes its nonnegative quadratic, with zero-curvature flat directions handled without a denominator epsilon. Finite differences verify gradients, and a separate active-set NNLS oracle checks 35 tiny random problems. Projected-gradient and complementarity diagnostics remain visible.

All six joint NMF fits exhaust their fixed budget without meeting joint stationarity tolerance. Decreasing loss is not convergence, global optimality or even a demonstrated local minimum. Frozen-basis NNLS is convex; all official test rows meet the numerical per-row KKT threshold in every saved run. An arbitrary input may instead exhaust 1,000 sweeps and is marked unfinished. Numerical residuals are not exact objective-gap bounds or coefficient-uniqueness certificates.

## Parts do not identify meaning

A plain multiplicative-update control with target [1,1], identity basis and initial coefficients [1,0] stays at loss 0.5 with a blocked gradient -1. Coordinate minimization reaches zero on the same objective. This isolates zero-locking in that plain update, not every modified multiplicative method.

Positive factor rescaling and shared permutations preserve a reconstruction. Duplicate basis rows allow different coefficients even with the dictionary fixed. Unit-L2 basis normalization fixes a display scale only. These controls do not prove the actual fitted dictionaries have duplicate or nonunique optima. The basis is not a learned semantic digit label or a causal explanation.

## Checked, not claimed

38 Python and eleven Node/real-Chrome tests: independent scalar objective/coordinates, full finite differences, 35 support-enumerated NNLS optima, zero/duplicate/budget cases, six full refits with test access forbidden, frozen guards, every holdout/control score and exact SVG regeneration. Native and browser decompositions agree for all 120 model/example pairs. Real Chrome checks all 2,048 pixels in the 32-part contribution grid, arbitrary edits, keyboard, basis controls, copy denied/success, download and expanded 320/390/1280 layouts. The installed wheel imports ten modules and executes all ten CLIs outside the checkout, reproducing all six fits and held-out scores.

Original data: Alpaydin & Kaynak (1998), [UCI Optical Recognition of Handwritten Digits](https://archive.ics.uci.edu/dataset/80/optical+recognition+of+handwritten+digits), CC BY 4.0. Original numeric files, source hashes and license retained. Basis images and reports are new transformations. Original code MIT. Established algorithms, no endorsement.


## v0.2: exact fixed-basis objective bounds

The v0.2 fixed-basis certificate adds exact binary64 primal/dual arithmetic, outward-rounded objective intervals and portable JSON proofs with an independent Python Fraction verifier. Eighty exact rational active-set optima and all 120 cross-language witness references are checked. The live browser verifies its own candidates, including zero-sweep unfinished solves, and accepts valid pasted proofs while rejecting tampered ones. A residual-shift bound can be loose; even zero gap does not imply unique coefficients. Original fits, scores and selection remain unchanged. [Certificate proof and limits](https://github.com/midya8/partslab/blob/main/CERTIFICATE.md).

The certificate exports the actual represented pixels, basis and candidate coefficients together with a rational dual vector and primal/dual/gap values. The checker certifies the embedded problem, not its origin or model quality. The displayed bounds are half squared error rather than per-pixel MSE. No joint NMF global optimum or semantic interpretation follows. The 120 witness references cover only the twenty already-public examples for six models, not all holdout rows. All six original joint fits still exhaust their fixed stationarity budget.

## v0.3: exact fixed-face response

V0.3 adds an [exact fixed-face pixel inspector](https://midya8.github.io/partslab/face.html): nominate a face from the numeric NNLS result, re-solve it exactly, and intersect every affine KKT inequality with the pixel domain. All endpoint ties, singular refusals, singleton faces and duplicate-basis nonuniqueness stay explicit. 38 Python and eleven Node/Chrome tests cover 200 independently enumerated tiny face candidates, all 120 stored nominations, 54 complete native/BigInt/Worker witnesses and 10,368 endpoint pixel colors. Ten modules/ten commands with all six fresh fits reproduced. Original data, models and scores remain unchanged. One candidate interval, not a full path, unique support, robustness or joint-NMF optimum. [Math and limits](https://github.com/midya8/partslab/blob/main/FACE.md).
