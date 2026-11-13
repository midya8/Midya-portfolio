# PromptGuard: scanner baselines and occurrence quotas

## Occurrence-limited suppression

An opt-in actual-scanner baseline limits how many equal-identity findings can be suppressed. One prior allowance suppresses one of three current occurrences; two remain reported, while the legacy set suppresses all three. Inspect exact path/severity identity, every before/after allowance, unused entry and gate decision. The original scanner patterns, v1 baseline and prior policy inspector stay unchanged.

The current suite has 100 Python tests, including all 87 earlier tests, and seven Node/actual-Chrome tests, including all three earlier tests. Independent occurrence-rank references cover 4,374 exhaustive controls, 200 seeded complete native/browser reports and 162 browser duplicate-count controls. All 24 complete reports include 52 current rows, 32 prior rows, 22 quota entries, 52 legacy-control rows and 104 SVG marks. Chrome checks every displayed row, full selected record, gate/payload, stale/invalid state, 320/390/1280 containment and two trusted exports replayed through native CLI. Separate installed API/module/console reproduces all reports and actual scanner duplicate-contact gates, plus the original eight-module wheel, 27 audits, adapters and offline demo.

Exact path spelling is not repository isolation. Equal-identity occurrences are interchangeable, not historically tracked: reordering can change which line survives. A manually editable quota is not acceptance provenance or safety; a hash is not anonymity. No new detection patterns, security-effectiveness or new-method claim, and no automatic v1 migration. Missing/malformed quotas fail closed; incomplete scans cannot write quotas. Atomic replacement preserves previous quota bytes on a write/replace failure. Public fixtures use only abstract tags and reserved-domain contacts; real witnesses remain private.

[Live quota inspector](https://midya8.github.io/promptguard/quota.html) · [Source](https://github.com/midya8/promptguard) · [Contract, limits and credited sources](https://github.com/midya8/promptguard/blob/main/QUOTAS.md)

### Reproduce occurrence quotas

```sh
python -m promptguard.quota_audit --input examples/quota.json
bash tools/quota_wheel_smoke.sh
promptguard scan prompts/ --quota-baseline private-quota.json --audit private-witness.json
```

Actual quota creation is explicit with --write-quota-baseline. It captures eligible counts without suppressing that scan and can still fail a configured gate. Re-running it can accept larger counts, so it is a review decision, not automatic maintenance. The browser recomputes supplied abstract records, not prompts or secret detection. Finite occurrence baselines and indexed findings are established approaches; alint, Semgrep and Kingfisher are credited with differences stated. Package/SARIF version 0.2.0 remains to retain the original fixed contract; the quota schema is separately versioned.

## Retained scanner and original policy audit

Earlier counts below describe the unchanged prior build. The current suite includes all 87 tests.

Local-first prompt linting with a complete filter, baseline and CI-gate witness.

[Interactive inspector](https://midya8.github.io/promptguard/) | [Source and reproduction](https://github.com/midya8/promptguard)

## What the audit records

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
