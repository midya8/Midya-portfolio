# RetrievalBench

Offline retrieval evaluation for RAG and search pipelines.

## Problem

Retrieval quality decides what a RAG pipeline can answer, but retrieval changes are rarely measured. Adjusting chunk sizes, overlap or index parameters, or editing source documents, silently shifts which passages a pipeline surfaces. Without golden queries and relevance judgments, a regression ships unnoticed and answers get worse for reasons nobody can see.

## Approach

RetrievalBench builds an exact Okapi BM25 index over a local JSONL corpus, ranks golden queries, and scores the rankings against graded qrels. It is dependency-free and runs fully offline, so retrieval quality becomes a reproducible CI gate instead of a vibes check.

- Exact BM25 with no pruning and no ANN approximation, so scores and rankings are fully deterministic and diffable between runs
- Token-window chunking with configurable overlap; chunk hits collapse back to their parent document so qrels stay at document granularity while the index works at passage granularity
- Per-query and macro-averaged recall@k, precision@k, MRR and nDCG@k from graded qrels, with the weakest queries surfaced for review
- Quality gates (`--min-recall`, `--min-precision`, `--min-mrr`, `--min-ndcg`) that fail CI when a retrieval change drops quality
- JSON reports for tooling and Markdown reports that fit native CI job-summary surfaces, plus an ad-hoc `search` command for spot-checking the index

## Verification

- 42 unit tests cover tokenization, BM25 scoring edge cases (ties, empty documents, unknown terms, length normalization), JSONL loading validation, chunking windows and overlap, every metric, report escaping and the CLI including gates and chunked evaluation.
- `bash examples/demo.sh` runs fully offline against a small AI/ML corpus and asserts the aggregate metrics, the Markdown report, chunked-evaluation parent collapsing, and both sides of the quality gates.
- CI runs the same suite across Python 3.10-3.13.

BM25 is a lexical baseline: it measures term-matching retrieval, not embedding quality. Graded qrels for the example corpus are illustrative judgments, not a research benchmark.

## Links

- Repository: [midya8/retrievalbench](https://github.com/midya8/retrievalbench)
