# ForestLab: tree votes, bootstrap membership and leaf collisions

[Repository](https://github.com/midya8/forestlab) | [Live inspector](https://midya8.github.io/forestlab/) | [Method, sources and limits](https://github.com/midya8/forestlab/blob/main/METHOD.md)

## What the inspectors show

ForestLab fits binary CART forests to the UCI Banknote Authentication numeric descriptors. It orders Gini split candidates using exact integer comparisons and retains every bootstrap count. An editable browser separates all-tree predictions from votes made only by trees that did not train on a given group.

The original inspector shows predictions, paths and membership. The joint-permutation inspector moves feature blocks through frozen models; the leaf-collision inspector compares all-tree geometry with separately normalized jointly-OOB pairs. No estimator library or model API does the fitting.

## Implementation

Binary CART split costs are compared by arbitrary-precision integer cross products. Sixty independent Fraction designs and a separate BigInt complete-mask enumerator check the criterion. Lower-observed thresholds, feature/cut ties, minimum leaves, pure nodes and nonpositive gains have explicit conventions. Exact node ordering does not imply a globally optimal tree.

Eight 31-tree forests retain all 248 bootstrap vectors and 7,102 tree nodes. The browser recomputes all 31 paths and exposes every in-bag count for a stored training group. Edited inputs drop group membership immediately. An OOB score uses only trees with zero draws of that group; zero eligible trees means no prediction, never the full-forest result.

## Keep the stronger comparison

The original licensed UCI file has 1,372 numeric records but only 1,348 unique four-feature vectors. Exact copies are collapsed and kept together before the fixed 808/270/270 train/validation/test split. Original row IDs remain auditable. No physical specimen identifier is available, so near-duplicates and shared specimens are not ruled out.

Each model family selects by validation errors, then Brier score, then ID before test labels are read. All eight forests, four single trees and seven controls remain visible. The selected forest makes 3/270 test errors; the stronger selected 5NN control makes 0/270 and the selected single tree makes 8/270. This is one historical split, not a claim of zero future error or a test of real authentication.

## Joint permutation with frozen models

[Joint permutation inspector](https://midya8.github.io/forestlab/permutation.html) | [Method and sources](https://github.com/midya8/forestlab/blob/main/PERMUTATION.md)

All 15 nonempty feature blocks move through the same 16 fixed row bijections. Selected columns come from the same donor; recipient labels and remaining features stay in place. Both frozen models, the selected forest and stronger selected 5NN, retain all 240 cases and 129,600 model-row prediction counts. Every repeat, including negative error changes, remains visible. The browser recomputes the selected hybrid row independently and exposes all tree paths, neighbor votes, donor mapping and model binding.

These diagnostics use the same validation set that already selected the models. Baseline validation errors are 4/270 and 1/270, distinct from the unchanged original test errors 3/270 and 0/270. No model is refitted, removed-feature control fitted or selection changed. Repeat ranges are not confidence intervals. Moving a block preserves dependence within it, not across its boundary; joint changes are not sums or isolated causal interactions. An exact three-row, six-bijection control exposes off-support singleton hybrids without copying a source figure. Even full-row shuffling can preserve observed support while destroying label pairing.

## Reproduction and checks

39 Python and 12 Node/real-Chrome tests check fresh fitting, source/group/split provenance, all bootstrap vectors, complete node witnesses, train-only standardization and logistic gradients. Test-label poisoning leaves fits and selections unchanged. Source, split, bootstrap, gain, metric and selection mutations are rejected.

Independent scalar JavaScript checks 10,784 forest evaluations, 8,088 control scores and 6,464 OOB records. Chrome drives all 992 native path references and every model/partition state, physical-keyboard membership changes, invalid-input clearing/recovery, clipboard success/failure, actual JSON Blob download and 320/390/1280px layouts. The installed ten-module package runs all ten commands, refits all 19 models, audits them and reproduces the checked browser exports outside the checkout.

The added diagnostic has independent scalar-JavaScript predictions for all 129,600 model-row evaluations, exact Fraction metric controls, full fresh regeneration, fit/map/count mutation rejection, train/test-label poisoning and 1,230 actual browser states. Outside-checkout reproduction regenerates all 240 cases, audits them and compares seven archive/loader exports exactly.

## Scope

Classes stay the source's labels 0 and 1, not an invented genuine/forged mapping. These are historical precomputed image descriptors, not an image-upload classifier or a currency detector. Hard votes, leaf fractions and neighbor fractions are not calibrated probabilities, confidence intervals or conformal sets. OOB is a training-sample diagnostic, not the held-out full-forest test or independent specimen validation. Paths are not causal explanations.

Original data: Lohweg, V. (2012), UCI Banknote Authentication, DOI 10.24432/C55P57, CC BY 4.0. Original bytes are retained in lossless checked text encoding; exact-copy grouping and partitioning are this project's transformations. No source images were copied. MIT code. Established CART/forest methods are credited in the method note; attribution is not endorsement.

## Leaf-collision geometry

The [leaf-collision inspector](https://midya8.github.io/forestlab/proximity.html) exposes all-tree similarity as an explicit Gram matrix, with exact integer/BigInt sum-of-squares witnesses. A separate jointly-OOB view keeps pair-specific tree counts and undefined comparisons. A constructed negative quadratic form (-2) and triangle failure show why OOB normalization is not a universal kernel guarantee. All 512 small partition controls, 5,760 native/scalar-JS matrix entries, 1,152 actual pair states and 13,824 heatmap colors are checked. Frozen supervised model geometry, not semantic similarity, causal influence, uncertainty or a new score. [Geometry derivation and limits](https://github.com/midya8/forestlab/blob/main/PROXIMITY.md).

The all-tree proximity is the mean of per-tree leaf collisions. Keeping tree identity in each leaf-indicator column makes P=ZZᵀ/T, including singular matrices. Exact Python integer and browser BigInt witnesses evaluate the full quadratic expression and every leaf-bucket square. Squared feature-space distance is 2(1-P); distinct raw inputs can have zero distance. This is not a semantic identity proof.

Indexed jointly-OOB comparisons use the original training order and complete bootstrap multiplicities. A zero eligible denominator is undefined, not zero similarity. Feature-only edits cannot inherit source identity, even if their numbers match an original row. The constructed three-row partition/eligibility control has cᵀP_oob c=-2 for c=(1,-2,1), while the corresponding all-tree form is 10/3. It disproves a universal PSD guarantee, not every OOB matrix's PSD status. No matrix repair or hidden missing-entry fill is used.

The new diagnostic checks 6,272 source-pair entries through independent traversal/set intersections; complete native/scalar-JS reference matrices have 1,152 mixed-partition and 4,608 heatmap entries plus 8,928 terminal coordinates. Real Chrome checks every pair and all 13,824 view-specific colors, exact large integers, indexed/feature-only states, invalid retention, model context, keyboard, clipboard and actual Blob JSON. The installed wheel preserves all 19 fresh fits and permutation audits, then checks two new exact exports. The fixed 24-row matrix is descriptive, not selected for quality or a whole-data embedding. No labels are read by the new calculation, but the already fitted partitions retain supervised label information.
