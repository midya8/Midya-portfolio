# RAGLine

## RAGLine: a zero can win

An opt-in fixed-corpus signed-vector postings backend runs the actual retrieval loop. An unvisited, implicit zero can outrank a negative match; shared-bin products can cancel to zero. Complete raw-score stable ranking stays intact before slicing and six-decimal score display. The original scan remains the default, with unchanged extraction, citations and lexical grounding.

49 Python tests retain all 31 originals byte-for-byte. Independent dense references cover 729 exhaustive signed-cube controls, 400 seeded real-vector matrices and 1,350 actual hashed-pipeline query/k comparisons. Four Node/actual-Chrome tests check 24 complete integer-engine reports plus 200 seeded native/browser reports, all 186 rows, 1,161 products and 186 signed SVG marks, stale/invalid state, 320/390/1280 containment and two trusted exports replayed natively. A separate installed wheel checks nine module origins, API/module/console reports, 45 real-pipeline fixture comparisons and both CLI gate sides.

The browser is a bounded integer-vector ENGINE reference, not text/IDF pipeline parity. Native text-pipeline comparisons use the original scan within each supported Python runtime. A constructed 32×64 control visits one posting versus 2,048 dense dot-coordinate products, but query still makes all row scores and fully sorts the corpus. These are structural counts, not time, memory or semantic-quality gains. Construction retains a dense snapshot plus postings and cached norms; rebuild after corpus/fit changes. Signed collisions, extractive copying and lexical grounding retain their original limits. No new method or retrieval-quality claim.

[Live engine inspector](https://midya8.github.io/ragline/) · [Source](https://github.com/midya8/ragline) · [Contract, limits and credited sources](https://github.com/midya8/ragline/blob/main/POSTINGS.md)

### Reproduce the real retrieval backend

```bash
python -m ragline.cli ask --question "How does TCP provide reliable delivery?" --backend postings --require-grounded
python -m ragline.cli evaluate --backend postings --min-recall 1 --min-mrr .9 --min-grounded 1
python -m unittest discover -s tests -v
node --test tests/test_postings_browser.cjs tests/test_postings_chrome.cjs
bash tools/postings_wheel_smoke.sh
```

The earlier scan, original eight-question fixture and their limitations are retained below. The integer-engine controls are not a second quality evaluation.

---

Retrieval-augmented answering built from scratch in pure Python, with citations and verifiable grounding.

## Problem

Retrieval-augmented generation is the standard answer to hallucination, but most demonstrations outsource every step that matters - the embeddings, the vector store, and the language model - and never check whether the answer is actually supported by what was retrieved. RAGLine builds the retrieval-and-verification loop itself and makes grounding a checkable, gateable property: every answer cites the chunk it came from, and a lexical-overlap check scores the answer against that citation.

## Approach

- **Deterministic corpus** - documents are expanded from fixed templates by one seeded RNG, then chunked into paragraph windows with stable ids, so a seed reproduces the corpus, the rankings and the answers bit for bit.
- **Sparse embeddings, no model** - token-hashed TF vectors (signed hash buckets) with IDF weights computed over the chunk set; cosine similarity is the retrieval score.
- **Extractive answering with citations** - the best-matching sentence from the top-k chunks becomes the answer, returned with its chunk id. There is deliberately no generator: the project isolates retrieval and verification.
- **Grounding as a gate** - the check scores the fraction of answer content tokens present in the cited chunk. Correct citations pass at 100% overlap on the fixture; in the suite's negative control, corrupting the citation to an unrelated chunk makes the check flag the answer. The check is lexical: it catches these tested wrong-citation cases, not arbitrary misinterpretation.

## Verification

- 31 unit tests cover corpus determinism and chunking, tokenizer and IDF behavior, cosine properties, ranking determinism and ordering, answer citation validity, both grounding directions (correct citations grounded, corrupted or missing citations flagged), fixture metrics, and every CLI gate.
- Fixture evaluation over 8 questions with known topics: recall@3 = 1.00, MRR = 0.94, grounded-answer rate = 1.00, pinned by CI gates `--min-recall 1.0 --min-mrr 0.9 --min-grounded 1.0`.
- `bash examples/demo.sh` runs fully offline: grounded answers with citations, the gated evaluation, and a negative control proving an impossible gate fails.
- CI runs the same suite across Python 3.10-3.13.

Bounds worth stating: answers are extractive - a copied sentence, never generated text - because the no-dependency rule excludes a language model. The embedding is lexical, so paraphrases sharing no content tokens will not match. The grounding check is lexical overlap with the cited chunk; it catches the tested wrong-citation cases and unsupported wording, not misreadings of a correctly cited source.

## Links

- Repository: [midya8/ragline](https://github.com/midya8/ragline)
