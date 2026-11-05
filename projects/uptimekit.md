# uptimekit — case study

Synthetic uptime monitoring and availability reporting in pure Python, no dependencies and no database — if Python is installed, uptimekit runs. CLI plus importable library, 98 unit tests running fully offline, CI on Python 3.11.

## The problem

Uptime monitoring usually means either a hosted service or a monitoring stack: an account, a server, and a database to keep running just to answer "is it up?" uptimekit targets the middle: a checker you can run from cron, whose history is a plain file you can read, and whose report is a page you can publish without standing anything up.

## What it does

Probes cover HTTP (status, keyword-in-body, latency), TCP connect, and TLS certificate expiry. Results go to an append-only JSONL history with atomic retention compaction, so history survives interrupted runs and does not grow without bound.

Availability roll-ups report p50/p95 latency percentiles, a per-day trend strip where monitoring gaps stay visible rather than being smoothed over, and window-over-window comparison. SLO targets (`"slo": 99.9`) are measured by `report --config`: error budget consumed so far and met-or-breached status, with `--fail-slo` exiting 1 on a breach — so an SLO breach gates a pipeline the same way an open incident does. Incident detection uses a consecutive-failure flap guard plus a sustained-outage gate (`--max-open-minutes` pages on real outages, not self-healing blips). A watch mode covers hosts without cron, and a self-contained HTML status-page renderer (inline CSS, no JavaScript, fully escaped) turns the same data into a publishable page.

Latency assertions turn slow into down, and TLS expiry thresholds turn a certificate quietly approaching expiry into a failure while there is still time to act.

## Design decisions

### Probing — what a check is
- **Check from the outside, like a visitor.** uptimekit probes endpoints the way a visitor experiences them — HTTP status, content, and latency, plus TCP connect and TLS expiry — rather than reading server logs after the fact, so it catches a site that is up for the server but broken for the people trying to use it.
- **Up means the content is right, not just the status code.** An HTTP probe checks status, latency, and keyword-in-body, so a page that returns 200 with the wrong content still counts as down — a status check alone would have called it healthy.
- **TCP connect checks the layer below HTTP.** A TCP connect probe verifies the host is reachable and listening before any HTTP exchange, so a refused connection or unreachable host is a failure even when there is no HTTP response to grade — the checker catches outages at the network layer, not only at the application layer.
- **Slow is down.** A latency assertion converts a degraded endpoint into a failure, and a TLS expiry threshold converts an expiring certificate into one, instead of leaving both as warnings nobody acts on.
- **One request, three verdicts.** A single HTTP probe returns status, latency, and body content in one request, so availability, slowness, and wrong content are all judged from the same observation — the checker never has to probe the same endpoint three times to answer three questions, and the three verdicts can never disagree about which moment they describe.
- **Expiry is a failure while there is still time to act.** A TLS expiry threshold turns a certificate quietly approaching expiry into a failure, so the problem surfaces with time left to renew instead of being discovered when the site breaks — expiry, unlike an outage, is predictable, and the probe treats it that way.
- **Different failures stay distinguishable.** A refused TCP connection, a wrong keyword in the body, a slow response, and a certificate near expiry are different failures, and the history records them as such — so diagnosing an outage starts from what kind of failure it was, not just from "down", and the first question after an alert is already partly answered.
- **A failure is a result, not a crash.** When a probe fails — a refused connection, a wrong keyword, a slow response — uptimekit records it as a probe result in the history and exits 1, rather than dying mid-run: a down endpoint is data the checker is built to handle, not an exception that stops the check, so one failed probe never prevents the record — or the next probe — from happening.
- **Probes observe, they do not change.** A synthetic probe only reads — an HTTP request, a TCP connect, a TLS handshake — and never writes to the monitored service, so monitoring itself cannot cause an outage, corrupt state, or alter what it measures. The checker watches from outside without becoming another way the service can break.
- **Nothing to install on what you monitor.** Synthetic probes run from outside the service, so monitoring needs no agent, sidecar, or instrumentation on the monitored endpoint itself — the checker observes from elsewhere, and adding a service to monitoring never means modifying that service.
- **Endpoints are configuration, not code.** The checker knows nothing about the services it monitors — what to probe, and with which thresholds, lives in config — so adding an endpoint means editing a file, not changing the checker: the same tool monitors one site or twenty without a code change, and the list of what is watched is itself a document you can review.

