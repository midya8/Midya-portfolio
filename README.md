# Midya Rahmani

Toronto-based technologist with 12+ years across technology, financial services, and telecommunications. Lately building with large language models, agentic systems, and workflow automation.

## What I build

- **LLM and agentic systems** — practical AI workflows, not demos: systems that do real work end to end.
- **Workflow automation** — taking manual, multi-step processes and making them reliable and repeatable.
- **Web platforms** — TypeScript, React, Next.js, and static-first architectures that stay fast and maintainable.

## How I build

The projects below share an approach, written up in [approach.md](approach.md): choose the simplest architecture that meets the requirement, make tools that fit into scripts as well as terminals, validate before executing, and let reports and documents be outputs of the work rather than afterthoughts — all designed around real constraints, from right-to-left layouts to reduced-motion preferences.

## Selected projects

### EvalForge

Local-first evaluation for LLM and agent outputs: versioned JSONL task suites, deterministic scorers, a stdin/stdout adapter contract, retries, timeouts, bounded parallel execution, persistent run artifacts, baseline regression gates, and self-contained escaped HTML plus JUnit XML reports.

- **Evaluation as a repeatable gate** - run the same suite against any command-line model or agent adapter, compare a candidate to a saved baseline, and fail on score regressions, adapter errors, or latency policy breaches.
- **Deterministic checks before model judging** - exact, contains, regex, JSON schema-ish, numeric tolerance, length, and similarity scorers make results reproducible without a network dependency.
- **Artifacts built for review** - JSON run records preserve prompts, outputs, scores, errors, and timings; JUnit XML reports expose results to CI test viewers; HTML reports are standalone and escape untrusted model output by default.
- Dependency-free Python 3.10+, 60 unit tests, a fully offline six-task demo that validates JUnit output, and CI across Python 3.10-3.13.

- Repo: [midya8/evalforge](https://github.com/midya8/evalforge)

### AgentTrace

Local-first validation, analysis and reporting for AI agent execution traces: JSONL trace structure checks, run summaries, tool/LLM call counts, latency and cost rollups, graph depth, repeated-step loop detection, baseline/candidate regression comparison, quality gates, a standalone escaped HTML timeline, and deterministic JUnit XML output for CI test viewers.

- **Agent runs as inspectable data** - parse JSONL traces from local agents, test fixtures, internal tools or hosted-model adapters without sending prompts or outputs anywhere.
- **Gates that catch agent failure modes** - fail CI on errored steps, p95 latency, cost, step count, a repeated tool/action signature that indicates a loop, or regressions against a saved baseline trace.
- **Reports built for review** - deterministic JSON analysis artifacts, JUnit XML for CI test viewers, and a self-contained HTML report show run summaries and per-step timelines with untrusted trace fields escaped by default.
- Dependency-free Python 3.10+, 30 unit tests, a fully offline fixed-trace baseline/candidate demo that validates JUnit output, and CI across Python 3.10-3.13.

- Repo: [midya8/agenttrace](https://github.com/midya8/agenttrace)

### PromptGuard

Local-first prompt, secret and prompt-injection linting for AI systems: OpenAI/AWS-style key checks, assigned-secret and private-key detection, email/phone/Luhn-validated card detection, injection-language rules, prompt metadata frontmatter checks, redacted terminal/JSON/SARIF/escaped HTML reports, and severity or finding-count CI gates.

- **Prompt files as reviewed production configuration** - scan prompt, Markdown, JSON and YAML files before credentials, personal data or unsafe instruction patterns ship with an AI workflow.
- **Redaction by default** - reports keep enough location and excerpt context for review without copying full credentials or contact details into output artifacts.
- **Gates that fit CI** - deterministic rule IDs, severities, JSON output and exit codes let a repository fail on high-severity findings or cap total findings.
- Dependency-free Python 3.10+, 31 unit tests, a fully offline safe/risky fixture demo that validates SARIF output, and CI across Python 3.10-3.13.

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
