# Projects

Longer write-ups on selected work. Everything here links back to the public repository (and live site, where there is one) so the code can speak for itself.

## At a glance

| Project | Stack | What it is for | Start here |
|---|---|---|---|
| ScratchGPT | Python, NumPy; CLI plus importable package | Transformer and reverse-mode autograd built from scratch, with training, sampling and finite-difference verification | [Case study](scratchgpt.md) |
| Kurdistan International Sociological Association website | Next.js, TypeScript, Tailwind; static export on Cloudflare | Trilingual editorial site (English, Sorani Kurdish right-to-left, Kurmanji Kurdish) | [Case study](kurdistansociology-website.md) |
| Personal site — midya.ca | React, TypeScript, Vite, Three.js | Personal site around a procedurally generated galaxy that adapts to the device and respects reduced-motion settings | [Case study](midya-ca.md) |
| sre-toolkit | Python, standard library only; CLI plus importable library | Day-to-day SRE work: error budgets, burn-rate alerting, alert triage, SLO definitions, status reports, and postmortems | [Case study](sre-toolkit.md) |
| loglens | Python, standard library only; CLI plus importable library | Access-log analysis for incident work: error rates, failing paths, 5xx sources, latency, timelines, and Markdown incident reports | [Case study](loglens.md) |
| flowkit | Python, standard library only; CLI plus importable library | Running JSON-defined DAGs of shell commands with retries, timeouts, parallel steps, conditional steps, and run reports | [Case study](flowkit.md) |
| uptimekit | Python, standard library only; CLI plus importable library | Synthetic uptime monitoring and availability reporting: probes, JSONL history, SLO measurement, incident gating, and an HTML status page | [Case study](uptimekit.md) |

## AI systems

Local-first tools for evaluating, tracing and reviewing LLM and agent workflows, plus a transformer built from scratch.

- **ScratchGPT** - GPT built and trained from scratch in pure NumPy, with hand-written autograd, a pre-LN causal transformer, Adam training, sampling CLI and finite-difference gradient checks. 11 unit tests.
  - Case study: [scratchgpt.md](scratchgpt.md)
  - Repo: [midya8/scratchgpt](https://github.com/midya8/scratchgpt)
- **EvalForge** - Versioned JSONL task suites, deterministic scorers, adapter execution, persistent run artifacts and baseline regression gates for LLM and agent outputs. 60 unit tests.
  - Repo: [midya8/evalforge](https://github.com/midya8/evalforge)
- **AgentTrace** - Validation, analysis, baseline/candidate comparison and escaped HTML timelines for AI agent execution traces. 30 unit tests.
  - Repo: [midya8/agenttrace](https://github.com/midya8/agenttrace)
- **PromptGuard** - Secret, PII, prompt-injection and metadata linting for prompt files with redacted JSON/HTML reports and CI gates. 28 unit tests.
  - Case study: [promptguard.md](promptguard.md)
  - Repo: [midya8/promptguard](https://github.com/midya8/promptguard)

## Web platforms

- **Kurdistan International Sociological Association website** — Trilingual site (English, Sorani Kurdish right-to-left, Kurmanji Kurdish) in Next.js, TypeScript, and Tailwind, exported as static HTML and hosted on Cloudflare.
  - Case study: [kurdistansociology-website.md](kurdistansociology-website.md)
  - Repo: [midya8/kurdistansociology-website](https://github.com/midya8/kurdistansociology-website) · Live: [kurdistansociology.com](https://kurdistansociology.com)
- **Personal site — midya.ca** — React, TypeScript, and Vite, set against a procedurally generated Three.js galaxy that adapts rendering quality to the device and respects reduced-motion settings.
  - Case study: [midya-ca.md](midya-ca.md)
  - Repo: [midya8/midya.ca](https://github.com/midya8/midya.ca) · Live: [midya.ca](https://midya.ca)

## Python utilities

Dependency-free, standard-library-only tools: a CLI for day-to-day use plus an importable library for automation, backed by unit tests and CI.

- **sre-toolkit** — Error-budget and burn-rate math, multi-window burn-rate alerting, rule-based alert triage, and Markdown SLO definitions, status reports, and postmortems. 254 unit tests.
  - Case study: [sre-toolkit.md](sre-toolkit.md)
  - Repo: [midya8/sre-toolkit](https://github.com/midya8/sre-toolkit)
- **loglens** — Access-log analysis for incident work: error rates, failing paths, 5xx sources, latency percentiles, incident timelines, and Markdown incident reports. Parses nginx/Apache combined and JSON logs. 241 unit tests.
  - Case study: [loglens.md](loglens.md)
  - Repo: [midya8/loglens](https://github.com/midya8/loglens)
- **flowkit** — Workflow runner: JSON-defined DAGs of shell commands with retries and exponential backoff, timeouts, fail-fast or continue-on-error semantics, parallel execution, conditional steps, end-phase hooks, dry-run plans, and text/JSON run reports. Standard library only, 123 unit tests.
  - Case study: [flowkit.md](flowkit.md)
  - Repo: [midya8/flowkit](https://github.com/midya8/flowkit)
- **uptimekit** — Synthetic uptime monitoring and availability reporting in pure Python, no dependencies and no database: HTTP, TCP connect, and TLS certificate-expiry probes, an append-only JSONL history, availability roll-ups with latency percentiles, incident detection with a consecutive-failure flap guard and a sustained-outage gate, SLO measurement (error budget consumed, met-or-breached status, --fail-slo exits 1 on a breach), a watch mode for hosts without cron, and a self-contained HTML status page. 98 unit tests running fully offline, CI on Python 3.11.
  - Case study: [uptimekit.md](uptimekit.md)
  - Repo: [midya8/uptimekit](https://github.com/midya8/uptimekit)
