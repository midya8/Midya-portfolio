# TokenForge: count the pairs, then check the replacements

Train a byte-level BPE tokenizer offline, inspect every merge, and save the model
as plain JSON. The original full-recount trainer stays the default. An optional
occurrence-indexed trainer changes the bookkeeping with live pair sets, linked
positions and a lazy heap, while keeping the same merge rules and saved format.

[Live merge inspector](https://midya8.github.io/tokenforge/) · [Source](https://github.com/midya8/tokenforge) · [Method and source notes](https://github.com/midya8/tokenforge/blob/main/INDEXED.md)

## Occurrence indexing and overlapping frequency

Each pre-token is a separate UTF-8 byte row. Training counts all adjacent pairs,
including overlaps, chooses the highest count, and breaks ties by the smallest
numeric token pair. It replaces leftmost nonoverlapping occurrences. For five
`a` bytes, the first `aa` pair has four matches but only two replacements, leaving
`[256,256,97]`. Frequency and compression gain are different quantities.

The indexed trainer updates only the edges around a replacement. Its heap keeps
old entries until they are popped and checked against current counts. The method
notes explain the adjacency invariant and why the numeric priority preserves the
original choice. Bounded tests support the implementation; they are not a formal
proof of every possible input or an imported complexity theorem.

## Compare work without calling it a speedup

Both trainers produce 44 identical merges and saved vocabulary bytes on the
bundled 1,227-byte corpus. The full-recount trainer visits 30,664 adjacent
positions. The index records:

| Operation | Count |
|---|---:|
| Initial adjacency insertions | 985 |
| Edge removals | 1,014 |
| New edge insertions | 568 |
| Snapshot positions visited | 446 |
| Pair replacements | 446 |
| Heap pushes | 652 |
| Heap pops | 117 |
| Stale pops, included above | 73 |

These are different units, not a ratio. Link arrays, sets, sorting, heap entries
and Python object costs are not a timing or RAM measurement. Stale entries can
accumulate; this backend does not compact the heap. Optional tracing separately
copies 13,857 pair records and 82,178 token entries on that corpus. Small inputs
may favor the simpler scan. This is a new backend in TokenForge, not a duplicate
tokenizer project or continued training on an online corpus.

## Replay the semantic history

The browser takes explicit byte rows and independently recounts every pair,
building fresh output rows rather than running the Python index. Inspect every
selected pair, complete pair table, replacement position and before/after row.
Edits clear stale results and disable downloads. Trusted-click downloads contain
the input and full semantic report, which can be replayed through the native
bounded CLI. No upload or model API is used.

The browser verifies semantic histories, not native heap counters. Its schema is
`tokenforge-indexed-semantic/1`; native output additionally contains
`indexed_work` under `tokenforge-indexed/1`. The original-row control uses Python's
first 12 pre-token rows, while the Unicode control supplies explicit UTF-8 bytes.
Neither establishes cross-language regex splitting parity.

## Checks and limits

49 Python tests retain all 40 original tests. Independent Python and JavaScript
oracles each cover 2,555 small binary-row/cap/count settings; native checks add
250 seeded multirow tables and 39 overlap/boundary cases. The 27 complete audit reports
retain 160 selected merge steps. Four Node/actual-Chrome tests compare those full
histories, 3,033 displayed pair rows, 24 responsive views, strict input failures,
invalidation and two trusted downloads. Installed-wheel checks run outside the
checkout and reproduce original/new CLI modes, all 27 audits and 44 corpus merges.

The original trainer, pre-tokenizer, encoding, statistics, corpus and offline demo
remain. The README's encode/decode example now uses actual encoded ids rather
than ids outside the advertised 300-token vocabulary. Compression gates check
bytes per token on the supplied corpus, not model quality. UTF-8 text encoded by
the tokenizer round-trips; arbitrary valid ids may decode to replacement
characters, and unknown ids fail.

This is established BPE with a simplified ASCII-oriented split, not GPT-2
pre-tokenization parity, a production vocabulary, a global compression optimum
or a representative language benchmark. Gage, Sennrich and colleagues,
subword-nmt, formal BPE analysis, existing indexed implementations and Python's
heap documentation are credited in the method notes. Their algorithm variants,
complexity theorems and benchmark results are not transferred to this backend.
