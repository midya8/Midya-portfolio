# uptimekit

Synthetic HTTP, TCP and TLS checks with JSONL history and local reports. The code uses the Python standard library. There is no monitoring database or hosted-service dependency.

[Source and commands](https://github.com/midya8/uptimekit)

## What it measures

An HTTP check can test the status code, an optional body keyword and a latency limit. TCP checks test connection success and an optional latency limit. TLS checks compare certificate expiry with a supplied minimum number of days. Connection failures become failed results; invalid configuration is rejected before probing.

A failed check is an observation under those rules, not a diagnosis of the service. A slow response can fail even with HTTP status 200. A certificate can fail its expiry threshold while the endpoint remains reachable. The checks do not establish what every visitor experiences.

Results are appended to a JSONL file. Reports read that file without probing again. Retention compaction writes a replacement file and renames it into place. This is not a transactional database, a tamper-proof audit log or a guarantee against every interrupted write. Run compaction when retention is needed; appending alone does not enforce a size bound.

## Availability and incidents

Availability is successful checks divided by total checks in the selected window. It is not duration-weighted uptime. Irregular sampling and missing checks affect what the ratio can tell you. The daily trend shows empty buckets as gaps. Average latency and p50/p95 use successful checks only.

The incident classifier opens an incident after the selected number of consecutive failed checks and records its start at the first failure in that run. The next success closes it. The default threshold is one; `--threshold 2` excludes isolated failures. These are boundaries in the sampled record, not exact physical outage times.

`--fail-open` returns exit status 1 when an incident remains open. With incident reporting enabled, `--max-open-minutes` returns 1 when the age of a recorded open incident reaches the supplied limit. An old last sample can therefore leave an incident open even if the service has recovered without another check.

SLO reporting compares the check-success fraction with the configured target and reports error-budget consumption in those same check-based units. It does not turn the sample ratio into measured minutes of downtime.

None of these options sends a page, email or message. A scheduler, CI job or notification service must decide what to do with the exit status. Monitoring also needs a host, permissions and network access; standard-library code does not make operating it cost-free.

## Saved status pages

The renderer produces a single HTML file with inline CSS and no JavaScript. It includes the latest recorded state, check-success fraction, recent checks and latency details. Rendered values are escaped.

The page does not refresh itself or classify old samples as stale. Regenerate it after checks, and choose hosting and freshness rules for the intended audience. A page generated earlier can disagree with a newer report because they read the history at different times. Static hosting can be independent of the monitored service, but its availability is a separate concern.

## Run it

From a checkout of the source repository:

```sh
python -m unittest discover -s tests -v
python -m uptimekit --help
python -m uptimekit report --window 24h
python -m uptimekit report --incidents --threshold 2 --fail-open
python -m uptimekit report --incidents --max-open-minutes 15
python -m uptimekit status-page --out status.html
```

Reporting commands read the local history. To collect real checks, configure endpoints you are allowed to probe, then use `check` or `watch` as described in the source README. No example endpoint needs to be contacted to run the tests.

## Verification and limits

The 98 tests cover probes, history, reports, incident gates, status rendering and CLI behavior. HTTP and TCP probe tests use loopback servers; TLS paths use injected certificates and CLI tests mock the probe engine. The suite requires no remote service, but it does use local sockets. CI runs Python 3.11.

The source changes reviewed for this case study are documentation and docstrings only. Executable AST comparison, fresh public-checkout tests and merged-main CI were used to check that the wording change did not change behavior. These checks do not prove that a deployed monitor is configured correctly or that a published page is current.
