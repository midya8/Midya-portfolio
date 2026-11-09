# KVLens

[Live attention and cache inspector](https://midya8.github.io/kvlens/) ·
[Source and reproduction](https://github.com/midya8/kvlens) ·
[Equations, state contract and sources](https://github.com/midya8/kvlens/blob/main/CACHE.md)

A cache is state, not a shortcut in the answer. This offline project implements
one untrained causal multi-head attention block and checks its actual logits,
every retained key/value, absolute position and counted operation against four
independently executed paths.

## The comparison needed a stronger baseline

The original full-recompute path calculates every old query's attention, although
this single-block model only uses the last row. A new final-query-only no-cache
path drops that unnecessary work. Optimized prefill uses the same shortcut;
the two original positive-budget paths and all 28 original tests stay intact.

For vocabulary 16, width 8, two heads, seed 1, prompt [0,1,2,3] and eight predictions:

| path | counted operations |
|---|---:|
| historical full | 34,944 |
| final-query no-cache | 21,376 |
| historical cache | 9,408 |
| optimized cache | 8,832 |

Historical-cache versus historical-full saves 73.08%; optimized-cache versus the
stronger no-cache baseline saves 58.68%. These are named comparisons with
different prefill policies, not an isolated effect or measured speedup. The old
32-token historical fixture remains 500,224 versus 45,888 (90.8% to one decimal),
with the same original CI gate. One prediction offers no reuse within either
matched pair; zero predictions perform no work and have no savings percentage.

## Make every value inspectable

The separate scalar JavaScript engine computes seven complete seeded model
weight inputs locally. Edit the prompt and prediction budget; follow every
prediction, head and position through Q/K/V, scaled score terms, softmax weights,
weighted values, output projections and all vocabulary-logit contributions.
Complete cache states before/after each step and seven-component operation ledgers
are visible. All model weight matrices are available, with full audit and full
model JSON downloads. Static input specifications and pinned costs/tokens are
not a replacement for inference; the browser computes all intermediate tensors.

The final emitted token is not fed back because the requested generation has
ended. For G>0 predictions from L prompt tokens, L+G-1 positions are processed.
Retained K/V state has 2 × positions × width elements; multiplying by eight gives
an ideal packed binary64 payload, not actual Python/browser memory or traffic.

## Fix the state bug, then test the lifecycle

Prefill on occupied state previously appended new rows while restarting positions
at zero. It now fails before mutations or counter changes. Owner/shape/token
checks reject incompatible state; deep forks keep parent and sibling rows
independent. Weights must stay fixed. Same-object weight changes are not
fingerprint-detected; mutable state guards are not a security boundary.

A strict bounded JSON audit CLI rejects duplicate/unknown fields, nonfinite
numbers, invalid IDs/types, excessive depth and oversized input, with exit 2,
stderr and no partial output. Browser edits clear stale tables and disable
exports until a valid recomputation. Unsupported browser models are rejected,
not silently replaced with other weights.

## Verification and reproduction

- 55 Python tests on 3.10-3.13, retaining all 28 unchanged originals, hand-computable
  attention, per-component counter reconciliation, 36 randomized configurations,
  zero/one-prediction controls, forks, occupied-prefill atomicity and strict errors.
- Three Node/actual-Chrome tests compare 32 complete native reports, 97 predictions
  and 66,940 full-report numeric entries. Chrome checks every displayed cell across
  227 head-step views and 1,279 attention-position rows, every weight table, two
  complete JSON exports, invalid clearing, keyboard and 320/390/1280 layouts.
- Isolated installed-wheel reproduction verifies five module origins, all 32
  reports, original complete curve/equivalence, lifecycle/fork checks, audit and
  all four original CLI modes outside checkout. Full model/spec regeneration
  uses normalized tolerance 1e-12 and restores checked-in bytes.

```bash
python -m unittest discover -s tests -v
node --test tests/*.cjs
python scripts/verify_regeneration.py
bash examples/verify_wheel.sh
python -m kvlens.audit --input examples/audit.json
```

## Limits and attribution

This is standard attention/cache reuse, not a new algorithm, trained language
model, production cache or GPU benchmark. Original native paths agree bitwise
on checked inputs; cross-runtime native/browser parity uses normalized tolerance
1e-11 and actual greedy-decision checks, not a universal bitwise proof.

Counts charge two operations per dot-product term, including accumulation, but
exclude embeddings, positional functions, score scaling, softmax, bias adds,
validation and report copying. They do not measure latency, bandwidth, throughput
or hardware instructions. The final-query shortcut applies to this single block;
it does not skip representations that deeper layers need for their own K/V.
No cache eviction, batching or paged storage is claimed. Sources include the
original attention paper, Hugging Face cache docs, NVIDIA's inference guide,
independent cache/roofline explanations and Brown teaching notes, with specific
attribution and distinctions in the linked contract.
