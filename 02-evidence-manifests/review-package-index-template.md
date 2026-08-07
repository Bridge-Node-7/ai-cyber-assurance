# Review Package Index

> **Artifact type:** TEMPLATE  
> **Completion status:** Blank for reuse  
> **Required for:** Quick Review and Full Assurance Lifecycle packages

Use this record as the home page and status authority for one review package. Keep sensitive evidence in an approved private location and reference it by controlled location or evidence ID.

## Package Metadata

| Field | Value |
|---|---|
| Package ID | |
| System or workflow | |
| System version | |
| Review path | Quick Review / Full Assurance Lifecycle |
| Scope | |
| System owner | |
| Review lead | |
| Decision owner | |
| Review date | |
| Review expiration | |
| Sensitivity | |
| Evidence storage location or reference | |

## Controlled Values

### Applicability

Use exactly one:

- **Required**
- **Conditional**
- **Not Applicable**

### Status

Use exactly one for each applicable record:

- **Not Started**
- **Draft**
- **Blocked**
- **Ready for Review**
- **Complete**

Applicability and status are separate. Document the reason for every **Not Applicable** decision.

## Artifact Matrix

| Record | Applicability | Status | Owner | Location | Blocking gap |
|---|---|---|---|---|---|
| Review Package Index | Required | Draft | | | |
| Evidence Manifest | Required | Not Started | | | |
| AI Agent Security | Conditional | Not Started | | | |
| Human Approval Gates | Conditional | Not Started | | | |
| Zero Trust Readiness | Conditional | Not Started | | | |
| LLM and Generative AI Risk | Conditional | Not Started | | | |
| Secure-by-Design Review | Conditional | Not Started | | | |
| Software and AI Supply Chain Readiness | Conditional | Not Started | | | |
| Cyber Survivability Review | Conditional | Not Started | | | |
| High-Impact System Readiness | Conditional | Not Started | | | |
| Incident Review | Conditional | Not Started | | | |
| Security Policy and Target | Conditional | Not Started | | | |
| Identity and Authority Register | Conditional | Not Started | | | |
| Threat-Control-Evidence Map | Conditional | Not Started | | | |
| Control Validation Record | Conditional | Not Started | | | |
| Recovery Assurance Record | Conditional | Not Started | | | |
| Review Decision | Required | Not Started | | | |
| Corrective actions and retest record | Conditional | Not Started | | | |

For a Full Assurance Lifecycle review, apply the minimum completion package in [`ASSURANCE_LIFECYCLE.md`](../ASSURANCE_LIFECYCLE.md).

## Decision Hierarchy

1. **Module assessment**  
   A local conclusion within a specialist record.

2. **Assurance recommendation**  
   The package-level recommendation prepared by the review team, with AI assistance where appropriate.

3. **Final assurance decision**  
   The bounded decision made by the authorized human decision owner.

A module assessment or AI-assisted recommendation does not replace the final assurance decision.

## Package-Level Evidence Gaps

| Gap ID | Missing or conflicting evidence | Affected record | Owner | Due date | Blocking? |
|---|---|---|---|---|---|

## Package-Level Corrective Actions

| Action ID | Action | Owner | Due date | Required evidence | Retest status |
|---|---|---|---|---|---|

## Assurance Recommendation

- [ ] Green
- [ ] Amber
- [ ] Red
- [ ] More Evidence Required

Recommendation owner:

Date:

Scope and conditions:

## Required Human Decisions

| Decision | Authorized owner | Authority basis | Required by | Status |
|---|---|---|---|---|

## Final Assurance Decision

- [ ] Green
- [ ] Amber
- [ ] Red
- [ ] More Evidence Required

Decision owner:

Authority basis:

Decision date:

Expiration or next review date:

Scope:

Conditions and prohibited uses:

Accepted residual risks:

Limitations:

## Package Completion Rule

A package is not complete until:

- Every Required record is Complete.
- Every Conditional record is Complete or justified as Not Applicable.
- Blocking gaps are resolved or explicitly accepted by an authorized decision owner.
- Corrective actions and retest status are recorded where applicable.
- The final assurance decision is recorded with scope, conditions, owner, date, expiration, and limitations.
