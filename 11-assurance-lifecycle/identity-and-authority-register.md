# Identity and Authority Register
> **Artifact type:** TEMPLATE  
> **Completion status:** Blank for reuse  
> **Required for:** Full Assurance Lifecycle

## What this document is

A lifecycle inventory of human, service, workload, supplier, device, and AI-agent identities and the authority assigned to them.

## Who should complete it

Identity owners, system owners, security reviewers, platform administrators, and accountable decision owners.

## When to use it

Use before granting access, connecting tools, enabling automation, reviewing privilege, changing roles, or approving a high-impact system.

## Decision supported

Whether every material identity has attributable ownership, bounded authority, appropriate approval, review, expiration, and revocation.

## Record Information

| Field | Value |
|---|---|
| Register ID | |
| System / Workflow | |
| Owner | |
| Review Date | |
| Next Review Date | |

## Identity Classes

- Human user
- Privileged administrator
- Supplier or external party
- Service account
- Workload identity
- AI agent
- API client
- Device identity
- Emergency or break-glass identity
- Other

## Identity Register

| Identity ID | Identity Class | Display Name / Function | Owner | Purpose | Authoritative Source | Authentication Method | Roles / Scopes | Tools and Data Permitted | Privileged Actions | Required Approver | Created | Review Date | Expiration | Revocation Path | Last Observed Use | Evidence ID | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

## Authority Rules

### Prohibited Self-Approval

| Action | Initiating Identity | Prohibited Approver | Required Independent Approver | Evidence Required |
|---|---|---|---|---|

### Consequential Actions

| Action ID | Action | Eligible Initiator | Execution Authority | Human Approval | Approval Expiration | Post-Action Validation | Rollback Owner |
|---|---|---|---|---|---|---|---|

### Emergency Authority

| Emergency Action | Trigger | Eligible Identity | Approver | Time Limit | Logging | Post-Event Review |
|---|---|---|---|---|---|---|

## Lifecycle Review

- [ ] Every identity has a named owner.
- [ ] Every identity has a stated purpose.
- [ ] Authentication strength matches the risk.
- [ ] Roles and scopes are no broader than necessary.
- [ ] Privileged actions have explicit approval and logging.
- [ ] Dormant, orphaned, expired, and duplicate identities are identified.
- [ ] Agent and workload credentials are short-lived where feasible.
- [ ] Revocation paths are documented.
- [ ] Session and token termination is included where material.
- [ ] Periodic review dates are assigned.
- [ ] Last observed use is evaluated before retention.
- [ ] Evidence references support the decision.

## Findings and Corrective Actions

| Finding ID | Identity ID | Finding | Risk | Owner | Corrective Action | Due Date | Retest / Recheck | Status |
|---|---|---|---|---|---|---|---|---|

## Decision

- [ ] Green — identity and authority evidence is sufficient for the current stage
- [ ] Amber — proceed only with documented conditions
- [ ] Red — do not proceed
- [ ] More evidence required

Decision owner:

Reviewer:

Conditions:

Residual risk:

Next review date:

## Limitations

This register does not replace the authoritative identity source or prove that access controls operate correctly. Validate material controls and revocation paths separately.
