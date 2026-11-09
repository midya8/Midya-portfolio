# GroundCheck

A citation is not evidence. GroundCheck exposes the lexical machinery behind that distinction in a complete, editable provenance inspector.

## What is implemented

The original offline CLI remains available: citation validation, best-document content-token containment, number presence, JSON/Markdown reports and CI gates. A new bounded ASCII audit retains every raw sentence unit, content-token occurrence, citation resolution, source-score fraction and equal-valued numeric occurrence with exact input offsets. Every source text is shown in full, including sources outside the current policy.

The inspector independently recomputes the full report in scalar JavaScript. Switch between all provided sources and only citations in the same raw unit, edit the answer/sources/threshold, inspect all documents and export the current JSON. Neither policy unions documents. A resolved citation can point to the wrong passage; negation and wrong attribution can pass both policies.

## Correctness work

- Exact decimal-string equality replaces float conversion, which collapsed adjacent large integers and distinct 310-digit finite numbers.
- Numbers before terminal periods are recognized without treating dotted versions as numeric evidence.
- Scores retain full precision before thresholds and gates. A displayed 0.6667 is not allowed to pass a 0.66668 gate when its actual value is 2/3.
- Explicit bounds, invalid-input handling, stale-result hiding and safe text rendering keep the browser computation inspectable.

## Verification

66 Python tests retain all 43 originals unchanged. The 50 retained reports cover 25 controls in both scopes: wrong/missing/post-period citations, semantic false positives, split-document claims, exact decimal collisions, zero-content inputs and tie rules. Exact Fraction comparisons and exhaustive small token subsets check the arithmetic. Python 3.10-3.13 runs regenerate the same artifacts. Four Node/actual-Chrome tests check full-report parity, every displayed source score, edits/export and 320/390/1280 containment. An isolated installed wheel verifies eight module origins and both audit/original CLI paths outside the checkout.

## Limits

Lexical support is not semantic entailment, factuality or source authentication. These are synthetic controls, not a RAG-quality benchmark. Audit offsets/parity use an explicit bounded ASCII profile; the original CLI keeps its Unicode behavior. Citation attachment is an explicit same-raw-unit convention, not a general citation parser. Numeric comma grouping is not validated and exponent notation is not recognized as one number. Empty/stopword-only inputs can have vacuous support, not evidence.

## Links

- [Repository](https://github.com/midya8/groundcheck)
- [Live provenance inspector](https://midya8.github.io/groundcheck/)
- [Evidence contract, prior work and limits](https://github.com/midya8/groundcheck/blob/main/EVIDENCE.md)
