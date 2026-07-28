# Recovery Assurance Record
> **Artifact type:** TEMPLATE  
> **Completion status:** Blank for reuse  
> **Required for:** Full Assurance Lifecycle when recovery is material

## What this document is

An execution-focused record for testing recovery, rollback, revocation, restoration, degraded operation, or manual fallback.

## Who should complete it

Recovery owners, operators, system owners, incident responders, continuity leads, and accountable reviewers.

## When to use it

Use before making recovery claims, after significant change, during exercises, following incidents, and after corrective action.

## Decision supported

Whether the reviewed recovery capability has been executed successfully for a defined condition and may be relied upon with stated limitations.

## Record Information

| Field | Value |
|---|---|
| Recovery Record ID | |
| System / Workflow | |
| Version | |
| Recovery Owner | |
| Test Owner | |
| Reviewer | |
| Test Date | |

## 1. Recovery Objective

Recovery capability being tested:

Mission or business function supported:

Trigger or failure condition:

Expected recovery time:

Expected data or state loss:

Required human approval:

## 2. Scope and Preconditions

Environment:

In-scope components:

Out-of-scope components:

Dependencies:

Required backup, rollback, key, credential, or alternate capability:

Stop conditions:

Safety and public-impact constraints:

## 3. Procedure

| Step | Action | Responsible Identity | Approval Required? | Expected Result | Rollback / Stop Point |
|---|---|---|---:|---|---|

## 4. Execution Evidence

| Step | Start / End Time | Observed Result | Evidence ID | Pass / Fail / Partial | Deviation |
|---|---|---|---|---|---|

## 5. Outcome

Actual elapsed time:

Actual data or state loss:

Mission or service state after recovery:

Control or identity changes made:

Evidence integrity method:

## 6. Mismatches and Corrective Action

| Finding ID | Expected vs Observed Mismatch | Consequence | Owner | Corrective Action | Due Date | Retest Required? | Status |
|---|---|---|---|---|---|---:|---|

## 7. Retest

| Retest Date | Changed Condition | Expected Result | Observed Result | Evidence ID | Decision |
|---|---|---|---|---|---|

## 8. Recovery Decision

- [ ] Green — demonstrated for the tested condition and current stage
- [ ] Amber — usable only with documented conditions
- [ ] Red — recovery path is not reliable
- [ ] More evidence required

Decision owner:

Reviewer:

Conditions:

Untested dependencies:

Residual risk:

Next test date:

## Limitations

A recovery plan, backup, or written procedure is not proof of recoverability. This record supports only the tested scope, condition, environment, and date.
