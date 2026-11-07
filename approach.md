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
- [sre-toolkit](projects/sre-toolkit.md), [loglens](projects/loglens.md), [flowkit](projects/flowkit.md), [uptimekit](projects/uptimekit.md)
- [Personal site — midya.ca](projects/midya-ca.md)

## One tool, one job

There are four Python utilities here, not one, because each one does a
different job: sre-toolkit does the SRE math and the documents around an
incident, loglens reads access logs, flowkit runs a DAG of shell commands,
and uptimekit probes endpoints and keeps the history. None of them imports
another, and none of them grows a second job — a new need becomes a new
small tool rather than a new mode on an old one. They still work together,
because they share conventions rather than code: every one is
standard-library only, every one is both a command and an importable
library, every one reports through exit codes and text or JSON reports,
and every one writes its documents as Markdown. A shell script — or a
flowkit flow — can chain them without any of them knowing about the
others. The web side follows the same split: the association site and the
personal site are separate repositories, separate builds, and separate
hosts, each doing exactly its own job.

- [sre-toolkit](projects/sre-toolkit.md), [loglens](projects/loglens.md), [flowkit](projects/flowkit.md), [uptimekit](projects/uptimekit.md)
- [Kurdistan International Sociological Association website](projects/kurdistansociology-website.md)
- [Personal site — midya.ca](projects/midya-ca.md)

## Make tools that fit scripts as well as terminals

A tool that only works interactively is half a tool. Every Python utility
here is both a command you run by hand and a library you import into
automation, and every command communicates its result through its exit
code: sre-toolkit exits 1 when an error budget is exhausted, loglens exits
1 when a 5xx rate breaches a threshold, and flowkit uses 0 for success, 1
for a failed step, and 2 for an invalid flow file. uptimekit's `check`
exits 1 on any failure, so a cron line doubles as alerting,
`report --fail-open` gates CI on open incidents, and
`report --fail-slo` exits 1 on an SLO breach, so a breached error
budget gates a pipeline the same way an open incident does. A pipeline or scheduled
check can act on the result without parsing human-readable output.

## Prefer a scheduled check over a service to keep alive

Nothing here runs as a daemon, because a daemon is a second system to
keep alive, watch, and restart — and its own failures are the ones nobody
notices. Every Python utility is a one-shot command: uptimekit's `check`
exits 1 on any failure, so a cron line doubles as alerting, and
`report --fail-open` and `report --fail-slo` gate a pipeline the same way;
flowkit flows, loglens analyses, and sre-toolkit reports all run the same
way, on demand or on a schedule, and then exit. There is no process to
babysit, no port to watch, and no state held in memory that can go stale —
the record on disk is the state. The one exception proves the rule:
uptimekit ships a watch mode for hosts without cron, but it is the
fallback, not the default.

- [uptimekit](projects/uptimekit.md), [flowkit](projects/flowkit.md), [sre-toolkit](projects/sre-toolkit.md), [loglens](projects/loglens.md)

## Make automation runnable by hand

There is no automation-only mode here, and no hidden path the schedule
takes that a person cannot. Every scheduled check is an ordinary command:
uptimekit's `check` is the same invocation whether cron runs it or a
person types it at 3 a.m., and it answers the same way either time — exit
1 on any failure. When the schedule misbehaves, debugging it is running
the command yourself and reading the same output the schedule saw, not
reconstructing what some service did behind a dashboard. And where the
action would have consequences, the command can be previewed first:
flowkit's `--dry-run` validates the flow and prints the plan without
executing anything, so what the nightly run would do is visible before it
does it. Nothing about the automation is special except that something
else typed the command — and that is the point: a check a person cannot
run by hand is a check nobody can fix when it breaks.

- [uptimekit](projects/uptimekit.md), [flowkit](projects/flowkit.md), [sre-toolkit](projects/sre-toolkit.md), [loglens](projects/loglens.md)

## Validate before executing

A bad input should fail loudly before anything happens, not halfway
through. flowkit rejects duplicate step names, dangling dependencies,
cycles, unknown keys, and malformed interpolation before running a single
step, and its `--strict-env` check fails up front on any unset variable
reference instead of letting a blank value silently change a command. The
same instinct shows up in loglens, where filters scope every statistic, so
narrowing to a failing slice never leaves stray numbers computed over the
full log. uptimekit applies the same instinct to monitoring: a latency
assertion turns a slow endpoint into a failure, and a TLS expiry threshold
turns a certificate quietly approaching expiry into one, instead of leaving
both as warnings nobody acts on.

## Show the plan before you run it

Validation says the input is well-formed; a dry run says what would actually
happen. flowkit's `--dry-run` validates the flow and prints the plan — the
steps in order, the `--only` / `--skip` selection, the `when` conditions
annotated, the hooks listed under their own end-of-run heading — without
executing anything, and it exits 0 when the plan validates, so a pipeline
can gate on the review itself. The point is that the run that changes state
is reviewable before it is real: a step that should have been skipped, a
condition evaluating the wrong way, a dependency pointing where it
shouldn't — all of it is visible in the plan, where it costs nothing,
instead of in the run, where it costs the thing the run was supposed to do.
A tool that only offers run-or-nothing forces its operator to trust the
input sight unseen; a tool that can show its plan lets the operator check
the work before the work happens.

- [flowkit](projects/flowkit.md)

## Fail closed, not open

When a tool cannot answer the question it was asked, the safe default is
to fail — not to pass quietly and let the pipeline carry on. flowkit
refuses to run a flow it cannot validate: an invalid flow file exits 2,
before a single step executes, rather than running a broken definition
and hoping for the best. loglens's `--min-apdex` gate fails a log with no
durations instead of passing it unmeasured, because a gate that passes
what it cannot measure is not a gate. uptimekit's `report --fail-open`
gates CI on any open incident and `--fail-slo` exits 1 on a breached SLO,
so an outage nobody has closed keeps failing the pipeline until a success
closes it. sre-toolkit's budget command exits 1 when the error budget is
exhausted, and `metrics --action-items` exits 1 when postmortem items go
stale — unfinished work cannot quietly age out of sight. In each case the
tool would rather stop the pipeline, or refuse to run, than report "fine"
about something it has not actually checked. A false alarm costs a look;
a false all-clear costs the incident nobody saw coming.

- [flowkit](projects/flowkit.md), [loglens](projects/loglens.md), [uptimekit](projects/uptimekit.md), [sre-toolkit](projects/sre-toolkit.md)

## Prefer explicit over implicit

A default nobody chose is a decision nobody made. flowkit interpolates
environment variables into commands only from declared, layered values,
and its `--strict-env` check fails up front on any unset reference instead
of letting a blank value silently rewrite a command. sre-toolkit's triage
maps services to owning teams with an explicit default owner, so every
alert has a named owner and none falls through to nobody. uptimekit
measures SLOs against a target declared in the config (`"slo": 99.9`), so
met-or-breached is a measurement against a stated number, not a feeling.
Where a value matters — who owns it, what the target is, what the
environment holds — it is written down where the tool can see it, not left
to whatever happens to be in scope.

- [flowkit](projects/flowkit.md), [sre-toolkit](projects/sre-toolkit.md), [uptimekit](projects/uptimekit.md)

## Make the default the safe choice

A tool is mostly used the way it ships — with its defaults, in a hurry,
by someone who has not read the manual. So the defaults here are chosen
to be the safe ones, not the convenient ones. loglens detects the log
format per line, with `--format auto` the default, so the tool adapts to
the log instead of assuming a format and silently misreading the lines
that do not match. uptimekit's default deployment is a cron line, not a
daemon — nothing to keep alive, restart, or patch — and watch mode
exists only for hosts without a scheduler, so the fallback is the
exception, not the shape of the tool. sre-toolkit's triage routes every
alert to a named owner with an explicit default owner, so the alert that
matches no rule still lands with someone instead of falling through to
nobody. The personal site applies the same instinct to its visitors: a
visitor who prefers reduced motion gets a single static frame of the
galaxy without asking, because the respectful rendering is the default
one, not a setting to discover.

