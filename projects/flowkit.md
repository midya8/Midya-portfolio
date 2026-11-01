# flowkit — case study

A dependency-free workflow runner: JSON-defined DAGs of shell commands, standard library only — if Python is installed, flowkit runs. CLI plus importable library, 123 unit tests, CI across Python 3.10–3.13.

## The problem

Scheduled jobs and multi-step pipelines are usually held together with shell scripts or a heavyweight orchestrator. Scripts grow implicit ordering, silent failures, and environment quirks; orchestrators bring a server, a database, and a deployment to maintain. flowkit targets the middle: a flow you can read in one JSON file, run from cron or a pipeline, and trust to fail loudly.

## What it does

A flow names its steps and wires them with `depends_on`. Each step is a shell command with retries and exponential backoff, per-attempt timeouts, and fail-fast or continue-on-error semantics. Independent steps can run in parallel (`--jobs`), steps can be conditional on environment variables (`when`), and subsets can be run (`--only` / `--skip`). End-phase hook steps — `on_failure`, `on_success`, or `finally` — pin cleanup and notification work to the run's outcome, so a notify step cannot be skipped by the very failure it is meant to report.

Layered environment variables (flow-level, overridden per step) interpolate into commands as `$VAR`, `${VAR}`, or `${VAR:-default}`, and `--strict-env` fails the run up front on any unset reference instead of letting a blank variable silently change a command.

## Design decisions

- **Validation first.** Duplicate step names, dangling dependencies, cycles, unknown keys, and malformed interpolation are all rejected before anything runs, with a message naming the problem. A bad flow file should never half-execute.
- **Deterministic order.** Steps run in topological order; among ready steps, declaration order wins. Parallel runs still report in declaration order, so output is comparable run to run.
- **Exit codes as a contract.** 0 means the flow succeeded (or a dry run validated), 1 means a step failed, 2 means the flow file itself is invalid. That makes flowkit a scriptable gate: a pipeline or cron job can act on the result without parsing output.
- **Dry run as a plan.** `--dry-run` validates and prints the plan without executing, so a flow can be reviewed before it touches anything.
- **Reports, not just logs.** Text or JSON run reports carry captured output tails, and a JSON report file plus `--output-dir` full per-step logs give a post-run record without needing a separate logging setup.

## Example

The repository's example flow is a nightly ETL: extract, then transform, then load, each depending on the previous step, with retries and timeouts — followed by a failure notification, a success announcement, and a cleanup step that always runs.

## Links

- Repo: [midya8/flowkit](https://github.com/midya8/flowkit)
