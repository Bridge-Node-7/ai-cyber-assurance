# Completed Synthetic Threat-Control-Evidence Map
> **Artifact type:** COMPLETED SYNTHETIC EXAMPLE  
> **Operational authority:** None  
> **Coverage:** Partial assurance profile

## Example Status

**Synthetic / fictional example.** All threats, controls, evidence, identities, and outcomes are invented.

## Map Information

| Field | Value |
|---|---|
| Map ID | SYN-TCE-017 |
| System / Workflow | Synthetic Supplier Evidence Review S-17 |
| Owner | Fictional Security Reviewer |
| Review Date | 2025-01-15 |

## Map

| Map ID | Threat / Failure Mode | Attack or Failure Path | Asset / Decision | Mission Consequence | Likelihood / Uncertainty | Requirement ID | Preventive Control | Detective Control | Corrective Control | Recovery Control | Evidence ID | Validation Record | Control Owner | Risk Owner | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SYN-M-001 | Supplier-account misuse | Unauthorized person uses fictional supplier account | Evidence provenance | Unreliable source attribution | Unknown; synthetic scenario | SYN-R-001 | SYN-C-001: role-bound identity and MFA requirement | SYN-C-003: login and submission logging | SYN-C-004: human-approved session revocation and submission reverification | SYN-C-005: restore approved account state | SYN-E-001 | Self-review only | Fictional identity owner | Fictional assurance lead | Amber |
| SYN-M-002 | Evidence alteration or mismatch | Submitted bytes differ from declared synthetic hash | Evidence integrity | Reviewer may rely on wrong record | Demonstrated in fictional example | SYN-R-002 | SYN-C-002: required digest declaration and evidence retention | SYN-C-003: AI-assisted read-only digest comparison | SYN-C-004: request corrected package and preserve superseded evidence | SYN-C-005: restore from retained approved evidence | SYN-E-002, SYN-E-003, SYN-E-004 | Synthetic comparison rerun | Fictional evidence custodian | Fictional human reviewer | Green for tested comparison condition |
| SYN-M-003 | Excessive AI authority | Agent is permitted to approve or change status | Supplier-status decision | Unaccountable automated decision | Controlled by design; not independently tested | SYN-R-003 | SYN-C-003: read-only tools and denied decision scope | SYN-C-003: tool-call and decision-log review | SYN-C-004: human-approved agent disablement | SYN-C-005: manual review fallback | SYN-E-003, SYN-E-005 | Self-review only | Fictional workflow owner | Fictional human reviewer | Amber |
| SYN-M-004 | Unsupported AI inference | Agent treats mismatch as malicious intent | Review finding | False attribution or unfair decision | Plausible; synthetic | SYN-R-004 | SYN-C-003: prompt and policy require fact/inference separation | SYN-C-004: human review of finding language | SYN-C-004: correct report, update instructions, and retest | SYN-C-005: manual evidence analysis | SYN-E-003, SYN-E-005 | Synthetic reviewer check | Fictional workflow owner | Fictional assurance lead | Green for example |
| SYN-M-005 | Evidence service unavailable | Repository cannot return the approved package | Evidence availability | Review cannot proceed or be reproduced | Untested | SYN-R-005 | SYN-C-005: retention and backup plan | SYN-C-005: availability monitoring | SYN-C-005: switch to controlled fallback | SYN-C-005: restore service and verify evidence | None | Not executed | Fictional platform owner | Fictional assurance lead | More evidence required |

## Corrective Actions

| Gap ID | Related Map ID | Missing or Weak Element | Consequence | Owner | Corrective Action | Due Date | Retest / Review | Status |
|---|---|---|---|---|---|---|---|---|
| SYN-G-001 | SYN-M-002 | Initial declared hash mismatch | Uncertain integrity | Fictional evidence custodian | Preserve original; obtain corrected synthetic evidence; rerun comparison | Demonstration date | Completed synthetic rerun | Closed |
| SYN-G-002 | SYN-M-005 | No executed recovery test | Availability claim unsupported | Fictional platform owner | Run controlled recovery exercise and record evidence | Before stronger decision | Required | Open |

## Decision Summary

| Decision | Count | Notes |
|---|---:|---|
| Green | 2 | Limited to the demonstrated fictional conditions |
| Amber | 2 | Requires continued human authority and bounded tools |
| Red | 0 | |
| More evidence required | 1 | Recovery remains untested |

Overall decision:

**Amber — controlled fictional pilot only.**

Decision owner: Fictional Human Assurance Reviewer

Conditions:

- Preserve read-only AI authority.
- Preserve fact/inference separation.
- Complete recovery exercise before stronger assurance.
- Reassess after changes.

## Limitations

Mapped controls are not proof of real implementation or effectiveness. This is a synthetic demonstration of traceability.
