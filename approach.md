# How I build

The approach behind the projects in this portfolio, stated once so the
pattern is visible across them. Each principle below is demonstrated by a
project linked from it — not asserted in the abstract.

## Contents

- [Choose the simplest architecture that meets the requirement](#choose-the-simplest-architecture-that-meets-the-requirement)
- [One tool, one job](#one-tool-one-job)
- [Make tools that fit scripts as well as terminals](#make-tools-that-fit-scripts-as-well-as-terminals)
- [Prefer a scheduled check over a service to keep alive](#prefer-a-scheduled-check-over-a-service-to-keep-alive)
- [Make automation runnable by hand](#make-automation-runnable-by-hand)
- [Validate before executing](#validate-before-executing)
- [Show the plan before you run it](#show-the-plan-before-you-run-it)
- [Fail closed, not open](#fail-closed-not-open)
- [Prefer explicit over implicit](#prefer-explicit-over-implicit)
- [Name the numerical assumptions](#name-the-numerical-assumptions)
- [Make the default the safe choice](#make-the-default-the-safe-choice)
- [Put the policy in a file](#put-the-policy-in-a-file)
- [Describe the work in data, not in code](#describe-the-work-in-data-not-in-code)
- [Prefer a file to a form](#prefer-a-file-to-a-form)
- [Test the behaviour you depend on](#test-the-behaviour-you-depend-on)
- [Test the bad input, not just the good path](#test-the-bad-input-not-just-the-good-path)
- [Let reports and documents be outputs, not afterthoughts](#let-reports-and-documents-be-outputs-not-afterthoughts)
- [Make the same answer readable by people and by machines](#make-the-same-answer-readable-by-people-and-by-machines)
- [One record, many views](#one-record-many-views)
- [Prefer plain text for the record](#prefer-plain-text-for-the-record)
- [Make the same input give the same answer](#make-the-same-input-give-the-same-answer)
- [Make work resumable](#make-work-resumable)
- [Record the when, not just the what](#record-the-when-not-just-the-what)
- [Reduce noise; answer the question first](#reduce-noise-answer-the-question-first)
- [Put the worst thing at the top](#put-the-worst-thing-at-the-top)
- [Make different failures look different](#make-different-failures-look-different)
- [Prefer a number to an adjective](#prefer-a-number-to-an-adjective)
- [Don't claim what you didn't observe](#dont-claim-what-you-didnt-observe)
- [One observation is not a signal](#one-observation-is-not-a-signal)
- [Compare against a baseline, not against nothing](#compare-against-a-baseline-not-against-nothing)
- [Automate the check, not the judgement](#automate-the-check-not-the-judgement)
- [Put an expiry on every exception](#put-an-expiry-on-every-exception)
- [Bound the history you keep](#bound-the-history-you-keep)
- [Keep a failure contained](#keep-a-failure-contained)
- [Design for the failure mode](#design-for-the-failure-mode)
- [Keep the check cheap enough to run often](#keep-the-check-cheap-enough-to-run-often)
- [Write down why, not just what](#write-down-why-not-just-what)
- [Make the first run useful](#make-the-first-run-useful)
- [Detect, don't configure](#detect-dont-configure)
- [Work without the network](#work-without-the-network)
- [Put the check in the pipeline](#put-the-check-in-the-pipeline)
- [Make a failure explain itself](#make-a-failure-explain-itself)
- [Answer the question, don't just raise the alarm](#answer-the-question-dont-just-raise-the-alarm)
- [Measure the response, not just the outage](#measure-the-response-not-just-the-outage)
- [Don't act on a single failure](#dont-act-on-a-single-failure)
- [Name the command for the job, not the mechanism](#name-the-command-for-the-job-not-the-mechanism)
- [Degrade in stages, not all at once](#degrade-in-stages-not-all-at-once)
- [Prefer boring technology](#prefer-boring-technology)
- [Small enough to read end to end](#small-enough-to-read-end-to-end)
- [Measure from the outside, like a user would](#measure-from-the-outside-like-a-user-would)
- [Don't let the monitor share the fate of what it monitors](#dont-let-the-monitor-share-the-fate-of-what-it-monitors)
- [Design around the constraint, not against it](#design-around-the-constraint-not-against-it)
- [Pin the ending to the outcome, not the step list](#pin-the-ending-to-the-outcome-not-the-step-list)
- [Treat what you observe as data, never as instructions](#treat-what-you-observe-as-data-never-as-instructions)
- [Keep the words and the code on different schedules](#keep-the-words-and-the-code-on-different-schedules)
- [A marginal is not a path](#a-marginal-is-not-a-path)
- [A zero gradient is not a zero effect](#a-zero-gradient-is-not-a-zero-effect)
- [Choose the metric the failure cannot pass](#choose-the-metric-the-failure-cannot-pass)
- [Audit each term of a sum, not just the total](#audit-each-term-of-a-sum-not-just-the-total)
- [Make the fast path prove it equals the slow path](#make-the-fast-path-prove-it-equals-the-slow-path)
- [Agreement between two approximations is not evidence](#agreement-between-two-approximations-is-not-evidence)
- [A guarantee is a contract with its assumption](#a-guarantee-is-a-contract-with-its-assumption)
- [A mean is not the distribution](#a-mean-is-not-the-distribution)
- [A repaired number needs its own audit](#a-repaired-number-needs-its-own-audit)
- [A narrower window is a new distribution](#a-narrower-window-is-a-new-distribution)
- [Acceptance is not exploration](#acceptance-is-not-exploration)
- [A proposal that returns home is not a move](#a-proposal-that-returns-home-is-not-a-move)
- [A repair that cannot change the decision](#a-repair-that-cannot-change-the-decision)
- [A cancelled mean is not exploration](#a-cancelled-mean-is-not-exploration)
- [Zero correlation is not independence](#zero-correlation-is-not-independence)
- [The reference is part of the question](#the-reference-is-part-of-the-question)
- [A figure is a claim about its data](#a-figure-is-a-claim-about-its-data)
- [A conditioned prior must be renormalized](#a-conditioned-prior-must-be-renormalized)
- [Marginal peaks are not a joint partition](#marginal-peaks-are-not-a-joint-partition)
- [A held-out label is not a held-out node](#a-held-out-label-is-not-a-held-out-node)
- [Differentiate the computation you ran, not the optimum you wish you had](#differentiate-the-computation-you-ran-not-the-optimum-you-wish-you-had)
- [Zero visits is not zero mass](#zero-visits-is-not-zero-mass)
- [Two possible cuts can be jointly impossible](#two-possible-cuts-can-be-jointly-impossible)
- [A sum of marginal entropies is not the joint entropy](#a-sum-of-marginal-entropies-is-not-the-joint-entropy)
- [The most probable partition is not the cheapest decision](#the-most-probable-partition-is-not-the-cheapest-decision)
- [One scale for a whole matrix is a claim about every row](#one-scale-for-a-whole-matrix-is-a-claim-about-every-row)
- [Two metrics can disagree, and the choice is the claim](#two-metrics-can-disagree-and-the-choice-is-the-claim)
- [A p-value cannot be smaller than its own resolution](#a-p-value-cannot-be-smaller-than-its-own-resolution)
- [A gain needs a control that could have produced it](#a-gain-needs-a-control-that-could-have-produced-it)
- [A safeguard that never fires is not evidence it works](#a-safeguard-that-never-fires-is-not-evidence-it-works)
- [Show the bill with the gain](#show-the-bill-with-the-gain)
- [Measure the side you did not optimize](#measure-the-side-you-did-not-optimize)
- [Label what the data cannot identify](#label-what-the-data-cannot-identify)
- [Pin the baseline, not just the result](#pin-the-baseline-not-just-the-result)
- [A weight is a measurement on a task, not an explanation](#a-weight-is-a-measurement-on-a-task-not-an-explanation)
- [Effective sample size measures weights, not support](#effective-sample-size-measures-weights-not-support)
- [Grounding is a check you run, not a property you claim](#grounding-is-a-check-you-run-not-a-property-you-claim)
- [Determinism is what makes a quality number testable](#determinism-is-what-makes-a-quality-number-testable)
- [A plan has a cost before it has a result](#a-plan-has-a-cost-before-it-has-a-result)
- [Hold the distribution fixed and vary only the strategy](#hold-the-distribution-fixed-and-vary-only-the-strategy)
- [A wider beam is not guaranteed to be a better beam](#a-wider-beam-is-not-guaranteed-to-be-a-better-beam)
- [Keep the exact answer next to the approximation](#keep-the-exact-answer-next-to-the-approximation)
- [A clipped attack cannot prove robustness](#a-clipped-attack-cannot-prove-robustness)
- [Keep the recipe with the artifact](#keep-the-recipe-with-the-artifact)
- [A lexical check can catch a fabrication, not certify a truth](#a-lexical-check-can-catch-a-fabrication-not-certify-a-truth)
- [A strong association does not say what an intervention would do](#a-strong-association-does-not-say-what-an-intervention-would-do)
- [Measure the retrieval before you blame the answer](#measure-the-retrieval-before-you-blame-the-answer)
- [Check a hand-derived gradient against finite differences](#check-a-hand-derived-gradient-against-finite-differences)
- [Lint the prompt like code](#lint-the-prompt-like-code)
- [Optimizing the bound is not recovering the marginals](#optimizing-the-bound-is-not-recovering-the-marginals)
- [A green suite is a regression gate, not a certificate](#a-green-suite-is-a-regression-gate-not-a-certificate)
- [Validate the record before you trust the numbers](#validate-the-record-before-you-trust-the-numbers)
- [A small residual is not a small error](#a-small-residual-is-not-a-small-error)
- [Direction is layout, not translation](#direction-is-layout-not-translation)
- [A pooled diagnostic cannot see inside one chain](#a-pooled-diagnostic-cannot-see-inside-one-chain)
- [Let the baseline learn too](#let-the-baseline-learn-too)
- [Optimal at one belief is not optimal at every belief](#optimal-at-one-belief-is-not-optimal-at-every-belief)
- [The natural baseline is not the best baseline](#the-natural-baseline-is-not-the-best-baseline)
- [A one-step quantity is not a long-run quantity](#a-one-step-quantity-is-not-a-long-run-quantity)
- [A filtered row is not a smoothed row](#a-filtered-row-is-not-a-smoothed-row)
- [An unbiased estimate need not be a possible value](#an-unbiased-estimate-need-not-be-a-possible-value)
- [A conditioned proposal is not a better filter](#a-conditioned-proposal-is-not-a-better-filter)
- [A maximum effective sample size can still miss the mass](#a-maximum-effective-sample-size-can-still-miss-the-mass)
- [A gate with nothing to measure must fail, not pass](#a-gate-with-nothing-to-measure-must-fail-not-pass)
- [The best first move can be the one that looks worse now](#the-best-first-move-can-be-the-one-that-looks-worse-now)
- [A local metric does not certify a finite step](#a-local-metric-does-not-certify-a-finite-step)
- [A group deletion is not the sum of its single deletions](#a-group-deletion-is-not-the-sum-of-its-single-deletions)
- [The value of feedback is the gap to the best open-loop plan](#the-value-of-feedback-is-the-gap-to-the-best-open-loop-plan)
- [A unique prediction does not identify a coefficient](#a-unique-prediction-does-not-identify-a-coefficient)
- [An aggregate improvement can hide a per-context regression](#an-aggregate-improvement-can-hide-a-per-context-regression)
- [Reconstruction is not generation](#reconstruction-is-not-generation)
- [Marginals do not compose when randomness is shared](#marginals-do-not-compose-when-randomness-is-shared)
- [Locally best choices need not fit together](#locally-best-choices-need-not-fit-together)
- [A float pass at the boundary is not an exact pass](#a-float-pass-at-the-boundary-is-not-an-exact-pass)
- [Rectangular uncertainty is a different problem, not a different solver](#rectangular-uncertainty-is-a-different-problem-not-a-different-solver)
- [Separate worst cases are not a joint worst case](#separate-worst-cases-are-not-a-joint-worst-case)
- [A free restart is not optional stopping](#a-free-restart-is-not-optional-stopping)
- [A recommendation changes the deviation](#a-recommendation-changes-the-deviation)
- [A stable value does not mean a stable strategy](#a-stable-value-does-not-mean-a-stable-strategy)
- [The price decides the policy](#the-price-decides-the-policy)
- [A test that cannot see the mistake is not a test of it](#a-test-that-cannot-see-the-mistake-is-not-a-test-of-it)
- [At the boundary, the rule decides](#at-the-boundary-the-rule-decides)
- [A zero error bar is not a zero error](#a-zero-error-bar-is-not-a-zero-error)
- [Gate the claim, report the diagnosis](#gate-the-claim-report-the-diagnosis)
- [Fit the repair where the failure is visible](#fit-the-repair-where-the-failure-is-visible)
- [A search that runs out of budget owes you the gap](#a-search-that-runs-out-of-budget-owes-you-the-gap)
- [A control that cannot win is not a control](#a-control-that-cannot-win-is-not-a-control)
- [One residual is not a value certificate](#one-residual-is-not-a-value-certificate)
- [An optimum is not a uniqueness proof](#an-optimum-is-not-a-uniqueness-proof)
- [A sum that closes is not a correct split](#a-sum-that-closes-is-not-a-correct-split)
- [A sufficient certificate is not a complete detector](#a-sufficient-certificate-is-not-a-complete-detector)
- [An exact audit needs an exact anchor](#an-exact-audit-needs-an-exact-anchor)
- [An input-dependent recurrence is not a fixed convolution](#an-input-dependent-recurrence-is-not-a-fixed-convolution)
- [The objective you minimize is not the score you report](#the-objective-you-minimize-is-not-the-score-you-report)
- [A row left out is not a row held out](#a-row-left-out-is-not-a-row-held-out)
- [Decreasing loss is not convergence](#decreasing-loss-is-not-convergence)
- [Score only what was missing](#score-only-what-was-missing)
- [A reconstruction does not identify the parts](#a-reconstruction-does-not-identify-the-parts)
- [A cheaper sampler is not the same sampler](#a-cheaper-sampler-is-not-the-same-sampler)
- [A running interval must remember what it excluded](#a-running-interval-must-remember-what-it-excluded)
- [A deletion is defined by what you hold fixed](#a-deletion-is-defined-by-what-you-hold-fixed)
- [A set is a coverage claim, not a probability claim](#a-set-is-a-coverage-claim-not-a-probability-claim)
- [A reveal on an impossible history costs nothing](#a-reveal-on-an-impossible-history-costs-nothing)
- [Likelihood is not identity](#likelihood-is-not-identity)
- [A stopping rule is not a mode certificate](#a-stopping-rule-is-not-a-mode-certificate)
- [Coarsening a signal costs exactly its slacks](#coarsening-a-signal-costs-exactly-its-slacks)
- [A suggestion is not an evaluation](#a-suggestion-is-not-an-evaluation)
- [A valid proof does not authenticate its source](#a-valid-proof-does-not-authenticate-its-source)
- [More controls do not always make a valid adjustment](#more-controls-do-not-always-make-a-valid-adjustment)
- [A cap is a choice, not a guarantee](#a-cap-is-a-choice-not-a-guarantee)
- [A missing rating is not a zero](#a-missing-rating-is-not-a-zero)
- [A saving is a curve, not a number](#a-saving-is-a-curve-not-a-number)
- [Out-of-bag is still in-sample](#out-of-bag-is-still-in-sample)
- [A perfect training score is not a finished optimization](#a-perfect-training-score-is-not-a-finished-optimization)
- [The base vocabulary decides what can ever be encoded](#the-base-vocabulary-decides-what-can-ever-be-encoded)
- [The graph decides the answer before the eigensolver runs](#the-graph-decides-the-answer-before-the-eigensolver-runs)
- [A permutation that refits is a different question](#a-permutation-that-refits-is-a-different-question)
- [The normalizer is part of the model](#the-normalizer-is-part-of-the-model)
- [A count is not an expectation](#a-count-is-not-an-expectation)
- [Point the optimizer at noise and see what it buys](#point-the-optimizer-at-noise-and-see-what-it-buys)
- [A tangent is not a map](#a-tangent-is-not-a-map)
- [An exact interval is not a path](#an-exact-interval-is-not-a-path)
- [Edits add; deletions couple](#edits-add-deletions-couple)
- [Proximity is a leaf-collision average, not a similarity score](#proximity-is-a-leaf-collision-average-not-a-similarity-score)
- [A sample is not the range](#a-sample-is-not-the-range)
- [A slice is not a projection](#a-slice-is-not-a-projection)
- [A deletion report is not a deletion experiment](#a-deletion-report-is-not-a-deletion-experiment)
- [A gate that cannot fail is not a gate](#a-gate-that-cannot-fail-is-not-a-gate)
- [Valid syntax is not a valid record](#valid-syntax-is-not-a-valid-record)
- [A null threshold is not a missing threshold](#a-null-threshold-is-not-a-missing-threshold)
- [A chunk hit is not a document hit](#a-chunk-hit-is-not-a-document-hit)
- [A negative derivative is not a downhill step](#a-negative-derivative-is-not-a-downhill-step)
- [A zero gap certifies the optimizer, not the reward](#a-zero-gap-certifies-the-optimizer-not-the-reward)
- [Equivalent factors are not equivalent steps](#equivalent-factors-are-not-equivalent-steps)
- [Three statistics that agree on ties are not the same statistic](#three-statistics-that-agree-on-ties-are-not-the-same-statistic)
- [A byte count is not a file](#a-byte-count-is-not-a-file)
- [An exact margin is not a runtime prediction](#an-exact-margin-is-not-a-runtime-prediction)
- [A sum of gradients is not the sequence that produced it](#a-sum-of-gradients-is-not-the-sequence-that-produced-it)
- [A time limit is not a terminal state](#a-time-limit-is-not-a-terminal-state)
- [A mask is not a condition](#a-mask-is-not-a-condition)
- [A kink is not a failed finite difference](#a-kink-is-not-a-failed-finite-difference)
- [A saving measured against busywork is not a saving](#a-saving-measured-against-busywork-is-not-a-saving)
- [A visible attention pattern is not a contribution](#a-visible-attention-pattern-is-not-a-contribution)
- [A checkpoint is not the weights](#a-checkpoint-is-not-the-weights)
- [The loss you report and the gradient you step must be the same function](#the-loss-you-report-and-the-gradient-you-step-must-be-the-same-function)
- [A self-query is not a held-out query](#a-self-query-is-not-a-held-out-query)
- [A lower threshold is not a lower recall](#a-lower-threshold-is-not-a-lower-recall)
- [A lossy view of a number is not the number](#a-lossy-view-of-a-number-is-not-the-number)
- [A falling mean is not a falling task](#a-falling-mean-is-not-a-falling-task)
- [A complete record is not a complete explanation](#a-complete-record-is-not-a-complete-explanation)
- [A passing gate is not a clean scan](#a-passing-gate-is-not-a-clean-scan)
- [The best path is not the likeliest transcript](#the-best-path-is-not-the-likeliest-transcript)
- [Equal marginals are not independence](#equal-marginals-are-not-independence)
- [A guarantee is not an optimum](#a-guarantee-is-not-an-optimum)
- [A sum is not a max](#a-sum-is-not-a-max)
- [A local minimum is not a global optimum](#a-local-minimum-is-not-a-global-optimum)
- [A label that leaves can come back](#a-label-that-leaves-can-come-back)
- [A minimal repair is not a cheapest repair](#a-minimal-repair-is-not-a-cheapest-repair)
- [Removing an attack can remove an acceptance](#removing-an-attack-can-remove-an-acceptance)
- [A circle is not a proof](#a-circle-is-not-a-proof)
- [The same traces are not the same choices](#the-same-traces-are-not-the-same-choices)
- [A safe next step can still lose](#a-safe-next-step-can-still-lose)
- [A winning state is not a winning policy](#a-winning-state-is-not-a-winning-policy)
- [Local support is not a shared solution](#local-support-is-not-a-shared-solution)
- [Unknown is not false](#unknown-is-not-false)
- [Used does not mean necessary](#used-does-not-mean-necessary)
- [A binding is not a solution](#a-binding-is-not-a-solution)
- [A tight bound is not an attained bound](#a-tight-bound-is-not-an-attained-bound)
- [Deleting is not negating](#deleting-is-not-negating)
- [A closed table is not a correct language](#a-closed-table-is-not-a-correct-language)
- [A resolved citation is not a correct citation](#a-resolved-citation-is-not-a-correct-citation)
- [Fitting the examples is not identifying the function](#fitting-the-examples-is-not-identifying-the-function)
- [Zero length is not absence](#zero-length-is-not-absence)
- [Occupancy is not a coupling](#occupancy-is-not-a-coupling)
- [Fitting is not reaching](#fitting-is-not-reaching)
- [A ranking is not an entailed preference](#a-ranking-is-not-an-entailed-preference)
- [A restriction is not an announcement](#a-restriction-is-not-an-announcement)

## Choose the simplest architecture that meets the requirement

The Kurdistan International Sociological Association site is editorial
content, not a transaction system, so it is exported to static HTML and
served from Cloudflare: no server to keep up, scale, or patch. The Python
utilities are standard-library only for the same reason — if Python is
installed, they run, with no dependency tree to maintain. The personal site
uses React and Vite for the same end: a static build with nothing to keep
running behind it.

- [Kurdistan International Sociological Association website](projects/kurdistansociology-website.md)
- [sre-toolkit](projects/sre-toolkit.md), [loglens](projects/loglens.md), [flowkit](projects/flowkit.md), [uptimekit](projects/uptimekit.md)
- [Personal site — midya.ca](projects/midya-ca.md)

## One tool, one job

There are four Python utilities here, not one, because each one does a
different job: sre-toolkit does the SRE math and the documents around an
incident, loglens reads access logs, flowkit runs a DAG of shell commands,
and uptimekit probes endpoints and keeps the history. None of them imports
another, and none of them grows a second job — a new need becomes a new
small tool rather than a new mode on an old one. They still work together,
because they share conventions rather than code: every one is
standard-library only, every one is both a command and an importable
library, every one reports through exit codes and text or JSON reports,
and every one writes its documents as Markdown. A shell script — or a
flowkit flow — can chain them without any of them knowing about the
others. The web side follows the same split: the association site and the
personal site are separate repositories, separate builds, and separate
hosts, each doing exactly its own job. The AI systems follow the same
split: eighty-eight small tools — evaluation, tracing, linting, attribution,
calibration, decoding, retrieval, planning, exploration, policy-gradient estimation, stationary sensitivity, latent-variable modelling, natural-gradient geometry and the rest — each a separate repository
doing exactly one job, each built from scratch and standing alone, so a new
need becomes a new small tool rather than a new mode on an old one.

- [sre-toolkit](projects/sre-toolkit.md), [loglens](projects/loglens.md), [flowkit](projects/flowkit.md), [uptimekit](projects/uptimekit.md)
- [Kurdistan International Sociological Association website](projects/kurdistansociology-website.md)
- [Personal site — midya.ca](projects/midya-ca.md)
- [AI systems](projects/README.md#ai-systems)

## Make tools that fit scripts as well as terminals

A tool that only works interactively is half a tool. Every Python utility
here is both a command you run by hand and a library you import into
automation, and every command communicates its result through its exit
code: sre-toolkit exits 1 when an error budget is exhausted, loglens exits
1 when a 5xx rate breaches a threshold, and flowkit uses 0 for success, 1
for a failed step, and 2 for an invalid flow file. uptimekit's `check`
exits 1 on any failure, so a cron line doubles as alerting,
`report --fail-open` gates CI on open incidents, and
`report --fail-slo` exits 1 on an SLO breach, so a breached error
budget gates a pipeline the same way an open incident does. A pipeline or scheduled
check can act on the result without parsing human-readable output.

## Prefer a scheduled check over a service to keep alive

Nothing here runs as a daemon, because a daemon is a second system to
keep alive, watch, and restart — and its own failures are the ones nobody
notices. Every Python utility is a one-shot command: uptimekit's `check`
exits 1 on any failure, so a cron line doubles as alerting, and
`report --fail-open` and `report --fail-slo` gate a pipeline the same way;
flowkit flows, loglens analyses, and sre-toolkit reports all run the same
way, on demand or on a schedule, and then exit. There is no process to
babysit, no port to watch, and no state held in memory that can go stale —
the record on disk is the state. The one exception proves the rule:
uptimekit ships a watch mode for hosts without cron, but it is the
fallback, not the default.

- [uptimekit](projects/uptimekit.md), [flowkit](projects/flowkit.md), [sre-toolkit](projects/sre-toolkit.md), [loglens](projects/loglens.md)

## Make automation runnable by hand

There is no automation-only mode here, and no hidden path the schedule
takes that a person cannot. Every scheduled check is an ordinary command:
uptimekit's `check` is the same invocation whether cron runs it or a
person types it at 3 a.m., and it answers the same way either time — exit
1 on any failure. When the schedule misbehaves, debugging it is running
the command yourself and reading the same output the schedule saw, not
reconstructing what some service did behind a dashboard. And where the
action would have consequences, the command can be previewed first:
flowkit's `--dry-run` validates the flow and prints the plan without
executing anything, so what the nightly run would do is visible before it
does it. Nothing about the automation is special except that something
else typed the command — and that is the point: a check a person cannot
run by hand is a check nobody can fix when it breaks.

- [uptimekit](projects/uptimekit.md), [flowkit](projects/flowkit.md), [sre-toolkit](projects/sre-toolkit.md), [loglens](projects/loglens.md)

## Validate before executing

A bad input should fail loudly before anything happens, not halfway
through. flowkit rejects duplicate step names, dangling dependencies,
cycles, unknown keys, and malformed interpolation before running a single
step, and its `--strict-env` check fails up front on any unset variable
reference instead of letting a blank value silently change a command. The
same instinct shows up in loglens, where filters scope every statistic, so
narrowing to a failing slice never leaves stray numbers computed over the
full log. uptimekit applies the same instinct to monitoring: a latency
assertion turns a slow endpoint into a failure, and a TLS expiry threshold
turns a certificate quietly approaching expiry into one, instead of leaving
both as warnings nobody acts on.

## Show the plan before you run it

Validation says the input is well-formed; a dry run says what would actually
happen. flowkit's `--dry-run` validates the flow and prints the plan — the
steps in order, the `--only` / `--skip` selection, the `when` conditions
annotated, the hooks listed under their own end-of-run heading — without
executing anything, and it exits 0 when the plan validates, so a pipeline
can gate on the review itself. The point is that the run that changes state
is reviewable before it is real: a step that should have been skipped, a
condition evaluating the wrong way, a dependency pointing where it
shouldn't — all of it is visible in the plan, where it costs nothing,
instead of in the run, where it costs the thing the run was supposed to do.
A tool that only offers run-or-nothing forces its operator to trust the
input sight unseen; a tool that can show its plan lets the operator check
the work before the work happens.

- [flowkit](projects/flowkit.md)

## Fail closed, not open

When a tool cannot answer the question it was asked, the safe default is
to fail — not to pass quietly and let the pipeline carry on. flowkit
refuses to run a flow it cannot validate: an invalid flow file exits 2,
before a single step executes, rather than running a broken definition
and hoping for the best. loglens's `--min-apdex` gate fails a log with no
durations instead of passing it unmeasured, because a gate that passes
what it cannot measure is not a gate. uptimekit's `report --fail-open`
gates CI on any open incident and `--fail-slo` exits 1 on a breached SLO,
so an outage nobody has closed keeps failing the pipeline until a success
closes it. sre-toolkit's budget command exits 1 when the error budget is
exhausted, and `metrics --action-items` exits 1 when postmortem items go
stale — unfinished work cannot quietly age out of sight. In each case the
tool would rather stop the pipeline, or refuse to run, than report "fine"
about something it has not actually checked. A false alarm costs a look;
a false all-clear costs the incident nobody saw coming.

- [flowkit](projects/flowkit.md), [loglens](projects/loglens.md), [uptimekit](projects/uptimekit.md), [sre-toolkit](projects/sre-toolkit.md)

## Prefer explicit over implicit

A default nobody chose is a decision nobody made. flowkit interpolates
environment variables into commands only from declared, layered values,
and its `--strict-env` check fails up front on any unset reference instead
of letting a blank value silently rewrite a command. sre-toolkit's triage
maps services to owning teams with an explicit default owner, so every
alert has a named owner and none falls through to nobody. uptimekit
measures SLOs against a target declared in the config (`"slo": 99.9`), so
met-or-breached is a measurement against a stated number, not a feeling.
Where a value matters — who owns it, what the target is, what the
environment holds — it is written down where the tool can see it, not left
to whatever happens to be in scope.

- [flowkit](projects/flowkit.md), [sre-toolkit](projects/sre-toolkit.md), [uptimekit](projects/uptimekit.md)

## Name the numerical assumptions

A number that stabilises a computation is still a decision about the question being answered. KernelLab's Gaussian-process conditioning takes its jitter as an explicit parameter: it enters the training covariance and the leave-one-out variance, and it is never silently added to future observation noise — no adaptive jitter, no PSD projection, no silent retry when a matrix will not factor. A singular model is rejected and the caller supplies the jitter, because a stabiliser that quietly changes the model is a bug wearing a fix's clothes. The same rule holds for the priors and length scales: they are declared up front, fixed, and reported alongside the result, not tuned until the output looks right.

The test is whether the uncomfortable result survives. KernelLab keeps its wide-kernel arm in the report — a visibly bad fit on the same fixture — instead of tuning it away, because that arm is evidence about what the method does when its assumptions are wrong, and hiding it would make the good arm look inevitable rather than chosen. A tool that reports only the settings that worked is advertising, not engineering. State the conditioning, the stabiliser and the prior where the user can see them, and let the bad arm stay in the room.

- [KernelLab](projects/kernellab.md)

## Make the default the safe choice

A tool is mostly used the way it ships — with its defaults, in a hurry,
by someone who has not read the manual. So the defaults here are chosen
to be the safe ones, not the convenient ones. loglens detects the log
format per line, with `--format auto` the default, so the tool adapts to
the log instead of assuming a format and silently misreading the lines
that do not match. uptimekit's default deployment is a cron line, not a
daemon — nothing to keep alive, restart, or patch — and watch mode
exists only for hosts without a scheduler, so the fallback is the
exception, not the shape of the tool. sre-toolkit's triage routes every
alert to a named owner with an explicit default owner, so the alert that
matches no rule still lands with someone instead of falling through to
nobody. The personal site applies the same instinct to its visitors: a
visitor who prefers reduced motion gets a single static frame of the
galaxy without asking, because the respectful rendering is the default
one, not a setting to discover.

The point is that a default is a decision made on the user's behalf, and
the user never gets to review it. A default that assumes, that keeps
something running, or that drops the awkward case is a decision the tool
made quietly and the user inherits loudly, usually at 3 a.m. Make the
default the thing you would choose if you were standing next to the
person using it — detect instead of assume, schedule instead of serve,
route instead of drop, respect instead of animate — and leave the
riskier choices as flags the user has to reach for on purpose, knowing
what they are reaching for.

- [loglens](projects/loglens.md), [uptimekit](projects/uptimekit.md), [sre-toolkit](projects/sre-toolkit.md), [Personal site — midya.ca](projects/midya-ca.md)

## Put the policy in a file

The decisions these tools enforce — what counts as a breach, who owns an
alert, what a flow does — live in files, not in settings somebody clicked
once and nobody can review. sre-toolkit's SLO definitions are Markdown or
JSON files, so the target and the window are written down where a pull
request can see them, and its triage rules come from custom rule files, so
the policy that shapes the board is versioned with the code that enforces
it instead of re-typed as flags each run. flowkit's flows are JSON files:
steps, dependencies, retries, and environment in one definition that can
be diffed, so a change to the nightly ETL is a change to a file, reviewed
like any other. uptimekit's targets and SLO target (`"slo": 99.9`) live in
config, and the history the reports derive from is a file on disk. Even
the policy a tool suggests arrives as a file to adopt: sre-toolkit's
`burn --suggest` emits the standard three-tier multi-window policy for a
human to take, it does not install one. The web side follows the same
instinct: the association site's news posts are Markdown files, so
publishing is editing a file — versioned with the site, reviewable in a
pull request, rendered by the same build as everything else. A decision
that lives in a file can be reviewed, reverted, and carried to the next
machine; a decision that lives in a setting can only be remembered — and
remembered settings are how a working setup quietly becomes an
undocumented one.

- [sre-toolkit](projects/sre-toolkit.md), [flowkit](projects/flowkit.md), [uptimekit](projects/uptimekit.md)
- [Kurdistan International Sociological Association website](projects/kurdistansociology-website.md)

## Describe the work in data, not in code

A tool should not make you learn its language before it will do its job.
flowkit's flows are JSON files: steps, dependencies, retries, and
environment in one definition you can read in a single file — the shell
commands inside are the work, the JSON is only the shape around them, and
there is no scripting language to learn or debug. loglens needs no query
language: nobody should have to remember `awk` incantations during an
incident, so a log file you already have becomes a one-screen summary in
a single command. uptimekit's endpoints are configuration, not code — what
to probe, and with which thresholds, lives in a file, so adding an
endpoint means editing a file, not changing the checker, and the same tool
monitors one site or twenty without a code change. sre-toolkit's triage
rules come from rule files and its SLO definitions are Markdown or JSON,
so the policy is data the tool reads, not code it runs. Data can be read,
diffed, and handed to someone who has never used the tool; a language has
to be learned first, and during an incident that learning is the work that
stands between you and the answer.

- [flowkit](projects/flowkit.md), [loglens](projects/loglens.md), [uptimekit](projects/uptimekit.md), [sre-toolkit](projects/sre-toolkit.md)

## Prefer a file to a form

Wherever something needs to be created, configured, or changed, it lives
in a file you can read — not behind a form that hides the change. The
association site publishes news by adding a Markdown file with
frontmatter, one per locale, so a post is versioned with the site,
reviewable in a pull request, and rendered by the same build as
everything else; there is no admin panel to log into and no database row
to write, and the UI text lives in per-locale JSON dictionaries for the
same reason. flowkit's flows are JSON files, uptimekit's endpoints and
SLO targets live in one config file, and sre-toolkit's triage rules and
SLO definitions are files the tools read rather than screens they show.
loglens needs nothing set up at all: the log file you already have is
the input. A file can be diffed, reviewed, reverted, and changed with
the same tools as the code around it; a form hides the change behind a
login and leaves no reviewable trace. Files are also what let these
tools compose — a file one tool writes is a file the next tool can read.

- [Kurdistan International Sociological Association website](projects/kurdistansociology-website.md)
- [flowkit](projects/flowkit.md), [uptimekit](projects/uptimekit.md), [sre-toolkit](projects/sre-toolkit.md), [loglens](projects/loglens.md)

## Test the behaviour you depend on

These tools are meant to be trusted at 3 a.m. — the exit code that gates a
pipeline, the burn-rate rule that pages, the triage board that ranks the
noisiest alert first. That trust is pinned down by tests, not by hope:
sre-toolkit's 254 unit tests cover the budget math (including boundary and
validation cases), severity classification, dedupe and ordering, silence
validation and expiry, burn-rate rules, and time-series replay; loglens's
241 cover parsing (both formats, mixed files, corrupt lines), statistics,
timeline bucketing and spike windows, filters, before/after comparisons,
and every CLI flag including the exit-code gates; flowkit's 123 cover flow
validation, topological ordering, retries, timeouts, skip and fail-fast
semantics, and end-phase hook execution; and uptimekit's 98 run fully
offline — probe behaviour verified against loopback HTTP/TCP servers, TLS
paths against injected certificates, and CLI tests that mock the probe
engine, so the suite never touches the network it exists to monitor. CI
runs the same suite on every change — Python 3.10–3.13 for sre-toolkit,
loglens, and flowkit, and Python 3.11 for uptimekit — so the tests that
prove a tool on a laptop are the ones that gate it before it lands.

- [sre-toolkit](projects/sre-toolkit.md), [loglens](projects/loglens.md), [flowkit](projects/flowkit.md), [uptimekit](projects/uptimekit.md)

## Test the bad input, not just the good path

A test suite that only runs the happy path proves the tool works when
everything is already fine — which is the one situation that never needs
proving. The suites here spend their effort on the input the incident
actually brings. loglens's 241 tests cover parsing both formats, mixed
files, and corrupt lines, and the tool itself treats an unparseable line
as a skip, not a fatal error, so a damaged line never costs the analysis
of the thousands of good ones around it. flowkit's 123 cover the flow
file that is wrong on purpose — duplicate step names, dangling
dependencies, cycles, malformed interpolation — rejected before a single
step runs — and retries and timeouts, so a flaky step gets another
chance and a hung step fails instead of stalling the flow. sre-toolkit's
254 include boundary and validation cases for the budget math, and
`burn --replay` tests a policy against a past incident's time series
before it pages anyone. uptimekit's 98 run fully offline, with probe
behaviour verified against loopback HTTP/TCP servers and TLS paths
against injected certificates, so the suite proves the checker without
depending on the very thing it monitors.

The point is that the failure modes are the behaviour you depend on: the
gate that must fail closed, the parser that must not choke, the retry
that must not run forever. Testing the good path proves the tool can do
its job; testing the bad input proves it still does its job when the
world does not cooperate — and the world not cooperating is the whole
reason the tool exists.

- [loglens](projects/loglens.md), [flowkit](projects/flowkit.md), [sre-toolkit](projects/sre-toolkit.md), [uptimekit](projects/uptimekit.md)

## Let reports and documents be outputs, not afterthoughts

The analysis tools generate the documents the workflow runs on, in formats
that can be committed, reviewed, and searched: SLO definitions, status
reports with budget-exhaustion projections, and postmortems with automatic
response metrics from sre-toolkit; Markdown incident reports with per-path
breakdowns and spike windows from loglens; text or JSON run reports with
captured output tails from flowkit; and availability roll-ups with p50/p95
latency percentiles, a per-day trend strip where monitoring gaps stay
visible, SLO status reports (error budget consumed, met-or-breached
status), and a self-contained HTML status page from uptimekit. The report is not a separate chore
after the work — it is what the tool produces.

## Make the same answer readable by people and by machines

A report written for a person should stay written for a person — no
mangled text that a script has to scrape. So every tool offers the same
result in two shapes: the human one by default, and JSON on request.
loglens's `--json` emits the whole summary — counts, rates, top-N,
latency, timeline — for dashboards and scripts to consume without parsing
prose; sre-toolkit's `budget` and `downtime` emit `--json` for pipelines,
postmortem response metrics are available as `--json`, and `metrics
--json` feeds MTTR to dashboards; flowkit's `--json` summary and
`--report` JSON file carry the same run report, including an `output`
field per step; uptimekit's `check --json` gives a machine-readable
verdict, and its JSONL history is the same record every report is derived
from. The two shapes carry the same data — the JSON is not a different
answer, just the same answer in a shape a tool can consume. When a
pipeline needs a number it asks for JSON; when a person needs to
understand, they read the text — and neither has to parse the other's
format.

- [loglens](projects/loglens.md), [sre-toolkit](projects/sre-toolkit.md), [flowkit](projects/flowkit.md), [uptimekit](projects/uptimekit.md)

## One record, many views

Every view of the same work should come from the same record, so two
answers about the same thing cannot disagree. uptimekit keeps one
append-only JSONL history and derives the roll-ups, the SLO reports, and
the public status page from it — the page the public reads and the report
the team acts on are generated from the same file, so they can never drift
apart. loglens does the same with a log file: the summary, the timeline,
the per-path tables, and the Markdown incident report are all computed
from the same parsed records, and `--json` emits that same summary for
tooling to consume. sre-toolkit's incident files feed the postmortem, the
MTTR aggregation, and the fleet roll-ups from one set of records, and a
single flowkit definition produces both the dry-run plan and the run
report. On the web side, the association site's news posts are Markdown
files rendered by the same build into every locale's pages, and the
personal site keeps all of its copy in one data file, separate from the
scene and the components. When there is one record, there is nothing to
keep in sync — and nothing to go stale.

- [uptimekit](projects/uptimekit.md), [loglens](projects/loglens.md), [sre-toolkit](projects/sre-toolkit.md), [flowkit](projects/flowkit.md)
- [Kurdistan International Sociological Association website](projects/kurdistansociology-website.md)
- [Personal site — midya.ca](projects/midya-ca.md)

## Prefer plain text for the record

Every record these tools keep is a file you can open in any editor:
uptimekit's history is append-only JSONL, flowkit's flows and run reports
are JSON and plain text, sre-toolkit's incidents, postmortems, and SLO
definitions are Markdown, and loglens's summaries can be emitted as JSON
for tooling to consume. There is no database to query, no binary state to
decode, and nothing that requires the tool itself to read back what it
wrote. That makes the record greppable, diffable, and committable with the
tools that already exist — the history of a service can be reviewed in a
pull request the same way code is, and a run report can be opened years
later with nothing installed. On the web side the same instinct holds: the
association site's content is Markdown files, and the personal site's copy
lives in one data file, so the words are editable without touching the code
that renders them.

- [uptimekit](projects/uptimekit.md), [flowkit](projects/flowkit.md), [sre-toolkit](projects/sre-toolkit.md), [loglens](projects/loglens.md)
- [Kurdistan International Sociological Association website](projects/kurdistansociology-website.md)
- [Personal site — midya.ca](projects/midya-ca.md)

## Make the same input give the same answer

A tool that gives a different answer each time it is asked is a tool you
cannot reason about, so these tools are built to be reproducible. flowkit
runs steps in deterministic topological order, with declaration order
breaking ties, so the same flow reports the same way run to run even when
steps run in parallel. uptimekit derives every roll-up, SLO report, and
status page from the one append-only history, so the same history always
produces the same report — re-running yesterday's report gives
yesterday's numbers, not a fresh interpretation of them. loglens computes
every view from the same parsed records, and its before/after comparisons
run the same statistics over two slices of one log, so a change in the
numbers means a change in the traffic, not in the tool. sre-toolkit's
burn-rate rules are checked against recorded time series, so a rule that
fires today would have fired on the same data yesterday. The web side
follows the same rule: both sites are static builds from files, so the
same content produces the same site. When the answer changes, the change
is in the world the tool is measuring — and that is the only change worth
investigating.

- [flowkit](projects/flowkit.md), [uptimekit](projects/uptimekit.md), [loglens](projects/loglens.md), [sre-toolkit](projects/sre-toolkit.md)
- [Kurdistan International Sociological Association website](projects/kurdistansociology-website.md)
- [Personal site — midya.ca](projects/midya-ca.md)

## Make work resumable

Work that cannot be picked up where it stopped gets redone from the
beginning — and redone work gets done differently the second time. These
tools keep the state that lets a run resume instead of restart. flowkit's
`--only` / `--skip` reruns a named subset — the steps plus their
transitive dependencies, or everything else — without editing the flow
file, so a failed nightly ETL is rerun from the step that failed, not
from the extract that already succeeded. uptimekit's history is
append-only, so monitoring resumes from the record on disk: a report
re-derived after an outage covers the whole window, including the gap,
and nothing is lost because the process stopped. sre-toolkit keeps
incidents and postmortems as files, so an open action item is still there
with its days-since-resolution count the next time anyone looks, and
`metrics --action-items` exits 1 when items go stale past `--stale-days`,
so unfinished work cannot quietly age out of sight. The record is the
resume point: nothing depends on a process still running, or on anyone
remembering where it stopped.

- [flowkit](projects/flowkit.md), [uptimekit](projects/uptimekit.md), [sre-toolkit](projects/sre-toolkit.md)

## Record the when, not just the what

A result without its time is a fact without its context: it cannot say
when something started, whether it is getting better, or whether a change
made it worse. These tools record time with the observation, so the same
record answers questions about a window, not just about a moment.
uptimekit keeps every probe result in its append-only history, so roll-ups,
the per-day trend strip, and SLO reports can be derived for any window —
and compared window-over-window, so a report says whether availability
improved or regressed, not just what it is now. loglens buckets requests
per minute with `--timeline`, so an incident's start is visible, and
`--split-at` compares the windows either side of a deploy, so "did this
release make things worse?" is a measurement, not a guess. sre-toolkit
replays burn-rate rules against timestamped buckets with `burn --replay`,
so a policy is tested against a past incident before it pages anyone, and
its MTTR aggregation includes a weekly trend view, so "are we getting
faster?" is answered over time. flowkit's run reports carry each step's
captured output tail, so a run stays readable after it finishes. When time
is in the record, the question "when did this change?" has an answer in
the data — not in someone's memory of the night it happened.

- [uptimekit](projects/uptimekit.md), [loglens](projects/loglens.md), [sre-toolkit](projects/sre-toolkit.md), [flowkit](projects/flowkit.md)

## Reduce noise; answer the question first

Incident tooling fails when it adds to the wall of symptoms. sre-toolkit's
triage dedupes repeat alerts, keeps each alert's fire count so frequency
stays visible, and inhibits lower-severity symptoms while a critical is
active, so an incident surfaces as one problem to solve. loglens leads
with the headline answers — error rate, status distribution, hottest
failing paths, and the source IPs behind 5xxs — and only then narrows
into timelines, latency tables, and per-client breakdowns. uptimekit
applies the same discipline to paging: a consecutive-failure flap guard
and a sustained-outage gate mean a self-healing blip does not page, so
an alert still means something worth acting on.

- [sre-toolkit](projects/sre-toolkit.md), [loglens](projects/loglens.md), [uptimekit](projects/uptimekit.md)

## Put the worst thing at the top

A report's order is a decision about where attention goes, so these
tools sort by what needs attention, not by what arrived first.
sre-toolkit's status reports sort worst-first, triage ranks by severity,
`--top-talkers` leads with the noisiest alerts, and `--by-owner` rolls
the board up per team, worst severity first — the first thing on the
board is the thing that needs attention first, and nobody has to scan
past healthy services to find the one that is burning. loglens does the
same with traffic: the per-path Apdex table runs worst-first, so the
endpoint dragging the score down leads; `--path-status` ranks the failing
endpoints worst-first with their per-status-code counts; `--by-path`
ranks endpoints by error count, and `--vs` ranks the paths carrying the
biggest error-count increases as regressions. Sorting by arrival order or
alphabet would be a decision to make the reader do the ranking
themselves — and at 3 a.m., the reader should not have to.

- [sre-toolkit](projects/sre-toolkit.md), [loglens](projects/loglens.md)

## Make different failures look different

A single word — "down", "failed", "error" — hides the diagnosis. These
tools keep failure kinds apart, so the first question after an alert is
already partly answered. uptimekit records a refused connection, a wrong
keyword in the body, a slow response, and a certificate near expiry as
different failures, not just as "down". loglens separates status classes
and pivots per path and per status code, so a spike reads as 502s from one
upstream rather than as a generic error rate, and the methods, agents, and
referers behind the 5xxs say whether it is a bot or real users.
sre-toolkit classifies alerts by severity, ranks triage worst-first, and
reports MTTR per severity, so a critical and a warning never look the same
on the board. flowkit makes the same distinction at the shell: exit code 2
means the flow itself is invalid, 1 means a step failed. When every
failure looks the same, every failure gets the same response — and the
wrong one, half the time.

- [uptimekit](projects/uptimekit.md), [loglens](projects/loglens.md), [sre-toolkit](projects/sre-toolkit.md), [flowkit](projects/flowkit.md)

## Prefer a number to an adjective

"Healthy", "slow", "degraded" — an adjective is a report that cannot be
argued with, because there is nothing to check it against. These tools
report health as a measured number instead, so two people looking at the
same system get the same answer, and a change in the number is a change in
the world. loglens scores user experience as an Apdex number at a stated
threshold — satisfied, tolerating, frustrated — and `--min-apdex 0.94`
turns it into a gate a pipeline can fail on; its latency tables report
p50/p95/p99, not averages, so a slow tail stays visible instead of being
averaged away by mostly fast requests. uptimekit's roll-ups report p50/p95
latency percentiles, and its SLO report states the error budget consumed
and met-or-breached against the declared 99.9 target, so "is it getting
worse?" is a comparison of two numbers, not two impressions.
sre-toolkit's budget command projects when the error budget runs out and
how many bad events remain, its burn-rate rules fire on measured rates over
two windows, and MTTR is reported as mean, median, and p90 per severity
with a weekly trend view, so "are we getting faster?" has numbers to point
at. A number can be wrong — and then it can be checked, argued with, and
fixed. An adjective can only be believed.

- [loglens](projects/loglens.md), [uptimekit](projects/uptimekit.md), [sre-toolkit](projects/sre-toolkit.md)

## Don't claim what you didn't observe

A report is only as honest as the observations behind it, and these tools
refuse to fill in the blanks. uptimekit never credits an endpoint with
uptime it did not observe: a period with no probe results produces no
success records, so the per-day trend strip shows a gap rather than a
green stretch the checker never actually saw — the report never rewards
the checker for time it was not running. loglens does the same with messy
input: a line it cannot parse is skipped, not guessed at, so a damaged
line never costs the analysis of the thousands of good ones around it and
never becomes a made-up data point either. sre-toolkit's burn-rate rules
are evaluated against the recorded time series — `burn --replay`
re-evaluates every rule at each timestamped bucket and reports each firing
interval — so an alerting policy is tested against a past incident that
actually happened, not against a scenario somebody imagined. The
discipline is the same in each case: the record says what was seen, and
what was not seen stays visibly absent instead of being smoothed over
into a reassuring answer.

- [uptimekit](projects/uptimekit.md), [loglens](projects/loglens.md), [sre-toolkit](projects/sre-toolkit.md)

## One observation is not a signal

A single bad reading is not evidence — it is a reading. These tools act
only when the pattern holds across more than one observation, because the
cost of acting on noise is an alert nobody trusts and a gate that fails
for nothing. uptimekit's flap guard counts consecutive failures, so one
failed probe never opens an incident — an endpoint failing once an hour
all day never looks like an outage — and the sustained-outage gate pages
only on an incident that stays open, so a blip that heals within minutes
is a record in the history, not a 3 a.m. wake-up. sre-toolkit's burn-rate
rules fire on measured rates over two windows — a fast burn over a short
window and a slow bleed over a long one — so one bad minute is not enough
to page, and `burn --replay` tests a policy against a past incident's time
series before it pages anyone. loglens's spike buckets flag only when both
the error rate and the count clear a threshold, so a single error in a
quiet minute never reads as a spike. flowkit gives a flaky step another
chance — `retries: 2` means at most three attempts — before the run is
declared failed. In each case the tool waits for the pattern to confirm
itself, and what it records in the meantime stays visible: the failed
probe is in the history, the single error is in the log, the first failed
attempt is in the run report. Waiting is not ignoring — it is refusing to
mistake one data point for a conclusion.

- [uptimekit](projects/uptimekit.md), [sre-toolkit](projects/sre-toolkit.md), [loglens](projects/loglens.md), [flowkit](projects/flowkit.md)

## Compare against a baseline, not against nothing

A number on its own is a fact without a verdict. An error rate of 2%
means nothing until you know what it was before the deploy; an
availability of 99.8% means nothing until you know what the last window
looked like. So these tools always answer against something real, never
in isolation. loglens compares the windows on either side of a deploy —
`--split-at` reports the error-rate delta, the newly failing paths, and
the paths that recovered — and `--vs baseline.log` answers "did this
release make things worse?" across two whole logs, ranking the paths
with the biggest error-count increases as regressions. uptimekit's
roll-ups carry a window-over-window comparison, so a report says whether
availability improved or regressed against the previous window instead
of presenting one window alone. sre-toolkit tests a policy the same way:
`burn --replay` re-evaluates every rule at each timestamped bucket of a
past incident's time series and reports each firing interval, so an
alerting policy is judged against an incident that actually happened
before it pages anyone.

The baseline has to be real — recorded history, not an imagined normal.
A comparison against a made-up target flatters the present just as
surely as a number with no context at all. But with a real baseline the
question changes from "what is the number?" to "worse than what?" — and
that is the question that decides whether anything needs doing. A tool
that only reports the moment can tell you something happened; a tool
that compares it with what came before can tell you whether it matters.

- [loglens](projects/loglens.md), [uptimekit](projects/uptimekit.md), [sre-toolkit](projects/sre-toolkit.md)

## Automate the check, not the judgement

These tools are built to answer the question, not to act on the answer —
the judgement stays with the person reading the report. sre-toolkit's
`burn --suggest` emits a policy for a human to adopt, it does not install
one; triage ranks the board and routes each alert to a named owner, so the
triaged list is an assignment list, not an auto-resolution. loglens's
`--vs` ranks the paths carrying the biggest error-count increases as
regressions and `--split-at` answers "did this release make things
worse?" — but neither rolls anything back; `--errors` lists the exact
failing requests, so a person can follow the spike to its cause in one
step. uptimekit's gates stop a pipeline, and the sustained-outage gate
pages a person — the tool escalates to a human, it never resolves the
incident itself, and the incident stays open on the record until a success
closes it. flowkit's `--dry-run` prints the plan for review before
anything executes, and its exit code says whether the flow succeeded so a
pipeline — or a person — can act on the result. The web side follows the
same split: the association site's deploy is a push to `main`, so the
thing that is reviewed in a pull request is the thing that goes live — the
build renders it, a person decides when. A tool that acts on its own
conclusions hides the decision from the person who owns it; a tool that
reports clearly and stops there keeps the judgement where it belongs —
with someone who can see the context the tool cannot.

- [sre-toolkit](projects/sre-toolkit.md), [loglens](projects/loglens.md), [uptimekit](projects/uptimekit.md), [flowkit](projects/flowkit.md)
- [Kurdistan International Sociological Association website](projects/kurdistansociology-website.md)

## Put an expiry on every exception

Every tool here has a way to hold something back — a silence, a retry, a
flap guard, a gate that waits — and every one of those holds is bounded,
because a suppression with no expiry is a problem that stops existing on
paper while it keeps happening in the world. sre-toolkit's silences are
bounded, reasoned, and expiring: matched on service, severity, or summary
text, and the alerts they match move into a visible silenced section
rather than disappearing, so an alert that is still firing when the
silence ends comes back to the board instead of staying hidden. flowkit
bounds its retries — `retries: 2` means at most three attempts, with the
backoff doubling each time — and a timeout is a failed attempt that still
consumes a retry, so a step that cannot finish does not get retried
forever on the hope that it eventually will. uptimekit's flap guard needs
consecutive failures before an incident opens, and its sustained-outage
gate only pages once the outage has lasted — but the incident stays open
on the record until a success closes it, and `report --fail-open` keeps
gating CI on it in the meantime. The pattern is the same in each case:
the tool is allowed to wait, to retry, to stay quiet for a while — and
the waiting always has a limit, after which the problem is visible again
whether anyone remembered it or not.

- [sre-toolkit](projects/sre-toolkit.md), [flowkit](projects/flowkit.md), [uptimekit](projects/uptimekit.md)

## Bound the history you keep

A record that grows without bound is a second problem waiting to happen —
a disk that fills, a report that slows, a history nobody can move. The
answer is not to delete the past, and not to keep all of it forever: it is
to bound the history by a rule declared up front. uptimekit keeps every
probe result in an append-only JSONL history, because roll-ups, trend
strips, and SLO measurement all need the past — and then
`compact --keep 30d` prunes that history to the last thirty days, so a
checker that runs from cron for months needs no manual cleanup and never
grows without bound. Nothing already recorded is rewritten in the
process: results are appended, never edited in place, so pruning removes
old entries without ever altering what remains — and the compaction
rewrites the history atomically, so a crash mid-compaction leaves either
the old file or the new one, never a half-written record. The bound is
part of the design, not a chore left for later: the history stays complete
enough to answer for, small enough to carry — one file, readable with
ordinary text tools, that a fresh install can pick up and continue.

- [uptimekit](projects/uptimekit.md)

## Keep a failure contained

A failure should stop the work that depended on it, and nothing else.
flowkit draws that line with the dependency graph: a failed step skips
its dependents — and theirs — so nothing runs on a result that never
happened, while `continue_on_error` lets the rest of the flow proceed,
and the run's exit code still says the flow failed. The same boundary
holds for the hooks that report the outcome: a broken notification hook
skips only its own hook dependents, never the cleanup step, and fail-fast
is deliberately not applied to hooks, so the failure being reported
cannot silence the report. loglens draws the same line around bad input:
a line it cannot parse is skipped, not fatal, so one damaged line never
costs the analysis of the thousands of good ones around it. uptimekit
draws it around the report itself: the status page is a single
self-contained HTML file served from static hosting, independent of the
endpoints it reports on, so the page describing an outage does not go
down with the service it describes. In each case the tool decides in
advance what a failure is allowed to take with it — its dependents, its
bad line, its own process — and everything outside that boundary keeps
working, so one failure stays one failure instead of becoming a cascade.

- [flowkit](projects/flowkit.md), [loglens](projects/loglens.md), [uptimekit](projects/uptimekit.md)

## Design for the failure mode

A tool that watches something fail should be shaped by the ways that
thing can fail — not by the happy path with error handling added
afterwards. Start by listing the failure modes, then give each one its
own treatment. flowkit does this for shell commands: a step can be
flaky, so it gets bounded retries with backoff that doubles each time;
it can hang, so every attempt has a timeout and a timeout counts as a
failed attempt; it can fail outright, so its dependents are skipped,
and fail-fast stops the rest of the flow while `continue_on_error`
lets the independent steps proceed. uptimekit does the same for
endpoints: a single failed probe is a blip, not an outage, so the flap
guard only opens an incident on consecutive failures; a brief outage
is a record, not a page, so the sustained-outage gate waits for
`--max-open-minutes` before paging; slow is a failure mode of its own,
so a latency assertion turns a slow response into down, and a
certificate near expiry is a failure while there is still time to
renew it. sre-toolkit's burn-rate alerting is built the same way: a
fast burn and a slow bleed are different failure modes, so different
windows catch each one, and both windows must agree before anything
pages — a blip on one window never wakes anyone. When the failure
modes are named up front, the tool's behaviour in each one is a
decision, not an accident — and the operator never has to discover, at
3 a.m., which failure the tool never thought about.

- [flowkit](projects/flowkit.md), [uptimekit](projects/uptimekit.md), [sre-toolkit](projects/sre-toolkit.md)

## Keep the check cheap enough to run often

A check that is expensive to run gets run rarely, and a check run rarely
notices anything in time. So these tools are built to cost almost
nothing per run: standard-library only, no database to start, no daemon
to keep alive, no service to call home to. uptimekit's `check` is one
process that probes its endpoints, appends to the JSONL history, and
exits — cheap enough to run from cron for months, which is what makes a
flap guard and a sustained-outage gate meaningful instead of
theoretical, and there is nothing to pay for to keep it running: no
subscription, no hosting bill, no service to patch. loglens turns a log
file into a one-screen summary in a single command, without standing up
a log pipeline first, and the same command drops into a cron health
check against a fresh log slice. flowkit runs a flow by executing shell
commands — the runner adds validation and ordering, not a scheduler
service to install. sre-toolkit's budget math, burn-rate rules, and
triage run on files on disk — SLO definitions, incident records, rule
files — not on a query against a service that might itself be down. The
same instinct sets the cost of the checks that guard the code: the test
suites run on every change, and uptimekit's 98 tests run fully offline,
so the suite that proves the monitoring tool never waits on the network
it exists to monitor. When the check is cheap, running it often is the
default — and a check that runs often is the one that catches the
problem while it is still small.

- [uptimekit](projects/uptimekit.md), [loglens](projects/loglens.md), [flowkit](projects/flowkit.md), [sre-toolkit](projects/sre-toolkit.md)

## Write down why, not just what

Every project in this portfolio records its decisions, not just its
behaviour. uptimekit's design decisions run to six subsections —
probing, history, reports, incidents and SLOs, the status page, running
it — and each bullet carries its reason with it: a TLS expiry threshold
turns a certificate quietly approaching expiry into a failure while
there is still time to act. flowkit's fifteen decisions are written the
same way, as rules with their reasons attached: validation happens
before execution because a bad flow file should never half-execute.
sre-toolkit and loglens each keep a Decisions section, and both websites
record theirs — the association site's direction-is-layout choice, the
personal site's generated-not-shipped galaxy. The reasoning is the part
that survives: code gets rewritten and defaults get changed, but the
constraint or trade-off behind a choice is what tells a later reader
whether the choice still holds, or whether the world moved and the
decision should move with it. A decision written down can be argued
with, revisited, and reversed on purpose; one that lives only in the
author's head gets re-litigated from scratch — or preserved as cargo
cult, because nobody remembers why it was made. This file is the same
instinct applied once more: the principles here are the reasons,
collected in one place, so the next project starts from them instead of
re-deriving them.

- [sre-toolkit](projects/sre-toolkit.md), [loglens](projects/loglens.md), [flowkit](projects/flowkit.md), [uptimekit](projects/uptimekit.md)
- [Kurdistan International Sociological Association website](projects/kurdistansociology-website.md)
- [Personal site — midya.ca](projects/midya-ca.md)

## Make the first run useful

A tool earns its place by answering its question the first time it is
run, before any setup has been paid for. uptimekit is explicit about
this: a single `check` invocation answers "is it up?" immediately — no
scheduler, daemon, or setup needed to try it — and if Python is
installed, uptimekit runs, with no dependencies, no database, and
nothing to install, patch, or keep running. loglens takes the same
stance toward the incident: a log file you already have is enough,
turned into a one-screen summary in a single command, without learning
a query language or standing up a log pipeline first. sre-toolkit's
`burn --suggest` works the same way for a new service: it emits the
standard three-tier multi-window policy for any SLO window, so the
first alert policy comes from a known-good default instead of a guessed
threshold. flowkit runs a JSON flow file as written — the file is the
whole definition, checked up front and then executed — so the first run
is a real run, not a configuration exercise.

The point is that setup is a cost charged before value, and most tools
charge it up front: accounts, servers, schemas, a query language to
learn. These tools push that cost to zero or near it, because the
moment a tool is most needed — an incident, a new service, a first
check — is the moment nobody has time to configure it. Defaults carry
the knowledge — the standard policy, the sensible probe thresholds — so
the first run is useful and the second run is a refinement, not a
rescue. A tool you can run once, by hand, and get an answer from is a
tool that will actually be there when it matters.

- [uptimekit](projects/uptimekit.md), [loglens](projects/loglens.md), [flowkit](projects/flowkit.md), [sre-toolkit](projects/sre-toolkit.md)

## Detect, don't configure

Every question a tool asks its user is a question the user has to
answer correctly, in the middle of whatever they were doing. The
tools here answer the ones they can answer themselves. loglens never
asks what format a log is in: format detection runs per line, with
`--format auto` the default, so a file that switches between combined
and JSON lines parses both, and the tool adapts to the log instead of
the other way around. midya.ca never asks a visitor to pick a quality
setting: a low, mid, or high rendering profile is chosen from the
device itself — viewport size, device memory, CPU cores, pixel
ratio — and the profile sets the particle budgets, the bloom
strength, and a 40/55/60 fps frame cap. The same instinct covers the
edges: a visitor who prefers reduced motion gets a single static
frame without asking, and if WebGL is unavailable at all, a CSS
gradient takes over so the page still reads.

The point is that configuration is a guess the user makes on the
tool's behalf, and the tool is usually in a better position to know.
A log file declares its own format line by line; a device reports its
own capabilities. Asking the user to restate what the environment
already says adds a step, a chance to be wrong, and a setting to
maintain — and a setting chosen once is a setting that goes stale
when the environment changes. Detection keeps the decision where the
facts are, at the moment the tool runs. The user still gets an
override — loglens accepts `--format` for a single forced format —
because detection is the default, not a cage: the tool guesses first
and lets the human correct it, instead of making the human guess
first and letting the tool correct them.

- [loglens](projects/loglens.md), [midya-ca](projects/midya-ca.md)

## Work without the network

The tools here do their job on the machine they run on, with nothing
to reach out to. uptimekit's reports are generated from the local JSONL
history, so producing a report makes no network call — the checker only
touches the network when it probes, never when it reports, and a report
can be built even while the monitored endpoints are unreachable. Its 98
unit tests run fully offline, so the suite proves the checker without
depending on the very thing it monitors. The other utilities are the
same shape: sre-toolkit, loglens, and flowkit are standard-library-only
Python that read local files and write local output, and the two
websites are static builds with no server behind them — there is no
account to sign into, no API key to rotate, and no hosted service that
has to be up for the tool to work.

That matters most at the moment the tool is needed. An incident tool
that needs the network is a tool that fails exactly when the network is
the problem: the log file is on the disk in front of you, the history
is in a file you can read, and the answer should come from those, not
from a service that may itself be down. Working offline is also what
makes the tools droppable into any environment — a laptop, a server
mid-incident, a minimal host with only Python installed — with no
install step, no package to fetch, and no runtime to provision. The
network is used only where the job itself demands it: uptimekit probes
endpoints because probing is the job. Everything else — the analysis,
the report, the verdict — happens locally, so the tool keeps working
through the outage it exists to describe.

- [uptimekit](projects/uptimekit.md), [sre-toolkit](projects/sre-toolkit.md), [loglens](projects/loglens.md), [flowkit](projects/flowkit.md)
- [Kurdistan International Sociological Association website](projects/kurdistansociology-website.md), [Personal site — midya.ca](projects/midya-ca.md)

## Put the check in the pipeline

A check that only reports is a check that can be ignored. The same
command that investigates an incident should also be the gate that
stops a bad state from shipping, so the check is wired into the
pipeline rather than sitting beside it. uptimekit's `report
--fail-open` gates CI on open incidents, and `--fail-slo` exits 1
when an SLO budget is breached — a breached budget stops a pipeline
the same way an open incident does, instead of sitting in a dashboard
nobody checks. loglens does the same for a deploy: `--min-apdex 0.94`
turns the user-satisfaction score into a pipeline gate, and
`--max-error-rate 0.05` exits 1 when the 5xx rate breaches the
threshold, so the command that investigates an incident also guards
against the next one. flowkit's exit codes are the same contract at
the workflow level — 0 the flow succeeded, 1 a step failed, 2 the
flow file itself is invalid — so a pipeline or cron job can act on
the result without parsing output. sre-toolkit carries it through
every command: meaningful exit codes make each one a scriptable
health gate, and `metrics --action-items` exits 1 when postmortem
items go stale past the threshold.

The point is that a gate is a check with a consequence attached. A
report asks a human to notice; a gate makes the pipeline notice on
its own. That is the difference between a tool that tells you
something is wrong and a tool that stops something wrong from going
out. The checks here are built to be gates from the start — exit
codes, not parsed output — because a check that has to be remembered
will be forgotten, and one that is wired in will run whether or not
anyone is watching.

- [uptimekit](projects/uptimekit.md), [loglens](projects/loglens.md), [flowkit](projects/flowkit.md), [sre-toolkit](projects/sre-toolkit.md)

## Make a failure explain itself

An exit code says something failed. It does not say what, or why — and
a gate that fails without saying why hands the person it pages a second
incident: the investigation. So the verdict and the evidence travel
together, in the same output, in the same place. flowkit prints a failed
step's captured output tail under its report line, so the reason for the
failure is in front of you without opening a log file — and
`--output-dir` keeps the full per-step logs for the whole story. loglens's
`--errors` lists the failing requests themselves — timestamp, client,
method, path, status, duration — so the path from "the rate spiked" to
the exact requests that failed is one flag. sre-toolkit's status reports
carry budget-exhaustion projections: not just that the budget is burning,
but when it runs out and how many bad events remain, which turns a number
into a decision about whether there is room to ship. uptimekit's SLO
report does the same for availability: it states the error budget
consumed against the declared 99.9 target, so "breached" arrives with
the measurement behind it.

The point is that a check's job is not finished when it returns 1. The
person reading the failure at 3 a.m. should not have to re-run the tool,
open a log, or reconstruct what the tool already knew in order to
understand it. If the tool had to look at the evidence to reach its
verdict, it should show the evidence with the verdict — the failing
step's tail, the failing requests, the number behind the breach. A
failure that explains itself gets fixed; a failure that only announces
itself gets investigated first, and fixed later.

- [flowkit](projects/flowkit.md), [loglens](projects/loglens.md), [sre-toolkit](projects/sre-toolkit.md), [uptimekit](projects/uptimekit.md)

## Answer the question, don't just raise the alarm

An alert says something needs attention. It does not say what to do about
it — and a tool that only pages has handed the decision to the person it
woke up. These tools are built to answer the question the person actually
asked, not just to notice that something changed. uptimekit's single
`check` answers "is it up?" right now, and the same history answers how
it has been — roll-ups, trend strip, and SLO status — so one checker gives
both the momentary answer and the longer view. loglens turns a log file
into a one-screen summary that answers "what broke, when, and for whom",
without a query language or a log pipeline first. sre-toolkit's burn-rate
math does not stop at the current rate: its exhaustion projections say
when the budget runs out and how many bad events remain, which turns a
number into a decision — ship, or do reliability work first. flowkit's
reports carry the captured output tails, so the run's report is the record
of what happened, not a pointer to a log somewhere else.

The difference is between a tool that watches and a tool that informs. An
alert is a starting point: it tells you to look. An answer is an ending
point: it tells you what you are looking at, and often what follows from
it. A check that answers its question on the first run — "is it up?",
"what broke?", "how long do we have?" — is a tool you reach for; a check
that only raises the alarm is a tool you learn to ignore, because every
alarm still costs the same investigation. The alarm gets your attention.
The answer earns it back.

- [uptimekit](projects/uptimekit.md), [loglens](projects/loglens.md), [sre-toolkit](projects/sre-toolkit.md), [flowkit](projects/flowkit.md)

## Measure the response, not just the outage

An incident is two things: the failure, and the response to it — and
only the second one is under your control. So these tools measure the
response the same way they measure the system. sre-toolkit's postmortems
carry automatic response metrics, and its MTTR aggregation reports mean,
median, and p90 per severity with a weekly trend view, so "are we getting
faster?" is answered over time, not from a single window's average — a
single fast incident proves nothing, but a trend that moves does. The
follow-through is measured too: `metrics --action-items` groups open
postmortem items per incident with days since resolution, and exits 1
when items go stale past `--stale-days`, so unfinished work cannot
quietly age out of sight — the fix for the incident is itself a gate,
not a list somebody meant to get to. uptimekit keeps the same discipline
on the monitoring side: an incident stays open on the record until a
success closes it, so the outage is not declared over by a silence, and
`report --fail-open` keeps gating CI on it in the meantime.

The point is that an incident ends when the response is measured and
the follow-up is done, not when the alert stops firing. A team that
only measures the outage learns how often things break; a team that
measures the response learns whether it is getting better at fixing
them. The numbers are the same kind in both cases — mean, median, p90,
days since resolution — but they point at the people, not the system,
and the people are the part that can improve. Measure the failure and
you know what happened. Measure the response and you know whether the
next one will go better.

- [sre-toolkit](projects/sre-toolkit.md), [uptimekit](projects/uptimekit.md)

## Don't act on a single failure

A failure is worth recording the moment it happens, but acting on it —
waking someone, opening an incident, failing a step — should cost more
than one bad result. uptimekit records every probe result in its
history, yet a single failed probe does not open an incident: the flap
guard counts consecutive failures, so an endpoint that fails once an
hour all day never looks like an outage, and only an unbroken run of
failures does. Paging costs more still: the sustained-outage gate
(`--max-open-minutes`) pages only on an incident that stays open, so a
failure run that heals within minutes never reaches a pager. Opening an
incident and paging a person are two different thresholds, and a
self-healing blip is a record in the history, not a 3 a.m. wake-up.
sre-toolkit applies the same rule to burn-rate alerting: it fires only
when burn is elevated on both the long and the short window, so a blip
on one window never pages anyone — the pair, not a single threshold,
decides — and `burn --replay` tests a policy against a past incident's
time series before it pages anyone at all. flowkit does it at the step
level: a flaky step gets bounded retries with exponential backoff, and
a timeout is a failed attempt that still consumes a retry, so a hung
step fails instead of stalling the flow — but only after it has had
its chances.

The point is that recording and acting are different decisions, and the
tools keep them apart. Every failure is written down, because the
history is where the pattern shows up later; but the expensive action —
the page, the incident, the failed run — waits for the failure to prove
it is real, by persisting, by agreeing across windows, or by surviving
its retries. An alert that fires on noise trains people to ignore it,
and an ignored alert is worse than no alert at all, because the next
real one arrives to an audience that has already learned not to listen.
Wait for the second failure and you still catch every real outage; the
only thing you lose is the false alarm.

- [uptimekit](projects/uptimekit.md), [sre-toolkit](projects/sre-toolkit.md), [flowkit](projects/flowkit.md)

## Name the command for the job, not the mechanism

The command line is the interface most people will actually meet, so its
words should say what the user wants, not how the tool does it. The
commands here are verbs for the job: `burn` for burn-rate alerting,
`triage` for alert triage, `metrics` for the postmortem numbers, `check`
and `report` for uptimekit. The flags read the same way:
`--max-error-rate` states the line that must not be crossed,
`--min-apdex 0.94` states the satisfaction the traffic must meet,
`--fail-open` and `--fail-slo` say what the gate does when it fails,
`--top-talkers` asks for the noisiest alerts, and `--stale-days` asks
how old an open item may be before it counts as stale. Nothing is named
after its implementation — there is no `--compute-rolling-window` or
`--parse-combined-log` — because the person typing the command is
thinking about the incident, not the algorithm.

That matters most at the moment the tool is used under pressure, when
nobody is reading documentation. A flag whose name states its intent
can be guessed, remembered, and typed correctly the first time; a flag
named after a mechanism has to be looked up, and the lookup happens
while the incident is still open. The same instinct is behind the exit
codes — 0 for success, 1 for a failed step, 2 for an invalid flow —
and behind `--dry-run` printing a plan instead of a trace: the tool
should be readable at the point of use, by the person using it, without
a manual open beside it.

- [sre-toolkit](projects/sre-toolkit.md), [loglens](projects/loglens.md), [flowkit](projects/flowkit.md), [uptimekit](projects/uptimekit.md)

## Degrade in stages, not all at once

A system that only knows two states — working and broken — fails the
moment conditions get worse. The ones here step down instead. The
personal site chooses a low, mid, or high rendering profile from the
device — viewport size, device memory, CPU cores, pixel ratio — and the
profile sets the particle budgets, the bloom strength, and a 40/55/60
fps frame cap, so a weak device gets a lighter galaxy rather than a
stalled page. A visitor who prefers reduced motion gets a single static
frame, rendering pauses while the tab is hidden, and if WebGL is
unavailable at all, a CSS gradient takes over so the page still reads.
uptimekit watches the same slope from the other side: p50/p95 latency
percentiles make a rising slow tail visible before it crosses a latency
assertion and turns into a failure, and a TLS expiry threshold turns a
certificate quietly approaching expiry into a failure while there is
still time to act. flowkit degrades a run the same way: a flaky step
gets bounded retries with backoff — another chance, not an endless one
— a timeout is a failed attempt rather than a stalled flow, and a
failed step skips only its dependents, so the rest of the flow still
runs.

The point is that degradation is a spectrum with room to act in it, and
the design should use that room. A hard cliff turns every bad day into
an outage; a staircase gives the system somewhere to stand while
conditions improve, and gives the people watching it time to respond
before the last step. Step down gracefully, and surface the slope early
— the failure that arrives after a visible decline is a decision made
too late, not a surprise.

- [Personal site — midya.ca](projects/midya-ca.md), [uptimekit](projects/uptimekit.md), [flowkit](projects/flowkit.md)

## Prefer boring technology

Every project here is built on the least surprising thing that does
the job. The four Python tools are standard library only — no
dependencies to install, no third-party package to break when it
changes, nothing to fetch on a machine mid-incident. uptimekit adds no
database and no server to that: its whole state is one JSONL file, its
report is plain HTML, and the checker is small enough to read end to
end, so trusting the monitor never means trusting a stack of code
nobody has read. The two websites make the same choice in a different
shape: both are static builds from files — the association site a
Next.js static export served from Cloudflare, the personal site a Vite
build on App Platform — so there is no server to keep up, no admin
panel, and no database row to write when a news post is published; the
post is a Markdown file, and pushing to main is the deploy.

Boring is not a lack of ambition; it is a budget. Every dependency,
service, and moving part is a future failure mode, a future patch, and
a future thing to explain to the next person. Spend that budget only
where the requirement genuinely needs it, and the system you build is
one a stranger can run, read, and fix — on the first day, and on the
worst day.

- [sre-toolkit](projects/sre-toolkit.md), [uptimekit](projects/uptimekit.md), [flowkit](projects/flowkit.md), [loglens](projects/loglens.md), [Kurdistan International Sociological Association website](projects/kurdistansociology-website.md), [Personal site — midya.ca](projects/midya-ca.md)

## Small enough to read end to end

A tool you cannot read is a tool you have to take on faith — and faith
is the first thing that fails at 3 a.m., when the monitor itself is
suspect and the question is whether the tool is lying to you. So these
tools are kept small enough that a reader can audit the whole thing in
one sitting. uptimekit's checker is standard library only with no
dependencies, and its whole state is one JSONL history file — the
checker is source a reader can audit, so trusting the monitor never
means trusting a stack of third-party code nobody has read, and a bug
in the checker is one you can find by reading it. flowkit's flows are
the same shape at the definition level: the whole run — steps,
dependencies, retries, environment — is one JSON file you can read in
a single file, so the nightly ETL is visible as written rather than
assembled from configuration spread across screens. The websites
follow the same rule for their content: the association site's news
posts are Markdown files, and the personal site keeps all of its copy
in one data file, so the words are readable without the code that
renders them.

The point is that size is a trust decision. A tool with a dependency
tree, a database, and a service behind it can only be trusted through
its documentation and its reputation; a tool small enough to read can
be trusted through its source. That matters most exactly when trust is
scarce — during an incident, on a machine you did not set up, in front
of a result you do not believe. If you can read the whole thing, you
can answer the question "is the tool wrong, or is the world wrong?"
yourself, from the code, instead of guessing. Keep the tool small
enough that the answer is in reach.

- [uptimekit](projects/uptimekit.md), [flowkit](projects/flowkit.md)
- [Kurdistan International Sociological Association website](projects/kurdistansociology-website.md), [Personal site — midya.ca](projects/midya-ca.md)

## Measure from the outside, like a user would

A server that reports itself healthy is not the same as a service a
person can use. The health that matters is the one the user
experiences, so these tools measure from the outside, the way a
visitor would. uptimekit probes endpoints over HTTP — status, content,
and latency — plus TCP connect and TLS expiry, rather than reading
server logs after the fact, so it catches a site that is up for the
server but broken for the people trying to use it; and "up" means the
content is right, not just the status code, so a page that returns 200
with the wrong body still counts as down. The probes only read — they
never write to the service they watch — and nothing is installed on
what is monitored, so the check sees the service the way a visitor
does without becoming another way it can break. loglens measures the
same way from the other side: its Apdex score is one number for how
the traffic felt — satisfied, tolerating, frustrated at a stated
threshold — with a per-path table worst-first, so the endpoint
dragging the experience down leads, and `--min-apdex 0.94` turns that
feeling into a pipeline gate. The personal site applies the same
instinct to rendering: it chooses its low, mid, or high profile from
the visitor's actual device — viewport size, device memory, CPU cores,
pixel ratio — so the experience is judged on the hardware it actually
runs on, not the machine it was built on.

The point is that internal metrics flatter the system that produces
them. A process can be running, a queue can be draining, a dashboard
can be green — and the person on the other end still cannot get their
work done. Measure the thing the user touches, from where the user
stands, and the numbers stop being a report about the system and start
being a report about whether it works.

- [uptimekit](projects/uptimekit.md), [loglens](projects/loglens.md), [Personal site — midya.ca](projects/midya-ca.md)

## Don't let the monitor share the fate of what it monitors

A monitoring tool that goes down with the thing it watches is worse
than no monitor at all: it fails silently at the exact moment you need
it, and the outage takes the record of itself with it. So these tools
are built to keep working when the thing they watch does not.
uptimekit's reports are generated from the local JSONL history, so
producing a roll-up, a trend strip, an SLO status, or the status page
makes no network call — the checker only touches the network when it
probes, never when it reports, and a report can be built even while
the monitored endpoints are unreachable. The status page is a plain
HTML file, so the page describing an outage never goes down with the
service it describes, and the reports are plain files that can be
committed and searched like any other document, so the record of an
incident lives alongside the code instead of inside a service that
might itself go down. loglens works the same way from the other side:
point it at a local log file and it gives you the numbers, with no
pipeline or service standing between you and the answer. flowkit's
run reports carry captured output tails, so the record of a run
survives the run itself without a separate logging setup. And the
checker's own test suite runs fully offline, so the tests prove the
checker without depending on the very thing it monitors.

The rule is about shared fate: whatever the tool depends on becomes a
second thing that can fail at the same time as the first. A monitor
that needs the network to tell you the network is down, a status page
hosted on the service whose outage it announces, a report that lives
in a database that is itself the incident — each one turns one failure
into two. Keep the tool's own needs smaller than the thing it watches,
and the answer is still there when the system it describes is not.

- [uptimekit](projects/uptimekit.md), [loglens](projects/loglens.md), [flowkit](projects/flowkit.md)

## Design around the constraint, not against it

The hard parts of these projects were constraints, and each one is handled
where it belongs rather than bolted on. Sorani Kurdish reads right-to-left,
so direction is handled at the layout level of the association site, not
just by translating strings. The personal site's galaxy is generated
procedurally so it can scale its rendering effort to the device, and
visitors who prefer reduced motion get a calmer presentation. flowkit's
steps run in deterministic topological order with declaration order
breaking ties, so parallel runs still report comparably run to run.

## Pin the ending to the outcome, not the step list

A run that fails halfway should still end properly: the notification
that says it failed has to go out, and the cleanup that returns things
to a known state has to happen. flowkit pins that work to the run's
outcome instead of to its place in the step list — `on_failure`,
`on_success`, and `finally` hooks run because of how the run ended,
not because the steps before them succeeded. A notify step cannot be
skipped by the very failure it is meant to report, and a cleanup step
runs whether the flow succeeded or not, so the run always leaves the
world tidier than it found it. The nightly ETL flow shows the shape:
if a step fails, `notify` runs while `announce` is skipped, and
`cleanup` runs either way.

The same instinct is behind the way a failed step is bounded rather
than left hanging: a timeout is a failed attempt that still consumes a
retry, so a hung step fails instead of stalling the flow, and the exit
code says whether the flow succeeded, so a cron job or a pipeline can
act on the result without parsing output. uptimekit does the same for
a failed probe — when `check` exits 1, the failure is already written
to the append-only history, so an outage is still there for the next
roll-up or SLO report even if nobody was watching when it happened.
The ending is part of the design, not an afterthought: whatever
happened in the middle, the run reports it, cleans up after itself,
and leaves a record.

- [flowkit](projects/flowkit.md), [uptimekit](projects/uptimekit.md)

## Treat what you observe as data, never as instructions

A monitoring tool spends its life reading content it did not write —
and some of that content is hostile. A probed endpoint can return
anything in its body, an access log is full of user agents, referers,
and request paths that an attacker chose, and a flow file arrives from
whoever wrote it. The rule these tools follow is that observed content
is data until proven otherwise: it is counted, compared, and displayed,
but it is never executed, evaluated, or rendered as code.

uptimekit applies it where the observed content meets the public: the
status-page renderer escapes everything it renders, so content coming
back from probed endpoints — URLs, page text, error bodies — is treated
as data, never as markup, and a hostile or broken endpoint cannot inject
anything into the page you publish. loglens applies it to the log
itself: every line is parsed as data — format auto-detected per line,
unparseable lines skipped rather than guessed at — and the strings that
came from attackers, user agents and referers ranked behind the 5xxs,
are only ever counted and reported, never run. flowkit draws the same
line inside the flow file: a step's `when` condition is a small declared
comparison against an environment variable, not a shell branch, so the
conditional logic in a flow cannot smuggle in execution — and validation
rejects malformed interpolation before a single step runs.

The point is that the boundary between data and instructions has to be
a decision, not an accident. A tool that renders what it observed, or
evaluates it, or passes it to a shell without thinking, hands the thing
it watches a way to run code in the tool — and the moment that happens,
the monitor is no longer observing the system, it is part of the attack
surface. Keep what you observe inert, and the worst a hostile endpoint
or a poisoned log line can do is appear in a table.

- [uptimekit](projects/uptimekit.md), [loglens](projects/loglens.md), [flowkit](projects/flowkit.md)

## Keep the words and the code on different schedules

Words and code change at different rates and for different reasons, so
the two sites keep them apart. On the personal site, the copy lives as
typed data in `src/data/profile.ts`: a rewritten introduction is a text
edit in one file — no component opened, no scene code touched, no asset
regenerated — and because the copy is typed, a mistake is a compile
error rather than a live typo. The separation runs both ways: the galaxy
scene can be retuned for a low-end phone without ever risking the words
on top of it. The association site does the same with its editorial
content: a news post is a Markdown file per locale, with `title`,
`date`, `excerpt`, and `author` frontmatter, and the UI strings live in
per-locale JSON dictionaries, so publishing a conference announcement
means writing three files and pushing to `main` — no admin panel, no
database row, no server restarted.

The point is that every change should touch only what it is about. When
copy is embedded in components, a wording fix becomes a code change,
reviewed and deployed like one, and a rendering change becomes a risk to
the words. When the words are data — typed on one site, files on the
other — a copy edit is a data edit with the same local check as any
other change, and the code can keep moving on its own schedule. The
words stay correct while the rendering gets faster, and the rendering
stays working while the words get rewritten.

- [Personal site — midya.ca](projects/midya-ca.md), [Kurdistan International Sociological Association website](projects/kurdistansociology-website.md)

## A marginal is not a path

A per-position summary and a whole-path answer are different questions, and
one cannot stand in for the other. ChainLab's exact counterexample makes the
gap visible: on a single observation, the most probable state at each position
is A/A — but that pair uses a transition the model says is impossible, so the
string of per-position winners is not a path at all. The valid best path is
B/A. Multiplying the posterior rows as if the positions were independent
invents an answer the model never offered, and the error is silent: every
factor looks reasonable on its own.

The same discipline applies to the inputs. An impossible observation is
rejected, not quietly smoothed into plausibility; a transition or emission
row with no expected occupancy keeps its previous values and is reported,
not silently refilled. A tool that repairs its inputs without saying so is
reporting on a different model than the one it claims to run — and a summary
that hides which question it answered is doing the same. Name the question
each number answers, keep the invalid combination visible, and let the joint
answer be computed jointly.

- [ChainLab](projects/chainlab.md)

## A zero gradient is not a zero effect

A gradient answers one question: how does this output move when this input
moves a little, with everything else held fixed. GraphLab makes the boundary
of that question exact. In a two-layer graph convolution, a node's features
reach a target only within two hops — so a node beyond that range has exactly
zero gradient for the target's margin, and changing its features leaves the
margin untouched. But deleting an edge is not moving a feature: it changes
the graph itself, and the normalization is recomputed over the new degrees.
A node whose features cannot move the margin at all can still move it by
losing an edge, because the edge deletion changes what its neighbour's
features count for. The zero gradient was true and the zero effect was
false — they were answers to different questions, and the gradient never
claimed to answer the second one.

The same boundary runs the other way. A six-cycle and two disconnected
triangles, given identical constant features, give identical predictions
from this model at every node — the model cannot see structure its inputs
do not encode, and no amount of gradient inspection will find a difference
that is not in the inputs. An explanation method reports what the model
used; it cannot report what the model was never given. State which question
each number answers — feature sensitivity, or structural sensitivity, or
neither — and do not let a clean zero in one column stand in for a zero in
the other.

- [GraphLab](projects/graphlab.md)

## Choose the metric the failure cannot pass

DiffuseLab keeps a deliberately collapsed generator around as a test: it puts every sample near a center, so it passes the center-distance metric — and still fails. It fails coverage, and the symmetric nearest-neighbor distance, which compares samples to references and references to samples, exposes it. A one-sided score can be satisfied by collapsing onto the part of the answer that is easiest to reach. The metric that catches the failure is the one the failure cannot pass: coverage alongside distance, the reverse direction alongside the forward one.

The same choice runs the other way when a shortcut looks like a win. Eight-step DDIM sampling saves 87.5% of the predictor calls and even raises the near-center fraction slightly — but its symmetric distance is worse than the full DDPM run, so the saving is real and the quality is worse, and which of those two facts gets reported decides which story the reader hears. Pick the metric before looking at the result, ask what a broken model would have to do to pass it, and report the side the shortcut does not improve.

- [DiffuseLab](projects/diffuselab.md)

## Audit each term of a sum, not just the total

A quantity that is a sum of independently meaningful terms should be
checked term by term, because a test that only checks the total can pass
while one term is wrong and fail without saying which term broke.
FlowLab's input score is such a sum: the normal-base pullback, which
carries the latent score back through the inverse Jacobian, plus the
log-Jacobian gradient, which accounts for how the flow stretches volume.
Each component is audited separately against independent finite
differences, so a missing volume term is caught as a missing component,
not as a vague error in the total — and a version that drops it still
returns a plausible-looking vector of the right shape, which is exactly
why the total alone cannot be trusted to catch it.

The same trap holds wherever a total is assembled from parts: two errors
can cancel and leave a matching total, and a mismatching total cannot say
where to look. Name the terms, give each one its own reference, and let
the audit point at the term that is wrong. A check that only ever sees
the sum is a check that can only ever say "something, somewhere" — and
that is not a diagnosis.

- [FlowLab](projects/flowlab.md)

## Make the fast path prove it equals the slow path

A faster way to get an answer is only an optimization if it returns the same answer. A shortcut that changes the result is not a speedup, it is a different program wearing the old one's name — and the difference is silent, because the output still has the right shape. The burden of proof is on the fast path: prove equivalence first, then count the savings.

KVLens runs KV-cached decoding beside full recompute, and both paths run the same operations in the same order, so their logits are identical by construction. The equivalence is still checked, not assumed: an equivalence sweep compares the two paths across model configurations and prefix lengths, and greedy generations are checked token for token. SpecLab does the same for speculative decoding — its greedy construction emits only tokens the target greedily confirms or chooses itself, so it equals target-only decoding by invariant, and the implementation is verified against that invariant across draft and target configurations, generation lengths and block sizes. In both cases the savings are counted honestly: KVLens counts actual arithmetic operations instead of quoting asymptotic complexity, and SpecLab reports the modeled round saving alongside the real sequential scoring work, so a saving that costs more work than it avoids cannot hide behind the flattering number.

A shortcut measured only in the metric that flatters it is a claim, not a result. Make the fast path prove it equals the slow path — by construction where possible, by swept verification where not — and report the cost the fast path adds in the same breath as the cost it removes.

- [KVLens](projects/kvlens.md), [SpecLab](projects/speclab.md)

## Agreement between two approximations is not evidence

Two methods can agree and both be wrong, when they share the same blind spot. FlowLab's conditional slices are evaluated on a grid, and refining the grid is a natural check — but a peak narrower than the grid spacing falls between the points of every grid, coarse or fine. The demo proves it with an adversarial integrand: a narrow peak on a flat floor, where two grids of different resolutions both miss the peak entirely and report the same wrong integral and the same wrong mean. Their agreement is perfect and worthless, because both grids are blind in exactly the same place.

Refinement only tests sensitivity to the refinement — it cannot see what no grid in the family can see. The miss is caught only by a reference that does not share the method: an analytic formula for the same integral, which puts the peak back. That is the rule: a check must be independent of the thing it checks. Two runs of the same approximation are one run with extra steps, and agreement between them is a property of the method, not of the answer. When the stakes are accuracy, bring a second way of knowing — a different derivation, a closed form, a brute-force enumeration — and let the two disagree in the open.

- [FlowLab](projects/flowlab.md)

## A guarantee is a contract with its assumption

A guarantee that depends on an assumption is only as strong as the assumption. SetGuard's prediction sets carry a finite-sample coverage guarantee — but the guarantee is a contract with exchangeability: it holds while the calibration rows and the rows being predicted come from the same design. The demo meets its target under that contract, then deliberately breaks it: a shifted arm keeps the identical test probability rows and moves the truth to the least-probable class, and coverage collapses — a boundary example of what breaking exchangeability costs, not a measured rate of drift in the wild. The method does not fail loudly when the contract breaks; it still returns sets of the same shape, with the guarantee quietly void.

That is the rule: a guarantee is not a property of the code, it is a property of the code plus the conditions it was proved under. The assumption belongs in the report next to the number it protects, and the cost of breaking it belongs there too — shown as a deliberate counterexample, not left for a user to discover in production. A claim that survives only while its assumption holds is not a lie, but it is not the whole truth either, and the difference is exactly what the counterexample is for.

- [SetGuard](projects/setguard.md)

## A mean is not the distribution

A summary that keeps the average and drops the spread is not a compressed version of the distribution — it is a different object wearing the distribution's name. TransportLab's pushforward keeps every weighted interpolation atom, so the full representation preserves the actual endpoint marginals; the barycentric mean map keeps one conditional mean per source instead, and those means preserve the mean while collapsing the variance. The gap between the two is not noise or rounding: it is exactly the within-source covariance, the finite law of total covariance, and it grows with the interpolation — an arithmetic identity, not evidence for or against any matching, geometry or alignment.

The same discipline applies to the refusal around it: the push command solves first and refuses a plan that has not converged, directing the caller back to the residuals instead of silently returning a plausible-looking result. A mean that hides the spread and a result that hides its nonconvergence fail the same way — both hand over a shape that looks like an answer while quietly dropping the part that would change the decision. Report the whole object, or say plainly which part you dropped.

- [TransportLab](projects/transportlab.md)

## A repaired number needs its own audit

A raw objective computed from a plan with wrong marginals is not a feasible primal bound — it can sit below its own dual, which would read as a violated bound if the failure were hidden. TransportLab's audit keeps that raw result visible and returns a separate rounded plan with its own dual evaluation: rounding the plan into feasibility changes the plan, so the rounded objective gets its own signed gap, and the raw failure stays beside it, not overwritten. The gap itself stays signed, including negative roundoff — a displayed zero is a rounding artifact that happens to land on zero, not a proof of exact optimality.

The rule generalizes: any step that changes a number — rounding, renormalizing, clipping, filling a deficit — is a new computation, and the audit must run on the number that actually ships, not the one it was derived from. A repaired value that inherits the original's certificate is a certificate for a number nobody will ever see. Keep the failure, audit the repair, and let the signed gap say what it says.

- [TransportLab](projects/transportlab.md)

## A narrower window is a new distribution

Cutting a distribution down to a smaller interval and renormalizing does not give you a piece of the old distribution — it gives you a new distribution that happens to live on a smaller interval. FlowLab's window audit makes the point concrete: the same outer grid is reused, and the inner window takes a contiguous, index-aligned slice of it, so both curves come from the same sampled heights — and still the inner curve is not a crop of the outer one. It has a new normalizer and new quantiles, and the mass removed by narrowing is a fraction within the finite outer window, not a tail probability for the whole line; everything outside the outer window was never in the picture at all.

The trap is treating a conditional on a smaller window as if it were the same question with less data. It is a different question, with a different answer, and the difference is silent: the numbers still have the right shape, the medians still move by plausible amounts, and nothing in the output says the normalizer changed. Name the window next to the number it produced, and say what the window excludes — a fraction removed within a window is a fact about the window, not about the world outside it.

- [FlowLab](projects/flowlab.md)

## Acceptance is not exploration

A sampler that accepts almost every proposal has not necessarily explored anything. HamiltonLab's separated-mixture audit makes the point concrete: four chains run on a two-component target with the starts split evenly between the components, and every chain accepts nearly all of its proposals — yet not one chain ever crosses from one component to the other. The pooled summaries look healthy only because the starts were balanced, not because any chain mixed: the occupancy was induced by where the chains began, not learned by moving between modes. A chain that never visits a mode has no evidence about it, however precise its within-mode statistics are.

The check that catches it counts transitions inside each chain, never across concatenation boundaries — a switch is something one chain does, and pooling chains before counting manufactures mixing that never happened. Acceptance measures how smoothly a chain moves where it already is; exploration is whether it ever leaves. Judge each chain on its own crossings, and treat a pooled summary that looks right as a question — which chain actually went there — not as an answer.

- [HamiltonLab](projects/hamiltonlab.md)

## A proposal that returns home is not a move

A sampler can accept every proposal and still go nowhere, and the failure needs no separated modes at all. HamiltonLab's quadratic-resonance audit makes the point concrete: on a standard Gaussian with a particular step size, four leapfrog steps form an identity map in exact arithmetic — the trajectory returns to its starting position, so refreshing the momentum cannot help, because the motion itself closes the loop. The chain accepts every proposal because the proposal is, up to rounding error, the state it already has; the accepted states span almost nothing, and the sampler's apparent success is a property of the map, not of the exploration.

The checks that catch it measure movement, not acceptance: the span of accepted states within each chain and the mean squared accepted jump, computed within chains and never across starts. Two related traps sit beside it: a proposal map's moments are computed before Metropolis acceptance, so a proposal moment is not a moment of the accepted chain — and ignoring the accept step would change the target — and linear stability with a unit determinant says the map preserves volume, not that it moves anything. Judge a proposal by where its accepted states actually go, and treat a perfect acceptance rate as a question — what did the chain do with the proposals it accepted — not as evidence it went anywhere.

- [HamiltonLab](projects/hamiltonlab.md)

## A repair that cannot change the decision

Temperature scaling divides the logits by one positive scalar, and a positive scaling cannot change which class has the largest logit — so the repair changes the confidence numbers and nothing else. CalibrLab's one guarantee is exactly that: accuracy cannot move, and the suite asserts the drift is zero bit-for-bit. That makes the repair a different kind of change from one that touches decisions. A repair that cannot change what the system does needs no outcome evidence to be safe; its safety is provable from the form of the change itself. A repair that can change decisions needs the opposite standard — measured outcomes on data the repair never saw, because its effect cannot be read off its form.

The same discipline shows in what the project refuses to use. An oracle temperature fitted on the test split would give a better number, and it is computed and shown — but labeled unattainable, a reference that quantifies what the honest validation fit leaves on the table, never a target to fit against. And the repair is reported honestly where it falls short: one scalar cannot match a per-bin curve, so after scaling most bins skew the other way, under-confident instead of over. A repair whose safety is provable and whose limits are shown is trustworthy in a way a stronger-sounding repair is not: it says exactly what it changes, exactly what it cannot change, and exactly where it stops helping.

- [CalibrLab](projects/calibrlab.md)

## A cancelled mean is not exploration

An average that comes out at zero can mean the chain explored evenly — or it can mean the values cancelled each other out while nothing moved at all. HamiltonLab's finite-window audit makes the point concrete: under exact harmonic dynamics, at a duration where each step flips the sign of the position, the average of consecutive positions over an even window cancels exactly, while the average of the squared positions over the same window keeps its full variance — squaring removes the sign, and the random initial magnitude never averages away. The signed average reports perfect stillness; the magnitude average reports a chain frozen at whatever size it started with. Both are correct about their own average, and neither alone says whether the chain explored.

The trap is reading a single summary as a verdict on mixing. Negative correlation can help one observable and hurt another, so a diagnostic that watches only the signed mean can report stillness as success while the magnitude stays stuck. The check that catches it pairs the signed average with a magnitude average — the mean of the positions and the mean of their squares — and asks both, because a chain whose mean cancels while its magnitude stays stuck has not mixed, whatever the first number says. The audit itself is scoped honestly: it evaluates variances under a hypothetical stationary exact-flow kernel, not the recorded chains, so it is a statement about what a finite window can and cannot show, not a claim about any chain that was actually run. Judge a window by more than one average, and treat a zero in any single one as a question — what did the magnitude do — not as evidence the chain went anywhere.

- [HamiltonLab](projects/hamiltonlab.md)

## Zero correlation is not independence

A correlation of zero between an observable and its own lags says nothing about the next observable. HamiltonLab's random-duration audit makes the point concrete: in the first schedule, independent choices between a sign flip and the identity make every nonzero-lag position correlation zero — yet the magnitude never changes at all, and the variance of the mean of the squared positions sits far above the value independent draws would give. A second schedule shows the same gap in milder form: the position correlation is near zero while the squared positions stay correlated. The positions look uncorrelated while the magnitudes stay stuck, because squaring removes the sign that the correlation was measuring.

The derivation keeps the two observables on separate tracks for exactly this reason. The conditional mean of the next position is one coefficient times the current position, and the conditional mean of the next squared position — measured from its stationary mean — is a different coefficient times the current squared position measured the same way, each derived by conditioning on one state-independent branch at a time. Using the first coefficient squared in place of the second would silently give the wrong uncertainty for the squared observable — the two numbers answer different questions, and no algebra turns one into the other. The audit is scoped honestly, too: these are specified analytic kernels, not a controlled efficiency comparison and not a claim that random lengths fix mixing, and neither one is the project's leapfrog random-length sampler. A diagnostic that watches only the first observable can report a chain as mixed while the second stays frozen, so ask the magnitude what it did, not just the signed position — and treat a zero correlation as a statement about the observable it was computed on, nothing more.

- [HamiltonLab](projects/hamiltonlab.md)

## The reference is part of the question

An attribution is not a property of a model alone. It is a property of a
model, a point, and a reference — and changing the reference changes the
question while the model and the point stay exactly the same. ShapleyLab
makes the point concrete: on a product scorer, the same point gets one
attribution against a zero background and a different attribution against a
background whose first two coordinates are one, while the prediction itself
does not move at all and only the baseline shifts. Neither answer is wrong;
they answer different questions, and reporting the numbers without naming
the background is reporting an answer without its question.

The same holds for the checks that are supposed to certify an attribution.
A diagonal background with a diagonal target gives zero attribution and a
zero efficiency residual — every internal check passes — while the singleton
hybrids the calculation leans on sit entirely off the observed manifold.
Additivity held and validity did not follow, because the game was defined
on combinations the data never shows. Grouping features changes the game
again: treating a correlated block as one atomic player gives a different
split than adding up the individual values after the fact, and no arithmetic
on the individual numbers can recover the grouped answer, because the
grouped game never asks the individual question.

An explanation method reports what its stated game says, and the game is a
choice — which background, which partition, which combinations are allowed
to exist. State the choice alongside the numbers, and distrust any
attribution whose reference was never written down: a clean residual proves
the arithmetic closed, not that the question was the right one.

- [ShapleyLab](projects/shapleylab.md)

## A figure is a claim about its data

A figure is not decoration for a result; it is a claim about the data behind it, and it should be checked the way a number is checked. HamiltonLab's observable-window figure makes the point concrete: a deterministic renderer evaluates the analytic reference directly, and continuous integration regenerates the committed figure and checks it byte for byte — the picture in the repository is the output of the code in the repository, not a screenshot taken once and left to drift. Every rendered vertex is checked against the data it is supposed to draw, so a wrong point cannot hide behind a plausible-looking curve.

The figure also shows everything it claims to show. Every integer window length is drawn, with no thinning, no clipping, no fitted smoothing and no silent replacement of zeros — the curve is the full set of summaries, not a selection of them. The panels share linear axes, and each observable is normalized by its own stationary variance, so panels can be compared without one scale swallowing the other. And the scope is written on the figure itself: the lines join window-length summaries, not a sampled trajectory, and the figure shows no empirical chains and proves nothing about mixing. A figure that can be regenerated, that draws all of its data, and that states what it is not is evidence; a figure that cannot is only a picture.

- [HamiltonLab](projects/hamiltonlab.md)

## A conditioned prior must be renormalized

A prior that is conditioned on admissibility is a different prior, and its evidence must be computed under the conditioned version, not the original one. SegmentLab's partition prior starts as independent Bernoulli cuts on the interior gaps, then conditions on every segment meeting the minimum length and the total staying under the maximum count. Conditioning removes mass, so the reported data evidence divides by the admissibility mass — the share of the unconstrained prior that survives the constraints. Without that division the number would be an unnormalized score wearing a marginal likelihood's name: it would rank partitions by a quantity that no longer sums to anything.

The same bookkeeping applies to the count posterior. The number of admissible partitions differs by segment count, so the posterior over counts counts them rather than treating every count as equally likely before seeing the data. And renormalization fixes the arithmetic, not the assumption: a confident posterior is still conditional on the settings supplied. The same observed sequence that recovers the true cuts under one supplied noise confidently isolates a single outlier as its own segment under a lower one — the evidence is exact given the model, and the model is still a choice.

- [SegmentLab](projects/segmentlab.md)

## Marginal peaks are not a joint partition

SegmentLab reports two different objects that look interchangeable and are not: the complete MAP partition from a max-product recurrence, and the per-gap marginal probability that a cut sits at each gap. The MAP is one joint partition; the marginals are averages over every admissible partition. The highest marginal at each gap need not agree with the MAP's cuts, and stringing the per-gap winners together need not give an admissible partition at all — the length and count constraints bind whole partitions, not individual gaps, so a stitched-together set of winners can violate them.

Keeping both is what makes the uncertainty visible instead of hidden. The fixture's MAP recovers the true cuts while a third marginal peak elsewhere carries real probability, so showing only the MAP would pretend the posterior is more settled than it is. The same split applies to the pointwise latent means, which average over every interval covering each point rather than reporting the MAP's segment means alone. A joint answer and a set of marginals answer different questions; report the one you actually computed, and do not let one stand in for the other.

- [SegmentLab](projects/segmentlab.md)

## A held-out label is not a held-out node

GraphLab's evaluation is transductive: the test nodes' labels are masked — passed as None, never entering the training gradient — yet the test nodes themselves are never hidden. Their features and their edges stay visible and shape every message-passing step, because the graph is the input the model learns on. Masking the answer is not the same as hiding the question: a split that withholds labels while leaving the graph intact measures performance on nodes the model has already seen in every way except the one field being predicted.

Calling that unseen-node or unseen-graph generalization would overclaim what was measured, and the case study says so plainly — it is transductive node evaluation on one graph, not unseen-graph, unseen-node, or temporal generalization. The honest statement names exactly what was held out, labels only, and what was not: features, edges, and the graph they form. Whenever a split is described, say which parts of each example were actually withheld, because a model can learn a great deal from the parts left in view.

- [GraphLab](projects/graphlab.md)

## Differentiate the computation you ran, not the optimum you wish you had

TransportLab's sensitivity command propagates analytic derivatives through a fixed number of log-scaling updates — the computation that actually ran — and never through an adaptive stopping rule, because there is no stopping rule to differentiate: the update count is fixed up front. It is a hand-derived directional computation, not automatic differentiation, not an implicit-optimum gradient, and not a derivative through rounding.

The envelope shortcut is the tempting alternative: differentiate the optimum as if the computation had already arrived there, keeping only the terms that would survive at a stationary point. On a short, unconverged run the shortcut disagrees with the full derivative while the residuals are still plainly visible; on a long run the two agree. That agreement is earned by the run, not assumed by the shortcut — a stationary, feasible optimum may justify an envelope derivative, and a finite, non-feasible computation does not gain that justification from a small-looking objective. Differentiate the steps you took; the shortcut is only honest once the computation has earned the right to be treated as an optimum.

- [TransportLab](projects/transportlab.md)

## Zero visits is not zero mass

A sample that never visits an outcome is not evidence that the outcome has probability zero — it is evidence about the sample. SegmentLab's fixed seed-19 audit draws 10,000 joint posterior partitions, and the four-segment partition is visited by none of them, yet its exact posterior mass is 0.000115427: the exact inference retains the positive mass, the committed figure writes it in text because its bar is too short to inspect at normal size, and the audit keeps the exact probability beside the zero frequency instead of letting the sample overwrite it. Sampling cannot replace the exact rare-event probabilities, and a zero in a frequency table is a property of the draws, not of the posterior.

The same discipline is why the figure shows whole draws instead of only the average: its first panel draws the first three complete latent-mean paths in generation order, as steps at their segment boundaries, beside the exact pointwise mean — because a pointwise posterior average is not itself a sampled partition, and no single sampled path looks like the mean. Report the exact value where you have it, show whole samples where you do not, and never let a zero count stand in for a zero probability.

- [SegmentLab](projects/segmentlab.md)

## Two possible cuts can be jointly impossible

Two cuts can each be possible on their own and still never occur together — and multiplying their marginals invents an event the model forbids. SegmentLab's exact joint cut queries ask whether both cuts occur, allowing any other admissible cuts, by rerunning the constrained recurrence over only the partitions that contain both gaps. On the committed six-zero fixture, capped at two segments, each cut at 2 or 4 has posterior marginal .011658220257, so the independence product is .000135914100 — but both cuts together would need at least three segments, so their exact joint probability is 0, structurally impossible, and the conditional P(cut4 given cut2) is 0 rather than undefined, because cut2 itself is possible. A second fixture shows the milder form of the same error: the exact joint .005542191566 against a marginal product of .016465692251, with the conditional .088361267381 against a marginal of .262518792097. The audit keeps impossibility distinct from underflow: conditioning on an impossible event returns null, not 0, while a possible event can exponentiate to 0 and still keep its finite log mass. A marginal is a summary of one gap; the joint question has to be asked jointly, and the answer can be zero even when every factor is positive.

- [SegmentLab](projects/segmentlab.md)

## A sum of marginal entropies is not the joint entropy

Adding up the entropy of each cut's marginal tells you how uncertain each gap looks on its own — and it overstates the uncertainty of the partition by exactly the dependence between the gaps. SegmentLab's `partition_information` returns the discrete entropy of the complete partition alongside every binary marginal cut entropy, their sum, and the sum's gap above the joint entropy: that gap is the total correlation of the whole cut-inclusion vector, the KL of its joint distribution to the product of its binary marginals — not a sum of pairwise correlations, and zero pairwise dependence would not establish full independence. On the committed six-zero fixture, capped at two segments, the full posterior entropy is .338772920 nats against a marginal entropy sum of .340428836, a total correlation of .001655915: count constraints create dependence even when all observations agree. The marginal sum is a comparison, never the reported entropy.

The same audit keeps the other direction honest: the four-point fixture has posterior entropy 1.029013408, above its conditioned prior entropy of .836308115, yet the KL from posterior to conditioned prior is still positive at .166962288 — an observation can increase entropy, and KL is not prior entropy minus posterior entropy. And the outlier fixture shows the trap from the other side: the low-noise fit has lower entropy and a much larger KL (6.894031384) yet confidently isolates contamination at cuts 12/13, while the high-noise fit's MAP has no cuts at all. Neither lower entropy nor higher information proves the model right. Report the joint quantity, keep the marginal sum as a comparison, and never let a smaller entropy stand in for a better answer.

- [SegmentLab](projects/segmentlab.md)

## The most probable partition is not the cheapest decision

The most probable partition and the least costly decision are answers to different questions, and on the same data they can disagree. SegmentLab's `decide` command minimizes expected false/missed boundary loss under supplied relative costs, while the MAP partition maximizes posterior probability — and on the committed seven-point decision fixture the two part ways: the no-cut decision carries the lower expected boundary risk, .680000591, while the MAP partition is a single cut at position 3, with higher risk, .869071786. Neither number is observed accuracy, and the costs are supplied loss units, not money: the comparison is only meaningful because both answers are computed under the same constrained prior and the same loss. The case study keeps MAP and infeasible-threshold comparisons separate for the same reason — a threshold that cannot be met is not a decision, and a probable partition is not a cheap one. Report the decision rule alongside the estimate, and never let the most probable answer stand in for the least costly one.

- [SegmentLab](projects/segmentlab.md)

## One scale for a whole matrix is a claim about every row

A single scale for a whole matrix is set by its largest entry, so every other row inherits a resolution chosen for someone else. QuantLab's symmetric int8 quantization uses scale = absmax/127 per tensor or per channel, and the controlled magnitude study shows what that choice costs: boost one matrix row by a factor of 100 and per-tensor's single scale crushes the rest — small-row SNR 9.25 dB — while per-channel scales hold 48.39 dB, a measured gain of 39.14 dB. The headline numbers would never have shown it: per-channel int8 matches fp32 test accuracy exactly on the fixture (0.9833 against 0.9833, a measured drop of 0.0000) at 3.3103x smaller storage (768 B to 232 B for binary32 row scales). An average error rate is not a location; the aggregate can pass while one part of the model is destroyed. The study is post-training only, with int8 codes now stored in real QLB1 files with IEEE scales — the claim is about where the error concentrates, not about production deployment. When a method shares one parameter across unlike parts, audit the parts separately: the case for per-channel scales is the located error, not the average.

- [QuantLab](projects/quantlab.md)

## Two metrics can disagree, and the choice is the claim

Two metrics can disagree on the same model, and whichever one selects the model is doing the claiming. BoostLab's development fixture makes the split concrete: the selected stumps keep round zero — test accuracy .4980, logloss .7060 — while their unselected 80-round checkpoint reaches accuracy .6367 with worse logloss .7366. Accuracy improved and the probability ranking got worse at the same time, so selecting on accuracy alone would have kept a model that is less honest about its own confidence. The selection rule is explicit about this: validation logloss chooses the earliest prefix improving by over 1e-12, patience stops after that many rounds without a qualifying improvement, and changing the validation labels can change the chosen prefix but never the fitted prefix itself. The scope stays descriptive — the Newton arm's .900390625/.3341242425 at round 35 against the depth-2 control's .8906/.3400 does not isolate a causal curvature or regularization benefit, and the fixture is development data already seen. Report both numbers, name the metric that selected the model, and never let one score stand in for the other.

- [BoostLab](projects/boostlab.md)

## A p-value cannot be smaller than its own resolution

A permutation p-value is a count over allocations, so its smallest reportable value is set by how many allocations exist — no test can return a smaller number than its own resolution. DriftLens's Monte Carlo mode samples allocations uniformly with replacement under a seeded RNG and uses the +1 formula, not a zero-capable tail fraction, so with B499 the floor is 1/500 = .002; the seed-13 shifted demo sits exactly on it, with MMD squared .63453882456 and p .002 against the same-generator arm's -0.00487090068 and p .55 (30x4 standard-normal samples, shifted arm adding 2 to each coordinate, bandwidth 2, alpha .05). The tiny 2-vs-2 separated fixture makes the same point in exact mode: only six allocations exist, so even perfect separation reports p 1/3 — low resolution, not weak evidence. The Holm family shows correction cannot manufacture resolution the test never had: bandwidths [1,2,4] each carry raw p .002 and Holm p .006, while the tiny exact example's raw p 1/3 tested at alpha .4 across two kernels does not reject after Holm, even though both raw p-values pass. These are selected development fixtures, not a power or type-I error study, and they say nothing about deployment drift detection — but they do say to read the resolution before the p-value, because a number at the floor is a statement about the test, not about the data.

- [DriftLens](projects/driftlens.md)

## A gain needs a control that could have produced it

A measured improvement is only as informative as the controls that could have produced it for the wrong reason. DistillLab's checked-in fixture holds seeds, capacity, learning rate and epoch budget fixed and varies only the targets: the distilled student reaches test accuracy 0.7469 against 0.6813 for direct training on one-hot labels — a +0.0656 gain with the teacher at 0.8344 — but the decomposition is what earns the claim. Training on the teacher's argmax predictions alone, with no distribution content, already gains +0.0281; soft targets add a further +0.0375 over pseudo-labels. Uniform label smoothing, which softens targets without any input-specific teacher signal, scores 0.6781, at or below direct — so softness alone is not the mechanism. And a permuted-target control, the same teacher soft-target vectors attached to different inputs, sits at exactly chance, 0.1250 on eight classes, showing the gain rides on input-specific signal. The mechanism is visible in the overfit gap too: the direct student memorizes its 80 training samples (train 1.0000, gap 0.3187) while the distilled student does not (train 0.8000, gap 0.0531), and KL(teacher || student) falls from 1.0932 to 0.9563. The scope stays honest: soft-versus-argmax also changes target confidence and the optimization problem, so the split does not isolate dark knowledge as the cause, and temperature helps only modestly here (T=1 already reaches 0.7219; T=4 adds +0.0250). Report the gain with the controls that could have explained it away, or the number is just a comparison.

- [DistillLab](projects/distilllab.md)

## A safeguard that never fires is not evidence it works

A safeguard earns its place on a fixture where the failure it guards against can actually happen, not on one where the failure never shows up. MoeLab's mixture-of-experts routes four well-separated input regimes to four linear experts with a Switch-style top-1 gate, and on its checked-in fixture the routing is exact — purity 1.0000, usage shares exactly [0.25, 0.25, 0.25, 0.25], test MSE 0.0303 against a dense MLP's 0.1853 at slightly more parameters (136 against 145). The load-balancing auxiliary loss exists to stop expert collapse, but collapse never happens here: the maximum expert share is 0.25 with the term and 0.25 without it, and dropping the term fits slightly better (0.0015 against 0.0303). The fixture is symmetric by construction, so it is the wrong place to justify the term — the standard motivation, imbalanced expert traffic in production serving, is untested here. The same fixture shows the objective is sparse, not an ensemble: evaluating with soft averaged experts costs 0.6291 against the sparse 0.0303. The scope stays narrow — linear experts and router, top-1 straight-through gradients finite-difference verified, 39 Python tests and five Node/actual-Chrome tests, synthetic data — but the lesson travels: report a safeguard with the failure rate it actually prevented, or a term that never binds is just a term that never got tested.

- [MoeLab](projects/moelab.md)

## Show the bill with the gain

AlignLab's alignment result is reported as a pair, not a single number: the policy's true latent utility rises from 2.0375 to 4.5704, and the KL paid to the reference policy is 1.0750. The KL term is what keeps the policy from collapsing onto the single highest-reward style — without it, the beta=0 ablation puts all the mass on one style, entropy 0.0407 against 0.7167 with the term, and pays more KL, 1.7510 against 1.0750, for the privilege. Reporting the reward alone would hide that the gain was bought by moving away from the reference, and the price is the number that tells you whether the move was cheap or ruinous. The same discipline shows up in the reward model: holdout accuracy 0.7800 on 150 fresh pairs, with the CI gate pinned at an achievable 0.75 because the labels are sigmoid-noisy and even the Bayes-optimal ranker falls short of 1.0 — a gate set at perfection would fail the best honest run. The suite is 47 Python tests, including all 15 original tests unchanged, fully offline, with CI across Python 3.10–3.13. A result that shows what it cost is a result you can price; one that shows only the gain is an advertisement.

- [AlignLab](projects/alignlab.md)

## Measure the side you did not optimize

A trade-off has as many sides as the method touches, and reporting only the ones it improves is a selection effect, not a result. LoRALab's low-rank adaptation reports three numbers for every configuration because any two alone flatter it: accuracy on the shifted distribution, trainable-parameter share, and retention on the original distribution. On the checked-in fixture the base classifier collapses from 1.0000 on distribution A to 0.4444 on the disjoint-vocabulary distribution B, and a rank-2 adapter recovers to 1.0000 on B while training 67.7% of the parameters (262 against 387) — the headline. The third number is the one the method did not optimize: retention on A is 0.7556 for the adapter against 0.9556 for full fine-tuning, and rank-1 is worse still (0.9333 on B, 0.7333 retention, 33.9% of parameters), while rank-4 and rank-8 buy no more accuracy and cost 135.4% and 270.8% of the parameters. The same discipline applies to the merge: the algebra `(W + B @ A) x = W x + B (A x)` is exact, but the floating-point association is not, so the suite measures the max abs logit diff at ~1e-14 and pins it below 1e-12 — and pins that it is nonzero, because a test that asserts zero would be asserting a falsehood. The gates fail in both directions: `--min-base-drop 0.3` keeps the shift honest, `--max-rank2-param-share 0.7` pins the cost, and an impossible `--max-rank2-param-share 0.5` fails, as it should. The scope stays narrow — a linear classifier, not a transformer, 14 unit tests, fully offline, CI across Python 3.10–3.13 — but the lesson travels: report the side you did not optimize, or the trade-off you measured is only the trade-off you liked.

- [LoRALab](projects/loralab.md)

## Label what the data cannot identify

PolicyLens evaluates a target policy from logged contextual-bandit data, and the estimate it returns is only as identified as its support. A target action with positive probability under the target policy and zero under the behavior policy at an observed context is not a zero-weight success — it is a row the data cannot speak about, so the tool labels it no-nonparametric-identification instead of folding it silently into the average, and the numeric estimate stays diagnostic rather than an identified policy value. A logged action with zero behavior probability is rejected outright as inconsistent input, and tiny positive probabilities are flagged for the variance they can create even without a support violation. The same labeling discipline applies to the estimator's own knobs: clipping at 1 moves IPS from 0.78 to 0.185, SNIPS to 0.6166667 and DR to 0.535 while ESS rises 4.9231 to 8.4706 — a different estimand, explicitly labeled, not a quieter version of the same number. On the constructed two-context demo with known target value 0.78, IPS, SNIPS and DR all recover 0.78 against a wrong direct estimate of 0.5, and on a 2000-row seed-13 Bernoulli log with oracle q, DR gives 0.7532475 — close to, not equal to, population truth. The optional crossfit helper fits held-out categorical reward means (five folds, seed 17, fixed prior: direct 0.7496455, DR 0.7509088) and reports itself as not closer to truth than the oracle arm, with row-iid splits that do not protect clustered or time-ordered data. The scope stays narrow — standard IPS/SNIPS/DM/DR only, 28 unit tests, fully offline, CI across Python 3.10–3.13, no confidence bounds and no deploy decision — but the lesson travels: when the data cannot identify the answer, label the gap; a number that hides it is worse than no number at all.

- [PolicyLens](projects/policylens.md)

## Pin the baseline, not just the result

A comparison is only as honest as the baseline it is measured against, and a baseline that is allowed to drift is a comparison that can silently disappear. StructGate's grammar-constrained generation produces valid JSON on 40 of 40 seeded draws and schema-conforming records on 40 of 40, against an unconstrained control that manages 3 of 40 — but the control is not just reported, it is gated from above (`--max-unconstrained-rate`), so a fixture change that made the control pass would fail the suite instead of quietly erasing the contrast the numbers depend on. The same discipline applies to the guarantee itself: masking renormalizes the distribution to the legal token set, and the cost is measured in the same units as the guarantee — -ln(Z) per step is exactly KL(p || p_masked), 1.3496 nats per step for the grammar mask and 0.8209 for the schema mask — so the price of conformance is a number, not an adjective. The validator earns its trust the same way, matching Python's json module on 32 adversarial cases with snapshot and restore for exact queries, and the demo runs fully offline asserting both sides of every gate. The scope stays narrow — an order-3 character n-gram that is exact by design rather than fluent, flat closed records with three slot types, 33 unit tests, CI across Python 3.10–3.13 — but the lesson travels: pin the baseline with a gate, or the day the fixture changes, the comparison you published stops meaning what it meant.

- [StructGate](projects/structgate.md)

## A weight is a measurement on a task, not an explanation

Attention weights get quoted as if they were explanations, but a weight is a number the model produced on one task under one configuration, and quoting it without the task is quoting a measurement without its instrument. AttnLens trains causal multi-head self-attention from scratch in pure Python on a recall task designed so the mechanism is visible: each sequence hides one key after a marker at a varying position and asks for it at the end, and one layer cannot solve it cleanly — the key token's own content does not say it followed a marker — while two layers can, so success and failure are both on the table and the gap between them is the demonstration. The head statistics are then measurements, not interpretations: per-head mean entropy, previous-token mass, and recall attention — the query position's weight on the key token — with the top head concentrating 0.80–0.91 of its weight on the key on the checked-in seed, and CI gates pinning the trained quality at 95% accuracy and 0.7 recall attention over 100 seeded epochs. The measurement apparatus is checked before the weights are quoted: every parameter group's hand-derived gradients are verified against finite differences to about 1e-11, and without global-norm gradient clipping the training was observed to diverge in the tested configurations, so the run that produced the weights is itself a guarded result. And the scope is written on the measurement: a two-layer model on a synthetic recall task, 46 unit tests, CI across Python 3.10–3.13 — what these heads learned is an observation consistent with induction-head behavior, not proof of the same circuit and not an explanation method for larger models. Quote the weight with the task that produced it, the gates that held it, and the check that verified the instrument — or do not quote it at all.

- [AttnLens](projects/attnlens.md)

## Effective sample size measures weights, not support

Effective sample size is a statement about how concentrated the weights are, not about how much of the state space the particles still cover — and a filter can report the first while having lost the second. ParticleLab's support-collapse fixture runs twenty zeros through a scalar filter with zero process noise, 32 particles and seed 0: with resampling on, weight ESS is a perfect 32, yet only one initial label is carried, the latent variance is 0 against an exact reference of .000499972224, and the mean sits at -.2163600684 against an exact 0 — the resampled set is copies of one badly placed ancestor. With resampling off, all 32 labels survive but the ESS is 1.00002950, nearly all the weight on one particle, and the latent variance is .00000308085 — keeping the labels is not the same as keeping the support either, because with zero process noise no method can create a state value that was never sampled. The same failure shows up without resampling at all: on the static square fixture an eight-particle run loses one sign of a symmetric distribution while carried ESS reads 8/8, and in a 64-step genealogy the filter ends with 32 distinct current states but a single retained initial path, so time-0 variance is 0 against an exact smoothed .009521314; 512 backward draws reach two initial indices and still report .022290238, over twice the exact value. The scope stays narrow — a scalar supplied-parameter model, 114 unit tests, development fixtures, no convergence certificate — but the lesson travels: report the carried labels and the retained paths next to the ESS, or a tidy score will certify a distribution that has already collapsed.

- [ParticleLab](projects/particlelab.md)

## Grounding is a check you run, not a property you claim

Retrieval-augmented generation is usually sold on the claim that the answer is grounded in what was retrieved, but a claim is not a check — RAGLine makes grounding a property you can run and gate on. The system builds the retrieval-and-verification loop itself instead of outsourcing every step that matters: documents are expanded from fixed templates by one seeded RNG and chunked into paragraph windows with stable ids, so a seed reproduces the corpus, the rankings and the answers bit for bit; retrieval scores token-hashed TF vectors with IDF weights by cosine similarity, with no model anywhere in the loop. Answering is deliberately extractive — the best-matching sentence from the top-k chunks becomes the answer, returned with its chunk id — because a copied sentence has a citation you can verify, and there is no generator to hide behind. The grounding check then scores the fraction of answer content tokens present in the cited chunk: correct citations pass at 100% overlap on the fixture, and the suite's negative control proves the check bites — corrupting the citation to an unrelated chunk makes it flag the answer. On a fixture evaluation over 8 questions with known topics, recall@3 is 1.00, MRR is 0.94 and the grounded-answer rate is 1.00, pinned by CI gates `--min-recall 1.0 --min-mrr 0.9 --min-grounded 1.0`, with an impossible gate failing as it should. The scope stays narrow — 31 unit tests, fully offline, CI across Python 3.10–3.13 — and the limits are stated on the check itself: it is lexical overlap, so it catches the tested wrong-citation cases and unsupported wording, not misreadings of a correctly cited source, and paraphrases sharing no content tokens will not match at all. The lesson travels: if the answer's support cannot be scored and gated, "grounded" is a word in the marketing copy, not a property of the system.

- [RAGLine](projects/ragline.md)

## Determinism is what makes a quality number testable

EmbedKit trains word embeddings from scratch with pure-Python skip-gram
with negative sampling, and the point of the exercise is not the vectors
— it is the evaluation loop that tells you whether the vectors learned
anything. The training is deterministic by construction: weight
initialization, epoch shuffling and negative draws all come from one
seeded RNG, so the same corpus and seed reproduce the same vectors bit
for bit. That is what makes a quality number a testable claim instead of
a one-off observation: with the vectors pinned, the suite can assert that
same-topic similarity beats cross-topic similarity and that neighbor
purity clears 90% on the checked-in corpus, and the CI gates
`--min-coherence` and `--min-margin` — the fraction of each word's k
nearest neighbors in its own topic cluster, and the margin between mean
intra-cluster and inter-cluster similarity — can be run on every change
instead of eyeballed once. The training itself is the classic Word2Vec
recipe, stated plainly: sigmoid-gradient SGD pushes each center vector
toward its context vector and away from k negatives drawn from a
unigram^0.75 distribution by binary search over a cumulative table, with
the dot product clamped for numerical stability. And the scope is stated
on the score: the demo corpus is three topics, well separated by
construction, so coherence 1.0 there shows the objective learns the
structure it is given, not that the method solves topic modeling — the
file names PPMI + SVD over a co-occurrence matrix as the classical
baseline for real text. The suite is 40 unit tests, fully offline, CI
across Python 3.10–3.13, covering tokenization, the Embeddings API,
negative sampling, training determinism, `min_count` filtering, parameter
validation, the trained-quality assertions, the coherence and separation
math including error cases, all three report formats, and the CLI end to
end including both sides of every gate. A quality gate you can re-run on
a deterministic pipeline is a check; the same number on a pipeline that
drifts run to run is a story.

- [EmbedKit](projects/embedkit.md)

## A plan has a cost before it has a result

An agent plan fails in boring, checkable ways — a step calls a tool that
does not exist, waits on an input nobody produces, or sits in a dependency
cycle — and the plans that look fine on paper still miss their budgets once
real tool latency, failures and retries are counted. PlanBench checks the
plan twice before anything runs: semantic validation beyond JSON shape
(duplicate step ids, unknown tools, unknown or self dependencies, cycles
by Kahn's algorithm, `requires` inputs that no dependency's tool
produces), with findings severity-ranked so structural blockers are high
and unproduced inputs are medium; and a deterministic parallel simulation,
a discrete-event simulator that starts each step as soon as its
dependencies succeed, in parallel where the DAG allows, with tool calls
failing independently at the tool's declared rate from a seeded RNG, so the
same plan, registry and seed always produce the same trace. Steps retry
within `max_retries`; when attempts are exhausted the step fails and its
dependents are skipped, visibly. The simulation then reports the
plan-shape metrics the budget depends on: makespan from the event trace,
total cost including retry cost, critical path by summed duration, and
parallelism as total work over critical path — how much concurrency the DAG
actually offers — and CI gates `--require-success`, `--max-makespan`,
`--max-cost` and `--max-findings` fail the pipeline when a plan stops
meeting policy. The scope is stated on the numbers: durations and failure
rates are declared in the fixtures, not learned from real executions, so
the simulation measures what a plan would do under those assumptions, not
real-world latency, and validation checks structure and producibility, not
whether a tool call would actually succeed. The suite is 29 unit tests,
fully offline, with a demo that simulates a research-agent plan with flaky
tools green (retries exercised, real concurrency asserted), rejects a
broken plan with findings, and exercises both sides of every gate, CI
across Python 3.10–3.13. A plan's budget is a property of its shape;
measure it before you pay for it.

- [PlanBench](projects/planbench.md)

## Hold the distribution fixed and vary only the strategy

Every language-model pipeline picks a decoding strategy — greedy,
sampling at some temperature, top-k, top-p, beam search — and most pick
by vibe, even though the choice changes output length, diversity and
degeneracy. DecodeLab makes the comparison honest by controlling
everything except the strategy: an add-k smoothed n-gram model whose
next-token probabilities come straight from corpus counts, so every
token has defined probability mass, unseen contexts included, and the
strategies decode against ground truth rather than against a black box.
Decoding itself is deterministic — greedy resolves ties by corpus
frequency then lexicographic order, beam search ranks by total log
probability with deterministic ordering, and samplers take an explicit
seed, so the same seed, corpus and text always produce the same output.
Quality is measured, not eyeballed: distinct-1 and distinct-2 for
diversity, repetition rate for immediate self-repeats, and unigram
entropy, computed per strategy and reported side by side in terminal,
JSON and Markdown, with CI gates `--min-distinct-2` and
`--max-repetition` failing the pipeline when a decoding change pushes
generation below policy. The scope is stated on the numbers: the n-gram
model is a stand-in that gives the strategies a real, exact distribution
to work against — it demonstrates decoding behaviour, not modern
language-model quality — and distinct-n and repetition rate catch
degenerate repetition, not factual correctness or coherence. The suite is
36 unit tests, fully offline, with a demo over a small AI-themed corpus
that asserts the greedy output exactly, asserts seeded sampling
reproducible, runs a five-strategy comparison with JSON and Markdown
reports, and exercises both sides of the quality gate, CI across Python
3.10–3.13. A decoding comparison is only a comparison when everything
else is held fixed.

- [DecodeLab](projects/decodelab.md)

## A wider beam is not guaranteed to be a better beam

Beam search feels like it should be monotone: keep more candidates alive and the result can only improve. DecodeLab shows it is not, under the beam semantics it documents, with complete witnesses rather than an anecdote. The staged sampling is fixed first — stable temperature scaling subtracts the largest log probability before division so no event underflows, and normalized top-k precedes normalized top-p, with every intermediate distribution, retained mass and cutoff-prefix mass returned. The normalization matters: for probabilities (0.6, 0.3, 0.1), temperature 0.5 and top-p 0.7, the old unnormalized powers sum to 0.46 and keep all three events, while normalization gives the first event 0.7826 mass, so it alone is the nucleus. Then the search is checked against an exhaustive oracle that uses exactly the same conditional log-probability objective, without a length penalty, over bounded complete continuation trees that return every EOS-terminated and cap-censored outcome with its filtered sampling probability, original-model log score, total/EOS/cap mass and expected generated length — the conditioned prompt is not scored and capped paths carry no invented EOS factor. On the first synthetic table the horizon-3 oracle is `b + EOS` at probability 0.3822: width 1 ends at the cap with `a a a`, log-score gap 1.7066336993, while widths 2 and 3 attain the oracle. On the second table the oracle is `a + EOS` at 0.1940719831: widths 1 and 3 attain it, but width 2 prunes it and finishes capped with `b b a`, log-score gap 0.6275452747. Full beam traces retain every expanded candidate, parent, emission and pruning decision, and finished paths remain in the shared finished/live beam, so the failure is inspectable step by step rather than asserted. A strict JSON table CLI and an editable browser inspector let readers change the transition weights, temperature, filters, prompt and cap and re-run the whole audit, with edits hiding stale results until recomputation. The scope stays narrow — 54 Python tests including all 36 unchanged originals, unshifted 90-digit Decimal powers against production log/exp, rational Cartesian path products and rational forward mass/expected-length propagation on 40 random tables, 32 full audits and 120 staged cases, 7,927 independent scalar-JavaScript numerical comparisons, actual Chrome inspection of 96 distribution views, 231 outcome rows and 956 candidate rows, Python 3.10–3.13 CI and an installed-wheel reproduction, nine original files byte-exact — but the lesson travels: when a search can prune the best future, do not rank widths by intuition; run the oracle and read the gap, because a wider beam is a bigger beam, not a better one. Both counterexamples are on original synthetic tables under the documented shared finished/live beam semantics — a search counterexample, not evidence about human writing quality. Distinct from 'Hold the distribution fixed and vary only the strategy', DecodeLab's first principle, which is about comparison design — here the distribution and the strategies are fixed and the question is what the search itself guarantees — and from 'Keep the exact answer next to the approximation', VectorLite's principle, which is about measuring an approximation's error against an exact baseline — here the oracle is the baseline too, but the claim is about the search pruning the best answer, not about how far an approximation sits from exact.

- [DecodeLab](projects/decodelab.md)

## Keep the exact answer next to the approximation

Vector search demos usually show an index returning results, not how
wrong those results are. An approximate nearest-neighbour index trades
recall for speed, and the size of that tradeoff depends on the data, the
seed and the configuration — without an exact baseline to compare
against, "approximate" is a promise nobody checked. VectorLite keeps
the exact answer standing next to the approximation and measures the
gap: brute-force exact kNN over every vector, cosine and L2, with
score-then-id tie-breaking so results are deterministic, O(n) per
query by design because it exists to be correct, not fast; and a
random-hyperplane LSH index in which each vector hashes to a bit
signature from seeded random hyperplanes, candidates are the vectors
sharing enough signature bits with the query and are rescored exactly
before ranking, so the same seed and data rebuild the identical index
bit for bit. Recall is a first-class metric, not an afterthought:
`benchmark` self-queries every vector through both indexes and reports
mean recall@k of the approximate index against the exact one, with
per-query detail in the JSON report, and a CI gate `--min-recall`
fails the pipeline when an approximation change — fewer bits, a
different seed, a lower sharing threshold — drops recall below policy,
so the tradeoff is enforced rather than documented. The scope is
stated on the numbers: the LSH approximates cosine similarity only
(the L2 metric is exact-search only), measured recall is a property of
the dataset, seed and configuration under test — evidence, not a
guarantee for other data — and both indexes are in-memory and
single-machine, a correctness-first reference and evaluation harness
rather than a production-scale index. The suite is 50 Python tests on 3.10–3.13, including all 31 original tests unchanged, fully offline, with a demo over a clustered 12-vector dataset that runs an exact query, benchmarks self-inclusive mean recall@3 at 1.0, and exercises both sides of the gate. An approximation is only a claim until the exact answer is standing next to it.

- [VectorLite](projects/vectorlite.md)

## A clipped attack cannot prove robustness

RobustLab's box audit solves the ball intersected with the box, and does not adapt the answer from the ball alone: when a threat set gains per-coordinate bounds, the worst case inside the intersection is a new optimization problem, not the old optimum pushed back inside. Clipping the all-real attack to the box is the tempting shortcut — take the perturbation that was optimal without bounds and clamp each coordinate — but a clipped candidate is only a feasible point, and a feasible point with a positive margin proves nothing about the minimum. The audit returns the exact rational movement that attains the minimum plus a matching dual gain bound, so the claim is witnessed from both sides instead of asserted from one.

A dyadic fixture makes the gap concrete: weights (4,1), bias -1/4, point (1/16,3/4), positive label, unit box, L1 radius 5/8. Clipping the old all-real attack leaves margin +1/2, a comfortable-looking pass; the actual minimum is -1/16, attained by movements (-1/16,-9/16), with exact primal and dual gains both equal to 13/16 and zero gap — the model is not robust at this radius, and the clipped candidate would have said otherwise. The L1 problem is bounded fractional knapsack; L-infinity separates by coordinate, where independent adverse-direction clipping is optimal — so the shortcut is sometimes right, which is exactly why it cannot be trusted without the check. Whenever a constraint is added to a problem, re-solve the constrained problem; an answer carried over from the unconstrained one is a guess wearing the old answer's confidence.

- [RobustLab](projects/robustlab.md)

## Keep the recipe with the artifact

A tokenizer usually arrives as a finished artifact: a vocabulary file produced by a training run nobody can reproduce, so when token ids drift between pipelines or a cached vocabulary goes stale, there is nothing to check against — "why is this word three tokens?" becomes guesswork. TokenForge keeps the recipe with the artifact: training is deterministic, exact adjacent-pair counts over pre-token sequences with ties broken on the pair itself, and the merges are persisted as plain JSON that can be diffed, reviewed, and rebuilt byte for byte. Rank-ordered encoding applies the same merges lowest-rank-first, so the token stream at encode time is identical to the one training produced.

The point is not the format but the property it buys: an artifact whose construction is recorded can be audited, and one whose construction is lost can only be trusted. The compression statistics are reported the same way, with a gate that fails CI when a tokenizer regresses, so a change in the artifact shows up as a number rather than a silent drift. A vocabulary is a dependency like any other — if you cannot rebuild it from its recipe, you do not own it, you only rent it from the run that made it.

- [TokenForge](projects/tokenforge.md)

## A lexical check can catch a fabrication, not certify a truth

GroundCheck turns grounding into deterministic, offline lexical checks against the exact sources an answer claims to use: every `[n]` citation marker must resolve to a provided source, with unresolvable citations flagged as high-severity findings and the report showing how many of the provided sources were actually cited; each answer sentence is scored by content-token containment against every source document, stopwords removed, at document granularity so a sentence combining facts from several sentences of one passage is still supported by that passage; and every number in the answer must appear in the sources by exact or equal-value match, with decimal handling that keeps `1.57` one number rather than two sentence fragments. Three CI gates pin the result: `--min-support` on mean sentence support, `--max-unsupported` on unsupported sentence count, and `--max-findings` on total findings. A grounded answer passes every gate while an ungrounded one — a fabricated test count, a citation with no source, invented claims — is rejected, with JSON and Markdown reports asserted for both; 66 Python tests, retaining all 43 originals unchanged, cover tokenization, decimal-safe sentence splitting, number extraction and matching, citation parsing, source loading validation, support scoring including cross-sentence combinations, every finding kind, report escaping, and the CLI end to end including all three gates, with CI across Python 3.10–3.13.

The bound is stated in the same file as the check: these are useful fabrication signals, not semantic entailment, and they cannot establish that a claim is actually supported. The documented cases that pass every check prove it — negation ("does not contain 40 tests" scores supported, since containment ignores word order), wrong attribution (a number that belongs to one project assigned to another), and coincidental number matches (a figure appearing anywhere in the sources, even in an unrelated sentence) — and a fully paraphrased true sentence can score below the threshold. A mechanical check is a tripwire for ungrounded output, not proof of correctness: use it to catch what it can see, and never let a green gate stand in for the judgement it cannot make.

- [GroundCheck](projects/groundcheck.md)

## A strong association does not say what an intervention would do

CausalLab is exact finite structural-causal-model enumeration — categorical exogenous noise with topologically ordered deterministic truth tables — and it keeps observational, post-intervention and factual-evidence counterfactual queries separate, because the same observed joint can be produced by mechanisms that disagree about actions. A 100-world confounding fixture makes the reversal concrete: the observed conditional outcome probability rises from .42 to .68 with the action (+.26), while the supplied-model intervention difference is .60 to .50 (−.10); within each context the difference is −.10 in both (.90 to .80 where Z=0, .30 to .20 where Z=1), and backdoor adjustment using the supplied Z distribution matches intervention enumeration. Two two-world models share X=U with U~Bernoulli(.5) and an identical observed joint — half the mass at (0,0), half at (1,1) — yet with Y=X the probability Y=1 under do(X=1) is 1, and with Y=U it is .5; given factual X=0,Y=0, the probability Y would be 1 under X=1 is 1 versus 0, because factual evidence fixes U=0 and changing X does not redraw U.

The multi-world API abducts one factual noise posterior and evaluates named action scenarios jointly on every retained assignment instead of multiplying marginals. Stable (Y=U) and flip (Y=X xor U) models share a uniform observed joint and P(Y=1 | do(X=x))=.5 under either action, yet their (Y0,Y1) response joints are (.50, 0, 0, .50) versus (0, .50, .50, 0) while the naive product puts .25 everywhere — and factual X=0,Y=0 gives (0,0) for stable and (0,1) for flip. Sharp bounds replace choosing a coupling: with .50/.50 action marginals the helped and harmed fractions each range [0,.50] with mean effect .00, and with .25/.75 the helped fraction ranges [.50,.75], harmed [0,.25], mean effect +.50, each bound shipped with a joint witness that attains it, and explicit monotonicity rules out flip. The graph-only d-separation API agrees with an independent reference on 49,152 singleton/conditioning/surgery combinations and 7,040 disjoint set queries across all 64 four-node DAGs, and the bounded backdoor search checks every subset of 0..10 candidates — an independent reference agrees on 3,072 adjustment sets across 768 searches, and in the fixed A→X, A→C←B, B→Y, X→Y graph the empty set passes while adding C alone opens a collider and fails, so the search does not prune by assuming valid supersets. 138 tests, independent rational references including all 64 tiny Boolean mechanism pairs, five reproducible audit SVGs, CI on Python 3.10..3.13, standard library only. The bound is explicit: the graph, functional tables and noise distributions are supplied assumptions, not causes learned from observational data — no graph discovery, no automatic do-calculus identification, no continuous or cyclic models, and no empirical confidence intervals. An association is a fact about the data you have; what an intervention would do is a claim about the mechanism you assume — keep them in separate queries, or the first will quietly stand in for the second.

- [CausalLab](projects/causallab.md)

## Measure the retrieval before you blame the answer

When a RAG pipeline gives a bad answer, the generator takes the blame — but the answer can only use what retrieval surfaced, and retrieval changes are rarely measured. Adjust a chunk size, change the overlap, edit a source document, and the passages the pipeline retrieves shift silently; without golden queries and graded relevance judgments, the regression ships unnoticed and answers get worse for reasons nobody can see. RetrievalBench makes retrieval quality a reproducible CI gate instead of a vibes check: an exact Okapi BM25 index over a local JSONL corpus, with no pruning and no ANN approximation, so scores and rankings are fully deterministic and diffable between runs. Token-window chunking with configurable overlap keeps the index at passage granularity while chunk hits collapse back to their parent document, so qrels stay at document granularity. Per-query and macro-averaged recall@k, precision@k, MRR and nDCG@k are scored against graded qrels, with the weakest queries surfaced for review, and four gates — `--min-recall`, `--min-precision`, `--min-mrr`, `--min-ndcg` — fail CI when a retrieval change drops quality. JSON reports feed tooling, Markdown reports fit native CI job summaries, and an ad-hoc `search` command spot-checks the index. 68 Python tests on 3.10–3.13, including all 42 original tests unchanged, cover tokenization, BM25 edge cases (ties, empty documents, unknown terms, length normalization), JSONL loading validation, chunking windows and overlap, every metric, report escaping, and the CLI including gates and chunked evaluation; the offline demo runs against a small AI/ML corpus and asserts the aggregate metrics, the Markdown report, chunked-evaluation parent collapsing, and both sides of the quality gates, with CI across Python 3.10–3.13.

The bound is stated in the same file as the measurement: BM25 is a lexical baseline — it measures term-matching retrieval, not embedding quality — and the graded qrels for the example corpus are illustrative judgments, not a research benchmark. A gate that passes says the retrieval you specified still retrieves what your judgments say it should; it does not say the judgments are right, or that a different retrieval method would do better. Measure the layer that decides what the answer can see before you judge the answer itself.

- [RetrievalBench](projects/retrievalbench.md)

## Check a hand-derived gradient against finite differences

ScratchGPT's autograd engine is about 400 lines of hand-written backward rules in NumPy — broadcasting-aware arithmetic, matrix multiplication, reductions, softmax, log-softmax, gather, layer norm and fused cross-entropy — under a pre-LN character-level GPT with 419,328 parameters, 2 layers, 4 heads, d_model 128, context length 64 and a 65-character vocabulary. A falling loss does not prove those rules are right: the loss can move down on a given run even when a rule is wrong, and the shipped 3,000-step run reaches 1.83 nats/char validation loss in about 4.5 minutes on one CPU core without that number saying anything about the derivative. So the suite checks every autograd operation against central finite differences — the definition of the derivative, evaluated numerically — alongside forward and backward passes, a short training run that must reduce loss, and a causality test proving position t cannot attend to position t+1. 70 Python tests in all on 3.10–3.13, retaining all 11 original tests, with a fresh public clone passing the editable install and the full test suite and CI running the same checks across Python 3.10–3.13.

The rule is about what the check is independent of: a finite-difference check is not a second run of the same computation, it is the definition the derivation claims to implement, computed directly. When you derive a gradient by hand, check the gradient itself, operation by operation, before you trust the model built on it — the loss curve is evidence about the training run, not about the derivative.

- [ScratchGPT](projects/scratchgpt.md)

## Lint the prompt like code

Prompt files are production configuration — model instructions, tool policy, examples, user data — but they rarely get the same automated review as application code. A leaked API key or a prompt that tells the model to ignore its controls is easy to miss in review and expensive to discover later, so PromptGuard lints prompt, Markdown, JSON and YAML files locally, with no network dependency, the way a code linter treats source: deterministic findings with a rule ID, severity, file, line and redacted excerpt. It flags OpenAI-style and AWS-style keys, private key headers and assigned secrets, GitHub personal access tokens, Slack tokens, Google API keys and JSON Web Tokens, all redacted per rule in findings and reports; email addresses, phone numbers and payment-card numbers checked with the Luhn algorithm; prompt-injection language that asks a model to ignore earlier instructions, reveal hidden prompts, bypass controls or exfiltrate credentials; and missing or incomplete Markdown prompt metadata frontmatter. Reports come in terminal, JSON, SARIF 2.1.0, JUnit XML, Markdown and standalone escaped HTML, with severity and finding-count gates returning meaningful exit codes so CI can fail on them. Known findings are suppressed through a baseline that records them as SHA-256 fingerprints bound to a digest of the matched value, so a rotated or newly introduced credential is a new finding while the same credential stays suppressed — and the baseline file holds no raw material. 68 unit tests cover the scanner rules, token detection and redaction, report escaping, SARIF generation, JUnit XML, Markdown summaries, baseline suppression, filtering and gate exit codes; the offline demo runs against safe and risky fixtures plus a token fixture generated at runtime, and validates the SARIF, JUnit and Markdown reports and the baseline suppression flow — the risky fixture produces 8 findings with maximum severity critical, and the high-severity gate rejects it as expected — with CI across Python 3.10–3.13.

The bound is stated in the same file as the check: deterministic linting is a review signal, not a guarantee — it does not claim to catch every prompt-injection technique. All credential-shaped values in the fixtures are fake, and the demo builds its token fixture at runtime so the committed files contain no credential-shaped literals. Lint the prompt before it ships, with the same seriousness as the code that calls the model — and remember the lint is a check on the file, not a proof about the model.

- [PromptGuard](projects/promptguard.md)

## Optimizing the bound is not recovering the marginals

Mean-field variational inference is an optimization problem: it fits a product distribution by maximizing the ELBO, a lower bound on the log evidence. A better objective value feels like progress, but the objective is not the statistic you asked for — and on a small enough problem you can watch them diverge. VariLab makes the divergence inspectable on tiny supplied Ising distributions where every target state can be enumerated.

Two spins, zero fields, coupling J=3. The target favours aligned states, almost equally split between (−1,−1) and (1,1); the exact means are zero and the exact cross-covariance is tanh(3)=0.995055. Three product-distribution runs change only the initial means — same ascending sequential coordinate order, 100-sweep cap, 1e-12 sweep-change tolerance. A zero start stops at (0,0) after 1 sweep with ELBO 1.386294, reverse KL 2.309329 and maximum mean error 0. A positive .1 start stops at (.994902,.994902) after 7 sweeps with ELBO 3.005027, reverse KL 0.690596 and maximum mean error 0.994902; the negative start is symmetric. The higher-ELBO runs have lower reverse KL and worse marginal means, and every product approximation misses the target's nonzero cross-covariance entirely.

A stopping rule does not certify optimality either. The symmetric run stops with zero coordinate residual and gradient, yet it is not an ELBO maximum: a small joint positive perturbation raises the objective. VariLab's curvature API returns the analytic ELBO Hessian at supplied interior means using exact fractions of the compiled binary-float inputs, with symmetric congruence T^T H T = D and exact positive/negative/zero eigenvalue counts: at J=3,m=0 the inertia is (1,1,0) and direction (3,1) has exact positive form 8, so the coordinate fixed point is a saddle; at the broken-symmetry fitted point the inertia is (0,2,0). The no-edge control is exactly representable by the product family — its means match tanh(fields) to floating precision and its max-mean-error gate passes — while the positive-start coupled gate fails.

The bound is stated in the same file as the check: this is a constructed counterexample on supplied tiny distributions, not an empirical method ranking, and the finite-state reference is floating-point enumeration, not exact rational arithmetic. 183 tests cover the analytic references, the nonmaximum stopping example, the curvature certificates and the CLI. Optimize the bound if the bound is what you need — but check the marginals you actually asked for, because a better number on the wrong side of the approximation is still the wrong answer.

- [VariLab](projects/varilab.md)

## A green suite is a regression gate, not a certificate

Evaluating an LLM or agent output is not like unit-testing a function: the same prompt can come back different after a prompt edit, a model swap, or a slow dependency, and a single score hides which of those moved. EvalForge treats evaluation as a repeatable gate instead of a one-off notebook. Suites are JSONL files with stable IDs, prompts, expected values, tags and metadata, so a prompt edit is a diff and baseline comparisons match on the stable ID; and every response is scored by deterministic checks — exact, contains, regex, JSON equality or subset, token-F1 similarity, numeric tolerance, word and character length bounds — that give the same result for the same output, so CI stays stable and review discussions stay concrete. When `checks` is omitted, a default is derived from `expected`: JSON values use JSON equality, numbers use numeric matching, strings use normalized exact matching.

The adapter is just a command. The task prompt goes in on stdin and the answer comes back on stdout, with `EVALFORGE_TASK_ID` and `EVALFORGE_PROMPT` in the environment — so the harness does not care whether the text came from a local model, an internal agent binary, or a paid API command configured separately, and a non-zero exit is preserved as a run error rather than silently dropped. Invalid tasks fail before anything runs: unsupported check types, malformed regexes and invalid JSONL are reported with the task ID or line number before any adapter command runs, so a broken suite never spends model calls finding out it is broken.

The comparison is the gate. `compare` matches candidate to baseline by task ID, reports regressions before improvements, treats missing candidate tasks as failures, and exits 1 when a task drops more than `--max-drop`, a passing task starts failing, or a baseline task is missing — with `--format json` for automation, `--markdown` for a CI job summary, and `--sarif` for a SARIF 2.1.0 comparison that maps regressions to errors and missing tasks to warnings. `--fail-under` sets a minimum mean score, tag filtering scopes a run, and retries, timeouts and bounded parallel execution (`--workers`) keep a run within budget, with exit codes 0/1/2 making the whole thing scriptable. One HTML report with inline CSS, escaped model output, summary cards, tag roll-ups and per-task details — no JavaScript, no external assets, no trackers — plus JUnit XML, Markdown and SARIF 2.1.0 from the same run, so results reach the surfaces that already review code instead of living in a file only a human opens.

The demo runs six tasks against a deterministic local adapter and passes 6/6 offline with mean score 1.000 and zero errors; the mock adapter is a stand-in that proves the evaluation loop, not a model pretending to measure model quality. And the limit is stated, not hidden: a passing suite is a regression gate, not proof the system is safe or correct outside the tasks in the suite. 92 Python tests on 3.10–3.13, including all 68 original tests unchanged, with 24 complete retained reports independently compared at 11,808 numeric and 2,691 other scalar leaves, actual-Chrome paired, sign-assignment, record and binomial checks, and an isolated installed wheel verifying nine module origins; standard library only, fully offline. A green suite tells you the change did not regress what you wrote down — nothing more, and nothing less. Distinct from 'Compare against a baseline, not against nothing', which is about measuring a change against a prior window; this one is about what an evaluation suite can and cannot certify.

- [EvalForge](projects/evalforge.md)

## Validate the record before you trust the numbers

Agent frameworks are good at showing a friendly final answer and bad at preserving the operational truth of how it got there — which tool was called how many times, where the time went, what it cost, whether it looped. AgentTrace keeps that truth in a portable record: one JSONL event per step, each carrying `run_id`, `step`, `kind` and `name` — kinds `llm`, `tool`, `action`, `observation`, `error`, statuses `ok`, `failed`, `cancelled`, `timeout` — with optional `duration_ms`, token counts, `cost_usd`, input/output payloads, and a `parent` link to an earlier step in the same run. A format agents and test harnesses can append to and Unix tools can inspect.

Validation comes before analysis, because a corrupt trace produces confident-looking numbers. Malformed events, duplicate step IDs, unknown parents, negative numbers, unknown event types and bad timestamps are reported before any summary is trusted. The summary then makes the operational facts explicit in the same report: p95 step latency, run depth, token totals and cost alongside error counts, so "slow" and "expensive" are numbers next to "failed", not impressions from watching a run.

A loop is a repeated signature, not a repeated count. The signature is kind, name and the input payload serialized with sorted keys, so a retry with different arguments is a different signature — the gate fires on an agent stuck repeating itself, not on one retrying with new inputs. And the review is a script: `--fail-on-error`, `--max-loop-repeat`, `--max-p95-ms`, `--max-cost-usd` and `--max-steps` turn trace review into a command CI can run, with meaningful exit codes. `compare` measures a candidate run against a saved baseline — absolute and percentage deltas for runs, steps, errors, tool and LLM calls, repeated signatures, p95 latency, tokens and cost — and exits 1 when a configured gate fails, so an agent change is protected in CI without calling a model.

The report is built to be archived: a standalone HTML timeline with untrusted trace payloads escaped, no JavaScript and no external service, so the run stays reviewable after the agent and its logs are gone; the same analysis also emits JUnit XML for CI test viewers, Markdown for CI job summaries, and SARIF 2.1.0 that maps validation and gate failures to code-scanning tools. The offline demo proves the loop without a model: a fixed local fixture — a five-step baseline run and a slightly slower candidate, p95 212 ms against 272 ms, cost $0.0045 against $0.0060 — runs validation, analysis, gates, reporting and comparison end to end, asserting the JUnit report holds 2 tests with 0 failures, the Markdown summary starts with a PASS status, and the SARIF report is version 2.1.0 from driver AgentTrace with empty results. 33 unit tests, CI across Python 3.10–3.13, standard library only, fully offline.

The bound is stated in the same file as the check: the demo's timing and cost numbers are fixture data, not evidence about a real model, and the gates police the recorded run, not the quality of the agent's answers. Distinct from 'Compare against a baseline, not against nothing', which is about measuring a change against a prior window, and from 'A green suite is a regression gate, not a certificate', which is about what an evaluation suite can and cannot certify — this one is about the record itself: no analysis of a run is better than the trace it was computed from.

- [AgentTrace](projects/agenttrace.md)

## A small residual is not a small error

A residual is a number with a unit, and the unit is not the error you care about. BellmanLab's one-state self-loop pays 1/100 each step at discount 99/100, so its exact value is one. Starting from value zero, the Bellman residual is 1/100 — but the actual value error and the certified upper bound are both one. Testing the raw residual against a value-error tolerance of 1/10 passes the wrong gate: the check looks strict and the answer is wrong by a factor of a hundred. The contraction certificate divides the residual by 1 minus the discount, so the correct gate fails — and synchronous exact value iteration first meets the certified tolerance after 230 sweeps. The demo asserts all three states in sequence: initially passing raw residual, failing certified error, finally passing certified error. The residual was never the error; it was the error times (1 − discount), and at discount 99/100 that factor is 1/100.

The same discipline holds for a policy, not just a value. Exact policy evaluation solves `(I − discount·P_policy)v = reward_policy` with rational Gauss-Jordan elimination, and a zero residual on those equations only says the policy's own values are consistent — it does not certify the policy is optimal. A separate full Bellman audit checks every action, returns every greedy tie and computes the value-error bound. The delayed-return fixture makes the gap concrete: a three-state model pays 1 immediately and terminates, or pays 0 then reaches a state paying 1/5 forever; at discount 9/10 the immediate action gives start value 1, and exact policy improvement chooses the delayed return and reaches 9/5. The evaluation was exact either way; only the audit says which one is better.

And a number returned under a cap is not the number you asked for. BellmanLab's nested robust policy iteration never improves the controller from an unfinished inner solve: with the inner nature cap set to 1, the returned value is 4/5 — an upper bound on the risky policy's robust value, whose true value is −4/5 — and controller improvement is withheld. With the outer controller cap at 1 and a completed inner solve, the evaluated value is exactly −4/5 and the proposed safe action is stored separately, not passed off as evaluated. Only when both policies are stable does the run return 2/5 as the robust optimum, after two controller evaluations and three nature evaluations. A capped solve hands you a bound and labels it; treating it as the exact value is the same mistake as testing the raw residual against a value tolerance.

The bound is stated in the same file as the check: only finite, fully observed, discounted supplied models are supported, and the certificate bounds value error, not greedy-policy loss or statistical uncertainty — exact arithmetic cannot validate the supplied model's fit to the world. 70 tests cover the certificates, including 972 exact policy evaluations across 243 two-state stochastic models checked independently by two-by-two Cramer formulas, and 3,888 controller/adversary Cramer solutions verifying every exact fixed-controller value on the same grid. Distinct from 'Optimizing the bound is not recovering the marginals', which is about a stopping rule that halts at a non-maximum fixed point — this one is about testing a quantity against the tolerance it actually bounds: a small residual, a zero evaluation residual and a capped-solve value are three different numbers, and only the certificate says which one you hold.

- [BellmanLab](projects/bellmanlab.md)

## Direction is layout, not translation

Sorani Kurdish reads right-to-left, and a site that treats direction as a property of the translated string will eventually serve a Sorani page that reads the wrong way. The Kurdistan International Sociological Association site makes direction a property of the layout instead: one i18n config (`src/i18n/config.ts`) supplies each locale's `lang` and `dir`, and the locale layout sets them on the page — so a translated string can never arrive with the wrong direction, because direction was never the string's job. The same single-decision discipline runs through the rest of the site: every page lives once under `src/app/[locale]/`, so it exists in English, Sorani (`ku`) and Kurmanji (`kmr`) alike, and the locale is part of the URL rather than a cookie or a query parameter — a link to the Kurmanji conference page is a link. Interface strings live in per-locale JSON dictionaries with the keys kept in sync, so changing wording never means touching a component, and news posts are Markdown files per locale with `title`, `date`, `excerpt` and `author` frontmatter, parsed with gray-matter and remark. And because the content is editorial — no accounts, no search index, no per-visitor state — the whole site is a Next.js static export (`output: "export"`) served from Cloudflare, and pushing to `main` redeploys it: the build is the deploy, with no server to keep up, scale or patch. The lesson travels: when a property belongs to the page — direction, locale, identity — set it where the page is built, once, and let every string inherit it; patching it onto content one translation at a time is how it eventually arrives wrong. Distinct from 'Keep the words and the code on different schedules', which is about words and code changing at different rates — this one is about a page-level property that must never be a string's job.

- [Kurdistan International Sociological Association website](projects/kurdistansociology-website.md)

## A pooled diagnostic cannot see inside one chain

A diagnostic that only compares chains against each other can report that everything is fine while every chain is broken in a different way. HamiltonLab's rank-normalized split and folded R-hat checks make the gap concrete, independently implemented from Vehtari et al., Rank-normalization, folding, and localization, Sections 4.1/4.2: split every retained chain in half, pool the draws per coordinate, average tied ranks, map ranks to normal scores with the Blom offset and take the between/within ratio on those scores — then repeat after folding the draws around the pooled median, and report the maximum of both components. On a separated two-component mixture, four HMC chains accept .997 to 1.000 of their proposals yet never switch modes, and the classical unsplit x R-hat is 6.944902 — while the rank-split maximum is only 1.733936, smaller, not larger, because it is a different statistic, not evidence of better mixing. Two deterministic counterexamples show why the classical value alone is not enough: four 100-draw chains at two different scales give a classical R-hat of 0.994987 and a rank split of 0.989949, both looking low, while the folded rank-split component is 2.117248 and exposes the scale difference; and four identical chains, each with its first half negative and its second half positive, also give a classical R-hat of 0.994987 — it cannot see a difference between chains when there is none — while the rank split of 2.115500 exposes the shift inside each chain. The same checks stay quiet when the chains genuinely agree: on the correlated Gaussian, HMC gives rank split 1.007774 and folded 1.001669. The fix is structural, not a tighter threshold: values below 1 are left unclipped, no threshold is enforced, and when either component is undefined the maximum stays null rather than silently passing — a null is a result, not a pass. A diagnostic that only compares chains can certify that the chains agree with each other; only one that also looks inside each chain can say whether any one of them moved. 82 tests cover the diagnostics, including both counterexamples, tie ranks, the Blom inversion and affine and chain-order invariance. Distinct from 'Acceptance is not exploration', which is about a high acceptance rate hiding trapped chains — this one is about the diagnostic itself: agreement across chains is not evidence about what happened inside one.

- [HamiltonLab](projects/hamiltonlab.md)

## Let the baseline learn too

An adaptive method that beats a frozen baseline has proved nothing — the baseline has to be given the same information the method uses. BanditLab's greedy baseline is not frozen: it updates its posterior after every outcome and picks a new highest-mean arm at every remaining decision, the way any honest simple policy would. Even against that learning baseline, the optimal adaptive policy wins by exactly 1/36 over three pulls — 187/108 against greedy's 46/27 — and the audit shows the whole loss sits in greedy's first decision: its later occupied decisions have zero Bellman gap, so the comparison measures the opening choice, not a straw man left behind. The fixed-arm commitment, which never learns at all, loses 7/108, decomposed as 1/36, 8/297 and 1/99 across its decisions — a reminder that the gap between "simple" and "frozen" is itself measurable.

The clairvoyant comparator is the other side of the same discipline: it knows the latent rates beforehand and reaches 2 at three pulls, so it is an upper bound, not an available learning algorithm — the optimal Bayes regret is 29/108, and a bound that cannot be run is a yardstick, not a rival. The loss accounting is exact rather than sampled: `audit_policy` propagates probability mass forward and decomposes the gap as a performance-difference identity — optimal value minus expected reward equals the sum of occupancy-weighted Bellman gaps — with terminal mass one, and independent oracles check every complete depth-three two-arm policy tree for 16 prior pairs (2,048 references) and every depth-two three-arm tree for 64 prior triples (1,728 references), plus all 256 initial Beta shape pairs against an independent binomial/Bernstein CDF expression. The scope stays narrow — independent Beta-Bernoulli arms, 1–3 arms, horizon 0–12, exact arithmetic on supplied priors — and exact arithmetic does not make an assumed prior true. Distinct from 'Compare against a baseline, not against nothing', which is about measuring a change against a prior window, and from 'Pin the baseline, not just the result', which is about gating the control so fixture drift cannot erase the contrast — this one is about the baseline's strength: a baseline that cannot learn makes any adaptive method look good, and the comparison only means something when the simple policy is allowed to use the same outcomes the method does.

- [BanditLab](projects/banditlab.md)

## Optimal at one belief is not optimal at every belief

A plan that is optimal at the belief you happen to hold is not optimal at the beliefs you might hold — and a certificate that only names the one point hides the rest. BeliefLab's probe tree is the best plan at the uniform belief, worth 7/10 against zero for either exploit-first sequence, and it stays optimal across [13/40,27/40] — but at either certain-state prior it loses 13/10, because a probe that costs 1/10 is pure waste once the state is already known. The exploit-0-twice tree is the mirror image: uniform-prior value zero and regret 7/10, worst regret 4 at belief0 = 0, yet it is optimal on [27/40,1], where the state is likely enough that probing buys nothing. Either tree looks like the right answer if you only check it where it wins; the audit shows where each one stops winning.

So the certificate is the whole interval, not the point. `audit_policy` compares a supplied fixed tree against the optimized observation-contingent envelope and returns every closed zero-regret belief interval — isolated points included — plus the regret at the input belief, the maximum regret and every maximizing component, so the answer is a map of where the plan holds rather than a single verdict. It works even for a tree the planner pruned from its representative set, including one optimal only at a single belief, because a plan that is right at exactly one prior is still a fact worth recording, not a case to drop. The forward trace behind it accounts for every observation history, including impossible ones with null beliefs rather than fabricated posteriors, and the probe policy's uniform-prior accounting is −1/10 + (1/2)(4/5) + (1/2)(4/5) = 7/10, each branch contributing 2/5 — the conditional 4/5 is not the contribution.

The scope stays narrow — two hidden states, supplied trees up to horizon four, supplied models only — and the numbers are exact on those models: 86 tests cover 81 model settings against 2,187 complete depth-two policy trees, 729 fixed sequences, all 27 sensing-model trees' regret curves checked against complete-tree oracle crossing cells, four reproducible SVGs and an isolated ten-module wheel. Distinct from 'A small residual is not a small error', which is about testing a quantity against the tolerance it actually bounds — this one is about where a certificate holds: a plan's optimality is a region of beliefs, and reporting the point without the region is reporting a different claim.

- [BeliefLab](projects/belieflab.md)

## The natural baseline is not the best baseline

The obvious baseline for a policy gradient is the exact state value — it is the quantity the theory names, and it is exactly right. ScoreLab shows it can still be the worst choice on the table. Take one Bernoulli action with P(action=1)=4/5 and reward equal to the action: the expected reward is 4/5 and the exact gradient is 4/25. With no baseline at all, the per-trajectory gradient variance is 4/625. With the exact state-value baseline of 4/5, it is 36/625 — nine times worse. The value baseline is exact, yet it makes the estimator noisier, because subtracting the value moves the action-1 estimate from 1/5 down to 1/25 while moving the action-0 estimate from 0 up to 16/25: the score is 1/5 after action 1 and −4/5 after action 0, so the two estimates spread apart instead of converging on the gradient. The variance-minimizing scalar baseline is 1/5, not 4/5: with it, both actions produce the same estimate 4/25 and the variance is zero. The baseline that minimizes variance is a property of the score and the return together, not of the value function alone.

The optimal scalar baseline at each time/state node makes the point general: E[Z_j · G0]/E[||Z_j||²], using the whole reward-to-go gradient vector, not a local reward-weighted average and not the exact state value. ScoreLab returns both sides of the exact excess-variance identity for every supplied baseline, so the comparison is a calculation, not an argument about which baseline looks principled. And the matrix controls show how far the right baseline can go: on a one-step three-action policy with probabilities 1/6, 1/3, 1/2, features (0,0), (1,0), (0,1) and rewards 0, 1, 2, the exact gradient is [−1/9, 1/3] — no baseline leaves trace variance 269/324, the exact state-value baseline 29/324, the best scalar baseline (64/51) 53/612, and the exact matrix [[2/3,−2/3],[−1/2,1]] gives zero on every action, because a fixed matrix B Z at each time/state lets every output coordinate use every score coordinate. But the gain is not always large: on the separate 64-path sequential model the scalar-optimal trace is 1.462519 against matrix-optimal 1.460918, and its time/state score ranks are [1,0,1,1,1,1], so pretending every score covariance has an inverse would fail — rational RREF solves the singular normal equations with free coordinates set to zero, not a pseudoinverse.

The scope stays narrow — supplied finite models, 36 tests covering 256 one-step Bernoulli policies with analytic gradients and variance formulas, 24 shared-parameter sequential settings with 48 coordinate derivatives checked by a separate dual-number Cartesian path oracle plus central finite differences, 15 matrix-control settings with exact cross moments and principal minors, and two reproducible SVGs with a six-module wheel verified outside the checkout — and the reasoning follows Greensmith, Bartlett and Baxter (JMLR 2004, Sections 4–6), without implementing GPOMDP or reproducing that paper's experiments. Distinct from 'Compare against a baseline, not against nothing', which is about measuring a change against a prior window, from 'Pin the baseline, not just the result', which is about gating the control so fixture drift cannot erase the contrast, and from 'Let the baseline learn too', which is about the baseline's strength — this one is about the baseline's value: a baseline earns its place by the variance it removes, and the natural choice can remove less than nothing.

- [ScoreLab](projects/scorelab.md)

## A one-step quantity is not a long-run quantity

A policy changes two things at once: what happens on the next step, and where the chain spends its time afterwards. A quantity measured over one step cannot see the second change, so it can report zero while the long-run answer is nonzero. ErgodLab's occupancy fixture makes the gap exact: state rewards are 0 and 1, independent of the action, the controlled transition is `[[1/2,1/2],[1/4,3/4]]`, the stationary distribution is `[1/3,2/3]`, the average reward is `2/3` and the stationary derivative is `[-1/18,1/18]`. Freeze the stationary distribution and the immediate-reward gradient is zero — the policy looks like it does nothing. Let the distribution move and the true average-reward gradient is `1/18`: the whole effect is the policy moving where the chain spends its time, which is exactly the part the frozen calculation held fixed.

The same gap runs the other way for variance. Two symmetric chains with state rewards 0/1 have identical one-step stationary reward variance `1/4`, yet staying in the same state with probability `7/8` gives asymptotic reward-sum variance per step `7/4` while deterministic alternation gives zero. The alternating chain has period two, so its exact stationary block-sum variance is zero for even lengths and `1/4` for odd lengths, and the figure shows all lengths 1..16 with both exact limits on the same axis. One step cannot tell them apart; the long run can, because variance accumulates over the path the chain actually takes, not over the step it takes next.

The audit keeps the two quantities separate instead of letting one stand in for the other. A centered Poisson solve returns `h` satisfying `(I-P)h=r-rho` and `mu h=0`, and the average-reward gradient is checked in both forms, `d rho = (dmu) r + mu dr = mu dr + mu (dP) h`; for every positive edge the report returns the centered martingale increment `D=R-rho+h(next)-h(state)` and its nonnegative variance contribution, whose stationary second moment is the asymptotic variance of centered reward sums per step. The discounted extension draws the same line at a finite horizon: on a separate two-coordinate fixture with controlled switch probabilities `1/2,1/4`, derivatives `1/8,1/16` and average-reward gradient `[1/18,-1/18]`, at beta `1/2` the stationary proxy is `[1/21,-1/21]` while the true fixed-start objective is `2/7` with gradient `[5/98,-1/98]`, and the proxy's exact curl entry is `-1/147`, ruling out a local scalar potential — though zero curl alone is not a sufficient global-potential test. At beta `1` the audit solves the centered Poisson limit instead of inverting the singular discounted matrix, recovering the true average-reward gradient and zero curl, including periodic chains.

The scope stays narrow — supplied finite irreducible models, 1..5 states, 1..4 actions, 1..3 shared coordinates, rational probabilities and rewards, transition rows summing exactly to one, and the independent tree reference checking at most 1,280 parent assignments — and the numbers are exact on those models: 39 tests cover 25 analytic two-state transition settings, 16 exact policy-weight gradient settings, nine multi-state/two-coordinate determinant and finite-difference references, explicit path enumerations through four steps, the alternating chain through length 32, period-three chains and every SVG point/limit geometry, with two reproducible SVGs and a six-module v0.2 wheel. Stationary sensitivities, directed spanning-tree formulas, Poisson equations and martingale decompositions are standard — the repository cites Aldous and Fill Section 9.2, Glynn and Infanger's Poisson-equation framework, and Greensmith, Bartlett and Baxter's average-reward policy-gradient context — but this is not GPOMDP, a learned policy, a sampled gradient estimator or a mixing-rate result, and reward-sum variance is not policy-gradient estimator variance. Distinct from 'A zero gradient is not a zero effect', which is about a gradient answering one question (feature sensitivity) while a different change (edge deletion) answers another — this one is about the horizon: a quantity measured over one step and the same quantity measured over the long run are different numbers, and the frozen one can be zero while the long-run one is not. Distinct from 'A mean is not the distribution', which is about a summary dropping the spread — this one is about time: two chains can agree on every one-step statistic and still differ by 7/4 against zero in the long run.

- [ErgodLab](projects/ergodlab.md)

## A filtered row is not a smoothed row

A state estimate is only as honest as the evidence it was allowed to use. ChainLab's two-state absorbing example makes the gap exact: states A and B, initial 0.5/0.5, emissions A:[1,0], B:[0.5,0.5] for symbols x/y. After the first symbol x alone, filtering says P(state A at time 0) = 2/3. After both symbols x,y, smoothing says the same quantity is 0 — the second symbol y, which state A can never emit, rules A out entirely. Both numbers are correct; they answer different questions, because the filtered row may only use what had been observed by then, while the smoothed row uses the whole sequence. Using the smoothed row for an online decision at time 0 would decide with evidence from the future — a leak dressed as a better estimate. The final filtered and final smoothed rows agree, because at the last time step they have the same evidence; the disagreement lives only where the evidence differs.

The same discipline runs through the forecasts. `forecast` conditions on the whole supplied past and propagates states forward without assimilating any guessed observation: horizon 1 transitions once from the last conditioned state and predicts its emission, and each later step propagates again. The returned distributions are marginals, not a joint future path — in the absorbing example after x, each future marginal has P(y)=1/6, but P(y,y)=1/12, not (1/6)^2. The implementation does not multiply forecast marginals or feed their modes back as observed evidence, because a marginal at each horizon is not a path through the horizons.

The numbers stay exact on supplied models: 34 tests cover log-space forward/backward inference, Viterbi decoding and multi-sequence EM, with the prefix audit checking summed prefix predictive log scores across 12 test sequences (480 symbols) at -372.302842489947 against -372.30284248994707 from full forward likelihood — an absolute difference of 5.68e-14, an implementation audit, not a quality gain — and the rare-symbol example keeping a log likelihood of -3536.77070284 finite over 256 observations with emission 1e-6 while its probability underflows to 0. The scope stays narrow: supplied models only, N 1–8, alphabet 1–16, T 1–256, horizon 1–32, no stateful streaming API and no claim that a caller's training protocol is leak-free. Distinct from 'A marginal is not a path', which is about per-position winners not forming a valid joint path — this one is about time: a row's evidence is the observations up to its own time, and a number computed with more evidence is a different number, not a better version of the same one.

- [ChainLab](projects/chainlab.md)

## An unbiased estimate need not be a possible value

A squared distance cannot be negative — but an unbiased estimate of one can. DriftLens's unbiased squared MMD drops the diagonal: it averages off-diagonal within-group kernel pairs and the full cross-group average, so nothing in the formula constrains a single estimate to the range of the quantity it estimates. On two independent 30x4 standard-normal samples (seed 13, bandwidth 2, 499 permutations), the unbiased estimate is -0.00487090068 with p=0.55. The negative sign is not a bug and not evidence of a difference: unbiasedness is a property of the average over repetitions, not a promise about any one draw, and the permutation p-value correctly says there is no evidence against the null. The shifted arm — the same samples with 2 added to each current coordinate — gives 0.63453882456 with p=0.002, so the same estimator separates the constructed difference cleanly.

The report shows the negative value as it is rather than clipping it to zero — clipping would buy a plausible-looking range at the cost of the unbiasedness the statistic was chosen for. The witness diagnostics keep the two statistics separate: they report group means and their difference plus mmd2_biased, the diagonal-including version, alongside the diagonal-excluding unbiased statistic the permutation test uses — two numbers with different jobs, not two versions of the same answer. The finite-sample limits stay visible too: Monte Carlo p-values use the +1 formula, so they can never be zero, and a tiny separated 2-vs-2 fixture has exact p=1/3 over its six allocations — the resolution floor, not a verdict about the samples.

The scope stays narrow — 45 tests, Python 3.10–3.13 CI, bandwidth prespecified or chosen by a pooled label-invariant rule, exchangeability under the null required for the permutation to be valid, and no power or type-I-error study: the fixtures are selected development examples, not a drift-detection benchmark. Distinct from 'A p-value cannot be smaller than its own resolution', which is about the p-value floor on the same project — this one is about the statistic: an estimator can be unbiased and still return a value its estimand cannot take, and the fix is to read the number for what it is, not to clip it into range.

- [DriftLens](projects/driftlens.md)

## A conditioned proposal is not a better filter

Conditioning the proposal on the current observation sounds like it should only help: each particle is drawn from a distribution that already knows what was just observed, instead of blindly from the transition. ParticleLab's optional linear observation-conditioned Gaussian proposal tests that intuition on the same inherited sequence at N=32 across all sixteen fixed seeds — and the mean RMSE barely moves, .082871 for the bootstrap filter against .081548 for the conditional proposal, while the conditional variance RMSE is worse, .037895 against .035944. The proposal that uses more information at each step ends up with a worse estimate of the spread. The extra conditioning changes which particles are proposed and reweights them accordingly, but it does not add information about the latent state beyond what the observation already carried, and the reweighting itself costs precision.

The case study is careful about what the comparison can and cannot say: a more informative observation fixture has smaller conditional errors, so the result is not a general ranking and not a causal claim about proposals — it is a measured counterexample to the assumption that a smarter proposal is automatically a better filter. Seed labels do not ensure paired identical random streams, so the comparison is across the same sixteen seeds, not a paired draw-by-draw race. The proposal also exposes its own moments and predictive importance weights, with exact initial predictive evidence and deterministic q=0 moves, so the check is inspectable rather than asserted.

The scope stays narrow — 114 tests, Python 3.10–3.13 CI, a scalar supplied-parameter model, development fixtures, no convergence certificate. Distinct from 'Effective sample size measures weights, not support', which is about a weight score hiding lost support on the same project — this one is about the proposal: using the observation earlier in the pipeline does not guarantee a better estimate at the end of it, and the check is the measured error, not the cleverness of the mechanism.

- [ParticleLab](projects/particlelab.md)

## A maximum effective sample size can still miss the mass

Effective sample size is a statement about the weights you observed, and the weights you observed cannot tell you about the mass you never drew. LatentLab's two-atom failure control makes the gap exact: the joint masses are (0.000001, 0.999999) against proposal masses (0.999, 0.001), with true evidence 1 — so with probability (999/1000)^64 = 93.79749638258456%, all 64 draws hit the common proposal atom. The effective sample size is then 64, the maximum possible, every weight equal — and the log-evidence estimate is -13.814510 rather than 0, an underestimate by factor 999,000. Full support is present in the proposal; nearly all the joint mass is simply unseen, and no weight diagnostic can report on draws that never happened.

The control is stronger than a seed-picked bad run because the failure is enumerated, not observed once: finite binomial enumeration with exact rational event probabilities gives expected evidence exactly 1 for every K, while expected log estimates for K=1, 4, 16, 64 are about -13.793788, -13.737278, -13.529377 and -12.785808 — they rise with K and stay below 0 while remaining far from the truth, so more samples narrow the gap without closing it. The same extension keeps the honest contrast next to it: on a separate linear-Gaussian model with exact log evidence -2.15379530672424, using the exact posterior as proposal makes all weights constant and the 64-draw estimate recovers that value — the audit works when the proposal actually covers the mass. The scope stays narrow — 43 tests, two reproducible SVGs, a five-module wheel, a two-atom control and one two-dimensional fixture, inference auditing rather than an ESS accuracy certificate. Distinct from 'Effective sample size measures weights, not support', which is about a weight score hiding collapsed support in a particle filter — this one is about importance weights: a perfect ESS certifies balance among the draws you got, not coverage of the mass you did not.

- [LatentLab](projects/latentlab.md)

## A gate with nothing to measure must fail, not pass

A check that passes when it measured nothing is worse than no check at all: it stamps the run green and removes the reason to look. LogLens builds its gates the other way round. `--min-apdex 0.94` turns the Apdex user-satisfaction score into a pipeline gate — requests within T satisfied, within 4T tolerating, beyond 4T frustrated, with a per-path table worst-first so the endpoint dragging the score down leads — and a log with no durations fails the gate rather than passing unmeasured. There is nothing to score, so there is no pass to give. The same instinct governs the spike detector: `--timeline` buckets requests and 5xxs per minute, and a bucket only flags as a spike when both the error rate and the count clear a threshold, so a single error in a quiet minute never reads as an incident. A rate without a count is noise, and a gate that fires on noise trains everyone to ignore it.

The rest of the tool is built to keep the numbers honest once the gate has something to measure. Filters scope every statistic — `--since`/`--until` for the incident window, `--status 5xx,404` for exact codes and classes, `--path-prefix /api` for one service's surface — so narrowing to a failing slice never leaves stray numbers computed over the full log. Latency is reported as p50/p95/p99 and the slowest requests, never an average that would hide both a mass at 250–500ms and a long tail past 1s. And the same command that investigates also guards: `--max-error-rate 0.05` exits 1 when the 5xx rate breaches 5%, so loglens drops into CI or a cron health check against a fresh log slice.

The scope stays narrow — 241 unit tests, CI across Python 3.10–3.13, standard library only, CLI plus importable library; unparseable lines are skipped rather than aborting the run, so a damaged line never costs the analysis of the thousands of good ones around it; `--split-at` and `--vs` compare the windows around a deploy, and `--report` renders the findings as a Markdown incident document. Distinct from 'Validate the record before you trust the numbers', which is about validating a trace before any summary is trusted, and from 'A green suite is a regression gate, not a certificate', which is about what a passing suite can and cannot certify — this one is about the gate's behaviour on missing input: when there is nothing to measure, the only honest answer is a failure, not a pass.

- [LogLens](projects/loglens.md)

## The best first move can be the one that looks worse now

A decision that looks best right now is only best if the future holds nothing the present choice can change. BanditLab's three-pull example makes the gap exact: arm 0 has prior Beta(1,1), mean 1/2; arm 1 has prior Beta(5,4), mean 5/9. With one pull left, take arm 1 — there is nothing left to learn for. With three pulls, the optimal adaptive policy starts with arm 0, the lower-mean arm: if the first pull succeeds, pull arm 0 again; if it fails, switch to arm 1. The outcome of the first pull changes the second choice, and that is what the first pull is buying. The exact totals say so: the optimal policy expects 187/108 against 46/27 for the updating greedy policy that always takes the current best mean, 5/3 for the best fixed-arm commitment, and 2 for a clairvoyant that knows the latent rates beforehand. Information is only worth buying while there is budget left to spend it on — with two pulls, both first arms tie and the adaptive gain over greedy is exactly zero.

The audit keeps the claim narrow and checkable: the solver builds every reachable posterior/time state bottom-up and returns the whole graph, with all maximizing arms and ties at every state, so the first move is a computed optimum, not a heuristic preference for exploring. Independent oracles check every complete depth-three two-arm policy tree for 16 prior pairs (2,048 references) and every depth-two three-arm tree for 64 prior triples (1,728 references), so the 1/36 gain over greedy is a verified property of the stated priors, not a sampled trial result. The scope stays narrow — independent Beta-Bernoulli arms, 1–3 arms, horizon 0–12, six evaluated budgets (1, 2, 3, 4, 6, 8) — and exact arithmetic does not make an assumed prior true. Distinct from 'Let the baseline learn too', which is about giving the baseline the same information the method uses — this one is about the first move itself: a lower current mean can be the right opening when its outcome decides what comes next, and worth nothing when there is no next decision left to inform.

- [BanditLab](projects/banditlab.md)

## A local metric does not certify a finite step

Natural gradients are called "parameterization invariant", and FisherLab shows exactly where that claim ends: at the step. On the three-action fixture p=(1/2,1/3,1/6) with rewards (0,1,3), four full-tangent charts agree exactly on the natural probability tangent (-5/12,1/18,13/36) — the local object is genuinely chart-independent, with natural L1 gap 0 in all four. But a finite Euler step is not a local object. In a separate binary control with local coordinate z=theta^3 at theta=1, the natural directions dz=1 and dtheta=1/3 have the same initial mapped logit tangent, yet a step of eta=1/2 gives logit 3/2 directly versus 343/216 in the curved chart, an exact difference of 19/216, and updated action-1 probabilities of approximately 0.817574 versus 0.830329. The same gap shows on the three-action fixture itself: a step of 1 along the exact logit natural direction has actual KL 0.725586 against a local quadratic prediction of 41/72=0.569444, and the linear reward prediction 71/36=1.972222 against an actual 2.303238. The metric certifies the direction at a point; it is not a promise about where a step of any size lands — Martens (2020) Section 12 draws the same line between infinitesimal and finite-step invariance.

The scope stays narrow — 45 tests, two reproducible SVGs, exact rational arithmetic for geometry, logit differences and local predictions, with floating point used only for the probabilities and KL in the finite-step controls; full-support categorical expected reward only, no policy training, line search or trust-region enforcement — but the lesson travels: a certificate that holds in the limit holds only in the limit, and a step is a new claim that needs its own check. Distinct from 'Keep the exact answer next to the approximation', which is about measuring an approximation's error against an exact baseline — here the local quantity is exact and still does not certify the step — and from 'Check a hand-derived gradient against finite differences', which is about verifying a derivative implementation, not about what a verified local quantity does and does not promise.

- [FisherLab](projects/fisherlab.md)

## A group deletion is not the sum of its single deletions

An influence function answers a local question: how does the loss move if one row's weight changes infinitesimally? Deleting the row is a finite change, and InfluenceLab shows the linear answer can be far from the refit — and, more sharply, that exact single deletions do not add up either. On the seven-row logistic fixture (theta approximately (-0.275488, 0.220249), query loss 0.614042), the linear fixed-N prediction for deleting row 5 is +0.203204 against an actual converged refit of +0.305655, an error of -0.102451; damping the inverse Hessian (delta 0.5) moves the estimate further away, to +0.119499, not closer — a stabilizer is not a refit. The group effect is where the sum breaks: deleting rows 5 and 6 together changes the query loss by -0.357507, while their two separate finite deletions sum to -0.142898, and deleting all seven rows reverses the sign outright, -0.004253 first-order against +0.079105 actual, with the refit landing at theta zero and query loss log(2). At the base point the group derivative is exactly the sum of the individual derivatives — the non-additivity belongs to finite deletions, not to the derivative.

The scope stays narrow — 43 tests, two reproducible SVGs, five-module wheel parity; 17 grid nodes and 51 refits along the deletion paths, with Simpson16 residuals of +1.381e-7, +4.825e-6 and +7.442e-4 against the actual endpoints, and every one of the 15 base/deletion fits converged to a maximum absolute gradient of at most 8.197e-11 with undamped solve residuals at most 5.551e-17 — but the lesson travels: a derivative is a tangent and a deletion is a destination, and when the change is finite, only the refit knows where you land. Distinct from 'A local metric does not certify a finite step', which is about a verified local quantity failing to certify a finite step — here each single deletion is itself an exact refit, and their sum is still wrong.

- [InfluenceLab](projects/influencelab.md)

## The value of feedback is the gap to the best open-loop plan

A sensing action looks valuable when you compare it to doing nothing — but doing nothing was never the alternative. The alternative is the best plan that commits to all its actions before any observation arrives, and only the gap to that plan measures what feedback itself is worth. BeliefLab makes the comparison exact on the prescribed sensing model: at the uniform belief, four exploit-only two-step sequences tie at value zero and `[0,0]` is selected, while the observation-contingent optimum probes first and is worth 7/10 — so the feedback gap at the uniform belief is the full 7/10. Over every belief the open-loop envelope is `2*abs(2*b-1)` and the gap is `max(0, 7/10 - 2*abs(2*b-1))`, peaking at 7/10 at b=1/2 with a uniform-belief integral of 49/400, positive strictly between 13/40 and 27/40 and zero at the boundaries and outside. The control settles what the gap is a property of: change every action's observation rows to `(1/2,1/2)` and nothing else, and the gap is exactly zero at every belief — observations that carry no information are worth exactly nothing, at every prior.

`compare_feedback` reports the gap as a function, not a point: it partitions `[0,1]` at the union of both envelopes' exact breakpoints, names both envelope witnesses and their endpoint values on every segment, and returns the gap at the supplied belief, its global maximum, all closed belief intervals attaining that maximum — isolated points included — and its exact integral with respect to uniform `db`. The gap is nonnegative by feasible-policy inclusion, since every fixed sequence is also a contingent policy, but it need not be convex. And the integral is geometric area over beliefs, not expected deployed gain under an empirically measured belief distribution. `solve_open_loop` is the honest baseline it is measured against: it evaluates every fixed action sequence — at most 81 under the existing scope — returns every sequence with its exact alpha vector and input-belief value, all maximizing sequence IDs and the exact all-belief envelope, and is neither a myopic nor a hand-picked baseline, a fully observed oracle, nor a policy that replans after each observation.

The scope stays narrow — two hidden states, supplied models only, horizons up to four, 86 tests including 16 that compare all 729 fixed sequences across the same 81 depth-two models against independent full state-path sums, and four SVG tests checking every curve coordinate, the zero-gap control, complete metadata and regeneration — but the lesson travels: the value of information is a difference between two optima, and the baseline has to be optimized over the same horizon, or the gap measures the baseline's weakness instead of the information's worth. Distinct from 'Optimal at one belief is not optimal at every belief', which is about a fixed tree's optimality region — here the object is the gap between two envelopes, and its maximum, attaining intervals and integral are the certificate — and from 'Compare against a baseline, not against nothing', which is about measuring a change against a prior window, not about optimizing the baseline itself.

- [BeliefLab](projects/belieflab.md)

## A unique prediction does not identify a coefficient

A sparse fit that prints one coefficient vector is reporting a choice the solver made, not necessarily a fact about the data — and SparseLab makes the gap exact. On duplicate columns at lambda=1/4, the forward fit is [7/4,0,-1/2] and the reverse fit is [0,7/4,-1/2]: different selected features, the same objective 5/8, identical predictions and zero KKT residual in both. The exact rational active/sign enumerator finds both sparse witnesses, and convexity makes every mixture optimal, including the denser midpoint [7/8,7/8,-1/2]. No ridge term is added to hide the ambiguity. The prediction is identified; the coefficients are not — so reading the printed vector as a feature ranking mistakes the order the solver visited the columns for a property of the fitted model. The contrast sits in the same project, not a different solver: on correlated columns at lambda=1/8 the exact oracle independently agrees with [0,33/17] at objective 19/68, after one sweep leaves gap 0.330882353 and max KKT 0.176470588 and 18 sweeps reach the objective — there the coefficients are pinned, because the problem pins them, not because the solver is more careful.

The scope stays narrow — 62 tests, three reproducible SVGs, seven-module wheel parity, and an exact enumerator that tests all 3^p sign patterns for up to five columns, with fractions representing the validated binary64 inputs exactly — but the lesson travels: whenever a fit is presented as a selection or a ranking, ask whether the objective identifies it or the algorithm's tie-breaking does, and treat a coefficient that could be swapped for another without changing the prediction as unidentified, not as zero. Distinct from 'Label what the data cannot identify', which is about a target action with zero behavior probability — a row the data cannot speak about, labeled rather than averaged in — here the data and the objective are complete and the optimum is still a continuum.

- [SparseLab](projects/sparselab.md)

## An aggregate improvement can hide a per-context regression

A direction that improves the aggregate is not a direction that improves every part of it — and FisherLab makes the split exact. With context frequencies (3/4, 1/4), equal binary action probabilities, and rewards (0,1) in the first context and (0,-2) in the second, a shared parameter has natural direction 1/4 and the total reward derivative is positive 1/64 — yet the second context's own derivative is -1/8. Stepping along the shared direction raises the weighted total while making one context worse, and the decomposition says exactly how far the shared model can go: the full-conditional target has squared length 7/16 = 1/64 + 27/64, the reachable part plus a metric-orthogonal residual the shared parameter cannot touch. Giving each context its own parameters reaches both targets with zero residual — but that is a larger model, not a better step in the shared one.

The same lesson shows in the controls. Replacing the frequencies with uniform weights changes the objective itself: its natural direction -1/2 has derivative -1/32 when evaluated on the original weighted objective, so a direction computed under one weighting can point the wrong way under another. And a context-gauge control is frozen under conditional normalization yet shows spurious nonzero Fisher information and gradient if naively modeled as a global joint softmax — the model that ignores the conditioning invents signal where the conditioned model has none. An aggregate derivative is a weighted sum, and a weighted sum can be positive while one of its terms is negative; before stepping, check the terms, not just the total.

The scope stays narrow — 45 tests (28 original + 14 behavior + 3 SVG), two reproducible SVGs, exact rational arithmetic for the context systems, with the same full-support categorical scope as the rest of the project — but the lesson travels: whenever a single number summarizes several groups, ask what each group contributes to it, and treat an improvement that helps the average while hurting a part as a trade-off to name, not a win to report. Distinct from 'A mean is not the distribution', which is about a summary statistic hiding the shape of what it summarizes — here the object is a direction, a step the model is about to take, and the hidden part is which contexts it helps and which it hurts — and from 'A local metric does not certify a finite step', which is about a verified local quantity failing to certify a finite step — here both the aggregate and the per-context derivatives are local and exact, and the gap is between them, not between local and finite.

- [FisherLab](projects/fisherlab.md)

## Reconstruction is not generation

A model that reconstructs held-out inputs well has shown it can compress and
recover what it has seen — not that sampling its prior produces the same
distribution. LatentLab makes the split exact on a disclosed fixture: a
150-parameter Gaussian VAE trained on the same 128 synthetic eight-mode
points, from identical initialized weights and data/noise RNG streams, for
800 minibatch Adam updates, with another 128 points held out for evaluation.
The no-KL arm (beta 0) has the slightly lower deterministic reconstruction
error — posterior-mean MSE per coordinate 0.00268 against 0.00281 for beta 1
— yet its prior samples are further from the data: sliced W2 squared 0.0676
against 0.0241, with 71.09% of prior samples outside radius 0.3 of all mode
centers against 51.56% for beta 1. The ELBO agrees with the generation side,
not the reconstruction side: negative ELBO 8.0758 at beta 0 against 1.6600 at
beta 1, with analytic posterior KL 9.3704 against 2.2073. And beta 1 is no
certificate either — over half its prior samples still lie outside the
disclosed neighborhoods. Reconstruction and generation are two capabilities
measured on two different objects, and a good number on one does not certify
the other.

The scope stays narrow — 43 tests, two reproducible SVGs, a five-module
wheel, one two-dimensional fixture and default seed; only beta 1 is the
ordinary negative-ELBO objective, beta 0 omits KL, and the observation noise
0.2 is wider than the fixture jitter 0.06, so the distance diagnostic also
reflects likelihood-family mismatch — but the lesson travels: when a model is
judged on one capability, report the capability you actually need, and treat
a reconstruction score as a reconstruction score, not as evidence about what
the model generates. Distinct from 'Two metrics can disagree, and the choice
is the claim', which is about which metric selects the model — here the two
numbers measure two different capabilities, and the confusion is treating
success at one as evidence for the other — and from 'Choose the metric the
failure cannot pass', which is about designing a metric the failure cannot
pass — here the point is that no reconstruction number, however well
designed, can certify generation, because generation is a different task.

- [LatentLab](projects/latentlab.md)

## Marginals do not compose when randomness is shared

Two releases that each look private on their own can fail completely together when they share their
randomness — and PrivacyLab makes the failure exact. In the developed bit-secret control, Z is zero
with probability 3/4, and the releases are A = secret XOR Z and B = Z. A alone has pure privacy
factor 3 and B alone factor 1, yet A XOR B recovers the secret exactly: the joint release has delta
1 for every finite factor and its minimal pure factor is infinite, while the marginals at factors 1,
3 and 9 read 1/2, 0, 0 and 0, 0, 0. Conditioning on A = 0 makes B deterministically 0 versus 1 — the
missing premise is the conditional mechanism, not the marginals.

The same lesson shows in the envelope. The factor-frontier extension computes the complete
worst-neighbor delta profile for every finite factor, and on the developed three-secret/four-output
control with rows [1/16, 5/16, 1/8, 1/2], [5/16, 3/8, 1/16, 1/4], [1/8, 5/16, 3/16, 3/8] and edges
0-1, 1-2, the profile is 5/8-5t/16 from 1 to 5/4, 5/16-t/16 from 5/4 to 5, and zero after 5 — the
maximizing direction switches at 5/4, a point absent from the likelihood-ratio grid {1, 6/5, 3/2, 2,
5/2, 3, 5}, where both directions tie at delta 15/64. Connecting values on the grid would have
missed the switch entirely. Inverse budgets keep the same honesty: delta 1/4 needs factor 6/5, 15/64
needs 5/4, 0 needs 5, a singular plateau of 1/2 makes target 1/4 unattainable at any finite factor,
and a full-support control needs the finite factor 500000000000000000000000000000 — reported
exactly, not clipped or called impossible. The adaptive extension shows the same split
conditionally: the fair branch charges conditional delta 1 only to incoming mass 1/2, so its actual
delta is 1/2 against uniform and additive bounds of 1.

The scope stays narrow — 63 tests, three reproducible SVGs, a seven-module wheel, supplied tables of
at most 8 secrets and 64 outputs, and exactness that concerns the supplied finite table and listed
edges, not a deployed mechanism — but the lesson travels: when a guarantee is claimed for a
combination, audit the combination, not the parts, and treat a marginal number as a marginal number,
not as evidence about the joint. Distinct from 'Don't claim what you didn't observe', which is about
claiming more than the evidence supports — here each marginal claim is fully supported, and the
failure is assuming the parts compose — and from 'A group deletion is not the sum of its single
deletions', which is about attribution across a group — here the point is that shared randomness can
make the joint arbitrarily worse than any marginal suggests.

- [PrivacyLab](projects/privacylab.md)

## Locally best choices need not fit together

Choosing the best value for each variable separately can produce a joint answer that is not just suboptimal but incompatible — and VariLab makes the gap exact on supplied Ising models where every state can be enumerated. A directly constructed two-spin model with fields h=(1/4, 63/256) and coupling J=-2 has two unique ordinary marginal modes, both +1, with P(+1) about 0.506550 and 0.502723 — yet their joint (+1,+1) scores -385/256, while the unique joint MAP (+1,-1) scores 513/256, an exact gap of 449/128 = 3.5078125. Taking each spin's best value gives the wrong joint decision by a wide margin, and no amount of refining the marginals fixes it: the marginals are already exact. A symmetric zero-field J=-2 example makes the same point without any numbers favouring one side: two global optima exist, every local max-marginal permits either spin, but independent first choices (-1,-1) are incompatible — stored parent-conditioned traceback chooses (-1,+1), an actual optimum.

The cyclic case is sharper still, because there is no ordering that lets each choice be made locally. On the directly specified zero-field triangle with all three couplings -1, every singleton permits both spins in a global optimum, but independent first choices (-1,-1,-1) score -3 while compatible reverse traceback reaches +1, a gap of 4, with six global optima and no unique answer. The same couplings on a 63-spin odd ring give exact score 61 and 126 optima — matching the independent formula n-2 and 2n, one unsatisfied edge plus a global spin flip — at a peak of 8 bucket assignments. The remedy is not better local scores but a compatible joint decision: exact rational max-sum with separator context, every maximizing assignment counted, and a 128-isolated-spin fixture that counts exactly 2^128 maximizing assignments without enumeration. The elimination order matters too: on a 16-node zero-field star with J=1/2, hub-first needs 65,536 bucket assignments and is refused before any numeric table is built, while min-fill peaks at 4 and matches analytic log Z 12.892072 — a refused order is a property of the order, not of the graph.

The scope stays narrow — this is joint MAP, not marginal MAP: no variable is summed out, scores are not probabilities, and the witness is deterministic for its plan, not globally lexicographic or order-invariant — but the lesson travels: when the answer is a joint assignment, audit the joint assignment. 183 tests and six reproducible SVGs cover the analytic references, the curvature certificates and the CLI. Distinct from 'Two possible cuts can be jointly impossible', which is about joint probability — marginals inventing an event the model forbids — here every local choice is genuinely permitted and the failure is compatibility of the choices, not probability — and from 'A group deletion is not the sum of its single deletions', which is about effects not adding — here the object is the decision itself, and locally best need not be jointly best.

- [VariLab](projects/varilab.md)

## A float pass at the boundary is not an exact pass

RobustLab's exact audit treats each validated input as the binary float it actually is, not the decimal literal it was written as, and returns every score, dual norm, radius, worst margin and perturbation as a reduced numerator/denominator string, with certificate flags decided by integer signs instead of rounded decimal views. The float audit is kept beside the exact result, and where they disagree the disagreement is explicit. A selected boundary fixture makes the stakes concrete: its float worst margin is approximately +2.081668171e-17, so the float strict flag passes, while its exact rational worst margin is approximately -2.775557562e-18, so the exact strict flag fails — the same model, the same radius, opposite verdicts, separated by a rounding error. A second cancellation fixture disagrees in the reverse direction, and a dyadic exact-zero control fails both strict flags. A margin this small is not a pass; it is a rounding artifact wearing a pass's clothes, and only the arithmetic that decides the flag can tell which one it is.

The exactness has stated limits, and they are part of the certificate: the audit preflights at most 4,096 row-coordinate products before fraction conversion, and it refuses L2 outright, because general directions and margins there can be irrational. Seventeen additional arithmetic, API and CLI tests check independent rational vertex and corner minima across 156 model/label/norm configurations, serialized witness feasibility and attained scores, both rounding-disagreement directions, exact binary input semantics, prediction disagreements, zero and tied weights, the executed work-cap boundary and subnormal-squared underflow; that increment brought the suite to 56 tests and two SVGs, and the box audit brings it to 80 tests and three SVGs. An exact rational result certifies the stated mathematical linear function and the real-valued threat ball, not a separately rounded inference or attack pipeline, and rounding the rational witness can change a near-boundary result. At the boundary, the arithmetic is the claim: check the number in the arithmetic that will actually decide it. Distinct from 'A clipped attack cannot prove robustness', which is about solving the wrong optimization problem — here the optimization is right, and the arithmetic is what flips the verdict.

- [RobustLab](projects/robustlab.md)

## Rectangular uncertainty is a different problem, not a different solver

BellmanLab's robust planning takes a list of complete scenarios, and the scenario index is not one global model choice: at each state and action, nature may independently select any listed scenario's reward and transition row, after observing the action — the (state, action)-rectangular closure of the listed models. The shape of that set is part of the problem, and changing it changes the answer. A one-state fixture at discount 1/2 offers a risky reward of +2/5 or −2/5 against a safe +1/5: the nominal risky value is 4/5, its robust value is −4/5, and the robust safe optimum is 2/5 — so the policy that is optimal for the nominal model loses 6/5 in robust value. Optimizing the nominal model and then asking how robust the answer is does not recover the robust optimum; it answers a different question and gets a different number.

The two-state fixture makes the modeling choice visible. Two alternating states at discount 1/2 carry globally opposite reward vectors [1,−1] and [−1,1]. Keeping one global scenario fixed gives a worst start value of −2/3 — but the rectangular closure lets nature pick a negative row at both states, and its value is −2. Same listed scenarios, different problem: the closure lets the adversary switch scenarios state by state, and no solver for the rectangular problem can return the global problem's answer, because the two problems have different values. The audit returns every exact scenario Q-value, the minimum across scenarios and every minimizing scenario index, so the choice nature made is visible in the certificate rather than hidden in a single number.

The scope is stated with the set: 1 to 8 scenarios, at most 2,048 stored transition entries across all of them, a combined normalized model-denominator LCM capped at 1,000,000, and the ordinary 256 KiB file and 256-sweep caps. The v0.2 foundation has 54 tests — the 34 original checks plus 16 robust API/CLI tests and four robust SVG tests — and an independent oracle enumerates four controller policies and four stationary adversary choices on each of 243 two-state/two-scenario models, 3,888 closed-form two-by-two Cramer evaluations reproducing every exact robust fixed point. The rectangular formulation is attributed to Iyengar (2005) and Nilim and El Ghaoui (2005); the finite-scenario contract, implementation, certificates and fixtures are original. These are supplied ambiguity sets, not statistically learned confidence sets, and nothing certifies an unlisted environment. Distinct from 'A small residual is not a small error', which is about testing a quantity against the tolerance it actually bounds — here the solver is exact either way, and it is the stated problem that differs: write down which uncertainty set you mean, because the value depends on it.

- [BellmanLab](projects/bellmanlab.md)

## Separate worst cases are not a joint worst case

When two sides face the same unknown, the worst case for each side is not a worst case for both — because the two worst cases can demand incompatible values of the same fact. GameLab's shared-table interval extension makes the point exact: a fixed policy pair faces one unknown payoff table, not two independently selected adverse tables, and `interval_audit` computes the exact worst joint deviation gap over a supplied full Cartesian entrywise interval box. For every pure reply pair it constructs the signed coefficient of every entry before maximizing, retains endpoint choices and contributions, and returns an attaining matrix with a direct best-reply audit — and it also reports each player's separately maximized unilateral gain and the conservatism of their sum, so the gap between the two answers is visible, not hidden. In the developed shared-entry control only A[0,0] varies in [0,2], all other entries are one, and both policies choose action zero: the row player's worst deviation requires entry zero, the column player's worst requires entry two, so the exact shared worst gap is one while their incompatible separate maxima sum to two. The game value stays one throughout, and the separate robust-security pair is an equilibrium for every allowed table — the sum of the two worst cases is a world in which the same entry is zero and two at once.

The same shape shows up at a smaller scale and in the opposite direction. For a full 2x2 unit box with uniform fixed policies the shared worst gap is 1/2 against a separate worst-regret sum of one; and for a one-action game with sole payoff [-50,50] the value-range width is 100 but every policy pair's gap is zero — payoff uncertainty is not the same as incentive to deviate, and a wide range is not a large gap. Complete endpoint game solves certify the attainable game-value extrema v(L) and v(U): the lower-game row policy and upper-game column policy separately optimize worst security and guarantee pair gap at most v(U)-v(L), with a signed audit that can be tighter — though the construction does not claim to minimize worst joint gap over policies, and the certificate says so.

The scope stays narrow — 53 tests, two reproducible SVGs, a six-module wheel matching all six complete CLI JSON outputs outside checkout; all 16 zero/one-width boxes on a nonconstant 2x2 base, each at nine fixed policy pairs, checked against independent exhaustive endpoint enumeration, with corner game values, robust security, shared-entry and singleton cancellation, affine, zero-width, rectangular and 4x4 controls, strict schemas and no mutation, and three added SVG tests binding all 29 numbers in the interval figure — but the lesson travels: when the unknown is shared, maximize once over the shared unknown. Summing separately maximized worst cases counts a world that cannot exist. Distinct from 'Marginals do not compose when randomness is shared', which is about a joint release being worse than its marginals because one shared coin couples two releases — here the joint is better than the sum of the separate worst cases, because the two worst cases demand incompatible values of the same entry — and from 'Rectangular uncertainty is a different problem, not a different solver', which is about the shape of the uncertainty set changing the value — here the set is fixed, and it is the maximization that must be joint, not separate.

- [GameLab](projects/gamelab.md)

## A free restart is not optional stopping

BetLab's betting test lets you stop at any time: a past-measurable bet b_t in [0,1] multiplies wealth by 1+b_t·D_t, where D_t is the candidate-minus-baseline score difference in [−1,1] under the one-sided conditional null E[D_t | past] ≤ 0, and Ville's inequality bounds the probability of ever reaching 1/α by α — an arbitrary stopping time is allowed within the fixed test. What the test does not allow is a fresh unit of capital after ruin. The invalid comparator bets one and injects a fresh unit before the next round whenever wealth is zero, and on the eight-round fair-coin null tree — 255 internal histories, 256 equiprobable leaves, α = 1/4, threshold 4 — it crosses with probability 201/256, expected final wealth 9/2 and expected stopped wealth 423/128, against 5/64 for the fixed mixture over bets [0,1/4,1/2,3/4,1] and 9/128 for the past-only heuristic, both with expected final and stopped wealth exactly 1. The 201/256 is not a mystery: it is the chance of at least one run of two positive signs in eight fair flips, and the node audit exposes negative conditional-expectation slack after ruin. The refill is a counterexample to free restarts, not to optional stopping — stopping is a choice inside the test, restarting is a new test with the losses forgotten.

The valid alternative is to price the restarts before the stream starts. BetLab's start-allocation extension allocates one initial unit across deterministic start times chosen before observing anything — at most 16 starts in 1..256, positive weights summing exactly to one, ruined components staying zero, unstarted components contributing their reserved weight — and the complete statistic is a fixed convex mixture, not the largest start-specific result. On the delayed-signal control of eight negative, eight positive and eight negative differences, bet one with starts 1, 9, 17 at equal weights first crosses threshold 4 at round 12, holds wealth 257/3 including reserve 1/3 at round 16, and ends at zero, while the one-start control is permanently ruined at round one. On the fair eight-round null audit with starts 1, 3, 5, 9 at weight 1/4 each, the round-nine budget stays reserved at every leaf and the crossing probability is 5/32 at α = 1/4 with final and stopped expectations both 1 — the invalid free-refill control stays 201/256. The six-round negative-drift tree tells the same story at a smaller scale: crossing 1/81 for both valid constructions and 281/729 for the invalid restart, 17/729 for the start allocation, with expected final wealth 1261/2916 and stopped 683/1458. And the reversal control — eight +1 then twelve −1 — has both valid processes first cross threshold 4 at round 4 and then end below 4: a crossing stays recorded, and stopping does not erase the history that produced it.

The scope stays narrow — 67 tests, three reproducible SVGs, a seven-module wheel matching all ten complete CLI JSON outputs outside checkout; at most 64 observations, 16 fixed bets and 1..32 bisections, eight-round trees, supplied laws only — with no unbounded-score method, learned optimal bet, automatic stream selection, multiple-test correction, drifting-mean or causal-effect estimate, or production monitoring service, and a crossing is not a posterior probability, an effect-size estimate or proof that a particular model is generally better, while non-crossing is not evidence of equivalence — but the lesson travels: a stopping rule is part of the test, so a restart is a change to the test, and it has to be paid for in the design, not taken for free after the fact. Distinct from 'Marginals do not compose when randomness is shared', which is about one shared coin coupling two releases so the joint is worse than either marginal — here there is no shared coin and no second release; the test itself is changed by topping up its capital — and from 'Separate worst cases are not a joint worst case', which is about maximizing separately over one shared unknown — here the unknown is not shared, the budget is replenished, and the failure is a rule change disguised as a stopping decision.

- [BetLab](projects/betlab.md)

## A recommendation changes the deviation

A joint play distribution can leave no profitable fixed-action deviation and
still tell a player to take an action they would rather replace once they see
their recommendation — and Correlab makes the gap exact. In Roth's explicitly
attributed lecture-8 CCE-not-CE game, uniform diagonal play pays 3/10 per
player, the best raw fixed gain is -3/10, and the clipped coarse epsilon is
zero: no fixed action improves on the recommendation. But recommendation C
still permits a conditional gain of 11/10, with weighted and full-swap gain
11/30. The distribution passes the coarse test and fails the conditional one,
because the deviation a player can profitably make depends on what they know
when they make it.

The same split shows up wherever a single number averages over
recommendations. A rare recommendation with mass 1/1000 has weighted gain
1/1000 and conditional incentive one — the average calls it negligible, the
player who receives it faces a certain gain. Three equally likely
recommendations with row payoffs [0,0,1] have largest one-pair gain 1/3 but
full-swap gain 2/3, attained by sending every recommendation to action 2:
restricting the deviation class understates the gain by half. And removing
correlation changes the answer too: a developed coordination law pays 3/2 per
player and is a correlated equilibrium, while its product-marginals control
pays 3/4 and carries swap regret 1/4 — the marginals are identical, but the
joint law and its incentive properties are not. A six-round history finishes
as an empirical coarse correlated equilibrium while its final action pair
alone has coarse epsilon 11/10: the aggregate passes and the last round
fails, and both numbers are exact.

The audit keeps the deviation classes separate instead of collapsing them.
Full-swap optimization separates by recommendation — choose an action
maximizing each row of weighted gains, then add the maxima — and the report
retains every optimal choice, the number of optimal maps, the
lexicographically first attaining map and all its joint-cell contributions.
Conditional gains divide by the recommendation's positive probability;
zero-probability recommendations return null. Identity signals recover the
full-swap gain and identical-row channels recover the clipped coarse gain, so
the two ends of the information spectrum are pinned, not assumed. The v0.2
suite audits all deterministic own-action partitions through four actions
independently for each player, with Bell counts 1, 2, 5, 15 and every strict
refinement relation; a developed cyclic control gives row gains 0, 4/3, 5/3,
1, 2 across partitions 000, 001, 010, 011, 012, and the attributed Roth
control yields 0, 11/120, 11/60, 11/30 as C's reveal probability rises 0,
1/4, 1/2, 1.

The scope stays narrow — 50 tests in v0.2, including independent enumeration
for 8,505 channel audits, 28 larger four-signal controls up to 625 policies
per player, 243 supplied post-garbling lift certificates and all 16
signal-alphabet size pairs, with three SVG tests binding 25 numeric cells and
all seven complete CLI outputs matching an installed seven-module wheel
outside checkout; 33 tests in v0.1 cover 2,835 game/law cases, 28 controls up
to 256 maps per player and all 256 length-four histories at three prefixes.
The audit covers supplied finite general-sum bimatrix games and exact joint
laws, one to four actions per side, at most 1,000 realized rounds and 100
checkpoints — it does not search for an equilibrium, train an agent, or
certify safety, and its epsilon values are payoff incentives, not distance to
an equilibrium set. But the lesson travels: when an evaluation reports no
profitable deviation, ask which deviations it allowed and what the player
knew when choosing — a pass under one deviation class is not a pass under
another. Distinct from 'A mean is not the distribution', which is about a
summary hiding the shape of what it summarizes — here the weighted gain is a
mean over recommendations, and the conditional gain is the
per-recommendation number it averages away — and from 'Locally best choices
need not fit together', which is about locally permitted choices being
jointly incompatible — here every conditional deviation is individually
attainable, and the failure is that the audit never allowed it in the first
place.

- [Correlab](projects/correlab.md)

## A stable value does not mean a stable strategy

In a two-row/one-column game, a payoff flip of 10^-12 changes the unique
optimal row from [0,1] to [1,0] while the game value does not move at all.
GameLab's payoff-change audit bounds exactly how much can move and how much
cannot: with epsilon the maximum entry change, the value changes by at most
epsilon, and the old equilibrium pair's new gap is at most two epsilon. The
value is Lipschitz in the table; the optimal strategy is not. A solver that
reports only a value, or only one optimal policy, hides which half of the
answer is fragile — the number you can trust to a tolerance and the choice
that can flip under a rounding error.

The same project shows the other side of non-uniqueness. Duplicate rows in
a 4x2 game give optimal vertices [0,1/2,1/2,0] and [1/2,0,1/2,0], every
convex combination is optimal, and the fourth action is dominated; the
representative [1/4,1/4,1/2,0] is a deterministic equal average of distinct
optimal vertices that preserves the face rather than pretending it is
unique. Coordinate extrema include attaining vertices, and their ranges are
not independent choices. And a zero observed payoff certifies nothing on its
own: in rock-paper-scissors the value is zero with one-third mixed policies,
but both fixed action-zero policies also yield payoff zero while their
unilateral gains sum to two.

The scope stays narrow — 53 tests, including all 81 ternary 2x2 matrices
against an independent one-dimensional envelope oracle, optimal-vertex
cross-pairs and convex mixtures, and all 16 zero/one-width interval boxes at
nine policy pairs each; two reproducible SVGs, with four SVG tests binding 23
cells and three added tests binding 29 numbers; all six full CLI outputs
matching an installed six-module wheel outside checkout. The audit covers
supplied small zero-sum matrices of one to four actions per side, exact
bounded inputs, no runtime dependency — it does not rank real agents, solve
general-sum or hidden-information games, or claim a new algorithm. But the
lesson travels: when a solution looks stable, ask whether the value is stable
or the strategy is — a bound on one is not a bound on the other. Distinct
from 'Separate worst cases are not a joint worst case', which is about two
worst cases demanding incompatible values of the same unknown table — here
the table is fixed and known, and the instability is in the optimum itself,
not in the uncertainty about it.

- [GameLab](projects/gamelab.md)

## The price decides the policy

SpecLab's oracle planner chooses a block length from each emitted prefix
before drafting, using fully known finite target/draft tables: it retains
every Bellman action's immediate and future costs, transitions and
nonnegative slack, then separately composes complete policy sequence and
count laws. On the switching four-token fixture the optimal assigned cost
is 23/10 against the best fixed gamma's 47/20 — an exact gain of 1/20
hypothetical units, with no-draft action 0 and every fixed gamma 1..3 as
full-strength baselines and ties broken toward the smallest action. But
charge target positions instead of verification rounds and the same planner,
on the same tables, selects no drafting everywhere. The optimal policy is
not a property of the model pair; it is a property of the price. Change
what you charge and the "best" block length changes with it — the gain
exists only under the cost that produced it.

The same project keeps the rest of the bill honest. The original greedy
path reports 122 verification rounds against 480 target-only — a 74.6%
modeled reduction — and, in the same breath, 510 actual sequential scoring
calls against 480: the round saving is real and the work increase is real,
and neither number is allowed to stand alone. A mismatched order-2/order-3
draft pair drops acceptance to 0.03, pinned in the suite so the
measurement is demonstrably real. The v0.2 stochastic engine corrects the
four-token law to exact TV zero, where using the target directly as a
rejection fallback instead gives TV 141/1024; its expected 75/32 modeled
rounds require 179/32 target positions and 13/4 draft calls. And the v0.3
report keeps unreachable work out of the bill: the full target law stays
AAAA/BBBB with mass 1/2 each, only empty, BB and BBB are reached as policy
round starts, and unreachable prefix values remain inspectable, not charged
as executed work — while planning and policy-lookup overhead are declared
unpriced, not silently zero.

The scope stays narrow — 47 tests in v0.3, including all 12 tiny prefix
policies on 25 model pairs under three objectives, 72 prefix-dependent full
joint-law comparisons and 36 size/horizon/gamma-limit cases, with the
115-cell SVG embedding the complete report and CI checking seven modes from
a 12-module installed wheel outside checkout; 34 tests in v0.2, including
all 2,187 binary prefix-table pairs against an independent kernel oracle,
all 225 ternary quarter-grid pairs and every procedural RNG ticket for all
25 binary quarter-grid pairs at horizon 2, with a 96-cell figure and five
CI jobs; 14 tests in the original greedy path, with 8 prompts x 60 tokens
at gamma=4 giving identical output and mean acceptance 0.800. Supplied
finite tables only — vocabulary 1..3, horizon 1..4, gamma 1..3 — and the
oracle is not an online confidence/entropy stopping rule, a trained
acceptance head, a measured latency predictor or a new adaptive-decoding
algorithm: the comparison is descriptive under declared costs, not a
real-model throughput result. But the lesson travels: when an optimizer
recommends a policy, ask what it was charged for — a policy that is optimal
under one price can be the policy it never chooses under another. Distinct
from 'Show the bill with the gain', which is about reporting the cost
alongside the result — here the cost selects the result, so the bill is
part of the answer, not its footnote — and from 'Two metrics can disagree,
and the choice is the claim', which is about two measurements ranking the
same candidates differently — here one optimizer returns a different
optimum when the priced quantity changes — and from 'A plan has a cost
before it has a result', which is about the cost of planning — here the
planning overhead is declared unpriced, and the point is that the priced
quantity decides the plan itself.

- [SpecLab](projects/speclab.md)

## A test that cannot see the mistake is not a test of it

ScanLab's v0.3 extension couples dense state coordinates with full rational
transition matrices: matrix-affine composition preserves temporal
multiplication order, and reverse propagation uses the next transposed
matrix. The exact transposition identity is `-440563/15120` on both sides.
Omit only the transpose in reverse propagation and the gap is `7831/2520`.
Reverse only the matrix-product order, with write composition still correct,
and the final state changes from `[9/2,187/36]` to `[-14/9,2/3]`. Both
mistakes are real, both are exactly measured — and both become invisible
under diagonal restrictions, which are tested separately. A diagonal matrix
is its own transpose up to its entries and commutes with every other
diagonal matrix, so the restricted fixture cannot distinguish the correct
reverse pass from either wrong one. The suite passes, the code is wrong,
and the passing test is the reason nobody notices.

The same trap appears one version earlier. The v0.2 wrong-reverse-index
control uses the current decay instead of the next and gives `139/360`,
with gap `-259/36` against the exact identity `-817/120 = -817/120` — and
the case study says plainly that the control can be invisible on special
inputs, so independent checks matter. The remedy is not more tests of the
same restricted shape but checks that do not share the blind spot: 432
parameter coordinates across 36 models verified by independent bivariate
polynomial expansion, 24 full-direction polynomial models, 24 Hessian
symmetry checks and 51 independent future-decay product models, none of
them sharing the scan or derivative recurrence they verify. The v0.1
floating cancellation control makes the same point from the other side:
with input [1e16,1,-1e16,1] and decay 1, the sequential final state is 1,
the scan gives 0 and the exact rational result is 2 — and neither failing
control is turned into a tolerance-based success.

The project keeps the cost ledger honest alongside the correctness ledger.
The six-token, two-state dense fixture uses seven matrix-matrix and thirteen
matrix-vector products — 108 multiplications and 80 additions against the
sequential 24/24 — while unit-pair span falls from 6 to 4, treating whole
matrix operations as units rather than hardware latency. The v0.1 fixture
is the same shape in the other direction: span 7 against recurrence span 16,
but scalar multiplications rise from 32 to 136 and additions from 32 to 84.
The span improvement is real and the arithmetic increase is real, and the
counts exclude tangent construction, gradient products, loss reductions and
bit complexity — they are actual DAG counts on supplied pairs, not
end-to-end derivative costs or runtime claims.

The scope stays narrow — 63 tests in v0.3, including 96 independent
homogeneous-product shapes, full DAGs through length 32, 216 associativity
cases, 672 full-polynomial VJP parameter coordinates across 36 models, 24
full-direction polynomial models and 27 diagonal restrictions, with three
reproducible full-witness SVGs and six-command/nine-module installed wheel
parity; 46 tests in v0.2, including the new 68-cell figure embedding all
five complete DAGs with the original 114-cell figure preserved; 30 tests in
the original, including 729 scalar composition cases, 264 length/width
cases against an independent product expansion, 120 fixed LTI models, 123
independent gradient probes and all 64 streaming partitions. Supplied tiny
affine tables only — width 1..4 and length 0..32 in v0.3 — with no dense
HVP, general AD engine, trained-model quality, hardware-speed or
new-algorithm claim, and six sources attributed. But the lesson travels:
when a test passes, ask what it could have caught — a check that is
structurally blind to the mistake is not evidence against it, and the
restricted case that passes is not the general case. Distinct from 'Make
the fast path prove it equals the slow path', which is about two paths
agreeing — here the restricted path agrees with the wrong answer, so
agreement is exactly what misleads — and from 'Check a hand-derived
gradient against finite differences', which is about how to verify a
derivative — here the point is which inputs the verification can see — and
from 'A safeguard that never fires is not evidence it works', which is
about a safeguard with no observed trigger — here the test does fire, on
the restricted inputs, and its green result is the blind spot itself.

- [ScanLab](projects/scanlab.md)

## At the boundary, the rule decides

DigitLab's v0.3 extension solves all 1,797 clipped adversarial-radius
infima exactly for the fixed linear model: 99 clean errors, 796 positive
attained thresholds and 902 positive unattained infima — just over half
unattained. The infimum is a number, and whether the boundary itself is an
error is a separate question, one the tie rule answers. Lowest-index ties
determine whether the boundary counts as an error, and an error witness for
an unattained threshold lies strictly beyond it, not at it, so the
threshold alone does not describe the case at the threshold. The first
attained example is row 6 (true 6, competitor 4) and the first unattained
is row 0 (true 0, competitor 9); their zero-margin boundary predictions are
evaluated exactly and are not asserted to agree with floating evaluation on
a mathematical tie. The first examples are diagnostic, not a representative
sample — but the distinction is load-bearing: quoting the number without the
attainment silently converts a bound into a counterexample that does not
exist.

The same lesson appears one version earlier, in the box proofs. The v0.2
extension certifies exact affine-box correctness for the fixed linear model
— 1,698 / 1,495 / 1,028 / 23 of 1,797 test rows correct at radii 0 / 1/20 /
1/10 / 1/5 — by minimizing each true-label-versus-competitor affine margin
at its valid coordinate endpoints, with strict positivity required only when
a lower class index would win a tie. Attained witnesses expose 14 and 10
saved PGD survivors at the latter two radii: rows the finite PGD pool
counted as surviving are exactly foolable, so the attack's miss was a fact
about the attack, not about the model. And a zero-margin tie control is
correct for label 0 but fails for label 1 — the same zero margin, two
outcomes, decided entirely by the tie rule. A clipping control makes the
same point from the domain side: the minimum is 1 on the valid [0,3/10]
domain and -1 un-clipped, so the answer depends on stating the domain as
well as the number.

The scope stays narrow — 59 tests in v0.3, including 201 gradient probes,
two independent 144-case vertex references, 160 Fraction row references, 100
official-boundary checks and three full-report figures, with
nine-module/eight-CLI wheel reproduction; 45 tests in v0.2, including 201
gradient probes, 144 all-vertex certificates, 160 independent Fraction row
references and two full-report figures, with six-mode/eight-module wheel
parity; all 64,692 box margins and 7,188 witness decisions retained, with
exact real affine proofs only — not all floating executions, nonlinear MLP
verification, imperceptibility or an adaptive 1NN ranking. But the lesson
travels: a threshold is a claim about a number, and the case at the
threshold is a claim about a rule — state the tie rule, the attainment and
the domain alongside the number, or the number will be read as a case it
never was. Distinct from 'A float pass at the boundary is not an exact
pass', which is about floating arithmetic disagreeing with the exact answer
at the boundary — here the arithmetic is exact and the boundary still needs
a rule — and from 'A clipped attack cannot prove robustness', which is about
a finite attack's silence — here the exact certificate itself needs its
boundary rule stated before it can be read.

- [DigitLab](projects/digitlab.md)

## A zero error bar is not a zero error

ShapleyLab's sampled mode estimates attributions by averaging marginal increments over drawn feature orderings, and it reports a Monte Carlo standard error per feature — the sample standard deviation of the per-permutation increments divided by the square root of the number of orderings. On the three-way product, two orderings at seed 0 give [0.5, 0.5, 0] with standard errors [0.5, 0.5, 0] in six calls — and the exact attribution of the third feature is 1/3. The error bar reads exactly zero while the error is a third of the whole prediction-minus-baseline. The diagnostic measures how much the orderings you drew disagreed with each other, not how far their average sits from the exact answer, and two orderings that happen to agree on a feature report perfect certainty about a number that is wrong. A zero in the diagnostic is a statement about the draws, not about the distance to the truth.

At larger P the bars become honest about the wobble without becoming a certificate. With 4,096 orderings at seed 0 the same game gives [0.3220215, 0.3415527, 0.3364258] with standard errors about [0.0073017, 0.0074108, 0.0073835] in eight calls with caching, and the exact [1/3, 1/3, 1/3] sits within about 1.6 standard errors of each — but the diagnostic still describes only permutation randomness for this fixed model, point and background: not model-training uncertainty, not background representativeness, not confidence in feature importance. There are no confidence intervals, no adaptive stopping, no antithetic pairing and no convergence certificate, and each ordering telescopes to prediction minus baseline, so efficiency can pass while individual allocations remain wrong. Even when all eight coalition values have entered the cache, sampled output still averages the drawn increments — it never silently switches to the exact coalition-weight formula. Prefer exact mode when the game fits its budget. The linear case shows the other side of the same reading: a 64-feature sum with 32 orderings at seed 4 uses 2,002 calls against a preflight upper bound of 2,018, returns 64 unit attributions and reports zero Monte Carlo errors — there the zero is structural, because every linear marginal is constant. The same reading, zero, means "the draws never varied" in both cases; only the game tells you whether that is the truth or two draws that happened to agree.

The scope stays narrow — exact mode is the default, enumerating all 2^d coalition values with weight 1/(d·C(d−1,|S|)) and checking dimensions 1–6 against an independent factorial-ordering implementation; the full mask invokes the score once instead of B times, so calls equal (2^d − 1)·B + 1; individual mode takes 1–12 dimensions, group mode up to 64 raw features in at most 12 atomic groups, backgrounds of 1–1,000 rows and budgets of 1–1,000,000 with a 200,000 default; the preflight upper call bound is (max_masks − 1)·B + 1 with max_masks at most min(2^d, 2 + P·(d−1)), and a bound over budget rejects before any callback — conservative, because orderings can share masks; 49 Python tests and four Node/actual-Chrome tests, Python 3.10–3.13 CI, standard library only; the v0.2 live ledger checks 95 coordinate edits, 128 Fraction games, 64 independent BigInt product games, all 44 original coalitions, 18 players and 30 orderings, with an installed 11-module/four-command reproduction retaining the original exact/grouped/sampled modes and all prior demo reports. But the lesson travels: an error bar reports the variation in what you sampled, and a zero in it reports that nothing varied — read it for what it measures, and never as the distance to an answer you did not compute. Distinct from 'A test that cannot see the mistake is not a test of it', which is about a test restricted to inputs where the mistake cannot appear — here the estimator ran the full game and its own error estimate still read zero — and from 'A small residual is not a small error', which is about a residual measured in different units than the error — here the units match and the estimate is still zero while the error is not — and from 'The reference is part of the question', which is about the reference defining the question — here the question is fixed and the approximation's self-reported uncertainty is what misleads.

- [ShapleyLab](projects/shapleylab.md)

## Gate the claim, report the diagnosis

DistillLab's gates check the quantities the README actually claims: the teacher clears 0.80 accuracy (it reaches 0.8344), the distilled student beats direct training by at least 0.04 (the measured gain is +0.0656, 0.7469 against 0.6813), and the arm ordering holds — `python -m distilllab gates --min-teacher-acc 0.80 --min-distill-gain 0.04`. The control arms are not gated. Pseudo-labels at +0.0281 over direct, uniform smoothing at 0.6781, and the permuted-target control at exactly chance (0.1250 on eight classes) are reported as comparisons, not pass/fail criteria: they explain why the gain exists, and the suite pins the arm ordering from below as a fixture regression rather than promoting the explanation into a gate. A gate that can never fail is a decoration, so the demo also asserts an impossible gain of 0.5 fails — the check is proven live by watching it fail on a threshold nothing can reach. The scope stays narrow — 12 unit tests, fully offline, CI across Python 3.10–3.13, a small synthetic classification fixture, not language-model logit distillation — but the lesson travels: put a gate on the number you claim, keep the diagnosis as a report, and prove the gate can fail, or the green check is only a habit. Distinct from 'Pin the baseline, not just the result', which is about gating the comparison baseline so the contrast cannot silently disappear — here the baseline is already pinned and the split is between what is gated and what is merely reported — and from 'A gate with nothing to measure must fail, not pass', which is about a gate with no measurement at all — here the gate has its measurement and the question is whether it can fail.

- [DistillLab](projects/distilllab.md)

## Fit the repair where the failure is visible

CalibrLab's repair is a single temperature T fit by grid search on the validation split's NLL — and the split is the point, not the search. The fixture is built to be overconfident on purpose: a one-hidden-layer MLP trains on 20 samples per class and memorizes them, train accuracy 1.0000 against test 0.5563, and on held-out rows its top confidence bin averages 0.9735 confidence at 0.6602 accuracy, ECE 0.2765 before repair. On the training split the model is right on every row, so the failure the repair exists to fix — confidence far above accuracy — does not exist there to be fit: a temperature fitted to training NLL would be fitting to rows where the model is never wrong. On the test split the failure is visible, but fitting there would leak: the oracle temperature T = 3.30, fitted on test, reaches test NLL 1.1984, and it is computed and shown only as an unattainable reference. Validation is the one split where the failure is both visible and usable: the honest fit gives T = 3.85 (validation NLL 1.3118), test NLL 1.2060, and the 0.0076 gap to the oracle is the price of fitting honestly. The repair then does what it claims — ECE 0.2765 to 0.0651, MCE 0.3487 to 0.1216, Brier 0.7149 to 0.5964, NLL 2.0030 to 1.2060, accuracy drift exactly 0 — because it was fitted to the failure it was meant to fix. The same discipline holds past the fixture: the caller-supplied logits path never lets test labels fit T, and the tests verify that changing them does not change T.

The scope stays narrow — 45 tests, fully offline, CI across Python 3.10–3.13, the demo asserting both gate sides with an impossible ECE reduction of 0.9 failing as it should, gradients finite-difference verified to under 1e-6 — but the lesson travels: a repair fitted where its failure cannot show up is fitted to a different problem than the one it will meet, so name the split the repair was fitted on, and fit it where the failure is visible. Distinct from 'A repair that cannot change the decision', which is about what the repair can do — its safety provable from its form — here the question is where the repair is fitted, and a form-safe repair fitted on the wrong split is still the wrong repair — and from 'A test that cannot see the mistake is not a test of it', which is about a check restricted to inputs where the mistake cannot appear — here the check is fine and the fit is the thing that cannot see the failure.

- [CalibrLab](projects/calibrlab.md)

## A search that runs out of budget owes you the gap

TreeLab's whole-ensemble counterfactual search runs a best-first queue over all 32 unchanged trees, propagating forced branches and bounding each state with an exact-rational weighted-L1 lower bound from a box projection — so every search ends in one of three honest states: optimal, infeasible, or unfinished. The fixed 36-case audit crosses rows 1, 8 and 11, target bands [6,7] and [7,8], all-feature against alcohol-only policies, and budgets of 0, 128 and 4,096 expansions, and it keeps all three outcomes visible: at row 1, target [6,7], the alcohol-only search finishes with output 6.05953621031746 at cost 0.36290323, while the all-feature search at 4,096 expansions is still unfinished with objective bounds [0.01838427, 0.36290323], and the alcohol-only target [7,8] is proved infeasible. The unfinished case is the point: the incumbent cost 0.36290323 is not an optimum — the lower bound 0.01838427 says a much cheaper counterfactual may still exist — and calling the best found so far "the answer" would mislead exactly where the search is hardest, the unrestricted all-feature case that stays open while the restricted alcohol-only case closes. The scope stays narrow — 101 Python tests and five Node/real-Chrome tests, a nine-module/nineteen-CLI wheel, the live ensemble inspector and FOREST_SEARCH.md — but the lesson travels: budget exhaustion is a third answer, so report the gap the budget left, keep unfinished as a first-class status, and never let a stopped search borrow the authority of a finished one. Distinct from 'Gate the claim, report the diagnosis', which splits what is asserted from what is merely reported — here nothing is asserted about the unfinished case at all, and the gap is the report — and from 'A zero error bar is not a zero error', which is about a sampled error estimate misreporting its own uncertainty — here the bounds are exact, and the gap is a proof about the search, not an estimate.

- [TreeLab](projects/treelab.md)

## A control that cannot win is not a control

DenoiseLab's neural denoiser is measured against two controls built at full honest strength, and the controls are allowed to win — at 16 scattered missing pixels they do. The PCA ridge control fits its mean and SVD basis on fitting rows only, selects rank 16 and ridge 0.1 from ranks 8/16/32 and ridges .001/.01/.1/1 on the same validation masks the network was selected on, and infers coefficients from observed coordinates only, with ridge and output clipping — not a deliberately weak zero-filled projection. Nearest neighbor scores squared error on visible pixels only, lowest fitting index on ties, and labels are used for the split, never for fitting or prediction. On all 1,797 official UCI test digits, with error measured only on missing pixels in units normalized from [0,16] to [0,1], nearest neighbor (0.0312412) and PCA ridge (0.0317004) both beat the neural net (0.0353774) at 16 scattered missing pixels; the network is lower at 32 (0.0340515 against PCA 0.0410443 and neighbor 0.0363968); at 48 scattered the three are nearly tied (0.0546866, 0.0547961, 0.0549125); and on a 4-by-4 block the network leads (0.0649021 against neighbor 0.0650337 and PCA 0.0723497), with the pixel-mean baseline far behind in every case — and no universal ranking is inferred. The loss at 16 pixels is what makes the wins at 32 and on the block worth reporting: a zero-filled projection would have lost everywhere, and a network that "wins" against a control built to lose has proved nothing. The protocol keeps the comparison honest end to end: the official 3,823 training / 1,797 test split stays intact, a deterministic class-stratified feature-hash split gives 3,062 fitting / 761 validation rows, training hides exactly 32 randomly selected pixels per image refreshed on every presentation, and epoch 60 is selected on validation alone as validation hidden-pixel MSE falls from 0.1797185 to 0.0320862. The scope stays narrow — 27 Python tests including 200 independent gradient probes, complete refit with a test-loader prohibition and full evaluation reproduction, four Node/real-Chrome tests over all 40 public inference examples with hidden-target erasure and 320/390/1280 layouts, a seven-module/four-CLI wheel, data Alpaydin & Kaynak (1998), DOI 10.24432/C50P49, CC BY 4.0, Vincent et al. objective rather than a new algorithm — but the lesson travels: build the control as strong as you honestly can, report the cases where it wins, and a comparison that can falsify the model is the only one that can confirm it. Distinct from 'Let the baseline learn too', which is about giving the baseline the same information the method uses — here the controls see the same observed pixels by construction, and the point is they are built to full strength and allowed to win on the record — and from 'Pin the baseline, not just the result', which gates the baseline so the contrast cannot drift — here nothing is gated, the contrast is reported per case including the cases the model loses — and from 'A gain needs a control that could have produced it', which is about a null that could explain the gain — here the controls are rival methods, not nulls, and the question is whether the comparison can falsify the model at all.

- [DenoiseLab](projects/denoiselab.md)

## One residual is not a value certificate

BeliefLab's discounted certificate shows why a single Bellman residual certifies nothing about an infinite-horizon value. `certify_discounted` does not report the residual at the belief you asked about: it takes the global minimum m and maximum M of the residual T V_H - V_H over every belief, and returns the two-sided bracket V_H(b) + m/(1-discount) <= V*(b) <= V_H(b) + M/(1-discount) - a bound that holds at all beliefs because it is built from the worst residual anywhere, not the one at hand. The residual need not be convex or nonnegative, and a prescribed constant reward of 1/100 at discount 99/100 makes the point: the horizon-zero residual is 1/100 while the exact infinite value is 1, so the raw number understates the error a hundredfold, and a negative-reward control with residual -1/100 and exact infinite value -1 shows the signed direction matters. On the perfect-probe fixture - probe perfectly revealing at cost 1/10, exploit observations uninformative, discount 1/2 - the analytic infinite value is max(2*abs(2*b-1), 9/10) and satisfies the full belief Bellman fixed-point equation; at the uniform belief the horizon-three value is 13/20, the global residual range is [31/600, 1/8], the signed shifts are [31/300, 1/4], and the certified infinite-value interval is [113/150, 9/10], which contains the true 9/10. The scope stays narrow - discount strictly below one, base horizon 0-3, one planner call building through H+1 because T V_H = V_(H+1), twelve discounted-certificate tests against complete-tree oracles and Cramer-policy references, four SVG tests over the exact curve vertices, 86 tests and 81 models in total - and the certificate does not certify action optimality, finite-tree policy loss, learned-model validity or real-world safety: it certifies the value bracket, and only the value bracket. Distinct from 'A small residual is not a small error', which is about one value's residual understating one error by 1/(1-discount) - here the residual is a function over all beliefs and the certificate is its global range, a two-sided bracket rather than a corrected point - and from 'Optimal at one belief is not optimal at every belief', which maps where a fixed policy stops winning - here no policy is judged at all, only the value function is bracketed.

- [BeliefLab](projects/belieflab.md)

## An optimum is not a uniqueness proof

ClusterLab's v0.3 ambiguity audit exists because the v0.2 restart inspector had already proved the matching optimal - and optimal was not enough. A manual integer Hungarian solver supplies optimal center permutations with primal/dual witnesses, independently checked against subset-DP optima for all 220 matrices, and browser BigInt checks those exact saved rounded-cost certificates. That proves the matching is cheapest. It says nothing about whether it is the only cheapest matching, or how much cheaper it is than the next best. The v0.3 audit answers the question the optimum leaves open: 2,200 exact selected-edge exclusion witnesses, best-distinct permutations and optimal-matching counts; independent full-cost dynamic programs check all 220 gaps and counts; browser BigInt verifies all 4,000 oriented exclusions. The matching is unique in every saved real matrix - and the controls show why that needed proving rather than assuming: tied and unused-tight-edge controls produce optima that are not unique and margins that are not large, so an optimum alone proves neither uniqueness nor a large margin. All ten exclusion certificates together cover every possible replacement, without adding their overlapping solution counts, and the live inspector shows the exact optimal-permutation counts, the cheapest distinct permutation, every selected-edge exclusion and a smallest-gap control. The strict sufficient cost-entry perturbation bound is a bound on how far a cost entry can move before the optimum could change - not a sharp radius, not pixel robustness, not statistical uncertainty.

The scope stays narrow - 48 Python tests and thirteen Node/real-Chrome tests, a ten-module/six-CLI wheel, CI across Python 3.10-3.13, the same forty saved restarts (seeds 100-109, four arms, holdout ARI .662690/.665149/.669707/.665596) with fits and scores unchanged, data Alpaydin & Kaynak (1998), DOI 10.24432/C50P49 - but the lesson travels: an optimum is a claim about one candidate, uniqueness is a claim about all the others, so count the runners-up and prove the gap, or the optimum is only a winner with no margin. Distinct from 'A unique prediction does not identify a coefficient', which is about one prediction being compatible with many coefficients - here the optimum is known exactly and the question is whether it is the only one - and from 'A search that runs out of budget owes you the gap', which is about an unfinished search reporting the gap its budget left - here the search finished and the gap still has to be proved separately.

- [ClusterLab](projects/clusterlab.md)

## A sum that closes is not a correct split

DigitLab's v0.5 attribution adds baseline-relative class-logit Integrated Gradients to the unchanged UCI digit models: choose the class and a zero or fit-only mean reference, inspect all 64 signed contributions and their logit-sum residual, and keep the attack label separate. The references are explicit — all-zero, or the frozen mean of only the 3,062 fitting rows, never validation or official test rows — and neither is presumed neutral, realistic or causally meaningful; the explained quantity is a selected class logit, not a softmax probability. The 64 contributions sum to the logit difference by construction: integrated gradients integrate the gradient along the straight-line path from reference to input, so the total is the fundamental theorem of calculus, not a measurement. A completeness check that the sum closes can therefore only fail if the implementation is broken — it cannot fail on the question that matters, whether the total is split correctly among the 64 coordinates, because a permuted or redistributed split sums to the same total. The case study checks the thing the sum cannot see: independent 128-node Gauss-Legendre path integration checks individual coordinates on 40 fixed reference vectors, rather than checking completeness alone, with a saved maximum coordinate difference of 3.56e-15 and a maximum sum residual of 1.07e-14 across all 7,188 official model/reference/row cases. Those are finite numerical checks, not exact proofs, explanation-quality metrics or evidence of model trustworthiness — and changing the baseline changes both the path and the question, so the check is tied to the reference it was run against. The scope stays narrow — 78 Python tests and six Node/real-Chrome tests, 106 attribution reference vectors plus the existing 52 inference/gradient cases, four reproducible audit figures, a ten-module/ten-CLI wheel, ATTRIBUTION.md documenting the derivation, established sources, controls and limits — but the lesson travels: when a total is guaranteed by construction, check the parts, not the total, because the check that cannot fail on the split is not a check of the split. Distinct from 'A test that cannot see the mistake is not a test of it', which is about a check restricted to inputs where the mistake cannot appear — here the check runs on the full input, but the identity it verifies is true by construction, so the mistake it cannot see is a redistribution, not a hidden input — and from 'The reference is part of the question', which is about the reference defining the question — here the reference is fixed and stated, and the question is whether the split is right — and from DigitLab's own first principle 'At the boundary, the rule decides', which is about radius-infima boundary rules in the robustness audit — here the subject is attribution, not robustness.

- [DigitLab](projects/digitlab.md)

## A sufficient certificate is not a complete detector

SparseLab's Gap Safe screening extension audits an arbitrary supplied iterate with exact rational arithmetic over the stored binary64 inputs: it builds an exactly feasible residual-scaled dual vector, an exact primal-dual gap G and a sphere radius squared 2G/N, and for feature j a positive exact margin lambda-|X_j^T u| together with the strict inequality ||X_j||^2 * R_squared < margin^2 proves coefficient j is zero in every optimizer — no rounded square root, tolerance decision or coordinate dropping is used. The certificate is one-sided by construction, and the controls exist to stop anyone reading it as a detector: on a loose zero iterate at lambda=1/4 with gap 14357/8192 no feature is certified; on a near iterate with current beta_2=1/32 and gap 5/1024, feature 2 is certified zero with ball term 5/512 against squared margin 25/1024 and slack 15/1024; on an exact interior zero at lambda=1/4 with gap 0, feature 2 is certified; but on an exact boundary zero at lambda=1/8 with gap 0, feature 2 is zero yet radius=margin=0 fails the strict test, so it stays uncertified; on a duplicate-column optimum with gap 0, neither interchangeable copy is screened, because either can carry a nonzero optimum coefficient; and on a loose iterate with a zero column and gap 73/32, the zero column is certified despite its nonzero current coefficient. A separate equality control with ball term equal to squared margin at 1/4 must remain uncertified. `not_certified` never means active, useful or causally relevant — it means the certificate could not speak, and the six controls distinguish a sufficient screening certificate from current sparsity or a complete support detector. The scope stays narrow — 14 behavior checks and 3 SVG checks added for 45 tests total, 24 additional seeded designs comparing certified zeros against independent active/sign-oracle witnesses and checking exact dual-optimum containment, the new SVG checking 27 exact cells and coordinates, two squared-bound bars, full lossless report metadata and hidden-dual tampering, a six-module v0.2 wheel reproducing all four complete CLI JSON outputs outside checkout with both SVGs regenerating byte-exactly, standard Gap Safe rules due to Fercoq, Gramfort and Salmon, exact certificates applying to stored binary64-input rationals rather than unknown pre-rounding data, and no new screening theorem, causal selector, statistical guarantee, complete zero detector or solver speedup — but the lesson travels: a certificate that can only say yes is a proof about the cases it certifies, and its silence on the rest is not a verdict. Distinct from 'A unique prediction does not identify a coefficient', SparseLab's first principle, which is about one prediction being compatible with many coefficients — here the question is not what the fit identifies but what a one-sided certificate can and cannot say — and from 'Gate the claim, report the diagnosis', which is about gating a claim until the diagnosis is reported — here the certificate's silence is itself the honest output, not a missing diagnosis.

- [SparseLab](projects/sparselab.md)

## An exact audit needs an exact anchor

ScoreLab's policy-gradient audit is exact because it audits at the one point where the softmax is rational. For known state/action weights `w` and integer feature vectors `phi`, the policy is p_theta(a|s) = w(s,a) * exp(phi(s,a) . theta) / sum_b w(s,b) * exp(phi(s,b) . theta) — and at theta = 0 every exponential is 1, so p(a|s) = w(s,a) / sum_b w(s,b) and the log-probability score is phi(s,a) - sum_b p(b|s) * phi(s,b), both rational. Parameters are shared wherever their feature coordinates are used, transitions and rewards are fixed and independent of theta, and there is no floating-point softmax anywhere in the production audit. The payoff is a gradient that is a fraction, not a float: on the three-step, two-state sequential model the exact gradient is [1238843/7962624, -4477/31104], and all four estimator means equal it exactly — the audit computes the expected return and its exact derivative by a backward sensitivity recursion, then enumerates every complete positive-probability path and returns each path's probability, scores, return-to-go and gradient vector under every estimator. And the anchor's limit is stated where the anchor is: no policy training, and no claim that all nonzero-theta softmax probabilities are rational. The scope stays narrow — 1 to 3 states, 1 to 3 actions per state, 1 to 3 shared feature coordinates, weights 1..16, integer features -8..8, horizon 0..6, with booleans, floats, duplicate keys, extra fields and inputs over 64 KiB all rejected, and fractions serialized as [numerator, positive_denominator] — but the lesson travels: exact arithmetic is not a property of the code, it is a property of the point you evaluate at, so choose the point where the answer is exact and say plainly where it stops being exact. Distinct from 'The reference is part of the question', which is about the reference defining the question — here the anchor defines where exactness holds, not what is asked — and from 'A float pass at the boundary is not an exact pass', which is about a float computation failing an exact check — here nothing is computed in floats at all, and the audit is exact only because the anchor makes it so — and from ScoreLab's own first principle 'The natural baseline is not the best baseline', which is about which baseline minimizes variance — here the subject is whether the audit can be exact at all.

- [ScoreLab](projects/scorelab.md)

## An input-dependent recurrence is not a fixed convolution

ScanLab's fixed diagonal LTI recurrence equals direct causal convolution exactly — the nonzero-initial-state boundary term and the skip connection are explicit, and the equivalence is checked against an independent product expansion on 264 length/width cases and 120 fixed LTI models. The equivalence holds because the recurrence is fixed: the same decay and the same weights apply at every step, so the whole history collapses into one convolution. Add a sigmoid input gate and the collapse breaks measurably. The gate control gives a final f(2x) - 2f(x) of about 0.20243342 — not zero, not a tolerance dispute, a nonzero gap that says no single fixed linear convolution can represent the gated model on all inputs. The gate makes the recurrence input-dependent, and an input-dependent recurrence is a different model class from a fixed convolution, not a noisier instance of it.

The gated model is still fully inspectable — the separate sigmoid-gated recurrence exposes every forward state and every hand-derived parameter, input and initial-state adjoint, and streaming carries state across chunk boundaries without changing causal outputs, checked on all 64 streaming partitions — but inspectability is not equivalence, and the case study does not claim it. The 16 displayed gradient probes have maximum central-difference error about 8.419e-12, and finite differences validate fixtures, not all derivatives. The scope stays narrow — supplied tiny affine tables, width 1..8 and length 0..128, 30 tests in the original including 729 scalar composition cases, 123 independent gradient probes and all 64 streaming partitions, with rational algebra and float sigmoid arithmetic kept as separate paths and no learned-task quality, general long-context memory, GPU speed, FFT, HiPPO or Mamba/S4 implementation claim — but the lesson travels: when a mechanism depends on its input, do not ask whether one fixed map approximates it well enough; ask whether any fixed map can represent it at all, and measure the gap that says it cannot. Distinct from 'A test that cannot see the mistake is not a test of it', ScanLab's first principle, which is about restricted inputs hiding a mistake — here the inputs are general and the two model classes genuinely differ, so no wider test would close the gap — and from 'Make the fast path prove it equals the slow path', which is about two paths agreeing — here the fast path and the slow path provably disagree on the gated model, and the disagreement is the finding, not a failure of the check.

- [ScanLab](projects/scanlab.md)

## The objective you minimize is not the score you report

ClusterLab's four arms each choose their model by minimum fitting inertia among seeds 100–109 — never a test-label score. Selection and evaluation are different numbers on purpose, and the ranking between them can flip: careful k-means++ seeding reaches slightly lower raw fitting inertia (9682.7571 against uniform's 9683.1241) yet scores slightly lower on the held-out test set (ARI .662690 against .665149), so no general seeding win is claimed. The other two arms show the same split from the other side: PCA16 has the highest holdout ARI (.669707) and whitened PCA16 sits at .665596, while their NMI and silhouette move in different directions again (PCA16 NMI .740137, silhouette .224268; whitened NMI .739303, silhouette .149408; raw arms NMI .751821/.749688, silhouette .186434/.186142) — no single number orders the four arms, because each number answers a different question. Cross-geometry comparisons are not rankings at all: PCA and whitening change the distance metric, so inertia and silhouette differences across geometries are descriptive and cannot be ranked as one unchanged objective. NMI is not adjusted for chance, and no confidence interval, causal isolation or classifier accuracy is inferred; cluster IDs are groups, not digit labels, and distances are not probabilities. The scope stays narrow — 48 Python tests plus thirteen Node/real-Chrome tests, a full 40-fit reproduction that forbids test-loader access, frozen model and protocol hashes verified before evaluation opens the test file, every held-out distance, silhouette and composition reproduced, data Alpaydin & Kaynak (1998), DOI 10.24432/C50P49, CC BY 4.0 — but the lesson travels: decide in advance which number chooses the model and which number judges it, report both, and when they disagree, believe the disagreement rather than the number you optimized. Distinct from 'An optimum is not a uniqueness proof', ClusterLab's first principle, which is about whether a found optimum is the only one — here the optimum is not in question, the question is which number you let decide and which number you report — and from 'Fit the repair where the failure is visible', which is about fitting a repair on a split where its failure can show up — here nothing is fitted on the test set at all, and the point is that the fitted number and the reported number can rank the same two models in opposite directions.

- [ClusterLab](projects/clusterlab.md)

## A row left out is not a row held out

TreeLab's group bootstrap draws 2,376 fitting-feature groups 2,376 times with replacement for each tree, then expands every drawn group with multiplicity — so a row can be absent from the draw and still be in the bag. Out-of-bag has to exclude a row's entire exact-feature group, not the row alone: a four-row duplicate witness shows why row absence alone does not exclude an in-bag copy, and leaf size counts multiplicity, not unique source rows. The prefixes make the cost of getting this wrong visible — at 1, 4, 16 and 32 trees, 1,832, 482, 1 and 0 rows have no votes at all, and each prefix's out-of-bag MSE is computed on its own supported subset with a row-dependent number of trees, so it is not a fixed-set error curve and not a calibrated uncertainty interval. The same discipline governs the split itself: the v0.1 protocol hashes each parsed vector, sorts the 3,961 unique exact-feature groups and assigns the first floor(60%) to fitting, the next through floor(80%) to validation and the rest to test — target-blind, source-row-order invariant and exact-feature-group disjoint, with target conflicts kept together by construction, while near copies, unrecorded production batches and time-forward shift stay open. The 32-tree ensemble's test RMSE 0.705212 and MAE 0.545678 across 969 rows, against same-fit least squares 0.734217/0.573791 and selected CART 0.775952/0.607582, are descriptive results on the reused historical test, not a fresh blind benchmark — and the duplicate witness does not estimate real-data leakage magnitude, it only proves the mechanism by which a row-level holdout would leak.

The scope stays narrow — 57 tests and a six-module/ten-CLI installed-wheel check covering full reproduction, independent traversal, group multiplicity, missing support, corruption guards and test-target mutation, with the complete ensemble JSON, all group draws, fitting/validation/test member outputs, per-row out-of-bag votes and test predictions saved, seed 20261108 and the prefix grid [1,4,16,32] fixed before the run, validation MSE alone selecting 32 trees with no validation refit — but the lesson travels: when the unit of duplication is coarser than the unit of the row, define held-out at the coarser unit, report each error on the subset that actually supports it, and never let a row's absence from one draw stand in for its absence from the bag. Distinct from 'A search that runs out of budget owes you the gap', TreeLab's first principle, which is about a search that stops before finishing — here every search finished, and the question is what 'left out' meant in the first place — and from 'A stable value does not mean a stable strategy', which is about duplicate rows giving non-unique optimal vertices in a game — here the duplicates do not change the optimum, they change what counts as held out — and from 'A marginal is not a path', which is about per-position winners failing to form a valid joint path — here the failure is not in combining answers, it is in the exclusion itself being defined at the wrong granularity.

- [TreeLab](projects/treelab.md)

## Decreasing loss is not convergence

PartsLab's six manual nonnegative matrix factorization fits — ranks 8/16/32, seeds 11/23, 100 outer / 3 inner coordinate sweeps on all 3,823 original UCI training digits, no labels — all lower their loss through the run, and all six exhaust their fixed stationarity budget without meeting joint stationarity tolerance. Every scalar coordinate step minimizes its own nonnegative quadratic, with zero-curvature flat directions handled without a denominator epsilon, and finite differences verify the gradients — yet a falling loss is not convergence, not global optimality, and not even a demonstrated local minimum. The same data, the same objective family, shows what convergence actually looks like when the problem allows it: freeze the basis and the coefficient solve is convex nonnegative least squares, and every official test row meets the numerical per-row KKT threshold in every saved run. An arbitrary input may instead exhaust 1,000 sweeps and is marked unfinished, not rounded up to an answer. And the optimizer, not the objective, can decide whether the loss moves at all: a plain multiplicative-update control with target [1,1], identity basis and initial coefficients [1,0] stays at loss 0.5 with a blocked gradient of -1, while coordinate minimization reaches zero on the same objective — the zero-locking is in the update, and only the control isolates it.

The scope stays narrow — 30 Python tests plus eight Node/real-Chrome tests, 35 support-enumerated NNLS optima checked against a separate active-set oracle, native and browser decompositions agreeing on all 120 model/example pairs, real Chrome checking all 2,048 pixels in the 32-part contribution grid, an eight-module/seven-CLI installed wheel reproducing all six fits and held-out scores, data Alpaydin & Kaynak (1998), DOI 10.24432/C50P49 — and no superiority claim is made, since rank-matched signed PCA and SVD beat NMF on test MSE at every fixed rank (rank 8: 0.0309683 vs 0.0251267/0.0257206; rank 16: 0.0163996 vs 0.0118776/0.0119639; rank 32: 0.0046791 vs 0.0027689/0.0027681, against a training-mean baseline of 0.0735163). The v0.2 certificate keeps the same discipline on the other side: exact binary64 primal/dual arithmetic with outward-rounded objective intervals and portable JSON proofs bounds the frozen-basis objective — half squared error, not per-pixel MSE — while a residual-shift bound can stay loose and even zero gap does not imply unique coefficients, since positive rescaling, shared permutations and duplicate basis rows preserve a reconstruction. But the lesson travels: report the stopping rule and the certificate next to the loss curve, because a loss that falls proves only that the optimizer moved, not that it arrived — and when the budget runs out first, say so, the way the unfinished arbitrary input is marked, instead of letting a downward curve stand in for a converged fit. Distinct from 'A search that runs out of budget owes you the gap', TreeLab's first principle, which is about a search that stops before finishing and owes the gap it left — here every fit ran its full budget and the loss fell throughout, yet stationarity was never met, so the run finished and the fit did not converge — and from 'A sufficient certificate is not a complete detector', SparseLab's second principle, which is about a certificate staying silent on coefficients it cannot clear — here the certificate is exact but bounds the objective, not the parts, so convergence and certification are separate questions with separate answers — and from 'Check a hand-derived gradient against finite differences', which is about a falling loss not proving the derivatives right — here the gradients are verified and the loss still falls without the fit converging.

- [PartsLab](projects/partslab.md)

## Score only what was missing

DenoiseLab's neural denoiser, PCA ridge and nearest neighbor all copy the visible pixels unchanged — the only thing any of them has to produce is the erased part — so the audit scores mean squared error only on the missing pixels, averaged over all 1,797 official UCI test digits in units normalized from [0,16] to [0,1]. Score all 64 pixels instead and the 48 visible ones contribute exactly zero to every method, diluting every error by the missing fraction: at 16 scattered missing pixels the neural net's 0.0353774, PCA ridge's 0.0317004 and nearest neighbor's 0.0312412 would all be quartered to 0.0088444, 0.0079251 and 0.0078103, and the 0.0041362 gap that puts the neighbor ahead would shrink to 0.0010341 — the same ranking, with the differences that decide it compressed fourfold. The dilution is not uniform across cases either: at 48 scattered pixels the factor is three-quarters, so a single all-pixel score would weight the 16-pixel case a quarter as heavily as the 48-pixel case for no reason except how many pixels happened to be erased. The honest table keeps each case on its own missing-pixel scale — the network lower at 32 scattered pixels (0.0340515 against PCA 0.0410443 and neighbor 0.0363968), nearly tied at 48 (0.0546866, 0.0547961, 0.0549125), and ahead on the 4-by-4 block (0.0649021 against neighbor 0.0650337 and PCA 0.0723497) — with the pixel-mean baseline far behind in every case, and no universal ranking inferred. Training hides exactly 32 randomly selected pixels per image, refreshed on every presentation, and epoch 60 is selected on validation alone as validation hidden-pixel MSE falls from 0.1797185 to 0.0320862, so the selection and the score both stay on the hidden part.

The scope stays narrow — 27 Python tests including 200 independent finite-difference gradient probes, complete refit with a test-loader prohibition and full evaluation reproduction, four Node/real-Chrome tests over all 40 public inference examples with hidden-target erasure and 320/390/1280 layouts, a seven-module/four-CLI installed wheel, 14,544 learned parameters in a 64/16/64 tanh network with 64 sigmoid outputs, data Alpaydin & Kaynak (1998), DOI 10.24432/C50P49, CC BY 4.0, Vincent et al. objective rather than a new algorithm — and one seed and one mask per image and case, with no repeated-sample confidence interval, so the per-case gaps are reported as they are, not as significance claims. But the lesson travels: score the part the method actually had to produce, because every trivially-correct component you include in the denominator is a weight that dilutes the differences you are trying to measure — and when the easy part dominates the score, a model can look close to perfect while still failing at the only thing it was asked to do. Distinct from 'A control that cannot win is not a control', DenoiseLab's first principle, which is about whether the rival methods are built strong enough to beat the model — here the rivals are already honest and the question is what the score itself counts, before any comparison is made — and from 'The objective you minimize is not the score you report', ClusterLab's second principle, which is about the fitted number and the reported number ranking the same models in opposite directions — here the reported number is the right family, only computed over the wrong pixels, so the score's denominator, not the choice of score, is what has to be defended — and from 'A sum that closes is not a correct split', DigitLab's second principle, which is about a completeness identity that holds by construction whatever the split — here nothing sums to a total, the error is real, it is only diluted by pixels the method never had to fill in.

- [DenoiseLab](projects/denoiselab.md)

## A reconstruction does not identify the parts

PartsLab's six nonnegative factorizations — ranks 8/16/32, seeds 11/23, 100 outer / 3 inner coordinate sweeps on all 3,823 original UCI training digits, no labels — reconstruct the digits well: at rank 32 the held-out test MSE is 0.0046791 against a training-mean baseline of 0.0735163, and the lowest reencoded training MSE selects the restart within each rank before a frozen model/protocol hash is verified and the 1,797-row official test file is opened. But the reconstruction is not the parts. Rescale a factor up and its coefficients down by the same amount, permute the basis rows and the coefficients together, or duplicate a basis row and split its coefficient between the copies, and the reconstruction is exactly unchanged while the parts are different. Unit-L2 basis normalization fixes a display scale only. So a basis image that looks like the stroke of a 7 is a way of displaying the fit, not a meaning the fit discovered: the basis is not a learned semantic digit label or a causal explanation, and nothing in the fit says which of the many equivalent decompositions is the real one.

The exact certificate does not close that gap, because it was never a certificate about the parts. The v0.2 fixed-basis certificate proves the objective with exact binary64 primal/dual arithmetic, outward-rounded intervals and portable JSON proofs checked by an independent Python Fraction verifier — eighty exact rational active-set optima and all 120 cross-language witness references, twenty public examples across six models — and the live browser verifies its own candidates, including zero-sweep unfinished solves, accepting valid pasted proofs and rejecting tampered ones. But the bounds are half squared error rather than per-pixel MSE, a residual-shift bound can stay loose, and even a zero gap does not imply unique coefficients. The certificate answers how good this reconstruction is; it stays silent on whether these are the parts, because the objective it bounds cannot see the difference between equivalent decompositions.

The scope stays narrow — 30 Python tests plus eight Node/real-Chrome tests, 35 support-enumerated NNLS optima checked against a separate active-set oracle, native and browser decompositions agreeing on all 120 model/example pairs, real Chrome checking all 2,048 pixels in the 32-part contribution grid, an eight-module/seven-CLI installed wheel reproducing all six fits and held-out scores, data Alpaydin & Kaynak (1998), DOI 10.24432/C50P49, CC BY 4.0 — and no superiority claim is made, since rank-matched signed PCA and SVD beat NMF on test MSE at every fixed rank (rank 8: 0.0309683 vs 0.0251267/0.0257206; rank 16: 0.0163996 vs 0.0118776/0.0119639; rank 32: 0.0046791 vs 0.0027689/0.0027681). But the lesson travels: when many decompositions give the same reconstruction, do not present one of them as the explanation — report the reconstruction you can bound and say plainly that the parts are a representation, not a meaning, because a bound on the reconstruction is not a bound on the parts. Distinct from 'A unique prediction does not identify a coefficient', SparseLab's first principle, which is about one prediction being compatible with many coefficients — here the reconstruction is exact and fully determined, and the question is not which coefficients the data identify but whether any of the equivalent decompositions means something — and from 'Decreasing loss is not convergence', PartsLab's own first principle, which is about whether the optimizer arrived at all — here arrival is not in question, the six fits ran their full budgets and the frozen-basis solves meet their per-row KKT thresholds, and the point is what the arrived-at parts signify — and from 'A sufficient certificate is not a complete detector', SparseLab's second principle, which is about a one-sided certificate staying silent on features it cannot clear — here the certificate is exact and complete about the objective, and its silence about the parts is not a gap in the certificate but a property of the objective itself.

- [PartsLab](projects/partslab.md)

## A cheaper sampler is not the same sampler

DiffuseLab's one trained noise predictor — a 7 -> tanh(48) -> 2 network with 482 learned parameters, exact MSE gradients and minibatch Adam — is reused across DDPM and DDIM with no retraining and no checkpoint change, from the same 256 initial latents. DDPM at 64 steps makes 64 predictor calls per sample and reaches 60.55% of samples within 0.4 of a center, all eight neighborhoods, with a symmetric nearest-neighbor squared distance of 0.037103 against the fresh reference set. DDIM with eta=0 at 8 steps makes 8 calls — 87.5% saved — reaches 61.72% within 0.4 and still covers all eight modes, but its symmetric distance is 0.210661, about 5.7 times worse. Sixteen steps gives 0.188649, and even the full 64-step eta=0 run gives 0.175727 (62.89% within 0.4) against DDPM's 0.037103: the same step count does not give the same sampler, because DDPM adds step noise at every step and eta=0 adds none. The only exact match is full-grid eta=1, which agrees with DDPM arithmetic up to floating point on matched draws. The near-center fraction improving — 61.72% against 60.55% — does not establish better samples; every DDIM arm is worse on the symmetric distance, and the comparison shows all of them rather than a selected winner.

The scope stays narrow — eight equally likely centers on a radius-2 circle with isotropic noise SD 0.12; 1,024 training points (seed 31) and 256 fresh reference points (seed 37); network seed 7, training draws seed 8, sample seed 17; the 8/16/64 grids and eta=0 fixed for the comparison with no setting or seed search, and the fixture visible during development, not an untouched benchmark. Call savings count actual scalar predictor invocations — 256 samples times the listed calls per sample — not measured runtime, FLOPs, memory or quality equivalence. Thirty-three tests cover all-parameter central finite differences, independent posterior-mean algebra, DDPM/DDIM equivalence, skipped-step formulas and counted predictor invocations, and the terminal alpha-bar is about 0.006123, not zero, so starting from a standard normal is an approximation to the finite forward marginal. Equations from Ho, Jain and Abbeel (2020) and Song, Meng and Ermon for DDIM; no walltime speedup, image-generation or general ranking claim.

But the lesson travels: cost and fidelity are separate axes, and a saving on one does not imply equality on the other — report the calls saved next to the distance that got worse, because a sampler that is cheaper and different is a different sampler, not a free optimization. When the cheap version changes the answer, say what changed and how much, instead of letting the flattering fraction stand in for the whole comparison. Distinct from 'Choose the metric the failure cannot pass', DiffuseLab's first principle, which is about a one-sided metric letting a collapsed generator pass — here the near-center fraction actually improves for the cheaper sampler, so no metric was gamed; the procedure itself changed the samples, and the symmetric distance is what shows it — and from 'Make the fast path prove it equals the slow path', the KVLens/SpecLab principle, where the fast paths prove equality by construction or by invariant — here the fast path was checked and does not equal the slow path even at the same step count, so the savings are reported as savings with a measured quality change rather than as a free equivalence — and from 'A narrower window is a new distribution', FlowLab's principle, which is about an evaluation window renormalizing the mass it measures — here nothing is rewindowed or renormalized, the model and the initial latents are identical and only the reverse discretization changes, yet the samples still move.

- [DiffuseLab](projects/diffuselab.md)

## A running interval must remember what it excluded

A confidence sequence is an interval over time, and the time part is the claim: an exclusion earned on the evidence so far has to survive later evidence pointing the other way, or the sequence is only ever as strong as its latest prefix. BetLab's v0.3 confidence-sequence inversion builds the interval from a fixed wealth process — for each candidate mean m in [-1,1] the factors are 1+b·(D−m)/2 with fixed normalized mixtures, and monotone wealth makes the accepted set an interval — and it keeps the memory explicitly: running intersections retain earlier exclusions after reversal. Eight +1 differences then twelve −1 retain the earlier interval [1273/2048, 1] even while the current-prefix inversion weakens, because the exclusion was earned and the reversal does not un-earn it.

The inversion is exact, not approximate. Rational bisection retains component-level crossing and noncrossing witnesses and every midpoint comparison, without claiming that generally algebraic roots are rational; sixteen bisections bound the running-boundary uncertainty by 1/32768. With bet one and alpha 1/4, twenty-four repeated differences of 1/2 give the boundary bracket [12487/32768, 1561/4096] and the conservative closed interval [12487/32768, 1]. The coverage is checked the same way the betting test is checked: an eight-round sign law with positive probability 3/4 and constant conditional mean 1/2 enumerates all 256 paths, and ever-exclusion and true-mean crossing probabilities are both 2187/16384, below alpha 1/4, with every conditional mixture slack zero and final and stopped expectations one. And the inversion costs no multiplicity correction — candidate-mean inversion does not require a union bound over means, because one fixed wealth process is inverted at each candidate — but model, stream and scoring-rule selection are still uncorrected, and the interval is not a drifting-mean, causal-effect or two-sided estimate.

The scope stays bounded: up to 64 observations, 16 fixed bets and 1..32 bisections, the seven older CLI fixture outputs byte-identical, the seven-module wheel matching all ten complete CLI outputs outside checkout, and a 67-test suite including exhaustive independent products, brackets and trials on 81 ternary streams, exact endpoint and midpoint ties, refinement, reversal and prefix-only behaviour, all 256 coverage paths and full capacity, with the new figure checked at 92 coordinates, seven cells, full metadata and hidden-leaf tampering. But the lesson travels: a running interval that only reports its latest prefix forgets what it already proved — keep the intersection, because an exclusion that disappears when the data turns is not a confidence sequence, it is a snapshot. Distinct from 'A free restart is not optional stopping', BetLab's first principle, which is about whether a ruined test may be restarted — here nothing is restarted, the test runs once and the question is whether its interval keeps what it excluded — and from 'Record the when, not just the what', which is about timestamps in the record — here the memory is in the interval itself, an earlier exclusion retained as a bound rather than a date on a row — and from 'Keep the exact answer next to the approximation', which is about exactness beside approximation — here exactness is the mechanism, bisection with witnesses, and the claim is about the running interval's memory, not about which answer is exact.

- [BetLab](projects/betlab.md)

## A deletion is defined by what you hold fixed

'Delete row 5' sounds like one operation. On InfluenceLab's seven-row fixture it names three different computations with three different answers for the same query loss. The actual fixed-N numerical refit — holding the original normalizer 7 and ridge 0.1 fixed — moves the query loss by +0.305655. Refitting on the retained-row mean with the same ridge 0.1 gives +0.317231. A damped inverse with delta 0.5 gives +0.119499. None of these is the wrong one; they answer different questions, and the words 'delete row 5' do not say which question was asked until the held-fixed quantities are named.

The equivalences are exact where they hold, and they hold only where stated. Fixed-N deletion equals retained-mean deletion with ridge multiplied by N/(N-1) — 7/6 here, since N is 7 — and does not equal it with ridge left unchanged. Adding 0.5 to the inverse Hessian is likewise not refitting a ridge-0.6 model: the original optimum and gradients stay fixed, so the damped answer is a different object from a refit, not an approximation to one. The linear fixed-N prediction, +0.203204, is a fourth number again — a derivative at the base fit, not any of the three refits — and the gap between it and the refit is a separate fact from the gap between the refits themselves.

The scope stays narrow — seven synthetic rows, query (1,2) with label 1, ridge 0.1, original normalizer 7, theta approximately (-0.275488,0.220249), query loss 0.614042; all 15 base/deletion numerical fits converged to a maximum absolute gradient of at most 8.197e-11, with undamped influence solves at most 5.551e-17 residual; 43 tests, two reproducible SVGs, five-module wheel parity, and no causal attribution, privacy deletion or machine-unlearning guarantee — but the lesson travels: before reporting what a deletion did, state the normalizer and the regularizer you held fixed, because the same sentence describes different computations with different answers, and an effect size without its held-fixed quantities is not a result, it is a riddle. Distinct from 'A group deletion is not the sum of its single deletions', InfluenceLab's first principle, which is about the linear prediction missing the refit and single deletions not adding to the group deletion — here every number compared is itself an exact refit or an exact equivalence, and the question is which refit the words name, not whether the prediction matches one — and from 'A local metric does not certify a finite step', which is about a verified local quantity failing to certify a finite step — here nothing is local, the ambiguity is between three finite refits that differ only in what they hold fixed.

- [InfluenceLab](projects/influencelab.md)

## A set is a coverage claim, not a probability claim

A prediction set promises coverage, not confidence in any one label — and SetGuard builds the set so the promise is exactly what the rank says, nothing more. For n calibration scores the rank is k = ceil((n+1)(1−alpha)), the k-th smallest score is used without interpolation, alpha's decimal representation is converted to a Fraction before the ceiling, and the exact score comparison is repeated at prediction so no subtraction-based p-threshold rewrite introduces another floating boundary. When k = n+1 the threshold is an all-label sentinel. All equal scores at the threshold are included, which makes ties conservative; empty sets remain empty; and there is no randomized upper-coverage claim. On the development fixture — 200 calibration rows (seed 11), 2,000 test rows (seed 29), target 0.9 — the observed coverage is 0.9235 at mean set size 3.017 while the argmax accuracy is 0.496: the set covers nine times in ten while the single best guess is right about half the time, and that gap is the point of the set, not a defect in it.

The rank itself is audited, not assumed. Leave each score position out once, threshold the others and count inclusion: for every finite multiset the count is at least k among n+1 positions. The demo's distinct-score sequence covers 19 of 21 positions, and exhaustive tests cover 243 five-position sequences with tied scores at five alpha values. That audit checks deterministic rank mechanics only — it cannot establish exchangeability, training/calibration independence or a population guarantee from one dataset, and the case study says so. v0.2 makes every inclusion inspectable: five fixed public synthetic cases with a live rank ledger, 95 case/alpha witnesses, 160 independent Fraction games, 80 integer-grid games, 4,199 pooled positions, 8,341 pooled/classwise deletion records and 2,736 candidate-label decisions, with Python Fraction and JavaScript BigInt rationals checked independently and an installed wheel reproducing the original demo and all 95 witnesses outside the checkout, importing six modules and executing six CLI commands. The same honesty carries into the optional label-conditional mode: classwise thresholds use only calibration rows whose true label is that class, in a version-2 artifact, and absent classes or classes with too few rows for the requested rank get a null threshold and are always included, with no pooled fallback. On the same fixture the class counts are [43, 37, 50, 35, 35]; classwise empirical coverage is 0.9285 at mean size 3.1095 against pooled 0.9235 at 3.017 — and class d's realized coverage is only 0.8859, below the 0.9 target, reported as a finite-split fact rather than hidden. One split does not prove or refute the population theorem, and it is not evidence that classwise mode always improves coverage or size.

The scope stays narrow — 41 Python and four Node/actual-Chrome tests, offline CI on Python 3.10–3.13, standard split-conformal from Angelopoulos and Bates, supplied classifier probabilities plus calibration labels in a versioned JSON artifact whose class names and order must match at inference — but the lesson travels: report the set's coverage, its size and the rank it came from, and never read a 0.9235 coverage as a 92% chance on this row. The guarantee is marginal over calibration and future test data, not conditional on a particular split, class or input; empirical coverage can fall below target; tuning alpha, the score or the model after inspecting calibration or test data invalidates a naive application of the bound; and the artifact validates schema, rank and boundary consistency but carries no signed provenance, so an altered-but-valid threshold changes behavior and the artifact belongs with its model version and data lineage. Distinct from 'A guarantee is a contract with its assumption', SetGuard's first principle, which is about the exchangeability assumption the guarantee rests on and the shifted arm that breaks it — here the guarantee holds and the question is what the construction itself promises, rank, ties and empty sets included, not what breaks it — and from 'A mean is not the distribution', which is about a summary hiding the shape of what it summarizes — here the coverage number is a marginal average and the set's size, rank and per-class shortfall are reported alongside it rather than averaged away — and from 'Keep the exact answer next to the approximation', which is about exactness beside approximation — here the exact Fraction ceiling and repeated score comparison are the mechanism, and the claim is about what the resulting set does and does not promise.

- [SetGuard](projects/setguard.md)

## A reveal on an impossible history costs nothing

A conditional failure costs only what the mass reaching it can pay — and PrivacyLab's adaptive extension makes the weighting exact. At every node of a history-conditioned mechanism tree the caller supplies the next-output distribution given the secret and the entire transcript, and all histories are required, including impossible ones. For each directed neighbor pair a substochastic kernel clips each local probability to min(K_P, t_i·K_Q); good mass flows down the tree without normalization, leaf mass g sits below both P and TQ, and the telescoping deficit 1−sum(g) bounds the actual joint delta. The fair branch charges conditional delta 1 only to incoming mass 1/2, so its actual delta is 1/2 while the uniform and additive bounds both charge 1. And a reveal on a history that cannot happen costs nothing at all: the 'Reveal only on an impossible history' tree has actual delta 0 and clipped bound 0 at T = 1, against uniform and additive bounds of 1 — the impossible node still gets its conditional audit, but no mass flows through it, so no mass is killed.

The same weighting is what makes the shared-coin joint exact rather than merely bounded: reproduced by its true conditional laws, after A the release B = A XOR secret is deterministic and revealing, and its marginal privacy cannot substitute for that conditional guarantee. The maximum directional deficit is at most 1−∏(1−d_i), each d_i the worst conditional delta across all histories and listed directions, itself at most the clamped additive sum — but a bound that charges every conditional failure in full is an upper bound, not the answer: the clipping bound can be strictly looser than the actual profile, as the independent factor-one row shows with actual delta 1/2 against a clipped bound of 3/4. Fixed round factors multiply to T; they are not adaptively selected epsilon parameters, and the code cannot verify that an outside sampler really follows the supplied conditional laws.

The scope stays narrow — 46 tests retaining the original 29, adding 14 adaptive-behavior tests plus three SVG tests; 24 seeded three-round, three-secret trees checked against independent recursive path enumeration and exhaustive all-256-event searches per directed pair; limits of six rounds, eight outcomes per round, 64 transcripts, 128 conditional nodes and 512-bit constructed probability/flow components; both figures regenerate byte-exactly and the six-module wheel matches all four complete CLI JSON outputs outside checkout — but the lesson travels: charge a failure by the mass that can reach it, and never let a bound that ignores reachability stand in for the actual cost. Distinct from 'Marginals do not compose when randomness is shared', PrivacyLab's first principle, which is about a joint release being worse than its marginals because one shared coin couples two releases — here the joint is audited conditionally, and the question is what each conditional failure costs once the mass reaching it is counted — and from 'A running interval must remember what it excluded', which is about a confidence sequence retaining earlier exclusions as bounds — here nothing is retained as a bound; mass that never arrives is simply never charged, and the bounds that charge it anyway are loose, not wrong about the conditional.

- [PrivacyLab](projects/privacylab.md)

## Likelihood is not identity

A mixture that fits better does not know more about what the clusters are — and MixtureLab keeps the score and the identification separate so the gap stays visible. On UCI Wine, Aeberhard & Forina (1992) — 178 chemical analyses, 13 features, the cultivar target stripped before any splitting, fitting or scoring — a fixed label-free split of 106 training, 36 validation and 36 test rows, training-only scaling, both covariance families, k in {1,2,3,5} and three fixed seeds give 24 fits, with the covariance floor fixed at 0.05 in squared standardized units. Training likelihood picks each restart, validation NLL picks the configuration, and test scores open afterward with no validation refit. The validation pick, Diagonal k=5 seed 11, scores 13.40992 / 13.45753 / 15.34782 across train, validation and test; the best training configuration, Full k=5 seed 23, reaches 10.20168 on training and falls to 17.95955 / 18.47913 on validation and test — more capacity buys training density and spends test density, on one small historical split that shows no general superiority and no statistical significance.

The identification was never in the likelihood. The fitted-Gaussian control, Full k=1 seed 11 at 14.40496 / 14.99046 / 15.72686, is a single Gaussian, not a discovered category; the controls show unconstrained covariance collapse, label permutation and duplicate-component nonidentifiability — the same density from components that cannot be told apart — and the far-input control shows a nearly certain within-model posterior accompanying very low density, so a posterior is not a cultivar probability, not a calibrated certainty and not a chemical identity. The 90% PCA contours are two-dimensional marginals of the model, not full-dimensional decision regions or measured coverage. What the likelihood does identify is the fit itself: every EM update keeps the old posterior and records mean likelihood gain = complete-data Q gain + posterior KL, the precision-space KKT conditions for the constrained M-step — covariance clipped at C ≥ 0.05I, not 0.05I added — are checked numerically on 100 random scatters against 40 analytic 2D clipping references, and all 24 fits meet the stated likelihood-increment tolerance, which is not a stationary-point test and not a global-optimum certificate.

The scope stays narrow — 36 Python tests and eight Node/real-Chrome tests, 1,424 native/browser density evaluations (eight models × 178 source rows), a ten-module wheel running all seven CLI commands outside checkout, no cultivar prediction, wine-quality score, calibrated uncertainty, identified latent cause or population-wide conclusion — but the lesson travels: report the likelihood as a property of the fit, and never let a lower number stand in for knowing what the mixture's components are. Distinct from 'A unique prediction does not identify a coefficient', which is about one optimum that is still a continuum of coefficients — here the optimum is not the issue, the score itself improves while the identification gets worse — and from 'A reconstruction does not identify the parts', which is about many decompositions giving the same reconstruction — here there is one fitted density and the question is what its components mean, not whether the decomposition is unique — and from 'Label what the data cannot identify', which is about a row the data cannot speak about, labeled rather than averaged in — here the data speaks fluently, the likelihood moves, and the categories stay unidentified anyway.

- [MixtureLab](projects/mixturelab.md)

## A stopping rule is not a mode certificate

MixtureLab's v0.2 geometry extension turns a fitted mixture into something you can climb: the page computes all 13 input-score coordinates, the complete 13x13 Hessian, the kx13 component-posterior Jacobian and original-unit transforms, and a normalized-gradient line search accepts only an actual log-density gain at least 0.0001 times step length times gradient norm, retaining every accepted point and stopping explicitly on norm, budget or line-search exhaustion. Eight traces start from the same already-public input at budget 128: the four diagonal models and full k=1 reach the norm criterion; full k=2,3,5 remain budget-exhausted. No mode is certified — and that is the honest statement, because the two ways the search can end certify nothing on their own: a budget stop says the search ran out of steps, and a norm stop says only that the gradient at the stopping point is small.

The control that makes the point unmissable is a landscape with no mode at the stopping point at all. Two equally weighted unit Gaussians at -2 and +2 have zero input gradient and curvature +3 at zero, so the routine stops there — at a strict minimum, the worst point in the landscape for a mode-seeker — and the norm rule cannot tell it from a mode, because a zero gradient is equally necessary for a maximum, a minimum and a saddle. A perturbed start moves away; a single Gaussian and duplicate-component controls check closed forms. The gradient norm measures the slope where you stopped, not the kind of point you stopped at, and a search that stops on a small gradient has reported a stopping condition, not a discovery.

The scope stays narrow — 312 all-coordinate finite-difference probes, every posterior-Jacobian and Hessian column, 50 scalar directional second differences, affine/rotation/permutation checks, 40 complete native/browser geometry cases and eight trace references; the final suite has 36 Python and eight Node/real-Chrome tests, a ten-module wheel running all seven commands outside checkout, and all original models, split, scales and scores byte-for-byte unchanged — but the lesson travels: when a method's stopping rule is the only thing standing between a point and a claim about that point, test the rule on a point you already know is wrong, and report the stop as a stop, not as a certificate. Distinct from 'Optimizing the bound is not recovering the marginals', VariLab's principle, which is about a coordinate fixed point that is a saddle rather than an ELBO maximum — there the stopping observation supports a point about the bound versus the marginals, and the fixed point is almost a maximum; here the stopping rule is the subject, the routine halts at a strict minimum, and three real traces never reach the rule at all — and from 'A search that runs out of budget owes you the gap', TreeLab's first principle, which is about an unfinished search reporting the gap it left — here the budget-exhausted traces are reported as unfinished, but the principle's center is the traces that did stop, whose norm stop certifies nothing — and from 'Likelihood is not identity', MixtureLab's first principle, which is about a score improving while the identification gets worse — here no score is being chased, the question is what a stopping point proves.

- [MixtureLab](projects/mixturelab.md)

## Coarsening a signal costs exactly its slacks

A garbling is not "less information" in the abstract — Correlab measures what a coarser signal costs, exactly. In the v0.2 private-signal model a trusted executor retains the hidden baseline action, the player sees only a supplied private signal and may pass or override, and the opponent is left at its baseline action: an explicit unilateral decision model, not a correlated equilibrium of a changed game. A supplied post-garbling retains both audits and lifts an optimal coarse policy through the garbling, returning exact nonnegative per-signal slacks that sum to the information loss. The loss is a sum of named per-signal terms, not a single number taken on trust — each signal contributes its own slack, and the parts add up to the whole.

The two ends of the spectrum pin the scale. Identity signals recover the full-swap gain and identical-row channels recover the clipped coarse gain, so a garbling sits between two audited endpoints rather than in an unmeasured middle. The controls make the ordering concrete: all deterministic own-action partitions through four actions are audited independently for each player, with every strict refinement relation and Bell counts 1, 2, 5, 15; a developed cyclic control gives row gains 0, 4/3, 5/3, 1, 2 across partitions 000, 001, 010, 011, 012, so three two-signal partitions can differ; and the attributed Roth control yields 0, 11/120, 11/60, 11/30 as C's reveal probability rises 0, 1/4, 1/2, 1. More revelation is worth exactly what the audit says — and every signal/action retains its exact joint-cell contributions, conditional gains, zero-mass nulls, all optimal choices and an attaining policy, so the price of each signal can be checked, not just the total.

The scope stays narrow — 50 tests in v0.2, including independent enumeration for 8,505 channel audits, 28 larger and rectangular four-signal controls up to 625 policies per player, 243 supplied post-garbling lift certificates and all 16 signal-alphabet size pairs checked by direct lift simulation, with three SVG tests binding 25 numeric cells and all seven complete CLI outputs matching an installed seven-module wheel outside checkout; the original three CLI outputs and old SVG are unchanged — but the lesson travels: when a system coarsens what an agent can observe, ask for the loss per signal, not a single information number, and check that the parts sum to the whole. There is no simultaneous override outcome, global stochastic-channel optimization, universal Blackwell-order search, privacy, learning or agent-safety claim, and six additional source notes distinguish single-agent value from strategic welfare. Distinct from 'A recommendation changes the deviation', Correlab's first principle, which is about which deviations the audit allows — here the audit is fixed and the question is what coarsening the observation costs — and from 'A narrower window is a new distribution', which is about an evaluation window renormalizing the mass — here nothing is renormalized; the garbled channel is audited as supplied and the loss is decomposed per signal rather than averaged away — and from 'Marginals do not compose when randomness is shared', which is about a joint release being worse than its marginals because one shared coin couples two releases — here there is one channel at two resolutions, and the accounting is exact rather than a bound.

- [Correlab](projects/correlab.md)

## A suggestion is not an evaluation

KernelLab's `suggest` returns a proposal, not a result. It deterministically maximizes expected improvement over a finite candidate pool — 1 to 128 unique rows, exact binary64 matches to training rows excluded, duplicates rejected as errors — and audits every candidate's score, but it evaluates no objective, spends nothing, calls no service and changes no model. The proposal carries its index, row, mean, latent variance and EI; when every eligible EI is zero the first eligible candidate is still returned, which is a tie-break, not a convergence claim, and when the whole pool is known the answer is `status="exhausted"` with a null suggestion. A suggestion is a ranked next step to take, not a measurement already made.

The numbers that look like results come from a different step: actually executing the suggestions. The offline demo maximizes sin(2x)+0.4cos(5x)−0.05x² on an 81-point grid over [−4, 4] at step 0.1, giving each policy the same three starting indices (0/40/80) and six more evaluations — nine total — with EI at fixed length 0.7, signal variance 1, noise 0, jitter 1e-8, prior mean 0 and xi 0.01. EI finishes at 1.045544 at x=−2.5, simple regret 0.000163; farthest-point space filling reaches 0.972762 at x=1, regret 0.072944; uniform random (seed 29) reaches 0.646233, regret 0.399473. The grid oracle, 1.045706 at x=−2.4, is computed only after all policies finish, for reporting, never for selection — and the controls choose their next points without using target values at all. The comparison is fair because the pool, the budget and the starts are identical; change the objective, the priors, the seed, the budget or the pool and the ranking can reverse, and the case study says so. No statistical, universal-speedup or continuous-global-optimum claim follows from one toy demo, and `suggest` is not a noisy-EI method, a batch acquisition optimizer or a safe autonomous experiment runner — only the built-in offline demo executes its public toy objective.

The scope stays narrow — 43 Python tests and four Node/Chrome tests, dependency-free Python, a fit/predict/response JSON CLI, a reproducible SVG and Python 3.10–3.13 CI; the EI formula itself is delta·Φ(delta/σ)+σ·φ(delta/σ) with delta=mu−b−xi, and at zero variance the exact deterministic limit is max(delta,0), not an unconditional zero — but the lesson travels: keep the proposal and the measurement in separate columns, because a method that only ranks candidates cannot be credited with the outcome of running one, and a comparison that spends the same budget on every policy is the only one that can rank policies at all. Distinct from 'Name the numerical assumptions', KernelLab's first principle, which is about the stabilizers and priors declared before any computation — here the declarations are fixed and the question is what the suggest API's output is, a proposal awaiting execution — and from 'Hold the distribution fixed and vary only the strategy', which is about comparison design — here the shared pool and budget are the control that makes the suggestion/evaluation distinction measurable, not the claim itself — and from 'A search that runs out of budget owes you the gap', which is about an unfinished search reporting what it left — here the search finishes with a suggestion, and the gap is between proposing a point and evaluating it.

- [KernelLab](projects/kernellab.md)

## A valid proof does not authenticate its source

MarginLab's v0.2 extension starts from a defect in the saved model: the original floating-point coefficients carry nonzero exact signed dual mass. It converts their represented binary64 inputs to Fractions, clips to the box, and reduces coefficients in the excess class until the equality is exactly zero — recording the original residual and total movement, without changing the original model. A separate exact feasible primal and a repaired feasible dual then enclose each represented linear training optimum. The approximate gap readouts for C=.01, .1, 1, 10 are 7.97e-8, 1.42e-6, 2.90e-5 and 3.23e-4 — but those decimals are not the bounds; the full canonical objective ratios are. Two independently implemented readers, Python Fraction and browser BigInt, check all constraints, objectives and repair accounting without importing the optimizer, and 60 additional active-face exact optima must lie inside the produced intervals. The browser checks all four full proofs against every original standardized input, label, C, coefficient and bias.

The control that separates the two checks is a changed inactive row: its proof can remain mathematically valid for its changed declared problem while source matching rejects it. Proof validity does not authenticate data or authorship. And the bound itself is narrow by construction: it is a bound for the represented standardized linear problem, not exact real-number standardization, RBF kernels, generalization error, clinical reliability, or a claim that an exact optimum was attained. The original numerical inspector stays numerical; no prediction, score, split, pair history or original figure changes. The same separation runs through the v0.1 controls: four separable one-dimensional points reach 100% training accuracy after one pair update while the optimization gap is still 2/3; opposite labels at an identical input give zero pair curvature and require endpoint comparison; duplicate same-label inputs have nonunique support coefficients at the same decision function. Correct labels, unique causal importance and a solved optimization are different claims — and a proved bound, a matched source and a trustworthy dataset are three more.

The scope stays narrow — 36 Python and 15 Node/real-Chrome tests, four Python CI versions, an installed 11-module/nine-main-command wheel plus the box exporter, all eight fresh fits and full saved/fresh pair audits; the browser checks all 4,552 native/scalar-JavaScript scores, every feature, 24 UI model/example states, physical keyboard input, blocked/successful clipboard, actual JSON Blob download and 320/390/1280 layouts; training-only scaling, a frozen 341/113/115 split and validation-only selection, with all eight fits visible including two with a better test score than the validation choice, on one small historical split that establishes no general ranking; original UCI Wisconsin Diagnostic data CC BY 4.0 with exact source hashes, source metadata losslessly encoded to preserve its original missing final newline, and the plot a two-feature slice with the other 28 features at their training means, not a projection — but the lesson travels: when a system hands you a proof, ask what the proof is about — the represented problem, exactly as encoded — and check the provenance separately, because an exact bound on the represented problem is not a claim about the world the data came from. Distinct from 'A sufficient certificate is not a complete detector', SparseLab's second principle, which is about a certificate staying silent on features it cannot clear — here the certificate is complete for its represented problem, and the gap is not what it fails to cover but what validity itself does not say about the source — and from 'A guarantee is a contract with its assumption', SetGuard's first principle, which is about the assumption the guarantee rests on — here the guarantee's own terms are met, and the question is whether the problem it was proved for is the problem you think it is — and from 'Keep the exact answer next to the approximation', which is about measuring an approximation's error against an exact baseline — here the decimals are explicitly not the bounds, the exact ratios are, and even the exact bound is bounded by its representation.

- [MarginLab](projects/marginlab.md)

## More controls do not always make a valid adjustment

Adjusting for more variables is not adjusting better — CausalLab's backdoor checker treats an adjustment set as a claim about the graph, and the claim can fail when a control is added. In the fixed `A -> X`, `A -> C <- B`, `B -> Y`, `X -> Y` graph, the empty adjustment set passes: with nothing controlled, the only open path from treatment to outcome is the direct one. Add C alone and the set fails — C is a collider on `A -> C <- B`, and conditioning on it opens a path that was closed. Add A or B alongside C and the set passes again, because the new path is blocked at its other end. The bounded search checks every subset of the 0..10 explicitly available candidates rather than pruning by assuming valid supersets, and it returns all passing sets plus the inclusion-minimal sets and the minimum cardinality separately — because two minimal sets can be incomparable and of different sizes, and the smallest is not the only answer worth keeping.

The checker enforces Pearl's sufficient backdoor criterion, not a rule of thumb about controlling for confounders: it excludes original treatment descendants first, then checks separation after removing the treatment's outgoing arrows — a different surgery from the incoming-edge removal that implements do(X) — and a full result retains both conditions and all separation provenance. The other fixtures pin the edges of the rule: one requires the confounder Z, another rejects a descendant mediator, and a third leaves a hidden common cause in the graph even when it is unavailable as an adjustment candidate. A positive-support adjustment calculation on the existing synthetic fixture gives .60/.50, matching direct intervention enumeration. The d-separation API underneath uses ancestor restriction, moralization and connectivity rather than world enumeration: a connected result returns a moral-graph witness, and the collider motif `X -> C <- Y`, `C -> D` is separated with nothing conditioned on and connected given C or given D — while an explicit XOR-noise counterexample shows that connection does not imply dependence. An independent reference agrees on 3,072 adjustment sets across 768 searches on 64 fixed-order four-node DAGs, executes all 1,024 subsets at the candidate cap, and agrees with the d-separation reference on 49,152 singleton/conditioning/surgery combinations and 7,040 disjoint set queries.

The scope stays narrow — 138 tests, independent rational references including all 64 tiny Boolean mechanism pairs, five reproducible audit SVGs, CI on Python 3.10..3.13, standard-library only; at most 65,536 Cartesian noise worlds, 12 endogenous nodes and 16,384 truth-table entries; available variables are declared by the caller, not verified data columns; a passing set licenses the standard adjustment functional only under the causal graph and observed support and positivity assumptions — and no passing set does not prove non-identifiability, because this is Pearl's sufficient criterion, not complete general adjustment, frontdoor or do-calculus search — but the lesson travels: when a method asks you to choose controls, ask what each control does to the graph, not how many you have, and keep the passing set, the minimal sets and the failed ones together, because the set you did not take is part of the answer. Distinct from 'A strong association does not say what an intervention would do', CausalLab's first principle, which is about an association standing in for an intervention — here the intervention is already the question, and the choice is which variables the adjustment is allowed to use — and from 'Label what the data cannot identify', PolicyLens's first principle, which is about flagging a target action the data cannot speak about — here the search does not label and move on, it returns every passing set so the choice among them stays visible — and from 'A search that runs out of budget owes you the gap', TreeLab's first principle, which is about an unfinished search reporting the gap it left — here the search finishes exhaustively over all 1,024 subsets, and the gap is that a sufficient criterion can only ever say yes, never prove no.

- [CausalLab](projects/causallab.md)

## A cap is a choice, not a guarantee

A Newton leaf is a ratio, and a ratio with a near-zero denominator is a claim built on almost no evidence. BoostLab's optional Newton refinement replaces each leaf with sum(y-p)/(sum(p(1-p))+L2), with L2 in [0,1000000] (default 0) and the unshrunk step capped at a value in (0,10] (default 3); mean residuals in [-1,1] stay the default, and nondefault L2 or cap are errors in mean mode. When p is near 0 or 1, p(1-p) is near zero, so an uncapped ratio can hand a leaf near-certainty from a handful of rows. The cap bounds the step, and the implementation earns the right to divide: it compares the numerator against cap times the denominator before dividing, so a subnormal Hessian never produces an infinite intermediate, a zero denominator returns zero with a diagnostic count, and cap-hit counts are reported. Training probabilities from the start of each round define both residuals and Hessians, and the Hessians are checked by finite differences of the sigmoid, with direct tests for the leaf arithmetic, regularization, cap, zero and subnormal denominators.

The cap is recorded and enforced, not assumed: the Newton artifact version, boostlab_v2, records leaf_mode, l2 and max_leaf_step, and strict schema validation checks leaves against that cap instead of [-1,1] on prediction, while the default boostlab_v1 is still accepted unchanged. What the cap does not do is make the leaf right. The Newton depth-2 arm (L2=1, cap 3) has validation select round 35 — 237 nodes, test accuracy .900390625 and logloss .3341242425 — against the depth-2 mean-leaf control's .8906/.3400 at 556 nodes, and the last round-80 checkpoint has 538 nodes at .8984375/.3468631810; the setting was not chosen from a Newton grid search, the fixture is development data already seen, and the comparison does not isolate a causal curvature or regularization benefit. In this run no leaves clip and none have zero denominators — the guard was armed and never fired, and the counts are what make that checkable rather than assumed. The scope stays narrow — 36 Python tests and five Node/Chrome tests (the original 29 remain within the 36), Python 3.10–3.13 CI, 1–16 features, 1–2000 rows, 1–200 rounds, depth 1–3 — and the lesson travels: put the bound where the division happens, count when it binds, write it into the artifact, and never let a bounded step stand in for a claim about the fit. Distinct from 'A clipped attack cannot prove robustness', RobustLab's first principle, which is about carrying an unconstrained optimum into a constrained problem and calling it the answer — here nothing is carried over: the cap is applied inside the solve, before the division, and the gap is not optimality but what a bound on the step does and does not promise — and from 'A small residual is not a small error', BellmanLab's first principle, which is about a capped inner solve returning a bound labeled as a bound — here the cap returns a leaf value, not a bound on anything, and the cap-hit count is what keeps the intervention visible — and from 'Two metrics can disagree, and the choice is the claim', BoostLab's first principle, which is about the metric that selects the model — here the cap selects nothing; it bounds every leaf the same way, and the question is what the bound guarantees, which is only that the arithmetic stayed finite.

- [BoostLab](projects/boostlab.md)

## A missing rating is not a zero

A sparse rating matrix is not a dense matrix with zeros filled in. In RatingLab, 0 is an actual observation — a rating a user gave — so fitting an unobserved pair as zero would invent evidence the data never contained. The project keeps the observed-edge objective visible instead: every joint bias-and-factor block is derived as a regularized linear system with the training mean fixed, the sum-squared objective applies the regularizer once per parameter rather than once per observation, and each user and item update checks its local objective decrease, with half-pass accounting that must telescope to the global objective. Full gradients are kept separate from the residual of the last solved block, so the audits are about the stated objective and nothing else. Filling in the blanks before fitting is not a neutral preprocessing step; it is a claim about the world, and here it would be a false one.

The protocol is built on the same boundary. Only the overall rating in 1,161 distinct user-item pairs from 138 users and 130 items is modeled, on a frozen observed-edge split of 696 training, 232 validation and 233 test rows, and every candidate is judged on observed-edge RMSE alone: eight rank-2/rank-4 factor fits from two penalties and two seeds, and a separate bias-only family selecting among three penalties under the same validation rule, with test rows evaluated only after both selections and without refitting. The selected factor fit has test RMSE .656456774 against the bias-only .656175974 and a training mean of .758069714 — the simpler control wins, and it stays in the write-up. An all-zero-factor stationary control has objective 4 while an explicit feasible factorization has objective .4, so a zero gradient is not a global-minimum certificate even on the stated objective. The v0.2 conditional-response extension keeps the same boundary: an edit or deletion is answered inside a freshly re-solved block, with leverage, the positive deletion denominator and the bound 1 − h ≥ λ/(λ + ‖a‖²), while the frozen mean and opposite factors still retain the row's information — the response is exact inside the block, and the block is not the model.

The scope stays narrow — 30 Python and nine Node/real-Chrome tests, 60 independent exact rational ridge references, eleven fresh refits, test-label poisoning and 12,771 scalar/native predictions, plus sixty additional exact rational design systems, 2,784 deleted-block refits and 576 native/scalar-JavaScript witnesses for the conditional-response extension; an eight-module installed wheel with the original six commands and two conditional-response module commands, CC BY 4.0 historical UCI ratings and MIT code — and this is one historical split with no timestamps, so it is not chronological, not a significance claim and not a general-superiority claim; observed-rating RMSE is not top-N relevance, missing-pair accuracy or calibrated certainty, and synthetic cold-entity tests do not establish measured cold-start performance — but the lesson travels: when the data is sparse, define the objective on what was actually observed and audit it there, because every unobserved entry you fill in before fitting is evidence you invented, and no amount of exact arithmetic downstream can un-invent it. Distinct from 'Score only what was missing', DenoiseLab's second principle, which is about what the score counts — here the score is already on observed ratings, and the question is what the objective sums over while fitting — and from 'A row left out is not a row held out', TreeLab's principle, which is about the granularity at which a row counts as excluded — here nothing is excluded from the fit at all, the unobserved pairs were never in the objective — and from 'A stopping rule is not a mode certificate', MixtureLab's second principle, which is about a stopping rule certifying nothing — here the stationary control is only a check that the audits are about the stated objective, and the principle's center is the objective's domain, not the stopping rule.

- [RatingLab](projects/ratinglab.md)

## A saving is a curve, not a number

A KV cache saves the recompute it avoids, and the recompute avoided grows with every token generated — so the saving is a function of run length, not a single percentage. KVLens runs one attention block down two decode paths: the full path recomputes Q/K/V and attention over the entire prefix for each new token, while the cached path runs a batched prefill that computes each prompt position's K/V once, then one incremental step per generated token attending over the cache. At one generated token the two paths cost exactly the same, because prefill is the full forward — the saving starts at zero. On the default fixture it is 36.9% at two generated tokens and 90.8% at 32. Quoting "90.8% saved" without the length quotes the end of a curve as if it were the whole curve, and the first token is the counterexample: a cache that has not yet had anything to reuse has saved nothing.

The shape is measured, not asserted. The two paths are already known to be the same program — their final-position logits are bitwise identical, with a max absolute logit difference of exactly 0.0 across two model configurations and five prefix lengths, and greedy generations checked token for token — so the curve is a property of the saving, not a confound of a changed result. The suite pins the shape itself: a curve test pins the savings-curve shape including the zero at one token, cost ordering (cached never exceeds full) is tested, and the demo generates 32 tokens down both paths with `--require-identical --min-savings 0.85`. The counter inside both paths counts actual matmul FLOPs, so the percentages are counted arithmetic, not asymptotic complexity — and the scope stays narrow: the counter covers matmul FLOPs only, and the project makes no latency claim, because the real reason KV caching is fast is memory bandwidth, which a pure-Python model cannot measure. The weights are seeded, not trained, one attention block, greedy decoding only, no cross-sequence batching or cache eviction — but the lesson travels: when a benefit accumulates over a run, report the curve, the zero at the start and the shape in between, because a single percentage hides the length it was measured at. Distinct from 'Make the fast path prove it equals the slow path', the shared KVLens/SpecLab principle, which is about proving equivalence first and then counting the savings — here equivalence is already established, and the question is what the counted saving means at each length — and from 'A cheaper sampler is not the same sampler', DiffuseLab's second principle, which is about a cheaper procedure changing the samples — here the sampler is provably the same, bitwise identical, and the saving still is not one number — and from 'Show the bill with the gain', AlignLab's first principle, which is about reporting the price alongside the gain — here there is no extra price to report, the gain itself varies along the run.

- [KVLens](projects/kvlens.md)

## Out-of-bag is still in-sample

A hard-vote fraction can look reassuring while hiding which models saw the observation. ForestLab exposes every bootstrap count, path, leaf and vote, and its inspector separates the full-forest vote from the out-of-bag vote for a stored training group. An OOB score uses only the trees with zero draws of that group — and when no tree qualifies, there is no prediction at all, never the full-forest result quietly substituted in. The distinction matters because the OOB number is computed on training groups: every row it scores was in the training set, just not in every tree's bootstrap draw. It is a diagnostic of how the forest behaves on its own training data, not a measurement of the deployed forest on unseen rows. The deployed forest is all 31 trees; the OOB forest for any one group is a different, smaller forest. Quoting the OOB score as if it were the full forest's held-out performance credits the forest with a test it never took.

The held-out number is kept separate, and it is kept honest. The original licensed UCI file has 1,372 numeric records but only 1,348 unique four-feature vectors, so exact copies are collapsed and kept together before the fixed 808/270/270 train/validation/test split — no identical vector can straddle the boundary and flatter the test score. Each model family selects by validation errors, then Brier score, then ID, before test labels are read. All eight forests, four single trees and seven controls remain visible, and the stronger comparison stays in the write-up: the selected forest makes 3/270 test errors while the stronger selected 5NN control makes 0/270 and the selected single tree makes 8/270. The split ordering is exact too — binary CART split costs are compared by arbitrary-precision integer cross products, checked by 60 independent Fraction designs and a separate BigInt complete-mask enumerator — but exact ordering is not a claim about the trees being globally optimal, and the classes stay the source's labels 0 and 1, not an invented genuine/forged mapping.

The scope stays narrow — 31 Python and nine Node/real-Chrome tests, 10,784 forest evaluations, 8,088 control scores, 6,464 OOB records and 992 native path references, with an eight-module/seven-command installed package refitting all 19 models; hard votes, leaf fractions and neighbor fractions are not calibrated probabilities, and OOB is not the held-out full-forest test or independent specimen validation — but the lesson travels: when a score is computed by excluding part of the model, name what was excluded and what the remaining score actually measures, because a diagnostic that borrows the authority of a held-out test will be read as one. Distinct from 'A row left out is not a row held out', TreeLab's principle, which is about the granularity at which a row counts as excluded from a search — here nothing is excluded from the fit at all, and the question is what the out-of-bag subset's score means — and from 'A missing rating is not a zero', RatingLab's principle, which is about what the objective sums over while fitting — here the fit is not the issue, the score's meaning is — and from 'A set is a coverage claim, not a probability claim', SetGuard's principle, which is about what a set claims — here the vote fraction's claim is about held-out performance, and the membership list is what keeps that claim honest.

- [ForestLab](projects/forestlab.md)

## A perfect training score is not a finished optimization

Four separable one-dimensional points reach 100% training accuracy after one pair update while the optimization gap is still 2/3. The accuracy and the gap are different quantities: the accuracy is a property of the current decision function on four points it has just seen, while the gap is the solver's own measure of how far the dual is from done. The score saturates first — a perfect training score can arrive long before the optimization does, and it says nothing about the coefficients that produced it. The twin controls make the same point from the other side: opposite labels at an identical input give zero pair curvature and force an endpoint comparison, so the labels alone do not determine the step; duplicate same-label inputs have nonunique support coefficients at the same decision function, so the predictions do not identify the coefficients. Correct labels, a perfect score and a solved optimization are three different claims, and only the gap speaks to the third.

The same separation runs through the full fits. All eight fits stay visible, including two with a better test score than the validation choice — the validation choice stays the choice, because test rows are evaluated only after selection and are never a second selection round. The gap is reported next to the scores for the same reason: the approximate gap readouts for C=.01, .1, 1, 10 are 7.97e-8, 1.42e-6, 2.90e-5 and 3.23e-4, a number per penalty that says how unfinished the optimization is, and full-data stopping remains numerical rather than an exact-rational certificate. A score that looks finished and a solver that says it is not are both in the write-up, and the reader is expected to believe the solver.

The scope stays narrow — 36 Python and 15 Node/real-Chrome tests, 60 exact active-face optima checked by a separate active-face KKT oracle that never calls the pair solver, 4,552 original inference checks, four full proofs, an installed 11-module/nine-main-command wheel plus the box exporter, training-only scaling and a frozen 341/113/115 split with validation-only selection, original UCI Wisconsin Diagnostic data CC BY 4.0 with exact source hashes, and the plot a two-feature slice with the other 28 features at their training means, not a projection — but the lesson travels: report the optimization's own measure next to the score, because a score can be perfect before the optimization is, and the gap is the number that says so. Distinct from 'Decreasing loss is not convergence', PartsLab's principle, which is about the objective itself falling through a whole run without the fit ever meeting stationarity — here the reassuring number is accuracy, a different quantity from the objective, saturating at 100% after one update while the gap the solver minimizes is still 2/3 — and from 'A green suite is a regression gate, not a certificate', EvalForge's principle, which is about a passing suite certifying nothing beyond the tasks written down — here the score is on the training data the solver just fit, and the unfinished business is the solver's own gap, reported alongside — and from 'A valid proof does not authenticate its source', MarginLab's first principle, which is about what a proved bound says about the source — here no proof is involved, and the question is what a training score says about the optimization.

- [MarginLab](projects/marginlab.md)

## The base vocabulary decides what can ever be encoded

A tokenizer's coverage is decided before training starts, by the base vocabulary and the pre-tokenizer — not by the merges it learns. TokenForge starts from the 256 byte values, so any text — ASCII, Unicode, emoji — encodes and decodes exactly; there is no character the vocabulary has never seen, because the base is the byte alphabet itself. And the merges are fenced in before they are counted: a GPT-2-style regex pre-tokenizer splits text into words, numbers, symbol runs, whitespace and contractions, and merges never cross those boundaries, so a token can never glue a word to its punctuation or a number to its unit. Deterministic training then counts exact adjacent pairs over those pre-token sequences, merges the most frequent pair first with ties broken on the pair itself, and stops at the requested vocabulary size or the minimum pair frequency; rank-ordered encoding applies the same merges lowest-rank-first, so the token stream at encode time is identical to the one training produced.

The scope stays narrow — 40 unit tests cover pre-tokenization, pair counting and merging, deterministic training, vocabulary caps and minimum counts, encode/decode round trips across ASCII, Unicode and emoji, save/load, statistics math, Markdown escaping and the CLI end to end including both sides of the compression gate; the offline demo trains a 300-token vocabulary on the bundled corpus, verifies an encode/decode round trip, asserts the compression statistics and checks both sides of the gate; CI runs across Python 3.10–3.13 — and the bounds are stated on the construction: byte-level BPE is the tokenizer family GPT-style models use, but this is a from-scratch teaching-and-tooling implementation, not a drop-in replacement for production vocabularies, and the pre-tokenization pattern is ASCII-oriented and simplified relative to GPT-2's Unicode-aware split. But the lesson travels: the guarantees a tokenizer can offer — every text encodable, every token respecting a boundary — are properties of the base and the pre-tokenizer, fixed before a single merge is learned; a merge step can only combine what the construction already allows. Distinct from 'Keep the recipe with the artifact', TokenForge's first principle, which is about whether an artifact can be rebuilt from its recorded construction — here the question is what the construction permits the artifact to represent at all — and from 'Determinism is what makes a quality number testable', EmbedKit's principle, which is about determinism making a quality number re-runnable — here determinism is shared machinery, and the point is coverage, not testability — and from 'A weight is a measurement on a task, not an explanation', AttnLens's principle, which is about quoting a learned number with its task — here nothing about coverage is learned at all, it is fixed by the base vocabulary before training begins.

- [TokenForge](projects/tokenforge.md)

## The graph decides the answer before the eigensolver runs

The clustering is decided by the graph, not by the eigensolver. SpectralLab builds the affinity and the normalized Laplacian explicitly, retains the eigenspace, normalizes every row and runs manual k-means, with NumPy supplying only the symmetric eigenvalue solve through LAPACK — and the choice of which points are neighbors, and what their connection means, is made before any of that machinery runs. Two original seeded 96-point fixtures use noisy interleaving arcs and concentric rings, and nine fixed graph rules give 18 total fits: union/mutual kNN at 3/6/12 neighbors and full RBF at sigma .08/.25/1.0, with raw-coordinate k-means alongside and generator labels never choosing a graph or fit. The numbers keep the graph honest about what it did: moons union-3 reaches ARI 1.000 with eigengap .003156, while moons RBF sigma 1.0 gives ARI .242035 with the larger eigengap .350982 — a larger gap is not agreement with the intended classes, and raw-coordinate k-means gives the same .242035. Rings union-6 reaches ARI 1.000 while rings union-12 gives ARI -.010195, so adding edges does not promise a better grouping. And moons mutual-3 has four disconnected components, so its two-dimensional truncation of a four-dimensional zero eigenspace is not unique and that fit is refused, with no arbitrary cluster labels shown. The graph is the claim; the eigenvalues only execute it.

The relaxation is not the discrete optimum either, and the project says so with the exact number. An original seven-vertex weighted graph has only 63 distinct nonempty binary cuts after fixing one cluster label; independent rational enumeration finds the optimum 3450/4181 = .8251614446304711, while the archived spectral relaxation plus k-means returns .860832137733142 — a worse cut, with both partitions and every weight visible, and no exact-optimality claim for the larger fixtures. V0.2 makes the graph's influence differentiable instead of merely visible: a fixed undirected edge edit changes both endpoint degrees and every normalized incident edge, and manual differentiation retains those terms; the bottom-two spectral projector P = U Uᵀ has a basis-invariant derivative using only retained-to-excluded denominators, with internal repeated eigenvalues allowed and repeated eigenvalues crossing the retained boundary refused without an epsilon repair. Six original small graphs include four smooth base cases and 28 predeclared finite states, one reaching a five-cycle boundary tie; a six-cycle and an isolated vertex are refused at the base, while the two disconnected triangles retain their full zero eigenspace and have a valid one-sided graph-domain response when a missing bridge is added. Every actual finite eigensolve and 12-start k-means result is archived, not predicted from the derivative, and the archived tiny-step assignment change is explicitly a rounding-ambiguity control — distinct tested partitions with numerically equal inertia — not a unique-optimum, label-derivative, robustness-certificate or stability-rate claim.

The scope stays narrow — 33 Python and nine Node/real-Chrome tests, 83 normalized-Laplacian edge finite differences, 42 exact Fraction cut derivatives, 528 independent Fraction-distance graph references, 558 rational cut references, 4,896 scalar eigenpair-row equations, 1,728 actual browser point/graph states and 168 new sensitivity states, with a six-module/nine-command installed wheel refitting all 18 graphs and verifying four archived web exports byte-for-byte; dense full-data synthetic illustrations, not held-out prediction, exact discrete optimization, optimal-graph selection or calibrated uncertainty; eigenvector signs are arbitrary, zero-degree vertices are not silently connected, and numerical eigenpair residuals are checks, not formal proofs — but the lesson travels: when a method has a construction step before the solver, the construction is the claim, so audit the graph, not just the eigenvalues, because a solver can only be as right as the graph it was handed. Distinct from 'Zero correlation is not independence', HamiltonLab's principle, which is about a statistic computed on one observable saying nothing about independence — here the eigengap is a spectral statistic that says nothing about agreement with the intended classes, and the point is the graph that produced it, not the observable it was computed on — and from 'Two possible cuts can be jointly impossible', SegmentLab's principle, which is about the joint feasibility of two cuts — here one cut is computed and compared against its exact optimum, and the failure is the relaxation returning a worse cut, not joint impossibility — and from 'Differentiate the computation you ran, not the optimum you wish you had', TransportLab's principle, which is about when an envelope derivative is justified by an earned optimum — here the derivative is of the actual finite computation, degrees included, and it serves as the audit that proves the graph's influence rather than as the claim itself.

- [SpectralLab](projects/spectrallab.md)

## A permutation that refits is a different question

ForestLab's v0.2 joint permutation diagnostics move all 15 nonempty feature blocks through the same 16 fixed row bijections: selected columns come from the same donor, recipient labels and remaining features stay in place. Both frozen models — the selected forest and the stronger selected 5NN — retain all 240 cases and 129,600 model-row prediction counts, with every repeat, including negative error changes, remaining visible. No model is refitted, no removed-feature control is fitted, and no selection is changed. The frozen model is the point: the diagnostic asks what the model you actually have does when the pairing between feature blocks and labels is broken. Refit after permuting and you are asking a different question — how a fresh model would learn from scrambled data — and the answer tells you about the learning procedure, not about the model in front of you.

The diagnostics use the same validation set that already selected the models, so baseline validation errors are 4/270 and 1/270, distinct from the unchanged test errors 3/270 and 0/270. Moving a block preserves dependence within it, not across its boundary; joint changes are not sums, and not isolated causal interactions. Repeat ranges are not confidence intervals. The exact three-row, six-bijection control exposes off-support singleton hybrids, and even full-row shuffling can preserve observed support while destroying label pairing — so inputs that still look like real rows are not evidence the pairing survived. The browser recomputes the selected hybrid row independently and exposes all tree paths, neighbor votes, donor mapping and model binding.

The scope stays narrow — 31 Python and nine Node/real-Chrome tests, with independent scalar-JavaScript predictions for all 129,600 model-row evaluations, exact Fraction metric controls, full fresh regeneration, fit/map/count mutation rejection, train/test-label poisoning and 1,230 actual browser states; outside-checkout reproduction regenerates all 240 cases, audits them and compares seven archive/loader exports exactly, and the eight-module/seven-command installed package refits all 19 models — but the lesson travels: when a diagnostic is meant to interrogate a model, freeze the model and vary only the input structure, because the moment the model is refitted the diagnostic measures the training procedure instead, and the number it reports answers a question nobody asked. Distinct from 'Out-of-bag is still in-sample', ForestLab's first principle, which is about what the out-of-bag score measures when the subset of trees changes — here the model is frozen and the input pairing changes, and the question is what the diagnostic measures — and from 'A row left out is not a row held out', TreeLab's principle, which is about the granularity at which a row counts as excluded — here nothing is left out, the row stays whole and only the pairing between its blocks and its label is broken — and from 'Hold the distribution fixed and vary only the strategy', which is about holding the background fixed while the strategy varies — here the fixed thing is the object under test itself, and what varies is the joint structure of its inputs.

- [ForestLab](projects/forestlab.md)

## The normalizer is part of the model

TagLab trains linear-chain conditional random fields from scratch, and the first thing it refuses to hide is where the probabilities come from. A 39-parameter sequence score combines fixed observed features, FROM/TO label transitions and separate start/end scores; manual log-space forward/backward produces the global partition, node and adjacent-label marginals, and expected-minus-observed feature counts give the supervised conditional-likelihood gradient. Viterbi and token-marginal decisions stay separate. The point is that the normalizer is not plumbing underneath the model — it is a modeling choice, and moving it changes the distribution itself. The exact witness makes the difference arithmetic, not rhetorical: three allowed paths A/C, B/A and B/C have raw weights [1/9,1,1/9]; one global normalizer gives [1/11,9/11,1/11], while equal initial branch scores with local outgoing normalizers give [1/2,9/20,1/20]. A's only outgoing branch always keeps its incoming 1/2 mass, even when its continuation loses raw weight — a locally normalized step cannot take back probability it has already handed out, so later evidence never gets to revise an early commitment.

The comparison is kept honest by fitting the alternative instead of caricaturing it. The independent-label control uses exactly the same eight observed features, including left/right context; its 15 sequence scores are fixed at zero and its remaining 24 weights are fitted, not left as a weak untrained baseline. Both families fit three positive L2 penalties and select by validation conditional NLL per token, on a fixture of 24 training, 12 validation and 16 test sequences of noisy numeric observations from persistent synthetic states. The selected chain's test NLL/token is 0.557614 against the independent control's 0.813715 — but its Viterbi token errors are worse, 66/164 against 56/164, while marginal token errors tie at 56/164 and whole-sequence errors tie at 15/16: a better distribution score and a worse best path are different objectives, and the family comparison changes fitted parameters and penalty geometry too, so it is descriptive rather than an isolated causal effect. Every one of 327 stored states retains all parameters, all 39 analytic gradient entries, objective, gradient norm, accepted Armijo step and rejected larger steps; the browser independently recomputes objective and gradient from the original training examples. Three fits stop at the 1e-5 gradient tolerance and three exhaust their 80-update budget; the selected chain exhausts its budget with gradient norm about 0.000629, and convexity plus a decreasing curve do not certify that finite iterate as an optimum.

The scope stays narrow — 43 Python and 20 Node/Chrome tests, with independent Fraction and BigInt path enumerators testing 600 events across sixty fixtures, all 39 finite-difference event derivatives, 864 cross-language numerical witnesses and 864 browser queries, 5,895 UI states/queries overall, and an eleven-module/nine-command installed wheel reproducing six fresh fits, 327 audits and four exact archive exports; this models p(labels|observations), not p(observations), both neighboring observations are available so it is not streaming inference, and model posteriors are not calibrated real-world confidence — original synthetic sequences, not an NLP benchmark — but the lesson travels: when a model reports probabilities, ask what was normalized over, because a per-step normalizer and a whole-sequence normalizer are different models wearing the same scores, and the one that commits early cannot be fixed by better features. Distinct from 'A conditioned prior must be renormalized', which is about recomputing evidence after restricting a prior's support — here nothing is restricted, the question is where the normalizer sits in the first place, per step or over the whole sequence — and from 'A marginal is not a path', which is about two summaries of the same distribution disagreeing — here the distributions themselves differ, so the same paths get different probabilities depending on which normalizer produced them.

- [TagLab](projects/taglab.md)

## A count is not an expectation

TagLab's count inspector conditions on exactly r occurrences of a chosen label — a nonlocal event, because the positions have to agree on the total. An augmented (count, label) forward/suffix recursion exposes the full original count distribution and reconstructs conditional node and pair probabilities, entropy, a complete best path and all 39 event derivatives. Counts refer to positions, not runs or segments. The independent-node control shows why matching the expectation is not the same as meeting the total: a fair two-position control conditioned on exactly one A permits only AB and BA, each with mass 1/2, so the node marginals remain halves — but independent draws from those marginals leave the event half the time. The inspector separately computes the independent-node Poisson-binomial count law, so the gap is visible rather than assumed away. Conditioning can create dependence without any transition scores, and a correct expected count does not guarantee a valid complete path: the expectation is a property of the distribution, not a promise about any single draw.

The checks are exact where they claim to be. Each of the independent Fraction and BigInt path enumerators tests 600 events across sixty fixtures, all labels and counts, with all 39 finite-difference event derivatives, 864 cross-language numerical witnesses and 864 browser queries, for 5,895 UI states/queries overall. The combined suites pass 43 Python and 20 Node/Chrome tests, and an eleven-module/nine-command installed wheel reproduces six fresh fits, 327 audits and four exact archive exports.

The scope stays narrow — this is established state augmentation, not a new algorithm, training, causal intervention or accuracy gain; the quadratic count-state computation has a 64-position limit, numerical near-ties may yield different Python/JavaScript path representatives while constraints and attained scores are checked separately from identity, and probability underflow is distinguished from finite log probability, with original fitted scores, held-out metrics and exhausted budgets unchanged — but the lesson travels: when a requirement is stated on a total, check the total, because an expectation can be exactly right while half the draws fail it, and a per-position summary cannot state a constraint that only the whole sequence can satisfy. Distinct from 'The normalizer is part of the model', TagLab's first principle, which is about where the normalizer sits, per step or over the whole sequence — here the normalizer is fixed and the question is what an expected count guarantees about any actual draw — and from 'A marginal is not a path', which is about per-position winners combining into an impossible path — here the marginals agree, both halves, and the joint event still fails half the time, because the failure is not disagreement between summaries but that no per-position summary can express a total — and from 'A mean is not the distribution', which is about a summary dropping the spread — here nothing is summarized, the marginals and the expectation are exactly right, and the exact total still is not enforced.

- [TagLab](projects/taglab.md)

## Point the optimizer at noise and see what it buys

A gain is only evidence for the signal if the same machinery pointed at noise cannot buy it. AlignLab's alignment is gradient ascent on a learned reward, and gradient ascent will climb whatever reward you hand it — so the load-bearing check is to hand it a reward model trained on utility-independent labels and watch what happens to true utility. The real reward model buys a true-utility gain of +2.5329, from 2.0375 to 4.5704, while paying KL 1.0750. The noise-trained control buys −0.1826: the noise-aligned policy ends at 1.8549, worse than the uniform reference it started from. The optimizer did not merely fail to help on noise — it actively spent the KL budget moving the policy somewhere worse. That is the point of the control: it prices the machinery itself. If the control had gained, the +2.5329 could have been an artifact of ascent on any smooth signal, and the `--max-control-gain 0.2` gate exists to fail CI the moment it does. The comparison is kept honest in the other direction too: the reward model is only 0.7800 accurate on 150 fresh holdout pairs, bounded by sigmoid-noisy labels, and the label-shuffled control model lands at 0.4333 — so the contest is between a weak-but-real signal and a no-signal control, not a perfect model against a straw man. The scope stays narrow — one seeded fixture, 47 Python tests including all 15 original tests unchanged, fully offline, CI across Python 3.10–3.13 — so the control is a fixture comparison, not a general proof that signal alone causes improvement — but the lesson travels: when the method is an optimizer, the control is not a weaker method but the same optimizer pointed at noise, and a gain that survives that control is a gain the machinery alone could not have bought. Distinct from 'Show the bill with the gain', AlignLab's first principle, which is about reporting the price alongside the gain — here the price is already reported, and the question is whether the gain could have been bought by the machinery at any price — and from 'A gain needs a control that could have produced it', DistillLab's principle, which decomposes one gain into its parts — here nothing is decomposed, the same optimizer runs twice on different signals and the comparison is between the two runs, not between parts of one.

- [AlignLab](projects/alignlab.md)

## A tangent is not a map

DenoiseLab's v0.2 fixed-mask response derives the local answer from fixed parameters: full chain-rule matrices through the three tanh layers and sigmoid for the network, and an observed-only linear-system derivative for PCA. The tangent is exact at its point — saturated PCA rows have zero local response, and nonconstant clipping-boundary rows are null rather than an invented derivative — but it is a claim about an infinitesimal neighborhood, and the v0.2 work keeps actual edited reconstructions separate from tangent predictions for exactly that reason: a derivative says what happens if you nudge one pixel a little, and nothing about which fitting row wins one pixel-value away. The v0.3 scalar path and the v0.4 two-pixel map replace the local object with a global one. For a single observed-pixel edit, the complete retrieval path covers every open interval plus the complete endpoint tie; for two observed values, the exact rational closed minimum cells cover the whole plane — area cells, segment-only cells and point-only cells, with explicitly proved empty regions. Shared boundaries come from complete all-row exact tie queries, not an interior representative, and the Fraction/BigInt witnesses retain all 3,062 original fitting-row coefficients. The map answers, for every possible edit, which row is retrieved; the degenerate cases are the point, not the edge case — point-only and segment-only winners exist, empty regions are proved empty rather than unsampled, and a map that omitted them would be a sample with a border drawn around it.

The scope stays narrow — 35 Python and eight Node tests at v0.2, covering derivative checks including independent finite differences and augmented least squares, 120 full cross-language responses, 480 browser views and 8,192 heatmap pixel checks with an eight-module/five-command installed reproduction; 44 Python and eleven Node tests at v0.3, covering 5,344 independent rational oracle queries, 40 complete cross-language paths, 160 browser queries and 30,720 actual canvas colors with a nine-module/seven-command installed reproduction; 52 Python and fourteen Node/Chrome tests at v0.4, including independent boundary-pair enumeration of 238 small-source cells and 2,110 rational queries, forty complete cross-language maps, 160 browser queries and 30,720 actual canvas colors with a ten-module/nine-command installed reproduction — and the map is a fixed two-coordinate slice only, not general robustness, causal recourse, uncertainty, better accuracy or binary64 tie equivalence, with the original models and scores unchanged and the derivations in RESPONSE.md and PLANE.md — but the lesson travels: when the question is what happens for every input in a range, a derivative is the wrong object, so build the partition, enumerate every cell including the degenerate ones, prove the empty regions empty, and derive the boundaries from all the rows at once, because a local answer, however exact, is not a map of the territory it sits in. Distinct from 'A control that cannot win is not a control', DenoiseLab's first principle, which is about whether the rival methods are built strong enough to beat the model — here no rival is compared, and the question is what a local characterization does and does not tell you about the whole input plane — and from 'Score only what was missing', DenoiseLab's second principle, which is about what the score counts — here the score is not in question, and the question is local versus global description of the response — and from 'A local metric does not certify a finite step', FisherLab's principle, which is about one finite step, a single move from a point whose landing needs its own check — here the object is not one step but the whole plane, every possible edit value with every cell, tie and empty region enumerated exactly — and from 'A group deletion is not the sum of its single deletions', InfluenceLab's principle, which is about one finite change against its linear prediction — here no single destination is in question, the map answers every destination at once, and the tangent is not wrong about any of them, only local.

- [DenoiseLab](projects/denoiselab.md)

## An exact interval is not a path

PartsLab's v0.3 fixed-face inspector answers one question exactly. Nominate a face from the numeric NNLS result — a support pattern, a set of active parts — re-solve it exactly, and intersect every affine KKT inequality with the pixel domain, and the result is the exact interval of pixel values over which that face stays the optimal response. Endpoint ties, singular refusals, singleton faces and duplicate-basis nonuniqueness stay explicit rather than being rounded away, and the interval is a proved fact about that candidate, not an approximation. But it is a fact about one candidate. The inspector does not say which face takes over past either endpoint, where the kinks in the response path sit, or how many faces the full path crosses — one candidate interval is not the path, and the exactness inside the interval buys nothing outside it. That is the discipline the v0.3 work keeps: the certificate is exact and complete about the face it was asked about, and silent about everything else, and the silence is stated rather than filled in with an extrapolation. The same boundary ran through v0.2: the fixed-basis certificate proved the objective gap for a candidate exactly, with eighty exact rational active-set optima behind it, and even a zero gap did not imply unique coefficients — the proof certified the objective, not the parts.

The scope stays narrow — 38 Python and eleven Node/Chrome tests at v0.3, covering 200 independently enumerated tiny face candidates, all 120 stored nominations, 54 complete native/BigInt/Worker witnesses and 10,368 endpoint pixel colors, with a ten-module/ten-command installed wheel reproducing all six fresh fits, original data, models and scores unchanged, and the derivation in FACE.md — and the interval is for one candidate face only, not a full path, unique support, robustness or joint-NMF optimum — but the lesson travels: when a certificate is exact, say exactly what it covers, because exactness tempts the reader to extend it past its boundary, so name the boundary in the same breath as the result, and never let a proved interval stand in for the path it is only one segment of. Distinct from 'A tangent is not a map', DenoiseLab's principle, which is about a local linear approximation against the exact global partition — here the interval is exact, not approximate, and the gap is not accuracy but coverage: one candidate's exact range against the whole path — and from 'Decreasing loss is not convergence', PartsLab's first principle, which is about whether the optimizer arrived at all — here arrival is not in question, the face is re-solved exactly, and the question is what the exact answer does and does not extend to — and from 'A reconstruction does not identify the parts', PartsLab's second principle, which is about many decompositions giving the same reconstruction — here the reconstruction is fixed and the face is fixed, and the question is not which decomposition means something but how far one exact answer reaches before the response changes hands.

- [PartsLab](projects/partslab.md)

## Edits add; deletions couple

RatingLab's v0.3 joint-batch inspector asks one batch two different questions, and the two answers obey different laws. Change the target values of several rows inside one frozen block and the responses add: each edit shifts the conditional solution linearly, and the batch answer is the sum of the single-row answers. Remove those same rows instead and the responses do not add: a joint deletion re-solves a coupled Schur system, and the result generally differs from the sum of the separate-original-baseline deletions. The inspector shows both — the full source-bound problem, a conservative positive-ridge bound, numerical condition and refusal checks, and the joint and separate curves for every query — so the difference is measured, not assumed. The word "batch" hides the split: one operation composes by addition and the other by a coupled solve, and only the curves say which one you are looking at.

The single-row version was already exact. The v0.2 conditional-response extension answered one edit or one deletion at a time inside a freshly re-solved block: a target edit has exactly linear finite response within the quadratic problem, and Sherman-Morrison gives a deletion update scaled by the original conditional residual and 1 − h, with the bound 1 − h ≥ λ/(λ + ‖a‖²) following from the deleted system's ridge floor. The v0.3 batch inspector keeps the same frozen boundary — the mean and opposite factors stay frozen, the original fits, scores and stronger bias control stay unchanged — and extends the question from one row to many. The independent checks extend with it: 320 rational direct-system cases, 128 real augmented-least-squares cases and 320 complete native/browser Cholesky responses plus 4 controls, behind 37 Python and 14 Node/actual-Chrome tests, a ten-module wheel with eight main CLI commands and two single-row module commands, and the derivation in BATCH.md with the inspector at batch.html.

The scope stays narrow — 37 Python and 14 Node/actual-Chrome tests at v0.3, covering 320 rational direct-system cases, 128 real augmented-least-squares cases, 320 complete native/browser Cholesky responses plus 4 controls, with a ten-module installed wheel, eight main CLI commands and two single-row module commands — and this remains a conditional calculation, not full ALS retraining, cross-validation, causal attribution, uncertainty or data unlearning, with original fits, scores and the stronger bias control unchanged — but the lesson travels: when one tool answers two operations, check the composition law of each, because a batch that adds for edits and couples for deletions will be misread by anyone who assumes one law covers both, so show the joint and separate curves together and let the difference be visible. Distinct from 'A group deletion is not the sum of its single deletions', InfluenceLab's principle, which is about finite deletions not adding — here deletions not adding is the known half, and the question is the asymmetry: edits in the same batch do add, so the batch has two laws, not one — and from 'A deletion is defined by what you hold fixed', InfluenceLab's second principle, which is about which refit the words name — here every number compared sits inside one frozen block with the same held-fixed quantities, and the question is which operation composes, not which refit is meant — and from 'A missing rating is not a zero', RatingLab's first principle, which is about what the objective sums over while fitting — here the fit is frozen and the question is how batch responses compose, not what the objective counts.

- [RatingLab](projects/ratinglab.md)

## Proximity is a leaf-collision average, not a similarity score

ForestLab's v0.3 leaf-collision inspector exposes all-tree similarity as an explicit Gram matrix — but the numbers in it are counts, not measurements of likeness. The all-tree proximity is the mean of per-tree leaf collisions, P=ZZᵀ/T, with tree identity kept in each leaf-indicator column, including singular matrices. Two rows are "close" when they keep landing in the same leaf across trees, and the squared feature-space distance is 2(1−P), so distinct raw inputs can have zero distance. That is a fact about the fitted partitions, not about the rows: sharing a leaf is a shared routing decision by trees trained on the same labels, and no label is read by the new calculation — but the already fitted partitions retain supervised label information, so the geometry is frozen supervised model geometry, not semantic similarity, causal influence, uncertainty or a new score.

The jointly-OOB view makes the limit explicit. Indexed jointly-OOB comparisons use the original training order and complete bootstrap multiplicities, keep pair-specific tree counts, and leave undefined comparisons undefined — a zero eligible denominator is undefined, not zero similarity. The constructed three-row partition/eligibility control has cᵀP_oob c=−2 for c=(1,−2,1) while the corresponding all-tree form is 10/3, and with the triangle failure that disproves a universal PSD guarantee for OOB normalization — not every OOB matrix's PSD status, just the claim that the construction always yields a kernel. No matrix repair or hidden missing-entry fill is used, and the refusal to repair is the point: a repaired matrix would answer a different question. The checks are exact where they can be — 512 small partition controls, 5,760 native/scalar-JS matrix entries, 1,152 actual pair states and 13,824 heatmap colors, 6,272 source-pair entries through independent traversal/set intersections, complete native/scalar-JS reference matrices with 1,152 mixed-partition and 4,608 heatmap entries plus 8,928 terminal coordinates, and exact integer/BigInt sum-of-squares witnesses for the full quadratic expression and every leaf-bucket square. Real Chrome checks every pair and all 13,824 view-specific colors, exact large integers, indexed/feature-only states, invalid retention, model context, keyboard, clipboard and actual Blob JSON, and the installed wheel preserves all 19 fresh fits and permutation audits and checks two new exact exports. The fixed 24-row matrix is descriptive, not selected for quality or a whole-data embedding.

The scope stays narrow — 39 Python and 12 Node/real-Chrome tests at v0.3, with a ten-module/ten-command installed package refitting all 19 models, and the leaf-collision inspector at proximity.html with the derivation in PROXIMITY.md — but the lesson travels: when a matrix is built by counting shared leaves, call it a collision count and check whether it is a kernel before using it as one, because a similarity that can go negative under its own quadratic form will break every method that assumes a geometry, so show the counterexample alongside the matrix and let the undefined stay undefined. Distinct from 'Out-of-bag is still in-sample', ForestLab's first principle, which is about what the out-of-bag score measures when the subset of trees changes — here the object is pairwise, not a score, and the question is whether the numbers form a geometry at all — and from 'A permutation that refits is a different question', ForestLab's second principle, which is about what a frozen model does when the input pairing breaks — here the model is frozen too, but nothing about the inputs changes, and the question is what the pairwise numbers are — and from 'The graph decides the answer before the eigensolver runs', SpectralLab's principle, which is about the chosen graph deciding the answer before any solver runs — here the matrix can fail the premise itself, so there is no valid geometry for a solver to work with in the first place.

- [ForestLab](projects/forestlab.md)

## A sample is not the range

MarginLab's v0.3 extension changes the form of the answer: not a point, but the exact range over a stated region. The frozen represented linear models define an exact affine function in original feature units, so coordinate signs yield its exact minimum and maximum on a finite rational box, with complete corner vectors that attain each bound, and both label claims use the existing +1-at-zero rule. A sample of points inside the box can only ever land inside the range; the box returns the range itself, attained, with the corners that attain it. Independent native Fraction and browser BigInt readers check all coordinate support equalities and scores, and the page separately reconstructs the affine function from every original saved coefficient, represented training input, mean, scale and bias; valid changed-function controls keep source identity separate from mathematics.

The range is exact only for the box as declared. The presets expand eight fixed historical queries by exact plain-decimal multiples of training-only scales — synthetic independent-coordinate sets, not measurement tolerances, domain-valid inputs or plausible causal interventions. All 30 intervals can be edited, with the declared center required to remain inside; edits, malformed inputs and source mismatches clear old results and block export. Approximate plots include zero and stay separate from the full exact witness fractions and the unchanged scalar floating center scores, so the picture is never quoted as the answer. And the exact rational affine function is not a bound on rounded production inference or exact real-number standardization, and it carries no RBF, clinical, probability, causal, generalization, domain-validity or authenticity claim — change the box and the range changes with it.

The scope stays narrow — 36 Python and 15 Node/real-Chrome tests, with 120 exhaustive 1–5D corner problems, all 256 extremal scores independently recomputed from the exact original dual sum, 128 complete native/browser responses and 128 actual Chrome UI combinations, covering zero coefficients and nonunique corners, asymmetric intervals, point boxes, ties, strict schemas, stale and invalid states, physical keyboard, blocked and successful copy, actual JSON Blob and mobile layout; four bounded artifact chunks and a small source-affine declaration reproduce without fitting, while the existing 60 exact active-face optima, full pair replay, training-objective proofs and holdout-poisoning checks remain, and original fits, holdout scores, split and exact training-objective proofs are unchanged — but the lesson travels: when you want to know what a model can say over a region, ask for the exact attained range over that region, with the corners that attain it, because a sample can only ever land inside the range while the range is the answer — and the range is exact only for the box you declared, so state the box. Distinct from 'A valid proof does not authenticate its source', MarginLab's first principle, which is about what a proved bound says about the source — here the bound is attained by named corners and the question is what region the range is over, not whether the proof is genuine — and from 'A perfect training score is not a finished optimization', MarginLab's second principle, which is about a score saturating before the solver finishes — here no score is being chased and nothing is unfinished; the range is complete for its box, and the limit is the box itself — and from 'Keep the exact answer next to the approximation', which is about measuring an approximation against an exact baseline — here the exact range and the approximate plots are kept separate by construction, and the plots are never quoted as the answer.

- [MarginLab](projects/marginlab.md)

## A slice is not a projection

MarginLab's plot shows two features of a thirty-feature model. The other twenty-eight sit at their training means, and the boundary drawn is the model's boundary only there — on that slice. Move any one of the twenty-eight and the boundary moves with it; the picture says nothing about where it goes. A projection would collapse the thirty-dimensional decision surface onto two axes and present the result as the model's boundary, hiding the conditioning the slice makes explicit. The controls keep the distinction honest: the full-30D nearest-neighbor control is not weakened to the displayed two dimensions, so the control answers the thirty-dimensional question while the plot answers the two-dimensional slice question, and the two are never quoted as the same answer.

The trap is reading the picture as "the model's decision boundary" without its address. The picture has the right shape — a line, a region on each side, points on both — and nothing in it says which twenty-eight coordinates were fixed or at what values. A reader who takes the slice for the model will conclude the model separates what it does not, or fails where it does not, on inputs the picture never showed. Name the slice next to the picture: which features vary, which are fixed, and at what values — and when the question is about the full model, answer it with the full-dimensional check, not the picture.

The scope stays narrow — 36 Python and 15 Node/real-Chrome tests, 4,552 original inference checks, eight fits on a frozen 341/113/115 split with validation-only selection, two fits beating the validation choice on test score and staying visible, an installed 11-module/nine-main-command wheel plus the box exporter, 60 exact active-face optima and four full proofs, with the v0.3 box checks (120 corner cases, 256 dual sums, 128 responses, 128 UI combinations) unchanged; original UCI Wisconsin Diagnostic data CC BY 4.0 with exact source hashes — but the lesson travels: when you draw a low-dimensional picture of a high-dimensional model, label it as the slice it is — the coordinates that vary, the coordinates held fixed, and their values — because a picture without its slice is read as a projection, and a projection is a claim the picture never earned. Distinct from 'A narrower window is a new distribution', FlowLab's principle, which is about cutting a distribution down and renormalizing the mass that remains — here nothing is renormalized; the slice conditions on twenty-eight fixed values and the question is which cross-section the picture shows — and from 'A tangent is not a map', DenoiseLab's principle, which is about a local derivative standing in for the whole input plane — here the slice is a global view of one plane, exact on that plane and silent everywhere else — and from 'A sample is not the range', MarginLab's third principle, which is about points inside a box against the box's attained range — here nothing is sampled and no range is claimed; the picture is one exact cross-section, and the question is which one.

- [MarginLab](projects/marginlab.md)

## A deletion report is not a deletion experiment

PolicyLens's v0.2 live row-contribution ledger adds a delete-one-row report for every audited row — 589 audited rows and 589 deletion reports — but the report is explicit about what it holds fixed: the policy and the predictions do not move. Removing a row recomputes the estimator's sum without that row's term; it does not retrain anything, fit a new model, or estimate uncertainty. The number it returns is that row's contribution to the estimate as computed — how much of the reported IPS, SNIPS or DR value that row carries — not what the estimate would have been had the row never been logged. A reader who treats the report as a sensitivity experiment will conclude the policy is robust, or fragile, to data it never re-examined; the report answers a bookkeeping question, and only the bookkeeping question.

The ledger keeps the distinction visible everywhere else it draws a line. Five fixed synthetic cases expose every observed propensity, raw and used weight, direct prediction, signed residual, IPS/DM/DR additive term, normalized SNIPS term, unsupported target action and signed cap removal, and the independent browser evaluator checks bounded target-mixture and single-row reward edits against native Python witnesses, with raw and selected reports always sharing the edited log — so an edit cannot make the two reports disagree about the data. Unsupported actions stay flagged, and zero observed target mass leaves SNIPS undefined rather than silently substituting a value. The signed shared-axis cap path keeps negative DR visible; its samples and all in-range positive observed raw-weight breakpoints have an exact table, while the line connecting samples is a visual approximation for SNIPS, not an optimized cap recommendation, and the entered cap may lie between or outside the plotted samples. ESS stays descriptive, not a confidence certificate or proof that clipping improves an estimate.

The scope stays narrow — 36 Python and four Node/actual-Chrome tests, covering 160 independent Fraction cases, 80 independent integer-grid browser-oracle cases, 95 native/browser edit witnesses and 589 audited rows plus 589 deletion reports, with a seven-module/five-command installed reproduction; the original balanced, clipped, 2000-row oracle and cross-fitted reports, source data and estimator implementations are unchanged, and this remains standard IPS/SNIPS/DM/DR with no new method, causal-identification, confidence-bound or deployment-safety claim — but the lesson travels: when a tool offers a deletion diagnostic, ask what it holds fixed, because a report that holds the model fixed counts one row's contribution to a number, and only a refit can say what would have happened without the row. Distinct from 'A deletion is defined by what you hold fixed', InfluenceLab's second principle, which is about which refit the words 'delete row 5' name — here there is no refit to name; the policy and predictions are frozen by design, and the question is what a report that never refits can and cannot say — and from 'A group deletion is not the sum of its single deletions', InfluenceLab's first principle, which is about exact single deletions failing to add to the group deletion — here each report is a single-row accounting, not a deletion at all, and the composition question never arises — and from 'Edits add; deletions couple', RatingLab's third principle, which is about responses inside a freshly re-solved block — here nothing is re-solved, and the report's honesty is that it says so.

- [PolicyLens](projects/policylens.md)

## A gate that cannot fail is not a gate

A threshold in CI is a claim the run can fail — and a claim nobody has seen fail is a comment, not a check. QuantLab's demo pins its trade-off with three gates: `--max-accuracy-drop` caps what the smaller model may cost in accuracy, `--min-ratio` floors the compression, and `--min-snr-gain` floors the per-channel advantage over per-tensor. The demo runs both commands with their gates plus a negative control: an impossible gate, set so no honest run could pass it, and the run proves it fails. That failure is the point — it is the only evidence the gate is wired to the numbers it claims to guard. A gate that has only ever passed has demonstrated nothing about the code path that fails.

The numbers the gates guard are measured, not asserted. On the checked-in fixture, fp32 test accuracy is 0.9833 and per-channel int8 is 0.9833 — a measured drop of 0.0000 — at 768 B down to 232 B for binary32 row scales, 3.3103x smaller; the magnitude study gives per-channel a +39.14 dB small-row SNR gain over per-tensor, 48.39 dB against 9.25 dB when one row is boosted by a factor of 100. The gates pin those three quantities so a later change that quietly trades accuracy for size, or erodes the per-channel gain, fails CI instead of landing as a silent regression. The suite backs the gates with 39 Python tests, including the 27 unchanged original tests covering quantization range and round-trip error, zero handling, scale counts, size accounting, dataset and training determinism, fixture accuracy parity between fp32 and int8, both sides of the magnitude study and every CLI gate — plus four Node/actual-Chrome tests comparing 52 full reports and 59,004 numeric values — and the failing side is demonstrated by the demo's negative control, not just assumed.

The scope stays narrow — post-training quantization only, no quantization-aware training, int4 or activation quantization; int8 codes now live in real QLB1 files with IEEE binary32/64 scales and CRC32, not byte-arithmetic accounting; the fixture model is tiny, a perceptron-trained linear classifier over hashed features on a deterministic synthetic dataset, one seed reproducing the run bit for bit, so the measurement is exact and real models show non-zero drops, with nothing here claiming otherwise; CI runs the same suite across Python 3.10–3.13 — but the lesson travels: write the threshold with the check, run the impossible case, and keep the failing side demonstrated, because a threshold nobody has seen fail is a wish written in flag syntax. Distinct from 'One scale for a whole matrix is a claim about every row', QuantLab's first principle, which is about what one shared scale does to unlike rows — here the scales are fixed and the question is whether the check on the result can fire — and from 'A green suite is a regression gate, not a certificate', EvalForge's principle, which is about what a passing suite does and does not certify — here the suite's passing is not the point; the point is the gate's proven ability to fail — and from 'A gate with nothing to measure must fail, not pass', loglens's principle, which is about a gate with no measurement failing closed — here the gate has its measurements, and the question is whether it fails when the measurements are bad.

- [QuantLab](projects/quantlab.md)

## Valid syntax is not a valid record

StructGate measures two conformance rates because it makes two different promises. The grammar mask constrains each generated token to the set the JSON state machine allows, so the output parses — 40 of 40 seeded draws are valid JSON. The schema layer adds a second constraint on top of the same masking loop: required keys in a fixed order, typed slots (string, number, bool), no additional keys — and 40 of 40 draws are schema-conforming records. The unconstrained control manages 3 of 40 even for bare parseability, which is the point: a caller that needs a record with the right keys and types gets nothing from a guarantee that only promises parseable text. A JSON object with the wrong keys parses fine and still breaks the consumer, so the two rates are reported separately and neither is allowed to stand in for the other.

The machinery keeps the layers separate so the numbers stay honest. The validator is a stack-based JSON state machine that answers allowed() for any prefix — objects, arrays, strings with escapes, the full number grammar, literals, whitespace — matching Python's json module on 32 adversarial cases, with snapshot and restore for exact queries. The schema layer enforces key order and types during generation rather than in a second pass, so a record can never be valid JSON but the wrong shape by construction. The cost of each layer is measured in the same units as its guarantee: masking renormalizes the distribution to the legal set, -ln(Z) per step is exactly KL(p || p_masked), 1.3496 nats per step for the grammar mask and 0.8209 for the schema mask — so the price of each conformance is a number, not an adjective.

The scope stays narrow — an order-3 character n-gram with add-k smoothing that is exact by design rather than fluent, flat closed records with three slot types, 33 unit tests, CI across Python 3.10–3.13, a fully offline demo asserting both sides of every gate; nested schemas, unions and optional fields are future work, and the KL cost is measured against this model's own unconstrained distribution — but the lesson travels: when a system promises structured output, ask which structure it promises — syntax, shape, or both — and demand the rate for each, because a parseable object with the wrong keys is still a broken record. Distinct from 'A comparison is only as honest as the baseline it is measured against', StructGate's first principle, which is about the control being gated so the comparison cannot silently disappear — here the control is not the point; the question is what each layer of the guarantee itself does and does not promise — and from 'Validate the record before you trust the numbers', which is about validating a trace before any summary is trusted — here nothing is validated after the fact; both guarantees are enforced during generation, and the lesson is that they are two guarantees, not one — and from 'A gate that cannot fail is not a gate', QuantLab's second principle, which is about proving a check can fire — here the checks do fire, and the point is that the first firing says nothing about the second.

- [StructGate](projects/structgate.md)

## A null threshold is not a missing threshold

Classwise SetGuard fits one threshold per class, and each threshold uses only the calibration rows whose true label is that class. That rule has a sharp edge: a class with no calibration rows — or too few for the requested rank — has nothing to rank, so it gets a null threshold and is always included, with no pooled fallback. The null is not a hole in the method; it is the method's answer for that class. A pooled threshold would borrow evidence from other classes and pretend the class had been calibrated; dropping the class would pretend it did not exist; imputing a number would pretend a rank had been computed. The v0.2 ledger makes the decision visible instead of hiding it: every candidate-label decision carries its score, its rank and its inclusion or exclusion reason, and the absent-label infinity boundary is shown as a boundary, not replaced with a finite stand-in. A null threshold looks like a check that can never fail — but it is not a check at all; it is the construction saying, on the record, that this class has no evidence to exclude it, and the honest response to no evidence is inclusion, not invention.

On the development fixture no class is actually empty — the class counts are [43, 37, 50, 35, 35] — so the null path is exercised by the five fixed public synthetic cases, which show pooled and classwise thresholds, every equality tie, the absent-label infinity boundaries and each unlabeled candidate's inclusion or exclusion reason across 19 sampled alpha points. The suite behind the ledger is 41 Python and four Node/actual-Chrome tests checking 95 case/alpha witnesses, 160 independent Fraction games, 80 integer-grid games, 4,199 pooled positions, 8,341 pooled/classwise deletion records and 2,736 candidate-label decisions, with UI switching over all 20 candidate rows and 22 groups; Python ranks with Fraction decimals and JavaScript independently with BigInt rationals, while scores stay binary64. Classwise mode on the same fixture gives empirical coverage 0.9285 at mean size 3.1095 against pooled 0.9235 and 3.017 — but class d's realized coverage is only 0.8859, below the 0.9 target, which the case study reports rather than smoothing over: a per-class threshold is a per-class promise, and one finite split does not prove or refute the population theorem.

The scope stays narrow — 41 Python and four Node/actual-Chrome tests, an installed six-module/six-command wheel reproducing the original demo and 95 witnesses outside the checkout, standard classwise/Mondrian construction under exchangeability within each label with a predictor fixed independently of calibration, no candidate labels fitted, and the original three empirical arms, probabilities, calibration data and scores unchanged; the ledger's 8,341 deletion records are deterministic rank arithmetic — leave each score position out once, threshold the others, count inclusion — not uncertainty or an exchangeability test, and rare classes can make sets much larger or force inclusion on every row — but the lesson travels: when a method has no evidence for a case, record the absence as the decision it is — include, and say why — because a borrowed threshold, a dropped class or an invented number all hide the same fact the ledger is there to show. Distinct from 'A prediction set promises coverage, not confidence in any one label', SetGuard's second principle, which is about what the set promises once the thresholds exist — here the question is what happens before any threshold exists for a class — and from 'A missing rating is not a zero', RatingLab's principle, which is about what an objective sums over while fitting — here nothing is fitted or summed; the null threshold is an inclusion decision, not a term in a sum — and from 'A deletion report is not a deletion experiment', PolicyLens's principle, which is about a report that holds the model fixed and counts one row's contribution — here the ledger's deletion records are the same kind of accounting, deterministic rank arithmetic, but the principle is about the null threshold the ledger exposes, not the arithmetic that checks it.

- [SetGuard](projects/setguard.md)

## A chunk hit is not a document hit

RetrievalBench indexes passages and judges documents, and the two units must not be confused when the score is computed. Its token-window chunking splits each document into overlapping passages, the exact BM25 index ranks passages, and chunk hits collapse back to their parent document before any metric is computed — because the graded qrels grade documents, not chunks. Without the collapse, one relevant document surfacing five chunks would read as five relevant hits, and a system returning many passages of the same document would outscore one returning one passage each of five relevant documents, even though both found the same number of documents the judgments say matter. The collapse is what makes recall@k, precision@k, MRR and nDCG@k count documents: the counted unit is the judged unit, and the per-query and macro-averaged scores, with the weakest queries surfaced for review, are reported at that granularity.

The scope stays narrow — exact Okapi BM25 with no pruning and no ANN approximation, so scores and rankings are deterministic and diffable; 68 Python tests on 3.10–3.13, including all 42 original tests unchanged, and a fully offline demo that asserts the chunked-evaluation parent collapsing and both sides of the --min-recall/--min-precision/--min-mrr/--min-ndcg quality gates, with CI across Python 3.10–3.13 — but the lesson travels: whenever the retrieval unit and the judgment unit differ, collapse to the judged unit before counting, because a score that counts the wrong unit measures retrieval volume, not retrieval quality. BM25 is a lexical baseline — it measures term-matching retrieval, not embedding quality — and the example qrels are illustrative judgments, not a research benchmark. Distinct from 'Measure the retrieval before you blame the answer' (RetrievalBench's first: whether retrieval is measured at all before the generator is judged — here retrieval is measured, and the question is which unit the measurement counts), 'A count is not an expectation' (TagLab: matching an expected count versus meeting an exact total — here the count itself is over the wrong unit), and 'An aggregate improvement can hide a per-context regression' (FisherLab: a weighted total improving while one context regresses — here a single document's chunks inflate the count with no weighting involved).

- [RetrievalBench](projects/retrievalbench.md)

## A negative derivative is not a downhill step

A negative directional derivative says the loss falls if you move a little — and a step of size eta=2 is not a little. DistillLab's v0.2 inspector makes the gap visible with arithmetic, not adjectives: on a supplied two-hidden-unit control, the selected-row loss rises from 1.3466 to 3.6897 at eta=2 although the local directional derivative is negative. The derivative is exact at the point and still wrong about the step, because the step leaves the neighborhood where the linear approximation holds — and the inspector shows the whole update that proves it, not just the slope: hard/soft class derivatives, every simultaneous parameter update across all 254 student parameters, hidden activations, stable CE/entropy/KL terms and all 80 training/320 test predictions, exposed identically by independent Python and browser evaluators. The control is separate from the original trained models, so the overshoot is a property of finite steps, not of the fitted student — and the original results are retained unchanged: 24 Python tests keep all original 12, four Node/actual-Chrome tests check 36 complete native/browser witnesses with 8,900 parameter records and 14,001 evaluation positions, with 160 independent 70-digit Decimal logit controls, 80 uniform-class controls, every-parameter finite differences on the original initialization and the overshoot network, and 21 original backprop/update states; an installed wheel rebuilds the original teacher and six student fits outside the checkout.

The scope stays narrow — the inspector uses stable, unclipped logit-space objectives while the original helpers clamp probabilities at 1e-12, the distinction below that floor explicit; T changes target entropy and objective scale, so loss values across different T do not rank generalization; a lower local loss is not a generalization, calibration, causal-mechanism or deployment guarantee — but the lesson travels: a descent direction is a claim about the infinitesimal, and a step is a claim about the finite, so check the step at the size you will actually take it, because the derivative cannot tell you where the linear regime ends. Distinct from 'A local metric does not certify a finite step', FisherLab's principle, which is about a local geometric object whose finite-step landing differs by chart — here there is no chart and no metric, only a slope whose sign flips when the step leaves the linear neighborhood — and from 'Check a hand-derived gradient against finite differences', which is about verifying that the derivative is implemented correctly — here the derivative is verified, and the failure is inferring a finite step from it — and from 'Decreasing loss is not convergence', which is about a falling loss over training — here a single step raises the loss despite a negative slope, so the step itself is the claim that fails.

- [DistillLab](projects/distilllab.md)

## A zero gap certifies the optimizer, not the reward

AlignLab's v0.2 inspector adds the finite-policy Gibbs optimum, and with it a distinction the original experiment could not draw: how far a policy is from its own optimum, versus how good that optimum is. For positive beta and fixed finite support, `p*_i ∝ q_i exp(r_i/beta)` and the objective gap is exactly `J(p*) − J(p) = beta KL(p||p*)`, so the distance to the optimum is computable in closed form with nothing left to sampling. The noise-control run finishes with an objective gap of about 4e-15 — its optimizer is doing its job, essentially exactly, for a poor reward — yet its synthetic utility is 1.8548647, below the reference policy's 2.0375. The learned-reward run reaches utility 4.5704247 against a finite-policy optimum of about 4.5768334: close to optimal and good, but those are two separate facts, and only the gap identity lets you say which is which. A zero gap is a certificate about the optimizer; it says nothing about the reward, and a policy can be provably optimal and still lose.

The scope stays narrow — one seeded six-action fixture, 47 Python tests including all 15 original tests unchanged, four Node/actual-Chrome tests, 35 full report witnesses and 1,005 trajectory states, fully offline, CI across Python 3.10–3.13 — so the separation is a fixture measurement, not a general claim about alignment — but the lesson travels: whenever the optimum is computable, measure the distance to it separately from the value of it, because conflating the two lets a perfect optimizer launder a bad objective. Distinct from 'Point the optimizer at noise and see what it buys', AlignLab's second principle, which compares two runs on different signals to price the machinery — here there is one run and one signal, and the question is whether its policy is optimal for that signal at all — and from 'Show the bill with the gain', AlignLab's first principle, which is about reporting the price alongside the gain — here the price is already reported, and the question is whether the gain was even the best the stated objective allows.

- [AlignLab](projects/alignlab.md)

## Equivalent factors are not equivalent steps

Two factorizations can describe the same merged model and still take different optimization steps. For a frozen base, `W' = W + BA`, and an invertible change `B' = BC`, `A' = C^-1 A` preserves `BA` in real arithmetic — the models are identical before the step. Ordinary Euclidean SGD on the factors is invariant to orthogonal changes of basis, but a general scaling or shear need not preserve the next merged model, because the update is computed in factor coordinates, not in merged-model coordinates. LoRALab's inspector keeps the finite-step second-order term the first-order story drops: `delta(BA) = -eta_A BB^T G - eta_B GA^T A + eta_A eta_B G(BA)^T G`. For scalar `C = cI`, compensated rates `eta_A' = eta/c^2` and `eta_B' = eta*c^2` reproduce the original next merged model in real arithmetic — a coordinate identity, not a new optimizer. The arithmetic is on display, not asserted: at width 2, epoch 30, the first training example, learning rate 0.1 and scale 4, the before-step logit residual is 0, the ordinary next-matrix difference is 0.0056767304, and scalar compensation gives residual 0 in binary64. The page shows all 31 sampled scales, including the worse steps, rather than selecting a winner.

The scope stays narrow — 31 Python tests across Python 3.10–3.13 including all 14 unchanged original tests, finite differences of every factor coordinate and independent 80-digit Decimal finite-step checks; four Node/actual-Chrome tests over 54 complete reports containing 591,615 numeric values; an installed wheel of eight modules and four commands; seven CI jobs; a synthetic hashed bag-of-words classifier only, with no claim about transformers, Adam, unseen tasks, or the cause of retention loss — but the lesson travels: when the parameters are a factorization, equivalence of the model is not equivalence of the step, so check the update in the coordinates you actually optimize, because a reparameterization that changes nothing about the model can change everything about the next one. Distinct from 'Measure the side you did not optimize' (LoRALab's first: whether all sides of a trade-off are reported — here the trade-off is fully reported, and the question is whether the step survives a change of coordinates), 'A negative derivative is not a downhill step' (DistillLab: a verified slope that still misleads about a finite step — here the slope is not the issue, the step is taken in different coordinates), and 'A local metric does not certify a finite step' (FisherLab: a local geometric object whose finite-step landing differs by chart — here there is no metric and no chart, only Euclidean SGD whose next merged model depends on the factorization).

- [LoRALab](projects/loralab.md)

## Three statistics that agree on ties are not the same statistic

MoeLab v0.2 reports three load-balance statistics side by side, and they are three different statistics: the implementation's mean per-example E sum p², the old prose's E sum(mean p)², and Switch's E sum fP. They average different quantities over different rows, and on uniform ties all three read exactly 1 while every row routes to expert 0 — the one input where they cannot disagree, and where the number says nothing about routing at all. A tie is a degenerate input, not a measurement: agreement there is not evidence the statistics measure the same thing, so the inspector reports all three and the original training is unchanged. The same v0.2 inspector makes the seam concrete rather than merely naming it: retained-probability output is g_e h_e, not a renormalized top-1 weight of one; both neighboring limits and the exact point's chosen branch are shown, a route can change with zero jump, and a triple-tie point can differ from both limits; the fixed-branch derivative g_e [v_e + h_e(b_e - sum_j g_j b_j)] does not differentiate argmax or claim smoothness through a seam. Exact geometry and rounded inference are kept apart on purpose: the mathematics uses exact rational extensions of finite binary64 inputs while the actual rounded path, dot products, softmax and probability-argmax inference are reported separately, and a smallest-subnormal control proves the two owners can disagree.

The scope stays narrow — 32 complete witnesses cover 8,176 evaluation and 2,080 path display positions; 80 independent integer geometries, 160 independent 70-digit Decimal prediction/derivative controls, all 240 destination choices and all 340 row positions; the installed wheel imports seven modules, runs four commands outside the checkout, retrains the aux, no-aux and dense models and compares full data, models and report at 1e-11; the 65-point display curve does not discover boundaries and may miss sub-grid intervals, so exact tables preserve them; linear experts and router, top-1 routing, synthetic fixture, with no token-capacity, dropping, transformer, measured serving-cost, robustness-radius, causal-mechanism or generalization claim — but the lesson travels: when several numbers claim to measure the same balance, check them on inputs where they can disagree, because agreement on the inputs where they cannot is not agreement at all. Distinct from 'A safeguard that never fires is not evidence it works' (MoeLab's first: whether a safeguard earns its place on a fixture where the failure can happen — here the safeguard is not the question, and the numbers are three different statistics that happen to coincide on ties), 'A sum that closes is not a correct split' (DigitLab: a completeness identity true by construction — here nothing sums to a total, and the coincidence is on degenerate input, not an identity), and 'A control that cannot win is not a control' (DenoiseLab's first: whether rivals are built strong enough to win — here the tie input is where the statistics cannot disagree, so it cannot tell them apart, and the failure is treating that forced agreement as identity).

- [MoeLab](projects/moelab.md)

## A byte count is not a file

An analytic byte count is not a file, and QuantLab's packed-weight inspector is the receipt: the earlier 204 B row-scale figure was analytic payload accounting, not a serialized file, and the real QLB1 files are 232 B with binary32 row scales and 244 B with binary64 — 3.3103x and 3.1475x against the 768 B conceptual fp32 baseline, not the 3.765x the payload arithmetic implied. The difference is the format's fixed cost, and it is itemized rather than assumed: a 24-byte versioned little-endian header, IEEE binary32/64 scales, row-major signed int8 codes and a CRC32, with independent Python and JavaScript parsers that reject malformed lengths, counts, dimensions, reserved codes, nonfinite scales and corrupt checksums. The gap is small in absolute terms and that is exactly why it matters: the fixed cost bites hardest where the payload is smallest, which is also where a compression ratio looks most impressive — and the same accounting that understated the file also understated the suite, whose earlier documentation said 28 tests against 39 actually run, including the 27 unchanged original tests. The numbers that replace the estimate are measured end to end: all four storage choices retain 59/60 accuracy on the checked-in synthetic fixture with no examples filtered out, the magnitude study still reports the +39.14 dB small-row SNR gain for row scales, and four Node/actual-Chrome tests compare 52 full independent reports, 59,004 numeric values, every packed byte and every exact rational string.

The scope stays narrow — post-training quantization only, exact bounds on fixed represented-real linear maps rather than floating-point accumulation, a synthetic perceptron-trained classifier over hashed count features rather than an LLM, dequantized scalar inference in the browser rather than integer matmul, no speedup, RAM, checkpoint, authentication or ONNX/GGUF claim, with symmetric absmax quantization, ties-to-even rounding and triangle-inequality error bounds as standard methods — but the lesson travels: when a size claim is the result, ship the file and measure it, because payload arithmetic silently drops every fixed cost the format actually pays, and the ratio it prints is the ratio of a file that was never written. Distinct from 'One scale for a whole matrix is a claim about every row' (QuantLab's first: what one shared scale does to unlike rows — here the scales are fixed and the question is whether the byte count includes the format that carries them), 'A threshold in CI is a claim the run can fail' (QuantLab's second: whether the check on the result can fire — here the check exists and the question is whether the number it guards was measured on a real file), and 'A figure is not decoration for a result' (HamiltonLab: a figure as a claim about the data behind it — here the figure is a byte count, and the claim it makes is about a file that has to exist before it can be counted).

- [QuantLab](projects/quantlab.md)

## An exact margin is not a runtime prediction

QuantLab's packed-weight inspector does not ask the runtime whether a quantized decision is stable — it computes the answer exactly, twice, in two independent arithmetic systems: Python Fraction and browser BigInt dyadics independently compute exact logits for the represented-real maps and the pairwise sufficient margin bounds, including the first-index tie rule, with full rational witnesses available. The margin is a property of the fixed represented-real linear map, not of the floating-point path that happens to evaluate it: the exact bound says how far the decision is from flipping, and a tie is not an ambiguity — the first-index rule decides it deterministically, so the exact decision is defined even where the margin is zero. The runtime binary64 prediction is reported separately, on purpose, because it is a different computation on the same map: a bound on the map is not a bound on the rounding, and publishing only the runtime prediction would let one rounded evaluation silently stand in for the decision itself. The constructed prediction-flip and tie-collapse examples are labeled controls, not trained-model results — they exist to prove the bound can be exercised, that a margin can close and a decision can flip, on inputs the exact arithmetic can still describe.

The scope stays narrow — post-training quantization only; exact bounds apply to fixed represented-real linear maps, not floating-point accumulation, uncertain inputs, unseen accuracy or deployment; a synthetic perceptron-trained classifier over hashed count features, not an LLM; dequantized scalar inference in the browser, not integer matmul; 39 Python tests including the 27 unchanged original tests and four Node/actual-Chrome tests comparing 52 full independent reports, 59,004 numeric values, every packed byte and every exact rational string — but the lesson travels: when a decision has to survive rounding, compute the margin in exact arithmetic and report the runtime prediction beside it, because a prediction without a margin is a claim about one evaluation, and a margin without a tie rule is a claim that stops at the boundary. Distinct from 'Three statistics that agree on ties are not the same statistic' (MoeLab's second: three different statistics that coincide on degenerate tie input, where agreement conceals a difference — here the tie rule does the opposite work, resolving the decision deterministically so the exact margin can be stated at all, and the point is the separation of exact and rounded, not the identity of the statistics), 'A byte count is not a file' (QuantLab's third: whether a size number was measured on a real file — here the numbers exist and the question is which arithmetic owns the decision), 'A zero gap certifies the optimizer, not the reward' (AlignLab's third: a closed-form gap identity separating optimizer distance from reward value — here the separation is between an exact margin and a rounded runtime prediction, different objects with a different failure mode: rounding, not optimization), and 'A control that cannot win is not a control' (DenoiseLab's first: whether rivals are built strong enough to win — here the flip and tie-collapse examples are not rivals in a comparison at all, they are witnesses that the bound is exercisable).

- [QuantLab](projects/quantlab.md)

## A sum of gradients is not the sequence that produced it

EmbedKit's sampled-step inspector does not ask whether skip-gram with negative sampling works — it asks what one sampled step actually does, and the answer is that the order is part of the step. The unchanged trainer applies the positive event and each negative in order, with a ±15 logit clamp, so each event's update feeds the next event's inputs; a simultaneous step on the frozen summed gradient is a different policy, not a faster version of the same one. Both final losses are evaluated on the same fixed event list, so the comparison is clean — and the constructed overshoot control makes the difference undeniable: at lr=2 the simultaneous step increases loss from 16.0007 to 47.9464, while the sequential replay does not. The inspector shows why: every sampled event is exposed with pre/post vectors, raw and clipped logits, the true logistic factor and the original update factor, and every analytic gradient coordinate is compared with a central difference across all 1,593 coordinates, so the divergence is located in the order and the clamp, not in a disputed gradient. Repeated output rows accumulate gradients, and input and output roles are separate tables even when their word names match — the sum hides both facts, the sequence shows them. Twelve original pairs capture 72 actual calls, and seven labeled controls expose repetition, conflicting labels, saturation and overshoot; neither update is claimed to guarantee descent, so the point is descriptive, not a verdict on which policy is better.

The scope stays narrow — a 300-sentence corpus, a 32-word vocabulary, dimension 16, 30 epochs and seed 7, with coherence 1.0000 and separation margin 0.6033 on small synthetic topics separated by construction, so coherence 1.0 is not a natural-language benchmark; 53 Python tests including the 40 unchanged originals and four Node/actual-Chrome tests comparing 19 complete reports, 28,107 numeric values, all 1,593 finite-difference coordinates and all 992 cosine neighbors; no speed, generalization or new-algorithm claim is made — but the lesson travels: when an update is a sequence of events, audit the sequence, because a summed gradient erases the order that decided the result, and a step that looks equivalent on paper can move the loss in the opposite direction. Distinct from 'A negative derivative is not a downhill step' (DistillLab's: a verified slope misleading about a finite step — here the gradient is not in question, both policies use the same frozen gradient and the difference is order and clamping, not slope versus step size), 'Equivalent factors are not equivalent steps' (LoRALab's second: a coordinate change altering the next merged model — here there is no coordinate change, the same coordinates and the same gradient, only the order of application differs), and 'Determinism is what makes a quality number testable' (EmbedKit's first: determinism making a quality number re-runnable — here determinism is shared machinery, and the point is that two deterministic policies on identical inputs still diverge).

- [EmbedKit](projects/embedkit.md)

## A time limit is not a terminal state

PPOlab's training collector reset on a time-limit truncation but recorded only true failures as done, so its GAE calculation used the next episode's reset value and carried that episode's advantage backward — a time limit masquerading as a terminal state, and the tail-value unit test never exercised the collector's internal reset. The corrected collector saves each actual post-step state and value before reset, and two masks separate the questions: genuine termination suppresses bootstrap, while either termination or truncation cuts the recursive advantage trace. A documented seven-array compatibility adapter uses reward augmentation at truncation, with raw rewards and flags in the explicit transition API; the original model, optimizer, loss, physics and GAE helper are unchanged. Ten editable strict-JSON GAE fixtures hold four complete actual trajectories and six labeled controls, retaining all 186 transitions, with a signed contribution heatmap and complete residual table showing where each advantage gets its credit, including exact zeros across resets. Sixteen PPO fixtures cover advantage signs and ratios, and all 57 finite-difference stencils expose left/right slopes — four cross a clip kink and are explicitly not counted as ordinary central-gradient failures, and a ratio outside the clip interval can still have active policy gradients.

The scope stays narrow — 50 Python tests on 3.10–3.13 retaining all 18 original tests, four Node/actual-Chrome tests comparing 26 complete reports and 12,408 numbers, independent 80-digit Decimal residual sums on all 186 GAE rows, the live page running both tanh hidden layers and both heads from all 4,675 original checkpoint parameters across the 30 initial states of the full 20-episode evaluation, and a corrected seed-0 rerun reproducing the historical final return display of 493.6 +/- 27.7 — one run, not evidence of a training improvement; PPO, GAE and CartPole are standard methods, clipping is not a hard KL constraint, and a 500-step replay is not a universal solve — but the lesson travels: when a boundary ends an episode, say which kind of ending it is, because a cutoff and a failure bootstrap differently, and the advantage assigned to every earlier step depends on getting that one flag right. Distinct from 'Test the behaviour you depend on' (the suite pinning the behaviours a pipeline depends on — here the test existed and passed, and the gap is that it never exercised the collector's internal reset; the point is what the boundary flag means, not test coverage), 'A sum of gradients is not the sequence that produced it' (EmbedKit's second: two deterministic policies on identical inputs diverging because order and clamping differ — here the sequence, the gradient and the update are unchanged, and only the reset flag is wrong), and 'A null threshold is not a missing threshold' (SetGuard's: a null recorded as an explicit inclusion decision rather than a hole — here the truncation was recorded as not-done, a present flag carrying the wrong meaning; the fix is to distinguish two kinds of ending, not to record an absence).

- [PPOlab](projects/ppolab.md)

## A mask is not a condition

Masking a distribution to the legal set and renormalizing feels like conditioning on legality, and the cost of the mask even looks like a divergence — but the direction matters. For source next-character distribution p, legal mass Z and masked renormalization q, -log Z is KL(q || p), not KL(p || q): the reverse is infinite whenever the mask excludes positive source mass, and an empty mask does not define a distribution at all. StructGate's inspector keeps both directions and the explicit infinite/undefined status instead of reporting one number. Local masking (p/Z) and exact conditioning are different operations: exact conditioning weights each next character by h(next)/h(prefix), the source probability that a future suffix completes an accepted word, so it never walks into a dead end it cannot leave — local masking can, and the stranded mass stays in a failure sink that full total variation must include. A source-zero conditioning event is explicitly undefined, not an all-zero probability distribution. Per-step conditional KL is separate from a sampled path log-ratio or an expected sequence KL, and means from different masking modes visit different prefixes, so their ordering is descriptive, not a causal effect of a smaller legal set.

The scope stays narrow — exact rational computation for 1–4 ASCII alphanumeric symbols and up to 128 supplied equal-length words of length 1–8 under a first-order Markov source, checked by Python Fraction and independent JavaScript BigInt with a direct P(word)/P(event) check on every conditioned path; six labeled controls cover future acceptance distortion, an unrestricted identity, a locally stranded source-zero branch, a zero-probability event, a three-symbol language and a one-token case. The full original model is preserved — an order-3 smoothed character n-gram from all 287 context count rows and a 46-character vocabulary, trained on all 200 original synthetic records, with 120 full paths and 3,729 emitted characters across 40 seeds in each of none/grammar/schema; 54 Python tests retain all 32 originals byte-for-byte, and three Node/actual-Chrome tests compare 1,251 full prefix reports, 289 source contexts and 741,236 numeric entries. This is not arbitrary-CFG or JSON conditioning, ASAp, or an efficient LLM sampler; Grammar-Aligned Decoding, Local and Global Decoding and the Doob transform are standard methods, not a new algorithm.

- [StructGate](projects/structgate.md)

## A kink is not a failed finite difference

PPO's clipped surrogate is non-smooth by design: where the probability ratio crosses the clip boundary, the objective has a kink, and the left and right slopes disagree — so there is no single derivative there for a finite difference to approximate. PPOlab's inspector makes that visible instead of letting the audit misread it: sixteen fixtures cover advantage signs and ratios, including a complete tiny original-network batch, with every loss term, selected clip branch and output derivative exposed, and all 57 finite-difference stencils expose their left and right slopes separately. Four stencils cross a clip kink, and they are explicitly not counted as ordinary central-gradient failures — a central difference across a kink is not a derivative, and a mismatch there is the kink doing its job, not a gradient bug. The same discipline applies to the clipped term itself: a ratio outside the clip interval can still have active policy gradients, because the clipped surrogate going quiet on one sample is not the policy going quiet — entropy and value gradients are separate questions, and the full policy KL is separate from the ratio. Clipping bounds the step; it does not freeze the model, and an audit that treats either silence as a failure is auditing the wrong object.

The scope stays narrow — 50 Python tests on 3.10–3.13 retaining all 18 original tests, four Node/actual-Chrome tests comparing 26 complete reports and 12,408 numbers, independent 80-digit Decimal residual sums on all 186 GAE rows, the live page running both tanh hidden layers and both heads from all 4,675 original checkpoint parameters across the 30 initial states of the full 20-episode evaluation, and a corrected seed-0 rerun reproducing the historical final return display of 493.6 +/- 27.7 — one run, not evidence of a training improvement; PPO, GAE and CartPole are standard methods, clipping is not a hard KL constraint, and finite differences across kinks are not ordinary derivatives — but the lesson travels: when the objective is non-smooth, audit the slopes on each side of the kink instead of asking a central difference to speak for a derivative that does not exist, because a check that cannot tell a kink from a bug will fail the model for being exactly as designed. Distinct from 'Check a hand-derived gradient against finite differences' (ScratchGPT's: verifying a derivative implementation where the derivative exists and is smooth — here there is no derivative at the kink, so the check itself has to change, not the gradient), 'A negative derivative is not a downhill step' (DistillLab's: a verified slope misleading about a finite step — here the slope is not the issue, the audit's reading of a non-smooth point is), and 'A time limit is not a terminal state' (PPOlab's first: a boundary flag misread as a terminal state — here the misread object is the kink, and the fix is to show both slopes rather than to correct a flag).

- [PPOlab](projects/ppolab.md)

## A saving measured against busywork is not a saving

A cache optimization can look better than it is when the baseline it is measured against does work nobody ever reads. KVLens's original full-recompute path calculated every old query's attention at each step, although this single-block model only uses the last row — so part of the historical pair's 73.08% saving is the baseline doing recompute no consumer needed, not the cache avoiding work that mattered. The fix is to build the strongest no-cache path first: a new final-query-only no-cache path drops the unnecessary work (21,376 counted operations against the historical full path's 34,944), and the optimized cache measured against that stronger baseline saves 58.68% — the headline drops fourteen points once the baseline stops doing work the model never asked for. The two numbers are named comparisons with different prefill policies, not an isolated effect and not a measured speedup; the old 32-token historical fixture still stands at 500,224 versus 45,888 (90.8%), with the same original CI gate. One prediction offers no reuse within either matched pair, and zero predictions perform no work and have no savings percentage at all — the edge cases say plainly where the comparison stops applying instead of letting a percentage imply a saving that does not exist.

The scope stays narrow — vocabulary 16, width 8, two heads, seed 1, prompt [0,1,2,3] and eight predictions; 55 Python tests on 3.10–3.13 retaining all 28 unchanged originals, including 36 randomized configurations and zero/one-prediction controls; three Node/actual-Chrome tests comparing 32 complete native reports, 97 predictions and 66,940 numeric entries; isolated installed-wheel reproduction verifying five module origins, all 32 reports and all four original CLI modes outside the checkout, with regeneration at normalized tolerance 1e-12 restoring checked-in bytes. Counts charge two operations per dot-product term including accumulation and exclude embeddings, positional functions, score scaling, softmax, bias adds, validation and report copying; they do not measure latency, bandwidth, throughput or hardware instructions, and the final-query shortcut applies to this single block — it does not skip representations deeper layers need for their own K/V. This is standard attention/cache reuse, not a new algorithm, trained language model, production cache or GPU benchmark — but the lesson travels: before quoting a saving, check whether the baseline earns its cost, because a percentage measured against work nobody needed flatters the optimization and hides the part of the gain that was never the optimization's to claim. Distinct from 'A saving is a curve, not a number' (KVLens's first: the saving varies with run length at a fixed baseline — here the run length is fixed at the default eight predictions and the number moves because the baseline changed), 'The natural baseline is not the best baseline' (ScoreLab's: the theoretically obvious baseline can carry the worst variance — here the baseline is not wrong by theory but wasteful by construction, recomputing attention no row ever reads), and 'Compare against a baseline, not against nothing' (loglens's: having a baseline at all — here there are two baselines, and choosing between them moves the headline by fourteen points).

- [KVLens](projects/kvlens.md)

## A visible attention pattern is not a contribution

A sharp attention map does not tell you how much the model's prediction depends on that head — it tells you where the head looked, and looking is not contributing. AttnLens's workbench makes the gap concrete: each intervention zeroes a selected head's result slice before the shared output projection, at every sequence position, and later layers recompute all Q/K/V, attention and residuals from the muted state — while the original same-layer attention pattern is still visible in the inspector even when its result is muted. The pattern survives the removal of exactly what it supposedly explains. The fixed seed-7 checkpoint (dim 8, 2 heads, 2 layers, 100 epochs × 64 samples, SGD 0.1) gets 128/128 original held-out examples correct at mean loss 0.000482558 nats; muting all four heads leaves embeddings, positions and the output head, and accuracy falls to 19/128 at loss 2.900797842. All 16 subsets of the four heads are exposed and evaluated on the full 128-example held-out split, every intermediate result retained including non-monotone effects — head effects need not add, and removing more heads does not always cost more accuracy. Matched input edits get the same treatment: all ten recalled-key changes, including the original as a no-op, and one change at each filler position test input sensitivity at fixed weights — change the input, re-run, measure — never read the answer off the map.

The scope stays narrow — one checkpoint, one synthetic recall task, exact zero-vector replacement; zero ablation can produce out-of-distribution activations, and the results are descriptive: no attention-as-explanation or discovered-circuit claim, and neither a one-layer performance gap, a classic induction circuit, seed robustness, production language modeling nor a training improvement is established. The workbench is checked, not asserted: 59 Python tests on 3.10–3.13 retain all 46 originals, and three Node/actual-Chrome tests compare 352 complete tensor reports, 22 full audits and 4,096 held-out predictions, with 590,268 native numeric comparisons and 704 displayed head-row views — but the lesson travels: when a visualization is the evidence, ask what happens to the prediction when the thing visualized is switched off, because a pattern that outlives its own removal was never a measurement of dependence. Distinct from 'A weight is a measurement on a task, not an explanation' (AttnLens's first: quoting a learned weight honestly with its task, gates and checks — here the weight is quoted perfectly and still cannot answer the dependence question, because the pattern is visible even when the head contributes nothing), 'A zero gradient is not a zero effect' (GraphLab's: a local derivative that never claimed to answer a structural change — here the object is not a derivative but a forward-pass pattern routinely read as an explanation, and the intervention removes the head rather than changing the graph), and 'A strong association does not say what an intervention would do' (CausalLab's: an observational joint standing in for an action on the world, where the remedy is a causal model — here there is no confounding to model; the intervention is exact, on one fixed trained model, and the map is the thing that fails to move).

- [AttnLens](projects/attnlens.md)

## A checkpoint is not the weights

A checkpoint that restores the weights but not the rest of the run resumes a different run — silently, with no error. ScratchGPT's previous trainer saved parameters, Adam moments and the update clock but re-created both random generators on restart, and did not bind saved state to the text or numerical options. The v0.2 continuation checkpoint saves the whole state instead: complete named float32 parameters, Adam m/v buffers, update clock, beta values, epsilon and LR, both full PCG64 train/evaluation states including cached uint32 information, text SHA-256, character count, sorted vocabulary and split identity, dimensions, seed, batch, base LR, warmup, clipping and evaluation settings, plus scheduled history, last loss and a runtime fingerprint. The omission controls prove each piece earns its place: on a separate 1,056-parameter synthetic model continued to update 12 across 13 stop boundaries, exact continuation reproduces 13/13 complete final states identically, while legacy RNG reset and missing Adam memory each change the final weights at all 11 interior boundaries — at boundary 4 the maximum final weight difference is about 0.01715618 for RNG reset and 0.02066660 for missing moments — and resetting only the evaluation generator leaves training weights unchanged but changes future scheduled history. The weights load fine in every one of those cases; nothing fails, and the trajectory still moves.

The scope stays narrow — one small-run counterexample on a synthetic model, not a general ranking of state importance; exactness is scoped to uninterrupted/resumed runs in the same numerical environment, a matching fingerprint is necessary, not proof that every runtime detail is identical, and the historical 419,328-parameter Shakespeare checkpoint is preserved, not retrained. The contract is checked, not asserted: 70 Python tests on 3.10–3.13 retaining all 11 original tests, all 13 restart boundaries comparing full parameters, buffers, both RNGs and history rather than final loss alone, independent scalar Adam checks over 38,016 p/m/v values at maximum error about 5.933e-8 and an independent forward over 2,592 logits at about 3.031e-8, and three Node/actual-Chrome tests inspecting 101,376 coordinate-table cells, 468 coordinate views and 72 before/after inference views — but the lesson travels: when a run is supposed to resume, list everything the next step depends on and save all of it, because a checkpoint that restores the weights and drops the rest does not resume the run, it starts a new one wearing the old run's name. Distinct from 'Make work resumable' (flowkit/uptimekit/sre-toolkit: keeping the state that lets a run resume instead of restart — here the resume point exists and loads cleanly, and the question is whether the state it keeps is the whole state), 'Make the same input give the same answer' (a tool's determinism on the same input — here the tool is deterministic and the saved input is what is incomplete, so the same nominal resume gives a different trajectory), and 'A safeguard that never fires is not evidence it works' (MoeLab's load-balancing term never binds on its fixture — here the loader's refusals are armed against failure modes the omission arms proved real, so the guard is justified by a demonstrated failure, not an assumed one).

- [ScratchGPT](projects/scratchgpt.md)

## The loss you report and the gradient you step must be the same function

AttnLens's trainer reported a loss its gradient did not optimize. The old loss was `-log(max(p_target, 1e-12))` — the target probability floored at 1e-12 — while the gradient stayed `softmax - one_hot`, the gradient of the unclipped cross-entropy. Whenever the floor was active, the number on the screen was constant at about 27.63 nats while the gradient was nonzero, so the optimizer kept stepping on an objective the loss did not describe — and nothing failed, because each half was correct on its own terms. The repair is to make the loss the function the gradient differentiates: stable log-sum-exp computes the actual cross-entropy, so logits `[1000, -1000]` with target 1 report their true 2000 nats instead of the floored 27.63, and the repaired loss agrees with extreme-logit finite differences — the check that the number and the step finally come from one function.

The scope stays narrow — one two-layer attention trainer on a synthetic recall task; the original forward weights, optimizer, data, trainer configuration, 46 tests and demo/gates are unchanged, and exported training traces were regenerated rather than silently reused. The check is the point, not the fix: 59 Python tests on 3.10-3.13 retain all 46 originals, with added tests for extreme numerical gradients — but the lesson travels: when the loss is flat and the gradient is not (or the reverse), do not tune the optimizer first; check whether the number and the step come from the same function, because a floor, clip or epsilon in the loss that the gradient never sees is a second objective wearing the first one's name. Distinct from 'Check a hand-derived gradient against finite differences' (ScratchGPT's first: verifying a derived gradient is the derivative of the stated function — here the gradient was correct for the unclipped function, so checking the gradient alone would have passed while the mismatch stood; the failure is between two functions, not inside one derivative), 'A zero gradient is not a zero effect' (GraphLab's: a local derivative that never claimed to answer a structural change — here the shape is reversed, a nonzero gradient beside a flat loss, and the object is the objective itself rather than an attribution), and 'A kink is not a failed finite difference' (PPOlab's: a central difference across a clip kink is not a derivative — here there is no kink in the gradient to misread; the finite difference at extreme logits is the check that confirms the repair, not the thing that fails).

- [AttnLens](projects/attnlens.md)

## A self-query is not a held-out query

The protocol decides the headline before the index is judged. VectorLite's default benchmark is self-inclusive: every vector queries itself, so the query's own id sits in both the exact and the approximate rankings, and the checked-in demo reports a self-inclusive mean recall@3 of 1.0. Change nothing about the index — same query, same 8 planes, seed 0 and strict threshold — and exclude the query id from both rankings, and recall falls to 0: the number that looked like retrieval quality was the protocol finding the query itself. `--exclude-self` removes the query id from both rankings and is labeled leave-one-id-out, not held-out evaluation: duplicate vectors may remain, and `--queries` with external-supplied vectors does not establish an independent split or relevance quality. The same discipline runs through the rest of the v0.2 contract — probability references are labeled as ideal iid-isotropic rebuild expectations, not conditional probabilities for arbitrary fixed planes, and the browser replays the actual exported planes instead of claiming a cross-language PRNG match — so the number, the protocol and the model behind the probability are all stated together. A benchmark that lets the query find itself measures the protocol, not the retrieval: report the protocol next to the number, and read a recall of 1.0 as "the index returns the query" until the protocol says otherwise.

The scope stays narrow — 50 Python tests on 3.10–3.13 including all 31 original tests unchanged, with six original files including corpus, demo and tests byte-identical and the original README preserved byte-exact; 35 retained audits including the original 8D data, synthetic 2D/5D controls, exact sign boundaries, zero vectors and the self-exclusion pair, regenerating byte-for-byte in the tested environments; 120 cosine pairs checked with 90-digit Decimal arithmetic, rational binomial tails, exhaustive 8-bit sign patterns, full-circle angular geometry and 1,200 seeded Gaussian rebuilds; independent scalar JavaScript over 20,784 numerical fields across 643 threshold rows, with actual Chrome verifying all 332 vector rows, 643 threshold rows and 5,856 projection rows; an installed wheel imported outside checkout with six module origins, all 35 full audits, the audit CLI and the original-query CLI — but the lesson travels: when the test item is also in the candidate set, the protocol is part of the result, so name the inclusion rule with the score, because a perfect recall under a self-inclusive protocol is a property of the protocol, not evidence about the retrieval. The bounds stay stated: an O(N) signature scan, not a bucketed or sublinear index; candidate rescoring fractions are not latency; canonical score/id ties are a declared ground truth, not human relevance judgments; the audit is bounded to 64 items, 16 dimensions, 128 bits and a 128KiB strict JSON spec; and the vectors are synthetic, not learned embeddings or a retrieval-quality benchmark. Distinct from 'Keep the exact answer next to the approximation', VectorLite's first principle, which is about measuring an approximation's error against an exact baseline — here the exact baseline is fixed and the question is what the benchmark protocol itself contributes to the number — and from 'A row left out is not a row held out' (TreeLab: exclusion defined at the wrong granularity, a duplicate group keeping a row in the bag — here nothing is excluded by mistake; the query is deliberately in the corpus, and the question is whether the protocol counts finding it as retrieval) — and from 'A held-out label is not a held-out node' (GraphLab: labels held out while nodes and edges stay visible — here no label is held out at all; the test item is the query, and the protocol decides whether returning it counts) — and from 'Measure the retrieval before you blame the answer' (RetrievalBench: measuring the retrieval layer before judging the generator — here the retrieval is the thing measured, and the question is whether the measurement's own protocol is what produced the score).

- [VectorLite](projects/vectorlite.md)

## A lower threshold is not a lower recall

Lowering a retrieval threshold feels like it should trade something away — a looser filter, a worse result. VectorLite shows it cannot, for the threshold it documents: for a fixed query, planes, k and score/id order, an admitted canonical exact top-k item must survive exact candidate rescoring, because fewer than k corpus items precede it in the full ordering, so recall is the fraction of ground-truth ids admitted. Lowering the threshold creates nested candidates — everything admitted at the higher threshold is admitted at the lower one — so the recall cannot drop. The v0.2 contract corrects the earlier suggestion that lowering the sharing threshold can reduce recall for the same fixed index and score/id ordering; that suggestion is withdrawn, not hedged.

The guarantee is checked, not asserted: per-threshold marginal admission tails, expected candidate counts and expected canonical recall are computed from the binomial shared-bit law — a random isotropic plane agrees with probability p = 1 − θ/π — and the browser checks 643 threshold rows with 20,784 independent scalar-JavaScript numerical fields, with actual Chrome verifying all 643 threshold rows. The scope stays narrow — candidate events share planes and can be correlated, so no binomial law for the total candidate count is claimed; the audit is bounded to 64 items, 16 dimensions, 128 bits and a 128KiB strict JSON spec; this is an O(N) signature scan, not a sublinear index — and the claim says nothing about changing seeds or bit counts, semantic ties or another retrieval implementation — but the lesson travels: when a parameter only widens the candidate set, check whether the sets nest before assuming a tradeoff, because a threshold that only adds cannot take away. Distinct from 'Keep the exact answer next to the approximation', VectorLite's first principle, which is about measuring an approximation's error against an exact baseline — here the baseline is fixed and the question is whether recall can move at all when the threshold moves — and from 'A self-query is not a held-out query', VectorLite's second, which is about the benchmark protocol contributing to the number — here the protocol is fixed and the claim is about the index parameter itself — and from 'A wider beam is a bigger beam, not a better one', DecodeLab's second, which is about beam width being non-monotone because pruning can discard the oracle — here the candidate set nests, so no step removes what a higher threshold admitted; monotonicity comes from nesting, not from keeping more — and from 'A threshold in CI is a claim the run can fail', QuantLab's, which is about a gate threshold in a test suite — here the threshold is a retrieval parameter, not a gate.

- [VectorLite](projects/vectorlite.md)

## A lossy view of a number is not the number

A number and the way it is displayed are two different things, and GroundCheck treats them that way: exact decimal-string equality replaces float conversion, because converting to float collapsed adjacent large integers into the same value and made distinct 310-digit finite numbers compare equal. A float is a lossy view — it can only hold the nearest representable value — so two different numbers can share one float, and any check that compares floats is comparing the views, not the numbers. The same discipline applies to the display: scores retain full precision before thresholds and gates, so a displayed 0.6667 is not allowed to pass a 0.66668 gate when its actual value is 2/3 — the display rounds up past the gate while the value itself sits below it, and gating on the display would pass what the value fails. Numbers before terminal periods are recognized without treating dotted versions as numeric evidence, so `1.57` stays one number instead of two sentence fragments.

The check is verified against the numbers themselves, not their renderings: 66 Python tests retain all 43 originals unchanged, with the 50 retained reports covering 25 controls in both scopes — wrong, missing and post-period citations, semantic false positives, split-document claims, exact decimal collisions, zero-content inputs and tie rules — and exact Fraction comparisons plus exhaustive small token subsets check the arithmetic. Four Node/actual-Chrome tests check full-report parity, every displayed source score, edits and export, and 320/390/1280 containment, and an isolated installed wheel verifies eight module origins and both the audit and original CLI paths outside the checkout, with Python 3.10–3.13 regenerating the same artifacts. The bound is stated with the check: lexical support is not semantic entailment, factuality or source authentication, and these are synthetic controls, not a RAG-quality benchmark — but the lesson travels: whenever a value passes through a lossy representation — a float, a rounded display, a truncated printout — compare the value, not the view, because the view can make different numbers look the same and a failing value look like a pass. Distinct from 'A lexical check can catch a fabrication, not certify a truth', GroundCheck's first principle, which is about what a lexical check can certify about a claim — here the question is whether two numbers are the same number at all, not whether a claim is supported — and from 'A float pass at the boundary is not an exact pass', RobustLab's, which is about a float computation failing an exact check — here the check avoids the float entirely, and the risk is comparing the views instead of the values — and from 'A repaired number needs its own audit', TransportLab's, which is about auditing the rounded number that ships — here the rounded number never ships, only displays, and the gate must use the actual value.

- [GroundCheck](projects/groundcheck.md)

## A falling mean is not a falling task

A whole-run mean can fall while every matched task improves: the candidate may add hard tasks and omit easy ones, so the mean moves because the task set changed, not because any task got worse. EvalForge's original comparison hid exactly that — it silently collapsed duplicate ids and trusted stored summaries, so a changed cohort could read as a regression (or an improvement) that no task actually showed. The comparison now validates result rows, rejects duplicate ids, and recomputes the all-task and matched-task summaries separately, so the headline mean and the per-task record are read as two different claims. The per-task gate is preserved: a score drop beyond tolerance, a lost pass, or a missing baseline task fails, and added tasks do not fail it — every matched task retains its complete normalized baseline/candidate record, delta, margin, pass-loss and score-drop flags and classification, with native result-level metadata retained alongside. Equal ids remain supplied evidence, not proof that the task definitions or scorers match, and persistent failed or error tasks may pass a comparison if they do not regress. A comparison PASS is a verdict on the matched tasks, not an absolute evaluation-quality verdict — and it says nothing about the mean.

The scope stays narrow — 92 Python tests on 3.10–3.13, including all 68 original tests unchanged, all 780 short integer difference vectors against separate brute-force signs, small pass tables, 200 seeded original-gate references, and malformed rows, duplicate ids, stale summaries and metadata retention; 24 complete retained reports independently compared at all 11,808 numeric and 2,691 other scalar leaves; actual Chrome verifying 53 paired rows, 564 sign assignments, 118 displayed full records, 47 binomial rows, all chart dots and pass cells, export and invalidation, and 320/390/1280 containment; a fresh public source plus an isolated installed wheel outside the checkout checking nine module origins, all retained reports and the audit, mock-adapter and compare CLIs with HTML, JUnit, Markdown and SARIF outputs. The paired arithmetic is bounded and inspectable: sign flips enumerate every assignment of nonzero .001-score differences with inclusive absolute two-sided tails, zero differences factored out rather than silently dropped from coverage, and exact McNemar exposes the four paired pass-status cells and every binomial count with the doubled lower tail capped at one — it tests binary pass marginals, not score means. No pairs is undefined, all ties give p=1 rather than equivalence, and independent and exchangeable pairs, task selection, changed scorers, dependence and repeated benchmark searches limit interpretation, with no significance threshold, multiplicity correction or automatic inference gate added — established methods made inspectable, not a new statistical method or evidence of model superiority; the inspector is bounded to 12 rows per side and eight matched pairs on a .001 score/drop grid, native comparison is not, retained timings are one local execution rather than a latency benchmark, and no API key, paid API or hosted model call is used — but the lesson travels: whenever a summary covers a set that can change, report the matched-task result next to the all-task mean, because a mean that mixes different tasks is a statement about the mix, not about the tasks. Distinct from 'An aggregate improvement can hide a per-context regression', FisherLab's principle, which is about a weighted total improving while one context regresses under a shared parameter — here the total falls, no task regresses, and the mechanism is the task set changing, not a parameter trading contexts off — and from 'A green suite is a regression gate, not a certificate', EvalForge's first principle, which is about what a passing suite can and cannot certify — here the question is what a falling mean means, and the comparison PASS is a per-task verdict that says nothing about the mean.

- [EvalForge](projects/evalforge.md)

## A complete record is not a complete explanation

AgentTrace's graph and timing inspector shows the whole record: every endpoint, interval segment, parent path and relation, normalized record and p95 term, recomputed independently in Python and JavaScript with a current JSON export, so nothing about the run is hidden. But a display that hides nothing can still be misread, because the record's terms mean exactly what they record and nothing more: a parent link is a recorded link between steps, not a causal dependency — it says this step named that step as its parent, not that the parent caused it. Recorded coverage and overlap are intervals in the record, not CPU time, idle time, waste or utilization — two steps overlapping in the record does not mean two cores were busy, or one was waiting, or either was wasted. Completeness of display is not completeness of interpretation.

The display is checked, not asserted: 57 Python tests retain all original 33 tests, with 24 synthetic controls and 11,110 interval checks, plus an isolated installed-wheel reproduction — and what those checks verify is the record's arithmetic, not the reader's interpretation. The scope stays narrow — standard library only, CLI, fully offline with CI across Python 3.10–3.13, no model or API call — but the lesson travels: read the legend before reading conclusions off the picture, because a graph drawn from a record inherits the record's definitions, not the reader's intuitions. Distinct from 'Validate the record before you trust the numbers', AgentTrace's first principle, which is about whether the record is sound — malformed events, duplicate step IDs, unknown parents — here the record is valid and fully displayed, and the question is what its terms mean — and from 'A visible attention pattern is not a contribution', AttnLens's, which is about a pattern that cannot answer the dependence question at all — here the record does answer its own questions exactly, and the error is importing meanings it never claimed.

- [AgentTrace](projects/agenttrace.md)

## A passing gate is not a clean scan

A passing security gate can hide findings before the gate even runs. Severity filters remove rows, baselines suppress known identities, and an incomplete filesystem scan can look like an empty result — so a verdict of zero findings says nothing on its own about whether anything was found. PromptGuard’s answer is to witness every disappearance: `scan --audit` retains every current row with its fingerprint, filter eligibility, baseline match, disposition, used and unused identities, reported payload and gate decision, and the browser independently recomputes every stage in JavaScript with WebCrypto, exposing every current and prior row and the full selected record, drawing the stage path and exporting the complete current JSON. The native fixes close the holes the audit exposed: full lines are redacted before truncation and metadata excerpts are redacted, every recognized sensitive match on a line is enumerated instead of only the first, and the scan counts the files it successfully read and refuses a successful gate on scan errors — an incomplete scan cannot write a new baseline either, and strict baseline loading rejects malformed SHA-256 identities, duplicate JSON keys and invalid encoding. Even the identity scheme states its own limits: baseline identity excludes line and severity and normalizes slashes and whitespace, which can alias distinct paths, and metadata now binds its original first line privately when redaction changes it, so rotated material changes identity and old metadata entries surface again for review — a documented migration, not silently presented as unchanged behavior.

The witness is checked, not asserted: 87 Python tests on 3.10–13 retain all original 68 tests, fixtures and the offline demo unchanged; 13,320 exhaustive small policy controls derive expected row indices and exit precedence separately; 27 complete native and independent-JavaScript reports compare 735 numeric and 1,443 other leaves; actual Chrome checks 50 current rows, 17 prior rows, 16 baseline identities across cases, 50 full records and 181 exact-position stage circles, all table, card, gate and payload fields, export, stale invalidation and asynchronous races, with containment checked at 320, 390 and 1280 pixels; and an isolated installed wheel outside the checkout verifies eight module origins, all 27 reports, all CLI formats, baseline suppression and incomplete scans. The scope stays narrow — only reported findings reach severity and count gates, the count gate fails strictly above its cap, scan errors dominate with exit 2 and gate failure returns 1, and a passing policy does not prove prompt safety or detector completeness; the historical risky fixture still produces eight findings and the original analysis and HTML remain byte-exact. Distinct from ‘Lint the prompt like code’, PromptGuard’s first principle, which is about giving prompt files the same automated review as application code — here the review exists, and the question is what its passing verdict means — and from ‘A gate that cannot fail is not a gate’, QuantLab’s, which is about proving the failing path is wired with a negative control — here the gate can fail, and the question is whether its pass hides findings — and from ‘A complete record is not a complete explanation’, AgentTrace’s second principle, which is about a complete display being misread — here the display is the verdict itself, and the question is whether every disappearance behind it is witnessed.

- [PromptGuard](projects/promptguard.md)

## The best path is not the likeliest transcript

A frame-level best path is not the same as a highest-mass transcript, and a decoder that crowns the single best path can report the wrong answer with a straight face. CTCLab makes the gap visible on tiny synthetic logits: two uniform blank/A frames assign 0.25 to the empty output and 0.75 to A, so the greedy path and the summed transcript mass disagree — and the transcript wins. The check is exhaustive, not sampled: dependency-free Python computes blank-expanded-state log-space forward/backward with full state/symbol posteriors and logit gradients, while an independent oracle collapses all C^T paths and aggregates transcript masses, so every contribution to a target likelihood stays inspectable. The evidence is 25 Python tests on 3.10–3.13 with 90 seeded 90-digit Decimal controls, 40 independently enumerated state-sequence controls and 300 central finite-difference gradient coordinates; twenty retained reports match 5,764 numeric and 650 other leaves in independent JavaScript, and real Chrome checks 176 state rows, 142 gradient rows, 449 path rows and 143 transcript rows. The controls pin the semantics down: adjacent repeated labels need a separating blank, empty input supports only an empty target, changing the blank index must preserve the computation, ordinary probabilities can underflow while log likelihood stays finite, and impossible targets retain undefined loss and gradients rather than silently zeroing them. The scope stays narrow — at most six frames, four classes and 1,024 paths; established CTC on tiny synthetic logits, not a trained recognizer, speech/OCR benchmark or novel algorithm — and ranking uses disclosed 1e-8-nat score buckets followed by lexicographic indices, with raw masses and the raw greedy gap still available. The lesson travels: whenever a score is a sum over hidden alignments, compare the sums, not the single best alignment — the likeliest answer is a property of the whole distribution, not of its argmax. Distinct from 'A search that runs out of budget owes you the gap', TreeLab's principle, which is about a search that stops before it can certify anything — here the computation is exhaustive and complete, and the question is what the complete answer means — and from 'Decreasing loss is not convergence', PartsLab's principle, which is about a falling objective that never meets its stopping test — here every fit is exact and the loss is not the issue; the issue is which summary of the exact distribution you report — and from 'A sufficient certificate is not a complete detector', SparseLab's principle, which is about a certificate that stays silent outside its scope — here there is no certificate at all, only the full enumeration, and the error is reading the argmax as the answer.

- [CTCLab](projects/ctclab.md)

## Equal marginals are not independence

Two items can have the same inclusion probability and never appear together. DPPLab makes the gap exact on a three-item kernel L = [[4,4,0],[4,4,0],[0,0,1]] with normalizer 18: items 0 and 1 are each included with probability 4/9, but their joint inclusion is zero — while independent items with the same marginals would co-occur with probability 16/81. Item 2 is genuinely independent, included with probability 1/2. The marginals are identical in the two stories; the joint law is not. A summary that reports only per-item rates cannot tell repulsion from independence, and a system that treats "included 4/9 of the time" as a property of an item, rather than of the joint law, will be surprised exactly when the items interact.

The same confusion shows up when conditioning is mistaken for fixing a size. Include/exclude conditions are separate from an optional fixed total size k: the residual kernels condition only on what is in or out, and an identity kernel with k=1 gives zero probability to the pair even though its event-only inclusion determinant is 1/4. Impossible events return null laws instead of a silently repaired answer, and duplicate-item controls separate zero co-occurrence from equal-marginal independence — the two failure modes look the same in the marginals and opposite in the joint. Mean size 25/18 and variance 113/324 describe the whole law, not any single item.

The scope stays narrow — 24 Python tests on 3.10–3.13, including 120 determinant references, 50 inverse identities, 140 full Gram-kernel oracles, 100 conditioning oracles, 40 fixed-k scale controls and 20 sign-conjugation controls; 24 complete reports match all 4,050 exact native/BigInt leaves, and actual Chrome verifies 252 subset rows and full records, 786 matrix cells, 84 pair rows and 504 bar fraction/geometry witnesses. One to five real-symmetric PSD likelihood-kernel items, at most 32 subsets, every principal minor checked exactly, singular valid kernels kept — established bounded L-ensembles, not learned relevance, a scalable sampler or a downstream quality result. Distinct from 'Zero correlation is not independence', which is about a zero in one observable hiding dependence in another — here the marginals match exactly and the joint still differs — and from 'Marginals do not compose when randomness is shared', which is about a joint release being worse than its marginals because one shared coin couples two releases — here there is one kernel, and the repulsion is in the law itself rather than in how it was released.

- [DPPLab](projects/dpplab.md)

## A guarantee is not an optimum

SubmodLab's default control makes the gap between a guarantee and an optimum visible on six rows: with k=2, greedy starts with the item covering four rows and adds one more for value 5, while items 1 and 2 together cover all six rows — the exact optimum is 6, so greedy's actual ratio is 5/6. The finite-k worst-case factor is 3/4, and that number is a floor over instances, not a result: it says no instance can do worse than 3/4, this instance does better at 5/6, and neither number is the optimum. The certificate keeps the same discipline: for any visited prefix A, the bound uses the k largest remaining gains, because an optimal set need not contain A — substituting the remaining budget k-|A| would certify 5, below the true optimum 6, and a certificate that certifies a false bound is worse than no certificate at all. The actual ratio, the certificate bound and the worst-case factor are three different numbers, and the report keeps all three.

The same confusion shows up wherever a ranking is read as a selection. On a duplicate-representative matrix [[5,5,0],[0,0,4]], singleton top-k picks the duplicates for value 5 while updated greedy picks complementary items for value 9, the exact optimum — the top-k list is a ranking, not a set, and a set built from a ranking inherits the ranking's blind spot. A monotone synergy table gives greedy 3 against an optimum of 10 and fails submodularity, while a submodular but nonmonotone table makes exactly-k greedy end at 0 against an at-most-k optimum of 2 — both withhold theorem and bound fields rather than printing a guarantee their assumptions do not support. Rounding keeps the same honesty: a two-item half-probability control has expected count 1 yet exceeds budget 1 with probability 1/4, and its duplicate-coverage expectation of 3/4 rounds to a singleton worth 1 — the expectation is a number about the distribution, not a promise about the rounded set.

The scope stays narrow — 33 Python tests on 3.10–3.13 (24 for the selection audit, 9 for deterministic rounding), including 120 independently enumerated facility controls, 100 arbitrary-table full-lattice comparisons, 40 positive-scale controls, 30 equivalence controls and 60 all-subset prefix-bound controls; 24 complete reports match 16,426 exact native/BigInt leaves and 21 rounding reports match 10,682, with actual Chrome verifying 360 subset rows/bars and 2,056 full records. At most six selectable items, 64 subsets and eight facility rows; exact rational strings, no learned embeddings, cost/knapsack or matroid constraints, lazy or stochastic greedy, runtime benchmark, downstream quality metric or new theorem — and the theory is credited to Nemhauser, Wolsey and Fisher, not claimed as original. Distinct from 'A guarantee is a contract with its assumption', SetGuard's principle, which is about a guarantee going void when its assumption breaks — here the assumptions hold and the guarantee still is not the optimum — and from 'An aggregate improvement can hide a per-context regression', FisherLab's principle, which is about a mean improving while matched tasks worsen — here there is one instance, one greedy run and one optimum, and the gap is between the guarantee and that instance's own optimum — and from 'A search that runs out of budget owes you the gap', TreeLab's principle, which is about a search that stops before it can certify anything — here the certificate is complete and exact, and it still only bounds.

- [SubmodLab](projects/submodlab.md)

## A sum is not a max

FactorLab's retained control makes the difference between summing and maximizing visible on one tiny factor: on scope [0,1] with little-endian values [6,5,0,5], x0 is the MAP decision and x1 is hidden. Summing x1 out first gives x0 masses [6,10], so the optimum is x0=1 with probability 10/16=5/8. Maximizing x0 first instead computes max(6,5)+max(0,5)=11 — an upper bound that is not an attainable marginal-MAP mass, because no assignment of x0 reaches 11. The joint mode is x0=0,x1=0 with weight 6, and projecting it onto x0 picks the wrong marginal decision. Summing, maximizing the joint assignment and maximizing the marginal decision are three different questions, and answering one while reporting another is not a numerical instability — it is the wrong question, answered exactly.

The same confusion shows up wherever an elimination order is treated as a free choice. On a separate five-variable star, hub-first and leaves-first schedules give an identical all-sum partition, but their dense joined-table counts are 62 and 18, with induced widths 4 and 1 — the order changes the allocated table size while preserving the answer, when sum and max are not mixed. Mixing them changes the question itself: sum-before-max is sufficient for a marginal-MAP answer, not necessary, since disconnected or tied factors can make an interleaving agree — and an invalid schedule returns a bound, not an assignment or a posterior probability. A bound is a statement about the answer's range, not a candidate answer.

The scope stays narrow — 24 Python tests on 3.10–3.13, including 160 dense scalar references, 100 full current-factor-product references, all orders on 20 random four-variable graphs for all-sum, all-max and mixed queries, 40 rescaling controls and an independent adjacency-set census; 24 complete native/BigInt reports match 23,114 exact leaves, with actual Chrome checking 1,939 complete selected records — 325 joint, 406 joined products, 203 reductions, 75 steps, 69 sliced factors and 861 census records — plus 21 fill edges, 75 bars and 320/390/1280 containment. At most five binary variables, ten factors and 32 full assignments; exhaustive reference and census work is exponential, negative factors are rejected because only nonnegative multiplication supports the max distributivity used here, and zero evidence mass leaves probabilities null rather than inventing them. Established variable elimination and mixed-query theory is credited to Peyrard et al.; Liu and Ihler; Urtasun and Hazan; MIT 6.438; Gormley; and Lee, Marinescu, Dechter and Ihler — no belief propagation, variational inference, anytime search, learned predictor, new algorithm or formal verification is claimed. Distinct from 'Marginal peaks are not a joint partition', SegmentLab's principle, which is about per-gap marginal winners failing to compose into an admissible partition — here the marginal is computed exactly and the error is maximizing where a sum was required — and from 'Optimizing the bound is not recovering the marginals', VariLab's principle, which is about an optimized ELBO diverging from the target statistic — here no optimization runs and the bound is exact, yet it is still not the mass — and from 'The most probable partition is not the cheapest decision', SegmentLab's principle, which is about a MAP partition and a least-costly decision disagreeing under supplied loss — here there is no loss function at all, and the max-first number is not a competing decision but an upper bound no assignment attains.

- [FactorLab](projects/factorlab.md)

## A local minimum is not a global optimum

CutLab's strict single-flip control makes the gap visible on a two-variable fixture: the search starts at mask 0 with energy 2, and both one-flip neighbors cost 3, so it stops — by its own rule, correctly, and wrong. Mask 3 has energy 0. Nothing in the search's stopping condition was violated; the rule itself is what failed, because "no single flip improves" is a statement about the neighborhood, not about the landscape. The certificate is what closes the question: a feasible flow of 1 plus an offset of −1 proves the optimum is 0, and matching flow and cut leave no room for a better assignment to hide. The same control set keeps a second failure honest: unary-only chooses energy 5 in a separate coupling control while two exact tied minima cost 3, and the gap of 2 is labeled as an incomplete baseline, not a solver benchmark — a baseline that cannot see coupling is not evidence about the solver.

The solver does not report one cut as the only answer when several labels are ambiguous. Signed rational unary and asymmetric submodular pair tables reduce to a directed s-t network with original energy equal to offset plus cut capacity, non-submodular pairs refused rather than clipped, and every terminal shift retained; a six-augmentation fixture actually needs a reverse variable arc to cancel earlier flow, and every cut exposes capacity minus flow as outgoing residual slack. The residual SCC graph recovers the whole forward-closed family of minimum cuts with forced and free labels — and free does not mean independently selectable: tied agreement has two free variables but only two optimal masks, while the zero six-variable graph has all 64 assignments optimal. The family, not a single mask, is the answer.

The scope stays narrow — 21 Python tests on 3.10–3.13, including 250 independently enumerated original-energy cases, 160 every-cut slack audits, 100 positive-scaling/offset controls and 80 variable relabelings; 24 complete native and independent BigInt reports agree on 24,624 exact scalar leaves, with actual Chrome checking 570 cut records, 56 flow states, 73 pair reductions, 180 residual records and 50 local states, plus 87 terminal rows, 449 SVG edges and 4,166 node colors; an installed wheel reproduces all 24 reports and both CLI routes with four module origins checked. At most six binary variables and finite rational costs; established binary submodular inference and maxflow/mincut, not a new algorithm, with theory credited to Kolmogorov-Zabih and the Picard-Queyranne cut-family background — and no trained model, real-image segmentation, multilabel or higher-order method, or machine-checked formal proof is claimed. Distinct from 'A guarantee is not an optimum', SubmodLab's principle, which is about a complete exact certificate that still only bounds — here the certificate is exact and attains the optimum, and it is the search's stopping rule that falls short — and from 'A search that runs out of budget owes you the gap', TreeLab's principle, which is about a search that stops because its budget ran out and must report the gap — here the search finished by its own rule with budget to spare, and the gap is in the rule, not the budget — and from 'A stopping rule is not a mode certificate', MixtureLab's principle, which is about a norm stop that certifies nothing about the point — here a flow/cut certificate proves the global optimum, and the local rule is what falls short of it.

- [CutLab](projects/cutlab.md)

## A label that leaves can come back

CutLab's response-path inspector makes the non-monotonicity visible on a single rational parameter: vary the binary unary costs and keep the complete optimum family on every closed region, open cell and breakpoint, including point-only optima and persistent ties. Every assignment keeps its affine line and every line comparison keeps its exact inequality, so a label's membership in the optimum family is read off the region it sits in — not off the label. With mixed-sign slopes the lines cross and re-cross: a label can be optimal, leave the family as the parameter moves, and return later. Any method that assumes labels enter the optimum once and stay — nested labels, a monotone parametric-maxflow sweep — is wrong on exactly this material, and CutLab claims no such guarantee: the inspector enumerates all 2^n assignments for at most six variables instead, and independent graph-cut audits check every boundary and cell witness.

The evidence is 18 synthetic controls retaining 214 assignment lines, 6,084 inequalities and 92 full flow/cut witnesses, with the original flow/cut functionality and its 21 Python tests unchanged. The scope stays narrow — at most six binary variables and finite rational costs; exhaustive family verification is exponential, and no nested-label or scalable parametric-maxflow guarantee is claimed. The lesson travels: when the answer is a set that depends on a parameter, report the family on every region, not a single label and not a monotone story about it — optimality is a property of the region, not of the label. Distinct from 'A local minimum is not a global optimum', CutLab's first principle, which is about a search stopping early on one fixed landscape — here the landscape itself moves with the parameter, the search is exhaustive on every region, and the error is assuming the optimum family is nested — and from 'A guarantee is not an optimum', SubmodLab's principle, which is about a complete exact certificate that still only bounds — here the exact family is enumerated on every region, and the question is not whether a bound attains but whether membership in the family is monotone — and from 'A deletion is defined by what you hold fixed', InfluenceLab's second principle, which is about which refit the words name — here the graph and pair tables are held fixed while one rational parameter moves, and the question is whether the optimum family changes monotonically in that parameter.

- [CutLab](projects/cutlab.md)

## A minimal repair is not a cheapest repair

Diagnoselab makes the gap between minimal and cheapest visible on one default control: given fixed hard CNF and removable soft clauses, a repair is a set of clauses whose removal restores consistency, and a repair must hit every minimal unsatisfiable subset — every core, not merely one. Inclusion-minimal means nothing can be taken out of the set while it stays a repair; it says nothing about what the set costs. The default control puts the two apart: one removal at cost 5 is a minimal repair, minimal by cardinality, and two removals costing 2 together are a cheaper repair that removes more. A system that reports "minimal repair" and lets it be read as "cheapest repair" will pay 5 for a problem it could have fixed for 2, and the enumeration is what keeps the two honest: every relative MUS and every MCS is listed, every candidate's intersections with both families are checked for minimal-hitting-set duality in both directions, all MUS member-deletion model lists and all MCS reinsertion UNSAT references and unique-hit core witnesses are retained, and every cardinality and cost tie is kept, including the empty-family and empty-core boundaries. An inconsistent hard background is the limiting case: it gives an empty relative core and no soft repair at all, not a repair of cost zero.

The same confusion shows up one level up, in what a repair entails. The repair-policy consequences distinguish every/some repair from every/some surviving model: a query can hold in every repair, in some repair, in every surviving model, or in some surviving model, and those are four different claims. All tied minimum-cost and minimum-cardinality policies are kept rather than breaking the tie silently, the shared-clause intersection is a separate baseline with strict counterexamples rather than a shortcut for "what every repair agrees on", and a family with no repairs is inapplicable, not vacuous certainty — there is nothing for the quantifier to range over, so "true in every repair" is not a finding. Every repaired formula retains full truth-table query witnesses and the full deterministic search tree of the formula conjoined with the query's negation, so each entailment claim is a checked record, not a slogan.

The scope stays narrow — 17 Python test functions on 3.10–3.13, including 180 all-proper-subset family oracles, 80 complete-trace controls, positive-cost scaling, clause permutation, literal order and repetition, variable complementation, validation with no mutation, and invalid CLI output preservation; four Node/actual-Chrome tests compare all 18 retained reports on 74,292 exact scalar leaves and add 90 independent truth-mask controls, with actual Chrome checking 827 subset outcomes, 1,301 complete DPLL node records, 20 cores, 52 repairs and 304 truth rows, plus all family, duality, truth and subset tables, every selected repair and node record, export and 320/390/1280 containment; an isolated installed wheel reproduces all 18 reports outside the checkout, verifies four module origins and compares console and module CLI output. The repair-policy extension adds 26 new exact reports (16,165 scalar leaves), 67 repairs, 78 policy records and 151 full DPLL nodes including intersection baselines, with 24 Python and eight Node/Chrome tests preserving all originals, Chrome checking 78 policy records, 67 repairs, 70 selectable per-repair search nodes and 462 literal rows, and native independent replay covering all 151 nodes. At most six Boolean variables, eight hard and eight removable clauses; established DPLL and MUS/MCS theory with attributed sources, not a novel or scalable SAT or MaxSAT algorithm — and costs are supplied removal preferences, not failure probabilities, synthetic clauses are supplied assumptions not verified facts, restored consistency is not causal or physical diagnosis and establishes no real-world action is safe, and search traces are tested computational witnesses, not DRAT/LRAT exports or machine-checked proofs. Distinct from 'A guarantee is not an optimum', SubmodLab's principle, which is about a certified bound that still is not the instance's optimum — here there is no bound at all, only a structural property of the set, and the error is reading minimality as a cost claim — and from 'The best path is not the likeliest transcript', CTCLab's principle, which is about a single argmax versus the summed mass over alignments — here the enumeration is already complete, every core and every repair listed, and the question is what the complete family means — and from 'A deletion is defined by what you hold fixed', InfluenceLab's second principle, which is about which refit the words 'delete row 5' name — here there is no refit to name; the hard background is fixed and the clauses are removed, and the question is whether the removal set is minimal or cheapest.

- [Diagnoselab](projects/diagnoselab.md)

## Removing an attack can remove an acceptance

In abstract argumentation, acceptance is not monotone in the attack relation: removing an attack can remove an acceptance, not only a rejection. An attack on an attacker is a defense, so deleting an attack can delete the defense that held an argument in — and adding an attack can defend an argument that was out. An edit that "removes a conflict" therefore cannot be judged by the size or the direction of the edit alone; the only honest record is the acceptance before and after, for every configuration. ArgumentLab's switch audit keeps exactly that record: it enumerates every configuration of up to six supplied attack switches and records the exact extension gains and losses for each, retaining nonmonotone outcomes and nullable outcomes rather than assuming an edit moves acceptance one way. The audit is verified on 21 controls, 209 configurations, 5,205 subset classifications and 423 switch transitions, with every nearest tie and every inclusion-minimal match preserved and complete selected-framework defense witnesses for every configuration, so a flip in either direction stays visible instead of being averaged away.

The same discipline runs through the base semantics. Nine extension families are compared on every framework, with every subset's attackers, defenders and unanswered attacks, all inclusion and range witnesses, complete three-valued labellings and the entire grounded fixed-point chain — and the boundary case is reported rather than smoothed over: a self-attacking argument has no stable extension, so classical skeptical acceptance is true for every argument by vacuous quantification while credulous acceptance is false, and the inspector displays exists=false with a prominent warning and a separate null nonvacuous field rather than reporting the vacuous truth as a position. A zero-argument framework instead has one empty extension. The lesson travels: whenever the answer is a set defined by a relation, report the set under every edit of the relation, not a story about which direction the edit should move it — a defense is a relation, not a property of the edited item.

The scope stays narrow — 19 native tests on Python 3.10–3.13 and five Node/actual-Chrome tests; independent Python bitsets and JavaScript sets agree on all 531 directed frameworks through three arguments, 344,023 scalar leaves, and 19 retained full reports, 152,884 leaves; separate set and ternary oracles cover 120 native and 100 JavaScript seeded larger cases; actual Chrome checks every retained UI record and graph state, export and invalid clearing and all 19 controls at 320/390/1280; an installed wheel reproduces 19 full reports outside the checkout. At most eight arguments with exhaustive subsets and all ties retained; established Dung 1995 semantics with six inspected sources and exact parser differences documented — not a novel or scalable solver, probability model, benchmark win, real-world truth or debate winner. Distinct from 'A minimal repair is not a cheapest repair', Diagnoselab's principle, which is about a removal set being minimal by inclusion or cardinality versus cheapest by cost — here the question is not which removal set is cheapest but whether removing an attack helps or hurts acceptance at all, and while the switch audit also keeps minimum-cardinality and inclusion-minimal matches distinct, the lesson is the direction of the change, not the size of the set (and the vacuous-quantification point is already covered there: an empty family is not a finding) — and from 'A label that leaves can come back', CutLab's principle, which is about an optimum family being nonmonotone in a moving parameter with the graph fixed — here the graph itself is edited, the flip is in acceptance under that edit, and the witness is the defense relation, not a parameter region — and from 'A lossy view of a number is not the number', GroundCheck's principle, which is about a lossy numeric view hiding the exact value — here nothing is lossy, every switch configuration is enumerated exactly, and the error is assuming the edit's direction before looking — and from 'A complete record is not a complete explanation', AgentTrace's principle, which is about a complete display being misread as an explanation — here the complete record is read correctly, every configuration and witness retained, and the error it guards against is a monotonicity assumption about the edit, not a misreading of the display.

- [ArgumentLab](projects/argumentlab.md)

## A circle is not a proof

A supported assignment can satisfy every rule and still have no derivation. In HornLab, a circular assignment — atoms that support each other in a loop — is a supported model: every implication holds, and nothing in the assignment contradicts a rule. But derivation is a different question: does the least model, built round by round from the initial facts, reach it? A circle is not a proof: the least model is what the rules actually derive, and a supported model the derivation never reaches is a self-consistent story with no route from the seeds. HornLab makes the gap inspectable: it compares the least model with every classical and supported model, and for each non-entailed query it shows an atomic countermodel — not entailed does not mean classically false. The check is exhaustive, not sampled: independent Python bitsets and JavaScript sets match 210 full reports, and a separate native set/truth-table checker replays the complete report. Ten original controls, exhaustive two-atom programs, seeded tests, installed-wheel reproduction and actual Chrome record checks.

The same discipline runs through the rule-deletion stage. Keep the initial facts fixed and inspect every indexed-rule subset, every minimal rule support and every minimal deletion set: one broken route need not break the goal, each support retains one-rule removal failures, each deletion retains restoration successes, and both minimal-hitting-set dualities and every support/deletion intersection are explicit, including the empty-support and already-absent boundary cases. The evidence is eighteen native tests retaining all originals, with all 1,024 two-atom programs and 150 seeded rule lattices; independent Python and JavaScript match 131 audits covering 5,304 subsets, and eleven browser controls expose 305 subsets, 35 queries, 36 supports, 27 deletion sets and 36 intersections, all record-checked at 320/390/1280. A separate native set/truth-table checker validates the complete lattice without calling the generator, and installed-wheel reproduction checks both inspectors through both CLI entry points.

The scope stays narrow — at most six atoms and eight rules, no negation or variables; synchronous closure does not chain through a new atom until the next round; facts are fixed seeds, duplicate indexed rules remain distinct achievers, empty-body rules can derive atoms with empty seed support, and minimal supports are relative only to the given initial facts with rules held fixed; established semantics, not a new algorithm or production rule engine — and this is bounded exhaustive evidence, not a formal proof or a signed certificate, JSON export unsigned, the browser generator not an independent verifier — but the lesson travels: whenever a claim is that something follows from premises, check the derivation, not just the consistency — a conclusion compatible with the rules is not a conclusion the rules produce. Distinct from 'Valid syntax is not a valid record', StructGate's first principle, which is about two conformance rates for a record — here the assignment conforms to every rule and the record is valid, and the question is whether conformance is derivation — and from 'A complete record is not a complete explanation', AgentTrace's second principle, which is about what a complete display's terms mean — here the record answers its own questions exactly, and the error is reading satisfaction as derivation, not importing a meaning the display never claimed — and from 'A sufficient certificate is not a complete detector', SparseLab's principle, which is about a certificate that stays silent outside its scope — here there is no certificate at all, only the full enumeration of models and derivations, and the error is treating a model as a proof.

- [HornLab](projects/hornlab.md)

## The same traces are not the same choices

Two systems can produce exactly the same finite traces and still differ in what they can do next. BisimLab's default original control has equal finite trace languages but loses a choice after the same action: follow one action and one system still offers a move the other has lost. Trace equality is checked separately from branching equivalence by exact paired-subset BFS, and the inspector shows every strong-bisimulation refinement, every failed left/right step match, executable Hennessy-Milner witness DAGs, truth sets and a quotient graph. The check is independently computed: a native partition-signature checker never calls the generator, and independent JavaScript matches the full reports. Nine native tests include all 512 three-state/one-action graphs checked against relation enumeration and 100 seeded graphs; three Node/actual-Chrome tests include 593 complete cross-engine reports and every control record at 320/390/1280. Installed-wheel checks cover both CLI entry points outside the checkout.

The trace-product inspector keeps the whole reachable product of two states' possible successor sets, including every action edge after a mismatch and the both-empty sink, so a difference that only shows up after the traces diverge is still visible: canonical BFS discovery words, layers, all possibility-mismatch nodes and a shortest distinguishing path. Equal finite traces still do not imply branching equivalence. Python bitmasks, independent JavaScript sets and a separate native checker based on explicit subset tables agree on 4,715 trace reports. Seventeen native tests include exhaustive unary three-state graphs across every ordered pair, direct word enumeration, seeded multi-action cases and forged closure/provenance checks; six Node/actual-Chrome tests cover every control record, export and invalid-input clearing at 320/390/1280px. Installed-wheel checks cover six original and seven trace controls, two CLI entry points and six import origins.

The scope stays narrow — one to six states, all labels visible; no silent abstraction, probabilities, policy guarantee, source extraction, new algorithm or formal-proof claim; established theory and seven inspected sources are attributed in the method — but the lesson travels: whenever two systems are compared by what they have done, check what each can still do — an identical observable past is not an identical future. Distinct from 'A complete record is not a complete explanation', AgentTrace's second principle, which is about what a complete display's terms mean — here the record answers its own questions exactly, and the error is treating agreement on traces as agreement on behaviour, not importing a meaning the display never claimed — and from 'Locally best choices need not fit together', which is about local optima failing to compose into a global optimum — here nothing is optimized, both systems are compared exactly, and the gap is between two equivalence relations, not between a local and a global answer — and from 'A stable value does not mean a stable strategy', which is about a value staying put while the strategy behind it changes — here the trace set stays identical while the available choices differ, and the point is that the trace set was never a complete description of the system in the first place.

- [BisimLab](projects/bisimlab.md)

## A safe next step can still lose

ShieldLab is an exact tiny safety-game inspector for hand-written agent protocols, and it makes one failure visible that a single trajectory never shows: a step can be safe right now and still lose the game. The fast action reaches a currently safe pending state, but the environment can force a leak on its next turn, while review stays in a closed safe region. Change only who controls a state — flip pending to controller ownership, with no other graph change — and the same fast action becomes winning. The inspector exposes both quantifiers and every round rather than presenting a single attractive trajectory: every synchronous fixed-point obligation, winning controller move, losing rank and branching invariant/counterstrategy graph is visible. One-step safety is a property of the step; winning is a property of the whole game, and the opponent moves next.

The proof graphs keep the quantifiers honest. A winning proof graph fixes a controller policy and retains every environment move; a losing proof graph fixes a rank-decreasing environment counterpolicy and retains every controller move, stopping at unsafe states. Ranks bound forced failure, and canonical first choices are not promised optimal. The boundaries are explicit: a five-step forced chain, a safe environment cycle, indefinite waiting, and an already-unsafe root — safe waiting need not mean progress, and dead ends are rejected outright. The evidence is eight native tests including all 21,952 three-state graph/ownership/safety combinations and 150 seeded larger arenas, with independent bitmask Python and explicit-set JavaScript agreeing, plus a separate dual-attractor and exhaustive positional-policy checker; three Node/actual-Chrome tests compare 643 complete reports and all six controls at 320/390/1280, and installed wheels replay both CLI entry points outside the checkout.

The scope stays narrow — a finite total perfect-information model only: no runtime shield, LLM guarantee, liveness, timing, probability, new algorithm or formal proof — but the lesson travels: whenever a step is called safe, ask safe against what, and for how long — a step that is safe now is not a step that stays safe once the other side moves. Distinct from 'Removing an attack can remove an acceptance', ArgumentLab's principle, which is about acceptance changing when the attack relation itself is edited — here nothing is edited, the graph is fixed and the step is currently safe, and the failure is that the opponent's next move does not preserve it — and from 'The same traces are not the same choices', BisimLab's principle, which is about two systems agreeing on every finite trace while differing in what they can do next — here there is one game and one step, and the gap is between a step being safe now and the game being won, not between two systems — and from 'A free restart is not optional stopping', BetLab's first principle, which is about whether a ruined test may be restarted with fresh capital — here nothing is ruined and nothing restarts; the game continues, the opponent moves, and the safe step loses anyway.

- [ShieldLab](projects/shieldlab.md)

## A winning state is not a winning policy

In a repeated-goal game, being in a winning state is not the same as having a winning policy. BuchiLab's games are tiny finite adversarial repeated-goal games — the controller must visit a goal state infinitely often, not merely reach one once — and the inspector makes the gap visible: idle can stay inside the winning region forever and still lose. A state is winning when some policy forces repeated goals from it; a policy wins only when it actually keeps returning to a goal. Rank-guided progress is what separates the two: every nested greatest/least fixed-point obligation, progress rank, complete positional controller policy and reachable cyclic non-goal SCC is visible, and per-policy audits retain every environment move, so the check is about what the policy does, not where it sits.

The failure has to be shown as it actually repeats. A reachable bad component becomes an exact action-labelled lasso — a prefix once, then a nonempty non-goal cycle forever — for every failing fixed controller policy and root, with empty prefixes, self-loops, multiedge cycles, unreachable bad components and duplicate-target action choices all explicit. Seven original controls distinguish recurrence from one-time reachability, environment starvation from controller choice, full-graph SCCs from non-goal induced cycles, and an empty controller policy from no policy. The evidence is nine native tests including 21,952 exhaustive three-state games; three Node/actual-Chrome tests comparing 331 complete Python/JavaScript reports and every control record at 320/390/1280; a separate checker that replays with sets and Floyd reachability plus exact deterministic eventual-lasso replay for every joint positional-policy pair, without calling the generator; and installed wheels replaying seven original controls through both CLIs outside the checkout. The lasso stage adds 16 native tests across four Python versions and five Node/actual-Chrome tests, including 314 complete witness-report comparisons and every record in ten controls at 320/390/1280, with BFS generation independently checked by bounded simple walks and the joint-policy lasso oracle.

The scope stays narrow — at most six states and three moves per state; no fairness assumption, learned abstraction, deployed shield, general LTL compiler, formal proof or real-agent guarantee; rank-permitted actions are sufficient, not all winning policies; the lassos are per-policy counterexamples, not one environment strategy defeating every controller policy; and testing is not proof — supplied graphs can omit real behavior or mislabel goals — but the lesson travels: whenever a position is called winning, ask what the policy does from there — a place from which you could win is not a plan that wins. Distinct from 'A safe next step can still lose', ShieldLab's principle, which is about a step that is safe now losing because the opponent moves next — here the opponent need not move at all; the controller's own policy loses by idling inside the winning region and never returning to a goal — and from 'A free restart is not optional stopping', BetLab's first principle, which is about whether a ruined test may be restarted with fresh capital — here nothing is ruined and nothing restarts; the game continues, the policy keeps choosing, and the failure is the loop it repeats, not a restart — and from 'A time limit is not a terminal state', PPOlab's first principle, which is about a boundary flag misread as a terminal state — here nothing is mislabelled; the state really is winning, the policy really does stay inside the region, and the error is treating a property of the state as a property of the policy.

- [BuchiLab](projects/buchilab.md)

## Local support is not a shared solution

Every value in a problem can have local support and still no joint assignment exist. HallLab's tiny all-different workbench makes the gap exact: on the default control two variables reserve `{v0,v1}`, so pairwise disequalities leave all seven edges while global support leaves five, forcing x2 to v2 — the pairwise view keeps edges the global view proves impossible. A second control has three variables sharing two values: every binary constraint has support, yet no full assignment exists at all. The overlap stage sharpens it across scopes: a two-color triangle keeps every local value under full local all-different propagation to a synchronous fixed point, but has no joint assignment, and a satisfiable triangle keeps local values that never occur in a common solution. A full match for one constraint does not ensure a shared solution for several constraints, and local consistency is a property of each scope, not of the problem. The remedy is not stronger local propagation but the joint question asked jointly: propagate every scope to its fixed point, then check exact common-assignment support across the overlapping scopes, with every tight and deficient Hall subset listed — tight is not impossible, and a value survives only if some complete injective assignment uses it.

The evidence is checked, not asserted: 12 native tests include 8,777 exhaustive domain graphs and 120 seeded larger inputs, with 682 full Python/JavaScript report comparisons and actual Chrome replaying every control edge, subset and round at 320/390/1280, plus an independent exhaustive native checker that never calls the matcher and a separate JavaScript assignment engine. The overlap stage adds eight new native tests and three new Node/Chrome tests preserving the originals, 621 overlap reports and nine browser controls, over at most six variables, eight values and six scopes — at most 262144 full tuples. The conflicts stage adds 28 native tests and nine Node/actual-Chrome tests, 621 cross-engine reports and 4413 active subsets, with complete single-deletion witnesses, common kept-network assignments and contained conflicts for every restoration; the default diamond has a size-one and four size-two minimal removals, so minimal is not minimum, and with domains fixed an empty-domain background has no scope-removal repair. Installed wheels reproduce all three report families outside the checkout, and CI spans Python 3.10–3.13.

The scope stays narrow — at most six variables and eight values, one all-different relation; classic matching and Hall theory, not a new AI algorithm, an optimized Régin SCC propagator, a scalability benchmark or a whole-CSP solver; bounded exhaustive evidence, not a formal proof — but the lesson travels: whenever every part of a system passes its own check, ask whether the parts were ever checked together, because a value that is supported everywhere locally can still belong to no solution at all. Distinct from 'Locally best choices need not fit together', VariLab's principle, which is about locally best values — exact marginal modes — giving a suboptimal joint decision — here nothing is best, every value merely has support, and the failure is impossibility rather than suboptimality — and from 'Two possible cuts can be jointly impossible', SegmentLab's principle, which is about the joint probability of two cuts — here there are no probabilities, only deterministic constraint satisfaction, and the question is whether any joint assignment exists — and from 'A complete record is not a complete explanation', AgentTrace's principle, which is about a complete display being misread — here the record is read correctly, every scope and subset enumerated exactly, and the error is treating per-scope consistency as joint consistency, not importing a meaning the display never claimed — and from 'A minimal repair is not a cheapest repair', Diagnoselab's principle, which is about a removal set being minimal versus cheapest — here the question is whether any shared solution exists at all, and the diamond's minimal removals are the repair-side echo of the same local/global gap, not the lesson itself.

- [HallLab](projects/halllab.md)

## Unknown is not false

A table with unknown cells is not a table with false cells, and an implication that holds in the two extreme fill-ins need not hold in any world between them. ConceptLab's incomplete-context completions enumerate every compatible binary completion of a three-valued table — all 64 worlds of six unknowns — and classify each implication as certain, contingent or impossible: certain means it holds in every completion, contingent in some, impossible in none. The controls expose the trap directly: both extreme fill-ins can pass an implication while an intermediate world refutes it, so a check that only tries all-true and all-false has checked two worlds out of sixty-four and proved nothing about the rest. The same gap appears one level up, in goals: goals that are each possible on their own can be jointly impossible, so the inspector intersects them in one shared completion and retains every inclusion-minimal impossible goal set with deletion witnesses — separately possible is not jointly possible, and the shared completion is the check that says so.

The complete-context workbench underneath is what makes the classification exact rather than sampled. Independent Python and JavaScript engines enumerate every formal concept, cover, meet/join, attribute closure and object derivation, with canonical implications, pseudo-intent decisions, NextClosure pivots, forward rule traces and rule-removal countermodels, and every implication query retains supporting and counterexample rows. An empty premise extent is reported as vacuous validity with null confidence, not as evidence — the ratio has no denominator, so there is nothing to be confident about. The retained suite covers 194 attribute subsets, 390 object subsets, 69 concepts, 30 canonical rules, 635 ordered lattice operations and 5,762 implication queries across fourteen original controls, and independent set-based checks cover all 689 contexts with zero to three objects/attributes plus 100 seeded larger contexts per engine. The completions stage adds twelve controls covering 86 completions, 438 implication queries, 4,634 query/completion witness rows and 63 goal subsets, with 17 native tests on four Python versions, six Node/Chrome tests and 26 installed-wheel reports, and every retained UI record, export and invalid-input clearing checked at 320/390/1280.

The scope stays narrow — at most six attributes and eight objects for complete contexts, and four attributes, four objects and six unknown cells for completions; completion counts are not probabilities and confidence bounds describe supplied rows, not unseen data; no imputation, causal claim, graded possibility model, incomplete-context basis or new algorithm is claimed, and established FCA theory is attributed — but the lesson travels: whenever a value can be unknown, enumerate the worlds it could be, because a check that only visits the extremes has checked the boundary and called it the space — and a possibility that holds in some world is not a possibility that holds in the world you actually need. Distinct from 'Local support is not a shared solution', HallLab's principle, which is about values that each have support in their own scope but no joint assignment — here the object is not an assignment but a world: each goal is possible in some completion, and the question is whether one shared completion satisfies them all, so the jointly-impossible goals are the same shape of failure in a different object, not the lesson itself — and from 'A tangent is not a map', DenoiseLab's principle, which is about a local linear approximation against the exact global partition — here there is no approximation at all, the two extreme fill-ins are exact complete worlds, and the error is treating two points as the whole space rather than mistaking a local object for a global one — and from 'A minimal repair is not a cheapest repair', Diagnoselab's principle, which is about a removal set being minimal versus cheapest — here the vacuous case is a confidence ratio with an empty denominator, reported as null rather than as a finding, and the lesson's center is not the empty case but the unknown cells and the worlds between the extremes.

- [ConceptLab](projects/conceptlab.md)

## Used does not mean necessary

A plan that uses an action proves the action is usable, not that it is necessary — and a single representative plan is the weakest possible evidence for necessity. STRIPSLab's availability inspector answers the necessity question by disabling every static action subset and keeping every exact counterfactual: every counterfactual distance, shortest-plan count, original action ID, representative and optimal edge. That separates an action used by one representative from one required by every optimal plan, or by every valid plan — three different claims, checked separately. It retains all inclusion-minimal sufficient sets and all solvability and optimality cuts, with independently checked minimal-hitting-set duals, so the answer is the complete family of what suffices and what breaks, not one example of each. The original duplicate-shortcut control shows why the distinction matters in practice: remove both shortcuts and a longer detour remains, so optimality fails before solvability does — the plan still exists, it just costs more, and a check that only asks whether a plan exists would have missed the failure entirely.

The base workbench underneath is what makes the counterfactuals exact rather than sampled. Classical STRIPS planning on a tiny, fully disclosed state space — zero to six Boolean facts, positive initial, goal and precondition sets, at most eight positional unit-cost actions — where the real successor deletes then adds and the relaxed successor only adds, and facts absent from a state are false, not unknown. The export retains every one of the 2^m states including unreachable ones, with every blocked and applicable action, missing precondition, actual added and removed fact, real and relaxed successor, exact remaining goal distance, all shortest suffix choices and one representative replay, and initial optimal-plan edges retain every shortest tie. The approximation failures are the reason the exactness matters: a shared effect achieves two goals in one real action while h-add counts it twice; a consumable resource permits either goal but not both, so the relaxed graph finds a plan where the real graph has none; a restoration action makes the real optimum three steps against two relaxed; and the search inspector shows a controlled task returning cost 3 with h-add against exact cost 2, while zero, h-max and exact h-plus all return 2. The evidence is 18 controls retaining 466 scenarios, 21,731 state rows and 408 optimal edges, with Python BFS and independent JavaScript distance sweeps agreeing on 118 complete reports covering 2,515 scenarios and independent native set-transition and all-proper-subset oracles covering another 80 seeded tasks; 17 native tests, nine Node/Chrome tests and 47 isolated installed reports preserve all earlier modes, and the browser checks every retained scenario at 320/390/1280 — on top of the base eight native tests across Python 3.10–3.13, three Node/Chrome tests and an installed wheel reproducing all fourteen reports outside the checkout.

The scope stays narrow — six facts and eight unit-cost grounded actions maximum, static deterministic re-planning, not failure probabilities, timed outages, a scalable landmark extractor, real-world reliability or a new algorithm; established STRIPS and heuristic-planning theory with seven inspected sources attributed, no PDDL parsing or grounding, negative preconditions, conditional effects, non-unit costs, concurrency, probabilistic outcomes, partial observability, safety guarantee, scalable-planner or benchmark-win claim — but the lesson travels: whenever a plan, runbook or configuration is called necessary because it appears in the one plan you looked at, disable it and re-plan, because necessity is a claim about every plan, not a property of the plan in front of you. Distinct from 'Local support is not a shared solution', HallLab's principle, which is about values that each have support in their own scope but no joint assignment — here the question is not whether a joint assignment exists but whether one specific action is required across all plans, and the check disables actions rather than propagating scopes, so the same local/global shape appears in a different object with a different remedy — and from 'A minimal repair is not a cheapest repair', Diagnoselab's principle, which is about a removal set being minimal versus cheapest — here nothing is costed at all; minimality is the certificate format, all inclusion-minimal sufficient sets enumerated with hitting-set duals, while the lesson is used versus necessary, and the duplicate-shortcut control fails on optimality before solvability, not on cost — and from 'Unknown is not false', ConceptLab's principle, which is about implications that hold in the extreme fill-ins but fail in a world between them — here there is no unexamined middle: every static subset is disabled and every counterfactual kept, so the error is not a missing world but reading one representative plan as a necessity claim.

- [STRIPSLab](projects/stripslab.md)

## A binding is not a solution

A binding produced while solving is an intermediate assignment, not a verified unifier — and a solver that hands one back without checking it against the original system has shown a claim, not a solution. UnifyLab keeps every equation rewrite, every composed earlier binding, every exact constructor clash and every zero-based occurs-check cycle path, and applies a normalized simultaneous substitution to every original equation, so the binding that comes out is the one the record supports. Alias reversal is not automatically a cycle, and a resource limit never means non-unifiability: the lab distinguishes a run that stopped from a system that cannot unify. The certificate is checked independently of the solver that produced it: a separate native checker reconstructs the local rules without calling the solver, and a third lazy-environment oracle tests the controls, 600 seeded systems and all 64 term-pool pairs — so the solution is the binding plus the checked certificate, not the binding alone.

The evidence is the two engines agreeing with each other and a checker agreeing with neither. Independent Python and JavaScript engines reproduce 167 complete reports and 270 rewrites, seventeen controls retain 38 rewrites including actual state and result expansion limits, and twelve native tests on Python 3.10–3.13, three Node/Chrome tests and seventeen isolated installed reports through two CLIs in solve and verify modes preserve the modes; every retained browser step, equation, binding, witness, export and invalid edit is checked at 320/390/1280. The same discipline runs through the two extensions: the subset inspector tests every indexed subset, keeps duplicate equation identities, distinguishes an inclusion-minimal conflict from a smallest conflict, and lists deletion repairs as indices to REMOVE with failing single restorations — eight synthetic controls covering 371 subsets including all 256 masks at the eight-equation bound, with the independent engines matching 108 full audits and 1,032 subset summaries, nineteen native tests and six Node/Chrome tests — and the ground-generalization inspector keeps common constructors, gives the same ordered disagreement pair the same variable, and its independent native checker rejects coherent overgeneralization even when both inputs reconstruct, with Python and JavaScript agreeing on 209 reports, nine controls exposing 43 node records, 27 native tests and nine Node/Chrome tests.

The scope stays narrow — six variables and eight equations, 96 input nodes, 4,096-node state and result budgets, 256 rewrites; no rational trees, higher-order or AC unification, resolution prover, linear-time or benchmark-win claim; most-generality follows established rewrite and solved-form theory, and bounded ground-factorization tests are not a universal proof; six inspected source groups span Martelli/Montanari, Oxford rewrite theory, Norvig's binding-list correction, SWI-Prolog finite and rational-tree semantics, Dresden substitution and complexity notes and an independent explanatory article — but the lesson travels: whenever a solver hands you an assignment, re-check it against the original system with something that did not produce it, because a binding is a candidate until the certificate says otherwise. Distinct from 'A circle is not a proof', HornLab's principle, which is about a supported model with no derivation — here the binding may satisfy every rewrite step and still not be a solution until the independent checker confirms the final state, and the check replays a certificate rather than comparing models and derivations — and from 'Local support is not a shared solution', HallLab's principle, which is about values that each have support in their own scope but no joint assignment — here there is a single candidate binding for the whole system, and the question is whether it solves every equation, not whether local supports join — and from 'Unknown is not false', ConceptLab's principle, which is about implications that hold in the extreme fill-ins but fail in a world between them — here there is no unexamined middle: every rewrite is kept and the certificate is replayed in full, so the error is not a missing world but accepting an unchecked candidate as a solution.

- [UnifyLab](projects/unifylab.md)

## A tight bound is not an attained bound

A bound computed from a path is a number; the claim that the bound is real needs a schedule that attains it, or a ray proving it cannot be attained at all. STNLab's temporal workbench makes the gap exact: an edge `[u,v,w]` means `t[v] - t[u] <= w`, and a tight path gives a bound — but the bound is only evidence once a complete schedule meets it, with every time point assigned, and an unbounded pair is only settled by an anchored ray, not by the absence of a path. A negative cycle shows exactly why no schedule exists, even away from the anchor, and finite bounds are individually attainable, not necessarily jointly selectable — attaining every bound at once is a second claim the single-bound evidence never made. The same discipline runs through the extensions: hide time points and the projection must keep every bound their paths imply, restricting the closed network to retained original IDs and lifting jointly feasible retained assignments into full original schedules — naive edge deletion wrongly permits retained assignments the full network forbids, so a projection that drops the paths drops the constraints. Insert one proposed constraint and the answer is an exact consistency threshold plus every changed implied bound, with a complete schedule at the feasibility boundary or a candidate-first negative cycle — and duplicate edges can each be redundant when removed separately without being jointly removable, so one removal proves nothing about the pair.

The evidence is checked, not asserted: native Floyd-Warshall/Bellman-Ford generation, independent permutation/edge-product verification and recursive browser search agree, with nine native tests covering exhaustive tiny graphs, seeded networks and strict CLI rejection, and real Chrome checking all proof panels at three widths, over six points and twelve constraints in real-valued time. The insertion family adds ten new synthetic controls — exact-boundary feasibility, a missing return path, a pre-inconsistent base, duplicate and self-loop cases, a six-point threshold outside the input window, a 12-edge base plus candidate — with all finite post-insertion bounds carrying attaining schedules and 41 integer weights kept as separate alternatives, not accumulated changes; seventeen Python tests, six Node/real-Chrome tests and installed-wheel checks cover both families. The projection family is audited by independent Fourier-Motzkin elimination, path enumeration and pinned-cycle checks, with native Python and separate browser recomputation agreeing across 12 projection controls, installed CLI reproduction and real Chrome proof-panel tests at 320, 390 and 1280 pixels. The conflicts family enumerates every inclusion-minimal temporal conflict and every inclusion-minimal correction set, replaying negative cycles, conflict-deletion schedules, repaired schedules and restoration contradictions, with an independent native verifier checking complete hitting-set duality; 31 native tests on Python 3.10–3.13, 12 Node/Chrome tests, 316 cross-engine reports, exhaustive tiny networks and installed-wheel reproduction cover all four families, and Chrome visits every control proof at 320/390/1280.

The scope stays narrow — six points and twelve constraints, real-valued times, no resource capacity, uncertain durations or execution guarantee; classical temporal-network theory, not a new optimization algorithm — but the lesson travels: whenever a number is presented as a bound, ask for the witness that attains it, because a bound without a schedule is a claim about a path, not a fact about the system. Distinct from 'Local support is not a shared solution', HallLab's principle, which is about values that each have support in their own scope but no joint assignment — here there is a single bound and the question is whether one schedule attains it, and the projection's lifted schedules are about keeping implied bounds when points are hidden, not about scopes joining — and from 'A complete record is not a complete explanation', AgentTrace's principle, which is about a complete display being misread — here the record is read correctly, every bound computed exactly, and the error is treating a computed number as attained without the schedule that attains it — and from 'A minimal repair is not a cheapest repair', Diagnoselab's principle, which is about a removal set being minimal versus cheapest — here the conflicts stage's minimal sets are the certificate format, and the lesson is the bound versus its witness, not the cost of the repair.

- [STNLab](projects/stnlab.md)


## Deleting is not negating

Deleting an assertion is not negating it. EUFLab's costed repair planner makes the gap visible: a deletion set only omits assertions from the input — an omitted equality can still hold in the total minimum-domain model the plan carries, and the live control shows exactly that. Deleting means "no longer required", not "required to be false"; the planner enumerates every permitted deletion set, every cost-only optimum and a separate cost/count Pareto frontier, and each plan keeps the kept, protected and omitted assertion truth rows side by side so the omitted-but-true rows are visible rather than assumed away. Costs never override protection: a protected assertion cannot be bought out at any price, and protected intrinsic or cap-only cores explain infeasibility instead of letting a price silently decide it. The same discipline runs underneath: the base inspector gives every ordered equal pair a proof DAG and every non-entailed equality in a consistent input a separating finite interpretation — f(a)=f(b) does not imply a=b — and the domain-cap debugger separates intrinsic inconsistency from cap-only conflicts, enumerating every inclusion-minimal assertion conflict and deletion repair at a fixed cap, where minimal repairs need not have minimum size.

The evidence is checked, not asserted: native and browser engines agree on 358 complete planner reports; an independent certificate verifier rebuilds models and checks all masks and objectives without calling the generator; and fourteen synthetic controls cover different-size/same-cost optima, two-coordinate tradeoffs, duplicate occurrences, hard obstructions and function-driven cardinality. The base suite is nine native tests on Python 3.10–3.13 with 156 cross-engine reports and 251 query selections checked at 320/390/1280; the finite-model atlas adds 16 native tests, 76 complete cross-engine atlas reports and all 4,140 eight-name patterns with 4,317 admitted control patterns; the domain-cap debugger adds 23 native tests, 269 complete cross-engine reports and Chrome audits of 379 subset selections, 36 core-relaxation actions, 29 repair actions and 104 cap changes; and the sensitivity inspector varies one deletion cost over every integer from 0 to 1,000,000 with exact keep/delete intervals, breakpoint ties and every optimum mask, its affine plan-cost lines rebuilt by an independent native verifier. Installed-wheel reproduction runs the controls through both entry points outside the checkout.

The scope stays narrow — at most eight terms, arity at most two, eight equalities and eight disequalities, one uninterpreted sort, ground conjunctions only; proofs are valid explanations, not shortest proofs or minimal cores; a separating model does not prove a universal inequality; inconsistent inputs have no countermodel and entail everything classically; classical congruence closure, not new theory, a scalable solver or a real-code verifier — but the lesson travels: whenever a repair, redaction or cleanup is described as removing something, ask whether the removal changes what is true or only what is required, because an omitted requirement can still hold, and a plan that deletes cheaply without saying what stays true has not finished the job. Distinct from 'A minimal repair is not a cheapest repair', Diagnoselab's principle, which is about a removal set being minimal versus cheapest — here the planner keeps zero-cost nonminimal ties precisely because cost and minimality are separate questions from truth, and the failure is reading omission as negation, not picking the wrong optimum — and from 'A tight bound is not an attained bound', STNLab's principle, which is about a computed number needing a schedule that attains it — here the model is the witness and it is present in every plan, and the gap is semantic, between omitting an assertion and asserting its negation, not evidential — and from 'A deletion is defined by what you hold fixed', InfluenceLab's principle, which is about one deletion naming three different computations depending on the frame — here the frame is fixed and the deletion is one operation, and the error is treating that operation as a negation rather than as a release.

- [EUFLab](projects/euflab.md)

## A closed table is not a correct language

A finite sample can make two protocol states look identical, and a closed and consistent observation table can still propose the wrong language. What settles the question is the distinguishing experiment. DFALab's original implementation of Dana Angluin's classic L* learner asks globally cached membership queries, repairs observation-table closure and consistency, and processes all prefixes of each exact counterexample, and every cell, teacher-side query path, repair witness and conjecture is replayable. Each equivalence query includes the complete reachable target/hypothesis product, all outputs and all edges, and its first mismatch is a shortest shortlex counterexample — no mismatch proves all-word language equivalence for the supplied finite teacher. The working inspector lets you choose a synthetic teacher or edit up to six states and three letters, replaying every table, query, repair, hypothesis, product graph and final pair distinction, and the standard even/even parity language is attributed to Angluin. The final DFA carries a shortest access word and a shortest distinguishing suffix for every state pair, proving reachable-state minimality, which does not prove minimum query count: agreement on every experiment run so far is not agreement on the language, and only the experiment that separates the states can say which it is.

The evidence is checked, not asserted: eight native tests run on Python 3.10–3.13, including all 17,496 three-state binary teachers, all 648 three-state unary teachers and all 128 two-state binary teachers, with every start and accepting set, plus seeded larger teachers, disabled-generator verification, forged reports and strict atomic CLI caps. Four Node/Chrome tests compare 189 complete reports and replay 93 table selections, 45 conjectures and 411 new-query rows over 320/390/1280 pixels, and installed module/console generation and verification reproduce all nine controls outside the checkout. An independent native verifier replays the whole certificate without calling the generators, using separate shortest-access fixed points, and a separate pair-marking oracle checks language equivalence and minimal state counts. The same discipline runs through the two extensions: the bounded-conformance inspector separates finite suite agreement, the supplied candidate's reachable-state bound, a bounded equivalence certificate and a separate exact graph audit — a faulty extra-state candidate passes when its bound is understated, and increasing the bound exposes the fault — with six added native tests including 52,488 exhaustive reference/candidate cases, 131 full native/browser-engine reports cross-checked, and actual Chrome auditing 3,444 test selections and 141 probes across eleven controls and three widths, with four Python versions, seven Node/Chrome checks and installed two-family reproduction preserving the original L* learning page and schema; and the fault atlas enumerates every complete labeled implementation in a tiny unary/binary state domain, checks every subset of the constructed W-suite under test-count then letter-count cost, and retains all minima, escaping faults and chosen-test deletion witnesses — irredundancy is not minimum cardinality — with tests covering all 60 tiny minimal references, eleven complete cross-engine atlas reports matching, and actual Chrome auditing 6,996 candidate selections and 804 subset selections across eight controls and three widths, on eighteen native checks across four Python versions, ten Node/Chrome checks and installed three-family reproduction.

The scope stays narrow — complete deterministic finite synthetic teachers only, not real-world protocol benchmarks, noisy observations, timed automata or unknown services; exact equivalence is available because the target DFA is supplied, and random testing cannot inherit that guarantee; acceptance concerns the whole word, not a safety promise for every prefix; L* and its theoretical guarantees belong to Angluin (1987), with no algorithmic novelty, query-efficiency win or industrial scalability claimed, and no model, paid API or private data is needed — but the lesson travels: whenever two states agree on every test run so far, ask for the experiment that would separate them, because a sample that never distinguishes them has proved nothing about whether they differ. Distinct from 'A green suite is a regression gate, not a certificate', EvalForge's principle, which is about what a passing suite can and cannot certify — here the no-mismatch result is a proof, but only because the equivalence query carries the complete product, so the certificate is the product itself, not the pass count — and from 'A tight bound is not an attained bound', STNLab's principle, which is about a computed number needing a schedule that attains it — here the bound is the W-method state bound the check assumes, and the failure is stating it too low, not failing to attain it — and from 'Unknown is not false', ConceptLab's principle, which is about implications that hold in the extreme fill-ins but fail in a world between them — here every cell is known and the table is complete, and the gap is that no recorded cell distinguishes the states, so only a new distinguishing suffix can.

- [DFALab](projects/dfalab.md)

## A resolved citation is not a correct citation

A citation marker that resolves to a provided source proves the marker points somewhere — not that the passage it points to says what the sentence claims. GroundCheck's citation validation is exactly that narrow: every `[n]` marker must resolve to a provided source, with an unresolvable citation flagged as a high-severity finding. But a resolved citation can point to the wrong passage, and negation and wrong attribution can pass both of the inspector's policies — all provided sources, or only citations in the same raw unit — because neither policy unions documents and neither reads meaning: the sentence is scored by content-token containment against every source document, stopwords removed, at document granularity, so a sentence that negates its source keeps every content token and still scores as supported, and a claim attributed to the wrong source keeps its tokens too. Resolution is a property of the pointer; the claim's correctness is a property of the passage, and a check that confuses the two has verified the address while skipping the content.

The check is verified against the pointer, not the meaning: 66 Python tests retain all 43 originals unchanged, with the 50 retained reports covering 25 controls in both scopes — wrong, missing and post-period citations, semantic false positives, split-document claims, exact decimal collisions, zero-content inputs and tie rules — and exact Fraction comparisons plus exhaustive small token subsets check the arithmetic. Four Node/actual-Chrome tests check full-report parity, every displayed source score, edits and export, and 320/390/1280 containment, and an isolated installed wheel verifies eight module origins and both the audit and original CLI paths outside the checkout, with Python 3.10–13 regenerating the same artifacts. The bound is stated with the check: citation attachment is an explicit same-raw-unit convention, not a general citation parser; lexical support is not semantic entailment, factuality or source authentication; and these are synthetic controls, not a RAG-quality benchmark — but the lesson travels: whenever a reference resolves — a link that loads, a citation that matches, an id that exists — ask what it resolves to, because a pointer that lands is no evidence about the thing it lands on. Distinct from 'A lexical check can catch a fabrication, not certify a truth', GroundCheck's first principle, which is about what a lexical check can certify about a claim — here the citation resolves and the tokens match, so the check passes, and the failure is inside the passing case, not at the edge of what the check certifies — and from 'A lossy view of a number is not the number', GroundCheck's second, which is about a lossy representation hiding the exact value — here nothing is lossy, every token is present exactly, and the error is semantic, not representational — and from 'A complete record is not a complete explanation', AgentTrace's, which is about a complete display being misread as an explanation — here the record is complete and read correctly, and the gap is in what resolution itself establishes, not in how the display is read.

- [GroundCheck](projects/groundcheck.md)

## Fitting the examples is not identifying the function

A learner that fits every known example has not necessarily found the target function. SynthLab's counterexample-guided loop is exact inside its finite grammar: the learner chooses the cheapest grammar expression fitting the known examples, an exact finite verifier returns the first wrong input, and the loop repeats until the candidate passes every input. Passing every known example is correctness on those examples, not identification of the target -- the two-bit XOR control has 132 distinct rival functions over 65,536 input subsets, and CEGIS stops correctly with four examples while three rivals still fit them. The teaching atlas finds 182 four-row teaching sets that do identify the target: the same number of examples, different identifying power, because a teaching set is chosen to eliminate every rival, not merely to be satisfied by the target. Full-domain semantic signatures deduplicate programs without using the target, and a separate verifier enumerates every raw ordered grammar tree to check bounded completeness and canonical minimum cost -- so the claim stays inside the finite grammar, where examples are checked, not generalized from.

The check is verified against the finite domain, not the examples: 10 synthetic controls separate example agreement, exact finite correctness and minimum AST-node cost inside the explicit grammar, with 22 native tests on Python 3.10\u201313 -- 8 original, including 512 Boolean target/grammar pairs and 2,764 raw trees at each of three widths, plus 7 teaching and 7 adaptive -- and 12 Node/actual-Chrome checks: 4 original auditing 30 reports, 90 iterations, 903 candidate signatures and 3,420 expression probes; 3 teaching auditing 15 teaching reports, 1,203 subset selections and 597 rival truth selections; and 5 adaptive comparing 541 complete native/JavaScript reports with independent verification, with actual Chrome auditing 15 adaptive reports, 1,583 version-space selections, 111 query partitions, 306 answer branches, 84 target traces and 105 passive mask selections. The frontier is pure unsigned 1..3-bit expressions built from 0/1/x/y and selected add/and/neg/not/xor operators through AST node cost 5, with canonical representatives by minimum node cost then ASCII prefix-expression order. The adaptive coda sharpens the lesson: a full seeded two-bit grammar leaves ten functions after two known observations, two further adaptive queries suffice while every fixed passive separating set needs three rows, and immediate split balance is not the objective -- across all balanced tie resolutions, policies need two or three further queries, so let the answer choose the next question. The bound is stated with the check: finite target-specific identification, not class-wide teaching dimension or PAC learning; at most ten functions after separately counted initial observations, exact noiseless labels and unit query cost, with future answers simulated from supplied tables rather than a live oracle; classical CEGIS/enumeration, Goldman and Kearns teaching-set ideas, and decision-tree dynamic programming credited, with no novel algorithm, unbounded synthesis, cvc5 integration, production-code benchmark, expected-cost or PAC claim. Distinct from 'A closed table is not a correct language', DFALab's principle, which is about a closed observation table proposing the wrong language -- here the examples are satisfied exactly and the candidate is correct on them, and the gap is that correctness on the examples does not identify which rival function is the target -- and from 'A local minimum is not a global optimum', CutLab's first principle, which is about a search stopping early on one fixed landscape -- here the search is exhaustive inside the finite grammar and the candidate is verified on every input, and the gap is identification, not optimization -- and from 'A complete record is not a complete explanation', AgentTrace's principle, which is about a complete display being misread as an explanation -- here the record is complete and read correctly, and the gap is in what fitting the known examples establishes about the unknown function.

- [SynthLab](projects/synthlab.md)

## Zero length is not absence

A set can have zero length and still exist. HingeLab asks whether a closed perturbation ball is robust when the nearest decision boundary is distance one away, and the answer depends on which class owns the boundary: for margin(x) = x with class 1 at margin >= 0, from x = 1 the opposite-class set [-2, 0) is open at zero, so distance one is only an infimum and the closed ball is robust, while from x = -1 the opposite-class set [0, 2] contains an actual adversary at the same radius. An isolated tie sharpens the point: margin(x) = -|x| has class 1 only at x = 0, an entire opposite class that a continuous curve and two sampled points can miss. The all-reference atlas erodes exact class components while retaining endpoint ownership: for margin x on [-2,2] at radius 1 the robust class-0 references are [-2,-1) while class-1 references are [1,2], and the nested-tent class [-1/2,1/2] at radius 1/2 leaves exactly the singleton {0}, which disappears at 513/1024. The radius profile states it directly: for margin x on [-2,2] the robust length is max(4-2r,0), so at radius 2 the length is zero but the class-1 singleton {2} still exists -- class 0's existence radii are [0,2), class 1's are [0,2]. A robust fraction is interval length divided by domain length, not accuracy or probability under a data distribution; a singleton has zero length and still exists.

The check is verified by independent finite exhaustion, not by sampling: the base release is exact across all 24 source files on main 52871cd2298909dec76496dabbdf34c4408606c7, with 12 Python tests on each of 3.10-3.13 including 200 seeded two-layer networks, 144 complete Python/BigInt reports, four Node/Chrome tests, eight controls reproduced from a fresh installed wheel and live Chrome checking 54 region selections over 24 full reports, five deployed assets matching main and all 24 screenshots matching pixel for pixel. The all-reference atlas, merged main a26692d37e0faf7c0ad9af3a845c56f58618f702, is source-exact across 34 files, with 20 Python tests on each version, seven Node/Chrome tests, 160 new seeded networks, 200 new reference reports plus the preserved 144 base reports, a 972-case tiny-network sweep, eight base and eight reference controls, Chrome checking 47 robust-component selections over 28 reference reports, nine deployed assets and 52 screenshots matching. The radius-profile extension, merged main 4b1ceacf5ffeeb25ed8052c48053a926e91dd047, is source-exact across 44 files, with 26 Python tests on each version, ten Node/Chrome tests, 104 new complete cross-language profile reports plus 200 reference and 144 base reports, eight controls in each report family, Chrome checking 28 radius reports, 13 deployed assets and all 80 screenshots matching. The bound is stated with the check: one scalar input, one scalar margin, one or two hidden layers of width 1..3, at most six hidden neurons and 64 oracle masks, every parameter, endpoint, reference and radius an integer-valued number or rational string with absolute reduced value at most 32 and reduced denominator at most 1,024, radius horizon [0,32], and the domain part of the claim -- robustness outside it is not checked. Established piecewise-affine analysis and morphological erosion are credited -- Sotoudeh and Thakur, Bunel et al., Heijmans' Mathematical Morphology section 1.2 for the structuring-element containment definition, with Pegden's open-ball convention explicitly distinguished rather than silently substituted -- with no new algorithm, training or model import, high-dimensional certificate or benchmark. Distinct from 'A tight bound is not an attained bound', STNLab's principle, which is about a computed bound needing a schedule that attains it -- here the singleton is attained, the point exists and is robust at radius 2, and the error is reading its zero length as absence, not a missing witness -- and from 'A lossy view of a number is not the number', GroundCheck's principle, which is about a lossy numeric view hiding the exact value -- here every length, endpoint and radius is exact rational arithmetic, and the error is treating a zero measure as an empty set, not a rounding error -- and from 'A complete record is not a complete explanation', AgentTrace's principle, which is about a complete display being misread as an explanation -- here the record is complete and read correctly, and the gap is between a set's measure and its existence, not between a display and its meaning -- and from 'Zero visits is not zero mass', SegmentLab's principle, which is about a sample that never visits an outcome whose exact posterior mass is positive -- here nothing is sampled, the length is exactly zero and the set is exactly nonempty, so the gap is geometric, not statistical.

- [HingeLab](projects/hingelab.md)
## Occupancy is not a coupling

Numbers that look like probabilities are not a distribution until you check what they sum to. WarpLab's soft-DTW alignment exposes every cell occupancy and joint edge flow exactly, and the occupancies sum to expected path length, not one: they are not a normalized transport coupling, and the edge values are joint traversal probabilities, not conditional transitions. A signed cost perturbation moves occupancy according to negative path-incidence covariance, and the Hessian products that measure that movement are taken in independent cost coordinates, not sequence coordinates -- the same number can be exact and still answer a different question than the one asked. The controls make the misreading concrete: three zeros against themselves at temperature one have 13 equal-cost paths and a raw score of -log(13), not zero, and seven zeros against seven zeros have all 8,989 legal paths tied with a score of -log(8989) -- raw soft-DTW can be negative and is not a metric, so a zero self-score is a property a metric has, not one an alignment score owes you. The length atlas sharpens the same point: a per-visited-cell penalty changes the mixture, not the conditional laws, so a shorter alignment under a positive penalty is a changed objective, not an accuracy improvement, and the inverse inspector's penalty range of -4..4 may not reach a requested expected length at all -- an unreachable target returns a diagnostic response, not a solution.

The check is verified by independent exhaustive enumeration, not by trusting the dynamic program: the base release passes 15 Python tests on each of Python 3.10-3.13 and five Node/Chrome tests, comparing 168 complete Python/JavaScript reports, with a fresh installed wheel reproducing all eight controls and live Chrome checking 24 complete reports, 396 cell selections, 576 complete-path selections and 72 layer changes at 320/390/1280 pixels, all five deployed assets byte-identical to verified main and all 24 screenshots matching pixel for pixel. The path-length atlas adds 98 independently verified complete cross-language atlases, with 27 Python tests on each version and nine Node/Chrome tests, and live Chrome checking 81 length selections, 1,740 row/column cell inspections, 72 penalty changes and 96 complete reports, all ten deployed assets source-exact and all 48 screenshots matching. The inverse expected-length response adds 37 Python tests on each version and 12 Node/Chrome tests covering 36 complete cross-language inverse reports, with a separate complete-path oracle evaluating every witness penalty without calling the solver, and live Chrome checking 438 witness selections over 27 complete reports, all 15 deployed assets source-exact and all 75 screenshots across the three inspectors matching. The bound is stated with the check: scalar synthetic sequences of length 1..7 with values -8..8, temperature 0.05..8 and signed cost directions -4..4, at most 8,989 paths, with no learned model, benchmark, speed or novel-algorithm claim; the underlying soft-DTW mathematics is credited to Cuturi/Blondel and Blondel/Mensch/Vert, and the self-corrected divergence is absent because the 2021 nonnegativity theorem is ground-cost-specific. Distinct from 'Zero length is not absence', HingeLab's principle, which is about a set with zero length that still exists -- here the occupancies are positive and the path set is nonempty, and the error is reading an exact joint quantity as a normalized distribution, not reading zero measure as absence -- and from 'A lossy view of a number is not the number', GroundCheck's principle, which is about a lossy numeric view hiding the exact value -- here every occupancy and edge flow is exact rational arithmetic, and the error is mistaking what the number is conditioned on, not a rounding error -- and from 'A mean is not the distribution', TransportLab's principle, which is about a summary preserving the mean while collapsing the variance -- here nothing is collapsed, the occupancies are exact, and the gap is that an exact joint quantity is not a coupling -- and from 'A complete record is not a complete explanation', AgentTrace's principle, which is about a complete display being misread as an explanation -- here the record is complete and read correctly, and the gap is in what the quantity sums to, not between a display and its meaning.

- [WarpLab](projects/warplab.md)

## Fitting is not reaching

A budget can fit both ends of a rewrite and still admit no proof between them. RewriteLab's bounded graph over `0,1,x,y,+,*` at 3, 5 or 7 nodes (36, 548 or 10,788 terms) makes the gap concrete: `x*(1+1) -> x+x` first fits at budget 5 but is first reachable at 7, an extra budget of 2 for a shortest proof of distance 3, and 13 of its 213 cap-7 semantic candidates need a larger bridge still — while five of six weighted constant-product candidates remain unreached through seven nodes, and a null means not reached through the cap, not impossible at larger budgets. The same confusion runs through costs: one fixed graph has different cheapest answers under different operator costs, the constant-four product and addition-only vectors tying exactly when addition and multiplication costs agree (224 positive-gap, 288 zero-gap and 64 tied triples out of 512, each group winning at 288 because ties credit both), while the five-node bridge is strictly dominated with a gap at all 512 triples and no crossover is invented for it. A finite grid cannot settle the question either: the continuous-region extension computes complete optimum regions over every strictly positive cost ratio, and a boundary-only winner is not obtainable at strictly positive costs even though its region is closed geometry, while an interior tie point or segment can be a real winner despite zero area — area is not a probability and the zero-cost boundary closes the diagram, not the optimizer's request domain.

The check is verified by independent enumeration, not by trusting the generator: the base release is 25 exact source files with 11 Python tests on 3.10-3.13 and three Node/actual-Chrome tests, 72 complete cross-language reports with 111,316 proof rows and 111,342 semantic rows, live Chrome checking 26 reports, all 3,612 proof and 3,630 semantic selections at 320/390/1280, all five deployed assets matching main, with exact evaluation on a 5-by-5 grid proving polynomial identity for the degree-bounded grammar. The budget-barrier stage adds 35 source-exact files, 20 Python tests and six Node/actual-Chrome tests, 36 complete atlases comparing 13,016 candidate rows and 13,745 nested proof rows, Chrome checking 25 atlases and every 3,844 candidate selection, nine deployed assets and 57 screenshots matching without masks. The cost atlas adds 27 Python tests and nine Node/actual-Chrome tests, 17 complete weight reports comparing 8,704 outcomes and 93 groups, Chrome checking 25 weight reports, all 4,096 outcome selections and 34,570 expression selections, 13 live assets and 83 screenshots matching. The continuous-region stage adds 35 Python tests on each of 3.10-3.13 with eight Node engine and four actual-Chrome tests, 17 region reports agreeing on 93 groups and 215 vertices, independent tests over all 36 three-node sources, 500 random vector sets and 64 outside-grid positive points, Chrome checking 25 region reports, all 4,096 point selections and 34,570 expression selections, 16 deployed assets and 111 screenshots matching exactly. The bound is stated with the check: a fixed 3/5/7-node grammar with exact rational algebra that need not preserve IEEE floating-point behavior, no claim beyond the stated grammar, rules and budget, and no new algorithm, e-graph, learned policy, tensor engine or compiler-speed benchmark. Distinct from 'A tight bound is not an attained bound', STNLab's principle, which is about a computed bound needing a schedule that attains it — here the budget fits both terms and the bound is exact, and the gap is that no proof exists within it, not that no witness attains it — and from 'A lossy view of a number is not the number', GroundCheck's principle, which is about a lossy numeric view hiding the exact value — here every count, cost and region is exact rational arithmetic, and the error is reading fit as reachability, not a rounding error — and from 'A complete record is not a complete explanation', AgentTrace's principle, which is about a complete display being misread as an explanation — here the record is complete and read correctly, and the gap is between two different properties of the same graph, not between a display and its meaning — and from 'A minimal repair is not a cheapest repair', Diagnoselab's principle, which is about minimal and minimum repairs differing — here nothing is repaired, and the confusion is reachability versus equivalence, not minimal versus minimum — and from 'Fitting the examples is not identifying the function', SynthLab's principle, which is about examples underdetermining a function — here the terms are fully specified, and the gap is that a fitting budget does not supply a proof.

- [RewriteLab](projects/rewritelab.md)

## A ranking is not an entailed preference

A complete ranking can exist for each direction while the pair itself stays undecided. CPNetLab makes the gap concrete with supplied binary CP-nets, where a ranking is compatible with the tables and a pair is entailed only when every compatible ranking agrees on it: in a four-variable fanout, `0000 → 1000` is a legal improving flip even though violated rows rise from 1 to 3, and all 2,304 compatible strict rankings still put the target above the start — counting violated rows is not the preference semantics. A matching two-variable dependency cycle permits four strict rankings, while reversing one table produces the actual improving cycle `00 → 01 → 11 → 10 → 00`, zero strict rankings, and no vacuous dominance verdict — a cycle and an inconsistency are different, and neither is settled by asserting a ranking. Two independent consistent cycles admit exactly 101,977,088 rankings while leaving `0000` and `1111` incomparable, and the workbench displays a complete ranking for each direction, so the existence of a ranking for either direction does not entail the pair. The row-subsets extension sharpens the same confusion at the level of explanations: enumerating every whole conditional-row subset, the default 256-subset control has two minimal conflicts and six irreducible withdrawals — three removing one row, three removing two — and a separate control has two-row and four-row minimal path supports, so a minimal withdrawal is not a minimum one, and neither is the right human preference to abandon.

The check is verified by independent reconstruction, not by trusting the generator: a separate Python checker rebuilds the entire evidence report using Hamming-one pairs, Floyd-Warshall and suffix-removal counting, rather than the generator's conditional-row flips, breadth-first paths and prefix-ideal counting, and Python and JavaScript agree on all eight controls, 61 outcomes and 100 edges, with browser JSON independently checked only after the Python verifier accepts it. Reproduction covers all 36 two-variable networks and 576 ordered queries against all permutations, five three-variable fixtures against all 40,320 permutations each, 160 seeded additional networks and strict evidence forgeries on Python 3.10-3.13, with an installed wheel outside the checkout; actual Chrome checks 24 reports at three widths, all 689 ordered control comparisons, every rendered conditional row, path, ranking witness and no-path cut, all eight evidence exports, and stale/invalid/cycle recovery. The row-subsets stage adds 14 Python tests on 3.10-3.13 and six combined Node/actual-Chrome tests, all 576 ordered two-variable query atlases (6,400 subset records), all 400 two-variable masks against every possible total order, and 91 accepted seeded row atlases, with deployed Chrome selecting all 865 masks, all 46 antichain buttons, every row toggle and all eight exports. The bound is stated with the check: zero to four variables and at most 16 outcomes with complete strict binary local tables, and no learned human preferences, local ties, missing rows, constraints, cardinal utility, partial-model semantics or scalable-solver claim; CP-net theory and graph/counting methods are established prior work, and these are developed synthetic controls, not human-choice measurements or a new algorithm. Distinct from 'A lossy view of a number is not the number', GroundCheck's principle, which is about a lossy numeric view hiding the exact value — here every count is an exact enumeration, and the error is reading a ranking that exists as a preference that is entailed, not a rounding error — and from 'A complete record is not a complete explanation', AgentTrace's principle, which is about a complete display being misread as an explanation — here the record is complete and read correctly, and the gap is between a ranking existing and a pair being entailed, not between a display and its meaning — and from 'A tight bound is not an attained bound', STNLab's principle, which is about a computed bound needing a schedule that attains it — here the rankings are attained and displayed for both directions, and the pair is still not entailed, so the gap is entailment, not attainment — and from 'A minimal repair is not a cheapest repair', Diagnoselab's principle, which is about minimal and minimum repairs differing — here nothing is repaired, and the minimal-versus-minimum confusion is about which whole rows to withdraw, not about repair cost.

- [CPNetLab](projects/cpnetlab.md)

## A restriction is not an announcement

An arbitrary subset of worlds can be retained by a what-if restriction without any Boolean formula over the supplied atoms expressing it. EpistemLab's disclosure atlas makes the gap concrete: enumerate every retained-world subset, but count only actual Boolean-definable announcements as solutions — a restriction can split worlds with identical atomic facts, and no Boolean formula over those atoms can do that, so the atlas supplies a retained/removed pair with the same valuation as an explicit obstruction, or complete defining DNF cubes when the restriction is expressible. Eight developed controls cover 324 restrictions and 25 separate knowledge goals; the default goal has two inclusion-maximal successful disclosures retaining two and three worlds, and only the latter is maximum-retained, so inclusion-maximal is not maximum. Another control has two successful diagnostic restrictions and no Boolean solution at all, and a stronger truthful Boolean disclosure can also destroy an ignorance goal — a better announcement in one sense can be a worse one in another. The search checks all proper supersets, not just one-bit neighbours: a direct regression has successful masks 1 and 7 with failing intermediate masks 3 and 5, so a path through the subset lattice is not monotone in the mask. The same confusion runs through the base workbench: a public announcement can be truthful and make its own content false — in the default two-world experiment, "p, but agent a does not know p" retains one world and becomes false there, the fact remaining true while the ignorance does not — and eight developed controls separate everybody's knowledge from common knowledge with an actual two-agent failure chain, show distributed knowledge that neither agent has alone, inspect disconnected common-knowledge components, and follow three observers through an 8 → 7 → 4 → 1 world sequence, with a removed focus giving null pointed answers rather than false ones.

The check is verified by independent reconstruction, not by trusting the generator: a separate Python checker enumerates world combinations and unions of valuation classes with independent truth-set/fixed-point/Floyd semantics, rebuilding every defining cube, obstruction, post-update query truth set, frontier and stronger-disclosure loss witness without importing the atlas generator, while the base verifier rebuilds the complete report with truth-set algebra, descending fixed points, block intersections and Floyd-Warshall distances, and browser exports count as independently checked only after the Python verifier accepts them. Release checks are 14 Python tests on 3.10-3.13 and nine Node/actual-Chrome tests, all 200 small-model atlases (1,600 restriction records) against every one-atom Boolean truth function, 45 nested-goal atlases, malformed and forged-evidence rejection, and an installed 0.2.0 wheel reproduced outside the checkout through both CLI entry points for both eight-control families; deployed Chrome checks 24 responsive reports, 972 mask selections, 75 goal selections, 204 frontier/witness buttons, 2,596 subformula selections including 1,170 modal obligations, 87 world toggles, eight exports and stale/invalid/prior-anchor/empty recovery. The base release adds seven Python tests on 3.10-3.13 and four Node/actual-Chrome tests, all 200 three-world/two-agent partition-and-valuation models, 120 seeded nested requests and an installed 0.1.0 wheel through both module and console entry points, with Chrome checking 24 responsive reports, 51 round snapshots, 383 formula/world selections, 142 modal obligations and eight exports. The bound is stated with the check: finite supplied S5 models of at most 16 worlds, five atoms, three agents, six queries and four sequential global truthful restrictions, and disclosures of at most eight supplied worlds, five fixed atoms, three S5 agents, six separately evaluated goals, no prior announcements and one Boolean restriction — no beliefs, probabilities, fresh atoms, epistemic-announcement search, speaker-knowledge requirement, arbitrary-announcement logic, general planning, shortest-formula claim, privacy guarantee or new-algorithm claim; truth loss is evidence for the supplied model and update, and counting retained worlds is a finite combinatorial objective, not probability or real information leakage. Distinct from 'A ranking is not an entailed preference', CPNetLab's principle, which is about a ranking existing for each direction while the pair stays undecided — here the subset exists and is displayed, and the gap is whether any Boolean formula defines it, not whether every ranking agrees on a pair — and from 'A lossy view of a number is not the number', GroundCheck's principle, which is about a lossy numeric view hiding the exact value — here every subset is enumerated exactly, and the error is reading a retained subset as an announcement, not a rounding error — and from 'A complete record is not a complete explanation', AgentTrace's principle, which is about a complete display being misread as an explanation — here the atlas is complete and read correctly, and the gap is definability, not meaning — and from 'A tight bound is not an attained bound', STNLab's principle, which is about a computed bound needing a schedule that attains it — here the successful disclosures are attained and displayed, and the gap is whether a restriction is expressible at all, not whether a bound is reached — and from 'A minimal repair is not a cheapest repair', Diagnoselab's principle, which is about minimal and minimum repairs differing — here nothing is repaired, and the inclusion-maximal-versus-maximum gap is about which disclosures retain the most worlds, not about repair cost.

- [EpistemLab](projects/epistemlab.md)

## What this adds up to

Practical systems over demonstrations: tools that are available the
moment they are needed, that fail loudly, that fit into automation
unchanged, and that leave a readable record behind them. The repositories
linked above are the evidence — the code, not the claims, is the point.
