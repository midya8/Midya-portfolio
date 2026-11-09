# Midya Rahmani

Toronto-based technologist with 12+ years across technology, financial services, and telecommunications. Lately building with large language models, agentic systems, and workflow automation.

## What I build

- **LLM and agentic systems** — practical AI workflows, not demos: systems that do real work end to end.
- **Workflow automation** — taking manual, multi-step processes and making them reliable and repeatable.
- **Web platforms** — TypeScript, React, Next.js, and static-first architectures that stay fast and maintainable.

## How I build

The projects below share an approach, written up in [approach.md](approach.md): choose the simplest architecture that meets the requirement, make tools that fit into scripts as well as terminals, validate before executing, and let reports and documents be outputs of the work rather than afterthoughts — all designed around real constraints, from right-to-left layouts to reduced-motion preferences.

## Contents

- **AI systems:** [FactorLab](#factorlab) · [SubmodLab](#submodlab) · [DPPLab](#dpplab) · [CTCLab](#ctclab) · [PPOlab](#ppolab) · [TagLab](#taglab) · [SpectralLab](#spectrallab) · [ForestLab](#forestlab) · [RatingLab](#ratinglab) · [MarginLab](#marginlab) · [MixtureLab](#mixturelab) · [PartsLab](#partslab) · [ClusterLab](#clusterlab) · [DenoiseLab](#denoiselab) · [TreeLab](#treelab) · [DigitLab](#digitlab) · [ScanLab](#scanlab) · [Correlab](#correlab) · [GameLab](#gamelab) · [BetLab](#betlab) · [PrivacyLab](#privacylab) · [SparseLab](#sparselab) · [InfluenceLab](#influencelab) · [FisherLab](#fisherlab) · [LatentLab](#latentlab) · [ErgodLab](#ergodlab) · [ScoreLab](#scorelab) · [BanditLab](#banditlab) · [BeliefLab](#belieflab) · [BellmanLab](#bellmanlab) · [VariLab](#varilab) · [RobustLab](#robustlab) · [CausalLab](#causallab) · [ParticleLab](#particlelab) · [SegmentLab](#segmentlab) · [HamiltonLab](#hamiltonlab) · [TransportLab](#transportlab) · [FlowLab](#flowlab) · [GraphLab](#graphlab) · [DiffuseLab](#diffuselab) · [ChainLab](#chainlab) · [KernelLab](#kernellab) · [BoostLab](#boostlab) · [ShapleyLab](#shapleylab) · [PolicyLens](#policylens) · [DriftLens](#driftlens) · [SetGuard](#setguard) · [CalibrLab](#calibrlab) · [DistillLab](#distilllab) · [MoeLab](#moelab) · [AlignLab](#alignlab) · [LoRALab](#loralab) · [SpecLab](#speclab) · [StructGate](#structgate) · [QuantLab](#quantlab) · [RAGLine](#ragline) · [KVLens](#kvlens) · [AttnLens](#attnlens) · [EmbedKit](#embedkit) · [PlanBench](#planbench) · [DecodeLab](#decodelab) · [VectorLite](#vectorlite) · [GroundCheck](#groundcheck) · [TokenForge](#tokenforge) · [RetrievalBench](#retrievalbench) · [EvalForge](#evalforge) · [AgentTrace](#agenttrace) · [PromptGuard](#promptguard) · [ScratchGPT](#scratchgpt)
- **Python utilities:** [sre-toolkit](#sre-toolkit) · [loglens](#loglens) · [flowkit](#flowkit) · [uptimekit](#uptimekit)
- **Web platforms:** [Kurdistan International Sociological Association website](#kurdistan-international-sociological-association-website) · [Personal site — midya.ca](#personal-site--midyaca)
- [Find me](#find-me)

## Selected projects

### CutLab

Exact binary submodular energy graph cuts with signed rational offsets, every pair/terminal reduction, shortest augmenting paths including reverse routing, every-cut residual dual slack and the full SCC/closure optimum family. A strict single-flip control stops at energy 2 while the certified joint optimum is 0; a unary-only control has gap 2. Independent Python/BigInt agree on 24 reports / 24,624 exact leaves. 21 Python tests on 3.10-3.13, complete rendered records, SVG checks and installed reproduction. Supplied synthetic costs, at most six variables; classical methods, no learned model, image benchmark, speed or new-algorithm claim.

[Source](https://github.com/midya8/cutlab) · [Live inspector](https://midya8.github.io/cutlab/) · [Case study](projects/cutlab.md)

### FactorLab

Exact rational finite factor elimination with every joined product, reduction/tie, fill edge and small-order census. A mixed sum/max control returns an upper bound of 11 versus true marginal-MAP mass 10, while joint MAP weight 6 projects to the wrong decision. A five-variable star gives the same partition at 62 versus 18 joined entries, width 4 versus 1. Independent Python/BigInt agree on 24 reports / 23,114 exact leaves; 24 Python tests on 3.10-3.13, dense partial-product oracles, full-record Chrome checks and installed reproduction. Supplied synthetic potentials, not learned quality, a scalable solver or a timing benchmark.

[Source](https://github.com/midya8/factorlab) · [Live inspector](https://midya8.github.io/factorlab/) · [Case study](projects/factorlab.md)

### SubmodLab

Exact rational finite subset selection with every greedy marginal, optimum tie, monotonicity edge, local diminishing-return witness and proof-derived cardinality upper bound. The retained coverage counterexample gives greedy 5 versus optimum 6; a separate singleton top-k control gives 5 versus updated greedy 9. Invalid synergy/nonmonotone tables withhold theorem fields. Dependency-free Python and independent BigInt JavaScript agree on 24 complete reports / 16,426 exact leaves, with 24 Python tests on 3.10-3.13 and actual-Chrome checks of 360 subset rows/bars and 2,056 full records. Established theory on at most six items, not learned similarity, a scalable optimizer or downstream selection quality.

[Source](https://github.com/midya8/submodlab) · [Live inspector](https://midya8.github.io/submodlab/) · [Case study](projects/submodlab.md)

The separate rounding inspector now exposes the exact multilinear extension, every excluded-item gradient and excluded-pair Hessian context, independent-product count probabilities and both endpoints of every deterministic cardinality swap. A two-item half-probability control has expected count 1 yet exceeds budget 1 with probability 1/4; its duplicate-coverage expectation 3/4 rounds to a singleton worth 1. Nonmonotone submodular controls are accepted, while synergy and wrong total probability mass refuse rounding. The extension adds nine Python tests (33 total), 21 reports matching 10,682 exact native/BigInt leaves, independent product/derivative/path oracles, full-record Chrome checks and installed reproduction. This is bounded deterministic rounding, not continuous optimization, randomized marginal preservation, a general matroid method or a learned-quality claim.

[Live rounding inspector](https://midya8.github.io/submodlab/rounding.html) · [Rounding method](https://github.com/midya8/submodlab/blob/main/ROUNDING.md)

### DPPLab

Exact-rational finite DPP subset laws with every determinant, inclusion-kernel witness, Schur include/exclude conditioning and fixed-total-size contrast. Dependency-free Python and independent BigInt JavaScript agree on 24 complete reports / 4,050 exact leaves; 24 Python tests on 3.10-3.13 and actual-Chrome full-record/geometry checks. Duplicate-item controls separate zero co-occurrence from equal-marginal independence. Established bounded L-ensembles, not learned relevance, a scalable sampler or a downstream quality result.

[Code](https://github.com/midya8/dpplab) · [Live inspector](https://midya8.github.io/dpplab/) · [Case study](projects/dpplab.md)

### CTCLab

Offline CTC target marginalization with log-space forward/backward, full state/symbol posteriors and logit gradients, plus every exhaustive path and collapsed transcript. The editable independent JavaScript inspector shows why a greedy best path can lose to summed transcript mass: two uniform blank/A frames assign 0.25 to empty output and 0.75 to A. Twenty retained reports, 25 Python tests across 3.10-3.13, Decimal/state enumeration, 300 finite-difference checks and real-Chrome full-record/diagram audits. Established CTC on tiny synthetic logits, not a trained recognizer, speech/OCR benchmark or novel algorithm; numerical rank buckets and impossible-target conventions are explicit. [Live alignment inspector](https://midya8.github.io/ctclab/) · [Method and limits](https://github.com/midya8/ctclab/blob/main/METHOD.md). [Case study](projects/ctclab.md).

### PPOlab

From-scratch NumPy PPO with a corrected internal-timeout collector, separate bootstrap/trace masks, full GAE credit matrices and sign-dependent clip-gradient audits. Independent scalar JavaScript evaluates all 4,675 checkpoint parameters and real CartPole physics. Fifty Python tests retain all 18 original tests; four Node/actual-Chrome tests compare 26 full reports/12,408 numbers and all 14,871 original one-step observations. New free-running paths can diverge: the reference run differs on 377 actions despite matching all 30 return lengths. Original checkpoint/results retained; no training-improvement, speed, trajectory-equivalence, KL-bound or universal-solve claim. [Live boundary and policy inspector](https://midya8.github.io/ppolab/) · [Equations, bug and limits](https://github.com/midya8/ppolab/blob/main/BOUNDARIES.md). [Case study](projects/ppolab.md).

### TagLab

Manual linear-chain conditional random fields with analytic gradients and all 327 optimization states replayed. The selected chain improves test NLL (0.557614 versus 0.813715) but loses on Viterbi token errors (66/164 versus the trained same-feature control's 56/164). Exact fixed-score inference covers position-wise label events, auditable joint-path sampling and nonlocal occurrence-count events. Count-augmented prefix/suffix messages expose complete count laws, conditional nodes/pairs, best paths and event derivatives. An independent-node count control shows why matching expected counts does not enforce an exact total. 43 Python and 20 Node/Chrome tests cover rational/BigInt path oracles, finite differences, cross-language witnesses and 5,895 UI states/queries; eleven-module/nine-command installed reproduction. Original synthetic sequences, not an NLP benchmark, causal experiment or calibrated confidence. Original fits and budget-exhaustion warnings stay visible; deterministic PRNG, finite-precision and near-tie limits are explicit. [Count inspector](https://midya8.github.io/taglab/counts.html) · [Label events and joint sampling](https://midya8.github.io/taglab/evidence.html) · [Training inspector](https://midya8.github.io/taglab/) · [Method and limits](https://github.com/midya8/taglab/blob/main/METHOD.md). [Case study](projects/taglab.md).

### SpectralLab

Normalized spectral clustering with manual affinity/Laplacian/k-means code and explicitly disclosed NumPy eigensolves. All 18 fixed graphs and raw k-means controls remain visible; larger eigengaps and spectral rounding can still give worse answers. v0.2 adds full degree-response derivatives and a basis-invariant projector tangent, four smooth base graphs, 28 fixed finite states including a boundary refusal, and two refused base controls. Shared-scale heatmaps compare actual refits with first-order geometry; numerically equal tested rounding partitions remain explicit, not a label-gradient or robustness claim. Thirty-three Python and nine Node/real-Chrome tests cover independent graph/cut references, 83 derivative controls, repeated-block rotations, 1,728 original browser point states and 168 new sensitivity states. Installed six-module/nine-command reproduction checks four exact exports. Original synthetic full-data illustrations, not held-out prediction or exact discrete optimization. [Graph inspector](https://midya8.github.io/spectrallab/). [Sensitivity inspector](https://midya8.github.io/spectrallab/sensitivity.html). [Derivation and limits](https://github.com/midya8/spectrallab/blob/main/SENSITIVITY.md). [Case study](projects/spectrallab.md).

### ForestLab

Manual binary CART forests with exact integer Gini split ordering, complete bootstrap-count witnesses and an editable inspector that separates full-forest votes from OOB votes. Exact-copy grouping prevents identical licensed UCI feature vectors from crossing partitions. All eight forests, four single trees and seven controls stay visible: the validation-selected forest makes 3/270 test errors, versus a stronger selected 5NN control at 0/270 and a single tree at 8/270. 39 Python and 12 Node/real-Chrome tests cover 60 rational split oracles, 10,784 forest comparisons, 8,088 control scores, 6,464 OOB membership records and 992 actual browser paths. Ten-module/ten-command installed reproduction. Historical numeric classification, not banknote authentication; vote fractions are not calibrated probabilities and OOB is not independent specimen validation. [Live forest and OOB inspector](https://midya8.github.io/forestlab/). [Method and limits](https://github.com/midya8/forestlab/blob/main/METHOD.md). [Case study](projects/forestlab.md). V0.2 adds [joint permutation diagnostics](https://midya8.github.io/forestlab/permutation.html): all 15 feature blocks, 16 shared shuffles and 129,600 model-row prediction checks, including the stronger frozen 5NN control. Donor/recipient witnesses and an exact support counterexample stay visible. Reused-validation description, not causal importance, fresh test performance or uncertainty intervals.

The v0.3 [leaf-collision inspector](https://midya8.github.io/forestlab/proximity.html) exposes all-tree similarity as an explicit Gram matrix, with exact integer/BigInt sum-of-squares witnesses. A separate jointly-OOB view keeps pair-specific tree counts and undefined comparisons. A constructed negative quadratic form (-2) and triangle failure show why OOB normalization is not a universal kernel guarantee. All 512 small partition controls, 5,760 native/scalar-JS matrix entries, 1,152 actual pair states and 13,824 heatmap colors are checked. Frozen supervised model geometry, not semantic similarity, causal influence, uncertainty or a new score. [Geometry derivation and limits](https://github.com/midya8/forestlab/blob/main/PROXIMITY.md).

### RatingLab

Observed-only rating factorization with manual NumPy alternating ridge solves, per-block decrease accounting, normal-equation residuals and full gradients. All eleven fits remain inspectable. A separately validation-selected bias-only control slightly beats the selected factors on test RMSE (.656176 versus .656457); all eight factor fits exhaust their stationarity budget. 37 Python and 14 Node/real-Chrome tests include 60 independent exact rational ridge references, eleven fresh refits, test-label poisoning and 12,771 scalar/native predictions. The browser recomputes arbitrary indexed pairs and shared factor rotations, exposing why coordinate products are not causal preferences. Ten-module installed wheel with eight main CLI commands and two single-row conditional-response module commands. CC BY 4.0 historical UCI ratings, MIT code. Missing pairs are not negatives, and observed-rating RMSE is not top-N relevance, missing-pair accuracy or calibrated certainty.

The v0.2 conditional-response extension separates saved scores, a freshly re-solved unmodified ridge block and its finite rating edit or row deletion. It exposes leverage, the positive deletion denominator, query derivatives and all-opposite-index response curves. Sixty additional exact rational design systems, 2,784 direct deleted-block refits and 576 native/scalar-JavaScript witnesses check the formulas. Original factors and scores are unchanged. The mean and opposite factors remain frozen and retain information from the row: this is not full-model leave-one-out validation, causal influence, data unlearning or an uncertainty bound. [Conditional edit/deletion inspector](https://midya8.github.io/ratinglab/influence.html). [Derivation and limits](https://github.com/midya8/ratinglab/blob/main/INFLUENCE.md).

The v0.3 joint-batch inspector changes or removes multiple original training rows within one frozen block. Target edits add; joint deletions solve a coupled Schur system and generally differ from a sum of separate-original-baseline deletions. It shows the full source-bound problem, conservative positive-ridge bound, numerical condition/refusal checks and all-query joint/separate curves. Independent checks add 320 rational direct-system cases, 128 real augmented-least-squares cases and 320 complete native/browser Cholesky responses plus 4 controls. 37 Python and 14 Node/actual-Chrome tests, ten-module wheel and eight main CLI plus two single-row module commands. Original fits, scores and stronger bias control stay unchanged. This remains a conditional calculation, not full ALS retraining, cross-validation, causal attribution, uncertainty or data unlearning. [Joint batch inspector](https://midya8.github.io/ratinglab/batch.html). [Derivation and limits](https://github.com/midya8/ratinglab/blob/main/BATCH.md).

[Source](https://github.com/midya8/ratinglab) · [Live inspector](https://midya8.github.io/ratinglab/) · [Case study](projects/ratinglab.md)

### MarginLab

Manual linear/RBF soft-margin SVM learning with replayable pair updates and editable 30-feature scores. Version 0.3 adds exact finite original-unit input boxes: attained affine score bounds, both corners, tie-aware labels, all 30 interval edits and independent Fraction/BigInt readers with separate source consistency. 36 Python/15 Node-real-Chrome tests include 120 exhaustive corner cases, 256 direct exact dual endpoint sums, 128 full cross-language responses, 4,552 original inference checks and eight fresh fits. Installed reproduction covers 11 modules and 9 main commands plus the box exporter. Original fits, holdout scores, split and exact training-objective proofs are unchanged. Synthetic boxes are not clinical tolerances or plausible interventions; exact affine arithmetic is not a floating-inference safety, RBF, generalization or authenticity guarantee.

[Exact input-box inspector](https://midya8.github.io/marginlab/box.html) · [Box derivation and limits](https://github.com/midya8/marginlab/blob/main/BOX.md)

[Source](https://github.com/midya8/marginlab) · [Live inspector](https://midya8.github.io/marginlab/) · [Exact linear proofs](https://midya8.github.io/marginlab/certificate.html) · [Case study](projects/marginlab.md)

### MixtureLab

Manual Gaussian-mixture EM on licensed UCI chemistry: constrained covariance M-steps, complete likelihood/Q/KL witnesses and a frozen label-free holdout across all 24 fits. Scalar-browser density, input derivatives, full Hessians and bounded sufficient-ascent traces expose the difference between local calculations and mode certificates. Original models, data, splits and scores stay unchanged. Component posteriors are not cultivar probabilities or calibrated certainty. CC BY 4.0 data, MIT code. [Density inspector](https://midya8.github.io/mixturelab/). [Input geometry](https://midya8.github.io/mixturelab/geometry.html).

The new [observed-coordinate conditional inspector](https://midya8.github.io/mixturelab/conditional.html) reweights by marginal evidence and keeps full Schur-complement, within- and between-component covariance. Synthetic controls show a mean in a density gap and variance increasing from 1.09 to 25.1. 45 Python/eleven Node tests cover 100 independent precision-block controls, 5,696 original model/row/mask factorization checks, 160 complete native/scalar-JS references and 160 actual UI cases. Twelve-module/nine-command installed reproduction retains all original refits and audits. Analytical masks on complete source data, not real missingness validation, causal inference, calibrated intervals or new accuracy. [Conditional method and limits](https://github.com/midya8/mixturelab/blob/main/CONDITIONAL.md).

- Repo: [midya8/mixturelab](https://github.com/midya8/mixturelab)
- Case study: [projects/mixturelab.md](projects/mixturelab.md)

### PartsLab

Nonnegative parts learning on the original UCI digits: six manual NumPy factorization fits, fixed-basis NNLS with per-row numerical KKT stopping, and actual editable-input browser decompositions. All 3,823 training images fit without labels; training-only restart selection preserves the 1,797-row official holdout. Rank-matched signed PCA and SVD beat NMF on test MSE at every fixed rank and stay visible. All six joint fits exhaust their stationarity budget, rather than being mislabeled converged. Zero-locking, scale/permutation and duplicate-basis controls expose why additive parts are not unique semantic explanations. 38 Python and eleven Node/real-Chrome tests include independent active-set oracles, finite-difference gradients, full test-loader-prohibited refits, 120 native/browser decompositions and 2,048 contribution pixels. Ten-module/ten-CLI installed wheel; CC BY 4.0 data, MIT code. [Equations, protocol and limits](https://github.com/midya8/partslab/blob/main/METHOD.md). [Open the live parts inspector](https://midya8.github.io/partslab/).

- Repo: [midya8/partslab](https://github.com/midya8/partslab)
- Case study: [projects/partslab.md](projects/partslab.md)

The v0.2 fixed-basis certificate adds exact binary64 primal/dual arithmetic, outward-rounded objective intervals and portable JSON proofs with an independent Python Fraction verifier. Eighty exact rational active-set optima and all 120 cross-language witness references are checked. The live browser verifies its own candidates, including zero-sweep unfinished solves, and accepts valid pasted proofs while rejecting tampered ones. A residual-shift bound can be loose; even zero gap does not imply unique coefficients. Original fits, scores and selection remain unchanged. [Certificate proof and limits](https://github.com/midya8/partslab/blob/main/CERTIFICATE.md).

V0.3 adds an [exact fixed-face pixel inspector](https://midya8.github.io/partslab/face.html): nominate a face from the numeric NNLS result, re-solve it exactly, and intersect every affine KKT inequality with the pixel domain. All endpoint ties, singular refusals, singleton faces and duplicate-basis nonuniqueness stay explicit. 38 Python and eleven Node/Chrome tests cover 200 independently enumerated tiny face candidates, all 120 stored nominations, 54 complete native/BigInt/Worker witnesses and 10,368 endpoint pixel colors. Ten modules/ten commands with all six fresh fits reproduced. Original data, models and scores remain unchanged. One candidate interval, not a full path, unique support, robustness or joint-NMF optimum. [Math and limits](https://github.com/midya8/partslab/blob/main/FACE.md).

### ClusterLab

Real-data unsupervised clustering with manual k-means++/Lloyd updates, forty complete restart witnesses and fitting-only PCA/whitening controls. All 3,823 original UCI training digits fit without labels; the 1,797-row official holdout is audited with permutation-invariant scores and all-row silhouettes. The live browser recomputes membership for editable digits, displays mixed-label centroids and exposes all restart descents. Raw uniform initialization slightly beats careful seeding on test ARI despite slightly worse fitting inertia; no general seeding advantage or cross-geometry inertia ranking is claimed. 48 Python tests plus thirteen Node/real-Chrome tests cover independent pair/entropy/distance references, a rational local-minimum counterexample, full refit with test-loader prohibition, frozen-hash evaluation, all 80 public model/example cases and keyboard/copy/download/mobile controls. Ten-module/six-CLI installed wheel. [Open the live clustering inspector](https://midya8.github.io/clusterlab/). CC BY 4.0 data, MIT code; arbitrary groups, not digit predictions or calibrated confidence.

The v0.2 restart inspector exposes all forty saved models, 180 distinct within-arm restart comparisons and forty self-pairs. A manual integer Hungarian solver supplies optimal center permutations and primal/dual witnesses, independently checked against subset-DP optima for all 220 matrices. Browser BigInt checks those exact saved rounded-cost certificates; 800 native/scalar-JavaScript inference pairs and all 400 directed pair controls are tested. Same-data initialization sensitivity is not sampling stability or useful-class discovery; matching centers need not align the actual assignment for an input. Original fits and holdout scores remain unchanged. [Open the live restart inspector](https://midya8.github.io/clusterlab/stability.html). [Restart matching method](https://github.com/midya8/clusterlab/blob/main/STABILITY.md).

The v0.3 ambiguity audit adds 2,200 exact selected-edge exclusion witnesses, best-distinct permutations and optimal-matching counts. Independent full-cost dynamic programs check all 220 gaps and counts; browser BigInt verifies all 4,000 oriented exclusions. The matching is unique in every saved real matrix, while tied and unused-tight-edge controls expose why an optimum alone proves neither uniqueness nor a large margin. A strict sufficient cost-entry perturbation bound is not a sharp radius, pixel robustness or statistical uncertainty. All original fits, scores and earlier matching witnesses remain unchanged. [Uniqueness and gap proof](https://github.com/midya8/clusterlab/blob/main/AMBIGUITY.md).

- Repo: [midya8/clusterlab](https://github.com/midya8/clusterlab)
- Case study: [projects/clusterlab.md](projects/clusterlab.md)

### DenoiseLab

DenoiseLab's [two-pixel retrieval map](https://midya8.github.io/denoiselab/plane.html) now shows exact rational closed minimum cells over two observed values, including area, segment-only, point-only and explicitly proved empty regions. Fraction/BigInt witnesses retain all 3,062 original fitting-row coefficients. A source-matched verifier checks supporting halfplanes, maximal lower-dimensional cells and nonnegative infeasibility combinations without rerunning clipping. Shared boundaries use complete all-row exact tie queries, not an interior representative. [Geometry, proof and limits](https://github.com/midya8/denoiselab/blob/main/PLANE.md).

52 Python/fourteen Node/Chrome tests include independent boundary-pair enumeration of 238 small-source cells and 2,110 rational queries, forty complete cross-language maps, 160 browser queries and 30,720 actual canvas colors. Ten-module/nine-command installed reproduction retains full refit/evaluation. [Scalar paths](https://midya8.github.io/denoiselab/path.html), [neural/PCA response](https://midya8.github.io/denoiselab/response.html) and the [original reconstruction audit](https://midya8.github.io/denoiselab/) remain live with stronger winning controls visible. Fixed two-coordinate slice only, not general robustness, causal recourse, uncertainty, better accuracy or binary64 tie equivalence. Licensed UCI data, MIT code; original models and scores unchanged.

- Repo: [midya8/denoiselab](https://github.com/midya8/denoiselab)
- Case study: [projects/denoiselab.md](projects/denoiselab.md)

### TreeLab

Budgeted whole-ensemble counterfactual search with exact weighted-L1 objective bounds, verified common-input witnesses and explicit optimal/infeasible/unfinished states. A best-first queue intersects all 32 trees, propagates forced branches and uses known one-axis witnesses as checked warm starts. The fixed 36-case audit preserves unfinished all-feature searches at 4,096 expansions instead of calling them optimal or infeasible; alcohol-only cases can finish. 101 Python tests plus five Node/real-Chrome tests include independent tiny-forest exhaustive grids, budget-gap checks, member inference and responsive inspector controls. Nine-module/nineteen-CLI wheel reproduction; original models, reports and three figures unchanged. Established constrained model search, not causal recourse, plausible chemistry, scalable optimization or new accuracy. The [ensemble search inspector](https://midya8.github.io/treelab/forest.html), [single-tree explorer](https://midya8.github.io/treelab/counterfactual.html) and [one-axis explorer](https://midya8.github.io/treelab/) remain live.

- Repo: [midya8/treelab](https://github.com/midya8/treelab)
- Case study: [projects/treelab.md](projects/treelab.md)

### DigitLab

A [live model inspector](https://midya8.github.io/digitlab/) now adds baseline-relative class-logit Integrated Gradients for the unchanged UCI digit models. Choose the class and zero or fit-only mean reference, inspect all 64 signed contributions and their logit-sum residual, and keep the attack label separate. An algebraic tanh specialization is checked against independent 128-node quadrature on 40 reference vectors; all 7,188 official model/reference/row cases are finite. 78 Python tests and six Node/real-Chrome tests include 106 attribution reference vectors plus the existing 52 inference/gradient cases. Four reproducible audit figures, ten-module/ten-CLI wheel checks, and mobile/keyboard/touch controls. Established attribution, not a new method, causal importance, explanation quality or a certificate. The stronger same-fit 1NN clean result, exact linear box/radius proofs and original data/models remain visible.

- Live demo: [model inspector](https://midya8.github.io/digitlab/)
- Repo: [midya8/digitlab](https://github.com/midya8/digitlab)
- Case study: [projects/digitlab.md](projects/digitlab.md)

### ScanLab

Exact state-space scans with failure controls, not a speed benchmark.
v0.3 adds coupled full-matrix transitions, noncommuting order witnesses,
transposed reverse adjoints and every matrix/write/initial-state JVP/VJP.
The transpose identity is -440563/15120; a missing-transpose control gives gap
7831/2520. Reversing only matrix-product order changes the final state, while
both mistakes are invisible on diagonal restrictions. Six two-state steps use
108 multiplications/80 additions versus sequential 24/24, despite unit-pair
span 4 versus 6. 63 tests include 96 homogeneous-product shapes, 672 independent
polynomial VJP coordinates, 51 instrumented arithmetic cases and all preserved
diagonal/HVP/gated controls. Three full-witness SVGs, six-command/nine-module
wheel parity and five CI jobs. Serial Python, not a general AD engine,
dense HVP, trained Mamba/S4, new algorithm or GPU-throughput claim.

- Repo: [midya8/scanlab](https://github.com/midya8/scanlab)
- Case study: [projects/scanlab.md](projects/scanlab.md)

### Correlab

Exact-rational general-sum joint-play obedience, finite-history and private override-signal certificates. Coarse, pairwise, full-swap and conditional gains retain every term and attaining deviation. v0.2 adds explicit hidden-baseline pass/override channels, supplied post-garbling lifts with exact slack identities, and all action partitions through size four. Developed controls give gains 4/3, 5/3, 1 for three two-signal partitions; attributed Roth reveal controls bridge 0 to 11/30. Two reproducible SVGs, seven-module/seven-CLI wheel parity and 50 tests. Supplied finite models only, not an equilibrium solver, learned information design, universal channel-order test, privacy or safety guarantee.

- Repo: [midya8/correlab](https://github.com/midya8/correlab)
- Case study: [projects/correlab.md](projects/correlab.md)

### GameLab

Exact-rational zero-sum game audits with complete optimal faces, minimax witnesses and deterministic perturbation certificates. The interval extension computes fixed-policy worst joint gap using one shared payoff table: its developed control gives gap 1, not the incompatible separate worst-regret sum 2. Signed support witnesses, attainable value extrema and separate robust-security policies stay visible. Strict offline JSON CLI, two reproducible SVGs, six-module wheel parity and 53 tests. Small supplied boxes, not statistical coverage, coupled uncertainty, worst-gap policy optimization, real-agent strength or a scalable/new solver.

- Repo: [midya8/gamelab](https://github.com/midya8/gamelab)
- Case study: [projects/gamelab.md](projects/gamelab.md)

### BetLab

Exact-rational sequential evidence for bounded paired model scores, with fixed/past-only betting, full null-tree audits and prespecified start allocations with future reserve. The confidence extension inverts a separate conservative fixed-bet mean family, certifies rational crossing/noncrossing brackets and retains earlier bounds after reversal. Its 256-path coverage control excludes the true mean with probability 2187/16384 at alpha 1/4. Three reproducible SVGs, strict offline JSON CLI, seven-module wheel parity and 67 tests. Supplied-law/fixture audits, not drifting-mean estimation, optimized betting, causal effects or model-selection correction.

- Repo: [midya8/betlab](https://github.com/midya8/betlab)
- Case study: [projects/betlab.md](projects/betlab.md)

### PrivacyLab

Exact finite-channel differential privacy with rational hockey-stick events, adaptive transcript laws and clipped-mass certificates. The factor-frontier extension computes every affine piece of the worst-neighbor profile, including a developed switch at 5/4 absent from the likelihood-ratio grid. Exact inverse delta budgets retain minimality witnesses or singular-support obstructions, and distinguish huge finite factors from impossible targets. Three reproducible SVGs, strict offline JSON CLI, seven-module wheel parity and 63 tests. Small supplied-law certificates, not trained-model privacy, secure sampling or a production accountant.

- Repo: [midya8/privacylab](https://github.com/midya8/privacylab)
- Case study: [projects/privacylab.md](projects/privacylab.md)

### SparseLab

LASSO optimization audits with primal/dual/KKT witnesses, duplicate-coefficient ambiguity and exact Gap Safe zero certificates. The affine-branch extension solves rational Gram equations and every sign/inactive KKT half-line: its developed control has five exact intervals, a feature leaving at lambda = 1 and re-entering negative at 1/3. Boundary zeros are allowed; singular branches return explicit noncertificates. Strict offline JSON CLI, three reproducible SVGs, seven-module wheel parity and 62 tests. A supplied-branch verifier, not a general LARS solver, complete support recovery, causal feature selector or speedup claim.

- Repo: [midya8/sparselab](https://github.com/midya8/sparselab)
- Case study: [projects/sparselab.md](projects/sparselab.md)

### InfluenceLab

Convex logistic influence functions with converged Newton fits and full Hessian/solve witnesses. The deletion-path extension refits continuously along selected weight changes, then checks integrated local derivatives against actual endpoint loss. Deleting all seven developed rows reverses the frozen first-order sign (-0.004253 vs +0.079105); group deletion is not a sum of separate refits. Simpson16 residuals stay visible, including +0.000744 on that all-row path. Strict JSON CLI, two reproducible SVGs, five-module wheel parity and 43 tests. Small numerical reference, not causal attribution, certified quadrature or machine unlearning.

- Repo: [midya8/influencelab](https://github.com/midya8/influencelab)
- Case study: [projects/influencelab.md](projects/influencelab.md)

### FisherLab

Exact-rational natural-policy-gradient geometry, with singular Fisher solves, full RREF/nullspace witnesses and positive pairwise PSD certificates. Four full-tangent charts agree exactly; diagonal/identity-damped approximations and nonlinear finite steps expose the limits. The shared-context extension has positive aggregate reward derivative 1/64 but context 1 derivative -1/8, with exact projection 7/16=1/64+27/64. Independent context parameters reach both targets; uniform reweighting changes the objective, and naive joint logits can move supposedly fixed context mass. Strict offline JSON CLI, two reproducible SVGs and 45 tests. Local supplied-model audits, not an MDP trainer or optimizer-superiority benchmark.

- Repo: [midya8/fisherlab](https://github.com/midya8/fisherlab)
- Case study: [projects/fisherlab.md](projects/fisherlab.md)

### LatentLab

A Gaussian VAE from scalar Python, with all 150 pathwise gradients checked independently. The importance extension separates random log-evidence estimates, expected IWAE bounds and same-sample Jensen comparisons. An exact linear-Gaussian posterior recovers its known evidence; a full-support rare-atom control has ESS 64 yet underestimates evidence by factor 999,000 on an event with probability 93.80%. Neural noise prefixes are visibly nonmonotone. The original trained fixture still shows lower no-KL reconstruction error but worse prior samples; even beta 1 leaves 51.56% outside the mode neighborhoods. 43 tests cover independent derivatives/quadrature, exact rational rare-event expectations, extreme log weights, strict checkpoints and two reproducible SVGs. Five-module wheel reproduces both demos outside checkout. Evidence auditing, not IWAE training, an ESS accuracy certificate, exact nonlinear likelihood, image generation or distribution recovery.

- Repo: [midya8/latentlab](https://github.com/midya8/latentlab)
- Case study: [projects/latentlab.md](projects/latentlab.md)

### ErgodLab

Exact rational stationary policy sensitivity, Poisson bias and Markov reward audits. Independent directed spanning-tree derivatives match normalized stationary linear systems. The discounted extension separates the true fixed-start objective gradient from a stationary proxy: at beta 1/2 the proxy has exact curl -1/147, ruling out a local scalar potential, and differs from the true gradient [5/98,-1/98]. At beta 1 it uses the centered Poisson limit, not a singular inverse. Original fixtures retain the occupancy-only gradient 1/18 and sticky/alternating reward variances 7/4 versus 0 despite identical one-step variance 1/4. 39 tests cover independent paths, determinants, finite differences, analytic proxy/curl grids and two reproducible SVGs. Six-module wheel verified outside checkout. Supplied finite irreducible models, not GPOMDP, training, gradient-estimator variance, a CLT or a monotone-bias guarantee.

- Repo: [midya8/ergodlab](https://github.com/midya8/ergodlab)
- Case study: [projects/ergodlab.md](projects/ergodlab.md)

### ScoreLab

Exact policy-gradient distributions, complete trajectory witnesses and rational covariance certificates. Matrix-valued time/state score controls solve singular normal equations and minimize the full covariance within a fixed linear-control class. A three-action example has exact gradient [-1/9,1/3]: the best scalar baseline leaves trace variance 53/612, while a full matrix gives zero on every action. A separate 64-path sequential model has only a small change, 1.462519 to 1.460918, with singular score ranks [1,0,1,1,1,1]. Original scalar audits retain the value-baseline counterexample, increasing variance 4/625 to 36/625. 36 tests include 256 analytic Bernoulli policies, independent derivatives and Cartesian covariance references, matrix-control checks across 15 additional settings, all principal minors of gap certificates, nonunique coefficients with unique supported corrections, coordinate-transform congruence and two reproducible SVGs. Six-module wheel verified outside the checkout. Exact supplied finite models, not training results, a fitted critic or universal zero variance.

- Repo: [midya8/scorelab](https://github.com/midya8/scorelab) · Case study: [projects/scorelab.md](projects/scorelab.md)

### BanditLab

Exact finite-budget Beta-Bernoulli planning with complete posterior-state graphs, action values/ties, a fully updating greedy control and exact clairvoyant prior bound. A prescribed three-pull example chooses the lower-mean arm first: optimal expected reward 187/108 versus greedy 46/27, gain 1/36. At two pulls both first arms tie and gain is zero. New forward audits support named or exact randomized state policies, conserve probability at every pull and expose all reward/occupancy flows. Summed occupancy-weighted optimal Bellman gaps equal policy loss: greedy loses 1/36 at its first decision; fixed loses 7/108 across three decisions. Optimal/greedy visit 14 of 35 possible states, fixed visits 10. 34 tests include 2,048 two-arm and 1,728 three-arm policy-tree references, 144 independent named-policy history audits, randomized joint-history checks, independent Bernstein/Beta integrals and two reproducible SVGs. Six-module wheel verified outside the source tree. Exact supplied-prior expectations, not empirical trials, causal attribution or frequentist guarantees.

- Repo: [midya8/banditlab](https://github.com/midya8/banditlab) · Case study: [projects/banditlab.md](projects/banditlab.md)

### BeliefLab

Exact rational finite-horizon POMDP planning for two hidden states, with policy-tree witnesses and all-belief envelopes. An optimized open-loop baseline checks every fixed action sequence over the same model and horizon: the supplied sensing fixture gives contingent value 7/10 versus zero at the uniform belief, with exact feedback-gap area 49/400. A forward execution audit traces every history/state mass, conditional belief and discounted reward contribution, including impossible branches without fabricated posteriors. Fixed-tree regret certificates expose every zero-regret interval: a probe tree optimal at the uniform prior loses 13/10 at either certain-state prior. Discounted all-belief Bellman-residual brackets connect finite envelopes to infinite optimal value without pretending the finite tree runs forever: raw residual 1/100 can hide value error 1. A perfect-probe fixture brackets infinite value 9/10 by [113/150,9/10]. 86 tests cover exact residual cells, independent infinite-value references and 81 model settings, complete depth-two trees, fixed sequences, exact crossing cells, full joint path occupancies and independent belief recursion. Strict JSON CLI, preflight caps, four reproducible SVGs and an isolated ten-module wheel. Supplied-model calculations only, not learned information value, empirical calibration, causal sensor performance or real-world safety.

- Repo: [midya8/belieflab](https://github.com/midya8/belieflab) · Case study: [projects/belieflab.md](projects/belieflab.md)

### BellmanLab

Exact rational discounted planning with residual certificates, rectangular robust control and nested controller/adversary policy iteration. A residual of 1/100 hides value error 1; a nominal winner loses 6/5 under supplied ambiguity; global uncertainty (-2/3) differs from row-wise closure (-2). Exact inner nature solves expose every policy, scenario Q-value and tie. Controller improvement waits for inner stability: independent cap examples distinguish an upper bound, an exact nonoptimal policy value and a jointly stable optimum. 70 tests audit independent 972 nominal and 3,888 controller/adversary policy references, every nested witness, monotonicity, both cap paths and three SVGs. Strict rational JSON, full histories and an isolated eight-module wheel. Supplied models only, not learned confidence, online RL, unique-policy, policy-loss or real-world safety guarantees.

- Repo: [midya8/bellmanlab](https://github.com/midya8/bellmanlab) · Case study: [projects/bellmanlab.md](projects/bellmanlab.md)

### VariLab

Mean-field inference and exact graph inference from scratch, with inspectable certificates rather than optimizer success claims. A supplied two-mode Ising target improves ELBO from 1.386294 to 3.005027 while maximum mean error worsens from 0 to 0.994902. Exact-rational Hessian congruence and signed witnesses distinguish saddles, singular boundaries and adjacent binary-float inputs without a tolerance. Evidence-aware forest sum-product and rational MAP add full message traces, exact tie counts and compatible joint decisions. Bounded cyclic elimination adds symbolic resource preflight, conditional query tables and rational MAP traceback: a 63-spin odd ring has exact score 61 and 126 optima; independent locally optimal spins can still form a wrong joint answer. A refused star order is contrasted with an accepted order on the same graph. 183 tests and six reproducible SVGs cover independent exhaustive oracles, full intermediate factors, score/count certificates and both passing and failing gates. Dependency-free Python, strict JSON CLI and an isolated-wheel demo. Supplied models only; float sum-product is separate from binary-rational scores. No learned posterior, calibrated uncertainty, causal, optimal-treewidth or runtime claim.

- Repo: [midya8/varilab](https://github.com/midya8/varilab) · Case study: [projects/varilab.md](projects/varilab.md)

### RobustLab

Binary linear adversarial robustness from scratch: exact L1/L2/L-infinity norm-ball margins and attainable perturbation witnesses, with hand-derived robust logistic subgradients. A fixed shifted synthetic holdout exposes the clean/robust trade-off: ordinary training is 100% clean / 20% strict robust at L-infinity radius 0.30; robust training is 80% / 80%. Both robust-gate directions stay visible. Independent rational corner enumeration, finite differences and nonsmooth subgradient inequalities. Exact rational L1/L-infinity audits expose float boundary-flag disagreements while preserving the actual binary input values. Box-constrained L1/L-infinity audits return equal exact primal/dual bounds and expose a false robustness claim from clipping an L1 attack. 80 tests and three reproducible SVGs. Dependency-free Python and strict JSON CLI. Supplied linear models and explicit norm balls or box intersections only; mathematical audits, not neural-network or production security guarantees.

- Repo: [midya8/robustlab](https://github.com/midya8/robustlab) · Case study: [projects/robustlab.md](projects/robustlab.md)

### CausalLab

Exact finite structural causal models with distinct observation, intervention and shared-noise counterfactual queries. A 100-world confounding fixture reverses a +.26 association into a -.10 supplied-model intervention difference; observationally identical mechanisms still disagree on intervention and counterfactual answers. Log-space rare evidence, bounded noise-world traces and all 64 tiny Boolean mechanism pairs. Named multi-world counterfactual joints expose shared-noise response dependence missed by identical action marginals. Stable/flip mechanisms share all observations and single-action marginals but have different response-type joints. The naive-product failure stays visible. Sharp binary response bounds now return exact rational attaining joint witnesses from point action marginals, with optional explicit monotonicity and undefined zero-support conditional rates. Graphical d-separation adds ancestor/moral-edge certificates, collider-descendant checks and explicit incoming-edge surgery. A bounded backdoor-set search exposes collider bias, forbidden descendants and explicit candidate availability. 138 tests and five reproducible SVGs keep the missing coupling assumptions visible. Dependency-free Python and strict JSON CLI. Mechanisms are supplied assumptions, not causes learned from observational data.

- Repo: [midya8/causallab](https://github.com/midya8/causallab) · Case study: [projects/causallab.md](projects/causallab.md)

### ParticleLab

Bootstrap particle filtering from scratch with complete log-weight, resampling and ancestry histories. A static-support failure ends with full weight ESS but zero particle variance while the exact posterior remains uncertain. Kalman/static-square references, terminal-weighted genealogies and bounded backward-simulation smoothing with a linear RTS reference, a no-resampling comparison, all sixteen development seeds and 114 tests keep the approximation inspectable. Early path collapse stays visible even when current states are distinct; backward draws add path diversity without claiming exact uncertainty. An optional linear observation-conditioned proposal includes all-seed predictive-weight comparisons, including worse variance RMSE on the inherited example. Dependency-free Python, strict JSON CLI and reproducible SVG. Finite scalar models, not convergence or calibrated real-data claims.

- Repo: [midya8/particlelab](https://github.com/midya8/particlelab) · Case study: [projects/particlelab.md](projects/particlelab.md)

### SegmentLab

Exact offline Gaussian changepoint inference that exposes confident outlier cuts, impossible joint events and the gap between MAP and minimum expected boundary loss. Normalized constrained priors, full partition marginals, direct joint draws, same-design replicate mixtures and entropy/KL audits remain inspectable. 104 tests, exhaustive tiny references, dependency-free Python, strict JSON CLI and two reproducible SVGs. Supplied model assumptions, not online event detection or real-data calibration.

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

Hidden Markov models from scratch: log-space inference, Viterbi paths and multi-sequence Baum-Welch, now with prefix-only filtering and multi-step symbol/state forecasts. An exact example separates x-only filtering P(A)=2/3 from future-informed x/y smoothing P(A)=0. Forecasts are dependent horizon marginals, not a joint path. Prefix predictive log scores match full likelihood to about 5.68e-14 on the seed23 development fixture; that is an implementation audit, not a new quality gain. Existing test NLL per symbol: trained0.775631, iid control0.985993, initialization1.017638, generating reference0.771674. Exhaustive references, impossible-prefix rejection, 41 Python tests, four Node/actual-Chrome tests and offline CLI/SVG demo. No calibration or state-recovery claim.

Live v0.2 [prefix-evidence inspector](https://midya8.github.io/chainlab/) keeps all three original models and both exact counterexamples fixed. Edit a bounded observation window and compare each own-prefix filtered row, full-window smoothed row, supported Viterbi path and prefix-only future marginals. Original 40-symbol reports and scores remain unchanged; the first three displays show only the first 12 symbols. Independent scaled browser versus native log inference checks cover 114 symbol edits and 40 prefix boundaries, plus 62 exhaustive high-precision controls. Underflowed browser mass refuses instead of inventing a posterior. 41 Python tests, four Node/actual-Chrome tests and installed eight-module/nine-command reproduction. No new training, state accuracy, calibration or causal claim. [Conditioning and numerical limits](https://github.com/midya8/chainlab/blob/main/EVIDENCE.md).

- Distinct full-sequence posterior, best-path and prefix-filtering objectives. Marginal modes can form a forbidden path; smoothed states can use future observations.
- Forecast horizon1 transitions before emitting; later horizons do not assimilate guessed observations. Log messages preserve paths whose raw probabilities underflow. Exact future-path and prefix references check both behaviors.
- Unsmoothed EM preserves sequence boundaries, reports zero occupancy and accepts only nondecreasing likelihood updates. The inspected persistent-regime fixture is not an external benchmark, causal decomposition or general model ranking.

- Repo: [midya8/chainlab](https://github.com/midya8/chainlab) · Case study: [projects/chainlab.md](projects/chainlab.md)

### KernelLab

Gaussian-process regression and finite-grid expected-improvement suggestions from scratch. Cholesky solves, separate latent/observation covariance, explicit jitter, marginal likelihood and fixed-parameter LOO. Deterministic EI excludes known rows and returns a full candidate audit, without executing evaluations. A nine-evaluation toy optimization comparison reports grid regret 0.000163 (EI), 0.072944 (space filling) and 0.399473 (one seeded random control). Same pool/initialization/budget; development data, no general ranking or continuous optimum claim. The regression misspecification counterexample remains visible. Dependency-free Python, 43 Python tests, four Node/Chrome tests, offline CLI and reproducible SVGs.

Live v0.2 [target-response inspector](https://midya8.github.io/kernellab/) keeps both original GP models fixed. Edit one observed target and inspect all 15 signed response weights: the conditional mean moves, while latent/observation variances stay unchanged. Independent browser LDL versus native Cholesky checks cover 202 query witnesses and 3,030 direct edited-target predictions, plus high-precision tiny controls and shared-axis endpoint checks. Original misspecification results and optimization traces are unchanged. Signed weights are not causal attribution or calibrated confidence; refitting invalidates the fixed-kernel contrast. 43 Python tests, four Node/actual-Chrome tests and installed eight-module/seven-command reproduction. [Derivation and numerical limits](https://github.com/midya8/kernellab/blob/main/RESPONSE.md).

- The fixed-kernel regression fixture also shows a confidently wrong long-length-scale arm. Model-based pointwise bands are not calibrated coverage guarantees.
- Exact deterministic-maximization EI, zero-variance positive-part limit, stable Gaussian tails and numerical-integration reference checks. Rejects noisy models and duplicate candidates; all-known pools return no false next suggestion.
- Same 81-point pool, 3 initial points and 6 more evaluations per optimization policy. Full evaluated-target traces, report-only oracle and adverse/misspecification evidence. No objective execution by the suggest API.

- Repo: [midya8/kernellab](https://github.com/midya8/kernellab) · Case study: [projects/kernellab.md](projects/kernellab.md)

### BoostLab

Binary gradient boosting from scratch: mean-residual defaults plus optional capped, L2-regularized Newton leaves on residual-SSE trees. The development fixture selects 35 Newton trees/237 nodes, test accuracy 0.9004/logloss 0.3341; its unselected 80-round checkpoint is also shown (0.8984/0.3469). Mean depth-2 control: 0.8906/0.3400; full-budget stumps: 0.6367/0.7366. Different capacity and settings, no causal or external-benchmark claim. Backward-compatible v1/v2 inference, Hessian/leaf arithmetic tests, validation-only prefix selection. Dependency-free Python, 36 Python tests and five Node/Chrome tests and offline CI.

- Seed-7 noisy sign-of-product fixture, 256/128/512 train/validation/test rows. Newton depth-2 uses L2=1, leaf cap 3; validation selects 35 trees, not the last 80-round checkpoint. All fitted controls remain visible in the case study.
- Mean depth-2 and depth-1 controls retain the original settings and results. Validation selects the depth-1 zero-tree prefix (0.4980/0.7060). Same round budgets are not equal capacity.
- Newton refines only leaves, using residual-SSE splits rather than Hessian gains. History records cap and zero-denominator diagnostics. V1 mean artifacts still predict unchanged; new Newton artifacts use v2.
- Dependency-free Python 3.10+, 36 Python tests and five Node/Chrome tests, offline CLI demo and CI. Standard boosting sources credited. No line search, new-method, calibration or production-performance claim.

- Repo: [midya8/boostlab](https://github.com/midya8/boostlab) · Case study: [projects/boostlab.md](projects/boostlab.md)


Live v0.2 inspector retains all 80 fitted trees and 81 prefixes for each original arm, including the selected zero-tree stump. Editable inputs expose complete additive-logit/tree-route witnesses, original selected-versus-last checkpoints and shared zero-based loss curves. No new tuning, attribution, calibration or performance claim. All original development-fixture metrics and limits above are unchanged. Independent native/browser checks cover 4,860 original and 1,458 edited prefix states, 78 complete paths and all 243 metric states. 36 Python tests, five Node/actual-Chrome tests, installed seven-module/five-command reproduction. [Try the training path](https://midya8.github.io/boostlab/) · [Derivation and numerical limits](https://github.com/midya8/boostlab/blob/main/PATH.md).

### ShapleyLab

Exact small-feature Shapley attribution from scratch: empirical-background replacement, every coalition available for audit, scalar score callback API and strict JSON CLI.

- For a product prediction of 6, zero background gives [3, 3, 0] but a shifted background gives [2, 3, 0]. Reference choice changes the question, not the model prediction.
- Jointly sampled missing features preserve their mutual dependence. A diagonal-background counterexample has off-manifold singleton hybrids despite zero attribution/efficiency residual: additivity does not certify explanation validity.
- Enumerates all coalitions with a preflight call budget; 3 features/2 background rows require 15 calls. Independent factorial-order reference checks dimensions 1-6, plus linearity, symmetry, dummy and feature-permutation tests. No walltime, causality, conditional-SHAP or model-quality claim.
- Optional atomic groups move correlated blocks together. Three-way product gives grouped [1/2, 1/2], not post-hoc [2/3, 1/3]; grouped games answer a different question. Up to 64 raw features/12 groups, no within-group credit split or cross-group dependence guarantee.
- Optional seeded permutation mode handles up to 64 individual features with cached coalitions and descriptive MC standard errors. A two-permutation product gives [0.5, 0.5, 0] despite exact [1/3, 1/3, 1/3], showing zero observed MC error is not an accuracy bound. No confidence guarantee or sampled groups.
- Dependency-free Python 3.10+, 49 Python and four Node/actual-Chrome tests, offline demo and CI. Standard Shapley/SHAP formula and masking sources attributed; no new algorithm claim.

- Repo: [midya8/shapleylab](https://github.com/midya8/shapleylab) · Case study: [projects/shapleylab.md](projects/shapleylab.md)
- v0.2 [live coalition ledger](https://midya8.github.io/shapleylab/): actual native callback rows, weighted predecessor terms, cached full ordering paths and independent point-edit browser. 49 Python + four Node/Chrome tests; 95 edit witnesses, 128 Fraction and 64 BigInt controls. Original exact/grouped/sample reports unchanged. Finite replacement allocations, not causal importance or explanation quality.

### PolicyLens

Offline contextual-bandit evaluation from scratch: IPS, self-normalized IPS, direct method and doubly robust value estimates with full behavior/target probabilities, reward predictions and support/weight diagnostics.

- In a constructed 20-row balanced design, target truth 0.78 is recovered by IPS/SNIPS/DR despite a wrong constant reward model (direct 0.50). This is an arithmetic fixture, not a random-trial accuracy claim.
- Capping weights at 1 raises ESS 4.9231 to 8.4706 but moves IPS to 0.185 and DR to 0.535. A separate noisy 2000-row log uses an oracle reward model yet DR 0.7532 differs from truth 0.78. No universal-best-estimator claim.
- Optional held-out categorical reward fitting excludes each full fold, reports cell counts and prior-only predictions. On the same noisy log, five-fold DR 0.7509088 is not closer to truth than oracle DR 0.7532475; no estimator ranking. Row-iid splits do not protect clustered/time data.
- Flags unsupported target actions rather than treating reward-model extrapolation as identified policy value. Explicit propensity/support/context and independent/cross-fitted reward-prediction assumptions; no deployment decision or confidence guarantee.
- Dependency-free Python 3.10+, 28 tests, JSON CLI/API and offline CI on Python 3.10-3.13. Standard estimators attributed to their sources, no new theory.

- v0.2 [live row ledger](https://midya8.github.io/policylens/): independent browser evaluator, all signed row contributions/cap removals, five support controls, target/reward edits and fixed-prediction deletion reports. 36 Python + four Node/Chrome tests, 95 edits, 160 Fraction and 80 integer-grid controls; original four reports unchanged. Cap paths and ESS are descriptive, not confidence, tuning or deployment advice.

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
- Dependency-free Python 3.10+, 41 Python tests plus four Node/Chrome tests, CLI/API fit/predict/evaluate, per-class and size diagnostics, offline demo and Python 3.10-3.13 CI. Optional classwise thresholds with explicit rare/absent-class inclusion. Standard method attributed to Angelopoulos and Bates.
- v0.2 [live rank ledger](https://midya8.github.io/setguard/): five synthetic controls expose every threshold tie, pooled/classwise label decision and held-position rank check, with a 19-point alpha path and native-compatible JSON. Independent Python/BigInt-browser arithmetic; 95 witnesses, 41 Python/four Chrome tests and installed six-command wheel reproduction. Original three empirical arms unchanged. Rank counts are not an exchangeability test or fixed-candidate guarantee.

- Repo: [midya8/setguard](https://github.com/midya8/setguard) · Case study: [projects/setguard.md](projects/setguard.md)

### CalibrLab

Confidence calibration from scratch in pure Python, with a JSON CLI/API for caller-supplied validation/test logits, unclipped logit-space NLL and optional conditional paired test-row bootstrap intervals: ECE/MCE/Brier/NLL metrics, per-bin reliability tables, and temperature scaling fit on validation NLL only.

- **Measured calibration repair** - an overfit small-data MLP (train 1.0000, test 0.5563; top bin 0.9735 mean confidence at 0.6602 accuracy) goes from ECE 0.2765 to 0.0651 and test NLL 2.0030 to 1.2060 with one validation-fitted temperature (T = 3.85) - at exactly zero accuracy change, a property of the method asserted bit-for-bit in the gates.
- **Honest bounds, not just wins** - the test-optimal (oracle) temperature 3.30 would give NLL 1.1984, so the validation fit leaves only 0.0076 on the table; post-scaling bins skew mildly under-confident and MCE stays noisy (0.1216), both reported.
- **Gradients by hand, verified** - the MLP's backprop is derived in code and finite-difference checked; the suite separates metric unit tests from fixture regression.
- Dependency-free Python 3.10+, 56 Python tests plus four Node/Chrome tests, a fully offline demo asserting both gate sides, and CI across Python 3.10-3.13.

- Repo: [midya8/calibrlab](https://github.com/midya8/calibrlab) · Case study: [projects/calibrlab.md](projects/calibrlab.md)
- v0.2 [live score ledger](https://midya8.github.io/calibrlab/): independent native/browser arithmetic, all row logit NLL/class Brier terms, signed bin gaps/ECE terms, migration and fixed-temperature deletion; five public controls, 19 sampled temperatures and complete input/report JSON. 95 witnesses, 160 Decimal/80 integer games and installed original-training/wheel reproduction. Original adverse caller and all results retained. Binned ECE is not classwise calibration, proper losses are not calibration-only and deletion is not refitting/uncertainty. Full-precision oracle gap rounds to .0075; prior .0076 subtracts rounded NLLs.

### DistillLab

Knowledge distillation built from scratch in pure Python: a teacher trained on abundant data, a 10x smaller student trained on a tenth of the data, and the measured gain compared against matched control arms.

- **Measured against matched controls** - +0.0656 test accuracy over direct training at identical capacity and budget (0.7469 vs 0.6813; teacher 0.8344): pseudo-labels on the teacher's argmax exceed direct by +0.0281 and soft-label distillation exceeds pseudo-labels by +0.0375, uniform label smoothing at eps=0.1 adds nothing, and a permuted-target control sits at exactly chance (0.1250) - measured between-arm differences on this fixture, not causal attribution.
- **Smaller measured train-test gap** - the direct student memorizes its 80 training samples (train 1.0000, train-test gap 0.3187); the distilled student does not (train 0.8000, gap 0.0531) and sits closer to the teacher in KL (0.9563 vs 1.0932).
- **Gradients by hand, verified** - the temperature-scaled combined loss alpha*T^2*CE(softmax(z/T), soft) + (1-a)*CE(softmax(z), y) with its exact logit gradient, finite-difference checked; the T=1 ablation pinned (0.7219 vs 0.7469 at T=4).
- Dependency-free Python 3.10+, 24 Python tests plus four Node/Chrome tests, a fully offline demo asserting both gate sides, and CI across Python 3.10-3.13.

- Repo: [midya8/distilllab](https://github.com/midya8/distilllab) · Case study: [projects/distilllab.md](projects/distilllab.md)

- v0.2 [live gradient inspector](https://midya8.github.io/distilllab/): one real 254-parameter update from any original student model and training row, with signed hard/soft derivatives, CE/entropy/KL, all parameter changes and all 400 original split predictions. A separate small control visibly overshoots despite a negative local derivative. Independent native/browser witnesses, 160 Decimal and 80 uniform controls, all-parameter finite differences and installed original-training/wheel reproduction retain original results. Stable unclipped inspector losses are explicitly distinct from the old probability-floor helpers. One step is not a training run or causal/deployment guarantee.

### MoeLab

Mixture-of-experts from scratch, now with an [interactive route-boundary inspector](https://midya8.github.io/moelab/). Independent Python Fraction and browser BigInt arithmetic find exact affine cells and point ties, with retained-probability outputs, one-sided limits, jumps, zero-jump transitions, triple-tie point values and fixed-branch derivatives. Actual rounded inference remains separate from mathematical geometry.

- Original aux/no-aux training, initialization, dense baseline and all 340 data rows retained. Measured aux MSE 0.0303 vs dense 0.1853 (136 vs 145 parameters), purity 1.0000 and equal usage shares are descriptive fixture results, not causal/generalization claims. Soft MSE remains 0.6291. No-aux MSE is 0.0014970307791088836 (0.0015), correcting stale 0.0010 prose without retraining changes.
- Three balance conventions are reported separately. Uniform ties give penalty one yet send every row to expert 0. Eight arithmetic controls and strict JSON exports expose limits instead of treating a low penalty as a traffic guarantee.
- 39 Python tests and five substantive Node/actual-Chrome tests, 32 full witnesses, 80 integer geometries, 160 independent Decimal controls and installed-wheel reproduction. Full retraining uses documented 1e-11 runtime/libm tolerance; frozen rational geometry is checked exactly. No transformer, token capacity, measured serving speed or robustness certificate.

[Source](https://github.com/midya8/moelab) · [Case study](projects/moelab.md)

### AlignLab

Finite-policy Gibbs optimum and KL-budget inspector attached to a dependency-free Bradley-Terry preference experiment. Independent native/browser implementations separate optimization error from reward quality: the original noise-control policy is essentially reward-optimal and still loses synthetic utility.

- Retains all original data, reward fits, original three trajectories and 15 original tests. Two additional stiff-KL controls keep their large-step failure visible; all 1,005 states remain available.
- Shows the standard objective-gap identity, reference-weighted tied maxima, finite-support restrictions and a bracketed KL frontier. Tiny budgets and unresolved near ties are explicit, not false optimum claims. Utilities are evaluation-only.
- Corrects stale published numbers without changing training: utility 2.0375 to 4.5704247, noise control 1.8548647, KL 1.0750099. The full old/current table remains in the source.
- 47 Python tests across 3.10-3.13, four substantive Node/actual-Chrome tests, 35 full report witnesses, independent Decimal controls and complete installed-wheel reconstruction. Finite synthetic arithmetic, not a new alignment method, causal result or safety/generalization certificate.

- Repo: [midya8/alignlab](https://github.com/midya8/alignlab) · [Live inspector](https://midya8.github.io/alignlab/) · Case study: [projects/alignlab.md](projects/alignlab.md)


### LoRALab

Same model, different factor-SGD step. A dependency-free Python implementation and independent browser inspector expose equivalent low-rank factor coordinates, full gradients and the finite-step second-order identity. Scalar learning-rate compensation is an attributed coordinate identity, not a new optimizer.

- All 124 original epoch boundaries across widths 1/2/4/8 remain available, with full matrix-gauge input, 31-scale sweeps, per-example outputs and complete report/input/archive exports. No best-state selection or retraining from the controls.
- The unchanged width-2 result reaches B accuracy 1.0000 with 67.7% of full fine-tuning's parameters, but retains less A accuracy: 0.7556 versus 0.9556. Widths 4/8 cost more parameters than full fine-tuning; three output rows cap update-matrix rank at three.
- 31 Python tests, four Node/actual-Chrome tests, 54 complete native/browser witnesses with 591,615 numeric values, independent finite-difference/80-digit checks and isolated installed-wheel reproduction. All 14 original tests and gates remain intact.
- Synthetic finite classifier only. Orthogonal changes preserve ordinary SGD in real arithmetic; general scaling/shear need not. Binary64 residuals are diagnostics, not certificates or generalization evidence.

- [Interactive inspector](https://midya8.github.io/loralab/) · Repo: [midya8/loralab](https://github.com/midya8/loralab) · Case study: [projects/loralab.md](projects/loralab.md)

### SpecLab

Speculative decoding from scratch: greedy n-gram verification, exact stochastic
residual correction, and a finite **oracle lookahead planner** that includes
no speculation as a genuine action.

- **Choose lengths without weakening baselines** - exact Bellman values for every prefix/action, transitions and slacks, plus all fixed lengths including target-only. The switching fixture costs `23/10` assigned units versus best fixed `47/20`; score-position prices choose no drafting everywhere.
- **Full probability and count laws** - policy output law remains exactly the target law. Planning/lookup overhead and target-table access are not free in reality; they are explicitly outside this tiny oracle model, with no GPU or measured-latency claim.
- **Independent verification** - 47 tests include all 12 tiny policies on 25 pairs under three objectives, 72 prefix-dependent joint-law checks, 36 planner configurations, and the preserved stochastic checks over 2,187 prefix-table pairs and every procedural RNG ticket for 25 binary pairs.
- **Preserved original controls** - wrong target fallback has TV `141/1024`; original greedy fixture still uses 122 vs 480 modeled rounds and 510 vs 480 actual scoring calls. Supplied stochastic tables only, vocabulary 1..3, horizon 1..4, no EOS/real LLM benchmark.
- Dependency-free Python 3.10+, full saved Bellman/probability witnesses, 115-cell and 96-cell test-bound figures, five-job CI and seven-mode installed 12-module wheel parity. Prior adaptive-lookahead work is attributed; no novelty claim.

- Repo: [midya8/speclab](https://github.com/midya8/speclab) · Case study: [projects/speclab.md](projects/speclab.md)

### StructGate

Full-model constrained decoding with support-aware KL and exact finite-language conditioning. The independent browser evaluates every original n-gram count, all 120 historical paths/3,729 emitted characters and all 46 character probabilities at every step. Fifty-four Python tests retain all 32 originals; three Node/actual-Chrome tests compare 1,251 full prefix reports, 289 source contexts and 741,236 numeric entries. Fraction/BigInt controls expose local-versus-global distortion, stranded probability and undefined zero events. Original 3/40, 40/40, 40/40 fixture and gates retained. Prefix legality is not finite-budget completion; the historical fixed record is not JSON Schema. No LLM-quality, causal mask-cost or arbitrary-JSON conditioning claim. [Live mask and conditioning inspector](https://midya8.github.io/structgate/) · [Equations, support and limits](https://github.com/midya8/structgate/blob/main/CONDITIONING.md). Case study: [projects/structgate.md](projects/structgate.md).


### QuantLab

Real QLB1 int8 files, IEEE32/64 scales and an independent editable browser inspector: every coefficient, signed logit-error contribution and exact fixed-input margin. Original 60-example fixture and magnitude controls preserved; 39 Python tests and four Node/actual-Chrome tests compare 52 full reports. Actual row files are 232/244 B, not the original 204 B analytic payload. No integer-kernel or speed claim.

Original source and all four storage choices retain 59/60 synthetic test accuracy. Original small-row SNR difference remains +39.14 dB. Fraction/BigInt rational witnesses concern the fixed represented-real map, not floating accumulation or unseen performance.

- Live inspector: [QuantLab](https://midya8.github.io/quantlab/)
- Repo: [midya8/quantlab](https://github.com/midya8/quantlab) · Case study: [projects/quantlab.md](projects/quantlab.md)

### RAGLine

Retrieval-augmented answering built from scratch in pure Python: a deterministic templated corpus chunked with stable ids, token-hashed sparse TF-IDF embeddings, top-k cosine retrieval, extractive answers that always cite their source chunk, and a lexical-overlap grounding check scored against each answer's cited chunk - shown in a tested negative control to flag a corrupted citation.

- **The RAG loop as inspectable steps** - corpus, embed, retrieve, answer, verify, each dependency-free and deterministic from one seed.
- **Grounding as a gate, not a slogan** - the check scores token overlap between answer and cited chunk; `--require-grounded` and `--min-grounded` fail CI when overlap drops, and the suite's negative control shows a corrupted citation is flagged. Lexical scope: tested wrong-citation cases, not arbitrary misinterpretation.
- **Measured retrieval quality** - fixture evaluation over questions with known topics: recall@3 = 1.00, MRR = 0.94, grounded rate = 1.00, pinned in CI.
- Dependency-free Python 3.10+, 31 unit tests, a fully offline demo asserting both gate sides, and CI across Python 3.10-3.13.

- Repo: [midya8/ragline](https://github.com/midya8/ragline) · Case study: [projects/ragline.md](projects/ragline.md)

### KVLens

Independent full-tensor attention/cache inspector with final-query-only no-cache and optimized-prefill controls, atomic occupied-prefill rejection and independent cache forks. Named default eight-prediction savings: 58.68% against the stronger baseline versus 73.08% for the intact historical pair. Complete Q/K/V, score/value/output/logit contributions, before/after state and full JSON/model exports. 55 Python tests retain all 28 originals; three Node/actual-Chrome tests compare 32 complete reports, 97 predictions and 66,940 numeric entries, with every displayed cell and weight table checked. Counted arithmetic and ideal packed K/V payload, not latency or actual memory.

Original positive-budget outputs, full curve and CI gates stay intact. The final emitted token remains uncached; zero predictions do no forward work. Mutable weights must stay fixed and guards are not a security boundary. Native/browser agreement is tolerance-tested, not a universal bitwise claim.

- Live inspector: [KVLens](https://midya8.github.io/kvlens/)
- Repo: [midya8/kvlens](https://github.com/midya8/kvlens) · Case study: [projects/kvlens.md](projects/kvlens.md)

### AttnLens

A real manually differentiated attention trainer with a fixed-weight intervention workbench. Independent JavaScript recomputes all downstream tensors after head-output ablations, exposes all 16 head subsets on the original 128-example held-out split, and tests matched key/filler changes. Complete trained and same-seed initialization checkpoints, all source weights and full audit exports. Repairs a clipped-loss/nonzero-gradient mismatch with stable log-sum-exp. 59 Python tests retain all 46 originals; three Node/actual-Chrome tests compare 352 full tensor reports and 22 audits, with 704 displayed head-row views. One seed and synthetic task, zero-ablation distribution shift and nonadditivity visible; no attention-as-explanation or discovered-circuit claim.

- Live workbench: [AttnLens](https://midya8.github.io/attnlens/)
- Repo: [midya8/attnlens](https://github.com/midya8/attnlens) · Case study: [projects/attnlens.md](projects/attnlens.md)

### EmbedKit

Independent editable SGNS objective and gradient inspector: every sampled event, 1,593 coordinate finite differences, real sequential replay versus a frozen simultaneous step, and visible clamp/order effects. Twelve original pairs capture 72 actual calls; seven labeled controls expose repetition, conflicting labels, saturation and overshoot. Full 300-sentence corpus and all 32 trained vectors retained; browser recomputes all 992 cosine neighbors. 53 Python tests and four Node/actual-Chrome tests compare 19 complete reports. Original 40 tests, trainer and gates remain unchanged.

- Live inspector: [EmbedKit](https://midya8.github.io/embedkit/)
- Repo: [midya8/embedkit](https://github.com/midya8/embedkit) · Case study: [projects/embedkit.md](projects/embedkit.md)

### PlanBench

Validate and simulate agent task plans before they run: plans are DAGs of tool calls, checked for unknown tools, unknown or cyclic dependencies and inputs no dependency produces, then executed in a deterministic parallel simulation where flaky tools fail under a seeded RNG, steps retry within policy and dependents of failures are skipped - with makespan, cost, critical path and parallelism reported and gated in CI.

- **Semantic validation, not just syntax** - duplicate step ids, unknown tools, unknown/self/cyclic dependencies, and `requires` inputs no dependency's tool produces, each as a severity-ranked finding.
- **Deterministic parallel simulation** - steps start as dependencies succeed; tool failures come from a seeded RNG, so the same plan, registry and seed always produce the same trace, retries and skip cascades included.
- **Plan-shape metrics and gates** - makespan, total cost with retries, critical path by duration, parallelism; `--require-success`, `--max-makespan`, `--max-cost`, `--max-findings` fail the pipeline when a plan stops meeting policy.
- Dependency-free Python 3.10+, 29 unit tests, a fully offline demo with a flaky-tool research plan and a rejected broken plan, and CI across Python 3.10-3.13.

- Repo: [midya8/planbench](https://github.com/midya8/planbench) · Case study: [projects/planbench.md](projects/planbench.md)

### DecodeLab

Inspectable sampling and search from scratch, with every finite future accounted for. Stable temperature scaling, normalized top-k/top-p and retained-mass witnesses fix the earlier unnormalized nucleus cutoff and direct-power underflow. Short n-gram contexts now match training's start padding.

- Complete bounded trees separate EOS termination from cap censoring, filtered sampling mass from original-model log scores, and conditioned prompts from generated text.
- Full beam expansion/pruning witnesses and exhaustive same-objective oracles show a lost better future at width 1 and a width 2-worse-than-width 1/3 counterexample under the documented shared finished/live beam. Higher likelihood is not a writing-quality verdict.
- Editable independent scalar-JavaScript inspector: change all transition weights and decoding controls, paginate every outcome, follow candidate steps and export the complete current audit. Stale results disappear on edit.
- 54 Python tests, including all 36 original tests unchanged; 90-digit Decimal sampling and rational Cartesian/forward-DP references; 32 retained audits, 120 stage cases, 7,927 independent numerical checks. Actual Chrome covers 96 distribution views, 231 outcome rows, 956 candidate rows, export/invalidation and 320/390/1280 layouts. Installed wheel outside checkout and Python 3.10-3.13 CI.
- Original n-gram CLI, corpus/demo and diversity reports remain. Synthetic finite arithmetic/search audits, not a neural model, language-quality benchmark or new decoding algorithm. Explicit float/cutoff, exponential-tree and beam-semantics limits, with six prior sources.

- [Live inspector](https://midya8.github.io/decodelab/) · Repo: [midya8/decodelab](https://github.com/midya8/decodelab) · Case study: [projects/decodelab.md](projects/decodelab.md)

### VectorLite

A finite random-hyperplane geometry and retrieval audit: inspect every dot product, signature bit, candidate, canonical exact neighbor and threshold. Independent scalar JavaScript replays editable actual planes; no invented 2D projection for higher-dimensional data. Stable cosine avoids extreme-magnitude square overflow/underflow. Full-precision recall gates and explicit self-inclusive, leave-one-id-out and external-supplied protocols retain the original 12-vector recall@3 of 1.0; a same-two-vector id-exclusion control gives 1 versus 0.

- Complete marginal binomial admission reference, expected candidate count and expected canonical recall over iid-isotropic rebuilds, not a conditional guarantee for these fixed planes; zero-vector angular theory stays undefined.
- Fifty Python tests include all 31 original tests unchanged. Independent Decimal/rational/sign-pattern/geometry controls, 35 audits, 20,784 JavaScript numerical checks, 643 threshold rows and actual Chrome inspection of 5,856 projection rows. Installed-wheel CLI reproduction outside checkout.
- Linear all-signature scan, not sublinear lookup. Rescored fractions are not latency; synthetic vectors are not learned embeddings or relevance quality. No new algorithm, speed, confidence-interval or model-quality claim.

- Repo: [midya8/vectorlite](https://github.com/midya8/vectorlite) · [Live inspector](https://midya8.github.io/vectorlite/) · Case study: [projects/vectorlite.md](projects/vectorlite.md)

### GroundCheck

Complete lexical/citation/numeric provenance with independent scalar-JavaScript recomputation, editable source policies and full input offsets. 66 Python tests retain 43 originals; 50 synthetic controls expose semantic false positives. Four Node/Chrome checks and isolated-wheel reproduction. Lexical support is not entailment; audit parity is bounded ASCII.

- Repo: [midya8/groundcheck](https://github.com/midya8/groundcheck) · [Live provenance inspector](https://midya8.github.io/groundcheck/) · [Evidence contract](https://github.com/midya8/groundcheck/blob/main/EVIDENCE.md) · Case study: [projects/groundcheck.md](projects/groundcheck.md)

### TokenForge

Byte-level BPE tokenizers trained from scratch: deterministic merge training with exact pair counts over GPT-2-style pre-tokenization boundaries, rank-ordered encoding with exact round trips, JSON vocab persistence, and compression statistics with JSON/Markdown reports and a CI quality gate.

- **The tokenizer as an inspectable artifact** - exact pair counting, deterministic tie-breaking and plain-JSON merge storage mean a tokenizer can be diffed, reviewed and rebuilt byte for byte.
- **Byte-level coverage with boundary discipline** - the 256 byte values are the base vocabulary, so any text encodes and decodes exactly, while merges never cross word, number, symbol or whitespace boundaries.
- **Compression as a gate** - bytes-per-token and token-frequency statistics in terminal, JSON and Markdown form, with `--min-compression` failing CI when a tokenizer regresses.
- Dependency-free Python 3.10+, 40 unit tests, a fully offline demo that trains a 300-token vocabulary and asserts round trips and both sides of the gate, and CI across Python 3.10-3.13.

- Repo: [midya8/tokenforge](https://github.com/midya8/tokenforge) · Case study: [projects/tokenforge.md](projects/tokenforge.md)

### RetrievalBench

Complete BM25 arithmetic, explicit chunk parents, both parent budgets and per-rank metric gains with independent browser recomputation. 68 Python tests retain all 42 originals; 35 full reports, three Node/Chrome tests and installed-wheel reproduction. Synthetic arithmetic controls, not search-quality evidence.

Every term contribution, full unit/parent text, collapse decision, grade/discount and ideal denominator stays visible. The default CLI still takes k units then collapses; the alternative scans to k distinct parents on the same ranking. Whole/chunk indexing changes corpus statistics. Original corpus/demo/results stay visible; no Lucene equivalence or general quality claim.

- [Live inspector](https://midya8.github.io/retrievalbench/) · Repo: [midya8/retrievalbench](https://github.com/midya8/retrievalbench) · Case study: [projects/retrievalbench.md](projects/retrievalbench.md)

### EvalForge

Local-first LLM/agent evaluation plus an [editable paired comparison inspector](https://midya8.github.io/evalforge/). Recomputed all-task versus matched-task means reveal cohort reversal; every per-task gate decision and full normalized result record stays visible. Exhaustive paired sign flips and exact McNemar expose all assignments/counts without changing the original regression gate. Independent scalar JavaScript, responsive fixed-axis chart and current JSON export.

Original offline command-adapter/scorer/HTML/JUnit/Markdown/SARIF harness, all 68 tests and the six-task mock are retained. 92 Python tests across 3.10-3.13; 24 full reports (11,808 numeric and 2,691 other scalar leaves); actual Chrome pair/record/assignment/binomial/dot/export checks; isolated installed wheel with nine module origins. This is supplied evidence arithmetic, not rescoring or proof of model quality. Equal ids do not establish matching task definitions or independent samples. Persistent failures can pass a comparison; a comparison PASS is not a passing suite.

- Repo: [midya8/evalforge](https://github.com/midya8/evalforge)
- Case study: [projects/evalforge.md](projects/evalforge.md)

### AgentTrace

Local-first validation, analysis and reporting for AI agent execution traces: JSONL trace structure checks, run summaries, tool/LLM call counts, latency and cost rollups, graph depth, repeated-step loop detection, baseline/candidate regression comparison, quality gates, a standalone escaped HTML timeline, deterministic JUnit XML output for CI test viewers, Markdown job summaries, and SARIF 2.1.0 output for code-scanning integrations.

- **Agent runs as inspectable data** - parse JSONL traces from local agents, test fixtures, internal tools or hosted-model adapters without sending prompts or outputs anywhere.
- **Gates that catch agent failure modes** - fail CI on errored steps, p95 latency, cost, step count, a repeated tool/action signature that indicates a loop, or regressions against a saved baseline trace.
- **Reports built for review** - deterministic JSON analysis artifacts, JUnit XML for CI test viewers, Markdown job summaries, SARIF 2.1.0 for code-scanning tools, and a self-contained HTML report show run summaries and per-step timelines with untrusted trace fields escaped by default.
- Dependency-free Python 3.10+, 57 unit tests (original 33 retained), a fully offline fixed-trace baseline/candidate demo that validates JUnit, Markdown and SARIF output, and CI across Python 3.10-3.13.

- Repo: [midya8/agenttrace](https://github.com/midya8/agenttrace)
- Case study: [projects/agenttrace.md](projects/agenttrace.md)

Full-record graph/timing inspector: every endpoint, interval segment, parent path/relation, normalized record and p95 term. Independent Python/JavaScript recomputation and current JSON export. 57 Python tests retain all original 33 tests; 24 synthetic controls, 11,110 interval checks and an isolated installed-wheel reproduction. Parent links are not causal dependencies; recorded coverage/overlap is not CPU, idle, waste or utilization. No model/API call.

- [Live graph/timing inspector](https://midya8.github.io/agenttrace/)

### PromptGuard

Local-first prompt linting with a full-stage baseline and CI-gate witness. Native fixes redact before truncation, retain all recognized sensitive matches per line and fail incomplete scans. An [independent policy inspector](https://midya8.github.io/promptguard/) recomputes every abstract finding through filter, suppression and gate stages with complete JSON export.

- 87 Python tests on 3.10-3.13 preserve all original 68 tests, fixtures and offline demo; 13,320 exhaustive small policy controls.
- 27 complete independent reports, actual Chrome checks of 50 current rows, 17 prior rows and 181 stage circles, plus isolated installed-wheel reproduction across eight module origins.
- Existing scanner/report formats remain. Fingerprint aliases and metadata-identity migration are explicit; real baselines and witnesses must stay private. No new detection patterns or security-effectiveness claim.

- Repo: [midya8/promptguard](https://github.com/midya8/promptguard)
- Case study: [projects/promptguard.md](projects/promptguard.md)

### ScratchGPT

A NumPy GPT with hand-written autograd and a real Shakespeare checkpoint, now with a validated exact-continuation contract. Both complete PCG64 states, Adam memory/clock, data identity, options and runtime metadata survive restart; terminal previews do not consume evaluation randomness.

- All 13 stop boundaries reach identical complete final state in the same environment. RNG-reset and missing-moment controls change weights at all 11 interior boundaries; evaluation-only reset changes future validation history, not weights.
- Independent scalar Adam checks 38,016 p/m/v values and independent transformer inference checks 2,592 logits. Actual Chrome inspects all 101,376 coordinate-table cells, 468 coordinate views, 72 inference views, editable contexts and two exports.
- 70 Python tests retain all 11 original tests; three Node/Chrome tests, four Python versions and isolated installed-wheel reproduction. Original model/autograd/optimizer/data, historical checkpoint, loss records and sample preserved.

The replay is a separate 1,056-parameter synthetic model. The browser recomputes arithmetic and forward inference, not gradients/training. No cross-machine determinism, text-quality, speed or novelty claim.

- Repo: [midya8/scratchgpt](https://github.com/midya8/scratchgpt) · [Live replay](https://midya8.github.io/scratchgpt/) · Case study: [projects/scratchgpt.md](projects/scratchgpt.md)

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


### CutLab response-path extension

[Open the exact response-path inspector](https://midya8.github.io/cutlab/path.html) · [Source and method](https://github.com/midya8/cutlab/blob/main/PATH.md)

Vary binary unary costs with a rational parameter and retain the complete optimum family on every closed region, open cell and breakpoint, including point-only optima and persistent ties. Every assignment keeps its affine line and every line comparison keeps its exact inequality. Independent graph-cut audits check all boundary and cell witnesses.

18 synthetic controls retain 214 assignment lines, 6,084 inequalities and 92 full flow/cut witnesses. Mixed-sign slopes include a label that leaves and returns: no nested-label or scalable parametric-maxflow guarantee is claimed. The inspector enumerates all 2^n assignments for at most six variables. Original flow/cut functionality and tests remain.


### Diagnoselab: all conflicts, all minimal repairs

[Exact logical consistency inspector](https://midya8.github.io/diagnoselab/) · [Source](https://github.com/midya8/diagnoselab)

Full relative MUS/MCS families, bidirectional minimal hitting-set intersections, per-member minimality/unique-hit witnesses and exact rational removal costs. Every soft subset retains its DPLL/unit trace and independent full truth-table models. The smallest repair need not be cheapest; an inconsistent fixed background has no soft repair.

18 original synthetic controls retain 827 subsets, 1,301 search nodes, 20 cores and 52 repairs. 17 Python tests on 3.10-3.13, four Node/Chrome tests, 74,292 exact cross-language scalar checks and installed-wheel reproduction. Exhaustive six-variable/eight-soft-clause bound, established SAT theory, no scalable solver, real fault diagnosis or certified proof claim. No model/API.

[Case study](https://github.com/midya8/Midya-portfolio/blob/main/projects/diagnoselab.md)


#### Diagnoselab repair-policy consequences

[Live query inspector](https://midya8.github.io/diagnoselab/consequences.html) · [Method/sources](https://github.com/midya8/diagnoselab/blob/main/CONSEQUENCES.md)

Distinguishes every/some repair from every/some surviving model, with all tied minimum-cost/cardinality policies, complete countermodels and negated-query DPLL traces. Shared-clause intersection is a separate baseline with strict counterexamples. No-repair families are inapplicable, not vacuous certainty. 26 new exact reports (16,165 scalar leaves), 67 repairs, 78 policy records and 151 full DPLL nodes including intersection baselines; 24 Python/eight Node-Chrome tests preserve all originals. Installed-wheel reproduction and mobile/table/export checks. Finite propositional reasoning, not a database/DL engine or probability claim.


## ArgumentLab: defense, not a vote

[Source](https://github.com/midya8/argumentlab) · [Live inspector](https://midya8.github.io/argumentlab/) · [Method and six sources](https://github.com/midya8/argumentlab/blob/main/METHOD.md) · [Case study](https://github.com/midya8/Midya-portfolio/blob/main/projects/argumentlab.md)

An exact bounded abstract-argumentation workbench. Compare all nine extension families, inspect every subset's attackers/defenders and unanswered attacks, all inclusion/range witnesses, complete three-valued labellings and the entire grounded fixed-point chain. Directed graph keeps opposite attacks and self loops visible. Acceptance retains witnesses and counterexamples, with a prominent classical skeptical-vacuity warning when no stable extension exists.

Original strict controls distinguish preferred from maximum cardinality, preferred intersection from grounded, a nonadmissible preferred intersection, and stage from semi-stable. Independent Python bitsets and JavaScript sets agree on all531 directed frameworks through three arguments/344,023 scalar leaves and19 retained full reports/152,884 leaves. Separate set/ternary oracles cover120 native and100 JavaScript seeded larger cases.19 native tests run on four Python versions; five Node/actual-Chrome tests check every retained UI record and graph state, export/invalid clearing and all19 controls at320/390/1280. Installed wheel reproduces19 full reports outside the checkout.

Eight arguments; exhaustive subsets; all ties retained. Established semantics, not a novel/scalable solver, probability model, benchmark win, real-world truth or debate winner. Six inspected sources and exact parser differences documented; no external solver code/data/examples copied or affiliation with existing ArguLab/ARGTEACH.


### ArgumentLab attack switches

[Live switch-cube inspector](https://midya8.github.io/argumentlab/switches.html) · [Source and method](https://github.com/midya8/argumentlab/blob/main/SWITCHES.md)

Enumerates every configuration of up to six supplied attack switches. Preserves all nearest ties, all inclusion-minimal matches, exact extension gains/losses and complete selected-framework defense witnesses. Original controls distinguish minimum cardinality from inclusion minimality and retain nonmonotone and nullable outcomes.

Verified on 21 controls, 209 configurations, 5,205 subset classifications and 423 switch transitions. Independent Python and JavaScript engines, installed CLIs, browser exports and responsive inspection. These are bounded hypothetical edits, not causal effects, persuasion advice or a scalable solver.


## ConceptLab: exact concepts and implication witnesses

[Live inspector](https://midya8.github.io/conceptlab/) | [Source](https://github.com/midya8/conceptlab) | [Method and prior work](https://github.com/midya8/conceptlab/blob/main/METHOD.md)

A bounded knowledge-representation workbench for formal concept analysis. Independent Python and JavaScript enumerate every formal concept, cover, meet/join, attribute closure and object derivation. Inspect canonical implications, pseudo-intent decisions, NextClosure pivots, forward rule traces and rule-removal countermodels. Every implication query retains supporting and counterexample rows; an empty premise extent means vacuous validity and null confidence, not evidence.

Fourteen original controls include duplicate rows, zero support, empty universes, strict joins, nonminimal pseudo-intents and multi-rule closure. The retained suite covers 194 attribute subsets, 390 object subsets, 69 concepts, 30 canonical rules, 635 ordered lattice operations and 5,762 implication queries. Independent set-based checks cover all 689 contexts with zero to three objects/attributes plus 100 seeded larger contexts per engine. Native CLI, installed wheel and actual-Chrome checks accompany the interactive inspector.

Finite exact teaching/audit tool: at most six attributes and eight objects. Not learned prediction, fuzzy concept analysis, noisy-data inference, causality or a scalable mining system. Existing FCA theory and software are attributed; no new algorithm is claimed.


### ConceptLab incomplete-context completions

[Live completion inspector](https://midya8.github.io/conceptlab/partial.html) | [Semantics and sources](https://github.com/midya8/conceptlab/blob/main/PARTIAL.md)

Unknown is not false. Enumerate every compatible binary completion of a three-valued table. Inspect certain, contingent and impossible implications, all object counterexamples, exact defined row-confidence bounds and endpoint ties, with zero-support completions kept separate. Intersect goals in one shared completion and retain every inclusion-minimal impossible goal set with deletion witnesses.

Original controls expose two traps: both extreme fill-ins can pass while an intermediate world refutes an implication, and separately possible goals can be jointly impossible. Overlapping-premise tautologies, empty universes, duplicate objects and all 64 worlds of six unknowns remain explicit. Twelve controls cover 86 completions, 438 implication queries, 4,634 query/completion witness rows and 63 goal subsets.

Independent Python and JavaScript engines, 17 native tests on four Python versions, six Node/Chrome tests and 26 installed-wheel reports preserve the complete-context workbench. Every retained UI record, export and invalid-input clearing is checked; all controls are layout-tested at 320/390/1280. Limits: four attributes, four objects, six unknown cells. Completion counts are not probabilities; confidence bounds describe supplied rows, not unseen data. No imputation, causal claim, graded possibility model, incomplete-context basis or new algorithm is claimed.


### STRIPSLab exact planning and relaxation witnesses

[Live inspector](https://midya8.github.io/stripslab/) · [Source](https://github.com/midya8/stripslab) · [Method and prior work](https://github.com/midya8/stripslab/blob/main/METHOD.md)

An original bounded classical-AI planning lab: audit every state and every blocked/applicable action, compare exact real and delete-relaxed shortest-plan families, and inspect h-max/h-add fixed-point rounds and tied fact achievers. Strict controls expose shared-effect double counting, relaxed solvability hiding real dead ends, restoration costs, all shortest-order ties and unreachable cyclic prerequisites. Python bitsets/reverse BFS and independent JavaScript sets/Bellman sweeps reproduce the same complete reports.

Six facts, eight grounded positive-precondition unit-cost actions. No PDDL parser, real-world execution, scalable-planner claim or new planning algorithm. Fourteen original synthetic tasks; eight Python tests, three Node/Chrome tests and isolated wheel reproduction of all fourteen full reports. Established STRIPS and heuristic-planning work is attributed with inspected-source limits.

[STRIPSLab case study](https://github.com/midya8/Midya-portfolio/blob/main/projects/stripslab.md)


### STRIPSLab search witnesses: an actual suboptimal h-add plan

[Inspect four complete search runs](https://midya8.github.io/stripslab/search.html) · [Search policy and reproducible evidence](https://github.com/midya8/stripslab/blob/main/SEARCH.md)

The new A*/best-first inspector exposes every selected frontier, strict cost improvement, applicable action decision and returned plan. A controlled task returns cost 3 with h-add versus exact cost 2 under the disclosed tie and goal-pop policy. Zero, h-max and exact h-plus return cost 2. Includes admissibility/consistency diagnostics, unsolvable exhaustion, strict CLI certificates, an independently implemented browser engine, and a separate synthetic reopening test. Full-state precomputation is explicit: this is a bounded audit, not a planner speedup or new algorithm claim.


### STRIPSLab availability: used does not mean necessary

[Live action-availability inspector](https://midya8.github.io/stripslab/sensitivity.html) | [Exact source and policy](https://github.com/midya8/stripslab/blob/main/SENSITIVITY.md)

Disable every static action subset. Keep every exact counterfactual distance, shortest-plan count, original action ID, representative and optimal edge. Separate an action used by one representative from one required by every optimal plan or every valid plan. Retain all inclusion-minimal sufficient sets and all solvability/optimality cuts, with independently checked minimal-hitting-set duals.

The original duplicate-shortcut control leaves a longer detour when both shortcuts are removed: optimality fails before solvability does. Eighteen controls retain 466 scenarios, 21,731 state rows and 408 optimal edges. Python BFS and independent JavaScript distance sweeps agree on 118 complete reports covering 2,515 scenarios; independent native set-transition and all-proper-subset oracles cover another 80 seeded tasks. Seventeen native tests, nine Node/Chrome tests and 47 isolated installed reports preserve all earlier modes. Browser checks every retained scenario at 320/390/1280.

Six facts/eight unit-cost grounded actions maximum. Static deterministic re-planning, not failure probabilities, timed outages, a scalable landmark extractor, real-world reliability or a new algorithm. [Implementation, boundaries and inspected sources](https://github.com/midya8/stripslab/blob/main/SENSITIVITY.md).


## UnifyLab: a binding is not a solution

[Live finite-term inspector](https://midya8.github.io/unifylab/) | [Source](https://github.com/midya8/unifylab) | [Method and inspected sources](https://github.com/midya8/unifylab/blob/main/METHOD.md)

An original bounded classical-AI unification lab. Keep every equation rewrite, composed earlier binding, exact constructor clash and zero-based occurs-check cycle path. A normalized simultaneous substitution is applied to every original equation. Alias reversal is not automatically a cycle, and a resource limit never means non-unifiability.

Independent Python and JavaScript engines reproduce 167 complete reports and 270 rewrites. A separate native certificate checker reconstructs local rules without calling the solver; a third lazy-environment oracle tests controls, 600 seeded systems and all 64 term-pool pairs. Seventeen controls retain 38 rewrites, including actual state/result expansion limits. Twelve native tests on Python 3.10-3.13, three Node/Chrome tests and seventeen isolated installed reports through two CLIs in solve/verify modes. Every retained browser step, equation, binding, witness, export and invalid edit is checked, with layouts at 320/390/1280.

Established finite-tree unification, not new theory. Six variables/eight equations, 96 input nodes, 4,096-node state/result budgets and 256 rewrites. No rational trees, higher-order/AC unification, resolution prover, linear-time or benchmark-win claim. Most-generality follows the established rewrite/solved-form theory; bounded ground-factorization tests are not a universal proof. [UnifyLab case study](https://github.com/midya8/Midya-portfolio/blob/main/projects/unifylab.md).


## UnifyLab: minimal equation conflicts and deletion repairs

[Live subset inspector](https://midya8.github.io/unifylab/cores.html) · [Source](https://github.com/midya8/unifylab) · [Method and inspected sources](https://github.com/midya8/unifylab/blob/main/SUBSETS.md)

Test every indexed subset, keep duplicate equation identities, and distinguish an inclusion-minimal conflict from a smallest conflict. Confirmed deletion repairs list indices to REMOVE and failing single restorations. The default control has independent duplicate/cycle conflicts and repairs of different sizes. A resource limit stays unresolved: no inferred status, false inconsistency, complete-frontier or minimum-size claim. Any selected subsystem opens its detailed rewrite trace.

Eight synthetic controls cover 371 subsets, including all 256 masks at the eight-equation bound, real state/result limits and a known clash beside an unknown expansion. Independent Python/JavaScript engines match 108 full audits and 1,032 subset summaries. Nineteen native tests pass on Python 3.10-3.13; six Node/Chrome tests. Native tests use a third lazy-binding oracle, all proper subsets and independent minimal hitting-set enumeration. Actual Chrome checks every control/subset/neighbor at 320/390/1280, five linked rewrite reproductions, export and invalid-state clearing. Installed wheels reproduce seventeen base reports and eight subset audits through both entry points outside the checkout.

Established finite-tree and constraint-diagnosis concepts, not a new scalable MUS/MCS algorithm. At most 256 independent bounded solves; the aggregate is not an independently verified rewrite certificate. Eight inspected sources distinguish minimal from minimum, conflict from repair, and unifiability semantics from resource limits. No model, API, paid service or private dataset.


## UnifyLab: repeated differences, shared variables

[Ground generalization inspector](https://midya8.github.io/unifylab/generalize.html) · [Method and inspected sources](https://github.com/midya8/unifylab/blob/main/GENERALIZATION.md) · [Source](https://github.com/midya8/unifylab)

Finite ground-term anti-unification: keep common constructors and give the same ordered disagreement pair the same variable. Inspect fresh/reuse records, two substitution maps and exact reconstructions. The independent native checker rejects coherent overgeneralization even when both inputs reconstruct. Python and independently written JavaScript agree on 209 reports; nine synthetic controls expose 43 node records. Original solver and subset inspectors retained.

27 native tests, nine Node/Chrome tests, installed wheel checks through both CLI entry points and responsive 320/390/1280 inspection. Established syntactic anti-unification, not a new algorithm, semantic clone detector or code repair model. Ground finite trees only; the checker validates the canonical trace, not arbitrary renamed certificates or a formal proof.


## HornLab: a circle is not a proof

[Live inspector](https://midya8.github.io/hornlab/) · [Source and tests](https://github.com/midya8/hornlab) · [Method and sources](https://github.com/midya8/hornlab/blob/main/METHOD.md)

Bounded positive propositional Horn inference with synchronous derivation rounds and every indexed rule decision. Compare the least model with every classical and supported model: a supported circular assignment need not have a derivation. Inspect an atomic countermodel for each non-entailed query and every inclusion-minimal initial-fact support, including its deletion failures and all seed subsets. Not entailed does not mean classically false.

Independent Python bitsets and JavaScript sets match 210 full reports; a separate native set/truth-table checker replays the complete report. Ten original controls, exhaustive two-atom programs, seeded tests, installed-wheel reproduction and actual Chrome record checks. Six atoms/eight rules, no negation or variables; established semantics, not a new algorithm or production rule engine.


## HornLab: every route, every break

[Rule-deletion inspector](https://midya8.github.io/hornlab/rules.html) · [Method and primary sources](https://github.com/midya8/hornlab/blob/main/RULES.md) · [Source](https://github.com/midya8/hornlab)

Keep initial facts fixed and inspect all indexed-rule subsets, synchronous closures, every minimal rule support and every minimal deletion set. One broken route need not break the goal. Each support retains one-rule removal failures; each deletion retains restoration successes. Both minimal-hitting-set dualities and every support/deletion intersection are explicit, including empty-support and already-absent boundary cases.

Eighteen native tests retain all originals, with all 1,024 two-atom programs and 150 seeded rule lattices. Independent Python/JavaScript match 131 audits covering 5,304 subsets. Eleven browser controls expose 305 subsets, 35 queries, 36 supports, 27 deletion sets and 36 intersections, all record-checked at 320/390/1280. A separate native set/truth-table checker validates the complete lattice without calling the generator. Installed-wheel reproduction checks both inspectors through both CLI entry points. Established bounded monotone explanation, not causal attribution, ontology translation, a new algorithm or formal proof.


### BisimLab: same traces, different choices

[Source](https://github.com/midya8/bisimlab) · [Interactive inspector](https://midya8.github.io/bisimlab/) · [Method](https://github.com/midya8/bisimlab/blob/main/METHOD.md)

Finite agent-protocol equivalence from scratch: every strong-bisimulation refinement, every failed left/right step match, executable Hennessy-Milner witness DAGs, truth sets and a quotient graph. The default original control has equal finite trace languages but loses a choice after the same action; exact paired-subset BFS checks trace equality separately from branching equivalence. A native partition-signature checker never calls the generator, and independent JavaScript matches full reports. Nine native tests include all 512 three-state/one-action graphs against relation enumeration and 100 seeded graphs; three Node/actual-Chrome tests include 593 complete cross-engine reports and every control record at 320/390/1280. Installed-wheel checks cover both CLI entry points outside checkout. One to six states, all labels visible: no silent abstraction, probabilities, policy guarantee, source extraction, new algorithm or formal-proof claim. Established theory and seven inspected sources are attributed in the method.


### BisimLab: complete trace-product replay

[Interactive trace product](https://midya8.github.io/bisimlab/traces.html) | [Source and exact semantics](https://github.com/midya8/bisimlab/blob/main/TRACES.md)

The second inspector retains the entire reachable product of two states' possible successor sets, including every action edge after a mismatch and the both-empty sink. Inspect canonical BFS discovery words, layers, all possibility-mismatch nodes and a shortest distinguishing path. Equal finite traces still do not imply branching equivalence.

Python bitmasks, independent JavaScript sets and a separate native checker based on explicit subset tables agree on 4,715 trace reports. Seventeen native tests include exhaustive unary three-state graphs across every ordered pair, direct word enumeration, seeded multi-action cases and forged closure/provenance checks. Six Node/actual-Chrome tests cover every control record, export and invalid-input clearing at 320/390/1280px. Installed-wheel checks cover six original and seven trace controls, two CLI entry points and six import origins. One to six states, all actions visible; exponential and bounded, with no silent actions, model/API dependency, scalable-solver or new-algorithm claim. Established subset determinisation and product language equivalence are attributed in the source ledger.


### ShieldLab: a safe next step can still lose

[Source](https://github.com/midya8/shieldlab) | [Interactive inspector](https://midya8.github.io/shieldlab/) | [Exact method and seven-source ledger](https://github.com/midya8/shieldlab/blob/main/METHOD.md)

An exact tiny safety-game inspector for hand-written agent protocols. Every synchronous fixed-point obligation, winning controller move, losing rank and branching invariant/counterstrategy graph is visible. Changing only who controls a state flips the result: one-step-safe actions need not preserve safety forever. Independent bitmask Python and explicit-set JavaScript, plus a separate dual-attractor and exhaustive positional-policy checker.

Eight native tests include all 21,952 three-state graph/ownership/safety combinations and 150 seeded larger arenas. Three Node/actual-Chrome tests compare 643 complete reports and all six controls at 320/390/1280. Installed wheels replay both CLI entry points outside checkout. Finite total perfect-information model only: no runtime shield, LLM guarantee, liveness, timing, probability, new algorithm or formal proof. Dead ends are rejected; safe waiting need not mean progress.

### BuchiLab: a winning state is not a winning policy

[Interactive inspector](https://midya8.github.io/buchilab/) | [Source](https://github.com/midya8/buchilab) | [Method and seven-source ledger](https://github.com/midya8/buchilab/blob/main/METHOD.md)

Tiny finite adversarial repeated-goal games with every nested greatest/least fixed-point obligation, progress rank, complete positional controller policy and reachable cyclic non-goal SCC visible. Idle can stay inside the winning region forever and still lose: rank-guided progress and per-policy audits show why. A separate checker replays with sets/Floyd reachability and every joint-policy eventual lasso, without calling the generator. Nine native tests include 21,952 exhaustive three-state games; three Node/actual-Chrome tests compare 331 complete Python/JavaScript reports and every control record at 320/390/1280. Installed wheels replay seven original controls through both CLIs outside checkout. No fairness assumption, learned abstraction, deployed shield, general LTL compiler, formal proof or real-agent guarantee. Rank-permitted actions are sufficient, not all winning policies.

### BuchiLab: repeat the actual failure

[Action-level lasso inspector](https://midya8.github.io/buchilab/lassos.html) | [Exact witness contract](https://github.com/midya8/buchilab/blob/main/LASSOS.md)

A reachable bad component now becomes an exact action-labelled prefix once and nonempty non-goal cycle forever, for every failing fixed controller policy/root. Empty prefixes, self-loops, multiedge cycles, unreachable bad components and duplicate-target action choices are explicit. BFS generation is independently checked with bounded simple walks and the joint-policy lasso oracle. Original v1 reports and original tests stay intact: 16 native tests across four Python versions and five Node/actual-Chrome tests, including 314 complete witness-report comparisons and every record in ten controls at 320/390/1280. Installed wheels replay both report families outside checkout. Input-order anchor, shortest prefix/cycle individually, not globally shortest lasso. These are per-policy counterexamples, not one environment strategy defeating every controller policy or a real-agent guarantee.
