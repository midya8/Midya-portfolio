# ica-numpy

Blind source separation with FastICA, written from scratch in NumPy.

The setup is the classic cocktail party: four synthetic sources (a
sawtooth, a sine, gaussian chatter and a sparse pulse train) go through a
random 4x4 mixing matrix. Only the mixtures are observed. The unmixing
has to find them back with no side information.

## What the code does

- Whitening: center the observations, then rescale by the inverse square
  root of the covariance. The eigenvectors are sign-fixed and sorted by
  eigenvalue, because the library's eigendecomposition does not
  guarantee a stable order for near-tied eigenvalues, and a different
  whitened basis can send the fixed-point search to a different optimum.
- The tanh contrast with the classic fixed-point update
  `w <- E[x tanh(w'x)] - E[sech^2] w`, deflated one component at a time
  with Gram-Schmidt against the rows already found.
- Five random starts per component; the start with the largest
  non-gaussianity proxy (`E[tanh(w'x)]^2`) wins, which keeps a bad
  initialization from sticking.
- Scoring: match each estimated row to a true source by absolute
  correlation, rescale with the least-squares gain (which carries the
  sign), then per-source SNR. An earlier version applied the sign twice,
  which negated two of the four sources and showed up as an exact -6 dB
  SNR; the gain now carries the sign on its own.

## Results

On the 4000-sample run: mean absolute correlation 0.9997 against the
true sources, per-source SNR 27.4 / 45.5 / 28.0 / 13.3 dB. PCA with the
same dimension, inverted and rescored, reaches 0.53 mean correlation:
it finds the directions of largest variance, which are mixtures, not
sources. sklearn's FastICA on the same data lands at 0.9998, within a
hair of this implementation.

The pulse train scores lowest on SNR because its energy sits in
five-sample bursts, where a small timing misalignment dominates the
error even though the correlation is 0.9993.
