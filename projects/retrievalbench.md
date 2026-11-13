# RetrievalBench

## BM25 evaluation and exact rank fusion

RetrievalBench ranks documents with BM25, evaluates supplied relevance judgments and combines ranked lists with exact weighted rank fusion. An opt-in fuse-search command runs the original exhaustive BM25 index on explicitly supplied query variants, then fuses admitted prefixes using standard reciprocal rank fusion. Source scores never enter fusion; all original BM25 search, evaluation and audit commands retain their behavior.

The current suite has 80 Python tests, including all 68 earlier tests, and seven Node/actual-Chrome tests, including all three earlier tests. Independent Python Fraction and source-first BigInt arithmetic reproduce 230 complete reports: 2,006 candidate rows, 9,674 candidate/source contribution cells, 6,416 raw entries and 16 actual original-BM25 query-variant pipelines. Native controls include 432 exhaustive permutation/depth/constant comparisons, 200 conservation/order/weight-scaling controls and 100 random actual-BM25 pipeline comparisons. Installed-wheel checks verify nine module origins, every report/pipeline, both new CLI commands and invalid-output preservation.

Every missing versus beyond-depth rank, zero-weight candidate, duplicate ranking, exact fraction and inside/outside cutoff gap stays visible. Final k is separate from source depth. Exact score ties use printable ASCII document-id order, and zero-score candidates remain eligible. Duplicate sources add influence, not independent evidence. The browser replays supplied rankings exactly; it does not claim exact cross-language BM25 logarithms. Standard RRF is credited to Cormack, Clarke and Buettcher, SIGIR 2009. No new method, semantic-relevance improvement, calibrated confidence, speed, causal effect or vendor parity is claimed.

[Live exact fusion inspector](https://midya8.github.io/retrievalbench/fusion.html) · [Source and CLI](https://github.com/midya8/retrievalbench) · [Contract, bounds and inspected sources](https://github.com/midya8/retrievalbench/blob/main/FUSION.md)

### Reproduce the real query-variant pipeline

```bash
python -m retrievalbench fuse --spec examples/fusion.json --json fusion.json
python -m retrievalbench fuse-search --corpus examples/data/corpus.jsonl \
  --query 'bread yeast' --query 'fermentation' --depth 3 -k 3 --json fused.json
python -m unittest discover -s tests -v
npm test
bash tools/wheel_smoke.sh
```

The retained BM25 inspector and its original judgments, metric definitions and limitations are described below. These are development controls, not a relevance benchmark.

---

The BM25 inspector shows every term contribution, retrieval unit, parent selection and per-rank metric calculation.

[Open the inspector](https://midya8.github.io/retrievalbench/) · [Source and CLI](https://github.com/midya8/retrievalbench) · [Evidence contract](https://github.com/midya8/retrievalbench/blob/main/EVIDENCE.md)

## What the inspector exposes

Every retrieval unit retains full text, explicit parent identity, token windows and complete query-term tf/qtf/df/IDF, length normalization, saturation and score contributions. The complete ranking includes zero-score ties and every admitted/discarded duplicate. Metric rows expose grades, exponential gains, discounts, cumulative DCG and the full ideal denominator, including judged ids absent from the corpus.

Taking k units before collapsing duplicate parents can return fewer than k documents. Scanning to k distinct parents is a different budget. Both use the same fixed ranking here. Whole-document versus chunk indexing changes corpus statistics too, so it is not an isolated effect of shorter text. Neither comparison proves search quality.

Editable corpus/query/judgments, units, budget, cutoff, BM25 parameters and chunk overlap are recomputed by independent scalar JavaScript. Stale results hide until recomputed; JSON export contains the actual current report. Everything runs locally without a model or paid API.

## Corrections with the original protocol retained

Parent identity is no longer guessed by splitting a '#c' delimiter. Duplicate ids, qrel pairs and metric rankings are rejected. Nonfinite/Boolean parameters and invalid gates fail clearly; large finite BM25 parameters and high-grade nDCG avoid intermediate overflow. The default CLI still takes k units before parent collapse. Original whole/chunked JSON outputs, 12-document/six-query corpus, all 42 tests and demo are retained unchanged.

## Original BM25 release checks

- At that release, 68 Python tests on Python 3.10-3.13, including 200 Decimal BM25 comparisons and exhaustive small-ranking metric controls.
- 35 complete reports, independently compared across 27,694 numeric and 12,052 other scalar leaves.
- Actual Chrome checks all 268 units, 1,384 contribution rows and 89 selected-policy metric rows, both budgets, all full source text, ideal denominators, invalidation/export and 320/390/1280 containment.
- Isolated installed wheel verifies eight module origins, all reports, audit CLI and original gated CLI outside the checkout.

## Limits and prior work

BM25, chunking and ranked metrics are prior work, not a new algorithm. The original illustrative perfect recall is not a research result. The inspector is bounded ASCII/binary64 arithmetic, not arbitrary precision or a semantic oracle. No Lucene/trec_eval score-equivalence claim. Judgment incompleteness and lexical mismatch remain. Full definitions, sources, bounds and preserved evidence are in the [evidence contract](https://github.com/midya8/retrievalbench/blob/main/EVIDENCE.md).

## Documentation review

The README now explains the five commands directly and labels the earlier BM25 test counts separately from the current fusion suite. The fusion contract uses a descriptive workflow heading. Fresh source, installed-wheel and browser checks retain the same arithmetic, corpus, judgments and limits; this review adds no retrieval-quality result.
