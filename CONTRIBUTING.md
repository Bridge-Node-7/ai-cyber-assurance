
# Contributing to AI Cyber Assurance

Thank you for helping improve this public-safe defensive assurance toolkit.

## Contribution Principles

A contribution should improve one or more of the following:

- Defensive cybersecurity value
- Evidence quality and traceability
- Human authority and accountability
- Validation and recovery discipline
- Operator usability and accessibility
- Public safety
- Repeatability
- Source and claim integrity

## Accepted Contributions

Useful contributions include:

- Clearer templates and field guidance
- Better evidence, validation, recovery, or decision records
- Defensive threat and failure-mode analysis
- Safer AI-agent and workload-identity patterns
- Secure-by-design and supply-chain review improvements
- Public-safe synthetic examples
- Standard-library validation improvements
- Documentation, accessibility, and readability corrections

## Not Accepted

Do not contribute:

- Malware code
- Weaponization instructions
- Exploit-enabling operational details
- Harmful deployment procedures
- Persistence or evasion guidance
- Credential-theft workflows
- Unauthorized-access techniques
- Destructive or intrusive testing instructions
- Secrets, tokens, passwords, private keys, or production credentials
- Private infrastructure, customer, employer, government, or mission data
- Real vulnerabilities or sensitive operational findings
- Proprietary third-party material without permission
- Unauthorized third-party instructional, assessment, institutional, or proprietary material
- Claims of certification, authorization, independent validation, or production maturity without supporting evidence

High-level defensive analysis of malicious behavior may be included when necessary for prevention, detection, investigation, response, recovery, or assurance.

## Contribution Checklist

Every contribution should answer:

1. What defensive or assurance outcome does this improve?
2. Who should use it, and when?
3. What evidence does it capture or validate?
4. What decision does it support?
5. What human authority remains required?
6. Does it duplicate an existing record?
7. Does it preserve public safety and private boundaries?
8. Are limitations and unproven claims visible?
9. Do internal links, manifests, and validation checks pass?

## Pull Request Expectations

A pull request should include:

- Purpose and scope
- Files changed
- User-path impact
- Public-safety review
- Evidence or rationale
- Validation results
- Known limitations
- Screenshots only when they contain no sensitive information

Contributors should use focused changes and preserve:

- The `START_HERE.md` navigation path
- The `AGENTS.md` evidence classes and authority boundaries
- The Review Package Index applicability and status values
- The distinction between module assessment, assurance recommendation, and final assurance decision
- The repository's Quick Review and Full Assurance Lifecycle paths

## Repository Integrity Workflow

The repository uses both `REPO_MANIFEST.json` and `MANIFEST.sha256` to detect uncontrolled tree changes. Complete the applicable steps before opening a pull request.

### Controlled Change Sequence

Use the same deterministic sequence for edits, additions, renames, and removals:

```bash
python -m unittest discover -s tests -p "test_*.py"
python scripts/refresh_release_metadata.py --root . --write
python scripts/refresh_release_metadata.py --root . --check
python scripts/validate_repo.py --root .
sha256sum -c MANIFEST.sha256
git diff --check
```

`--write` refreshes only deterministic release metadata: the version derived from `VERSION`, controlled-file inventory, file count, and SHA-256 manifest. Human-reviewed release title, status, maturity statements, limitations, and decisions remain explicit review inputs.

Do not hand-edit individual checksum lines or commit generated validation reports. A change is not ready for review until metadata parity, hashes, links, safety checks, regression tests, and all configured validator checks pass.

## Changes Requiring Extra Review

Changes involving the following require explicit maintainer review:

- Human approval or authority rules
- Security-reporting procedures
- Validation and hash logic
- Public-safety restrictions
- New executable code or file types
- New external dependencies
- Changes to release status or maturity claims
- Changes that affect multiple modules

## Developer Certificate of Origin

By contributing, you represent that you have the right to submit the work under the repository license. Maintainers may require sign-off under the Developer Certificate of Origin for contributed commits.

## Code of Conduct

Participation is governed by [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md).
