# Midya Rahmani

Toronto-based technologist with 12+ years across technology, financial services, and telecommunications. Lately building with large language models, agentic systems, and workflow automation.

## What I build

- **LLM and agentic systems** — practical AI workflows, not demos: systems that do real work end to end.
- **Workflow automation** — taking manual, multi-step processes and making them reliable and repeatable.
- **Web platforms** — TypeScript, React, Next.js, and static-first architectures that stay fast and maintainable.

## How I build

The projects below share an approach, written up in [approach.md](approach.md): choose the simplest architecture that meets the requirement, make tools that fit into scripts as well as terminals, validate before executing, and let reports and documents be outputs of the work rather than afterthoughts — all designed around real constraints, from right-to-left layouts to reduced-motion preferences.

## Selected projects

### SegmentLab

Exact offline Gaussian changepoint inference with explicitly normalized constrained partition priors, forward/backward evidence, count/boundary/interval posteriors and complete MAP segmentation. A36-point synthetic fixture recovers cuts12/24; the same outlier sequence is confidently oversegmented under low assumed noise. Rolling interval statistics avoid rescans with exact work-count audits. Seeded direct backward draws preserve joint partition constraints and draw conditional Gaussian means; an exact-vs-sample audit retains positive rare mass even when no draw visits it. 42 tests, exhaustive tiny references, dependency-free Python, JSON CLI and two reproducible SVGs separating joint paths from marginal means. Model-conditional latent-mean variance, not online detection, event attribution or real-data calibration.

