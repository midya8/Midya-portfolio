# How I build

The approach behind the projects in this portfolio, stated once so the
pattern is visible across them. Each principle below is demonstrated by a
project linked from it — not asserted in the abstract.

## Choose the simplest architecture that meets the requirement

The Kurdistan International Sociological Association site is editorial
content, not a transaction system, so it is exported to static HTML and
served from Cloudflare: no server to keep up, scale, or patch. The Python
utilities are standard-library only for the same reason — if Python is
installed, they run, with no dependency tree to maintain. The personal site
uses React and Vite for the same end: a static build with nothing to keep
running behind it.

- [Kurdistan International Sociological Association website](projects/kurdistansociology-website.md)
- [sre-toolkit](projects/sre-toolkit.md), [loglens](projects/loglens.md), [flowkit](projects/flowkit.md)
- [Personal site — midya.ca](projects/midya-ca.md)

## Make tools that fit scripts as well as terminals

A tool that only works interactively is half a tool. Every Python utility
here is both a command you run by hand and a library you import into
automation, and every command communicates its result through its exit
code: sre-toolkit exits 1 when an error budget is exhausted, loglens exits
1 when a 5xx rate breaches a threshold, and flowkit uses 0 for success, 1
for a failed step, and 2 for an invalid flow file. A pipeline or scheduled
check can act on the result without parsing human-readable output.

## Validate before executing

A bad input should fail loudly before anything happens, not halfway
through. flowkit rejects duplicate step names, dangling dependencies,
cycles, unknown keys, and malformed interpolation before running a single
step, and its `--strict-env` check fails up front on any unset variable
reference instead of letting a blank value silently change a command. The
same instinct shows up in loglens, where filters scope every statistic, so
narrowing to a failing slice never leaves stray numbers computed over the
full log.

## Let reports and documents be outputs, not afterthoughts

The analysis tools generate the documents the workflow runs on, in formats
that can be committed, reviewed, and searched: SLO definitions, status
reports with budget-exhaustion projections, and postmortems with automatic
response metrics from sre-toolkit; Markdown incident reports with per-path
breakdowns and spike windows from loglens; text or JSON run reports with
captured output tails from flowkit. The report is not a separate chore
after the work — it is what the tool produces.

## Reduce noise; answer the question first

Incident tooling fails when it adds to the wall of symptoms. sre-toolkit's
triage dedupes repeat alerts, keeps each alert's fire count so frequency
stays visible, and inhibits lower-severity symptoms while a critical is
active, so an incident surfaces as one problem to solve. loglens leads
with the headline answers — error rate, status distribution, hottest
failing paths, and the source IPs behind 5xxs — and only then narrows
into timelines, latency tables, and per-client breakdowns.

## Design around the constraint, not around it

The hard parts of these projects were constraints, and each one is handled
where it belongs rather than bolted on. Sorani Kurdish reads right-to-left,
so direction is handled at the layout level of the association site, not
just by translating strings. The personal site's galaxy is generated
procedurally so it can scale its rendering effort to the device, and
visitors who prefer reduced motion get a calmer presentation. flowkit's
steps run in deterministic topological order with declaration order
breaking ties, so parallel runs still report comparably run to run.

## What this adds up to

Practical systems over demonstrations: tools that are available the
moment they are needed, that fail loudly, that fit into automation
unchanged, and that leave a readable record behind them. The repositories
linked above are the evidence — the code, not the claims, is the point.
