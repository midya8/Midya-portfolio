# SpectralLab

[Source](https://github.com/midya8/spectrallab) · [Live graph inspector](https://midya8.github.io/spectrallab/) · [Equations and limits](https://github.com/midya8/spectrallab/blob/main/METHOD.md)

## The graph changes the answer

Normalized spectral clustering exposes a choice that a scatter plot can hide: which points are neighbors, and what their connection means. SpectralLab builds the affinity and normalized Laplacian explicitly, retains the eigenspace, normalizes every row and runs manual k-means. NumPy supplies the symmetric eigenvalue solve through LAPACK. No clustering library or model API supplies the result.

The browser reconstructs all graph weights and every selected point's degree, neighbors, cut contributions and three eigenpair equations. Original coordinates and row-normalized embedding sit side by side. Select any actual archived graph or point; change colors or a display-only edge threshold; export the full point witness as JSON. A threshold that hides an edge never changes the fit.

## Fixed experiments, visible failures

Two original seeded 96-point fixtures use noisy interleaving arcs and concentric rings. Nine fixed graph rules each give 18 total fits: union/mutual kNN at 3/6/12 neighbors and full RBF at sigma .08/.25/1.0. All rows remain visible, along with raw-coordinate k-means. Two clusters and 12 starts are fixed; least embedding inertia chooses only a k-means restart. Generator labels never choose a graph or fit.

- Moons union-3: ARI 1.000, eigengap .003156. Moons RBF sigma 1.0: ARI .242035, larger eigengap .350982. A larger gap is not agreement with intended classes. Raw-coordinate k-means gives the same .242035 ARI.
- Rings union-6: ARI 1.000. Rings union-12: ARI -.010195. Adding graph edges does not promise a better semantic grouping.
- Moons mutual-3: four disconnected components. A two-dimensional truncation of its four-dimensional zero eigenspace is not unique, so that fit is refused and no arbitrary cluster labels are shown.

These are designed full-data synthetic illustrations, not held-out predictive accuracy. Raw versus spectral k-means is a comparison of different geometries, not causal isolation of one mechanism. Normalized cut is a common objective only when the graph itself is fixed.

## A relaxation is not a discrete optimum

An original seven-vertex weighted graph has only 63 distinct nonempty binary cuts after fixing one cluster label. Independent rational enumeration finds the optimum **3450/4181 = .8251614446304711**. The archived spectral relaxation plus k-means returns **.860832137733142**. Both partitions and every weight are visible in the demo and source. No exact optimality claim is made for the larger fixtures.

## Verification

22 Python tests cover 528 independent Fraction-distance graph references, 558 rational cut references, analytic cycle spectra and energy identities, component/zero-degree/boundary-tie refusals, invariant subspace rotations, every fresh graph fit, source/degree/eigenvector/label/score mutations and strict CLI behavior. Eigenspace comparisons use projectors, not signs.

Six Node/real-Chrome tests cover 18 reconstructed graphs, 4,896 scalar eigenpair-row equations, all fitted/raw cuts, separate BigInt enumeration of 63 tiny-graph cuts, exact browser dataset exports, 1,728 actual browser point/graph states, refusal clearing, physical keyboard changes that leave fit witnesses unchanged, clipboard success/failure, real JSON Blob downloads and 320/390/1280 layouts with 44-pixel controls.

Installed-wheel reproduction runs outside the checkout, imports all five modules, executes five commands, refits all 18 graphs, audits fresh and archived reports and verifies three archived web exports byte-for-byte. CI runs Python 3.10-3.13, package reproduction and real Chrome.

## Limits and attribution

Eigenvector signs are arbitrary. Orthogonal rotations within the fully retained eigenspace preserve normalized distances, but a repeated eigenvalue crossing the retained boundary can change them. That boundary is refused. Zero-degree vertices are not silently connected. Numerical eigenpair residuals are checks, not formal proofs or statistical confidence.

This is dense full-data clustering. Adding points changes the graph; there is no inductive prediction API, sparse/scalable solver, optimal-graph selection, calibrated uncertainty, causal interpretation or real-world validation. Original synthetic code/data are MIT licensed. The method follows Ng, Jordan and Weiss (2001), with von Luxburg's tutorial and explicit NumPy primitive attribution linked in the method. No external dataset or paper figure is republished.