The point is that a default is a decision made on the user's behalf, and
the user never gets to review it. A default that assumes, that keeps
something running, or that drops the awkward case is a decision the tool
made quietly and the user inherits loudly, usually at 3 a.m. Make the
default the thing you would choose if you were standing next to the
person using it — detect instead of assume, schedule instead of serve,
route instead of drop, respect instead of animate — and leave the
riskier choices as flags the user has to reach for on purpose, knowing
what they are reaching for.

- [loglens](projects/loglens.md), [uptimekit](projects/uptimekit.md), [sre-toolkit](projects/sre-toolkit.md), [Personal site — midya.ca](projects/midya-ca.md)

## Put the policy in a file

The decisions these tools enforce — what counts as a breach, who owns an
alert, what a flow does — live in files, not in settings somebody clicked
once and nobody can review. sre-toolkit's SLO definitions are Markdown or
JSON files, so the target and the window are written down where a pull
request can see them, and its triage rules come from custom rule files, so
the policy that shapes the board is versioned with the code that enforces
it instead of re-typed as flags each run. flowkit's flows are JSON files:
steps, dependencies, retries, and environment in one definition that can
be diffed, so a change to the nightly ETL is a change to a file, reviewed
like any other. uptimekit's targets and SLO target (`"slo": 99.9`) live in
config, and the history the reports derive from is a file on disk. Even
the policy a tool suggests arrives as a file to adopt: sre-toolkit's
`burn --suggest` emits the standard three-tier multi-window policy for a
human to take, it does not install one. The web side follows the same
instinct: the association site's news posts are Markdown files, so
publishing is editing a file — versioned with the site, reviewable in a
pull request, rendered by the same build as everything else. A decision
that lives in a file can be reviewed, reverted, and carried to the next
machine; a decision that lives in a setting can only be remembered — and
remembered settings are how a working setup quietly becomes an
undocumented one.

- [sre-toolkit](projects/sre-toolkit.md), [flowkit](projects/flowkit.md), [uptimekit](projects/uptimekit.md)
- [Kurdistan International Sociological Association website](projects/kurdistansociology-website.md)

## Describe the work in data, not in code

A tool should not make you learn its language before it will do its job.
flowkit's flows are JSON files: steps, dependencies, retries, and
environment in one definition you can read in a single file — the shell
commands inside are the work, the JSON is only the shape around them, and
there is no scripting language to learn or debug. loglens needs no query
language: nobody should have to remember `awk` incantations during an
incident, so a log file you already have becomes a one-screen summary in
a single command. uptimekit's endpoints are configuration, not code — what
to probe, and with which thresholds, lives in a file, so adding an
endpoint means editing a file, not changing the checker, and the same tool
monitors one site or twenty without a code change. sre-toolkit's triage
rules come from rule files and its SLO definitions are Markdown or JSON,
so the policy is data the tool reads, not code it runs. Data can be read,
diffed, and handed to someone who has never used the tool; a language has
to be learned first, and during an incident that learning is the work that
stands between you and the answer.

- [flowkit](projects/flowkit.md), [loglens](projects/loglens.md), [uptimekit](projects/uptimekit.md), [sre-toolkit](projects/sre-toolkit.md)

## Prefer a file to a form

Wherever something needs to be created, configured, or changed, it lives
in a file you can read — not behind a form that hides the change. The
association site publishes news by adding a Markdown file with
frontmatter, one per locale, so a post is versioned with the site,
reviewable in a pull request, and rendered by the same build as
everything else; there is no admin panel to log into and no database row
to write, and the UI text lives in per-locale JSON dictionaries for the
same reason. flowkit's flows are JSON files, uptimekit's endpoints and
SLO targets live in one config file, and sre-toolkit's triage rules and
SLO definitions are files the tools read rather than screens they show.
loglens needs nothing set up at all: the log file you already have is
the input. A file can be diffed, reviewed, reverted, and changed with
the same tools as the code around it; a form hides the change behind a
login and leaves no reviewable trace. Files are also what let these
tools compose — a file one tool writes is a file the next tool can read.

- [Kurdistan International Sociological Association website](projects/kurdistansociology-website.md)
- [flowkit](projects/flowkit.md), [uptimekit](projects/uptimekit.md), [sre-toolkit](projects/sre-toolkit.md), [loglens](projects/loglens.md)

## Test the behaviour you depend on

These tools are meant to be trusted at 3 a.m. — the exit code that gates a
pipeline, the burn-rate rule that pages, the triage board that ranks the
noisiest alert first. That trust is pinned down by tests, not by hope:
sre-toolkit's 254 unit tests cover the budget math (including boundary and
validation cases), severity classification, dedupe and ordering, silence
validation and expiry, burn-rate rules, and time-series replay; loglens's
241 cover parsing (both formats, mixed files, corrupt lines), statistics,
timeline bucketing and spike windows, filters, before/after comparisons,
and every CLI flag including the exit-code gates; flowkit's 123 cover flow
validation, topological ordering, retries, timeouts, skip and fail-fast
semantics, and end-phase hook execution; and uptimekit's 98 run fully
offline — probe behaviour verified against loopback HTTP/TCP servers, TLS
paths against injected certificates, and CLI tests that mock the probe
engine, so the suite never touches the network it exists to monitor. CI
runs the same suite on every change — Python 3.10–3.13 for sre-toolkit,
loglens, and flowkit, and Python 3.11 for uptimekit — so the tests that
prove a tool on a laptop are the ones that gate it before it lands.

- [sre-toolkit](projects/sre-toolkit.md), [loglens](projects/loglens.md), [flowkit](projects/flowkit.md), [uptimekit](projects/uptimekit.md)

## Test the bad input, not just the good path

A test suite that only runs the happy path proves the tool works when
everything is already fine — which is the one situation that never needs
proving. The suites here spend their effort on the input the incident
actually brings. loglens's 241 tests cover parsing both formats, mixed
files, and corrupt lines, and the tool itself treats an unparseable line
as a skip, not a fatal error, so a damaged line never costs the analysis
of the thousands of good ones around it. flowkit's 123 cover the flow
file that is wrong on purpose — duplicate step names, dangling
dependencies, cycles, malformed interpolation — rejected before a single
step runs — and retries and timeouts, so a flaky step gets another
chance and a hung step fails instead of stalling the flow. sre-toolkit's
254 include boundary and validation cases for the budget math, and
`burn --replay` tests a policy against a past incident's time series
before it pages anyone. uptimekit's 98 run fully offline, with probe
behaviour verified against loopback HTTP/TCP servers and TLS paths
against injected certificates, so the suite proves the checker without
depending on the very thing it monitors.

The point is that the failure modes are the behaviour you depend on: the
gate that must fail closed, the parser that must not choke, the retry
that must not run forever. Testing the good path proves the tool can do
its job; testing the bad input proves it still does its job when the
world does not cooperate — and the world not cooperating is the whole
reason the tool exists.

- [loglens](projects/loglens.md), [flowkit](projects/flowkit.md), [sre-toolkit](projects/sre-toolkit.md), [uptimekit](projects/uptimekit.md)

## Let reports and documents be outputs, not afterthoughts

The analysis tools generate the documents the workflow runs on, in formats
that can be committed, reviewed, and searched: SLO definitions, status
reports with budget-exhaustion projections, and postmortems with automatic
response metrics from sre-toolkit; Markdown incident reports with per-path
breakdowns and spike windows from loglens; text or JSON run reports with
captured output tails from flowkit; and availability roll-ups with p50/p95
latency percentiles, a per-day trend strip where monitoring gaps stay
visible, SLO status reports (error budget consumed, met-or-breached
status), and a self-contained HTML status page from uptimekit. The report is not a separate chore
after the work — it is what the tool produces.

## Make the same answer readable by people and by machines

