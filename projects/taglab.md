# TagLab: the normalizer is part of the model

[Source](https://github.com/midya8/taglab) · [Live inspector](https://midya8.github.io/taglab/) · [Method and sources](https://github.com/midya8/taglab/blob/main/METHOD.md)

## What it does

TagLab trains linear-chain conditional random fields from scratch, with no tensor library, autodiff, model API or external dataset. A 39-parameter sequence score combines fixed observed features, FROM/TO label transitions and separate start/end scores. Manual log-space forward/backward produces the global partition, node and adjacent-label marginals. Expected-minus-observed feature counts give the supervised conditional-likelihood gradient. Viterbi and token marginal decisions remain separate.

The trained independent-label control uses exactly the same eight observed features, including left/right context. Its 15 sequence scores are fixed at zero; its remaining 24 weights are fitted, not left as a weak untrained baseline. Both families fit three positive L2 penalties and select by validation conditional NLL per token.

## Don't hide the losing metric

| Selected model | Test NLL/token | Viterbi token errors | Marginal token errors | Whole-sequence errors |
| --- | ---: | ---: | ---: | ---: |
| Chain CRF, λ 0.3 | 0.557614 | 66/164 | 56/164 | 15/16 |
| Independent log-linear, λ 0.3 | 0.813715 | 56/164 | 56/164 | 15/16 |

The chain wins on distribution scoring but loses on one highest-probability path's token errors. Those are different objectives. The family comparison changes fitted parameters and penalty geometry too; it is descriptive, not an isolated causal transition effect. All six candidates remain visible; a lower-penalty chain's test result is not used to replace the validation-selected model.

The original fixture contains 24 training, 12 validation and 16 test sequences of noisy numeric observations from persistent synthetic states. Seeds, complete examples and labels are retained. This is not real text, an external NLP benchmark, a significance test or evidence of calibrated confidence.

## The full learning trace

Every one of 327 stored states retains all parameters, all 39 analytic gradient entries, objective, gradient norm, accepted Armijo step and rejected larger steps. The browser independently recomputes its objective and gradient from the original training examples. Three fits stop at the 1e-5 gradient tolerance; three exhaust their 80-update budget. The selected chain exhausts its budget with gradient norm about 0.000629. Convexity and a decreasing curve do not certify that finite iterate as an optimum.

The editable inspector accepts custom symbol sequences and explicitly marked transition-score changes. It recomputes messages, node and pair probabilities, complete best-path score, entropy and backpointers using scalar JavaScript. Original labels are shown only while symbols match the selected stored example; custom observations carry no invented labels. Modified scores are never presented as retraining or fresh test performance. Invalid input clears stale evidence. Keyboard access, clipboard failure/success and real JSON download are exercised.

## Exact normalization witness

Three allowed paths A/C, B/A and B/C have raw weights [1/9,1,1/9]. One global normalizer gives [1/11,9/11,1/11]. Equal initial branch scores and local outgoing normalizers instead give [1/2,9/20,1/20]. A's only outgoing branch always keeps its incoming 1/2 mass, even when its continuation loses raw weight. Five evidence weights are computed with exact fractions.

These are fixed-score distributions on the same restricted support, not equally trained competitors, and not the trained independent-label model above. It is an original illustration of standard label-bias theory, not a new method or a universal CRF advantage. The general finite-score API is fully connected and does not disguise large negative numbers as exact forbidden transitions.

## Independent checks and reproduction

22 Python and seven Node/real-Chrome tests include sixty exhaustive rational/integer path-potential controls in Python Fraction and independent JavaScript BigInt enumeration; all 39 finite differences; independent expected-feature enumeration; boundary, gauge, long-score and tie controls; all six fresh fits; test-label poisoning with unchanged fits/selection; full state audit and mutation rejection. Scalar JavaScript checks 12,753 gradient entries, all six model test metrics and 32 complete selected-model sequence witnesses. Real Chrome exercises 327 optimizer states plus 984 model/sequence/focus states, edited inputs, exact normalization cases and 320/390/1280 layouts.

```sh
python -m taglab demo
python -m taglab train --output /tmp/taglab-fresh.json
python -m taglab audit --input /tmp/taglab-fresh.json
python -m taglab infer --symbols '[-2, 0, 2]' --family chain
python -m taglab normalization
python -m taglab export --output /tmp/taglab-web
python -m unittest discover -s tests -v
node --test tests/*.cjs
```

Eight modules and six commands reproduce outside the checkout from the installed wheel, including six fresh fits, stored/fresh audits and four exact archive/loader exports. The lossless three-part compressed archive checks the raw report's SHA-256 before parsing in Python and the browser. Fresh floating-point fits use a declared finite tolerance, not a bitwise portability claim.

## Scope

This models p(labels | observations), not p(observations). Both neighboring observations are available, so it is not streaming inference. Model posteriors are not calibrated real-world confidence. No semantic language task, external validation, population significance, causal isolation, deployment readiness or universal ranking is claimed. Standard CRF, forward/backward and Viterbi theory is cited in the method, including explicit notation differences. Original code, tests, fixture and prose are MIT; cited papers are not redistributed.