### History — one record, honestly kept
- **One history for every probe type.** HTTP, TCP connect, and TLS certificate-expiry probes all write to the same append-only JSONL history, so a single report covers every probe type instead of each check keeping its own record.
- **History that survives interrupted runs.** Results go to an append-only JSONL history with atomic retention compaction, so history survives interrupted runs and does not grow without bound — the record a report is built from is a plain file you can read, not a database you have to keep running.
- **Append-only, so the past cannot be rewritten.** Results are appended to the JSONL history, never edited in place, so a later run cannot alter what an earlier probe recorded — the history is an audit trail of what was observed, not a mutable current-state file that a bad run could quietly overwrite.
- **The whole history, not just the latest result.** The checker keeps every probe result in the append-only history, not only the current status — because roll-ups, the per-day trend strip, window-over-window comparison, and SLO measurement all need the past, not just the present: a checker that only remembered "up or down right now" could answer the moment but never the story.
- **One file is the whole state.** The checker's only persistent state is the JSONL history file — no database, cache, or secondary store alongside it — so backing up, moving, or inspecting the monitor means copying one readable file, and a fresh install picks up exactly where the old one left off by reading that file alone.
- **History you can read without the tool.** The JSONL history is a plain file, so an incident can be investigated with ordinary text tools — grep, head, tail — without uptimekit itself running; the record outlives any particular version of the checker that wrote it.
- **Bounded history, no maintenance.** Retention compaction keeps the append-only JSONL history from growing without bound, so a checker that runs from cron for months needs no manual pruning — history stays bounded by design rather than by cleanup chores.
- **Compaction that cannot corrupt the record.** Retention compaction rewrites the history atomically, so a crash mid-compaction leaves either the old file or the new one — never a half-written history. The bound on growth is kept without ever risking the record it prunes.
- **Gaps stay visible.** The per-day trend strip shows monitoring gaps as gaps. A report that hides missing data overstates availability; an honest strip lets a gap be investigated instead of averaged away.
- **A gap is not uptime.** A period with no probe results produces no success records, so the per-day trend strip shows it as a gap rather than crediting the endpoint with uptime it never observed — the report never rewards the checker for time it was not running.
- **Timestamps turn failures into durations.** Every probe result lands in the history with its time, so an outage is not just a red state but a span — when it started, how long it has lasted, and whether it is still open — which is what the sustained-outage gate and the open-incident reports measure from, rather than a single momentary verdict.
- **A failure leaves a record, not just an alert.** When `check` exits 1, the failed probe is already in the append-only history — so an outage is still there for the next roll-up, trend strip, or SLO report even if nobody was watching at the moment it happened, instead of existing only as a momentary alert that fades.
- **Recovery is a record, not a reset.** An open incident ends when a later probe succeeds — the success lands in the same history as the failures, so the outage's end is as observable as its start, and the duration between the first failure and that success is measured from the record rather than reconstructed from an alert clearing.

