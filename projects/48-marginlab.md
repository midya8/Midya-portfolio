# MarginLab: keep the constraints visible

Manual linear/RBF soft-margin SVM learning on licensed public UCI data: bounded dual-pair updates, complete pair replay, numerical KKT/gap/feasibility witnesses and independent exact-rational active-face oracles. The editable browser recomputes all 30-feature scores and signed algebraic terms, with an honest two-feature decision slice. Twenty Python and five Node/real-Chrome tests cover 60 tiny exact optima, 4,552 score comparisons, eight fresh fits and real keyboard/copy/download/mobile behavior. Validation chooses 112/115 test correct versus full-30D 1NN 111/115; two unselected RBF fits get 113/115. Seven-module/five-command installed wheel reproduces all fits and audits. Educational historical data, not clinical validation, calibrated certainty or causal importance.

- [Repository](https://github.com/midya8/marginlab)
- [Live 30-feature inspector](https://midya8.github.io/marginlab/)
- [Equations, source attribution and limits](https://github.com/midya8/marginlab/blob/main/METHOD.md)

## What makes it inspectable

The original two-variable dual solver handles linear and RBF kernels, exact bounded line maxima and zero-curvature endpoints. Every accepted pair retains its indices, changes, curvature and objective gain. A separate replay checks all constraints, endpoints and the objective telescope. A tiny independent Fraction active-face KKT oracle checks 60 optima without calling the pair solver. Full-data stopping remains numerical, not an exact-rational certificate.

Training-only scaling, a frozen 341/113/115 split and validation-only selection prevent test-based selection. The full-30D nearest-neighbor control is not weakened to the displayed two dimensions. All eight fits remain visible, including two with a better test score than the validation choice. This small historical split does not establish a general ranking.

## Controls that prevent easy claims

Four separable one-dimensional points reach 100% training accuracy after one pair update while the optimization gap is still 2/3. Opposite labels at an identical input give zero pair curvature and require endpoint comparison. Duplicate same-label inputs have nonunique support coefficients at the same decision function. Correct labels, unique causal importance and a solved optimization are different claims.

## Reproduction and boundaries

Twenty Python and five Node/real-Chrome tests, four Python CI versions, an installed seven-module/five-command wheel, all eight fresh fits and full saved/fresh pair audits. The browser checks all 4,552 native/scalar-JavaScript scores, every feature, 24 UI model/example states, physical keyboard input, blocked/successful clipboard, actual JSON Blob download and 320/390/1280 layouts including horizontal-table reachability.

Original UCI Wisconsin Diagnostic data is CC BY 4.0 with exact source hashes. Source metadata is losslessly encoded to preserve its original missing final newline; readable bounded artifact files assemble to the identical full report. No medical advice, clinical validation, calibrated probabilities or deployment-readiness claim. The plot is a two-feature slice with the other 28 features at their training means, not a projection. Algebraic score terms are not causal effects. MIT code; no model API, paid API, private data or sklearn SVM.
