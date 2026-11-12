# DecodeLab

DecodeLab makes decoding decisions visible: each temperature/filter stage, every bounded continuation and each beam-pruning step. It uses a small offline model so probability, model score and stopping rules can be checked separately, without a model API.

## Normalize before choosing a nucleus

The sampler scales log probabilities by temperature, normalizes, applies top-k and normalizes again, then keeps the smallest top-p prefix that reaches the threshold. Each stage returns its distribution and retained mass. Equal sampling probabilities use lexical token order.

This corrects the earlier unnormalized nucleus rule. For probabilities `(0.6, 0.3, 0.1)`, temperature 0.5 and top-p 0.7, direct powers sum to 0.46 and the old rule keeps everything. After normalization the first token has about 0.7826 mass and is the entire nucleus. Log-space scaling avoids all-event direct-power underflow; tiny tails can still round to zero.

## Keep stopping rules and search scores separate

The bounded tree enumerates all filtered outcomes. EOS contributes its probability and stops. A path that reaches the generation cap has no invented EOS factor. Filtered sampling probability and unfiltered conditional model log score stay separate; the prompt is conditioned on, not scored.

Beam traces retain every candidate, parent, emission and pruning decision. Finished and live paths share one beam, without a length penalty or separate finished pool. The exhaustive oracle uses that same objective.

One original synthetic table has a horizon-3 oracle `b + EOS` with probability 0.3822. Width 1 returns capped `a a a`, with log-score gap 1.7066336993; widths 2 and 3 retain the oracle. Another table has oracle `a + EOS`, probability 0.1940719831: widths 1 and 3 attain it, but width 2 prunes it and returns capped `b b a`, gap 0.6275452747. More width need not improve this particular shared-pool algorithm. Neither control measures writing quality.

The browser exposes transition weights, temperature, filters, prompt and cap. Readers can inspect each distribution, paginate all outcomes, inspect candidate steps and export the current audit. Edits hide stale results until recomputation.

## Reproduce the checks

The 54 Python tests include all 36 unchanged original tests. Independent references use 90-digit Decimal powers, rational Cartesian path products and rational forward probability/expected-length audits on 40 random tables. Wide beams are checked against exhaustive oracles. Checked-in evidence retains 32 complete audits and 120 staged cases.

Three Node/actual-Chrome tests check 7,927 numerical values, 96 distribution views, 231 displayed outcome rows and 956 candidate rows, plus JSON export, stale-on-edit behavior and 320/390/1280 layout bounds. These are comparisons within documented floating-point tolerances, not exact real-arithmetic proofs. Python 3.10-3.13 CI and an installed wheel outside the checkout reproduce the audit. The wheel check verifies five module origins and both the audit and original generation commands.

Nine original files remain byte-exact, including the original 36-test file, tokenizer, metrics/reports, corpus and offline demo. The original generation/compare commands remain. Corrected nucleus normalization and short-context start padding intentionally change affected policies; original fixed greedy/demo assertions still pass.

## Limits and prior work

The examples are original synthetic Markov tables and a corpus-trained n-gram stand-in, not a neural model or language-quality benchmark. Diversity and repetition metrics do not establish factuality, coherence or safety. A common seed gives reproducibility, not a causal comparison or a representative distribution.

Exhaustive enumeration is exponential and bounded. Tiny tails can underflow; near-cutoff membership can depend on rounding. The width failure depends on the documented beam semantics. Temperature, nucleus sampling and beam search are prior work, not new algorithms here. The contract and demo link Holtzman et al., Higham's shifted-softmax discussion, Hugging Face generation documentation, OpenAI GPT-2 sampling, LabML and Raschka.

## Links

- [Interactive probability inspector](https://midya8.github.io/decodelab/)
- [Source and tests](https://github.com/midya8/decodelab)
- [Numerical and stopping contract](https://github.com/midya8/decodelab/blob/main/AUDIT.md)
- [Implementation PR](https://github.com/midya8/decodelab/pull/2)
- [Plain-language documentation review](https://github.com/midya8/decodelab/pull/4)
