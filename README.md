# Midya Rahmani

Toronto-based technologist with 12+ years across technology, financial services, and telecommunications. Lately building with large language models, agentic systems, and workflow automation.

## What I build

- **LLM and agentic systems** — practical AI workflows, not demos: systems that do real work end to end.
- **Workflow automation** — taking manual, multi-step processes and making them reliable and repeatable.
- **Web platforms** — TypeScript, React, Next.js, and static-first architectures that stay fast and maintainable.

## Stack at a glance

- **Languages:** TypeScript, Python
- **Web:** React, Next.js, Tailwind CSS, Vite, Three.js
- **Python utilities:** dependency-free and standard-library only, with a CLI, an importable library, unit tests, and CI

## How I build

- **Prefer foundations that are easy to maintain:** standard-library-only Python tools and static-first web builds, so there is less to break and less to keep up to date.
- **Ship tools that work two ways:** a CLI for day-to-day use and an importable library for automation, backed by unit tests and CI.
- **Design for real constraints:** trilingual content including right-to-left text, static hosting, and rendering that adapts to the device and respects reduced-motion settings.

## Selected projects

Longer write-ups live in [projects/](projects/README.md).

### sre-toolkit

Dependency-free Python utilities for day-to-day SRE work: error-budget and burn-rate math with exhaustion projection, remaining-bad-event counts, and JSON output for pipelines, multi-window burn-rate alerting with custom rules, rule-based alert triage with custom rule files that dedupes repeats, keeps each alert's fire count, and inhibits lower-severity symptoms under an active critical, and Markdown SLO definitions, status reports with budget-exhaustion projections and worst-first sorting, and postmortems with automatic response metrics (Markdown or JSON) plus MTTR aggregation (mean/median/p90 per severity, JSON output) across incidents. Every command doubles as a scriptable health gate through meaningful exit codes. CLI plus importable library, 146 unit tests, CI across Python 3.10-3.13.

- Repo: [midya8/sre-toolkit](https://github.com/midya8/sre-toolkit)
- Case study: [projects/sre-toolkit.md](projects/sre-toolkit.md)

### loglens

Dependency-free access-log analysis for incident work: error rate, status distribution, hottest failing paths, and the source IPs behind 5xxs, plus per-bucket incident timelines, p50/p95/p99 latency, time-window filtering, per-path volume/error/latency tables sortable by errors, volume or p95, a 2xx/3xx/4xx/5xx status-class roll-up, before/after comparison around a deploy timestamp, status-code, class and path-prefix filters that scope every statistic, method, user-agent and referer triage behind 5xxs (also surfaced in the incident reports), a pipeline gate that exits 1 when the 5xx rate breaches a threshold, and Markdown incident reports with per-path breakdowns, spike windows, and optional before/after deploy comparisons. Parses nginx/Apache combined and JSON logs with per-line auto-detection, standard library only, CLI plus importable library, 142 unit tests with CI across Python 3.10-3.13.

- Repo: [midya8/loglens](https://github.com/midya8/loglens)
- Case study: [projects/loglens.md](projects/loglens.md)

### Kurdistan International Sociological Association website

Trilingual website (English, Sorani Kurdish right-to-left, and Kurmanji Kurdish) built with Next.js, TypeScript, and Tailwind, exported as static HTML and hosted on Cloudflare.

- Repo: [midya8/kurdistansociology-website](https://github.com/midya8/kurdistansociology-website)
- Live: [kurdistansociology.com](https://kurdistansociology.com)
- Case study: [projects/kurdistansociology-website.md](projects/kurdistansociology-website.md)

### Personal site — midya.ca

A personal site set against a procedurally generated Three.js galaxy that adapts rendering quality to the device and respects reduced-motion settings. Built with React, TypeScript, and Vite.

- Repo: [midya8/midya.ca](https://github.com/midya8/midya.ca)
- Live: [midya.ca](https://midya.ca)
- Case study: [projects/midya-ca.md](projects/midya-ca.md)

## Find me

- [midya.ca](https://midya.ca)
- [LinkedIn](https://www.linkedin.com/in/midyarahmani/)
