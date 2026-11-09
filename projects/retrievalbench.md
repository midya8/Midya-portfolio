# RetrievalBench

A cutoff is a policy. Offline BM25 retrieval evaluation with complete arithmetic and an independent browser inspector.

[Open the inspector](https://midya8.github.io/retrievalbench/) · [Source and CLI](https://github.com/midya8/retrievalbench) · [Evidence contract](https://github.com/midya8/retrievalbench/blob/main/EVIDENCE.md)

## What the inspector exposes

Every retrieval unit retains full text, explicit parent identity, token windows and complete query-term tf/qtf/df/IDF, length normalization, saturation and score contributions. The complete ranking includes zero-score ties and every admitted/discarded duplicate. Metric rows expose grades, exponential gains, discounts, cumulative DCG and the full ideal denominator, including judged ids absent from the corpus.

Taking k units before collapsing duplicate parents can return fewer than k documents. Scanning to k distinct parents is a different budget. Both use the same fixed ranking here. Whole-document versus chunk indexing changes corpus statistics too, so it is not an isolated effect of shorter text. Neither comparison proves search quality.

Editable corpus/query/judgments, units, budget, cutoff, BM25 parameters and chunk overlap are recomputed by independent scalar JavaScript. Stale results hide until recomputed; JSON export contains the actual current report. Everything runs locally without a model or paid API.

## Corrections with the original protocol retained

Parent identity is no longer guessed by splitting a '#c' delimiter. Duplicate ids, qrel pairs and metric rankings are rejected. Nonfinite/Boolean parameters and invalid gates fail clearly; large finite BM25 parameters and high-grade nDCG avoid intermediate overflow. The default CLI still takes k units before parent collapse. Original whole/chunked JSON outputs, 12-document/six-query corpus, all 42 tests and demo are retained unchanged.

## Verified

- 68 Python tests on Python 3.10-3.13, including 200 Decimal BM25 comparisons and exhaustive small-ranking metric controls.
- 35 complete reports, independently compared across 27,694 numeric and 12,052 other scalar leaves.
- Actual Chrome checks all 268 units, 1,384 contribution rows and 89 selected-policy metric rows, both budgets, all full source text, ideal denominators, invalidation/export and 320/390/1280 containment.
- Isolated installed wheel verifies eight module origins, all reports, audit CLI and original gated CLI outside the checkout.

## Limits and prior work

BM25, chunking and ranked metrics are prior work, not a new algorithm. The original illustrative perfect recall is not a research result. The inspector is bounded ASCII/binary64 arithmetic, not arbitrary precision or a semantic oracle. No Lucene/trec_eval score-equivalence claim. Judgment incompleteness and lexical mismatch remain. Full definitions, sources, bounds and preserved evidence are in the [evidence contract](https://github.com/midya8/retrievalbench/blob/main/EVIDENCE.md).
