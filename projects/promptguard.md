# PromptGuard

Local-first prompt, secret and prompt-injection linting for AI systems.

## Problem

Prompt files are production configuration. They often contain model instructions, tool policy, examples and user data, but they rarely receive the same automated review as application code. A leaked API key or a prompt that asks a model to ignore controls can be easy to miss in review and expensive to discover later.

## Approach

PromptGuard scans local prompt, Markdown, JSON and YAML files without a network dependency. It reports deterministic findings for:

- OpenAI-style keys, AWS-style keys, private key headers and assigned secrets
- email addresses, phone numbers and payment-card numbers checked with the Luhn algorithm
- prompt-injection language that asks a model to ignore earlier instructions, reveal hidden prompts, bypass controls or exfiltrate credentials
- missing or incomplete Markdown prompt metadata frontmatter

Findings include a rule ID, severity, file, line and redacted excerpt. Reports are available in terminal, JSON and standalone escaped HTML formats. Severity and finding-count gates return meaningful exit codes for CI.

## Verification

- 28 unit tests cover scanner rules, redaction, report escaping, filtering and gate exit codes.
- `bash examples/demo.sh` runs fully offline against safe and risky fixtures.
- The risky fixture produces 8 findings with maximum severity critical, and the high-severity gate rejects it as expected.
- CI runs the same suite across Python 3.10-3.13.

The included credentials and contact details are fake fixture values. Deterministic linting provides a useful review signal; it does not claim to catch every prompt-injection technique.

## Links

- Repository: [midya8/promptguard](https://github.com/midya8/promptguard)
