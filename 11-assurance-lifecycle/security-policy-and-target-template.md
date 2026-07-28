# Security Policy and Target
> **Artifact type:** TEMPLATE  
> **Completion status:** Blank for reuse  
> **Required for:** Full Assurance Lifecycle

## What this document is

**Security policy:** the protection outcome the system must satisfy.

**Security target:** how that outcome is scoped, implemented, evidenced, tested, and reviewed for this particular system.

## Who should complete it

The system owner, security architect or reviewer, operational owner, and accountable decision owner.

## When to use it

Use at the beginning of a Full Assurance Lifecycle review and update it when the mission, boundary, threat environment, architecture, or risk decision materially changes.

## Decision supported

Whether the system has a clear, authorized, and testable protection objective for the current stage.

## Record Information

| Field | Value |
|---|---|
| Record ID | |
| System / Workflow | |
| Version | |
| System Owner | |
| Security Owner | |
| Decision Owner | |
| Review Date | |
| Next Review Date | |

## 1. Mission and Desired Outcome

Mission or business outcome:

Users or stakeholders served:

Consequences of failure:

## 2. Security Policy

Write a concise, testable protection requirement.

> No [protected asset or decision] may be [action] unless [identity, authority, evidence, control, and human-approval conditions].

Approved policy statement:

## 3. System Boundary

Reference Evidence Manifest ID:

### In Scope

### Out of Scope

### External Dependencies

| Dependency | Purpose | Trust Assumption | Failure Consequence | Owner | Evidence ID |
|---|---|---|---|---|---|

## 4. Protected Assets and Properties

| Asset / Decision | Confidentiality Need | Integrity Need | Availability Need | Additional Trust or Safety Need | Owner |
|---|---|---|---|---|---|

## 5. Subjects, Identities, and Authority

Reference Identity and Authority Register ID:

Critical identity classes:

Privileged or consequential actions:

Required human approval:

## 6. Threats, Failure Modes, and Assumptions

| ID | Threat / Failure Mode / Assumption | Affected Asset | Consequence | Evidence or Basis | Owner |
|---|---|---|---|---|---|

## 7. Security Objectives

| Objective ID | Security Objective | Policy Link | Threat / Failure Link | Owner | Validation Method |
|---|---|---|---|---|---|

## 8. Mechanisms and Controls

| Control ID | Control | Prevent / Detect / Correct / Recover | Objective ID | Implementing Owner | Evidence ID |
|---|---|---|---|---|---|

## 9. Required Telemetry and Evidence

| Evidence ID | Evidence Needed | Source | Collection Method | Integrity Method | Retention | Reviewer |
|---|---|---|---|---|---|---|

## 10. Validation and Recovery Requirements

| Requirement ID | Test or Review | Success Criteria | Test Owner | Recovery / Rollback Requirement | Evidence Output |
|---|---|---|---|---|---|

## 11. Constraints and Residual Risk

| ID | Constraint / Residual Risk | Consequence | Owner | Acceptance Authority | Expiration / Review Date |
|---|---|---|---|---|---|

## 12. Decision

- [ ] Green — policy and target are sufficient for the current stage
- [ ] Amber — proceed only with documented conditions
- [ ] Red — do not proceed
- [ ] More evidence required

Decision owner:

Reviewer:

Conditions:

Unproven assumptions:

Required corrective action:

Next review date:

## Limitations

Approval of this document does not prove that controls are implemented or effective. Those claims require evidence in the Control Validation Record and, where applicable, the Recovery Assurance Record.
