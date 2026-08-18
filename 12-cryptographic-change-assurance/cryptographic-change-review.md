# Cryptographic Change Review

> **Artifact type:** TEMPLATE
> **Completion status:** Blank for reuse
> **Required for:** Cryptographic Change Assurance

## Review Control

| Field | Entry |
|---|---|
| Review ID |  |
| System or boundary |  |
| Review owner |  |
| Decision owner |  |
| Change trigger |  |
| Trigger date |  |
| Review date |  |
| Review expiration or reassessment date |  |
| Evidence IDs |  |
| Sensitivity |  |

## 1. Change Trigger

State exactly what changed or may change. Keep the claim bounded to the supported primitive, parameter set, protocol profile, implementation, provider, key or trust configuration, policy, or support condition.

| Question | Entry |
|---|---|
| What condition changed? |  |
| What current authorization may be affected? |  |
| What is explicitly not established by the trigger? |  |
| What evidence supports the trigger? |  |
| What evidence remains missing or disputed? |  |

Do not generalize a research result, test result, advisory, or AI-generated finding beyond the conditions supported by reviewed evidence.

## 2. Cryptographic Dependency Map

Record every material in-scope use that could be affected.

| Usage ID | Asset or service | Cryptographic function | Primitive / profile | Implementation or provider | Dependency evidence ID | Owner | Status / unknown |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |

Include relevant certificates, trust anchors, signing paths, update paths, recovery paths, libraries, hardware, protocols, archived state, backups, and external dependencies.

A critical dependency that is not mapped remains **Unknown**.

## 3. State Mobility

Use these repository-specific working classes to make persistent-state migration explicit.

| Class | Meaning | Typical treatment |
|---|---|---|
| **SM-0** | Ephemeral or session state | Recreate, renegotiate, or expire |
| **SM-1** | Renewable or short-lived state | Replace through bounded renewal |
| **SM-2** | Key-rewrappable state | Rewrap or rotate the protecting key hierarchy where supported |
| **SM-3** | Bulk re-encryptable state | Plan controlled migration, capacity, rollback, and integrity verification |
| **SM-4** | Immutable, archival, or evidentiary state | Preserve required validity and access with an approved long-term treatment |

| State ID | Asset or data set | Mobility class | Volume / horizon | Migration method | Recovery method | Verification evidence | Unknown / blocker |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |

A material affected state that cannot be classified prevents a Green module assessment.

## 4. Cryptographic Blast Radius

No aggregate blast-radius score is used.

| Dimension | Current finding | Evidence | Limitation / unknown |
|---|---|---|---|
| Mission or business consequence |  |  |  |
| Affected assets and services |  |  |  |
| Persistent-state burden |  |  |  |
| Dependency depth and coupling |  |  |  |
| Policy or jurisdiction constraints |  |  |  |
| Replacement availability |  |  |  |
| Unresolved dependencies |  |  |  |

## 5. Substitution Readiness

| Candidate path | Functional compatibility | Protocol / interface compatibility | Key / trust changes | State migration | Recovery / rollback | Test evidence | Blocker |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |

A replacement option is not ready merely because an alternate algorithm exists. Readiness requires a supported path through the actual implementation, dependencies, state, policy, and verification requirements.

## 6. Time to Safe Substitution

Record defender-controlled stages only.

| Stage | Measured or bounded duration | Evidence basis | Unknown / blocker |
|---|---|---|---|
| Evidence intake |  |  |  |
| Validation |  |  |  |
| Decision and authorization |  |  |  |
| Preparation |  |  |  |
| Staging |  |  |  |
| Cutover |  |  |  |
| Persistent-state migration |  |  |  |
| Verification |  |  |  |
| **TSS** |  |  |  |

If any material stage lacks a defensible measurement or bound, report **Time to Safe Substitution: Unknown**.

## 7. Pre-Cutover Review

| Check | Result | Evidence | Required action |
|---|---|---|---|
| Functional behavior |  |  |  |
| Interoperability |  |  |  |
| Performance and resource constraints |  |  |  |
| Protocol and message-size effects |  |  |  |
| Key and trust handling |  |  |  |
| Persistent-state treatment |  |  |  |
| Monitoring and alerting |  |  |  |
| Recovery and rollback |  |  |  |
| Deprecated-crypto fallback blocked |  |  |  |

A rollback path must not silently restore a cryptographic state that current policy prohibits.

## 8. Module Assessment

Use the repository [Decision Rubric](../DECISION_RUBRIC.md).

| Field | Entry |
|---|---|
| Module assessment | Green / Amber / Red / More Evidence Required |
| Supported conclusion |  |
| Blocking unknowns |  |
| Conditions |  |
| Corrective actions |  |
| Retest evidence required |  |
| Reassessment trigger |  |

**Green is unavailable while a material critical dependency or affected persistent state remains Unknown.**

This module assessment does not authorize a production change. The final assurance decision remains with the authorized human decision owner.
