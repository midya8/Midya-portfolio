# sre-toolkit — case study

Dependency-free Python utilities for day-to-day SRE work: error budgets, burn-rate alerting, alert triage, and the Markdown documents an incident workflow runs on — SLO definitions, status reports, and postmortems.

- Repo: [midya8/sre-toolkit](https://github.com/midya8/sre-toolkit)

## The constraint that shaped the build

SRE tooling tends to arrive as a heavy platform: a service to run, dependencies to keep current, and a deployment to maintain before a single error budget is computed. For day-to-day reliability work, that overhead is the opposite of what the tools are for. The goal here was utilities that are available the moment you need them — no install ceremony, no runtime to babysit — and that fit into scripts and automation as naturally as they fit into a terminal session.

## Decisions

- **Standard library only, no dependencies.** Every utility is dependency-free Python, so there is nothing to install beyond Python itself and nothing to break when a third-party package changes. That is also what makes the tools safe to drop into any environment, including one mid-incident.
- **CLI plus importable library.** Each tool works two ways: as a command you run by hand, and as a library you import into automation. The same error-budget math that answers a question in the terminal can drive a scheduled check without being rewritten.
- **Error budgets with exhaustion projections.** Burn-rate math does not stop at the current rate — it projects when the budget runs out and how many bad events remain, which turns a number into a decision: whether there is room to ship, or whether reliability work comes first.
- **Remaining bad events, not just a percentage.** The budget answer is a concrete allowance — how many bad events the window still affords — so "can we ship?" is answered in events, not in an abstract percentage.
- **Multi-window burn-rate alerting with custom rules.** Different windows catch different failure modes — a fast burn over a short window and a slow bleed over a long one — and custom rules let the alerting match the service instead of forcing every service into one threshold.
- **Both windows must agree before paging.** Burn-rate alerting fires only when burn is elevated on both the long and short window, so a blip on one window never pages anyone — the pair, not a single threshold, decides.
- **Alert policy suggested, not hand-written.** `burn --suggest` emits the standard three-tier multi-window policy for any SLO window, so a new service starts from a known-good policy instead of a guessed threshold.
- **Alert policy tuned against history, not guesses.** `burn --replay` re-evaluates every rule's windows at each timestamped bucket and reports each firing interval, so a policy can be tested against a past incident before it pages anyone.
- **Alert triage that reduces noise instead of adding to it.** Triage dedupes repeat alerts, keeps each alert's fire count so frequency stays visible, and inhibits lower-severity symptoms while a critical is active — so an incident surfaces as one problem to solve, not a wall of symptoms.
- **Triage rules from a file, not just the command line.** Triage accepts custom rule files, so the policy that shapes the board is written down and reusable across runs instead of re-typed as flags each time.
- **Noisiest alerts first.** `triage --top-talkers` ranks the deduped alerts by fire count, so the alerts firing most often — the ones most likely to be a real, repeated problem rather than a one-off — lead the board.
- **Bounded, reasoned silences.** `triage --silences` applies silences matched on service, severity, or summary text — so suppressing an alert is a deliberate, scoped decision, not a mute that quietly swallows everything.
- **Alert ownership routing, so triage ends with an owner.** `triage --routes` maps services to owning teams with an explicit default owner so routing gaps stay visible, and `--by-owner` rolls the board up per team, worst severity first — so the triaged alert list is also an assignment list.
- **Documents as output, not an afterthought.** SLO definitions, status reports with budget-exhaustion projections and worst-first sorting, and postmortems with automatic response metrics (Markdown or JSON) and MTTR aggregation (mean/median/p90 per severity, JSON output) across incidents are all generated from the same tools that did the analysis, in a format that can be committed, reviewed, and searched.
- **Postmortem action items that don't go stale.** `metrics --action-items` groups open items per incident with days since resolution and exits 1 when items go stale past `--stale-days` — so follow-through is itself a gate, not a list that quietly ages.
- **A trend view, not just a snapshot.** MTTR aggregation includes a weekly trend view across incidents, so "are we getting faster?" is answered over time, not from a single window's average.
- **Fleet-wide roll-ups across whole incident sets.** Report summaries, triage ranked by severity, and metrics grouped by service — so a set of incidents reads as one picture, not a pile of separate reports.
- **Meaningful exit codes as health gates.** Every command doubles as a scriptable health gate: a pipeline or scheduled check can act on the result without parsing human-readable output.

## Testing and compatibility

146 unit tests, with CI across Python 3.10–3.13.

## Worked example: the first ten minutes of an SLO review

The commands below are the real sre-toolkit CLI, taken from the project's own usage docs. One question leads to the next — budget, burn, triage, report, postmortem, trend — and every step is the same tool, not a new setup:

```bash
python -m sre_toolkit budget --slo 0.999 --total 10000 --bad 5 --window-days 30
# how much of the error budget is consumed, the burn rate, and how many
# bad events the window still affords — exits 1 if the budget is exhausted

python -m sre_toolkit burn examples/burn-samples.json
# multi-window burn-rate alerting: fires only when burn is elevated on
# both the long and short window, so blips never page anyone

python -m sre_toolkit triage examples/alerts.json --inhibit
# deduped alerts sorted by severity, with lower-severity symptoms
# suppressed while a critical is active on the same service

python -m sre_toolkit report examples/slo-snapshots.json --worst-first
# a Markdown SLO status report, worst budgets first, with exhaustion
# projections for any snapshot carrying its window length

python -m sre_toolkit postmortem examples/incident.json
# a consistent Markdown postmortem, with response metrics computed
# automatically from the incident timestamps

python -m sre_toolkit metrics examples/incidents.json --json
# MTTR across incidents — mean, median, and p90 per severity — as JSON
# for dashboards, answering "are we getting faster?" with numbers
```

The same math is importable as a library (`from sre_toolkit.error_budget import compute_error_budget, allowed_downtime_minutes`), so an ad-hoc question in the terminal and a scheduled check share one implementation.

## What it demonstrates

Building reliability tooling that respects its own subject matter: small, dependency-free, and boring in the right ways, so the tools themselves never become the incident. The design favors the operator — one command, a clear answer, and output that slots directly into the incident workflow.
