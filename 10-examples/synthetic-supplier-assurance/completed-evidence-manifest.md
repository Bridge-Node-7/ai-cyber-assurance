# Completed Synthetic Evidence Manifest
> **Artifact type:** COMPLETED SYNTHETIC EXAMPLE  
> **Operational authority:** None  
> **Coverage:** Partial assurance profile

## Example Status

**Synthetic / fictional example.** All entities, records, identities, materials, and results are invented for demonstration.

## Manifest Information

| Field | Value |
|---|---|
| Manifest ID | SYN-EM-017 |
| System / Workflow | Synthetic Supplier Evidence Review S-17 |
| Version | Fictional pilot 0.2 |
| Owner | Fictional Assurance Operations Lead |
| Decision Owner | Fictional Human Assurance Reviewer |
| Review Date | 2025-01-15 |

## Mission and Purpose

Reduce repetitive review time for a fictional material-evidence package while preserving attributable identity, source integrity, bounded AI authority, evidence traceability, and human decision control.

## System Boundary

### In Scope

- Fictional supplier submission portal
- Synthetic supplier representative identity
- Read-only AI review agent
- Synthetic evidence repository
- Hash-comparison function
- Human review queue
- Decision record

### Out of Scope

- Real suppliers or people
- Real material qualification
- Laboratory operations
- Production systems
- Customer data
- Export-controlled or proprietary information
- Automated supplier approval

## Critical Assets and Decisions

| Asset / Decision | Owner | Protection Need |
|---|---|---|
| Synthetic evidence package | Fictional evidence custodian | Integrity, provenance, availability |
| Fictional supplier identity | Fictional identity owner | Authentication, authorization, accountability |
| AI review output | Fictional workflow owner | Traceability, limitation, human review |
| Supplier-status decision | Fictional human reviewer | Exclusive human authority and preserved evidence |

## Identities and Authority

| Identity ID | Class | Permitted Authority | Prohibited Authority | Owner |
|---|---|---|---|---|
| SYN-H-001 | Human reviewer | Review evidence; impose conditions; make fictional status decision | Modify source evidence without record | Fictional assurance lead |
| SYN-S-001 | Supplier representative | Submit synthetic evidence for assigned package | Approve own submission | Fictional supplier owner |
| SYN-A-001 | AI agent | Read approved files; compare identifiers and hashes; draft findings | Approve, reject, publish, delete, modify, or revoke | Fictional workflow owner |
| SYN-W-001 | Service identity | Retrieve approved evidence | Expand access or decide status | Fictional platform owner |

## AI and Automation Components

| Component | Purpose | Data Access | Tool Authority | Human Gate |
|---|---|---|---|---|
| Synthetic AI review agent | Compare evidence and draft findings | Read-only approved synthetic package | Hash comparison and report drafting | Human reviewer decides all material outcomes |

## Requirement and Control Register

| Requirement ID | Protection Outcome | Control ID | Control |
|---|---|---|---|
| SYN-R-001 | Supplier submissions are attributable to a bounded fictional identity | SYN-C-001 | Role-bound account and MFA requirement |
| SYN-R-002 | Submitted evidence can be checked for alteration and supersession | SYN-C-002 | Declared digest, retained original, and superseding-evidence linkage |
| SYN-R-003 | AI assistance cannot approve, reject, publish, or change supplier status | SYN-C-003 | Read-only AI tools, denied decision permissions, and activity logging |
| SYN-R-004 | Findings separate observed facts, inference, uncertainty, and attribution | SYN-C-004 | Human review and approval gate |
| SYN-R-005 | Approved evidence can be restored after service loss or corruption | SYN-C-005 | Controlled backup, fallback, restoration, and recovery test |

## Evidence Register

| Evidence ID | Evidence Type | Source | Collection Method | Collection Time | Related Control | Related Identity | Integrity Method | Confidence | Limitation | Retention | Review Date | Supersedes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SYN-E-001 | Identity record | Fictional portal | Synthetic export | 2025-01-15 | SYN-C-001 | SYN-S-001 | Demonstration hash | Medium | Not a real identity-proofing event | Example lifetime | 2025-01-15 | None |
| SYN-E-002 | Original evidence file | Fictional supplier | Synthetic upload | 2025-01-15 | SYN-C-002 | SYN-S-001 | Declared SHA-256 | Medium | Invented content | Example lifetime | 2025-01-15 | None |
| SYN-E-003 | AI comparison log | Fictional workflow | Automated synthetic run | 2025-01-15 | SYN-C-003 | SYN-A-001 | Demonstration log hash | Medium | Self-generated example | Example lifetime | 2025-01-15 | None |
| SYN-E-004 | Corrected evidence file | Fictional supplier | Synthetic resubmission | 2025-01-15 | SYN-C-002 | SYN-S-001 | Corrected demonstration SHA-256 | Medium | Invented content | Example lifetime | 2025-01-15 | SYN-E-002 |
| SYN-E-005 | Human review record | Fictional reviewer | Manual synthetic review | 2025-01-15 | SYN-C-004 | SYN-H-001 | Synthetic record digest | Medium | Internal example, not independent | Example lifetime | 2025-01-15 | None |

## Observed Gap

The hash declared for `SYN-E-002` did not match the synthetic file evaluated by the AI comparison step.

The AI agent flagged the mismatch but did not determine intent, attribution, supplier status, or legal effect.

## Corrective Action

The fictional human reviewer requested a corrected evidence package. The fictional supplier representative submitted `SYN-E-004`, and the comparison was repeated successfully for the synthetic condition.

## Remaining Gap

Recovery from unavailability or corruption of the fictional evidence service has not been executed.

## Manifest Decision

**Amber — sufficient only for a controlled fictional pilot with conditions.**

Conditions:

1. Human approval remains mandatory.
2. AI tools remain read-only.
3. All superseded evidence remains traceable.
4. Recovery must be tested before a stronger readiness claim.
5. Any material system, identity, model, provider, or tool change requires review.

## Limitations

This completed example is not evidence about any real supplier, material, AI system, control, or organization.
