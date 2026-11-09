# PromptGuard

Local-first prompt linting with a complete filter, baseline and CI-gate witness.

[Interactive inspector](https://midya8.github.io/promptguard/) | [Source and reproduction](https://github.com/midya8/promptguard)

## Problem

A passing security gate can hide findings before the gate even runs. Severity filters remove rows; baselines suppress known identities; incomplete filesystem scans can look like empty results. Reviewers need to see why each finding disappeared, not only a final count.

## Implementation

PromptGuard retains its dependency-free local scanner for prompt, Markdown, JSON and YAML files: recognizable secret/token patterns, private-key headers, assigned values, contact details and Luhn-validated cards, injection-language patterns and metadata frontmatter. Existing terminal, JSON, SARIF 2.1.0, JUnit XML, Markdown and escaped standalone HTML reports remain available.

New native corrections redact full lines before truncation and redact metadata excerpts, enumerate all recognized sensitive matches per line, count successfully read files and refuse a successful gate on scan errors. Incomplete scans cannot write a new baseline. Strict baseline loading rejects malformed SHA-256 identities, duplicate JSON keys and invalid encoding.

`scan --audit` retains every current row, fingerprint, filter eligibility, baseline match, disposition, used/unused identities, reported payload and gate decision. `audit --spec --json` recomputes bounded synthetic findings. The browser independently recomputes all stages using JavaScript and WebCrypto, exposes every current/prior row and full selected record, draws the stage path, and exports complete current JSON. Invalid or edited input clears stale output, including asynchronous digest races.

## Identity and privacy limits

Baseline identity still excludes line and severity and normalizes slashes/whitespace, which can alias distinct paths. Duplicate current identities count separately; duplicate prior identities collapse. Metadata now binds its original first line privately when redaction changes it, so rotated material changes identity. Old metadata baseline entries can therefore surface again for review. This migration is documented, not silently presented as unchanged behavior.

Only reported findings reach severity/count gates. The count gate fails strictly above its cap. Scan errors dominate with exit 2, gate failure returns 1, otherwise 0. No configured gate means findings alone do not fail the scan. A passing policy does not prove prompt safety or detector completeness.

A digest is not anonymity. Low-entropy values can be guessed; paths and errors can expose private context. Keep real baselines and witnesses private. Public controls accept abstract synthetic findings only, not raw prompts or secrets. This extension adds no new detection patterns and makes no injection-defense effectiveness claim or security certification claim.

## Verification

- 87 Python tests on 3.10-3.13 retain all original 68 tests, fixtures and offline demo unchanged.
- 13,320 exhaustive small policy controls derive expected row indices and exit precedence separately.
- 27 complete native/independent-JavaScript reports compare 735 numeric and 1,443 other leaves.
- Actual Chrome checks 50 current rows, 17 prior rows, 16 baseline identities across cases, 50 full records and 181 exact-position stage circles, all table/card/gate/payload fields, export, stale invalidation and asynchronous races. Containment is checked at 320, 390 and 1280 pixels.
- Isolated installed wheel outside the checkout verifies eight module origins, all 27 reports, all CLI formats, baseline suppression and incomplete scans.
- Original risky-fixture analysis and HTML remain byte-exact and visible; original source/test/demo hashes are archived. The historical risky fixture still produces eight findings. Existing dummy credentials remain documented; this extension adds reserved-domain contacts, abstract fixture tags and mocked noncredential patterns only.

## Prior work

SHA-256 identities, deterministic filters, baselines and gates are established methods. OWASP/CWE guidance supports careful handling of sensitive logs and output; SARIF examples distinguish suppression and execution status; GitHub documents bounded pattern coverage. No external scanner code or secret corpus copied. This witness does not implement SARIF suppression interoperability.

- [Evidence definitions and sources](https://github.com/midya8/promptguard/blob/main/EVIDENCE.md)
- [Repository](https://github.com/midya8/promptguard)
- [Interactive inspector](https://midya8.github.io/promptguard/)
