# ForestLab: a vote with an auditable membership list

[Repository](https://github.com/midya8/forestlab) | [Live inspector](https://midya8.github.io/forestlab/) | [Method, sources and limits](https://github.com/midya8/forestlab/blob/main/METHOD.md)

## Why build it

A hard-vote fraction can look reassuring while hiding which models saw the observation. This project exposes every bootstrap count, path, leaf and vote, then excludes in-bag trees before calling a prediction OOB. No estimator library or model API does the fitting.

## Implementation

Binary CART split costs are compared by arbitrary-precision integer cross products. Sixty independent Fraction designs and a separate BigInt complete-mask enumerator check the criterion. Lower-observed thresholds, feature/cut ties, minimum leaves, pure nodes and nonpositive gains have explicit conventions. Exact node ordering does not imply a globally optimal tree.

Eight 31-tree forests retain all 248 bootstrap vectors and 7,102 tree nodes. The browser recomputes all 31 paths and exposes every in-bag count for a stored training group. Edited inputs drop group membership immediately. An OOB score uses only trees with zero draws of that group; zero eligible trees means no prediction, never the full-forest result.

## Keep the stronger comparison

The original licensed UCI file has 1,372 numeric records but only 1,348 unique four-feature vectors. Exact copies are collapsed and kept together before the fixed 808/270/270 train/validation/test split. Original row IDs remain auditable. No physical specimen identifier is available, so near-duplicates and shared specimens are not ruled out.

Each model family selects by validation errors, then Brier score, then ID before test labels are read. All eight forests, four single trees and seven controls remain visible. The selected forest makes 3/270 test errors; the stronger selected 5NN control makes 0/270 and the selected single tree makes 8/270. This is one historical split, not a claim of zero future error or a test of real authentication.

## V0.2: break a pairing, freeze the model

[Joint permutation inspector](https://midya8.github.io/forestlab/permutation.html) | [Method and sources](https://github.com/midya8/forestlab/blob/main/PERMUTATION.md)

All 15 nonempty feature blocks move through the same 16 fixed row bijections. Selected columns come from the same donor; recipient labels and remaining features stay in place. Both frozen models, the selected forest and stronger selected 5NN, retain all 240 cases and 129,600 model-row prediction counts. Every repeat, including negative error changes, remains visible. The browser recomputes the selected hybrid row independently and exposes all tree paths, neighbor votes, donor mapping and model binding.

These diagnostics use the same validation set that already selected the models. Baseline validation errors are 4/270 and 1/270, distinct from the unchanged original test errors 3/270 and 0/270. No model is refitted, removed-feature control fitted or selection changed. Repeat ranges are not confidence intervals. Moving a block preserves dependence within it, not across its boundary; joint changes are not sums or isolated causal interactions. An exact three-row, six-bijection control exposes off-support singleton hybrids without copying a source figure. Even full-row shuffling can preserve observed support while destroying label pairing.

## Reproduction and checks

31 Python and nine Node/real-Chrome tests check fresh fitting, source/group/split provenance, all bootstrap vectors, complete node witnesses, train-only standardization and logistic gradients. Test-label poisoning leaves fits and selections unchanged. Source, split, bootstrap, gain, metric and selection mutations are rejected.

Independent scalar JavaScript checks 10,784 forest evaluations, 8,088 control scores and 6,464 OOB records. Chrome drives all 992 native path references and every model/partition state, physical-keyboard membership changes, invalid-input clearing/recovery, clipboard success/failure, actual JSON Blob download and 320/390/1280px layouts. The installed eight-module package runs all seven commands, refits all19 models, audits them and reproduces the checked browser exports outside the checkout.

The added diagnostic has independent scalar-JavaScript predictions for all 129,600 model-row evaluations, exact Fraction metric controls, full fresh regeneration, fit/map/count mutation rejection, train/test-label poisoning and 1,230 actual browser states. Outside-checkout reproduction regenerates all 240 cases, audits them and compares seven archive/loader exports exactly.

## Scope

Classes stay the source's labels 0 and 1, not an invented genuine/forged mapping. These are historical precomputed image descriptors, not an image-upload classifier or a currency detector. Hard votes, leaf fractions and neighbor fractions are not calibrated probabilities, confidence intervals or conformal sets. OOB is a training-sample diagnostic, not the held-out full-forest test or independent specimen validation. Paths are not causal explanations.

Original data: Lohweg, V. (2012), UCI Banknote Authentication, DOI10.24432/C55P57, CC BY4.0. Original bytes are retained in lossless checked text encoding; exact-copy grouping and partitioning are this project's transformations. No source images were copied. MIT code. Established CART/forest methods are credited in the method note; attribution is not endorsement.
