# ClusterLab: shapes first, labels later

[Repository](https://github.com/midya8/clusterlab) · [Live clustering inspector](https://midya8.github.io/clusterlab/) · [Method and sources](https://github.com/midya8/clusterlab/blob/main/METHOD.md)

## Why build it

A k-means demo can mistake arbitrary group IDs for digit recognition and monotone descent for a globally optimal fit. ClusterLab makes both errors hard to miss: forty optimization histories remain visible, learned centroids show mixed true-digit membership, and the browser runs actual editable inference rather than replaying saved predictions.

## Implementation

Manual NumPy Lloyd assignment/mean updates, D² k-means++ initialization, uniform distinct-value initialization, deterministic ties, empty-center repair and complete restart artifacts. Four fixed arms use raw 64-pixel geometry, raw uniform starts, fitting-only PCA16 and whitened PCA16. Each chooses minimum fitting inertia among seeds 100-109, never a test-label score. All 3,823 original UCI training features fit the models without class-label use; the 1,797 original official test rows remain held out. No test-based choice of k, rank, arm or seed.

The browser projects edited 8x8 inputs and computes distances to all ten learned centers locally, with keyboard controls, a centroid atlas, held-out composition, all restart curves and JSON copy/download. The first twenty original test rows are included by index, not success. Cluster IDs are groups, not digit labels; distances are not probabilities. No API, uploads, analytics or remote inference.

## What the holdout says

| Fixed arm | Adjusted Rand | Arithmetic NMI | Silhouette (own geometry) |
|---|---:|---:|---:|
| Raw / k-means++ | .662690 | .751821 | .186434 |
| Raw / uniform | .665149 | .749688 | .186142 |
| PCA16 / k-means++ | .669707 | .740137 | .224268 |
| Whitened PCA16 / k-means++ | .665596 | .739303 | .149408 |

Careful seeding has slightly lower raw fitting inertia (9682.7571 vs 9683.1241), but uniform has slightly higher test ARI. No general seeding win is claimed. PCA and whitening change the distance metric, so cross-geometry inertia/silhouette differences are descriptive and cannot be ranked as one unchanged objective. NMI is not adjusted for chance. No confidence interval, causal isolation or classifier accuracy is inferred.

## Evidence, not a screenshot alone

28 Python tests and four Node/real-Chrome tests. Independent scalar objective and D² sampling references, pair/null-permutation ARI, joint-entropy NMI, all-pair silhouette, PCA eigenspectrum and whitening checks. A full 40-fit reproduction forbids test-loader access and gives training code unusable labels. Frozen model/protocol hashes are verified before evaluation opens the test file; every held-out distance, silhouette and composition is reproduced.

The Python and independent scalar JavaScript implementations agree on all 80 public model/example pairs and all ten distances. Real Chrome checks all 640 displayed centroid pixels, custom edits, keyboard, copy denial/success, download and expanded 320/390/1280 layouts. The audit SVG checks all 640 raw-mean values, sixteen score cells and the full report metadata. The installed wheel imports all eight modules and exercises all four CLIs outside the checkout, including a full refit and evaluation. CI covers Python 3.10-3.13, packaging and the browser.

## A deliberate failure case

For `[0,1,4,5,9,10]` with k=2, initialization `[0,1]` converges to inertia 26.5. Exhaustive exact-rational enumeration of all 31 nonempty binary partitions yields global optimum 17.5. Stable descent is not a global certificate. No such global certificate is claimed for the real-data fits.

## Credit and boundaries

Established algorithms, original code, not a new clustering method. Data: Alpaydin & Kaynak (1998), UCI Optical Recognition of Handwritten Digits, CC BY 4.0, DOI 10.24432/C50P49. Original numeric-file hashes preserved; normalization and derived representations disclosed. 8x8 block counts, not image-file OCR or MNIST. The original split uses different writer groups according to UCI; individual writer IDs and near-duplicate independence are not established. No endorsement. Original code MIT. Six primary-research/documentation/dataset sources and all equations are linked in METHOD.md.
