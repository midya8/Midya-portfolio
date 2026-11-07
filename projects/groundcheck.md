# GroundCheck

Offline grounding checks for answers against their sources.

## Problem

RAG pipelines answer with confidence whether or not the answer is grounded in the retrieved documents. Fabricated figures, citations that point at nothing and claims no source supports all read identically in a chat transcript. Reviewing every answer by hand does not scale, and "the model said so" is not verification.

## Approach

GroundCheck turns grounding into deterministic, offline lexical checks against the exact sources an answer claims to use:

- **Citation validation** - every `[n]` marker must resolve to a provided source; unresolvable citations are high-severity findings, and the report shows how many of the provided sources were actually cited.
- **Lexical support scoring** - each answer sentence is scored by content-token containment (stopwords removed) against every source document. Support is measured at document granularity because answers draw on whole retrieved passages: a sentence combining facts from several sentences of one passage is supported by that passage. Sentences below the threshold are flagged.
- **Numeric consistency** - every number in the answer must appear in the sources, by exact or equal-value match. Invented figures are the most common grounding failure and the easiest to catch mechanically. Decimal handling keeps `1.57` one number rather than two sentence fragments.
- **Reports and gates** - terminal summaries, JSON artifacts for tooling, Markdown reports with per-sentence support tables, and three CI gates: `--min-support` (mean sentence support), `--max-unsupported` (unsupported sentence count) and `--max-findings` (total findings).

## Verification

- 43 unit tests cover tokenization, decimal-safe sentence splitting, number extraction and matching, citation parsing, source loading validation, support scoring including cross-sentence combinations, every finding kind, report escaping and the CLI end to end including all three gates.
- `bash examples/demo.sh` runs fully offline: a grounded answer passes every gate while an ungrounded one - a fabricated test count, a citation with no source, invented claims - is rejected, with JSON and Markdown reports asserted for both.
- CI runs the same suite across Python 3.10-3.13.

GroundCheck measures lexical grounding: token containment, citation resolution and number presence. These are useful fabrication signals but not semantic entailment, and they cannot establish that a claim is actually supported. Documented cases that pass every check: negation ("does not contain 40 tests" scores supported, since containment ignores word order), wrong attribution (a number that belongs to one project assigned to another), and coincidental number matches (a figure appearing anywhere in the sources, even in an unrelated sentence). A fully paraphrased true sentence can also score below the threshold. Treat it as a tripwire for ungrounded output, not proof of correctness.

## Links

- Repository: [midya8/groundcheck](https://github.com/midya8/groundcheck)