### Reports — derived from the same record
- **One source for checks and reports.** The probes write the JSONL history and every report — roll-ups, trend strip, SLO status, status page — reads that same file, so there is no second store to keep in sync and a report can never disagree with the checks that produced it.
- **One definition of down, everywhere.** A probe failure is defined once — a bad status, a missing keyword, a slow response, a refused connection, or a certificate near expiry — and every consumer reads that same record: the `check` exit code, the open-incident report, the SLO status, and the status page. "Down" never means one thing to the checker and another to the report, because they are all reading the same history.
- **One history, many questions.** A single probe run writes one record, and that record answers every later question — availability roll-ups, latency percentiles, SLO status, open incidents, and the status page — without re-probing. The checker does not collect separate data for each report; each report is a different reading of the same history, so the answers can never disagree about what was observed.
- **Reports are derived, not stored.** Roll-ups, trend strips, SLO status, and the status page are all generated from the JSONL history rather than stored as separate state, so a report can be regenerated at any time from the same record — there is nothing to rebuild after a report is lost, and no stored report can drift from the history it claims to summarise.
- **One answer now, the story over time.** A single `check` answers "is it up?" right now, while the accumulated history answers how it has been — roll-ups, trend strip, and SLO status turn the same probes into a record over time, so a momentary answer and a longer view come from one checker, not two tools.
- **Compare windows, not just snapshots.** Availability roll-ups include a window-over-window comparison, so a report answers whether availability improved or regressed against the previous window instead of presenting one window in isolation.
- **Percentiles, not averages.** Availability roll-ups report p50/p95 latency percentiles, so a slow tail is visible instead of being averaged away by mostly fast probes — the number that matters for a degraded endpoint is the slow end, not the mean.
- **Uptime is counted from successes, not from silence.** Availability roll-ups are computed from the probe history, where successes are recorded just like failures — so uptime is a measured ratio of successful probes, not the absence of alerts. A checker that only recorded failures could never prove a service was up; the history proves both.
- **Days, not just an overall number.** The per-day trend strip breaks availability down day by day, so a single bad day stays visible instead of being averaged into one overall figure, and a recovery shows up as better days following worse ones — the report keeps the shape of time, not just a single number.
- **Slow degradation shows up before it becomes an outage.** Availability roll-ups report p50/p95 latency percentiles over time, so a rising slow tail is visible in the trend before it crosses a latency assertion and turns into a failure — the report warns while there is still time to act, rather than only recording the outage after the fact.
- **Reports as outputs.** The availability roll-ups, the trend strip, SLO status reports (error budget consumed, met-or-breached status), and the HTML status page are what the tool produces, not a separate chore after running it.
- **Reports you can commit.** Roll-ups, trend strips, and the status page are plain files, not dashboard state — so a report can be committed, reviewed, and searched like any other document, and the record of an incident lives alongside the code instead of inside a service that might itself go down.
- **Reports need no network to render.** Roll-ups, the trend strip, SLO status, and the status page are all generated from the local JSONL history, so producing a report makes no network call — the checker only touches the network when it probes, never when it reports, and a report can be built even while the monitored endpoints are unreachable.

### Incidents, SLOs, and alerting
- **Page on real outages, not blips.** A single failed probe does not open an incident (the flap guard), and a brief self-healing outage does not page (the sustained-outage gate). Alerting that fires on noise trains people to ignore it.
- **Consecutive failures open an incident, not scattered ones.** The flap guard counts consecutive failures, so an endpoint that fails once an hour all day never opens an incident — only an unbroken run of failures does. Intermittent blips stay visible in the history without ever looking like an outage, and a real outage is a run of failures with no success in between.
- **The outage has to last before it pages.** The sustained-outage gate (`--max-open-minutes`) pages only on an incident that stays open — a failure run that heals within minutes never reaches a pager, even though the flap guard already recorded it as an incident. Opening an incident and paging a person are two different thresholds, so a self-healing blip is a record in the history, not a 3 a.m. wake-up.
- **Paging decisions live in the checker, not a separate alerting layer.** The flap guard and the sustained-outage gate decide when an outage is real, and `check`'s exit code and `--max-open-minutes` carry that decision to cron or a pager — so there is no separate alert manager to configure, keep in sync with the probes, or keep running alongside the checker.
- **Open incidents need no separate store.** An open incident is not a record in an alert database — it is the tail of the history, failures with no later success yet — so `report --fail-open` finds what is still open by reading the same JSONL file the probes write, with no incident table to keep in sync, migrate, or lose.
- **Downtime is priced in error budget.** An outage is not only minutes down — it is error budget consumed against the SLO target (`"slo": 99.9`), so the same history that records an incident also reports what that incident cost: a report answers both how long something was down and how much of the budget it spent.
- **Error budget remaining is headroom, not history.** The SLO report measures error budget consumed so far, and what is left is how much more downtime the target can still absorb — so the same number that records what an outage cost also says whether the next incident can be afforded, and a team can slow risky changes while the budget is thin instead of learning about it after the next outage.
- **An SLO breach is a gate, not a chart.** `report --config` measures each SLO target (`"slo": 99.9`) as error budget consumed so far and met-or-breached status, and `--fail-slo` exits 1 on a breach — so a breached budget stops a pipeline the same way an open incident does, instead of sitting in a dashboard nobody checks.
- **Exit codes as a contract.** `check` exits 1 on any failure, so a cron line doubles as alerting, `report --fail-open` gates CI on open incidents, and `report --fail-slo` exits 1 on an SLO breach. Like the other utilities here, uptimekit fits into automation unchanged — no output parsing required.
- **The record is written before the verdict is acted on.** A probe result is appended to the history first, and only then do the exit code, the flap guard, and the sustained-outage gate act on it — so an alerting decision can never outrun the evidence it is based on, and even a check that crashes right after probing has already left the record behind for the next report.