A report written for a person should stay written for a person — no
mangled text that a script has to scrape. So every tool offers the same
result in two shapes: the human one by default, and JSON on request.
loglens's `--json` emits the whole summary — counts, rates, top-N,
latency, timeline — for dashboards and scripts to consume without parsing
prose; sre-toolkit's `budget` and `downtime` emit `--json` for pipelines,
postmortem response metrics are available as `--json`, and `metrics
--json` feeds MTTR to dashboards; flowkit's `--json` summary and
`--report` JSON file carry the same run report, including an `output`
field per step; uptimekit's `check --json` gives a machine-readable
verdict, and its JSONL history is the same record every report is derived
from. The two shapes carry the same data — the JSON is not a different
answer, just the same answer in a shape a tool can consume. When a
pipeline needs a number it asks for JSON; when a person needs to
understand, they read the text — and neither has to parse the other's
format.

- [loglens](projects/loglens.md), [sre-toolkit](projects/sre-toolkit.md), [flowkit](projects/flowkit.md), [uptimekit](projects/uptimekit.md)

## One record, many views

Every view of the same work should come from the same record, so two
answers about the same thing cannot disagree. uptimekit keeps one
append-only JSONL history and derives the roll-ups, the SLO reports, and
the public status page from it — the page the public reads and the report
the team acts on are generated from the same file, so they can never drift
apart. loglens does the same with a log file: the summary, the timeline,
the per-path tables, and the Markdown incident report are all computed
from the same parsed records, and `--json` emits that same summary for
tooling to consume. sre-toolkit's incident files feed the postmortem, the
MTTR aggregation, and the fleet roll-ups from one set of records, and a
single flowkit definition produces both the dry-run plan and the run
report. On the web side, the association site's news posts are Markdown
files rendered by the same build into every locale's pages, and the
personal site keeps all of its copy in one data file, separate from the
scene and the components. When there is one record, there is nothing to
keep in sync — and nothing to go stale.

- [uptimekit](projects/uptimekit.md), [loglens](projects/loglens.md), [sre-toolkit](projects/sre-toolkit.md), [flowkit](projects/flowkit.md)
- [Kurdistan International Sociological Association website](projects/kurdistansociology-website.md)
- [Personal site — midya.ca](projects/midya-ca.md)

## Prefer plain text for the record

Every record these tools keep is a file you can open in any editor:
uptimekit's history is append-only JSONL, flowkit's flows and run reports
are JSON and plain text, sre-toolkit's incidents, postmortems, and SLO
definitions are Markdown, and loglens's summaries can be emitted as JSON
for tooling to consume. There is no database to query, no binary state to
decode, and nothing that requires the tool itself to read back what it
wrote. That makes the record greppable, diffable, and committable with the
tools that already exist — the history of a service can be reviewed in a
pull request the same way code is, and a run report can be opened years
later with nothing installed. On the web side the same instinct holds: the
association site's content is Markdown files, and the personal site's copy
lives in one data file, so the words are editable without touching the code
that renders them.

- [uptimekit](projects/uptimekit.md), [flowkit](projects/flowkit.md), [sre-toolkit](projects/sre-toolkit.md), [loglens](projects/loglens.md)
- [Kurdistan International Sociological Association website](projects/kurdistansociology-website.md)
- [Personal site — midya.ca](projects/midya-ca.md)

## Make the same input give the same answer

A tool that gives a different answer each time it is asked is a tool you
cannot reason about, so these tools are built to be reproducible. flowkit
runs steps in deterministic topological order, with declaration order
breaking ties, so the same flow reports the same way run to run even when
steps run in parallel. uptimekit derives every roll-up, SLO report, and
status page from the one append-only history, so the same history always
produces the same report — re-running yesterday's report gives
yesterday's numbers, not a fresh interpretation of them. loglens computes
every view from the same parsed records, and its before/after comparisons
run the same statistics over two slices of one log, so a change in the
numbers means a change in the traffic, not in the tool. sre-toolkit's
burn-rate rules are checked against recorded time series, so a rule that
fires today would have fired on the same data yesterday. The web side
follows the same rule: both sites are static builds from files, so the
same content produces the same site. When the answer changes, the change
is in the world the tool is measuring — and that is the only change worth
investigating.

- [flowkit](projects/flowkit.md), [uptimekit](projects/uptimekit.md), [loglens](projects/loglens.md), [sre-toolkit](projects/sre-toolkit.md)
- [Kurdistan International Sociological Association website](projects/kurdistansociology-website.md)
- [Personal site — midya.ca](projects/midya-ca.md)

## Make work resumable

Work that cannot be picked up where it stopped gets redone from the
beginning — and redone work gets done differently the second time. These
tools keep the state that lets a run resume instead of restart. flowkit's
`--only` / `--skip` reruns a named subset — the steps plus their
transitive dependencies, or everything else — without editing the flow
file, so a failed nightly ETL is rerun from the step that failed, not
from the extract that already succeeded. uptimekit's history is
append-only, so monitoring resumes from the record on disk: a report
re-derived after an outage covers the whole window, including the gap,
and nothing is lost because the process stopped. sre-toolkit keeps
incidents and postmortems as files, so an open action item is still there
with its days-since-resolution count the next time anyone looks, and
`metrics --action-items` exits 1 when items go stale past `--stale-days`,
so unfinished work cannot quietly age out of sight. The record is the
resume point: nothing depends on a process still running, or on anyone
remembering where it stopped.

- [flowkit](projects/flowkit.md), [uptimekit](projects/uptimekit.md), [sre-toolkit](projects/sre-toolkit.md)

## Record the when, not just the what

A result without its time is a fact without its context: it cannot say
when something started, whether it is getting better, or whether a change
made it worse. These tools record time with the observation, so the same
record answers questions about a window, not just about a moment.
uptimekit keeps every probe result in its append-only history, so roll-ups,
the per-day trend strip, and SLO reports can be derived for any window —
and compared window-over-window, so a report says whether availability
improved or regressed, not just what it is now. loglens buckets requests
per minute with `--timeline`, so an incident's start is visible, and
`--split-at` compares the windows either side of a deploy, so "did this
release make things worse?" is a measurement, not a guess. sre-toolkit
replays burn-rate rules against timestamped buckets with `burn --replay`,
so a policy is tested against a past incident before it pages anyone, and
its MTTR aggregation includes a weekly trend view, so "are we getting
faster?" is answered over time. flowkit's run reports carry each step's
captured output tail, so a run stays readable after it finishes. When time
is in the record, the question "when did this change?" has an answer in
the data — not in someone's memory of the night it happened.

- [uptimekit](projects/uptimekit.md), [loglens](projects/loglens.md), [sre-toolkit](projects/sre-toolkit.md), [flowkit](projects/flowkit.md)

## Reduce noise; answer the question first

Incident tooling fails when it adds to the wall of symptoms. sre-toolkit's
triage dedupes repeat alerts, keeps each alert's fire count so frequency
stays visible, and inhibits lower-severity symptoms while a critical is
active, so an incident surfaces as one problem to solve. loglens leads
with the headline answers — error rate, status distribution, hottest
failing paths, and the source IPs behind 5xxs — and only then narrows
into timelines, latency tables, and per-client breakdowns. uptimekit
applies the same discipline to paging: a consecutive-failure flap guard
and a sustained-outage gate mean a self-healing blip does not page, so
an alert still means something worth acting on.

- [sre-toolkit](projects/sre-toolkit.md), [loglens](projects/loglens.md), [uptimekit](projects/uptimekit.md)

## Put the worst thing at the top

A report's order is a decision about where attention goes, so these
tools sort by what needs attention, not by what arrived first.
sre-toolkit's status reports sort worst-first, triage ranks by severity,
`--top-talkers` leads with the noisiest alerts, and `--by-owner` rolls
the board up per team, worst severity first — the first thing on the
board is the thing that needs attention first, and nobody has to scan
past healthy services to find the one that is burning. loglens does the
same with traffic: the per-path Apdex table runs worst-first, so the
endpoint dragging the score down leads; `--path-status` ranks the failing
endpoints worst-first with their per-status-code counts; `--by-path`
ranks endpoints by error count, and `--vs` ranks the paths carrying the
biggest error-count increases as regressions. Sorting by arrival order or
alphabet would be a decision to make the reader do the ranking
themselves — and at 3 a.m., the reader should not have to.

