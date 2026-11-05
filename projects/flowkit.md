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
- **Hooks are pinned to the outcome, not the step list.** End-phase hook steps — `on_failure`, `on_success`, or `finally` — run on the run's outcome, so a failure notification cannot be skipped by the very failure it is meant to report, and a cleanup step always runs whether the flow succeeded or not. The steps that matter most when things go wrong are the ones that cannot be skipped by things going wrong.
- **One broken hook never hides the others.** Hooks run sequentially in dependency order after the normal pass, and a failed, gated-off, or condition-false hook skips only its own hook dependents — never the other hooks — so a broken notification cannot hide the cleanup step, and fail-fast is deliberately not applied to hooks. A hook whose trigger does not match the outcome reports as skipped, not failed, and the dependency rule is enforced at load time: hooks can depend only on other hooks, and normal steps cannot depend on hooks.
- **Failures cascade, they don't propagate.** A failed step skips its dependents — and theirs — so nothing runs on a result that never happened. Fail-fast also skips independent later work, while `continue_on_error` lets the rest of the flow proceed even as the failed step's own dependents still skip. A failure stops exactly the work that depended on it, and the run's exit code still says the flow failed.
- **Retries are bounded, and a timeout is a failure.** `retries: 2` means at most three attempts, with the backoff doubling each time from `--backoff` (default 0.5s) — a flaky step gets another chance, not an endless one. And `timeout_seconds` bounds every attempt: a timeout is a failed attempt that still consumes a retry, so a hung step fails instead of stalling the flow.
- **Environment, layered — and a typo is a pre-run error, not a silent blank.** Every step runs with the process environment, plus the flow's `env`, plus its own `env`, most specific wins — and commands are expanded against that merged mapping before they reach the shell, so `${VAR:-default}` behaves the same everywhere. Malformed interpolation is rejected at load time, and `--strict-env` turns a typo'd variable expanding to nothing into a pre-run error naming the step and the variable, so a misspelled variable can never silently change a command.
- **Conditions are data, not branches in the shell.** A step can carry a `when` condition — `{"when": {"env": "DEPLOY", "equals": "yes"}}` or `{"when": {"env": "DRY", "set": false}}` — evaluated against the merged environment at run time, so a step that only belongs in one context is declared in the flow instead of wrapped in a shell `if`. A false condition skips the step and its dependents without failing the flow, and `--only a,b` / `--skip c` select a subset — the named steps plus their transitive dependencies, or everything else — without editing the flow file. `--dry-run` shows the selection and annotates the conditions, so the plan is reviewable before anything runs.
- **Parallel is a schedule, not a second mode.** `--jobs N` runs up to N independent steps concurrently, but only steps whose dependencies are done are eligible — the DAG bounds the parallelism, not the flag, so a four-way run of a linear chain is still sequential. And fail-fast does not kill work in flight: steps already running finish while nothing new is scheduled, so stopping early never leaves a half-written step behind. Results still report in declaration order no matter which step finished first, so a parallel run's report reads like a sequential one.
- **Failure output is shown, not buried.** Each step captures its combined stdout/stderr tail, and a failed step always prints its tail under its report line — the reason for the failure is in front of you without opening a log file. `--show-output` prints successful steps' tails too, and the `--json` summary and `--report` file carry an `output` field per step. For the whole story, `--output-dir` writes each attempt's full output to disk while memory keeps only the tail, so the report stays small and nothing is lost.
- **Reports, not just logs.** Text or JSON run reports carry captured output tails, and a JSON report file plus `--output-dir` full per-step logs give a post-run record without needing a separate logging setup.
- **The same engine, in-process or on the command line.** The runner is importable, not just a CLI: `load_flow` from `flowkit.model` and `run_flow` from `flowkit.runner` run a flow inside another program and return a result with a `.status` of `"succeeded"` or `"failed"`. Automation that embeds the runner gets the identical validation, ordering, retries, and failure semantics as the command line — no shelling out, no second implementation to keep in sync.
- **Four small modules, one job each.** The code is split by responsibility: `model.py` holds flow definitions, validation, and topological order; `runner.py` does sequential execution, retries, timeouts, and skip semantics; `report.py` writes the text and JSON run summaries; and `__main__.py` is only the CLI. There is no god module, and the split is what lets the same runner be imported as a library or driven from the command line without a second implementation to keep in sync.

## Worked example: the nightly ETL

The flow below is the repository's own example (`examples/nightly-etl.json`), shown as written — a flow you can read in one file:

```json
{
  "name": "nightly-etl",
  "env": {
    "DATA_DIR": "/data/nightly"
  },
  "steps": [
    {
      "name": "extract",
      "command": "python extract.py --out ${DATA_DIR}",
      "timeout_seconds": 300
    },
    {
      "name": "transform",
      "command": "python transform.py --in ${DATA_DIR}",
      "depends_on": [
        "extract"
      ],
      "retries": 2,
      "timeout_seconds": 600
    },
    {
      "name": "load",
      "command": "python load.py ${DATA_DIR}",
      "depends_on": [
        "transform"
      ],
      "retries": 2,
      "timeout_seconds": 600
    },
    {
      "name": "notify",
      "command": "./notify.sh ${CHANNEL} 'nightly-etl FAILED'",
      "env": {
        "CHANNEL": "#data-ops"
      },
      "trigger": "on_failure"
    },
    {
      "name": "announce",
      "command": "./notify.sh ${CHANNEL} 'nightly-etl OK'",
      "trigger": "on_success",
      "env": {
        "CHANNEL": "#data-ops"
      }
    },
    {
      "name": "cleanup",
      "command": "rm -rf ${DATA_DIR}/scratch",
      "trigger": "finally"
    }
  ]
}
```

The same file answers the usual questions — validate first, run, then report:

```bash
python -m flowkit examples/nightly-etl.json --dry-run  # validate, print the plan
python -m flowkit examples/nightly-etl.json            # run it
python -m flowkit examples/nightly-etl.json --json     # machine-readable summary
python -m flowkit examples/nightly-etl.json --report run.json  # JSON run report
python -m flowkit examples/nightly-etl.json --only extract,transform  # subset + deps
python -m flowkit examples/nightly-etl.json --jobs 4   # independent steps in parallel
```

What the run shows: extract, transform, and load run in dependency order, each with retries and a per-attempt timeout — and if a step fails, `notify` runs while `announce` is skipped, and `cleanup` runs either way, because the hooks are pinned to the run's outcome rather than the step list. The exit code says whether the flow succeeded, so a cron job or pipeline can act on the result without parsing output.

## What it demonstrates

Orchestration without the orchestrator: a readable flow file, validation before anything runs, and failure semantics — cascade, bounded retries, outcome-pinned hooks — that make a scheduled job trustworthy enough to leave alone.

## Links

- Repo: [midya8/flowkit](https://github.com/midya8/flowkit)
