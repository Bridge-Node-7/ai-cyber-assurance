# Control Validation Record
> **Artifact type:** TEMPLATE  
> **Completion status:** Blank for reuse  
> **Required for:** Full Assurance Lifecycle for critical controls

## What this document is

A record that distinguishes whether a control is documented, implemented, observed in operation, tested, and supported as effective for a defined condition.

## Who should complete it

Control owners, system owners, security testers, operators, auditors or assessors, and decision owners.

## When to use it

Use before relying on a material control, after implementation or change, after a failure or incident, and when a review requires evidence beyond a policy statement.

## Decision supported

Whether the control can be relied upon for the stated requirement and current stage.

## Control State Doctrine

```text
Documented
≠ Implemented
≠ Operating
≠ Tested
≠ Effective
```

Each state requires its own evidence.

## Record Information

| Field | Value |
|---|---|
| Validation Record ID | |
| Control ID | |
| Control Name | |
| System / Workflow | |
| Control Owner | |
| Validator | |
| Review Date | |

## 1. Requirement and Intended Outcome

Requirement ID:

Threat / failure mode addressed:

Expected protection outcome:

Scope:

Dependencies and assumptions:

## 2. Control Description

Control mechanism:

Control category:

- [ ] Preventive
- [ ] Detective
- [ ] Corrective
- [ ] Recovery
- [ ] Compensating

Human authority or approval dependency:

## 3. State and Evidence

| State | Status: Yes / No / Partial / Unknown | Evidence ID | Evidence Date | Limitation |
|---|---|---|---|---|
| Documented | | | | |
| Implemented | | | | |
| Observed operating | | | | |
| Tested | | | | |
| Effective for defined test condition | | | | |
| Monitored | | | | |
| Recoverable / reversible | | | | |

## 4. Validation Method

Test or review method:

Authorization and scope:

Environment:

Preconditions:

Test data:

Success criteria:

Stop conditions:

Rollback path:

## 5. Results

| Test Step | Expected Result | Observed Result | Evidence ID | Pass / Fail / Partial | Notes |
|---|---|---|---|---|---|

## 6. Alternative Explanations and Uncertainty

Potential alternative explanation:

Data-quality limitation:

Coverage limitation:

Confidence:

## 7. Findings and Corrective Action

| Finding ID | Finding | Severity | Owner | Corrective Action | Due Date | Retest Required? | Status |
|---|---|---|---|---|---|---:|---|

## 8. Retest

| Retest Date | Changed Condition | Method | Expected Result | Observed Result | Evidence ID | Decision |
|---|---|---|---|---|---|---|

## 9. Validation Decision

- [ ] Green — sufficient evidence for the stated condition and current stage
- [ ] Amber — rely only with documented conditions
- [ ] Red — do not rely on the control
- [ ] More evidence required

Decision owner:

Validator:

Conditions:

Residual risk:

Expiration or next validation date:

## Limitations

A successful test demonstrates only the tested condition, scope, environment, and time. It does not prove universal effectiveness or future operation.

## Navigation

- Previous: [Threat-Control-Evidence Map](threat-control-evidence-map.md)
- Next: [Recovery Assurance Record](recovery-assurance-record.md)
- Final decision: [Review Decision](../02-evidence-manifests/review-decision-template.md)
- Back to toolkit: [START_HERE.md](../START_HERE.md)
