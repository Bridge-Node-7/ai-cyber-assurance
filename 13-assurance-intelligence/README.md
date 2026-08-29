# Assurance Intelligence

> **Artifact type:** CAPABILITY GUIDE  
> **Completion status:** Reference document  
> **Operational authority:** None

Assurance Intelligence adds a small machine-readable layer to AI Cyber Assurance. It does not replace the existing Quick Review, Full Assurance Lifecycle, specialist modules, or human decision process.

Its purpose is to keep one bounded assurance case structurally consistent from evidence through decision, corrective action, retest, and generated communication artifacts.

## Core flow

```text
Scope
→ Claims
→ Evidence
→ Findings
→ Controls
→ Human Decision
→ Corrective Action
→ Retest
→ Verified Closure
```

## One bounded decision, multiple views

Assurance Case schema v0.2 represents exactly one bounded human decision and is the source for:

- a Decision Receipt;
- an Assurance Passport; and
- an Executive Summary.

Generated views are communication artifacts, not separate sources of truth. Renderer prose is derived from the canonical case rather than from scenario-specific assumptions.

## Evidence classes

Use the repository evidence classes exactly:

- **Observed**
- **Tested**
- **Reported**
- **Inferred**
- **Unknown**

Confidence is separate from evidence class. If confidence is stated, record the basis.

## Relationship and authority invariants

The validator enforces typed references between claims, evidence, findings, controls, decisions, corrective actions, retests, and identities.

Nonhuman identities require an accountable human identity reference. The bounded case decision requires named human authority. Corrective actions preserve decision linkage. Closed findings require completed corrective action, successful retest, non-Unknown closure evidence, and matching finding relationships. Retests record whether they were independent; non-independent retests require a rationale.

## Validation boundary

`validate_assurance_case.py` checks structural consistency, typed relationship integrity, date fields, required authority fields, evidence-class discipline, and closure preconditions.

A validation pass does **not** establish that evidence is authentic or sufficient, that a control is effective in a real environment, that a system is secure or compliant, or that deployment or operation is authorized.

The JSON Schema documents the case envelope and key local field constraints. The standard-library Python validator is the executable authority for cross-object relational invariants, with regression tests checking key schema/validator parity.

## Public and private boundary

Public examples in this repository are synthetic and fictional.

For real work, create a private or access-controlled partner package outside this public repository. Keep real architecture, evidence, telemetry, supplier information, vulnerabilities, regulated data, credentials, and proprietary material in that controlled location.

See [Partner Start Here](partner-kit/START_HERE.md).

## Commands

Validate a case:

```bash
python scripts/validate_assurance_case.py path/to/assurance-case.json
```

Render deterministic views:

```bash
python scripts/render_assurance_outputs.py path/to/assurance-case.json
```

The renderer validates the case before producing output.

## Synthetic proofs

- [AI-agent assurance case](../10-examples/synthetic-ai-agent-assurance/) — identity authority, logging, corrective action, and retest.
- [Cryptographic assurance case](../10-examples/synthetic-cryptographic-assurance-case/) — a distinct non-AI domain proving generic rendering and relational validation.