### The status page
- **Probe to page in one tool.** Probes, history, roll-ups, and the status page all live in uptimekit itself — no separate collector, database, or dashboard service in between — so the path from a check to a published page has no handoff where data can drift or a service can go down.
- **A status page with no JavaScript.** The status-page renderer is self-contained HTML — inline CSS, no JavaScript, fully escaped — so the same probe history becomes a page you can publish without standing anything up, and nothing in it executes in a visitor's browser.
- **A status page that publishes like a static site.** The status page is a single self-contained HTML file — inline CSS, no JavaScript — so it can be published anywhere static files are served, with no server to stand up for the page itself: the same static-first instinct as the association site and the personal site, applied to monitoring output.
- **A status page that stays up when the service is down.** The status page is a single self-contained HTML file, so it can be served from static hosting independent of the endpoints it reports on — the page describing an outage does not go down with the service it describes, and it needs no dashboard service of its own to stay readable during an incident.
- **A status page anyone can read.** The self-contained HTML status page needs no dashboard account or login to view — publish it and anyone can read it, so the people affected by an outage see the same status without needing access to the monitoring setup itself.
- **Untrusted probe content stays inert.** The status-page renderer escapes everything it renders, so content coming back from probed endpoints — URLs, page text, error bodies — is treated as data, never as markup: a hostile or broken endpoint cannot inject anything into the page you publish.
- **The public page and the private report agree.** The status page is generated from the same JSONL history as the availability roll-ups and SLO status reports, so the page the public reads and the report the team acts on can never disagree about what was observed — an outage shown as resolved on the page is resolved in the report too, because both are readings of one record.

