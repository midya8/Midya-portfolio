# Projects

Longer write-ups on selected work. Everything here links back to the public repository (and live site, where there is one) so the code can speak for itself.

## Web platforms

- **Kurdistan International Sociological Association website** — Trilingual site (English, Sorani Kurdish right-to-left, Kurmanji Kurdish) in Next.js, TypeScript, and Tailwind, exported as static HTML and hosted on Cloudflare.
  - Case study: [kurdistansociology-website.md](kurdistansociology-website.md)
  - Repo: [midya8/kurdistansociology-website](https://github.com/midya8/kurdistansociology-website) · Live: [kurdistansociology.com](https://kurdistansociology.com)
- **Personal site — midya.ca** — React, TypeScript, and Vite, set against a procedurally generated Three.js galaxy that adapts rendering quality to the device and respects reduced-motion settings.
  - Case study: [midya-ca.md](midya-ca.md)
  - Repo: [midya8/midya.ca](https://github.com/midya8/midya.ca) · Live: [midya.ca](https://midya.ca)

## Python utilities

Dependency-free, standard-library-only tools: a CLI for day-to-day use plus an importable library for automation, backed by unit tests and CI across Python 3.10–3.13.

- **sre-toolkit** — Error-budget and burn-rate math, multi-window burn-rate alerting, rule-based alert triage, and Markdown SLO definitions, status reports, and postmortems. 146 unit tests.
  - Case study: [sre-toolkit.md](sre-toolkit.md)
  - Repo: [midya8/sre-toolkit](https://github.com/midya8/sre-toolkit)
- **loglens** — Access-log analysis for incident work: error rates, failing paths, 5xx sources, latency percentiles, incident timelines, and Markdown incident reports. Parses nginx/Apache combined and JSON logs. 142 unit tests.
  - Case study: [loglens.md](loglens.md)
  - Repo: [midya8/loglens](https://github.com/midya8/loglens)