- [sre-toolkit](projects/sre-toolkit.md), [loglens](projects/loglens.md)

## Make different failures look different

A single word — "down", "failed", "error" — hides the diagnosis. These
tools keep failure kinds apart, so the first question after an alert is
already partly answered. uptimekit records a refused connection, a wrong
keyword in the body, a slow response, and a certificate near expiry as
different failures, not just as "down". loglens separates status classes
and pivots per path and per status code, so a spike reads as 502s from one
upstream rather than as a generic error rate, and the methods, agents, and
referers behind the 5xxs say whether it is a bot or real users.
sre-toolkit classifies alerts by severity, ranks triage worst-first, and
reports MTTR per severity, so a critical and a warning never look the same
on the board. flowkit makes the same distinction at the shell: exit code 2
means the flow itself is invalid, 1 means a step failed. When every
failure looks the same, every failure gets the same response — and the
wrong one, half the time.

- [uptimekit](projects/uptimekit.md), [loglens](projects/loglens.md), [sre-toolkit](projects/sre-toolkit.md), [flowkit](projects/flowkit.md)

## Prefer a number to an adjective

"Healthy", "slow", "degraded" — an adjective is a report that cannot be
argued with, because there is nothing to check it against. These tools
report health as a measured number instead, so two people looking at the
same system get the same answer, and a change in the number is a change in
the world. loglens scores user experience as an Apdex number at a stated
threshold — satisfied, tolerating, frustrated — and `--min-apdex 0.94`
turns it into a gate a pipeline can fail on; its latency tables report
p50/p95/p99, not averages, so a slow tail stays visible instead of being
averaged away by mostly fast requests. uptimekit's roll-ups report p50/p95
latency percentiles, and its SLO report states the error budget consumed
and met-or-breached against the declared 99.9 target, so "is it getting
worse?" is a comparison of two numbers, not two impressions.
sre-toolkit's budget command projects when the error budget runs out and
how many bad events remain, its burn-rate rules fire on measured rates over
two windows, and MTTR is reported as mean, median, and p90 per severity
with a weekly trend view, so "are we getting faster?" has numbers to point
at. A number can be wrong — and then it can be checked, argued with, and
fixed. An adjective can only be believed.

- [loglens](projects/loglens.md), [uptimekit](projects/uptimekit.md), [sre-toolkit](projects/sre-toolkit.md)

## Don't claim what you didn't observe

A report is only as honest as the observations behind it, and these tools
refuse to fill in the blanks. uptimekit never credits an endpoint with
uptime it did not observe: a period with no probe results produces no
success records, so the per-day trend strip shows a gap rather than a
green stretch the checker never actually saw — the report never rewards
the checker for time it was not running. loglens does the same with messy
input: a line it cannot parse is skipped, not guessed at, so a damaged
line never costs the analysis of the thousands of good ones around it and
never becomes a made-up data point either. sre-toolkit's burn-rate rules
are evaluated against the recorded time series — `burn --replay`
re-evaluates every rule at each timestamped bucket and reports each firing
interval — so an alerting policy is tested against a past incident that
actually happened, not against a scenario somebody imagined. The
discipline is the same in each case: the record says what was seen, and
what was not seen stays visibly absent instead of being smoothed over
into a reassuring answer.

- [uptimekit](projects/uptimekit.md), [loglens](projects/loglens.md), [sre-toolkit](projects/sre-toolkit.md)

## One observation is not a signal

A single bad reading is not evidence — it is a reading. These tools act
only when the pattern holds across more than one observation, because the
cost of acting on noise is an alert nobody trusts and a gate that fails
for nothing. uptimekit's flap guard counts consecutive failures, so one
failed probe never opens an incident — an endpoint failing once an hour
all day never looks like an outage — and the sustained-outage gate pages
only on an incident that stays open, so a blip that heals within minutes
is a record in the history, not a 3 a.m. wake-up. sre-toolkit's burn-rate
rules fire on measured rates over two windows — a fast burn over a short
window and a slow bleed over a long one — so one bad minute is not enough
to page, and `burn --replay` tests a policy against a past incident's time
series before it pages anyone. loglens's spike buckets flag only when both
the error rate and the count clear a threshold, so a single error in a
quiet minute never reads as a spike. flowkit gives a flaky step another
chance — `retries: 2` means at most three attempts — before the run is
declared failed. In each case the tool waits for the pattern to confirm
itself, and what it records in the meantime stays visible: the failed
probe is in the history, the single error is in the log, the first failed
attempt is in the run report. Waiting is not ignoring — it is refusing to
mistake one data point for a conclusion.

- [uptimekit](projects/uptimekit.md), [sre-toolkit](projects/sre-toolkit.md), [loglens](projects/loglens.md), [flowkit](projects/flowkit.md)

## Compare against a baseline, not against nothing

A number on its own is a fact without a verdict. An error rate of 2%
means nothing until you know what it was before the deploy; an
availability of 99.8% means nothing until you know what the last window
looked like. So these tools always answer against something real, never
in isolation. loglens compares the windows on either side of a deploy —
`--split-at` reports the error-rate delta, the newly failing paths, and
the paths that recovered — and `--vs baseline.log` answers "did this
release make things worse?" across two whole logs, ranking the paths
with the biggest error-count increases as regressions. uptimekit's
roll-ups carry a window-over-window comparison, so a report says whether
availability improved or regressed against the previous window instead
of presenting one window alone. sre-toolkit tests a policy the same way:
`burn --replay` re-evaluates every rule at each timestamped bucket of a
past incident's time series and reports each firing interval, so an
alerting policy is judged against an incident that actually happened
before it pages anyone.

The baseline has to be real — recorded history, not an imagined normal.
A comparison against a made-up target flatters the present just as
surely as a number with no context at all. But with a real baseline the
question changes from "what is the number?" to "worse than what?" — and
that is the question that decides whether anything needs doing. A tool
that only reports the moment can tell you something happened; a tool
that compares it with what came before can tell you whether it matters.

- [loglens](projects/loglens.md), [uptimekit](projects/uptimekit.md), [sre-toolkit](projects/sre-toolkit.md)

## Automate the check, not the judgement

These tools are built to answer the question, not to act on the answer —
the judgement stays with the person reading the report. sre-toolkit's
`burn --suggest` emits a policy for a human to adopt, it does not install
one; triage ranks the board and routes each alert to a named owner, so the
triaged list is an assignment list, not an auto-resolution. loglens's
`--vs` ranks the paths carrying the biggest error-count increases as
regressions and `--split-at` answers "did this release make things
worse?" — but neither rolls anything back; `--errors` lists the exact
failing requests, so a person can follow the spike to its cause in one
step. uptimekit's gates stop a pipeline, and the sustained-outage gate
pages a person — the tool escalates to a human, it never resolves the
incident itself, and the incident stays open on the record until a success
closes it. flowkit's `--dry-run` prints the plan for review before
anything executes, and its exit code says whether the flow succeeded so a
pipeline — or a person — can act on the result. The web side follows the
same split: the association site's deploy is a push to `main`, so the
thing that is reviewed in a pull request is the thing that goes live — the
build renders it, a person decides when. A tool that acts on its own
conclusions hides the decision from the person who owns it; a tool that
reports clearly and stops there keeps the judgement where it belongs —
with someone who can see the context the tool cannot.

- [sre-toolkit](projects/sre-toolkit.md), [loglens](projects/loglens.md), [uptimekit](projects/uptimekit.md), [flowkit](projects/flowkit.md)
- [Kurdistan International Sociological Association website](projects/kurdistansociology-website.md)

## Put an expiry on every exception