### Running it — deployment and use
- **The middle, not the extremes.** Uptime monitoring usually means a hosted service or a full monitoring stack; uptimekit targets the middle — a checker you can run from cron, whose history is a plain file you can read, and whose report is a page you can publish — so answering "is it up?" needs no account, server, or database, and no stack to keep running.
- **No server, no database, no dependencies.** The history is JSONL, the report is HTML, and the only runtime requirement is Python. There is nothing else to install, patch, or keep running — the same simplest-architecture instinct as the static sites and the other standard-library utilities.
- **Cron first, no daemon to keep alive.** The default deployment is a cron line — no long-running service to monitor, restart, or keep patched — and watch mode exists only for hosts without a scheduler, so the checker itself adds nothing new to keep running.
- **A watch mode for hosts without cron.** Where there is no scheduler to run checks on a timer, uptimekit can run continuously in watch mode instead — so a host without cron still gets monitored, with the same probes, history, and incident gating, rather than going unwatched.
- **Watch mode is the same checker, not a second one.** Watch mode runs the same probes, writes the same JSONL history, and applies the same flap guard and sustained-outage gate as a cron invocation — so a host monitored continuously and a host monitored on a schedule produce one kind of record, and the two ways of running it can never disagree about what was observed.
- **Runs anywhere Python runs.** With no dependencies, no server, and no database, the only requirement is a Python installation — so the same checker runs on a laptop, a server, or a minimal host without an install step, a package to fetch, or a runtime to provision.
- **Run it once, by hand, and get an answer.** A single `check` invocation answers "is it up?" immediately — no scheduler, daemon, or setup needed to try it — so the same command cron runs is the one a person runs when investigating, and the checker is as usable interactively as it is automated.
- **A CLI and a library, not just a CLI.** The same probes, history, and reports are available as an importable library as well as a command line, so another script or tool can drive uptimekit directly instead of shelling out and parsing its output.
- **One config for checks and reports.** The same config that defines what to probe also carries the SLO targets that `report --config` measures, so the SLO a report grades is the SLO the probes were checking — there is no second definition of the target to keep in sync with the checks.
- **Tests that run with no network.** The suite runs fully offline, so probes, history, and reports are verified without hitting real endpoints — the tests prove the checker without depending on the very thing it monitors.
- **CI runs the same suite you run.** CI on Python 3.11 runs the same 98 offline unit tests, so the suite that proves the checker on a laptop is the one that gates every change — no separate integration environment, no network in tests, and a change that breaks a probe or a report fails before it lands rather than after it is deployed.
- **Small enough to read end to end.** With no dependencies and only the standard library, the whole checker is source a reader can audit — trusting the monitor does not mean trusting a stack of third-party code you have never read, and a bug in the checker is one you can find by reading it.
- **Nothing to pay for to keep it running.** With no hosted service, no server, and no database, uptimekit has no subscription, no hosting bill, and no service to keep patched — monitoring costs nothing beyond the machine it already runs on, so a small project gets the same answer to "is it up?" as a funded one.

## Worked example: a morning with three services

The commands below are the real uptimekit CLI, taken from the project's own usage docs. One config describes three services, one check records the morning, and every report after that reads the same history — no re-probing, no second store:

```json
[
  {"name": "api", "kind": "http", "url": "https://api.example.com/health",
   "expect_status": 200, "keyword": "ok", "timeout": 5},
  {"name": "postgres", "kind": "tcp", "host": "db.internal", "port": 5432},
  {"name": "web-tls", "kind": "tls", "host": "example.com", "port": 443}
]
```

```bash
python -m uptimekit check --config examples/targets.json
# probe once, record — exits 1 if any target fails, so a cron line
# doubles as an alerting path

python -m uptimekit report --window 24h
# availability roll-up with p50/p95 latency for the last day

python -m uptimekit report --window 7d --trend
# per-day availability strip — monitoring gaps show as gaps,
# not averaged away

python -m uptimekit report --window 24h --compare
# the same window against the previous 24h, so a regression
# reads as a regression, not just a number

python -m uptimekit report --incidents --threshold 2 --fail-open
# gate on open incidents — two consecutive failures open one,
# a single bad probe is noise

python -m uptimekit report --incidents --max-open-minutes 15
# gate on sustained outages only — a self-healing 2-minute blip
# never pages anyone

python -m uptimekit report --config examples/targets.json --fail-slo
# gate on error budgets — exits 1 when an SLO target is breached

python -m uptimekit status-page --out status.html
# the same history as a self-contained HTML status page,
# publishable from any static host

python -m uptimekit watch --config targets.json --interval 300
# probe forever, for hosts without cron

python -m uptimekit compact --keep 30d
# retention — the append-only history stays bounded
```

The same probes, history, and reports are available as an importable library as well as a command line, so another script can drive uptimekit directly instead of shelling out and parsing its output.

## What it demonstrates

Monitoring that respects its own subject matter: a checker you can run from cron, a history that is a plain file you can read, and reports that are generated from that record — so the answer to "is it up?" needs no account, server, or database, and the page describing an outage never goes down with the service it describes.

## Links

- Repo: [midya8/uptimekit](https://github.com/midya8/uptimekit)
