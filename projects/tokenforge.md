# TokenForge

Byte-level BPE tokenizers trained from scratch, with no dependencies.

## Problem

Every language model reads text through a tokenizer, but the tokenizer usually arrives as a black-box artifact: an opaque vocab file produced by a training run nobody can reproduce. When merges cannot be rebuilt deterministically, token ids drift between pipelines, cached artifacts go stale silently, and "why is this word three tokens?" becomes guesswork.

## Approach

TokenForge implements the full byte pair encoding pipeline in dependency-free Python:

- base vocabulary of the 256 byte values, so any text - ASCII, Unicode, emoji - encodes and decodes exactly;
- regex pre-tokenization (words, numbers, symbol runs, whitespace, contractions) in the style of GPT-2, so merges never cross those boundaries;
- deterministic training: exact adjacent-pair counts over pre-token sequences, most-frequent pair merged first, ties broken on the pair itself, stopping at the requested vocabulary size or the minimum pair frequency;
- rank-ordered encoding: the same merges applied lowest-rank-first at encode time, which keeps the token stream identical to the one training produced;
- merges persisted as plain JSON that can be diffed, reviewed and rebuilt byte for byte;
- compression statistics (bytes per token, unique tokens, most frequent tokens) as terminal, JSON and Markdown reports, with a `--min-compression` gate that fails CI when a tokenizer regresses.

## Verification

- 40 unit tests cover pre-tokenization, pair counting and merging, deterministic training, vocabulary caps and minimum counts, encode/decode round trips across ASCII, Unicode and emoji, save/load, statistics math, Markdown escaping, and the CLI end to end including both sides of the compression gate.
- `bash examples/demo.sh` runs fully offline against the bundled corpus: it trains a 300-token vocabulary, verifies an encode/decode round trip, asserts the compression statistics, and checks both sides of the quality gate.
- CI runs the same suite across Python 3.10-3.13.

Byte-level BPE is the tokenizer family used by GPT-style models; TokenForge is a from-scratch teaching-and-tooling implementation, not a drop-in replacement for production vocabularies. The pre-tokenization pattern is ASCII-oriented and simplified relative to GPT-2's Unicode-aware split.

## Links

- Repository: [midya8/tokenforge](https://github.com/midya8/tokenforge)
