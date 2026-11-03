# uptimekit — case study

Synthetic uptime monitoring and availability reporting in pure Python, no dependencies and no database — if Python is installed, uptimekit runs. CLI plus importable library, 83 unit tests running fully offline, CI on Python 3.11.

## The problem

Uptime monitoring usually means either a hosted service or a monitoring stack: an account, a server, and a database to keep running just to answer "is it up?" uptimekit targets the middle: a checker you can run from cron, whose history is a plain file you can read, and whose report is a page you can publish without standing anything up.

## What it does

Probes cover HTTP (status, keyword-in-body, latency), TCP connect, and TLS certificate expiry. Results go to an append-only JSONL history with atomic retention compaction, so history survives interrupted runs and does not grow without bound.

Availability roll-ups report p50/p95 latency percentiles, a per-day trend strip where monitoring gaps stay visible rather than being smoothed over, and window-over-window comparison. SLO targets (`"slo": 99.9`) are measured by `report --config`: error budget consumed so far and met-or-breached status, with `--fail-slo` exiting 1 on a breach — so an SLO breach gates a pipeline the same way an open incident does. Incident detection uses a consecutive-failure flap guard plus a sustained-outage gate (`--max-open-minutes` pages on real outages, not self-healing blips). A watch mode covers hosts without cron, and a self-contained HTML status-page renderer (inline CSS, no JavaScript, fully escaped) turns the same data into a publishable page.

Latency assertions turn slow into down, and TLS expiry thresholds turn a certificate quietly approaching expiry into a failure while there is still time to act.

## Design decisions

- **No server, no database, no dependencies.** The history is JSONL, the report is HTML, and the only runtime requirement is Python. There is nothing else to install, patch, or keep running — the same simplest-architecture instinct as the static sites and the other standard-library utilities.
- **Gaps stay visible.** The per-day trend strip shows monitoring gaps as gaps. A report that hides missing data overstates availability; an honest strip lets a gap be investigated instead of averaged away.
- **Compare windows, not just snapshots.** Availability roll-ups include a window-over-window comparison, so a report answers whether availability improved or regressed against the previous window instead of presenting one window in isolation.
- **Page on real outages, not blips.** A single failed probe does not open an incident (the flap guard), and a brief self-healing outage does not page (the sustained-outage gate). Alerting that fires on noise trains people to ignore it.
- **A watch mode for hosts without cron.** Where there is no scheduler to run checks on a timer, uptimekit can run continuously in watch mode instead — so a host without cron still gets monitored, with the same probes, history, and incident gating, rather than going unwatched.
- **Slow is down.** A latency assertion converts a degraded endpoint into a failure, and a TLS expiry threshold converts an expiring certificate into one, instead of leaving both as warnings nobody acts on.
- **Exit codes as a contract.** `check` exits 1 on any failure, so a cron line doubles as alerting, `report --fail-open` gates CI on open incidents, and `report --fail-slo` exits 1 on an SLO breach. Like the other utilities here, uptimekit fits into automation unchanged — no output parsing required.
- **An SLO breach is a gate, not a chart.** `report --config` measures each SLO target (`"slo": 99.9`) as error budget consumed so far and met-or-breached status, and `--fail-slo` exits 1 on a breach — so a breached budget stops a pipeline the same way an open incident does, instead of sitting in a dashboard nobody checks.
- **Reports as outputs.** The availability roll-ups, the trend strip, SLO status reports (error budget consumed, met-or-breached status), and the HTML status page are what the tool produces, not a separate chore after running it.

## Links

- Repo: [midya8/uptimekit](https://github.com/midya8/uptimekit)
