# Cyber Survivability Review
> **Artifact type:** TEMPLATE  
> **Completion status:** Blank for reuse  
> **Required for:** Conditional: material disruption or recovery risk

## What this document is

A mission-aware review of whether a system can anticipate, withstand, recover from, and adapt to cyber disruption.

## Who should complete it

System owners, operators, security engineers, continuity leads, incident responders, and recovery owners.

## When to use it

Use for high-impact systems, material dependencies, AI-enabled workflows, critical releases, major architectural changes, and post-incident improvement.

## Decision supported

Whether survivability evidence is sufficient for the current stage and whether recovery claims have been demonstrated or remain untested.

## System / Mission

## Version

## Owner

## Review Date

## 1. Mission Consequence

What mission, service, safety, business, or public-interest outcome is affected if the system is degraded, denied, manipulated, or compromised?

## 2. Critical Functions and Dependencies

| Function | Maximum Acceptable Disruption | Dependency | Failure Mode | Owner | Evidence ID |
|---|---|---|---|---|---|

## 3. Anticipate

| Area | Expected Capability | Evidence ID | Gap | Owner |
|---|---|---|---|---|
| Asset and dependency awareness | | | | |
| Threat and failure-mode analysis | | | | |
| Identity and privilege review | | | | |
| Supplier and third-party awareness | | | | |
| Detection requirements | | | | |
| Recovery planning | | | | |

## 4. Withstand

| Scenario | Expected Degraded Behavior | Preventive / Protective Control | Human Authority | Evidence ID |
|---|---|---|---|---|
| Loss of connectivity | | | | |
| Compromised identity | | | | |
| Data-integrity concern | | | | |
| AI-agent or tool malfunction | | | | |
| Supplier or provider failure | | | | |
| Ransomware or destructive event | | | | |

## 5. Recover

| Recovery Objective | Recovery Path | Responsible Owner | Required Approval | Expected Time | Evidence ID |
|---|---|---|---|---|---|
| Restore configuration | | | | | |
| Restore data | | | | | |
| Disable automation | | | | | |
| Revoke access | | | | | |
| Roll back release | | | | | |
| Resume critical operations | | | | | |

## 6. Adapt

| Lesson / Changed Condition | Required Design or Process Change | Owner | Due Date | Validation Method | Status |
|---|---|---|---|---|---|

## 7. Executed Recovery Evidence

Do not mark recovery as demonstrated based only on a plan or backup.

| Test ID | Test Condition | Expected Result | Observed Result | Elapsed Time | Evidence ID | Mismatch | Corrective Action | Retest Result |
|---|---|---|---|---|---|---|---|---|

## 8. Survivability Decision

- [ ] Green — sufficient evidence for the current stage
- [ ] Amber — proceed only with documented conditions
- [ ] Red — do not proceed
- [ ] More evidence required

Reviewer:

Decision owner:

Conditions:

Untested assumptions:

Residual risk:

Next test date:

## Limitations

A completed review is not proof that the system will survive every event. Claims should distinguish planned, implemented, observed, tested, and independently validated capabilities.

## Navigation

- Evidence source: [Evidence Manifest](../02-evidence-manifests/evidence-manifest-template.md)
- Full recovery record: [Recovery Assurance Record](../11-assurance-lifecycle/recovery-assurance-record.md)
- Decision semantics: [Decision Rubric](../DECISION_RUBRIC.md)
- Back to toolkit: [START_HERE.md](../START_HERE.md)