Every tool here has a way to hold something back — a silence, a retry, a
flap guard, a gate that waits — and every one of those holds is bounded,
because a suppression with no expiry is a problem that stops existing on
paper while it keeps happening in the world. sre-toolkit's silences are
bounded, reasoned, and expiring: matched on service, severity, or summary
text, and the alerts they match move into a visible silenced section
rather than disappearing, so an alert that is still firing when the
silence ends comes back to the board instead of staying hidden. flowkit
bounds its retries — `retries: 2` means at most three attempts, with the
backoff doubling each time — and a timeout is a failed attempt that still
consumes a retry, so a step that cannot finish does not get retried
forever on the hope that it eventually will. uptimekit's flap guard needs
consecutive failures before an incident opens, and its sustained-outage
gate only pages once the outage has lasted — but the incident stays open
on the record until a success closes it, and `report --fail-open` keeps
gating CI on it in the meantime. The pattern is the same in each case:
the tool is allowed to wait, to retry, to stay quiet for a while — and
the waiting always has a limit, after which the problem is visible again
whether anyone remembered it or not.

- [sre-toolkit](projects/sre-toolkit.md), [flowkit](projects/flowkit.md), [uptimekit](projects/uptimekit.md)

## Bound the history you keep

A record that grows without bound is a second problem waiting to happen —
a disk that fills, a report that slows, a history nobody can move. The
answer is not to delete the past, and not to keep all of it forever: it is
to bound the history by a rule declared up front. uptimekit keeps every
probe result in an append-only JSONL history, because roll-ups, trend
strips, and SLO measurement all need the past — and then
`compact --keep 30d` prunes that history to the last thirty days, so a
checker that runs from cron for months needs no manual cleanup and never
grows without bound. Nothing already recorded is rewritten in the
process: results are appended, never edited in place, so pruning removes
old entries without ever altering what remains — and the compaction
rewrites the history atomically, so a crash mid-compaction leaves either
the old file or the new one, never a half-written record. The bound is
part of the design, not a chore left for later: the history stays complete
enough to answer for, small enough to carry — one file, readable with
ordinary text tools, that a fresh install can pick up and continue.

- [uptimekit](projects/uptimekit.md)

## Keep a failure contained

A failure should stop the work that depended on it, and nothing else.
flowkit draws that line with the dependency graph: a failed step skips
its dependents — and theirs — so nothing runs on a result that never
happened, while `continue_on_error` lets the rest of the flow proceed,
and the run's exit code still says the flow failed. The same boundary
holds for the hooks that report the outcome: a broken notification hook
skips only its own hook dependents, never the cleanup step, and fail-fast
is deliberately not applied to hooks, so the failure being reported
cannot silence the report. loglens draws the same line around bad input:
a line it cannot parse is skipped, not fatal, so one damaged line never
costs the analysis of the thousands of good ones around it. uptimekit
draws it around the report itself: the status page is a single
self-contained HTML file served from static hosting, independent of the
endpoints it reports on, so the page describing an outage does not go
down with the service it describes. In each case the tool decides in
advance what a failure is allowed to take with it — its dependents, its
bad line, its own process — and everything outside that boundary keeps
working, so one failure stays one failure instead of becoming a cascade.

- [flowkit](projects/flowkit.md), [loglens](projects/loglens.md), [uptimekit](projects/uptimekit.md)

## Design for the failure mode

A tool that watches something fail should be shaped by the ways that
thing can fail — not by the happy path with error handling added
afterwards. Start by listing the failure modes, then give each one its
own treatment. flowkit does this for shell commands: a step can be
flaky, so it gets bounded retries with backoff that doubles each time;
it can hang, so every attempt has a timeout and a timeout counts as a
failed attempt; it can fail outright, so its dependents are skipped,
and fail-fast stops the rest of the flow while `continue_on_error`
lets the independent steps proceed. uptimekit does the same for
endpoints: a single failed probe is a blip, not an outage, so the flap
guard only opens an incident on consecutive failures; a brief outage
is a record, not a page, so the sustained-outage gate waits for
`--max-open-minutes` before paging; slow is a failure mode of its own,
so a latency assertion turns a slow response into down, and a
certificate near expiry is a failure while there is still time to
renew it. sre-toolkit's burn-rate alerting is built the same way: a
fast burn and a slow bleed are different failure modes, so different
windows catch each one, and both windows must agree before anything
pages — a blip on one window never wakes anyone. When the failure
modes are named up front, the tool's behaviour in each one is a
decision, not an accident — and the operator never has to discover, at
3 a.m., which failure the tool never thought about.

- [flowkit](projects/flowkit.md), [uptimekit](projects/uptimekit.md), [sre-toolkit](projects/sre-toolkit.md)

## Keep the check cheap enough to run often

A check that is expensive to run gets run rarely, and a check run rarely
notices anything in time. So these tools are built to cost almost
nothing per run: standard-library only, no database to start, no daemon
to keep alive, no service to call home to. uptimekit's `check` is one
process that probes its endpoints, appends to the JSONL history, and
exits — cheap enough to run from cron for months, which is what makes a
flap guard and a sustained-outage gate meaningful instead of
theoretical, and there is nothing to pay for to keep it running: no
subscription, no hosting bill, no service to patch. loglens turns a log
file into a one-screen summary in a single command, without standing up
a log pipeline first, and the same command drops into a cron health
check against a fresh log slice. flowkit runs a flow by executing shell
commands — the runner adds validation and ordering, not a scheduler
service to install. sre-toolkit's budget math, burn-rate rules, and
triage run on files on disk — SLO definitions, incident records, rule
files — not on a query against a service that might itself be down. The
same instinct sets the cost of the checks that guard the code: the test
suites run on every change, and uptimekit's 98 tests run fully offline,
so the suite that proves the monitoring tool never waits on the network
it exists to monitor. When the check is cheap, running it often is the
default — and a check that runs often is the one that catches the
problem while it is still small.

- [uptimekit](projects/uptimekit.md), [loglens](projects/loglens.md), [flowkit](projects/flowkit.md), [sre-toolkit](projects/sre-toolkit.md)

## Write down why, not just what

Every project in this portfolio records its decisions, not just its
behaviour. uptimekit's design decisions run to six subsections —
probing, history, reports, incidents and SLOs, the status page, running
it — and each bullet carries its reason with it: a TLS expiry threshold
turns a certificate quietly approaching expiry into a failure while
there is still time to act. flowkit's fifteen decisions are written the
same way, as rules with their reasons attached: validation happens
before execution because a bad flow file should never half-execute.
sre-toolkit and loglens each keep a Decisions section, and both websites
record theirs — the association site's direction-is-layout choice, the
personal site's generated-not-shipped galaxy. The reasoning is the part
that survives: code gets rewritten and defaults get changed, but the
constraint or trade-off behind a choice is what tells a later reader
whether the choice still holds, or whether the world moved and the
decision should move with it. A decision written down can be argued
with, revisited, and reversed on purpose; one that lives only in the
author's head gets re-litigated from scratch — or preserved as cargo
cult, because nobody remembers why it was made. This file is the same
instinct applied once more: the principles here are the reasons,
collected in one place, so the next project starts from them instead of
re-deriving them.

- [sre-toolkit](projects/sre-toolkit.md), [loglens](projects/loglens.md), [flowkit](projects/flowkit.md), [uptimekit](projects/uptimekit.md)
- [Kurdistan International Sociological Association website](projects/kurdistansociology-website.md)
- [Personal site — midya.ca](projects/midya-ca.md)

## Make the first run useful

A tool earns its place by answering its question the first time it is
run, before any setup has been paid for. uptimekit is explicit about
this: a single `check` invocation answers "is it up?" immediately — no
scheduler, daemon, or setup needed to try it — and if Python is
installed, uptimekit runs, with no dependencies, no database, and
nothing to install, patch, or keep running. loglens takes the same
stance toward the incident: a log file you already have is enough,
turned into a one-screen summary in a single command, without learning
a query language or standing up a log pipeline first. sre-toolkit's
`burn --suggest` works the same way for a new service: it emits the
standard three-tier multi-window policy for any SLO window, so the
first alert policy comes from a known-good default instead of a guessed
threshold. flowkit runs a JSON flow file as written — the file is the
whole definition, checked up front and then executed — so the first run
is a real run, not a configuration exercise.

