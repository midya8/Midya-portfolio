# StructGate: local masks and future acceptance

StructGate compares local viability masking with exact finite-horizon conditioning for a supplied first-order source and total DFA. The default word 01 has source probability 1/20, viability-mask probability 1/2 and global conditional probability 1/10. Inspect every future mass, transition, selected-word prefix and forward marginal. The original JSON/schema inspector and all source-model paths stay unchanged.

## DFA conditioning and future mass

64 Python tests retain all 54 previous tests; six Node/actual-Chrome tests retain all three previous tests. Independent complete-word checks cover 60 seeded small DFAs and all source/local/global marginals. Native Fraction backward recursion and independent BigInt full forward-kernel propagation agree on 24 complete reports, 2,043 future rows, 6,550 symbol rows and 2,239 marginal rows. Chrome checks all 156 selected-word prefixes, 24 responsive views and two trusted downloads. An isolated eleven-module install reproduces all new reports through API, module and console, while the original nine-module wheel/demo/evaluation/gates remain intact.

At most four symbols, eight DFA states and 32 emitted symbols. Zero-probability conditioning stays undefined; syntactically viable source-zero branches retain local failure mass. The 32-symbol ending control represents 4,294,967,296 possible source words with 192 transition rows, a structural count rather than a speed, RAM or scaling benchmark. Standard finite-state/Doob conditioning, not a new algorithm, random sampler, arbitrary JSON/CFG solver or LLM-quality result. Aggregated marginals are not full-word total variation.

[Live DFA conditioning inspector](https://midya8.github.io/structgate/automaton.html) · [Source](https://github.com/midya8/structgate) · [Exact contract and credited sources](https://github.com/midya8/structgate/blob/main/AUTOMATON.md)

## Original model masking and trie conditioning

The original character-model inspector separates legal prefixes from conditional sequence distributions.

- Repository: [midya8/structgate](https://github.com/midya8/structgate)
- Live: [Full-model mask and conditioning inspector](https://midya8.github.io/structgate/)
- Method: [CONDITIONING.md](https://github.com/midya8/structgate/blob/main/CONDITIONING.md)
- Reviewed implementation: [Support-aware masking and exact finite-language conditioning](https://github.com/midya8/structgate/pull/2)

## Mask cost and support

For source next-character distribution p, legal mass Z and masked renormalization q, -log Z is KL(q || p), not KL(p || q). The reverse is infinite whenever the mask excludes positive source mass. Empty masks do not define a distribution. The inspector retains all excluded probabilities, both directions and explicit infinite/undefined status. Both validators now return an empty mask after failure.

Per-step conditional KL is separate from a sampled path log-ratio or an expected sequence KL. Means from different masking modes visit different prefixes, so their ordering is descriptive, not a causal effect of a smaller legal set.

## Original model and historical paths

The browser runs the original order-3 smoothed character n-gram from all 287 context count rows and its 46-character vocabulary, trained on all 200 original synthetic records. It independently recognizes prefixes with a recursive parser rather than the Python streaming state machine. There is no inference service or prerecorded output substituted for model calculation.

All 40 seeds in each of none/grammar/schema remain, including failures: 120 full paths and 3,729 actual emitted characters. Recorded Python random uniforms are replay inputs; every next-character distribution, mask, choice, state and KL term is recomputed. Every decision and all 46 probability rows are selectable. Three JSON exports return the full prefix report, every trace step and the entire rational experiment.

The one-character budget control exhibits a legal incomplete prefix. EOF acceptance is separate from the historical streaming stop state: a root number can be complete JSON at EOF without the machine having consumed its closing boundary.

## Exact finite-language controls

The separate supplied finite-language experiment computes h(prefix), the source probability that a future suffix completes an accepted word. Local masking uses p/Z; exact conditioning uses p(next) h(next)/h(prefix). Python Fraction and independent JavaScript BigInt return all prefixes, transitions and accepted words. Every conditioned path also has the direct P(word)/P(event) check.

Six labeled constructed controls cover future acceptance distortion, an unrestricted identity, a locally stranded source-zero branch, a zero-probability event, a three-symbol language and a one-token case. Local dead-end mass stays in a failure sink; full total variation includes it. A source-zero conditioning event is explicitly undefined, not an all-zero probability distribution.

This is exact rational computation for 1-4 ASCII alphanumeric symbols and up to 128 supplied equal-length words of length 1-8 under a first-order Markov source. It is not arbitrary-CFG or JSON conditioning, ASAp, or an efficient LLM sampler.

## Preserved evidence

- 54 Python tests on 3.10-3.13 retain all 32 original tests byte-for-byte, plus exact direct-enumeration references for 24 random small languages, KL/support, EOF and error-path checks.
- Three Node/actual-Chrome tests compare 1,251 full prefix reports, all 289 source-context cases, all 120 historical paths, six exact controls and 741,236 numeric entries.
- Chrome recomputes and renders all 171,534 historical step-table rows; checks three actual JSON downloads, invalidation, keyboard and 320/390/1280 layouts.
- Isolated installed reproduction outside checkout checks nine module origins, every path/control, all three audit CLIs, original evaluation CLI and unchanged gates.
- The full original fixture remains none 3/40, grammar 40/40 and schema 40/40, with mean per-step mask cost 1.3496 grammar and 0.8209 schema. The negative control is not weakened. Source model, corpus, CLI and original demo remain unchanged.

## Limits and attribution

The source is a small character model that generates structured nonsense, not a useful-scale LLM. Prefix legality is not completion within a finite budget, semantic truth or safe downstream use. The historical flat fixed-order record is not JSON Schema: unicode escapes and fractional-exponent numbers remain visible unsupported cases rather than silently changing the old fixture. General JSON syntax can also represent numbers outside binary64 range.

[CONDITIONING.md](https://github.com/midya8/structgate/blob/main/CONDITIONING.md) attributes Grammar-Aligned Decoding, Local and Global Decoding, RFC 8259, ECMA-404, Wolfram MathWorld and Pierre C Bellec's Doob-transform exposition. Standard methods, not a new algorithm. These finite controls do not reproduce the papers' LLM results or imply output-quality gains.
