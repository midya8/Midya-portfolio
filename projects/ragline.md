# RAGLine

Retrieval-augmented answering built from scratch in pure Python, with citations and verifiable grounding.

## Problem

Retrieval-augmented generation is the standard answer to hallucination, but most demonstrations outsource every step that matters - the embeddings, the vector store, and the language model - and never check whether the answer is actually supported by what was retrieved. RAGLine builds the retrieval-and-verification loop itself and makes grounding a checkable, gateable property: every answer cites the chunk it came from, and a verifier confirms the answer against that citation.

## Approach

- **Deterministic corpus** - documents are expanded from fixed templates by one seeded RNG, then chunked into paragraph windows with stable ids, so a seed reproduces the corpus, the rankings and the answers bit for bit.
- **Sparse embeddings, no model** - token-hashed TF vectors (signed hash buckets) with IDF weights computed over the chunk set; cosine similarity is the retrieval score.
- **Extractive answering with citations** - the best-matching sentence from the top-k chunks becomes the answer, returned with its chunk id. There is deliberately no generator: the project isolates retrieval and verification.
- **Grounding as a gate** - the check scores the fraction of answer content tokens present in the cited chunk. Correct citations pass at 100% overlap on the fixture; the suite proves the check fails when a citation is corrupted to point at an unrelated chunk.

## Verification

- 31 unit tests cover corpus determinism and chunking, tokenizer and IDF behavior, cosine properties, ranking determinism and ordering, answer citation validity, both grounding directions (correct citations grounded, corrupted or missing citations flagged), fixture metrics, and every CLI gate.
- Fixture evaluation over 8 questions with known topics: recall@3 = 1.00, MRR = 0.94, grounded-answer rate = 1.00, pinned by CI gates `--min-recall 1.0 --min-mrr 0.9 --min-grounded 1.0`.
- `bash examples/demo.sh` runs fully offline: grounded answers with citations, the gated evaluation, and a negative control proving an impossible gate fails.
- CI runs the same suite across Python 3.10-3.13.

Bounds worth stating: answers are extractive - a copied sentence, never generated text - because the no-dependency rule excludes a language model. The embedding is lexical, so paraphrases sharing no content tokens will not match. The grounding check verifies token overlap with the cited chunk; it catches wrong citations and unsupported wording, not misreadings of a correctly cited source.

## Links

- Repository: [midya8/ragline](https://github.com/midya8/ragline)