The point is that setup is a cost charged before value, and most tools
charge it up front: accounts, servers, schemas, a query language to
learn. These tools push that cost to zero or near it, because the
moment a tool is most needed — an incident, a new service, a first
check — is the moment nobody has time to configure it. Defaults carry
the knowledge — the standard policy, the sensible probe thresholds — so
the first run is useful and the second run is a refinement, not a
rescue. A tool you can run once, by hand, and get an answer from is a
tool that will actually be there when it matters.

- [uptimekit](projects/uptimekit.md), [loglens](projects/loglens.md), [flowkit](projects/flowkit.md), [sre-toolkit](projects/sre-toolkit.md)

## Detect, don't configure

Every question a tool asks its user is a question the user has to
answer correctly, in the middle of whatever they were doing. The
tools here answer the ones they can answer themselves. loglens never
asks what format a log is in: format detection runs per line, with
`--format auto` the default, so a file that switches between combined
and JSON lines parses both, and the tool adapts to the log instead of
the other way around. midya.ca never asks a visitor to pick a quality
setting: a low, mid, or high rendering profile is chosen from the
device itself — viewport size, device memory, CPU cores, pixel
ratio — and the profile sets the particle budgets, the bloom
strength, and a 40/55/60 fps frame cap. The same instinct covers the
edges: a visitor who prefers reduced motion gets a single static
frame without asking, and if WebGL is unavailable at all, a CSS
gradient takes over so the page still reads.

The point is that configuration is a guess the user makes on the
tool's behalf, and the tool is usually in a better position to know.
A log file declares its own format line by line; a device reports its
own capabilities. Asking the user to restate what the environment
already says adds a step, a chance to be wrong, and a setting to
maintain — and a setting chosen once is a setting that goes stale
when the environment changes. Detection keeps the decision where the
facts are, at the moment the tool runs. The user still gets an
override — loglens accepts `--format` for a single forced format —
because detection is the default, not a cage: the tool guesses first
and lets the human correct it, instead of making the human guess
first and letting the tool correct them.

- [loglens](projects/loglens.md), [midya-ca](projects/midya-ca.md)

## Work without the network

The tools here do their job on the machine they run on, with nothing
to reach out to. uptimekit's reports are generated from the local JSONL
history, so producing a report makes no network call — the checker only
touches the network when it probes, never when it reports, and a report
can be built even while the monitored endpoints are unreachable. Its 98
unit tests run fully offline, so the suite proves the checker without
depending on the very thing it monitors. The other utilities are the
same shape: sre-toolkit, loglens, and flowkit are standard-library-only
Python that read local files and write local output, and the two
websites are static builds with no server behind them — there is no
account to sign into, no API key to rotate, and no hosted service that
has to be up for the tool to work.

That matters most at the moment the tool is needed. An incident tool
that needs the network is a tool that fails exactly when the network is
the problem: the log file is on the disk in front of you, the history
is in a file you can read, and the answer should come from those, not
from a service that may itself be down. Working offline is also what
makes the tools droppable into any environment — a laptop, a server
mid-incident, a minimal host with only Python installed — with no
install step, no package to fetch, and no runtime to provision. The
network is used only where the job itself demands it: uptimekit probes
endpoints because probing is the job. Everything else — the analysis,
the report, the verdict — happens locally, so the tool keeps working
through the outage it exists to describe.

- [uptimekit](projects/uptimekit.md), [sre-toolkit](projects/sre-toolkit.md), [loglens](projects/loglens.md), [flowkit](projects/flowkit.md)
- [Kurdistan International Sociological Association website](projects/kurdistansociology-website.md), [Personal site — midya.ca](projects/midya-ca.md)

## Put the check in the pipeline

