# High-Impact System Readiness
> **Artifact type:** TEMPLATE  
> **Completion status:** Blank for reuse  
> **Required for:** Full Assurance Lifecycle or high-impact review

## What this document is

A coordinating review for sensitive, operational, AI-enabled, or high-impact systems. It routes users through the full assurance lifecycle without duplicating the underlying records.

## Who should complete it

System owners, engineering leads, security reviewers, governance teams, operators, and accountable decision owners.

## When to use it

Use before piloting, deploying, materially changing, or reauthorizing a system whose failure could create significant security, privacy, safety, financial, legal, mission, or public-trust consequences.

## Decision supported

Whether the system has a sufficiently bounded, evidenced, validated, recoverable, and human-governed posture for the current stage.

## System / Workflow

## Version

## Owner

## Decision Owner

## Review Date

## 1. Lifecycle Record Map

| Required Record | Location / Evidence ID | Owner | Status | Gap |
|---|---|---|---|---|
| Evidence Manifest | | | | |
| Security Policy and Target | | | | |
| Identity and Authority Register | | | | |
| Threat-Control-Evidence Map | | | | |
| Human Approval Gates | | | | |
| Control Validation Record | | | | |
| Recovery Assurance Record | | | | |
| Review Decision | | | | |

## 2. System Boundary

Reference the boundary in the Evidence Manifest.

### In Scope

### Out of Scope

### Critical Functions

| Function | Mission or Business Consequence | Owner | Evidence ID |
|---|---|---|---|

### External Dependencies

| Dependency | Purpose | Failure Consequence | Replacement / Fallback | Owner | Evidence ID |
|---|---|---|---|---|---|

## 3. Identity and Authority

- [ ] Human, service, workload, supplier, and AI-agent identities are uniquely identified.
- [ ] Privileged authority is bounded and time-limited where feasible.
- [ ] High-impact actions have human approval gates.
- [ ] Self-approval and conflicting duties are prohibited where required.
- [ ] Revocation and session termination paths are documented and tested where material.
- [ ] Evidence references the Identity and Authority Register.

Key identity gaps:

## 4. Data, Tools, and AI Use

| Element | Classification / Sensitivity | Permitted Use | Prohibited Use | Human Review | Evidence ID |
|---|---|---|---|---|---|
| Data | | | | | |
| Model | | | | | |
| Retrieval source | | | | | |
| Memory | | | | | |
| Tool / API | | | | | |
| Output | | | | | |

## 5. Threats, Controls, and Evidence

Reference the Threat-Control-Evidence Map.

Critical unresolved threats or failure modes:

| ID | Threat / Failure Mode | Consequence | Control Gap | Owner | Decision Effect |
|---|---|---|---|---|---|

## 6. Monitoring and Incident Readiness

- [ ] Required telemetry is identified.
- [ ] Critical events are detectable.
- [ ] Time sources and evidence retention are defined.
- [ ] Investigation ownership is assigned.
- [ ] Containment actions requiring human approval are identified.
- [ ] Incident and near-miss review paths are documented.

## 7. Recovery and Continuity

- [ ] Safe degraded operation is defined where applicable.
- [ ] Manual fallback exists where required.
- [ ] Rollback ownership is assigned.
- [ ] Recovery objectives are documented.
- [ ] Recovery evidence distinguishes planned from tested capabilities.
- [ ] Corrective actions and retests are tracked.

## 8. Constraints and Assumptions

| ID | Constraint / Assumption | Evidence | Risk if False | Owner | Review Date |
|---|---|---|---|---|---|

## 9. Readiness Decision

- [ ] Green — sufficient evidence for the current stage
- [ ] Amber — proceed only with documented conditions
- [ ] Red — do not proceed
- [ ] More evidence required

Decision owner:

Reviewer:

Permitted stage or use:

Conditions:

Residual risk:

Unproven claims:

Next review date:

## Limitations

This record does not certify a system, authorize deployment by itself, replace legal or compliance review, or prove that listed controls are effective without supporting evidence and validation.
