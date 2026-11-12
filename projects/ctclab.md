# CTCLab

CTCLab makes two parts of CTC inspectable: summing paths for a target, and losing paths during prefix search. The target atlas computes likelihood, posteriors and logit gradients from synthetic logits. The prefix inspector uses exact rational frame probabilities to track surviving and discarded mass. Neither runs a speech model.

[Target atlas](https://midya8.github.io/ctclab/) · [Prefix inspector](https://midya8.github.io/ctclab/prefix.html) · [Source and CLI](https://github.com/midya8/ctclab)

## A path is not a transcript

Take two uniform blank/A frames. The greedy path is blank,blank, with mass 1/4. But three of the four paths collapse to A, so A has transcript mass 3/4. Choosing the best path and summing a transcript's paths answer different questions.

The target atlas uses dependency-free Python for blank-expanded-state log-space forward/backward. A separate exhaustive oracle enumerates all frame paths and groups their collapsed transcripts. Independent scalar JavaScript recomputes the editable specification and exposes every state, gradient, path and transcript record, with a posterior lattice and JSON export.

Adjacent repeated target labels need a separating blank. Empty input supports only an empty target. Ordinary probability can underflow while log likelihood stays finite. Impossible targets keep loss and gradients undefined rather than silently replacing them with zero.

## What the beam loses

The prefix inspector asks which paths survive each search cut. It accepts rational frame laws, keeps separate blank/nonblank endpoint masses, and records every positive transition, candidate prefix, first-cut loss and final transcript. Python uses Fraction; the independent browser engine uses BigInt.

Pruning is permanent for paths. A discarded prefix can reappear through new paths, but its old contributions never return. Some published prefix-search variants recover discarded contributions; this one does not. The unpruned transcript oracle is separate from the finite beam.

A selected five-frame development control makes the distinction concrete. Width 3 chooses the true MAP transcript with full mass 47403/226100. Width 4 chooses another transcript with lower full mass, 11691/56525, despite retaining more total path mass. Width 64 retains the whole law. This is a counterexample to monotonic finite-width quality, not evidence that narrower beams are generally better.

For the chosen transcript, let L be retained mass, R the largest retained mass of any other transcript, and D total discarded mass. The strict bound L > R + D certifies a unique MAP transcript under the supplied law. Failing the bound gives no conclusion about whether the answer is wrong. It is not a confidence or speech-correctness certificate.

## Checks and reproduction

The current repository passes 34 Python tests and 6 Node tests. Both isolated wheel checks run outside the checkout. The original target-mode subset has 25 Python tests; it is included in the current total, not an additional suite.

Target checks include 90 seeded 90-digit Decimal controls, 40 independently enumerated state-sequence controls and 300 central finite-difference gradient coordinates. Twenty retained reports match 5,764 numeric and 650 other leaves in independent JavaScript. Actual Chrome checks complete records, 176 state rows, 142 gradient rows, 449 path rows, 143 transcript rows, 176 posterior circles and 205 transition lines, plus stale/error input, export and narrow layouts. Its installed wheel reproduces all 20 reports, the console CLI and four module origins.

Prefix checks include 120 seeded path cases, 384 exhaustive binary-law cases, the maximum four-symbol/six-frame boundary and 270 altered report leaves. A separate verifier reconstructs reports from frame-path enumeration without importing the generator. JavaScript agrees on 155 complete reports. Actual Chrome exercises 36 control/width reports and 114 frame views at 1280, 390 and 320 pixels; twelve completed downloads pass native verification. The installed wheel checks nine module origins, both prefix CLI entrypoints, all twelve controls and 24 forged-report refusals.

```sh
python -m unittest discover -s tests -v
npm test
python tools/build_audits.py
PYTHONPATH=. python tools/build_prefix_controls.py
bash tools/wheel_smoke.sh
bash tools/prefix_wheel_smoke.sh
```

Both generated evidence sets rebuild without changing tracked files. Fresh baseline, revised, published and merged trees passed these checks for the [README review](https://github.com/midya8/ctclab/pull/3). The deployed inspectors match the merged assets and pass the full six-test Node suite.

## Two contracts, separate limits

The target atlas accepts at most six frames, four classes and 1,024 complete paths. It uses floating-point log-space calculations and disclosed 1e-8-nat ranking buckets, with raw scores retained. Target-conditioned alignments are latent model quantities, not observed timestamps or causal explanations. [Target method and conventions](https://github.com/midya8/ctclab/blob/main/METHOD.md) explains reductions, backward messages and impossible targets.

The prefix inspector accepts at most 4,096 complete paths and beam widths 1-64. Its serialized entrypoints reject duplicate keys, float/exponent tokens and noncanonical fractions. Exact arithmetic removes rounding error for the supplied law, not search approximation. Replay verifies internal consistency, not authenticity or model calibration. [Prefix method and variant boundaries](https://github.com/midya8/ctclab/blob/main/PREFIX.md) gives the recurrence, proof and source differences.

Both are bounded audits of synthetic development controls. There is no trained recognizer, held-out speech evaluation, new CTC algorithm, production-scale result, speed claim, paid API or private dataset.

## Attribution

CTC is established work by Graves et al. The source documents link the primary paper, framework contracts and decoding explanations, and distinguish recovery variants from strict path pruning. Implementation and synthetic controls are original to this project. No third-party implementation code, model weights, audio, datasets or diagrams were copied.
