# Midya Rahmani

Toronto-based technologist with 12+ years across technology, financial services, and telecommunications. Lately building with large language models, agentic systems, and workflow automation.

## What I build

- **LLM and agentic systems** — practical AI workflows, not demos: systems that do real work end to end.
- **Workflow automation** — taking manual, multi-step processes and making them reliable and repeatable.
- **Web platforms** — TypeScript, React, Next.js, and static-first architectures that stay fast and maintainable.

## How I build

The projects below share an approach, written up in [approach.md](approach.md): choose the simplest architecture that meets the requirement, make tools that fit into scripts as well as terminals, validate before executing, and let reports and documents be outputs of the work rather than afterthoughts — all designed around real constraints, from right-to-left layouts to reduced-motion preferences.

## Selected projects

### RAGLine

Retrieval-augmented answering built from scratch in pure Python: a deterministic templated corpus chunked with stable ids, token-hashed sparse TF-IDF embeddings, top-k cosine retrieval, extractive answers that always cite their source chunk, and a grounding check that verifies each answer against the chunk it cites - with the check proven to fail on corrupted citations.

- **The RAG loop as inspectable steps** - corpus, embed, retrieve, answer, verify, each dependency-free and deterministic from one seed.
- **Grounding as a gate, not a slogan** - the verifier scores token overlap between answer and cited chunk; `--require-grounded` and `--min-grounded` fail CI when unsupported answers appear, and the test suite proves corrupted citations are flagged.
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
