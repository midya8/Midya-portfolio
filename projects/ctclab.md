# CTCLab

Offline CTC target marginalization with log-space forward/backward, full state/symbol posteriors and logit gradients, plus every exhaustive path and collapsed transcript. The editable independent JavaScript inspector shows why a greedy best path can lose to summed transcript mass: two uniform blank/A frames assign 0.25 to empty output and 0.75 to A. Twenty retained reports, 25 Python tests across 3.10-3.13, Decimal/state enumeration, 300 finite-difference checks and real-Chrome full-record/diagram audits. Established CTC on tiny synthetic logits, not a trained recognizer, speech/OCR benchmark or novel algorithm; numerical rank buckets and impossible-target conventions are explicit.

[Live alignment inspector](https://midya8.github.io/ctclab/) · [Method and limits](https://github.com/midya8/ctclab/blob/main/METHOD.md) · [Source and CLI](https://github.com/midya8/ctclab)

## The question

A frame-level best path is not the same as a highest-mass transcript. How can every contribution to a CTC target likelihood, posterior and gradient remain inspectable?

## Implementation

Dependency-free Python computes blank-expanded-state log-space forward/backward. An independent exhaustive oracle collapses all C^T paths and aggregates transcript masses. Independent scalar JavaScript recomputes the editable specification, with complete state, gradient, path and transcript records, posterior lattice geometry and JSON export. No acoustic model, tokenizer, API or dataset is required.

## Evidence

- 25 Python tests on 3.10-3.13 include 90 seeded 90-digit Decimal controls, 40 independently enumerated state-sequence controls and 300 central finite-difference gradient coordinates.
- Twenty retained reports match 5,764 numeric and 650 other leaves in independent JavaScript.
- Actual Chrome checks 176 state rows, 142 gradient rows, 449 path rows and 143 transcript rows, every complete record, 176 posterior circles and 205 transition lines, invalid/stale input, export and 320/390/1280 containment.
- Isolated wheel reproduction runs outside the checkout, checks all 20 reports, the console CLI and four installed module origins.

## What the controls show

Adjacent repeated labels need a separating blank. Empty input supports only an empty target. Changing blank index must preserve the corresponding computation. Ordinary probabilities can underflow while log likelihood remains finite. Impossible targets retain undefined loss and gradients rather than silently zeroing them. The retained uniform two-frame counterexample separates greedy path decoding from transcript marginalization.

## Limits

At most six frames, four classes and 1,024 paths. This deliberately exponential audit is not a production decoder or speed benchmark. Target-conditioned latent alignments are not observed timestamps or causal explanations. Ranking uses disclosed 1e-8-nat score buckets followed by lexicographic indices, while raw masses and raw greedy gap remain available. Framework reduction/blank conventions and differing backward-message definitions are documented rather than conflated.

## Attribution

Established CTC by Graves et al.; independent implementation, synthetic controls and checks by Midya Rahmani. No external code, model weights, audio, dataset or diagrams copied. Primary paper, official framework contracts, educational and community sources are linked with convention differences in METHOD.md.


## CTCLab 0.2 - what the beam forgot

[Repository](https://github.com/midya8/ctclab) · [Exact prefix inspector](https://midya8.github.io/ctclab/prefix.html) · [Method and limits](https://github.com/midya8/ctclab/blob/main/PREFIX.md)

Exact supplied rational CTC frame laws make prefix pruning inspectable: every positive blank/nonblank transition, surviving prefix, first-cut loss and final transcript. A separate path-enumeration checker reconstructs the entire evidence report, and an independent browser BigInt engine agrees on 155 complete reports. The original floating-point target atlas remains intact.

Twelve original development controls include a selected five-frame counterexample: width 3 chooses the true MAP transcript with full mass 47403/226100; width 4 chooses a lower-mass transcript, 11691/56525, despite retaining more total path mass. Strict permanent path pruning does not restore discarded contributions. The sufficient bound L > R + D certifies a unique MAP only under the supplied independent-frame law; a false bound makes no failure claim.

Reproduction checks: 34 Python tests, 6 Node tests, 120 seeded path cases, 384 exhaustive binary-law cases, 270 altered report leaves, actual Chrome tables at 320/390/1280 pixels and 12 native-verified downloads. An isolated installed wheel checks both prefix CLI entrypoints across all 12 controls and refuses 24 forged reports. The original mode is reproduced too.

These are synthetic controls selected during development, not held-out speech evaluation. At most 4,096 complete paths. No trained recognizer, new CTC algorithm, calibrated confidence, production-scale, quality or speed claim. Exact arithmetic removes rounding error, not search approximation. No paid API, private data or model download.
