# ChainLab: paths, losses and uncertainty

[Public repository](https://github.com/midya8/chainlab)

Exact rational path decisions and whole-path uncertainty, alongside the original floating HMM trainer and prefix-evidence inspector. Four decoders expose different loss objectives; exact state and edge probabilities keep dependence and impossible paths visible. Dependency-free Python, independent browser BigInt and a standalone verifier. Standard HMM inference and decision theory, no new method.


## Three distinct questions

Forward inference sums over paths to score observations. Forward/backward gives
smoothed state and adjacent-state posterior marginals. Viterbi maximizes one
joint path, equivalent to the posterior path for fixed observations. They are
not interchangeable. The model emits the first symbol after sampling its initial
state, then transitions before each subsequent emission.

A path probability must respect initial, transition and emission factors.
The exact three-state one-symbol counterexample has initial .4/.35/.25 and
transition rows [0,.5,.5], [1,0,0], [1,0,0]. On x/x, marginal modes A/A use a
zero-probability transition. The valid best path is B/A with posterior .35.
The posterior rows .4/.35/.25 and .6/.2/.2 cannot be multiplied as independent
path factors. Tests enumerate all paths to check both objectives.

## Numerical representation

Zero probabilities map to negative infinity internally. Log-sum-exp sums forward
and backward alternatives; Viterbi uses maxima and backpointers. No epsilon
smoothing or fallback path. Truly impossible observations raise ValueError.
The one-state rare-symbol example keeps log likelihood -3536.77070284 finite
for256 observations with emission1e-6, while its probability underflows to0.

State and transition posterior outputs exponentiate log factors then normalize
for numerical roundoff. Record the largest raw mass deviation from1. Extremely
small posterior mass may still underflow; no arbitrary precision guarantee.
Input rows retain their values if their sum is within1e-12, otherwise reject.
No silent input normalization or matrix repair. Exact local ties take first
state index; whole-path lexicographic order is not guaranteed by that rule.

## Multi-sequence maximum-likelihood EM

Every sequence starts independently. Sum gamma at each start, xi on within-
sequence edges, and gamma for matching observed symbols. Normalize expected
counts to update initial, transition and emission probabilities. No cross-
sequence edges, pseudocounts or prior objective. A single-state check reduces
to empirical symbol frequencies; a tiny exhaustive-path expected-count reference
checks one whole multi-sequence EM update.

If a transition/emission row has zero expected occupancy, keep its previous
row and report its index. All-length-one data cannot fit transitions. Existing
zero support cannot recover through unsmoothed EM; absent symbols can lose
support. These are explicit limitations, not invisible smoothing choices.

Score every proposal. Accept only nonnegative likelihood changes. A tiny
negative change in[-1e-7,0) stops with rejected_proposal, keeping the previous
model/history. A change below-1e-7 raises an error. Simulated numerical branches
are tested. An accepted improvement<=tolerance stops; tolerance is absolute
nats for the sum over all sequences, not per symbol. Budget<=100 updates. No
stationarity, local/global optimum or identifiability certificate.

## Development fixture and controls

Seed23, two persistent regimes, three categorical emissions,20 training and12
test sequences of40 symbols. Supplied asymmetric initialization,30-update cap,
tolerance1e-6. No parameter/initialization search. Test likelihood does not enter
fit or stopping. The synthetic source, initialization and random seed are all
in the public demo; the fixture was inspected during development.

Training log likelihood improves -820.4336249187 to -651.3909460329 over20
accepted updates, then stops on tolerance. Test NLL per symbol (nats):
initial1.0176377671, iid training-frequency control.9859930334,
trained.7756309219, generating-model reference.7716741802. The generating model
is not learned or guaranteed to beat every finite-sample fit. The iid control
fits symbol frequencies but no transitions. Same observed train/test data, not
equal parameter count or a causal decomposition of transition benefits.

No state-recovery accuracy is reported: latent labels are arbitrary and the
likelihood objective is not ground-truth state identification. Full inference
on test sequences uses future symbols, not an online prediction benchmark.
One selected persistent-regime development fixture does not establish general
rankings, anomaly-detection performance or calibration.

## Prefix filtering and unobserved-future forecasts

```python
from chainlab import filter_sequence, forecast

online = filter_sequence(model, ["x", "y", "x"])
future = forecast(model, ["x", "y"], horizon=3)
```

The `model` is the same validated `chainlab_v1` artifact used by infer/fit.
`filter_sequence` returns a state posterior for each prefix, prior-predictive
symbol probabilities **before** its symbol is observed, each observed symbol's
log predictive score, and prefix log likelihoods. At time0 the prediction uses
the initial state distribution; later steps transition the last filtered state.
It never uses later observations to update an earlier row. This is a batch
prefix audit, not a persistent streaming session or evidence that the supplied
model was trained without future-data leakage.

The difference from smoothing is exact on a two-state example: absorbing states
A/B, initial0.5/0.5, emissions A:[1,0], B:[0.5,0.5] for symbols x/y.

| State inference | Available observations | P(state A at time0) |
|---|---|---:|
| Filtering after first symbol | x | 2/3 |
| Full-sequence smoothing after both | x,y | 0 |

Using the smoothed row for an online decision at time0 would use future y.
The final filtered and final smoothed rows agree because they have the same
evidence at that time. This is a conditioning difference, not a performance
contest between algorithms.

Log posterior messages stay in log space between steps, so a path with a
raw-probability product below binary64 range can still become the only supported
state after a later observation. Printed probability entries can underflow to
zero even with a finite `observed_log_predictive`; the log scores are the
likelihood record, not `log` of the rounded probability table.

`forecast` accepts horizon1-32 and conditions on the whole supplied **past**
sequence. Horizon1 transitions once from the last conditioned state, then
predicts its emission. Each later step propagates states again without
assimilating any guessed observation. Returned state/symbol distributions are
**marginals**, not a joint future path and not independent across horizons.
In the absorbing-state example after x, each future marginal has P(y)=1/6,
but P(y,y)=1/12, not (1/6)^2. The implementation does not multiply forecast
marginals or feed their modes back as observed evidence.

```sh
python -m chainlab filter --input examples/request.json
python -m chainlab forecast --input examples/request.json --horizon 3
python -m chainlab online-demo
```

On the same trained seed23 development fixture, summed prefix predictive log
scores across12 independent test sequences (480 symbols) are -372.302842489947,
versus -372.30284248994707 from full forward likelihood: absolute difference
5.68e-14 on this run. Mean negative log predictive score is0.775630921854.
Every sequence resets to the model's initial distribution. This equality is an
implementation audit, not a new quality improvement or calibration result.
The demo forecasts five steps after only the first10 symbols of one test
sequence; no future symbols enter those distributions.

Filtering costs O(T*(N^2+N*M)) for alphabet size M and stores the prefix outputs.
Forecasts add O(H*(N^2+N*M)); no xi matrices or backward pass are needed. Results
are numerically normalized, with filtering mass-error diagnostics. Existing
model bounds, impossible-prefix rejection and no input mutation still apply.
No stateful streaming API, adaptive model update, calibrated forecast promise,
or proof that a caller's training protocol is leak-free.

## Artifact and cost boundary

Strict chainlab_v1: ordered states/symbols, initial vector, transition matrix,
emission matrix. No serialized code, training data or dynamic factors. Every
operation validates. JSON round trips and label permutations have tests. No
mutation of caller inputs.

N1-8, alphabet1-16, T1-256;1-32 training sequences,total<=2048. Full gamma/xi
inference costs O(T*N^2) time/storage at the xi output scale. Viterbi also
computes inference for its posterior score, so its implementation is not the
minimal-memory path-only variant. Training repeats E-steps and proposal scoring.
Prefix filtering and marginal forecasts are separate methods; no dense
accelerator, neural component, persistent streaming-state or calibrated forecast claim.

## Sources

- https://www.cs.cmu.edu/~cga/behavior/rabiner1.pdf
- https://www.stats.ox.ac.uk/~caron/teaching/sb1b/slideshmm.pdf
- https://sites.stat.washington.edu/mmp/courses/stat534/spring19/Handouts/h4-hmm.pdf

Standard HMM/EM theory. Independent implementation, no new algorithm claim.

## Live prefix-evidence inspector (v0.2)

Live v0.2 [prefix-evidence inspector](https://midya8.github.io/chainlab/) keeps all three original models and both exact counterexamples fixed. Edit a bounded observation window and compare each own-prefix filtered row, full-window smoothed row, supported Viterbi path and prefix-only future marginals. Original 40-symbol reports and scores remain unchanged; the first three displays show only the first 12 symbols. Independent scaled browser versus native log inference checks cover 114 symbol edits and 40 prefix boundaries, plus 62 exhaustive high-precision controls. Underflowed browser mass refuses instead of inventing a posterior. 41 Python tests, four Node/actual-Chrome tests and installed eight-module/nine-command reproduction. No new training, state accuracy, calibration or causal claim. [Conditioning and numerical limits](https://github.com/midya8/chainlab/blob/main/EVIDENCE.md).

The displayed suffix is evidence for smoothing and Viterbi, but not the selected prefix forecast. Horizon h makes h transitions from the last filtered state. Marginals must not be multiplied into an independent joint future path. Native log inference can resolve tiny supported paths that scaled probability arithmetic loses. All 22 retained archive files regenerate with exact structure/nonfloats and 1e-11 absolute / 1e-12 relative float checks, without changing original inference tolerances. Invalid input clears stale rows and exports. Mobile heatmaps become labeled state rows; full predictive score tables scroll locally.


## v0.3: a path is a decision, not the uncertainty

[Open the path workbench](https://midya8.github.io/chainlab/paths.html) · [Derivation, input/report schemas, sources and limits](https://github.com/midya8/chainlab/blob/main/PATHS.md)

The separate rational model exposes MAP, supported maximum expected matches, supported product marginals and unconstrained posterior modes. The default control gives three different supported paths; its unconstrained modes form an impossible string. MAP has posterior about .05823316 and expected Hamming loss 2.880904. The supported expected-matches path has lower posterior .05686832 but lower expected loss 2.531237. The product-marginal path has posterior .03639572 and loss 2.535156. These are model-conditional expectations, not measured true-state accuracy or an algorithm ranking.

Whole-path entropy uses the smoothed posterior chain rule, not a sum of independent state entropies. Locked and independent five-position chains have identical half/half state marginals, but path entropies ln(2) and 5 ln(2). Their dependence gap equals summed adjacent-state mutual information. The UI exposes all state, edge and conditional probabilities, three full decision trellises, complete model/sequence editing and source-bound archive exports.

Thirteen controls include emission support, undefined zero-occupancy conditionals, whole-path lexicographic ties, 4^32 supported paths counted without enumeration and exact evidence 2^-3840 below binary64 range. The standalone verifier imports neither producer nor parser: independent suffix/prefix arithmetic, every Bellman alternative and Decimal80 logarithms check the report. Tiny exhaustive Fraction/Decimal controls add a different oracle.

The full suite passes 58 Python and 10 Node/actual-Chrome tests, preserving the earlier 41/four tests. New checks include 120 random tiny exhaustive models, 150 generated native/BigInt cases and all 438 primitive modifications of the default report. Chrome inspects 296 state cells, 1,532 edge cells, 867 reachable decoding states, 39 layouts, physical JSON edits and two completed downloads verified natively. Installed-wheel replay imports all 10 modules, retains old training/data/prefix reproduction and nine commands, then replays all 13 new controls, both new module commands and 26 malformed-report checks outside checkout.

### Limits of the new work

The rational model accepts 1-4 states, 1-8 symbols and 1-32 observations, with 128-bit input fractions, an 8,192-bit reported-fraction cap, 64 KiB input and 4 MiB verifier reports. Complex otherwise-valid models can refuse rather than round. Probabilities, support, path ties and objectives are exact; entropy and logarithms are approximate binary64 nats, independently checked at absolute 1e-10 tolerance. Low entropy can mean a misspecified model is confidently wrong.

Three original-model examples explicitly round probabilities to millionths then normalize rows exactly. They are different rational models, not unchanged original fits or newly trained arms. All original floating computational files, saved numerical artifacts, data and tests are unchanged. No calibration, true-state recovery, model identification, causal claim, external quality result, production/speed promise or algorithm novelty. Standard methods are attributed in PATHS.md.
