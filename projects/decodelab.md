# DecodeLab

Inspectable decoding from scratch: stable staged sampling, complete finite continuation trees and beam-pruning witnesses. Dependency-free Python and independent scalar JavaScript, without a model API.

## The question

What changes when temperature, top-k, top-p or beam width changes? A generated sentence and a diversity score cannot explain every decision. DecodeLab exposes the probability stages and every finite future, while keeping likelihood separate from text quality.

## Implementation

- Stable temperature scaling subtracts the largest log probability before division, preventing all events from underflowing together. Normalized top-k precedes normalized top-p. Every intermediate distribution, retained mass and cutoff-prefix mass is returned, with explicit lexical ties.
- This fixes the earlier unnormalized nucleus test. For probabilities (0.6, 0.3, 0.1), temperature 0.5 and top-p 0.7, the old powers sum to 0.46 and keep all events. Normalization gives the first event 0.7826 mass, so it alone is the nucleus.
- Bounded exhaustive continuation trees return all EOS-terminated and cap-censored outcomes, their filtered sampling probabilities, original-model log scores, total/EOS/cap mass and expected generated length. The conditioned prompt is not scored; capped paths have no invented EOS factor.
- Full beam traces retain every expanded candidate, parent, emission and pruning decision. Finished paths remain in the shared finished/live beam. An exhaustive oracle uses exactly the same conditional log-probability objective, without a length penalty.
- A strict JSON table CLI and editable browser let readers change transition weights, temperature, filters, prompt and cap; inspect all distributions and candidate steps; paginate every outcome; and export the complete current audit. Edits hide stale results until recomputation.

## Counterexamples with complete witnesses

The first original synthetic table has a horizon 3 oracle `b + EOS` with probability 0.3822. Width 1 ends at the cap with `a a a`, log-score gap 1.7066336993; widths 2/3 attain the oracle.

The second table has oracle `a + EOS`, probability 0.1940719831. Width 1/3 attain it, but width 2 prunes it and finishes with capped `b b a`, log-score gap 0.6275452747. A wider beam is not guaranteed to improve this particular shared finished/live algorithm. This is a search counterexample, not evidence about human writing quality.

## Independent verification

54 Python tests include all 36 unchanged original tests. The new checks use unshifted 90-digit Decimal powers against production log/exp, rational Cartesian path products, and rational forward mass/expected-length propagation on 40 random tables. Wide beams are compared with exhaustive oracles.

32 full audits and 120 staged cases are retained. Independent scalar JavaScript checks 7,927 numerical values. Actual Chrome tests inspect 96 distribution views, 231 displayed outcome rows and 956 candidate rows, plus JSON export, stale-on-edit behavior and 320/390/1280 layout bounds. Python 3.10-3.13 CI and an installed wheel outside the checkout reproduce the audit.

Nine original files remain byte-exact, including the original36-test file, tokenizer, metrics/reports, corpus and offline demo. The original generation/compare CLI remains. Corrected nucleus normalization and short-context start padding intentionally change affected sampling policies; original exact-output greedy/demo assertions still pass.

## Bounds and sources

These are original synthetic Markov tables and a corpus-trained n-gram stand-in, not a neural model or language-quality benchmark. Diversity and repetition metrics do not establish factuality, coherence or safety. Exhaustive enumeration is exponential and bounded. Floating-point comparisons use tolerances; very small tails can underflow, and near-cutoff membership can depend on rounding. The width failure is specific to the documented beam semantics.

Temperature, nucleus sampling and beam search are prior work. The contract and demo link Holtzman et al., Higham's shifted-softmax discussion, Hugging Face generation documentation, OpenAI GPT-2 sampling, LabML and Raschka. No new decoding algorithm is claimed.

## Links

- [Interactive probability inspector](https://midya8.github.io/decodelab/)
- [Source and tests](https://github.com/midya8/decodelab)
- [Numerical and stopping contract](https://github.com/midya8/decodelab/blob/main/AUDIT.md)
- [Implementation PR](https://github.com/midya8/decodelab/pull/2)
