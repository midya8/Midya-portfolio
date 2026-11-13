# ChainLab

Separate what an observation prefix supports, which hidden-state path to choose and how much uncertainty remains over whole paths. ChainLab includes a floating-point HMM trainer, a prefix-evidence inspector and a separate exact-rational path workbench.

[Prefix-evidence inspector](https://midya8.github.io/chainlab/) · [Path workbench](https://midya8.github.io/chainlab/paths.html) · [Source and reproduction](https://github.com/midya8/chainlab)

## Choose the loss before the path

A MAP path minimizes whole-path 0/1 loss. It need not minimize the expected number of wrong positions. Unconstrained state-by-state posterior modes minimize expected Hamming loss but can form a path the model forbids. The rational workbench makes those differences visible in one supplied HMM:

| Decision | Selected path | Posterior probability, approximate | Expected wrong positions, approximate |
| --- | --- | ---: | ---: |
| MAP | B/C/B/C/B | 0.05823316 | 2.880904 |
| Supported expected matches | B/A/C/A/C | 0.05686832 | 2.531237 |
| Supported product marginals | B/C/B/A/C | 0.03639572 | 2.535156 |
| Unconstrained marginal modes | B/C/C/A/C, unsupported | 0 | 2.456165 |

These are model-conditional expected losses, not measured true-state accuracy or a ranking of algorithms. The default is the first qualifying model from a disclosed deterministic search, seed 314159, candidate 1904. It was selected to show disagreement, not sampled as a typical case. The search is in the repository.

The supported decoders respect initial, transition and emission support. They retain every best prefix ending at each state. Objective ties select the lexicographically first whole index path; unconstrained modes choose the first index at each position. These tie rules belong to the rational workbench. The original floating Viterbi API uses its documented local predecessor/final tie rule instead.

## Keep dependence in the uncertainty

Locked and independent five-position chains both have state marginals `[1/2,1/2]`. The locked chain has two supported paths and entropy `ln(2)`; the independent chain has 32 and entropy `5 ln(2)`. Both selected paths have expected Hamming loss `5/2`. A chosen path and its expected per-position loss do not describe the full path distribution.

Whole-path entropy uses the smoothed posterior Markov chain: initial-state entropy plus the weighted next-state conditional entropies. The gap between summed state entropies and path entropy equals summed adjacent-state mutual information. Conditional rows at zero posterior mass stay undefined, not zero distributions. Probabilities, support and decoding fields use Fraction/BigInt arithmetic; entropy and logarithms are approximate binary64 nats, independently checked with Decimal precision 80 at absolute tolerance `1e-10`. Tiny entropy contributions can round to zero. There is no exact transcendental result or rigorous enclosure.

## Draw the evidence boundary

The prefix inspector compares filtering, full-window smoothing, Viterbi and prefix-only forecast marginals without retraining. On the absorbing-state example, filtering after `x` gives `P(A at time 0)=2/3`; smoothing after `x,y` gives zero. Using that smoothed row for an online decision would use future `y`. After `x`, each of the next two forecast marginals has `P(y)=1/6`, but `P(y,y)=1/12`, not `1/36`. Marginals are not independent future evidence.

The first three displayed models show only the first twelve observations of the original forty-symbol test sequence. Smoothing and Viterbi use that displayed window, not the omitted 28 symbols; forecasts use only the selected prefix. Edits do not replace the original reports or scores. Native inference uses log messages; the browser separately uses scaled probability recurrences. The browser refuses zero or underflowed mass rather than claiming mathematical impossibility. Native log inference can retain tiny supported paths that browser scaling loses.

## Training has controls, not a universal ranking

The original seed-23 fixture has twenty independent training sequences and twelve test sequences, forty categorical observations each, from a persistent two-regime HMM. A supplied asymmetric initialization uses a thirty-update cap and absolute total-likelihood tolerance `1e-6`. It stops after twenty accepted updates, increasing training log likelihood from `-820.433625` to `-651.390946`, without smoothing, validation selection, initialization search or test-based stopping.

| Model | Test NLL per symbol, nats |
| --- | ---: |
| Supplied initialization | 1.017638 |
| Training-only iid symbol control | 0.985993 |
| Trained HMM | 0.775631 |
| Generating-model reference, not learned | 0.771674 |

The iid control learns symbol frequencies without transitions. The generating model is an oracle reference, not an equally learned competitor or guaranteed finite-sample winner. This is one inspected synthetic development fixture, not an external benchmark, causal decomposition of transition benefits, significance test or evidence of hidden-state recovery. Latent state labels are arbitrary.

Baum-Welch resets starts for every sequence and never counts transitions across sequence boundaries. Unsmoothed EM retains zero-occupancy rows, cannot resurrect absent support and can lose support for unobserved symbols. Every proposal is scored: a decrease in `[-1e-7,0)` stops and retains the previous model; a larger decrease raises an error. Accepted likelihood is nondecreasing, but there is no local/global optimum or identifiability certificate. Input rows are validated, not silently repaired.

## What is checked

The current suite has **58 Python tests and 10 Node tests**, including actual Chrome for both inspectors. Original exhaustive references cover likelihood, state/edge marginals, path scores and expected-count updates. Prefix checks cover 114 position/symbol edits, forty prefix witnesses and 62 tiny high-precision exhaustive observation windows. Native/browser fields use a disclosed numerical tolerance, not an arbitrary-range equivalence claim.

The rational workbench has thirteen complete controls, 120 tiny exhaustive random models and 150 generated native/BigInt report comparisons. Its standalone verifier imports neither producer nor parser: it rebuilds suffix/prefix probabilities, checks every decoding alternative and whole-path tie, and checks entropy using Decimal80. Tests reject all 438 primitive modifications of the default report; floating changes below tolerance remain outside that promise. This is another implementation of the standard recurrences, not a formal proof assistant.

Actual Chrome checks 296 state cells, 1,532 edge cells, 867 reachable decision states and 39 layouts, with physical model/JSON editing and invalidation. Installed-wheel replay checks ten module origins outside the checkout, original training/data/prefix reports and all nine earlier commands, then thirteen rational controls, both new module commands and 26 malformed reports. Separate review checks also retain actual trusted completed downloads for all five prefix controls and thirteen path controls. Rational exports replay through the standalone checker; prefix exports replay shared mathematical fields while their different browser/native metadata contracts are checked separately.

## Numerical and model limits

- The floating API accepts 1-8 states, 1-16 symbols, sequence length 1-256 and up to 32 training sequences with 2,048 observations total. Probabilities are binary64; zero support is not replaced by epsilon. Printed tiny posterior probabilities can underflow while log scores remain finite.
- The rational workbench accepts 1-4 states, 1-8 symbols and 1-32 observations. Input fractions are capped at 128 bits, reported fractions at 8,192 bits, input at 64 KiB and verifier reports at 4 MiB. Otherwise-valid inputs can exceed the work cap and be refused rather than rounded.
- Three rounded original-model controls round probabilities to millionths, then normalize rows exactly. They are different rational models, not unchanged original fits or new trained arms.
- The work assumes a supplied model and labels. Low entropy can mean a misspecified model is confidently wrong. No calibrated uncertainty, true-state recovery, causal interpretation, external quality result, streaming service, production readiness, speed promise or algorithm novelty is claimed.

[Prefix conditioning and numerical limits](https://github.com/midya8/chainlab/blob/main/EVIDENCE.md) · [Path equations, schemas, verifier and sources](https://github.com/midya8/chainlab/blob/main/PATHS.md) · [Original design](https://github.com/midya8/chainlab/blob/main/DESIGN.md)

Standard HMM, EM and decoding-risk methods are credited to their published sources, including Rabiner and Lember/Koloydenko. Code, controls and UI are an independent educational implementation under MIT, not copied HMM library code or a new sequence-model theorem.
