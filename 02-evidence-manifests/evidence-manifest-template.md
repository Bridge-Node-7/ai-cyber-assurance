# Evidence Manifest
> **Artifact type:** TEMPLATE  
> **Completion status:** Blank for reuse  
> **Required for:** Quick Review and Full Assurance Lifecycle

## What this document is

The primary inventory and evidence package for a system, workflow, asset, review, or release.

## Who should complete it

The system owner and review lead, with input from security, operations, data, supplier, legal, privacy, safety, and mission stakeholders as applicable.

## When to use it

Use at the start of either the Quick Review or Full Assurance Lifecycle.

## System identity

- **System / workflow name:**
- **Version / configuration:**
- **Owner:**
- **Review lead:**
- **Review date:**
- **Decision deadline:**
- **Next review / expiration:**

## Mission and users

Describe the purpose, intended users, supported decision or operation, and consequence if the system is unavailable, manipulated, misused, or wrong.

## System boundary

### In scope

- People and roles:
- Applications and services:
- AI models and agents:
- Tools and APIs:
- Data stores and retrieval sources:
- Infrastructure and environments:
- Facilities and physical dependencies:
- Suppliers and third parties:

### Out of scope

-

### Interfaces and trust boundaries

| Interface / boundary | Source | Destination | Identity used | Data / action | Trust assumption | Evidence ID |
|---|---|---|---|---|---|---|

## Critical assets and dependencies

| Asset / dependency | Type | Owner | Required property | Mission consequence | External dependency? | Evidence ID |
|---|---|---|---|---|---:|---|

Required properties may include confidentiality, integrity, availability, authenticity, provenance, safety, privacy, recoverability, and nonrepudiation.

## Data handled

| Data class | Examples | Source | Allowed use | Access roles | Retention | Release restriction | Evidence ID |
|---|---|---|---|---|---|---|---|
| Public | | | | | | | |
| Internal | | | | | | | |
| Sensitive | | | | | | | |
| Regulated | | | | | | | |
| Mission-critical | | | | | | | |

## AI and automation components

| Component ID | Component | Function | Model / provider / version | Tools and access | Human oversight | Risk level | Owner | Evidence ID |
|---|---|---|---|---|---|---|---|---|

## Control summary

| Control ID | Control area | Requirement | Current status | Evidence ID | Validation status | Gap | Owner | Next action |
|---|---|---|---|---|---|---|---|---|
| | Identity and access | | | | | | | |
| | Logging and monitoring | | | | | | | |
| | Data protection | | | | | | | |
| | Software / AI supply chain | | | | | | | |
| | Incident response | | | | | | | |
| | Recovery and continuity | | | | | | | |
| | Human approval gates | | | | | | | |
| | Configuration and change management | | | | | | | |
| | Supplier / third-party risk | | | | | | | |
| | Physical / environmental dependency | | | | | | | |

## Risk and assumption summary

| Risk / assumption ID | Description | Likelihood | Impact | Uncertainty | Mitigation / validation needed | Owner | Due date | Status |
|---|---|---|---|---|---|---|---|---|

## Evidence register

| Evidence ID | Evidence type | Description | Source / authoritative origin | Collection method | Collection time | Owner | Related control / risk / identity | Integrity method | Confidence | Limitations | Retention | Review date | Supersedes / superseded by | Location |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

Evidence may support implementation, observed operation, testing, review, recovery, decision authority, or corrective action. Clearly distinguish these evidence types.

## Evidence gaps

| Gap ID | Missing evidence | Why it matters | Interim constraint | Owner | Due date | Evidence needed to close |
|---|---|---|---|---|---|---|

## Decision

Use [DECISION_RUBRIC.md](../DECISION_RUBRIC.md).

- [ ] Green — evidence sufficient for current scope and stage
- [ ] Amber — proceed with conditions
- [ ] Red — do not proceed
- [ ] More evidence required

Decision maker:

Authority basis:

Decision date:

Decision expiration / revisit date:

Conditions and constraints:

Residual risks accepted:

Required follow-up:

Notes:
