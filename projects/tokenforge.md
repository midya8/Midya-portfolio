# TokenForge: same merges, different work

Optional occurrence-indexed BPE training with exact original merges and saved artifacts. Live pair sets, linked positions and a lazy heap replace repeated recounting, while the unchanged scan stays the default. An independent browser recounts every overlapping frequency, numeric tie and leftmost replacement on explicit byte rows. Structural work is not a speed, RAM or complexity result.

## Occurrence indexing and overlapping frequency

49 Python tests retain all 40 originals; 4 Node/actual-Chrome tests check 27 full reports, 160 merge selections, 3,033 displayed pair rows, 24 responsive views and trusted exports. Independent Python and JavaScript small-row oracles each cover 2,555 settings, plus 250 native seeded multirow cases. An installed wheel reproduces original and new CLI modes outside the checkout. The original 1,227-byte corpus gives 44 identical merges and saved JSON bytes.

The browser validates semantic histories, not native heap operations or Python regex parity. Overlapping pair frequency differs from replacement gain: five equal bytes have four adjacent matches but only two first-round replacements. Trace copying, sorting, set/link storage and stale heap entries cost work and memory. Established BPE/indexing/heap ideas are credited; no imported complexity theorem, production quality or global compression optimum is claimed.

## Work witnesses and publication

The original full-corpus scan visits 30,664 adjacent positions. The index records 985 initial edges, 1,014 removals, 568 insertions, 446 snapshot positions/replacements and 117 heap pops, 73 stale. These are different operation units, not a speedup ratio. Optional tracing copies 13,857 pair records and 82,178 token entries separately. The browser uses a different full-recount algorithm and ships inputs only. Native work counts are not validated by JavaScript.

Feature/PR, merged-main and Pages checks passed. All six deployed assets and 24 public/deployed unmasked captures match checked source. Actual deployed exports replay natively exactly. The original trainer, split, stats, 40-test source, corpus and offline demo are byte-exact. This is an optional backend in the existing TokenForge, not a duplicate project or online training.

[Live merge inspector](https://midya8.github.io/tokenforge/) · [Source](https://github.com/midya8/tokenforge) · [Exact contract and sources](https://github.com/midya8/tokenforge/blob/main/INDEXED.md)

## Original tokenizer and checks retained

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
