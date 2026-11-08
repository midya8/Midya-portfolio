# MarginLab: keep the constraints visible

Manual linear/RBF soft-margin SVM learning with replayable pair updates and editable 30-feature scores. Version 0.2 repairs the saved binary64 dual equality before proving exact rational weak-duality bounds for all four represented linear training problems. Independent Fraction and BigInt readers recompute every constraint and objective; source matching is separate from proof validity. Twenty-nine Python and nine Node/real-Chrome tests cover 120 tiny exact optima, 4,552 inference comparisons, four full proofs, keyboard/copy/download/mobile behavior and eight fresh fits. Nine-module/seven-command installed wheel. Original models, holdout scores and split are unchanged. Educational historical UCI data, not clinical validation, calibrated certainty, generalization bounds or source authentication.

- [Repository](https://github.com/midya8/marginlab)
- [Live 30-feature inspector](https://midya8.github.io/marginlab/)
- [Equations, source attribution and limits](https://github.com/midya8/marginlab/blob/main/METHOD.md)

## What makes it inspectable

The original two-variable dual solver handles linear and RBF kernels, exact bounded line maxima and zero-curvature endpoints. Every accepted pair retains its indices, changes, curvature and objective gain. A separate replay checks all constraints, endpoints and the objective telescope. A tiny independent Fraction active-face KKT oracle checks 60 optima without calling the pair solver. Full-data stopping remains numerical, not an exact-rational certificate.

Training-only scaling, a frozen 341/113/115 split and validation-only selection prevent test-based selection. The full-30D nearest-neighbor control is not weakened to the displayed two dimensions. All eight fits remain visible, including two with a better test score than the validation choice. This small historical split does not establish a general ranking.

## Controls that prevent easy claims

Four separable one-dimensional points reach 100% training accuracy after one pair update while the optimization gap is still 2/3. Opposite labels at an identical input give zero pair curvature and require endpoint comparison. Duplicate same-label inputs have nonunique support coefficients at the same decision function. Correct labels, unique causal importance and a solved optimization are different claims.

## Reproduction and boundaries

Twenty-nine Python and nine Node/real-Chrome tests, four Python CI versions, an installed nine-module/seven-command wheel, all eight fresh fits and full saved/fresh pair audits. The browser checks all 4,552 native/scalar-JavaScript scores, every feature, 24 UI model/example states, physical keyboard input, blocked/successful clipboard, actual JSON Blob download and 320/390/1280 layouts including horizontal-table reachability.

Original UCI Wisconsin Diagnostic data is CC BY 4.0 with exact source hashes. Source metadata is losslessly encoded to preserve its original missing final newline; readable bounded artifact files assemble to the identical full report. No medical advice, clinical validation, calibrated probabilities or deployment-readiness claim. The plot is a two-feature slice with the other 28 features at their training means, not a projection. Algebraic score terms are not causal effects. MIT code; no model API, paid API, private data or sklearn SVM.


## Exact feasibility before an exact bound

The original saved floating-point coefficients have nonzero exact signed dual mass. The extension converts their represented binary64 inputs to Fractions, clips to the box and reduces coefficients in the excess class until the equality is exactly zero. It records the original residual and total movement, without changing the original model. A separate exact feasible primal and repaired feasible dual enclose each represented linear training optimum. The approximate gap readouts for C=.01,.1,1,10 are 7.97e-8, 1.42e-6, 2.90e-5 and 3.23e-4; the full canonical objective ratios, not those decimals, are the bounds.

Two independently implemented readers, Python Fraction and browser BigInt, check all constraints, objectives and repair accounting without importing the optimizer. Sixty additional active-face exact optima must lie inside the produced intervals. The browser also checks all four full proofs against every original standardized input, label, C, coefficient and bias. A changed inactive row is an explicit control: its proof can remain mathematically valid for its changed declared problem while source matching rejects it. Proof validity does not authenticate data or authorship.

This is a bound for the represented standardized linear problem, not exact real-number standardization, RBF kernels, generalization error, clinical reliability or a claim that an exact optimum was attained. The original numerical inspector stays numerical; no prediction, score, split, pair history or original figure changes.

- [Live exact linear proof inspector](https://midya8.github.io/marginlab/certificate.html)
- [Derivation, repair algorithm and limits](https://github.com/midya8/marginlab/blob/main/CERTIFICATE.md)
