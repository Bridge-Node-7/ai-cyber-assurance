# Cryptographic Withdrawal Exercise

> **Artifact type:** TEMPLATE
> **Completion status:** Blank for reuse
> **Required for:** Cryptographic Change Assurance when withdrawal readiness is material

A withdrawal exercise tests whether a scoped system can move away from an approved cryptographic dependency without hiding unknowns, losing required state, silently falling back, or skipping verification.

The public method supports tabletop and nonproduction exercises. It does not authorize production changes.

## Exercise Control

| Field | Entry |
|---|---|
| Exercise ID |  |
| System or boundary |  |
| Exercise owner |  |
| Decision owner |  |
| Scenario trigger |  |
| Execution mode | Tabletop / nonproduction / other authorized mode |
| Start time |  |
| End time |  |
| Evidence IDs |  |

## Preconditions

Confirm before the exercise:

- the change trigger has an appropriate Cryptographic Evidence Gate state;
- in-scope cryptographic dependencies are mapped;
- material persistent state has a mobility class or is recorded as Unknown;
- candidate substitution paths and major blockers are visible;
- rollback and recovery expectations are defined;
- the authorized exercise boundary is documented.

## Scenario

At the declared exercise start, treat the selected primitive, profile, implementation, provider, key or trust configuration, or policy state as unavailable or disallowed for the stated scope.

Do not broaden the injected condition beyond the approved scenario.

## Exercise Phases

| Phase | Expected result | Observed result | Evidence | Gap / action |
|---|---|---|---|---|
| Detect and intake |  |  |  |  |
| Validate trigger |  |  |  |  |
| Map affected dependencies |  |  |  |  |
| Confirm state mobility |  |  |  |  |
| Select bounded substitution path |  |  |  |  |
| Complete pre-cutover review |  |  |  |  |
| Simulate or perform authorized transition |  |  |  |  |
| Verify functional and security outcomes |  |  |  |  |
| Verify no silent fallback |  |  |  |  |
| Review recovery / rollback |  |  |  |  |

## Time to Safe Substitution

Record measured or bounded duration for each defender-controlled stage.

| Stage | Duration | Evidence |
|---|---|---|
| Evidence intake |  |  |
| Validation |  |  |
| Decision and authorization |  |  |
| Preparation |  |  |
| Staging |  |  |
| Cutover |  |  |
| Persistent-state migration |  |  |
| Verification |  |  |
| **TSS** |  |  |

If a material stage is Unknown, the exercise must not publish a precise TSS total.

## Exercise Findings

| Finding ID | Finding | Evidence | Severity / importance | Owner | Corrective action | Retest |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

## Exit Conditions

A completed exercise must make these conditions explicit:

- affected critical dependencies are resolved or remain visibly Unknown;
- affected persistent state is classified and accounted for;
- the proposed path has bounded functional, interoperability, key/trust, and recovery evidence;
- prohibited cryptography does not silently return through fallback or rollback;
- verification results are recorded;
- corrective actions and retest requirements have owners.

## Exercise Disposition

| Field | Entry |
|---|---|
| Exercise status | Complete / Incomplete |
| Module assessment | Green / Amber / Red / More Evidence Required |
| Blocking unknowns |  |
| Corrective actions |  |
| Retest required |  |
| Next reassessment trigger |  |

The exercise disposition is decision support. It does not authorize production operation or certify cryptographic safety.
