# Incident and Near-Miss Review
> **Artifact type:** TEMPLATE  
> **Completion status:** Blank for reuse  
> **Required for:** Conditional: incident, near miss, or exercise

## What this document is

A defensible record for separating observed facts, analyst interpretation, decisions, response actions, recovery, corrective action, and retest evidence.

## Who should complete it

Incident responders, system owners, investigators, security operations teams, legal or privacy stakeholders where required, and accountable decision owners.

## When to use it

Use for confirmed incidents, suspected incidents, significant alerts, integrity events, AI or automation failures, supplier events, near misses, and recovery exercises.

## Decision supported

What happened, what remains uncertain, what response is authorized, what must be corrected, and whether the system may return to the approved operating state.

## Incident / Near-Miss Name

## Record ID

## Date / Time

## System / Asset

## Incident Owner

## Decision Owner

## 1. Initial Question and Hypothesis

Investigation question:

Initial hypothesis:

Alternative explanations:

## 2. Classification

- [ ] Security incident
- [ ] Privacy incident
- [ ] Availability incident
- [ ] Integrity incident
- [ ] AI or automation incident
- [ ] Software or supplier incident
- [ ] Physical or environmental incident
- [ ] Near miss
- [ ] Other:

## 3. Observed Facts

Record only observations directly supported by evidence.

| Fact ID | Observation | Time | Evidence ID | Source | Confidence |
|---|---|---|---|---|---|

## 4. Interpretation and Inference

| Inference ID | Interpretation | Supporting Fact IDs | Alternative Explanation | Confidence | Reviewer |
|---|---|---|---|---|---|

Do not present inference, attribution, or legal conclusions as observed fact.

## 5. Impact

| Impact Area | Observed or Potential | Evidence ID | Notes |
|---|---|---|---|
| Confidentiality | | | |
| Integrity | | | |
| Availability | | | |
| Safety / mission | | | |
| Financial | | | |
| Legal / compliance | | | |
| Public trust | | | |

## 6. Timeline

| Time | Event | Actor / System | Fact or Inference | Evidence ID |
|---|---|---|---|---|

## 7. Response Decisions

| Decision ID | Proposed Action | Required Approver | Evidence Package | Decision | Conditions | Execution Confirmation |
|---|---|---|---|---|---|---|

AI may summarize, correlate, and recommend. Human authorization remains required for consequential containment, attribution, notification, legal conclusions, destructive actions, and acceptance of residual risk.

## 8. Containment and Recovery

| Action ID | Action | Owner | Approval | Start / End | Result | Evidence ID | Rollback |
|---|---|---|---|---|---|---|---|

## 9. Root Cause and Contributing Factors

| Factor ID | Factor | Evidence ID | Confidence | Corrective Action |
|---|---|---|---|---|

## 10. Corrective Actions and Retest

| Action ID | Corrective Action | Owner | Due Date | Validation Method | Retest Evidence ID | Result | Status |
|---|---|---|---|---|---|---|---|

## 11. Final Review Decision

- [ ] Incident closed
- [ ] Closed with continuing monitoring
- [ ] Return to service approved with conditions
- [ ] More evidence required
- [ ] Remains open
- [ ] Escalation required

Decision owner:

Reviewer:

Residual risk:

Unresolved uncertainty:

Lessons incorporated into architecture or operations:

Next review date:

## Limitations

This template does not establish attribution, legal responsibility, compliance status, or forensic admissibility by itself.
