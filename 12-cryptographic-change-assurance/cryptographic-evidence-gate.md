# Cryptographic Evidence Gate

> **Artifact type:** TEMPLATE
> **Completion status:** Blank for reuse
> **Required for:** Cryptographic Change Assurance

Use this record when a technical finding, advisory, standards change, policy change, provider notice, test result, or AI-assisted analysis may affect an approved cryptographic state.

The gate prevents an unverified or overgeneralized claim from becoming the basis for a consequential change.

## Evidence Record

| Field | Entry |
|---|---|
| Claim ID |  |
| Evidence ID(s) |  |
| Claim date |  |
| Primitive / profile / implementation in scope |  |
| Conditions and parameters |  |
| Claimed effect |  |
| Explicit limits |  |
| Reviewer |  |
| Current gate state |  |
| Next required evidence |  |

## Gate States

```text
QUARANTINED
→ REPRODUCED
→ CORROBORATED
→ IMPACT-MAPPED
→ HUMAN-AUTHORIZED
→ ACTIONABLE
```

### QUARANTINED

The claim has been received but is not trusted as a basis for consequential action.

Examples include an AI-generated result, unreviewed research result, advisory, report, or alert.

### REPRODUCED

A competent reviewer reproduced or independently verified the material result under documented conditions that are sufficient to understand what was actually demonstrated.

Do not expose exploit-enabling details in a public review package.

### CORROBORATED

Additional competent review, authoritative confirmation, or independent evidence supports the bounded claim and its limitations.

Corroboration must not be created by copying the same underlying source into multiple records.

### IMPACT-MAPPED

The supported claim has been mapped to the actual in-scope cryptographic uses, implementations, parameter sets, dependencies, and persistent state.

Non-applicable uses are excluded with evidence. Unknown applicability remains Unknown.

### HUMAN-AUTHORIZED

The authorized human decision owner approves using the bounded finding as a basis for change planning, testing, restriction, or another stated response.

This state does not itself authorize production execution.

### ACTIONABLE

The evidence state, impact map, authority, required controls, and change boundary are sufficient for the specific planned action to enter the approved change process.

A different action or broader scope requires a new review.

## Transition Record

| From | To | Evidence required | Reviewer / authority | Date | Result |
|---|---|---|---|---|---|
| QUARANTINED | REPRODUCED |  |  |  |  |
| REPRODUCED | CORROBORATED |  |  |  |  |
| CORROBORATED | IMPACT-MAPPED |  |  |  |  |
| IMPACT-MAPPED | HUMAN-AUTHORIZED |  |  |  |  |
| HUMAN-AUTHORIZED | ACTIONABLE |  |  |  |  |

## AI Boundary

AI may assist with organization, comparison, test planning, evidence summarization, dependency mapping, and consistency checks.

An AI-generated conclusion alone cannot advance a claim to **HUMAN-AUTHORIZED** or **ACTIONABLE**.

## Scope Boundary

A result against a reduced, modified, experimental, misconfigured, or otherwise different construction must not be silently generalized to a production construction.

Record exactly what was demonstrated, what was not demonstrated, and what evidence connects the claim to the in-scope system.
