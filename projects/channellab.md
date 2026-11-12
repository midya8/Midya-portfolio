# ChannelLab

ChannelLab compares two supplied binary experiments. It returns a state-independent randomized signal transformation when one channel can simulate the other, or a two-action decision problem with a strict value gap when it cannot. A separate prior atlas compares one fixed task over the whole prior interval.

Python 3.10+, with no runtime dependencies, and a separate BigInt browser inspector. The implementation uses classical Blackwell comparison; it does not learn channels, validate real sensors or introduce a new theorem.

[Live inspector](https://midya8.github.io/channellab/) · [Source](https://github.com/midya8/channellab) · [Reviewed change](https://github.com/midya8/channellab/pull/2)

## Choose a comparison

The information-order inspector asks whether one supplied channel can simulate the other through a state-independent randomized signal transformation. The prior atlas instead holds one payoff table fixed and compares task values at every prior. A task-value tie or crossing does not establish an information order across all decision problems.

## Equal classification value without dominance

At a uniform prior over states 0 and 1, consider:

```text
          signal0 signal1             signal0 signal1
A state0     1       0       B state0    1/2     1/2
A state1    1/2     1/2      B state1     0       1
```

Both experiments achieve exactly 3/4 optimal classification accuracy. Neither can simulate the other using a single state-independent randomized signal transformation.

| Decision task | Optimal value from A | Optimal value from B | Strict advantage |
|---|---:|---:|---:|
| Action 0=(0,0), action 1=(-1/3,2/3) | 1/6 | 1/4 | B by 1/12 |
| Action 0=(0,0), action 1=(-2/3,1/3) | 1/12 | 0 | A by 1/12 |

Payoff pairs list state 0 then state 1. The decision maker chooses after seeing the signal. These are exact supplied teaching problems, not measured sensors, a dataset, an accuracy leaderboard or a real-world recommendation.

## Run and inspect

```sh
python -m channellab demo
python -m channellab run examples/incomparable.json > report.json
python -m channellab verify report.json
python -m channellab atlas examples/incomparable.json > atlas.json
python -m channellab verify-atlas atlas.json
python -m pip install .
channellab demo
python -m unittest discover -s tests -v
node --test --test-concurrency=1 tests/test_engine.cjs tests/test_atlas.cjs tests/test_browser.cjs
python tools/check_installed.py
# Optional external numerical reference:
python tools/check_highs.py
python tools/check_atlas_highs.py
# Serve docs/ using any static server to open the browser inspector.
```

The local browser accepts the complete exact model, switches between both directions, exposes every signal/posterior, every call-function knot, stochastic kernel, reconstructed state law, prior-weighted coupling and every deterministic task policy. A failed direction exposes its own two-action counterexample with all signal action values and ties. Zero-mass signals have null posteriors, not invented beliefs. Downloads contain the full exact report for separate native replay. Editing clears old output and disables download; failed input leaves no stale result. All computation stays local, no backend, network model or paid API.

The default is one of 13 developed controls. Relabelled and split signals can be equivalent even with different output alphabets. A perfect signal can be more informative without helping a task whose best action ignores the state. A tiny full-support prior changes posterior positions and task values, not Blackwell order. A disclosed large-fraction control requires integer outputs beyond JavaScript's safe range.

## Fixed-task values over all priors

Hold the two channels and payoff table fixed, then vary p=P(state 1) over the complete closed interval [0,1]. Every deterministic signal-to-action policy has an exact affine value and a closed optimality range, including singleton endpoints. The atlas retains all tied policies, the no-signal value, each information-value line, and every additional A-B ranking root even when no policy changes. No posterior is invented at a zero-mass endpoint.

For the default classification task, the exact knots are 0, 1/3, 1/2, 2/3 and 1. A wins on (0,1/2), B on (1/2,1), while the supplied uniform prior ties. The 1/3 and 2/3 knots are policy changes, not ranking changes. This is the full prior domain for one fixed task, not a survey of all decision problems or a sequential POMDP solver.

The generator intersects complete-policy half-spaces. A separate checker uses per-signal action crossings, Cartesian products of ties and per-signal inequalities for every policy range. Importing the checker does not load the generator. Python and BigInt agree on complete exact atlas JSON. The browser exposes curve, knot, interval and every-policy tables plus a separate atlas download; the original information-order report stays unchanged. SVG coordinates approximate display only; exact fractions remain in tables and reports.

## The finite proof objects

For two states and any full-support prior, A dominates B exactly when its posterior distribution is larger in convex order. The upper-hinge call value is C(t)=E[max(posterior-t,0)]. ChannelLab checks all supported posterior knots plus 0 and 1. Their difference is affine between knots, so there is no threshold-sampling gap.

- A passing direction constructs K>=0 with each row summing to 1 and A K=B for both states. Exact bounded-polytope basis enumeration returns one feasible vertex, not every kernel.
- A failed direction supplies a knot t with C_B(t)>C_A(t), and payoffs (0,0) versus (-t,1-t). The returned strict value gap is a separating decision problem, not a failed numerical search.
- A separate verifier imports validation only, not the generator or its elimination/basis solver. It replays every field and checks feasible kernel equations or the strict witness. Valid alternative feasible kernels are accepted if their derived fields match. This is computational evidence, not a proof-assistant certificate.

The chart connects exact knots using floating-point pixel coordinates only. Inference, tables and report serialization use exact fractions. [METHOD.md](https://github.com/midya8/channellab/blob/main/METHOD.md) gives the derivation, complete schema, independent-check contract, development-search provenance and attributed primary notes and supporting sources for both report formats.

## Verification

- 30 Python tests, including 297 separately altered non-input atlas leaves rejected, all ties, endpoint-only policy ranges, a 1/1,000,001 policy boundary, ranking roots without policy changes, checker import independence, and 372 separately altered non-input primitive leaves rejected in the default report, unknown fields/type confusion, signal/state relabelling, full-support prior changes, null signals, strict CLI errors and a valid alternative feasible kernel.
- 710 complete Python/checker/BigInt report comparisons: 13 controls, all 625 ordered pairs of denominator-four binary-output channels, and 72 seeded rectangular pairs over all nine 1..3 by 1..3 signal-count combinations. Reports include 6,994 task policies, 627 feasible directional kernels and 793 strict directional counterexamples. This is a declared small finite grid, not a universal empirical benchmark.
- The optional SciPy 1.15.3 HiGHS reference executes 1,420 directional feasibility solves. Its 627 feasible cases match the exact relation. Worst equality residual below 2.8e-16, against a 1e-8 tolerance. SciPy is optional reference evidence, never a production dependency.
- The installed-wheel check builds a 0.2.0 wheel and runs outside the checkout. It checks eight module origins in site-packages, all 13 reports and 13 atlases through console/module entrypoints. Each report type rejects 26 direct and 52 CLI forgeries.
- Atlas parity covers 710 complete cases: 8,486 policies, 3,401 knots and 2,691 open intervals. Independent SciPy 1.15.3 HiGHS diagnostics rebuild policy values from input and execute 16,972 LPs to minimize/maximize policy-optimal prior ranges. All 6,251 nonempty ranges agree, worst tested endpoint difference 0 against 1e-8 tolerance. Floating diagnostics are corroboration, not the production checker or a universal proof.
- Actual Chrome checks 39 control/width reports at 1280, 390 and 320 pixels, 78 directions, 165 posterior rows, 162 hinge rows, 366 task-policy rows, 99 kernel rows and 147 witness-signal rows. Six Node/actual-Chrome tests pass. Atlas tables add 444 policy rows, 180 knot rows and 141 interval rows. Thirteen original-report and thirteen atlas trusted completed downloads are byte-exact and accepted by their native verifiers. All visible signal, task, kernel/coupling/moment and separating-witness tables are checked. Stale/invalid clearing, touch-target heights, horizontal table scroll and viewport containment are tested. These checks cover the declared controls and widths, not every possible input or device.

## Scope and limits

Exactly two states. One to three signals per channel, one to three actions. The supplied comparison uses a full-support prior; the atlas includes both certain-state endpoints. Exact non-boolean integer/pair input, raw components<=1,000,000; normalized denominator LCM<=1,000,000; payoff magnitude<=100. Strict JSON input 64 KiB, report verification 8 MiB. Enumeration bounds do not bound all arithmetic bit complexity, output size, wall time or memory. Full details in METHOD.

No channel learning, sequential design, real sensor validation, privacy guarantee, finance, safety promise, multi-state scalar-order shortcut, scalability claim or new Blackwell algorithm. Shared mathematical assumptions remain shared failure modes in cross-language/reference agreement. Exact arithmetic does not make the supplied model true. MIT.