A check that only reports is a check that can be ignored. The same
command that investigates an incident should also be the gate that
stops a bad state from shipping, so the check is wired into the
pipeline rather than sitting beside it. uptimekit's `report
--fail-open` gates CI on open incidents, and `--fail-slo` exits 1
when an SLO budget is breached — a breached budget stops a pipeline
the same way an open incident does, instead of sitting in a dashboard
nobody checks. loglens does the same for a deploy: `--min-apdex 0.94`
turns the user-satisfaction score into a pipeline gate, and
`--max-error-rate 0.05` exits 1 when the 5xx rate breaches the
threshold, so the command that investigates an incident also guards
against the next one. flowkit's exit codes are the same contract at
the workflow level — 0 the flow succeeded, 1 a step failed, 2 the
flow file itself is invalid — so a pipeline or cron job can act on
the result without parsing output. sre-toolkit carries it through
every command: meaningful exit codes make each one a scriptable
health gate, and `metrics --action-items` exits 1 when postmortem
items go stale past the threshold.

The point is that a gate is a check with a consequence attached. A
report asks a human to notice; a gate makes the pipeline notice on
its own. That is the difference between a tool that tells you
something is wrong and a tool that stops something wrong from going
out. The checks here are built to be gates from the start — exit
codes, not parsed output — because a check that has to be remembered
will be forgotten, and one that is wired in will run whether or not
anyone is watching.

- [uptimekit](projects/uptimekit.md), [loglens](projects/loglens.md), [flowkit](projects/flowkit.md), [sre-toolkit](projects/sre-toolkit.md)

## Make a failure explain itself

An exit code says something failed. It does not say what, or why — and
a gate that fails without saying why hands the person it pages a second
incident: the investigation. So the verdict and the evidence travel
together, in the same output, in the same place. flowkit prints a failed
step's captured output tail under its report line, so the reason for the
failure is in front of you without opening a log file — and
`--output-dir` keeps the full per-step logs for the whole story. loglens's
`--errors` lists the failing requests themselves — timestamp, client,
method, path, status, duration — so the path from "the rate spiked" to
the exact requests that failed is one flag. sre-toolkit's status reports
carry budget-exhaustion projections: not just that the budget is burning,
but when it runs out and how many bad events remain, which turns a number
into a decision about whether there is room to ship. uptimekit's SLO
report does the same for availability: it states the error budget
consumed against the declared 99.9 target, so "breached" arrives with
the measurement behind it.

The point is that a check's job is not finished when it returns 1. The
person reading the failure at 3 a.m. should not have to re-run the tool,
open a log, or reconstruct what the tool already knew in order to
understand it. If the tool had to look at the evidence to reach its
verdict, it should show the evidence with the verdict — the failing
step's tail, the failing requests, the number behind the breach. A
failure that explains itself gets fixed; a failure that only announces
itself gets investigated first, and fixed later.

- [flowkit](projects/flowkit.md), [loglens](projects/loglens.md), [sre-toolkit](projects/sre-toolkit.md), [uptimekit](projects/uptimekit.md)

## Answer the question, don't just raise the alarm

An alert says something needs attention. It does not say what to do about
it — and a tool that only pages has handed the decision to the person it
woke up. These tools are built to answer the question the person actually
asked, not just to notice that something changed. uptimekit's single
`check` answers "is it up?" right now, and the same history answers how
it has been — roll-ups, trend strip, and SLO status — so one checker gives
both the momentary answer and the longer view. loglens turns a log file
into a one-screen summary that answers "what broke, when, and for whom",
without a query language or a log pipeline first. sre-toolkit's burn-rate
math does not stop at the current rate: its exhaustion projections say
when the budget runs out and how many bad events remain, which turns a
number into a decision — ship, or do reliability work first. flowkit's
reports carry the captured output tails, so the run's report is the record
of what happened, not a pointer to a log somewhere else.

The difference is between a tool that watches and a tool that informs. An
alert is a starting point: it tells you to look. An answer is an ending
point: it tells you what you are looking at, and often what follows from
it. A check that answers its question on the first run — "is it up?",
"what broke?", "how long do we have?" — is a tool you reach for; a check
that only raises the alarm is a tool you learn to ignore, because every
alarm still costs the same investigation. The alarm gets your attention.
The answer earns it back.

- [uptimekit](projects/uptimekit.md), [loglens](projects/loglens.md), [sre-toolkit](projects/sre-toolkit.md), [flowkit](projects/flowkit.md)

## Measure the response, not just the outage

An incident is two things: the failure, and the response to it — and
only the second one is under your control. So these tools measure the
response the same way they measure the system. sre-toolkit's postmortems
carry automatic response metrics, and its MTTR aggregation reports mean,
median, and p90 per severity with a weekly trend view, so "are we getting
faster?" is answered over time, not from a single window's average — a
single fast incident proves nothing, but a trend that moves does. The
follow-through is measured too: `metrics --action-items` groups open
postmortem items per incident with days since resolution, and exits 1
when items go stale past `--stale-days`, so unfinished work cannot
quietly age out of sight — the fix for the incident is itself a gate,
not a list somebody meant to get to. uptimekit keeps the same discipline
on the monitoring side: an incident stays open on the record until a
success closes it, so the outage is not declared over by a silence, and
`report --fail-open` keeps gating CI on it in the meantime.

The point is that an incident ends when the response is measured and
the follow-up is done, not when the alert stops firing. A team that
only measures the outage learns how often things break; a team that
measures the response learns whether it is getting better at fixing
them. The numbers are the same kind in both cases — mean, median, p90,
days since resolution — but they point at the people, not the system,
and the people are the part that can improve. Measure the failure and
you know what happened. Measure the response and you know whether the
next one will go better.

- [sre-toolkit](projects/sre-toolkit.md), [uptimekit](projects/uptimekit.md)

## Don't act on a single failure

A failure is worth recording the moment it happens, but acting on it —
waking someone, opening an incident, failing a step — should cost more
than one bad result. uptimekit records every probe result in its
history, yet a single failed probe does not open an incident: the flap
guard counts consecutive failures, so an endpoint that fails once an
hour all day never looks like an outage, and only an unbroken run of
failures does. Paging costs more still: the sustained-outage gate
(`--max-open-minutes`) pages only on an incident that stays open, so a
failure run that heals within minutes never reaches a pager. Opening an
incident and paging a person are two different thresholds, and a
self-healing blip is a record in the history, not a 3 a.m. wake-up.
sre-toolkit applies the same rule to burn-rate alerting: it fires only
when burn is elevated on both the long and the short window, so a blip
on one window never pages anyone — the pair, not a single threshold,
decides — and `burn --replay` tests a policy against a past incident's
time series before it pages anyone at all. flowkit does it at the step
level: a flaky step gets bounded retries with exponential backoff, and
a timeout is a failed attempt that still consumes a retry, so a hung
step fails instead of stalling the flow — but only after it has had
its chances.

The point is that recording and acting are different decisions, and the
tools keep them apart. Every failure is written down, because the
history is where the pattern shows up later; but the expensive action —
the page, the incident, the failed run — waits for the failure to prove
it is real, by persisting, by agreeing across windows, or by surviving
its retries. An alert that fires on noise trains people to ignore it,
and an ignored alert is worse than no alert at all, because the next
real one arrives to an audience that has already learned not to listen.
Wait for the second failure and you still catch every real outage; the
only thing you lose is the false alarm.

- [uptimekit](projects/uptimekit.md), [sre-toolkit](projects/sre-toolkit.md), [flowkit](projects/flowkit.md)

## Name the command for the job, not the mechanism

The command line is the interface most people will actually meet, so its
words should say what the user wants, not how the tool does it. The
commands here are verbs for the job: `burn` for burn-rate alerting,
`triage` for alert triage, `metrics` for the postmortem numbers, `check`
and `report` for uptimekit. The flags read the same way:
`--max-error-rate` states the line that must not be crossed,
`--min-apdex 0.94` states the satisfaction the traffic must meet,
`--fail-open` and `--fail-slo` say what the gate does when it fails,
`--top-talkers` asks for the noisiest alerts, and `--stale-days` asks
how old an open item may be before it counts as stale. Nothing is named
after its implementation — there is no `--compute-rolling-window` or
`--parse-combined-log` — because the person typing the command is
thinking about the incident, not the algorithm.

That matters most at the moment the tool is used under pressure, when
nobody is reading documentation. A flag whose name states its intent
can be guessed, remembered, and typed correctly the first time; a flag
named after a mechanism has to be looked up, and the lookup happens
while the incident is still open. The same instinct is behind the exit
codes — 0 for success, 1 for a failed step, 2 for an invalid flow —
and behind `--dry-run` printing a plan instead of a trace: the tool
should be readable at the point of use, by the person using it, without
a manual open beside it.

- [sre-toolkit](projects/sre-toolkit.md), [loglens](projects/loglens.md), [flowkit](projects/flowkit.md), [uptimekit](projects/uptimekit.md)

## Degrade in stages, not all at once

A system that only knows two states — working and broken — fails the
moment conditions get worse. The ones here step down instead. The
personal site chooses a low, mid, or high rendering profile from the
device — viewport size, device memory, CPU cores, pixel ratio — and the
profile sets the particle budgets, the bloom strength, and a 40/55/60
fps frame cap, so a weak device gets a lighter galaxy rather than a
stalled page. A visitor who prefers reduced motion gets a single static
frame, rendering pauses while the tab is hidden, and if WebGL is
unavailable at all, a CSS gradient takes over so the page still reads.
uptimekit watches the same slope from the other side: p50/p95 latency
percentiles make a rising slow tail visible before it crosses a latency
assertion and turns into a failure, and a TLS expiry threshold turns a
certificate quietly approaching expiry into a failure while there is
still time to act. flowkit degrades a run the same way: a flaky step
gets bounded retries with backoff — another chance, not an endless one
— a timeout is a failed attempt rather than a stalled flow, and a
failed step skips only its dependents, so the rest of the flow still
runs.

The point is that degradation is a spectrum with room to act in it, and
the design should use that room. A hard cliff turns every bad day into
an outage; a staircase gives the system somewhere to stand while
conditions improve, and gives the people watching it time to respond
before the last step. Step down gracefully, and surface the slope early
— the failure that arrives after a visible decline is a decision made
too late, not a surprise.

- [Personal site — midya.ca](projects/midya-ca.md), [uptimekit](projects/uptimekit.md), [flowkit](projects/flowkit.md)

## Prefer boring technology

Every project here is built on the least surprising thing that does
the job. The four Python tools are standard library only — no
dependencies to install, no third-party package to break when it
changes, nothing to fetch on a machine mid-incident. uptimekit adds no
database and no server to that: its whole state is one JSONL file, its
report is plain HTML, and the checker is small enough to read end to
end, so trusting the monitor never means trusting a stack of code
nobody has read. The two websites make the same choice in a different
shape: both are static builds from files — the association site a
Next.js static export served from Cloudflare, the personal site a Vite
build on App Platform — so there is no server to keep up, no admin
panel, and no database row to write when a news post is published; the
post is a Markdown file, and pushing to main is the deploy.

Boring is not a lack of ambition; it is a budget. Every dependency,
service, and moving part is a future failure mode, a future patch, and
a future thing to explain to the next person. Spend that budget only
where the requirement genuinely needs it, and the system you build is
one a stranger can run, read, and fix — on the first day, and on the
worst day.

- [sre-toolkit](projects/sre-toolkit.md), [uptimekit](projects/uptimekit.md), [flowkit](projects/flowkit.md), [loglens](projects/loglens.md), [Kurdistan International Sociological Association website](projects/kurdistansociology-website.md), [Personal site — midya.ca](projects/midya-ca.md)

## Small enough to read end to end

A tool you cannot read is a tool you have to take on faith — and faith
is the first thing that fails at 3 a.m., when the monitor itself is
suspect and the question is whether the tool is lying to you. So these
tools are kept small enough that a reader can audit the whole thing in
one sitting. uptimekit's checker is standard library only with no
dependencies, and its whole state is one JSONL history file — the
checker is source a reader can audit, so trusting the monitor never
means trusting a stack of third-party code nobody has read, and a bug
in the checker is one you can find by reading it. flowkit's flows are
the same shape at the definition level: the whole run — steps,
dependencies, retries, environment — is one JSON file you can read in
a single file, so the nightly ETL is visible as written rather than
assembled from configuration spread across screens. The websites
follow the same rule for their content: the association site's news
posts are Markdown files, and the personal site keeps all of its copy
in one data file, so the words are readable without the code that
renders them.

The point is that size is a trust decision. A tool with a dependency
tree, a database, and a service behind it can only be trusted through
its documentation and its reputation; a tool small enough to read can
be trusted through its source. That matters most exactly when trust is
scarce — during an incident, on a machine you did not set up, in front
of a result you do not believe. If you can read the whole thing, you
can answer the question "is the tool wrong, or is the world wrong?"
yourself, from the code, instead of guessing. Keep the tool small
enough that the answer is in reach.

- [uptimekit](projects/uptimekit.md), [flowkit](projects/flowkit.md)
- [Kurdistan International Sociological Association website](projects/kurdistansociology-website.md), [Personal site — midya.ca](projects/midya-ca.md)

## Measure from the outside, like a user would

A server that reports itself healthy is not the same as a service a
person can use. The health that matters is the one the user
experiences, so these tools measure from the outside, the way a
visitor would. uptimekit probes endpoints over HTTP — status, content,
and latency — plus TCP connect and TLS expiry, rather than reading
server logs after the fact, so it catches a site that is up for the
server but broken for the people trying to use it; and "up" means the
content is right, not just the status code, so a page that returns 200
with the wrong body still counts as down. The probes only read — they
never write to the service they watch — and nothing is installed on
what is monitored, so the check sees the service the way a visitor
does without becoming another way it can break. loglens measures the
same way from the other side: its Apdex score is one number for how
the traffic felt — satisfied, tolerating, frustrated at a stated
threshold — with a per-path table worst-first, so the endpoint
dragging the experience down leads, and `--min-apdex 0.94` turns that
feeling into a pipeline gate. The personal site applies the same
instinct to rendering: it chooses its low, mid, or high profile from
the visitor's actual device — viewport size, device memory, CPU cores,
pixel ratio — so the experience is judged on the hardware it actually
runs on, not the machine it was built on.

The point is that internal metrics flatter the system that produces
them. A process can be running, a queue can be draining, a dashboard
can be green — and the person on the other end still cannot get their
work done. Measure the thing the user touches, from where the user
stands, and the numbers stop being a report about the system and start
being a report about whether it works.

- [uptimekit](projects/uptimekit.md), [loglens](projects/loglens.md), [Personal site — midya.ca](projects/midya-ca.md)

## Don't let the monitor share the fate of what it monitors

A monitoring tool that goes down with the thing it watches is worse
than no monitor at all: it fails silently at the exact moment you need
it, and the outage takes the record of itself with it. So these tools
are built to keep working when the thing they watch does not.
uptimekit's reports are generated from the local JSONL history, so
producing a roll-up, a trend strip, an SLO status, or the status page
makes no network call — the checker only touches the network when it
probes, never when it reports, and a report can be built even while
the monitored endpoints are unreachable. The status page is a plain
HTML file, so the page describing an outage never goes down with the
service it describes, and the reports are plain files that can be
committed and searched like any other document, so the record of an
incident lives alongside the code instead of inside a service that
might itself go down. loglens works the same way from the other side:
point it at a local log file and it gives you the numbers, with no
pipeline or service standing between you and the answer. flowkit's
run reports carry captured output tails, so the record of a run
survives the run itself without a separate logging setup. And the
checker's own test suite runs fully offline, so the tests prove the
checker without depending on the very thing it monitors.

The rule is about shared fate: whatever the tool depends on becomes a
second thing that can fail at the same time as the first. A monitor
that needs the network to tell you the network is down, a status page
hosted on the service whose outage it announces, a report that lives
in a database that is itself the incident — each one turns one failure
into two. Keep the tool's own needs smaller than the thing it watches,
and the answer is still there when the system it describes is not.

- [uptimekit](projects/uptimekit.md), [loglens](projects/loglens.md), [flowkit](projects/flowkit.md)

## Design around the constraint, not against it

The hard parts of these projects were constraints, and each one is handled
where it belongs rather than bolted on. Sorani Kurdish reads right-to-left,
so direction is handled at the layout level of the association site, not
just by translating strings. The personal site's galaxy is generated
procedurally so it can scale its rendering effort to the device, and
visitors who prefer reduced motion get a calmer presentation. flowkit's
steps run in deterministic topological order with declaration order
breaking ties, so parallel runs still report comparably run to run.

## Pin the ending to the outcome, not the step list

A run that fails halfway should still end properly: the notification
that says it failed has to go out, and the cleanup that returns things
to a known state has to happen. flowkit pins that work to the run's
outcome instead of to its place in the step list — `on_failure`,
`on_success`, and `finally` hooks run because of how the run ended,
not because the steps before them succeeded. A notify step cannot be
skipped by the very failure it is meant to report, and a cleanup step
runs whether the flow succeeded or not, so the run always leaves the
world tidier than it found it. The nightly ETL flow shows the shape:
if a step fails, `notify` runs while `announce` is skipped, and
`cleanup` runs either way.

The same instinct is behind the way a failed step is bounded rather
than left hanging: a timeout is a failed attempt that still consumes a
retry, so a hung step fails instead of stalling the flow, and the exit
code says whether the flow succeeded, so a cron job or a pipeline can
act on the result without parsing output. uptimekit does the same for
a failed probe — when `check` exits 1, the failure is already written
to the append-only history, so an outage is still there for the next
roll-up or SLO report even if nobody was watching when it happened.
The ending is part of the design, not an afterthought: whatever
happened in the middle, the run reports it, cleans up after itself,
and leaves a record.

- [flowkit](projects/flowkit.md), [uptimekit](projects/uptimekit.md)

## Treat what you observe as data, never as instructions

A monitoring tool spends its life reading content it did not write —
and some of that content is hostile. A probed endpoint can return
anything in its body, an access log is full of user agents, referers,
and request paths that an attacker chose, and a flow file arrives from
whoever wrote it. The rule these tools follow is that observed content
is data until proven otherwise: it is counted, compared, and displayed,
but it is never executed, evaluated, or rendered as code.

uptimekit applies it where the observed content meets the public: the
status-page renderer escapes everything it renders, so content coming
back from probed endpoints — URLs, page text, error bodies — is treated
as data, never as markup, and a hostile or broken endpoint cannot inject
anything into the page you publish. loglens applies it to the log
itself: every line is parsed as data — format auto-detected per line,
unparseable lines skipped rather than guessed at — and the strings that
came from attackers, user agents and referers ranked behind the 5xxs,
are only ever counted and reported, never run. flowkit draws the same
line inside the flow file: a step's `when` condition is a small declared
comparison against an environment variable, not a shell branch, so the
conditional logic in a flow cannot smuggle in execution — and validation
rejects malformed interpolation before a single step runs.

The point is that the boundary between data and instructions has to be
a decision, not an accident. A tool that renders what it observed, or
evaluates it, or passes it to a shell without thinking, hands the thing
it watches a way to run code in the tool — and the moment that happens,
the monitor is no longer observing the system, it is part of the attack
surface. Keep what you observe inert, and the worst a hostile endpoint
or a poisoned log line can do is appear in a table.

- [uptimekit](projects/uptimekit.md), [loglens](projects/loglens.md), [flowkit](projects/flowkit.md)

## What this adds up to

Practical systems over demonstrations: tools that are available the
moment they are needed, that fail loudly, that fit into automation
unchanged, and that leave a readable record behind them. The repositories
linked above are the evidence — the code, not the claims, is the point.
