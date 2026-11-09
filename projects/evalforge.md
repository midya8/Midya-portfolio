# EvalForge — case study

Local-first evaluation for LLM and agent outputs: run a versioned set of prompts through any model or agent adapter, score every response with deterministic checks, keep a durable JSON run record, render self-contained HTML, JUnit XML, Markdown and SARIF reports, and compare candidate runs against a baseline so regressions fail before they ship. Standard library only, CLI, 68 unit tests with CI across Python 3.10–3.13.

- Repo: [midya8/evalforge](https://github.com/midya8/evalforge)

## The constraint that shaped the build

AI features fail in ways ordinary unit tests miss: a prompt edit improves one answer and silently regresses three others, a model swap changes output shape, a latency spike only shows up in a long tail. The goal was a harness that makes those changes reviewable — prompts and acceptance criteria in versioned files, checks that are deterministic and inspectable rather than another opaque model judging the output, and a regression gate CI can enforce — without requiring an API key or a hosted service to run.

## Decisions

- **The adapter is just a command.** The task prompt goes to the adapter on stdin and the answer comes back on stdout, with `EVALFORGE_TASK_ID` and `EVALFORGE_PROMPT` in the environment — so the harness does not care whether the text came from a local model, an internal agent binary, or a paid API command configured separately. A non-zero exit is preserved as a run error, not silently dropped.
- **Tasks are versioned files.** Suites are JSONL with stable IDs, prompts, expected values, tags, and metadata — so a prompt edit is a diff, a suite is reviewable in a pull request, and baseline comparisons match on the stable ID.
- **Deterministic scorers before model judging.** Exact, contains, regex, JSON equality or subset, token-F1 similarity, numeric tolerance, and word/character length bounds — checks that produce the same result for the same output, so CI stays stable and review discussions stay concrete. When `checks` is omitted, a sensible default is derived from `expected`: JSON values use JSON equality, numbers use numeric matching, strings use normalized exact matching.
- **Invalid tasks fail before anything runs.** Unsupported check types, malformed regexes, and invalid JSONL are reported with the task ID or line number before any adapter command runs — a broken suite never spends model calls finding out it is broken.
- **Raw evidence first.** JSON run records keep per-task scores, check details, raw output, latency, attempts, adapter command, timestamp, and tag roll-ups — a report never hides the response behind a single number.
- **The comparison is the gate.** `compare` matches candidate to baseline by task ID, reports regressions before improvements, treats missing candidate tasks as failures, and exits 1 when a task drops more than `--max-drop`, a passing task starts failing, or a baseline task is missing — with `--format json` for automation, `--markdown` for a CI job-summary comparison, and `--sarif` for a SARIF 2.1.0 comparison that maps regressions to errors and missing candidate tasks to warnings.
- **Gates, not just reports.** `--fail-under` sets a minimum mean score, `--max-drop` caps per-task regression, tag filtering scopes a run, and retries, timeouts, and bounded parallel execution (`--workers`) keep a run within its budget — exit codes 0/1/2 make the whole thing scriptable.
- **The report is safe to share, and fits CI.** One HTML file with inline CSS, escaped model output, summary cards, tag roll-ups, and per-task details — no JavaScript, no external assets, no trackers — so a report can be opened anywhere without a server. The same run also emits JUnit XML for ordinary CI test viewers, Markdown for native CI job summaries, and SARIF 2.1.0 so failed tasks, adapter errors and regressions feed code-scanning tools — the results reach the surfaces that already review code, instead of living in a file only a human opens.
- **Useful without an API key.** The included demo runs six tasks against a deterministic local adapter and passes 6/6 offline; the mock adapter is a stand-in that proves the evaluation loop, not a model pretending to measure model quality.

## Testing and compatibility

68 unit tests, with CI across Python 3.10–3.13. The suite runs fully offline.

## Worked example: gating a prompt change

The commands below are the real EvalForge CLI, taken from the project's own usage docs. Validate the suite, run the offline demo, run a real agent as a candidate, then compare it against the baseline:

```bash
python3 -m evalforge validate examples/tasks.jsonl
# the suite is checked before any adapter runs — a bad task
# definition fails here, not halfway through a run

python3 -m evalforge run \
  --tasks examples/tasks.jsonl \
  --cmd "python3 examples/mock_model.py" \
  --out .evalforge-demo/run.json \
  --report .evalforge-demo/report.html \
  --junit .evalforge-demo/results.xml \
  --markdown .evalforge-demo/summary.md \
  --sarif .evalforge-demo/analysis.sarif \
  --fail-under 1.0
# 6/6 passed · mean score 1.000 · errors 0 — the six-task demo,
# fully offline against the deterministic local adapter; the same
# run writes the HTML report, a JUnit report for CI test viewers,
# a Markdown summary for CI job summaries, and a SARIF 2.1.0 log
# for code-scanning tools

python3 -m evalforge run \
  --tasks tasks/production-agent.jsonl \
  --cmd "python3 adapters/my_agent.py --model candidate" \
  --out runs/candidate.json \
  --report reports/candidate.html \
  --timeout 45 --retries 1 --workers 2
# the same runner against a real agent: a candidate build,
# bounded in time, retries, and parallelism

python3 -m evalforge compare runs/baseline.json runs/candidate.json --max-drop 0.05 \
  --markdown reports/comparison.md --sarif reports/comparison.sarif
# regressions reported before improvements; exit 1 if any task
# drops more than 0.05, a passing task starts failing, or a
# baseline task is missing from the candidate — with a Markdown
# comparison for the CI job summary and a SARIF comparison that
# maps regressions to errors and missing tasks to warnings
```

## What it demonstrates

Evaluation as a repeatable gate rather than a one-off notebook: versioned suites, deterministic checks, raw evidence kept with every score, and a baseline comparison that fails the build on regression — all without a network call or an API key. And the limit is stated, not hidden: a passing suite is a regression gate, not proof the system is safe or correct outside the tasks in the suite.

## Links

- Repo: [midya8/evalforge](https://github.com/midya8/evalforge)
