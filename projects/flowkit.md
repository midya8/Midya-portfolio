# flowkit

A standard-library runner for JSON-defined DAGs of shell commands. It provides retries, per-attempt timeouts, conditional steps, parallel scheduling and end-phase hooks. The CLI and importable runner share the same execution code. CI tests Python 3.10-3.13.

## Execution model

A flow names its steps and connects them with `depends_on`. Ready steps follow declaration order; `--jobs N` allows independent steps to run concurrently. Reports remain in declaration order. Fail-fast stops scheduling new normal steps but lets running steps finish. `continue_on_error` permits independent work to proceed; dependents of the failed step still skip.

`retries: 2` permits at most three attempts. Backoff doubles from the configured base, and a timeout consumes an attempt. These are execution controls, not a rollback or transaction system. A failed command may already have changed files or external state.

End-phase hooks run after the normal phase. `on_failure` and `on_success` depend on that phase's outcome; `finally` is eligible under either outcome. Hooks still obey selection, conditions and hook dependencies, so `finally` is not a guarantee that a cleanup command executes. A failed or skipped hook skips its own dependents without stopping unrelated hooks. Hooks can depend only on hooks, and normal steps cannot depend on hooks.

## Planning and safety boundaries

Validation rejects structural errors such as duplicate names, unknown keys, dangling dependencies and cycles. `--dry-run` lists selected step names, dependencies, conditions and hook gates without executing commands. It does not show expanded shell commands or prove that commands are safe.

Commands run in a shell with the caller's permissions. Flow-level and step-level environment values override the process environment and interpolate into commands as `$VAR`, `${VAR}` or `${VAR:-default}`. Values are not shell-escaped. Unset references without defaults expand to empty strings unless `--strict-env` rejects them first. Review the actual commands, values and paths before execution, especially when a flow or its inputs come from someone else.

`--only` selects named steps plus their dependencies. `--skip` excludes steps and causes their dependents to skip. A false `when` condition also skips a step and its dependents without failing the flow.

## Reports

Text and JSON reports include status and combined stdout/stderr tails. `--report` writes a JSON report, while `--output-dir` appends full per-step output to disk. Review output for secrets before sharing logs. CLI exit codes are 0 for success or a valid dry-run, 1 for step failure, and 2 for invalid input or a pre-run/report-writing error.

## The ETL example is a template

`examples/nightly-etl.json` describes three normal steps and three end-phase hooks. It references `extract.py`, `transform.py`, `load.py` and `notify.sh`, none of which are included. Its cleanup command deletes the configured scratch directory. Supply the scripts and review paths and commands before running it.

```bash
python -m flowkit examples/nightly-etl.json --dry-run
python -m flowkit examples/nightly-etl.json --dry-run --only extract,transform
```

The first command lists the three normal steps and all three hooks. The second lists only extract and transform, in dependency order. Neither executes the template's commands.

## Verification

The 123-test suite covers flow validation, ordering, retries, timeouts, fail-fast and skip behavior, hook gates and dependencies, conditions, selection, environment interpolation, output capture and CLI exit codes.

```bash
python -m unittest discover -s tests -v
python -m compileall -q flowkit
```

A fresh public checkout passes both commands and the two dry-runs above. A copied module was also checked outside the checkout: all six imported module paths resolve to that copy, and harmless passing and failing flows return the expected CLI status and exit code. This is a local functional check, not a durability or production-safety claim. There is no package build configuration or hosted app in this repository.

## Links

- Repo: [midya8/flowkit](https://github.com/midya8/flowkit)
