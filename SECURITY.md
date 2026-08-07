
# Security Policy

## Scope

AI Cyber Assurance contains public-safe defensive cybersecurity templates, examples, and repository-validation tooling.

## Reporting a Security Issue

Do not disclose a suspected vulnerability or sensitive exposure in a public issue, discussion, pull request, or commit comment.

Use the repository's private **Security → Report a vulnerability** workflow.

**Maintainer release condition:** Public release is prohibited until GitHub private vulnerability reporting is verified as enabled from an authorized repository account. No alternate public vulnerability-reporting channel is provided.

## Report Content

Include only what is necessary:

- Affected file, workflow, or release
- Impact
- Reproduction details that are safe to share privately
- Whether sensitive information may have been exposed
- Suggested remediation, when available

Do not include live secrets, private keys, customer data, or harmful payloads unless the private reporting channel and maintainer explicitly require a safe handling method.

## Public-Safety Boundary

This repository must not include:

- Malware code
- Weaponization instructions
- Exploit-enabling operational details
- Harmful deployment procedures
- Persistence or evasion guidance
- Credential-theft workflows
- Unauthorized-access procedures
- Destructive or intrusive testing instructions
- Secrets, tokens, passwords, private keys, or production credentials
- Private infrastructure, real vulnerabilities, or sensitive findings
- Customer, employer, government, mission, or regulated data

High-level defensive analysis may be included when necessary for prevention, detection, investigation, response, recovery, or assurance.

## Maintainer Response

Security reports should be evaluated for:

1. Public-safety impact
2. Repository and release integrity
3. Possible sensitive disclosure
4. Need for private remediation
5. Affected tags, releases, archives, or documentation
6. Required notification or escalation
7. Corrective action and retest

Maintainers should acknowledge the report when practicable, preserve relevant evidence, limit unnecessary disclosure, and avoid unsupported timelines or claims.

## Supported Versions

| Version | Status |
|---|---|
| Latest public release | Supported for documentation and repository-integrity corrections |
| Pre-release branches | Best-effort support during active review |

This repository is a documentation and validation toolkit, not a hosted security service.

## Defensive Use

All materials are intended for authorized defensive cybersecurity, governance, review, readiness, recovery, and assurance work.