- Repo: [midya8/segmentlab](https://github.com/midya8/segmentlab) · Case study: [projects/segmentlab.md](projects/segmentlab.md)

### HamiltonLab

Hamiltonian Monte Carlo from scratch with full rejection histories, leapfrog energy/reversibility and quadratic resonance audits. High acceptance can hide zero mode switches or almost-identity trajectories; optional state-independent random lengths retain every choice and work count. Rank-normalized split/folded R-hat exposes deterministic scale and half-chain failures missed by classical ratios; undefined components remain null. Analytic harmonic-flow references separate leapfrog error, mass convention and exact-duration resonance, including large jumps that only flip sign. Fixed and IID random-duration q/q² covariance audits and a reproducible shared-axis SVG expose frozen magnitude even with zero position correlation; no sampled-chain ESS/MCSE claim. 82 tests, dependency-free Python, offline sample/demo/quadratic/diagnose/harmonic/window/window-mixture CLI and SVG. No speed ranking, adaptive NUTS, ESS/MCSE or convergence certificate. Synthetic chains and analytic truths, not fitted posterior results.

- Repo: [midya8/hamiltonlab](https://github.com/midya8/hamiltonlab) · Case study: [projects/hamiltonlab.md](projects/hamiltonlab.md)

### TransportLab

Log-domain entropic optimal transport with full mass plans, explicit nonconvergence and weighted interpolation atoms. Full pushforward preserves actual endpoint marginals; barycentric means do not. Separate rounded primal/dual audits retain raw failed solves and report signed numerical gaps, marginal residuals and L1 changes. Analytic fixed-iteration plan tangents expose a nonconverged envelope-shortcut error0.007670872, checked against central differences. Zero support, covariance decomposition and exact tiny assignment remain visible. 46 tests, offline solve/assignment/push/audit/sensitivity CLI and SVGs. Not a metric, sampled trajectory, implicit-optimum gradient or certified OT bound.

- Log-sum-exp scaling avoids an entirely underflowed kernel. Full plans and row/column errors expose feasibility separately from cost and entropy.
- Exhaustive720-permutation uniform assignment reference, independent coupling and a deliberately capped failure. No comparison of unlike regularized objectives as a ranking.
- Numeric full-cell heatmaps retain all mass; barycentric target means are explicitly not samples or one-to-one matching.

- Repo: [midya8/transportlab](https://github.com/midya8/transportlab) · Case study: [projects/transportlab.md](projects/transportlab.md)

### FlowLab

Affine-coupling flow from scratch: exact fitted-model density, inverse sampling, analytic input scores and bounded conditional CDF/quantile slices. Aligned window audits reuse one scored grid and expose renormalization effects: narrowing[-4,4] to[-1,1] removes24.35%-31.94% of interpolated mass inside the finite outer window. An analytic narrow-peak counterexample shows two agreeing grids can both be wrong. 45 tests, strict artifacts, offline CLI/SVGs and actual call budgets. No whole-line tail, exact-conditional, calibrated-coverage, OOD or causal claim.

- Alternating invertible 2-D couplings, analytic change of variables, shared tanh conditioners and exact manual gradients. Tiny-model parameter/Jacobian finite differences, both inverse directions and density-normalization sanity checks.
- Same-initialization flow and a genuinely train-fitted Gaussian baseline; independent test rows, final checkpoint and no setting/seed sweep. Full likelihood and sample summaries distinguish invertibility from fit quality.
- Shared-axis figure reports every outside-plot count. Real NVP equations credited, with the image architecture and benchmark claims explicitly out of scope.

- Repo: [midya8/flowlab](https://github.com/midya8/flowlab) · Case study: [projects/flowlab.md](projects/flowlab.md)

### GraphLab

Two-layer GCN from scratch with exact input-margin gradients and budgeted single-edge deletion sensitivity. Input locality differs from graph normalization: node 3 has zero feature gradient for node 0, yet deleting edge 2-3 changes its margin by +0.016852 after degree renormalization. Full signed contributions, every edge effect, preflight call budgets and zero-gradient/large-change counterexample. Original transductive development results remain: selected GCN0.96875, MLP0.34375, scrambled GCN0.515625; final/centroid controls visible. Synthetic graph carries class signal; no causal, probability-attribution, unseen-graph or general ranking claim. 42 tests, strict artifacts and offline CLI/SVGs.

- Sparse normalized GCN, exact model/input gradients and permutation/mask audits. Validation-only selection and selected/final checkpoints remain visible.
- Signed zero-reference margin decomposition has an explicit algebraic sum audit, not a causal validity certificate. Two-hop feature support does not freeze graph degree factors.
- Full leave-one-edge-out audits recompute normalization and preflight E+1 actual model forwards. No joint-deletion, robustness or walltime guarantee.

- Repo: [midya8/graphlab](https://github.com/midya8/graphlab) · Case study: [projects/graphlab.md](projects/graphlab.md)

### DiffuseLab

Learned 2-D diffusion from scratch, now with selected-grid DDIM sampling and exact denoiser-call audits. The same 482-parameter model uses 8/16/64 DDIM steps without retraining. Eight steps saves 87.5% of predictor calls but has worse symmetric reference distance here (0.210661 vs DDPM 0.037103), despite a slightly higher near-center fraction. All 8 neighborhoods reached, uneven frequencies and outliers retained. Full-grid eta=1 matches DDPM arithmetic with matched draws. 33 tests, strict artifacts and offline train/sample/DDIM CLI. Development fixture only, no walltime speedup, image-generation or general ranking claim.

- Explicit DDPM forward/reverse Gaussian arithmetic, handwritten MLP gradients and Adam, fresh-draw noise-MSE audit and same-initialization control.
- DDIM eta [0,1], unique selected grids, clean endpoint and counted predictor invocations. Exact epsilon/path references and full-schedule DDPM equivalence checks. No retraining or claimed quality equivalence.
- Per-mode coverage, symmetric reference distance, collapsed-generator counterexample and shared-axis plots with outside counts. Source equations credited to Ho et al. and Song et al.

- Repo: [midya8/diffuselab](https://github.com/midya8/diffuselab) · Case study: [projects/diffuselab.md](projects/diffuselab.md)

### ChainLab

Hidden Markov models from scratch: log-space inference, Viterbi paths and multi-sequence Baum-Welch, now with prefix-only filtering and multi-step symbol/state forecasts. An exact example separates x-only filtering P(A)=2/3 from future-informed x/y smoothing P(A)=0. Forecasts are dependent horizon marginals, not a joint path. Prefix predictive log scores match full likelihood to about 5.68e-14 on the seed23 development fixture; that is an implementation audit, not a new quality gain. Existing test NLL per symbol: trained0.775631, iid control0.985993, initialization1.017638, generating reference0.771674. Exhaustive references, impossible-prefix rejection, 34 tests and offline CLI/SVG demo. No calibration or state-recovery claim.

- Distinct full-sequence posterior, best-path and prefix-filtering objectives. Marginal modes can form a forbidden path; smoothed states can use future observations.
- Forecast horizon1 transitions before emitting; later horizons do not assimilate guessed observations. Log messages preserve paths whose raw probabilities underflow. Exact future-path and prefix references check both behaviors.
- Unsmoothed EM preserves sequence boundaries, reports zero occupancy and accepts only nondecreasing likelihood updates. The inspected persistent-regime fixture is not an external benchmark, causal decomposition or general model ranking.

- Repo: [midya8/chainlab](https://github.com/midya8/chainlab) · Case study: [projects/chainlab.md](projects/chainlab.md)

### KernelLab

Gaussian-process regression and finite-grid expected-improvement suggestions from scratch. Cholesky solves, separate latent/observation covariance, explicit jitter, marginal likelihood and fixed-parameter LOO. Deterministic EI excludes known rows and returns a full candidate audit, without executing evaluations. A nine-evaluation toy optimization comparison reports grid regret 0.000163 (EI), 0.072944 (space filling) and 0.399473 (one seeded random control). Same pool/initialization/budget; development data, no general ranking or continuous optimum claim. The regression misspecification counterexample remains visible. Dependency-free Python, 36 tests, offline CLI and reproducible SVGs.

- The fixed-kernel regression fixture also shows a confidently wrong long-length-scale arm. Model-based pointwise bands are not calibrated coverage guarantees.
- Exact deterministic-maximization EI, zero-variance positive-part limit, stable Gaussian tails and numerical-integration reference checks. Rejects noisy models and duplicate candidates; all-known pools return no false next suggestion.
- Same 81-point pool, 3 initial points and 6 more evaluations per optimization policy. Full evaluated-target traces, report-only oracle and adverse/misspecification evidence. No objective execution by the suggest API.

- Repo: [midya8/kernellab](https://github.com/midya8/kernellab) · Case study: [projects/kernellab.md](projects/kernellab.md)

### BoostLab

Binary gradient boosting from scratch: mean-residual defaults plus optional capped, L2-regularized Newton leaves on residual-SSE trees. The development fixture selects 35 Newton trees/237 nodes, test accuracy 0.9004/logloss 0.3341; its unselected 80-round checkpoint is also shown (0.8984/0.3469). Mean depth-2 control: 0.8906/0.3400; full-budget stumps: 0.6367/0.7366. Different capacity and settings, no causal or external-benchmark claim. Backward-compatible v1/v2 inference, Hessian/leaf arithmetic tests, validation-only prefix selection. Dependency-free Python, 29 tests and offline CI.

- Seed-7 noisy sign-of-product fixture, 256/128/512 train/validation/test rows. Newton depth-2 uses L2=1, leaf cap 3; validation selects 35 trees, not the last 80-round checkpoint. All fitted controls remain visible in the case study.
- Mean depth-2 and depth-1 controls retain the original settings and results. Validation selects the depth-1 zero-tree prefix (0.4980/0.7060). Same round budgets are not equal capacity.
- Newton refines only leaves, using residual-SSE splits rather than Hessian gains. History records cap and zero-denominator diagnostics. V1 mean artifacts still predict unchanged; new Newton artifacts use v2.
- Dependency-free Python 3.10+, 29 tests, offline CLI demo and CI. Standard boosting sources credited. No line search, new-method, calibration or production-performance claim.

- Repo: [midya8/boostlab](https://github.com/midya8/boostlab) · Case study: [projects/boostlab.md](projects/boostlab.md)

### ShapleyLab

Exact small-feature Shapley attribution from scratch: empirical-background replacement, every coalition available for audit, scalar score callback API and strict JSON CLI.

- For a product prediction of 6, zero background gives [3, 3, 0] but a shifted background gives [2, 3, 0]. Reference choice changes the question, not the model prediction.
- Jointly sampled missing features preserve their mutual dependence. A diagonal-background counterexample has off-manifold singleton hybrids despite zero attribution/efficiency residual: additivity does not certify explanation validity.
- Enumerates all coalitions with a preflight call budget; 3 features/2 background rows require 15 calls. Independent factorial-order reference checks dimensions 1-6, plus linearity, symmetry, dummy and feature-permutation tests. No walltime, causality, conditional-SHAP or model-quality claim.
- Optional atomic groups move correlated blocks together. Three-way product gives grouped [1/2, 1/2], not post-hoc [2/3, 1/3]; grouped games answer a different question. Up to 64 raw features/12 groups, no within-group credit split or cross-group dependence guarantee.
- Optional seeded permutation mode handles up to 64 individual features with cached coalitions and descriptive MC standard errors. A two-permutation product gives [0.5, 0.5, 0] despite exact [1/3, 1/3, 1/3], showing zero observed MC error is not an accuracy bound. No confidence guarantee or sampled groups.
- Dependency-free Python 3.10+, 43 tests, offline demo and CI. Standard Shapley/SHAP formula and masking sources attributed; no new algorithm claim.

- Repo: [midya8/shapleylab](https://github.com/midya8/shapleylab) · Case study: [projects/shapleylab.md](projects/shapleylab.md)

### PolicyLens

Offline contextual-bandit evaluation from scratch: IPS, self-normalized IPS, direct method and doubly robust value estimates with full behavior/target probabilities, reward predictions and support/weight diagnostics.

- In a constructed 20-row balanced design, target truth 0.78 is recovered by IPS/SNIPS/DR despite a wrong constant reward model (direct 0.50). This is an arithmetic fixture, not a random-trial accuracy claim.
- Capping weights at 1 raises ESS 4.9231 to 8.4706 but moves IPS to 0.185 and DR to 0.535. A separate noisy 2000-row log uses an oracle reward model yet DR 0.7532 differs from truth 0.78. No universal-best-estimator claim.
- Optional held-out categorical reward fitting excludes each full fold, reports cell counts and prior-only predictions. On the same noisy log, five-fold DR 0.7509088 is not closer to truth than oracle DR 0.7532475; no estimator ranking. Row-iid splits do not protect clustered/time data.
- Flags unsupported target actions rather than treating reward-model extrapolation as identified policy value. Explicit propensity/support/context and independent/cross-fitted reward-prediction assumptions; no deployment decision or confidence guarantee.
- Dependency-free Python 3.10+, 28 tests, JSON CLI/API and offline CI on Python 3.10-3.13. Standard estimators attributed to their sources, no new theory.

- Repo: [midya8/policylens](https://github.com/midya8/policylens) · Case study: [projects/policylens.md](projects/policylens.md)

### DriftLens

Embedding-distribution tests from scratch in pure Python: unbiased RBF MMD, one cached pooled kernel, exact tiny-sample enumeration and seeded Monte Carlo permutations with nonzero finite p-values.

- On the selected 30x4 development fixture, independent same-generator samples give MMD squared -0.004871, p=0.550; adding +2 to each current coordinate gives 0.634539, p=0.002, the 1/500 resolution floor. Not a power/type-I error benchmark.
- A tiny separated 2-vs-2 example still has exact p=1/3 over six allocations, making finite resolution and non-rejection limits visible.
- Explicit exchangeability, prespecified bandwidth/preprocessing and repeated-test caveats. No cause, model-performance or continuous-monitoring guarantee; non-rejection is not equivalence.
- Dependency-free Python 3.10+, 45 tests, JSON CLI/API with prespecified bandwidth families and Holm correction and prespecified within-block permutations and descriptive row-index witness diagnostics and counted imbalanced-group scoring savings, exact rank-superuniformity check, cached-kernel verification, offline demo and CI on Python 3.10-3.13. Standard method attributed to Gretton et al. and permutation convention to Phipson/Smyth.

- Repo: [midya8/driftlens](https://github.com/midya8/driftlens) · Case study: [projects/driftlens.md](projects/driftlens.md)

### SetGuard

Split-conformal classification sets from scratch: a fixed classifier's probabilities plus held-out calibration labels become a versioned JSON artifact and unlabeled prediction sets. This is set coverage, not probability calibration.

- On the five-class development fixture, alpha=0.1 gives empirical coverage 0.9235 at mean set size 3.017 versus argmax accuracy 0.4960 with one label. An intentionally adversarial label-shift arm drops coverage to 0.0760 at the same set size, showing why exchangeability matters, not a real-world drift rate.
- Corrected finite-sample rank, inclusive ties, all-label boundary and empty sets are explicit. An exact leave-one-out rank audit covers 19/21 positions; tests exhaust 243 tied-score sequences at five alpha values.
- Marginal coverage is a standard theorem under exchangeability and a predictor fixed independently of calibration. It is not coverage for every class, input, fixed split or shifted deployment.
- Dependency-free Python 3.10+, 31 tests, CLI/API fit/predict/evaluate, per-class and size diagnostics, offline demo and Python 3.10-3.13 CI. Optional classwise thresholds with explicit rare/absent-class inclusion. Standard method attributed to Angelopoulos and Bates.

- Repo: [midya8/setguard](https://github.com/midya8/setguard) · Case study: [projects/setguard.md](projects/setguard.md)

### CalibrLab

Confidence calibration from scratch in pure Python, with a JSON CLI/API for caller-supplied validation/test logits, unclipped logit-space NLL and optional conditional paired test-row bootstrap intervals: ECE/MCE/Brier/NLL metrics, per-bin reliability tables, and temperature scaling fit on validation NLL only.

- **Measured calibration repair** - an overfit small-data MLP (train 1.0000, test 0.5563; top bin 0.9735 mean confidence at 0.6602 accuracy) goes from ECE 0.2765 to 0.0651 and test NLL 2.0030 to 1.2060 with one validation-fitted temperature (T = 3.85) - at exactly zero accuracy change, a property of the method asserted bit-for-bit in the gates.
- **Honest bounds, not just wins** - the test-optimal (oracle) temperature 3.30 would give NLL 1.1984, so the validation fit leaves only 0.0076 on the table; post-scaling bins skew mildly under-confident and MCE stays noisy (0.1216), both reported.
- **Gradients by hand, verified** - the MLP's backprop is derived in code and finite-difference checked; the suite separates metric unit tests from fixture regression.
- Dependency-free Python 3.10+, 45 unit tests, a fully offline demo asserting both gate sides, and CI across Python 3.10-3.13.

- Repo: [midya8/calibrlab](https://github.com/midya8/calibrlab) · Case study: [projects/calibrlab.md](projects/calibrlab.md)

### DistillLab

Knowledge distillation built from scratch in pure Python: a teacher trained on abundant data, a 10x smaller student trained on a tenth of the data, and the measured gain compared against matched control arms.

- **Measured against matched controls** - +0.0656 test accuracy over direct training at identical capacity and budget (0.7469 vs 0.6813; teacher 0.8344): pseudo-labels on the teacher's argmax exceed direct by +0.0281 and soft-label distillation exceeds pseudo-labels by +0.0375, uniform label smoothing at eps=0.1 adds nothing, and a permuted-target control sits at exactly chance (0.1250) - measured between-arm differences on this fixture, not causal attribution.
- **Smaller measured train-test gap** - the direct student memorizes its 80 training samples (train 1.0000, train-test gap 0.3187); the distilled student does not (train 0.8000, gap 0.0531) and sits closer to the teacher in KL (0.9563 vs 1.0932).
- **Gradients by hand, verified** - the temperature-scaled combined loss alpha*T^2*CE(softmax(z/T), soft) + (1-a)*CE(softmax(z), y) with its exact logit gradient, finite-difference checked; the T=1 ablation pinned (0.7219 vs 0.7469 at T=4).
- Dependency-free Python 3.10+, 12 unit tests, a fully offline demo asserting both gate sides, and CI across Python 3.10-3.13.

- Repo: [midya8/distilllab](https://github.com/midya8/distilllab) · Case study: [projects/distilllab.md](projects/distilllab.md)

### MoeLab

Mixture-of-experts built from scratch in pure Python: a Switch-style sparse router over linear experts, trained on a regime-switching fixture and measured against a same-budget dense MLP baseline, with gradients derived by hand and finite-difference verified in the suite.

- **The mixture wins on structure, not size** - 0.0303 vs 0.1853 test MSE against a dense MLP with slightly more parameters (136 vs 145) on the checked-in fixture - a measured trained-baseline comparison, with CI regression gates on the mixture's own fit rather than on the baseline staying weak.
- **Routing measured, not assumed** - worst-regime routing purity 1.0000 (every regime routes to exactly one expert on the test set), expert usage shares reported, and the soft-vs-sparse gap pinned: soft evaluation costs 0.6291 vs 0.0303 because the objective is sparse and averaging specialized experts hurts.
- **Honest aux-loss note** - on this symmetric fixture the load-balancing term is not load-bearing (max share 0.25 with and without it, and dropping it fits slightly better at 0.0010); the README says so instead of selling the auxiliary loss.
- Dependency-free Python 3.10+, 9 unit tests, a fully offline demo asserting both gate sides, and CI across Python 3.10-3.13.

- Repo: [midya8/moelab](https://github.com/midya8/moelab) · Case study: [projects/moelab.md](projects/moelab.md)

### AlignLab

Preference-based alignment built from scratch in pure Python: a Bradley-Terry reward model trained on pairwise preferences with a hand-derived logistic gradient, then a categorical policy aligned by gradient ascent on expected reward minus an exact KL penalty to a reference policy - with expectations, KL, and both gradient terms in closed form, so nothing hides behind sampling noise.

- **Utility gained, with a fixture-level control** - on the checked-in fixture, aligning to the learned reward raises true latent utility 2.0375 to 4.6154, while aligning to a reward model trained on utility-independent labels buys only 2.5800 (gated from above). One seeded control is a fixture comparison, not a general proof that signal alone causes improvement.
- **The KL cost measured, not asserted** - the aligned policy pays KL 1.0216 to the reference (entropy 0.7701); the beta=0 ablation collapses onto the argmax-reward style (entropy 0.0136, KL 1.7781) and is gated from below.
- **Exact optimization, verified gradients** - the hand-derived reward and policy gradients are finite-difference checked in the suite; reward holdout accuracy 0.7800 against a noise-trained control at 0.4333, with the achievable gate pinned below the preference-noise ceiling rather than at a flattering 1.0.
- Dependency-free Python 3.10+, 15 unit tests, a fully offline demo asserting both gate sides, and CI across Python 3.10-3.13.

- Repo: [midya8/alignlab](https://github.com/midya8/alignlab) · Case study: [projects/alignlab.md](projects/alignlab.md)

### LoRALab

Low-rank adaptation built from scratch in pure Python: freeze a trained classifier, learn only a rank-r delta `W' = W + B @ A` with hand-derived gradients through the low-rank factors, and measure what adaptation actually bought - accuracy on the shifted distribution, trainable-parameter share, and retained accuracy on the original one.

- **The trade-off measured, all three sides** - on the checked-in fixture (base accuracy on the shifted distribution collapses to 0.44), a rank-2 adapter recovers to 1.0000, matching full fine-tuning while training 67.7% of the parameters; retention on the original distribution is measured too (0.7556 adapter vs 0.9556 full fine-tuning on this fixture) and reported rather than hidden.
- **Merge equivalence pinned to float reassociation** - the merged model `(W + B @ A) x` reproduces adapter logits `W x + B (A x)` with max abs diff ~1e-14 on the fixture; the test pins the diff below 1e-12 and pins that it is nonzero - exact algebra, approximate arithmetic, claimed as such.
- **Gates that fail in both directions** - `--min-base-drop` proves the distribution shift still exercises adaptation, `--min-adapted-accuracy` and `--max-rank2-param-share` pin the recovery story, `--max-merge-diff` pins merge fidelity; the suite shows an impossible cap fails.
- Dependency-free Python 3.10+, 14 unit tests, a fully offline demo asserting both gate sides, and CI across Python 3.10-3.13.

- Repo: [midya8/loralab](https://github.com/midya8/loralab) · Case study: [projects/loralab.md](projects/loralab.md)

### SpecLab

Speculative decoding built from scratch in pure Python: a cheap draft model proposes a block of tokens, a target model verifies it, and a greedy-construction invariant keeps the output identical to target-only decoding - with the implementation verified token-for-token on the tested configurations and verification rounds counted exactly.

- **Equivalence: algorithm invariant plus finite verification** - the ideal greedy construction emits only target-confirmed or target-chosen tokens; the checked-in implementation is verified against that invariant across four draft/target configurations, three lengths, and gamma 1/2/4/8.
- **Verification rounds counted, honestly labeled** - on the checked-in fixture (order-3 draft, order-4 target, 8 prompts x 60 tokens, gamma=4): mean draft acceptance 0.800, 122 modeled verification rounds against 480 naive (74.6% fewer) - a modeled batched-pass count, reported alongside the implementation's actual sequential scoring work (510 vs 480 calls).
- **Acceptance measured, including the failure mode** - a deliberately mismatched draft/target pair drops acceptance to 0.03 and is pinned in the suite, so acceptance is demonstrably measured rather than assumed.
- Dependency-free Python 3.10+, 14 unit tests, a fully offline demo asserting both gate sides, and CI across Python 3.10-3.13.

- Repo: [midya8/speclab](https://github.com/midya8/speclab) · Case study: [projects/speclab.md](projects/speclab.md)

### StructGate

Grammar-constrained generation built from scratch in pure Python: an incremental JSON validator and a closed-schema validator compute the exact set of legal next tokens for any prefix, generation samples from an exact character-level n-gram distribution masked to that set, and the evaluation measures both what the constraints buy and what they cost.

- **Conformance, measured** - on the checked-in fixture, grammar-constrained sampling yields valid JSON on 40/40 seeded draws and schema-constrained sampling yields schema-conforming records on 40/40, against an unconstrained control at 3/40 on the same model and seeds. The control is gated from above so it cannot quietly stop exercising the constraint.
- **The mask's cost in nats** - renormalizing to the legal token set costs -ln(Z) per step, exactly KL(p || p_masked); the report shows it per mode (mean 1.3496 grammar, 0.8209 schema on the fixture) instead of hiding it.
- **Validators verified against the stdlib** - the JSON state machine matches Python's json module on 32 adversarial cases in the suite, with exact allowed-set queries, snapshot/restore determinism, and a pinned number/whitespace boundary regression.
- Dependency-free Python 3.10+, 33 unit tests, a fully offline demo asserting both gate sides, and CI across Python 3.10-3.13.

- Repo: [midya8/structgate](https://github.com/midya8/structgate) · Case study: [projects/structgate.md](projects/structgate.md)

### QuantLab

Post-training int8 quantization built from scratch in pure Python: symmetric per-tensor and per-channel scales, byte-exact size accounting, reconstruction error metrics, and a perceptron-trained fixture model whose int8 accuracy cost is measured exactly on held-out data - plus a controlled study showing where quantization error actually lives.

- **Measured, not benchmarked** - on the checked-in fixture, per-channel int8 matches fp32 test accuracy exactly (drop 0.0000) at 3.765x smaller weight storage; CI pins `--max-accuracy-drop 0.0` and `--min-ratio 3.5`.
- **Error located** - boost one matrix row x100 and per-tensor's single scale crushes the rest (small-row SNR 9.25 dB) while per-channel holds 48.39 dB: a measured 39.14 dB gain, gated in CI.
- **Honest scope** - simulated int8 storage with values proven in range, byte arithmetic for sizes, post-training only; the README says what real models would change.
- Dependency-free Python 3.10+, 28 unit tests, a fully offline demo asserting both gate sides, and CI across Python 3.10-3.13.

- Repo: [midya8/quantlab](https://github.com/midya8/quantlab) · Case study: [projects/quantlab.md](projects/quantlab.md)

### RAGLine

Retrieval-augmented answering built from scratch in pure Python: a deterministic templated corpus chunked with stable ids, token-hashed sparse TF-IDF embeddings, top-k cosine retrieval, extractive answers that always cite their source chunk, and a lexical-overlap grounding check scored against each answer's cited chunk - shown in a tested negative control to flag a corrupted citation.

- **The RAG loop as inspectable steps** - corpus, embed, retrieve, answer, verify, each dependency-free and deterministic from one seed.
- **Grounding as a gate, not a slogan** - the check scores token overlap between answer and cited chunk; `--require-grounded` and `--min-grounded` fail CI when overlap drops, and the suite's negative control shows a corrupted citation is flagged. Lexical scope: tested wrong-citation cases, not arbitrary misinterpretation.
- **Measured retrieval quality** - fixture evaluation over questions with known topics: recall@3 = 1.00, MRR = 0.94, grounded rate = 1.00, pinned in CI.
- Dependency-free Python 3.10+, 31 unit tests, a fully offline demo asserting both gate sides, and CI across Python 3.10-3.13.

- Repo: [midya8/ragline](https://github.com/midya8/ragline) · Case study: [projects/ragline.md](projects/ragline.md)

### KVLens

KV-cached incremental decoding built from scratch in pure Python: a tiny causal multi-head attention block with seeded weights runs greedy generation down two paths - naive full recompute over the whole prefix, and a production-style KV cache with batched prefill plus one incremental step per new token - and the two paths are verified bitwise-identical while a matmul FLOP counter measures the savings directly.

- **Bitwise equivalence, not approximate** - both paths share the same operations in the same order, so the equivalence sweep reports a max absolute logit difference of exactly 0.0 across model configurations and prefix lengths; greedy generations match token for token in the test suite.
- **Measured savings** - a FLOP counter in both paths reports the saved fraction (90.8% at 32 generated tokens on the default fixture); `--min-savings` and `--require-identical` gates fail CI when either property regresses.
- **Honest bounds** - the counter covers matmuls only and the project makes no latency claim; the README states what is counted and why memory bandwidth, not FLOPs, is the real reason caching is fast.
- Dependency-free Python 3.10+, 28 unit tests, a fully offline demo asserting both gates, and CI across Python 3.10-3.13.

- Repo: [midya8/kvlens](https://github.com/midya8/kvlens) · Case study: [projects/kvlens.md](projects/kvlens.md)

### AttnLens

Causal multi-head self-attention trained from scratch in pure Python: two residual blocks of Q/K/V projections and masked scaled dot-product attention, hand-derived backpropagation checked against finite differences for every parameter group on the suite's fixture model, and a marker-recall task where the trained model's query position concentrates attention on the recalled key token (~0.9 weight on the checked-in seed) - an observed recall pattern in the family of induction-head behaviors.

- **Real training, no autograd** - gradients for embeddings, per-head Q/K/V, output projections and both layers through the residuals, all derived by hand and finite-difference verified on the fixture configuration in the test suite.
- **Attention you can measure** - the recall task is one a single layer cannot solve cleanly in principle (the key's content does not say it followed a marker); after training, per-head entropy, previous-token mass and recall-attention stats plus text heatmaps show the query position attending to the key. An observation on this task and seed, not a claim about larger models.
- **Deterministic and gated** - one seeded RNG for init and per-epoch sample generation; `--max-final-loss`, `--min-accuracy` and `--min-recall-attention` fail CI when training regresses; without gradient clipping, training was observed to diverge in the tested configurations.
- Dependency-free Python 3.10+, 46 unit tests, a fully offline demo that verifies the recall pattern, and CI across Python 3.10-3.13.

- Repo: [midya8/attnlens](https://github.com/midya8/attnlens) · Case study: [projects/attnlens.md](projects/attnlens.md)

### EmbedKit

Word embeddings trained from scratch with pure-Python SGNS (skip-gram with negative sampling): sigmoid-gradient SGD over (center, context) pairs with negatives drawn from the unigram^0.75 distribution, all randomness from one seeded RNG, plus a coherence evaluator that scores how often a word's nearest neighbors stay in its topic cluster - with CI gates.

- **Real SGNS, no dependencies** - weight init, pair shuffling and negative draws all come from one seeded generator, so a corpus and seed reproduce the same vectors bit for bit.
- **Coherence as a measurable gate** - per-word neighbor purity against labeled topic clusters plus an intra-vs-inter separation margin; `--min-coherence` and `--min-margin` fail CI when training regresses.
- **Reproducible end to end** - the demo corpus is regenerated deterministically, training pins quality numbers in tests, and terminal/JSON/Markdown reports carry the evaluation.
- Dependency-free Python 3.10+, 40 unit tests, a fully offline demo that asserts same-topic neighbors and both gate sides, and CI across Python 3.10-3.13.

- Repo: [midya8/embedkit](https://github.com/midya8/embedkit) · Case study: [projects/embedkit.md](projects/embedkit.md)

### PlanBench

Validate and simulate agent task plans before they run: plans are DAGs of tool calls, checked for unknown tools, unknown or cyclic dependencies and inputs no dependency produces, then executed in a deterministic parallel simulation where flaky tools fail under a seeded RNG, steps retry within policy and dependents of failures are skipped - with makespan, cost, critical path and parallelism reported and gated in CI.

- **Semantic validation, not just syntax** - duplicate step ids, unknown tools, unknown/self/cyclic dependencies, and `requires` inputs no dependency's tool produces, each as a severity-ranked finding.
- **Deterministic parallel simulation** - steps start as dependencies succeed; tool failures come from a seeded RNG, so the same plan, registry and seed always produce the same trace, retries and skip cascades included.
- **Plan-shape metrics and gates** - makespan, total cost with retries, critical path by duration, parallelism; `--require-success`, `--max-makespan`, `--max-cost`, `--max-findings` fail the pipeline when a plan stops meeting policy.
- Dependency-free Python 3.10+, 29 unit tests, a fully offline demo with a flaky-tool research plan and a rejected broken plan, and CI across Python 3.10-3.13.

- Repo: [midya8/planbench](https://github.com/midya8/planbench) · Case study: [projects/planbench.md](projects/planbench.md)

### DecodeLab

Decoding strategies for language models, from scratch: greedy decoding with deterministic tie-breaking, seeded temperature/top-k/top-p sampling, and beam search, all over an add-k smoothed n-gram model with an exact next-token distribution, plus generation-quality metrics (distinct-1/2, repetition rate, unigram entropy) with terminal/JSON/Markdown reports and CI gates.

- **An exact distribution to decode from** - the n-gram model's next-token probabilities come straight from counts, so strategies are compared against ground truth, never an approximation.
- **Reproducible sampling** - every sampler takes an explicit seed; the same seed and corpus produce the same text, so differences are attributable to the strategy, not luck.
- **Quality as metrics, not impressions** - distinct-1/distinct-2, repetition rate and entropy per strategy, side by side; `--min-distinct-2` and `--max-repetition` fail CI when a decoding change pushes generation below policy.
- Dependency-free Python 3.10+, 36 unit tests, a fully offline demo that asserts exact greedy output and seeded reproducibility, and CI across Python 3.10-3.13.

- Repo: [midya8/decodelab](https://github.com/midya8/decodelab) · Case study: [projects/decodelab.md](projects/decodelab.md)

### VectorLite

Exact and approximate kNN vector search from scratch: brute-force exact kNN (cosine and L2) with deterministic tie-breaking, a seeded random-hyperplane LSH index for approximate cosine search, and recall@k of the approximate index measured against the exact baseline and enforced with a CI gate.

- **Recall is measured, not assumed** - `benchmark` self-queries every vector through both indexes and reports mean recall@k of LSH against the exact baseline; `--min-recall` fails the pipeline when fewer bits, a new seed or a lower sharing threshold drops recall below policy.
- **Deterministic LSH** - bit signatures from seeded Gaussian hyperplanes; the same seed and data rebuild the identical index bit for bit, and candidates are rescored exactly before ranking.
- **An exact baseline that is always right** - brute-force scan with score-then-id tie-breaking, O(n) per query by design: it exists to be correct, not fast.
- Dependency-free Python 3.10+, 31 unit tests, a fully offline demo that asserts mean recall@3 of 0.9 or better plus both sides of the gate, and CI across Python 3.10-3.13.

- Repo: [midya8/vectorlite](https://github.com/midya8/vectorlite) · Case study: [projects/vectorlite.md](projects/vectorlite.md)

### GroundCheck

Offline lexical grounding checks for answers against their sources: citation validation, per-sentence lexical support scoring against source documents, numeric consistency checks, terminal/JSON/Markdown reports, and CI gates that fail on lexically ungrounded output.

- **Grounding as a CI gate** - `--min-support`, `--max-unsupported` and `--max-findings` fail the pipeline when an answer cites nothing real, makes claims no passage lexically supports, or invents figures.
- **Passage-aware support scoring** - content-token containment measured against whole source documents, so a sentence combining facts from several sentences of one retrieved passage is correctly supported while claims no passage contains are flagged.
- **Numbers get no slack** - every figure in the answer must appear in the sources by exact or equal-value match, with decimal-safe sentence splitting so `1.57` is one number, not two fragments. Known pass-throughs are documented: negation, wrong attribution and coincidental matches all pass.
- Dependency-free Python 3.10+, 43 unit tests, a fully offline demo that accepts a grounded answer and rejects an ungrounded one, and CI across Python 3.10-3.13.

- Repo: [midya8/groundcheck](https://github.com/midya8/groundcheck) · Case study: [projects/groundcheck.md](projects/groundcheck.md)

### TokenForge

Byte-level BPE tokenizers trained from scratch: deterministic merge training with exact pair counts over GPT-2-style pre-tokenization boundaries, rank-ordered encoding with exact round trips, JSON vocab persistence, and compression statistics with JSON/Markdown reports and a CI quality gate.

- **The tokenizer as an inspectable artifact** - exact pair counting, deterministic tie-breaking and plain-JSON merge storage mean a tokenizer can be diffed, reviewed and rebuilt byte for byte.
- **Byte-level coverage with boundary discipline** - the 256 byte values are the base vocabulary, so any text encodes and decodes exactly, while merges never cross word, number, symbol or whitespace boundaries.
- **Compression as a gate** - bytes-per-token and token-frequency statistics in terminal, JSON and Markdown form, with `--min-compression` failing CI when a tokenizer regresses.
- Dependency-free Python 3.10+, 40 unit tests, a fully offline demo that trains a 300-token vocabulary and asserts round trips and both sides of the gate, and CI across Python 3.10-3.13.

- Repo: [midya8/tokenforge](https://github.com/midya8/tokenforge) · Case study: [projects/tokenforge.md](projects/tokenforge.md)

### RetrievalBench

Offline retrieval evaluation for RAG and search pipelines: an exact Okapi BM25 index over local JSONL corpora, token-window chunking with overlap and parent-document collapsing, graded qrels, per-query and macro-averaged recall@k/precision@k/MRR/nDCG@k, JSON and Markdown reports, and quality gates that fail CI on retrieval regressions.

- **Retrieval quality as a reproducible gate** - rank golden queries against graded qrels and fail CI when a chunking, indexing or document change drops recall@k, precision@k, MRR or nDCG@k below policy.
- **Exact and deterministic by design** - no pruning and no ANN approximation, so scores and rankings are stable and diffable; chunk hits collapse back to their parent document so qrels stay at document granularity.
- **Reports built for review** - per-query breakdowns with the weakest queries surfaced, JSON artifacts for tooling, and Markdown reports that fit native CI job-summary surfaces.
- Dependency-free Python 3.10+, 42 unit tests, a fully offline demo that asserts metrics, chunked evaluation and both sides of the quality gates, and CI across Python 3.10-3.13.

- Repo: [midya8/retrievalbench](https://github.com/midya8/retrievalbench) · Case study: [projects/retrievalbench.md](projects/retrievalbench.md)

### EvalForge

Local-first evaluation for LLM and agent outputs: versioned JSONL task suites, deterministic scorers, a stdin/stdout adapter contract, retries, timeouts, bounded parallel execution, persistent run artifacts, baseline regression gates, and self-contained escaped HTML, JUnit XML, Markdown and SARIF run/comparison reports.

- **Evaluation as a repeatable gate** - run the same suite against any command-line model or agent adapter, compare a candidate to a saved baseline, and fail on score regressions, adapter errors, or latency policy breaches.
- **Deterministic checks before model judging** - exact, contains, regex, JSON schema-ish, numeric tolerance, length, and similarity scorers make results reproducible without a network dependency.
- **Artifacts built for review** - JSON run records preserve prompts, outputs, scores, errors, and timings; JUnit XML reports expose results to CI test viewers; Markdown run and regression-comparison summaries fit native CI job-summary surfaces; SARIF 2.1.0 output feeds failed tasks, adapter errors and regressions to code-scanning tools; HTML reports are standalone and escape untrusted model output by default.
- Dependency-free Python 3.10+, 68 unit tests, a fully offline six-task demo that validates JUnit, Markdown and SARIF run/regression output, and CI across Python 3.10-3.13.

- Repo: [midya8/evalforge](https://github.com/midya8/evalforge)

### AgentTrace

Local-first validation, analysis and reporting for AI agent execution traces: JSONL trace structure checks, run summaries, tool/LLM call counts, latency and cost rollups, graph depth, repeated-step loop detection, baseline/candidate regression comparison, quality gates, a standalone escaped HTML timeline, deterministic JUnit XML output for CI test viewers, Markdown job summaries, and SARIF 2.1.0 output for code-scanning integrations.

- **Agent runs as inspectable data** - parse JSONL traces from local agents, test fixtures, internal tools or hosted-model adapters without sending prompts or outputs anywhere.
- **Gates that catch agent failure modes** - fail CI on errored steps, p95 latency, cost, step count, a repeated tool/action signature that indicates a loop, or regressions against a saved baseline trace.
- **Reports built for review** - deterministic JSON analysis artifacts, JUnit XML for CI test viewers, Markdown job summaries, SARIF 2.1.0 for code-scanning tools, and a self-contained HTML report show run summaries and per-step timelines with untrusted trace fields escaped by default.
- Dependency-free Python 3.10+, 33 unit tests, a fully offline fixed-trace baseline/candidate demo that validates JUnit, Markdown and SARIF output, and CI across Python 3.10-3.13.

- Repo: [midya8/agenttrace](https://github.com/midya8/agenttrace)

### PromptGuard

Local-first prompt, secret and prompt-injection linting for AI systems: OpenAI/AWS-style key, GitHub/Slack/Google token and JWT checks, assigned-secret and private-key detection, email/phone/Luhn-validated card detection, injection-language rules, prompt metadata frontmatter checks, redacted terminal, JSON, SARIF, JUnit XML, Markdown and escaped HTML reports, severity or finding-count CI gates, and fingerprint-based baseline suppression so CI only gates on new findings.

- **Prompt files as reviewed production configuration** - scan prompt, Markdown, JSON and YAML files before credentials, personal data or unsafe instruction patterns ship with an AI workflow.
- **Redaction by default** - reports keep enough location and excerpt context for review without copying full credentials or contact details into output artifacts.
- **Gates that fit CI** - deterministic rule IDs, severities, JSON/SARIF/JUnit/Markdown artifacts and exit codes let a repository fail on high-severity findings or cap total findings.
- Dependency-free Python 3.10+, 68 unit tests, a fully offline fixture demo that validates SARIF, JUnit and Markdown output and the baseline suppression flow against safe, risky and runtime-generated token fixtures, and CI across Python 3.10-3.13.

- Repo: [midya8/promptguard](https://github.com/midya8/promptguard)

### ScratchGPT

A GPT built and trained from scratch in pure NumPy: a ~400-line reverse-mode autograd engine with hand-written backward rules, a pre-LN transformer, Adam training, resumable checkpoints, and a temperature/top-k sampling CLI.

- **Backprop without an ML framework** - hand-written broadcasting-aware backward rules for core tensor ops, reductions, softmax/cross-entropy, layer norm and gather, verified against central finite differences.
- **A model, not just a diagram** - a 419,328-parameter, 2-layer/4-head character GPT with causal multi-head self-attention, GPT-2-style residual initialization, gradient clipping, warmup and periodic evaluation.
- **Reproducible from a fresh clone** - TinyShakespeare data, loss records, a trained checkpoint and sample output ship with the repository; editable install runs the training and sampling CLIs, and a causal-leak test proves position t cannot attend to t+1.
- 11 unit tests, a documented 3,000-step CPU training run reaching 1.83 nats/char validation loss in the shipped config, and CI on Python 3.12.

- Repo: [midya8/scratchgpt](https://github.com/midya8/scratchgpt) · Case study: [projects/scratchgpt.md](projects/scratchgpt.md)

### sre-toolkit

Dependency-free Python utilities for day-to-day SRE work: error budgets, burn-rate alerting, alert triage, and the Markdown documents an incident workflow runs on.

- **Error budgets and burn-rate alerting** — budget math with exhaustion projections and remaining-bad-event counts, multi-window burn-rate alerting with custom rules, a `--suggest` mode that emits the standard three-tier multi-window policy for any SLO window, and `burn --replay` to tune alert policy against a past incident's time series.
- **Alert triage that reduces noise** — rule-based triage (custom rule files) that dedupes repeats, keeps each alert's fire count, ranks the noisiest alerts first (`--top-talkers`), inhibits lower-severity symptoms under an active critical, and applies bounded, reasoned silences matched on service, severity, or summary text (`--silences`). `triage --routes` maps services to owning teams with an explicit default owner, and `--by-owner` rolls the board up per team, worst severity first.
- **Documents as output** — SLO definitions (Markdown or JSON), status reports with budget-exhaustion projections and worst-first sorting, and postmortems with automatic response metrics (Markdown or JSON), plus MTTR aggregation (mean/median/p90 per severity, weekly trend view, JSON output) across incidents and fleet-wide roll-ups across whole incident sets. `metrics --action-items` groups open postmortem items per incident with days since resolution and exits 1 when items go stale past `--stale-days`.
- CLI plus importable library, 254 unit tests, CI across Python 3.10-3.13. Every command doubles as a scriptable health gate through meaningful exit codes.

- Repo: [midya8/sre-toolkit](https://github.com/midya8/sre-toolkit) · Case study: [projects/sre-toolkit.md](projects/sre-toolkit.md)

### loglens

Dependency-free access-log analysis for incident work: the numbers that matter in the first five minutes — error rate, status distribution, hottest failing paths, and the source IPs behind 5xxs.

- **Headline answers first, then the detail** — per-bucket incident timelines, p50/p95/p99 latency, per-path and per-client volume/error/latency tables sortable by errors, volume, or p95, a 2xx/3xx/4xx/5xx status-class roll-up, throughput (mean/peak per bucket), fixed-bucket latency-distribution reports, and an hour-of-day (UTC) pattern breakdown.
- **Narrow to the failing slice** — time-window, status-code, class, and path-prefix filters scope every statistic; consecutive-bucket spike windows, method/user-agent/referer triage behind the 5xxs, and a listing of the individual requests behind the 5xxs.
- **Before/after around a deploy** — `--split-at` compares the windows on either side of a deploy timestamp (error-rate delta, newly failing paths, paths that recovered), and `--vs` compares two whole logs, ranking the paths carrying the biggest error-count increases as regressions.
- **A gate, not just a report** — Apdex user-satisfaction scoring at a chosen threshold T (overall and per-path, worst first) with a `--min-apdex` gate, a `--max-error-rate` gate that exits 1 when the 5xx rate breaches the threshold, the failing-path status pivot (`--path-status`), and Markdown incident reports with per-path breakdowns, spike windows, and optional before/after deploy comparisons.
- Parses nginx/Apache combined and JSON logs with per-line auto-detection, standard library only, CLI plus importable library, 241 unit tests with CI across Python 3.10-3.13.

- Repo: [midya8/loglens](https://github.com/midya8/loglens) · Case study: [projects/loglens.md](projects/loglens.md)

### flowkit

Dependency-free workflow runner: JSON-defined DAGs of shell commands with retries and exponential backoff, per-attempt timeouts, fail-fast or continue-on-error semantics, and parallel execution of independent steps (`--jobs`).

- **Flows that stay readable** — conditional steps (`when` on environment variables), subset runs (`--only`/`--skip`), and end-phase hook steps (`trigger: on_failure`, `on_success`, or `finally`) for cleanup and notify work pinned to the run's outcome.
- **Validated before executing** — definitions are checked up front (duplicate step names, dangling dependencies, cycles, malformed interpolation) and executed in deterministic topological order; layered flow-level and per-step environment variables interpolate into commands (`$VAR`, `${VAR:-default}`), with a `--strict-env` pre-run check that fails on unset references.
- **Reports as output** — dry-run plan mode and text/JSON run reports with captured output tails (also writable to a JSON report file, with full per-step logs via `--output-dir`); exit codes make it a scriptable gate (0 ok / 1 step failed / 2 invalid flow file).
- Standard library only, CLI plus importable library, 123 unit tests, CI across Python 3.10-3.13.

- Repo: [midya8/flowkit](https://github.com/midya8/flowkit) · Case study: [projects/flowkit.md](projects/flowkit.md)

### uptimekit

Synthetic uptime monitoring and availability reporting in pure Python, no dependencies and no database.

- **Probes that call a failure a failure** — HTTP (status, keyword-in-body, latency), TCP connect, and TLS certificate-expiry probes, with latency assertions that turn slow into down and TLS expiry thresholds that turn a quietly approaching expiry into one.
- **One history, honestly kept** — an append-only JSONL history with atomic retention compaction, availability roll-ups with p50/p95 latency percentiles, a per-day trend strip where monitoring gaps stay visible, and window-over-window comparison.
- **Alerting that means something** — incident detection with a consecutive-failure flap guard and a sustained-outage gate (`--max-open-minutes` pages on real outages, not self-healing blips); `check` exits 1 on any failure so a cron line doubles as alerting, `report --fail-open` gates CI on open incidents, and `report --fail-slo` exits 1 on an SLO breach.
- **SLOs and a status page from the same record** — SLO targets (`"slo": 99.9`) measured by `report --config` (error budget consumed, met-or-breached status), a watch mode for hosts without cron, and a self-contained HTML status-page renderer (inline CSS, no JavaScript, fully escaped).
- CLI plus importable library, 98 unit tests running fully offline, CI on Python 3.11.

- Repo: [midya8/uptimekit](https://github.com/midya8/uptimekit) · Case study: [projects/uptimekit.md](projects/uptimekit.md)

### Kurdistan International Sociological Association website

Trilingual website (English, Sorani Kurdish right-to-left, and Kurmanji Kurdish) built with Next.js, TypeScript, and Tailwind, exported as static HTML and hosted on Cloudflare.

- **Three languages, one route tree** — English, Sorani Kurdish (right-to-left), and Kurmanji Kurdish under a single `[locale]` route tree, with `lang` and `dir` set per locale from one i18n config, so direction is handled at the layout level rather than patched onto translated strings.
- **Publishing is a file, not a form** — news posts are Markdown files per locale with frontmatter, UI text lives in per-locale JSON dictionaries, and pushing to `main` redeploys the static export from Cloudflare — no CMS, no server, no database.

- Repo: [midya8/kurdistansociology-website](https://github.com/midya8/kurdistansociology-website)
- Live: [kurdistansociology.com](https://kurdistansociology.com)
- Case study: [projects/kurdistansociology-website.md](projects/kurdistansociology-website.md)

### Personal site — midya.ca

A personal site set against a procedurally generated Three.js galaxy that adapts rendering quality to the device and respects reduced-motion settings. Built with React, TypeScript, and Vite.

- **A galaxy that fits the device** — the procedural WebGL scene picks a low, mid, or high quality profile from viewport size, device memory, CPU cores, and pixel ratio, setting particle budgets, bloom strength, and a 40/55/60 fps frame cap.
- **Respectful by default** — `prefers-reduced-motion` gets a single static frame, rendering pauses while the tab is hidden, and a CSS gradient takes over if WebGL is unavailable; geometries, materials, the post-processing composer, and the WebGL context are all disposed on unmount.

- Repo: [midya8/midya.ca](https://github.com/midya8/midya.ca)
- Live: [midya.ca](https://midya.ca)
- Case study: [projects/midya-ca.md](projects/midya-ca.md)

## Find me

- [midya.ca](https://midya.ca)
- [LinkedIn](https://www.linkedin.com/in/midyarahmani/)
