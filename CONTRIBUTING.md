
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

Contributors should use focused changes and preserve the repository's Quick Review and Full Assurance Lifecycle paths.

## Repository Integrity Workflow

The repository uses both `REPO_MANIFEST.json` and `MANIFEST.sha256` to detect uncontrolled tree changes. Complete the applicable steps before opening a pull request.

### Editing an Existing Controlled File

Regenerate the hash manifest, then run the full validator:

```bash
python scripts/validate_repo.py --root . --generate-hashes
python scripts/validate_repo.py --root .
```

### Adding, Renaming, or Removing a Controlled File

1. Update the sorted `files` array in `REPO_MANIFEST.json`.
2. Update `file_count` so it equals the number of controlled files.
3. Regenerate `MANIFEST.sha256`.
4. Run the full validator.

```bash
python scripts/validate_repo.py --root . --generate-hashes
python scripts/validate_repo.py --root .
```

`--generate-hashes` updates `MANIFEST.sha256` only. It does not update `REPO_MANIFEST.json`. Do not hand-edit individual hash lines. Do not commit generated validation reports. A change is not ready for review until manifest parity, hashes, links, safety checks, and all configured validator checks pass.

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
