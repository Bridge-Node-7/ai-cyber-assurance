# Assurance Intelligence

> **Artifact type:** CAPABILITY GUIDE  
> **Completion status:** Reference document  
> **Operational authority:** None

Assurance Intelligence adds an optional machine-readable layer to AI Cyber Assurance. The Markdown templates remain sufficient for many bounded reviews; this layer is for teams that need stronger structural validation, repeatable generated views, or partner-to-partner interchange.

It does not replace Quick Review, Full Assurance Lifecycle, specialist modules, or the human decision process.

Its purpose is to keep one bounded assurance case consistent from evidence through decision, corrective action, retest, and generated communication artifacts.

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

Assurance Case schema v0.3 represents exactly one bounded human decision and is the source for:

- a Decision Receipt;
- an Assurance Passport; and
- an Executive Summary.

Generated views are communication artifacts, not separate sources of truth. Renderer prose is derived from the canonical case rather than from scenario-specific assumptions.

The renderer treats case-controlled free text as untrusted presentation data: Markdown structural characters and raw HTML are escaped, Unicode formatting controls are rejected by validation, and output-fidelity checks prevent a case field from creating a forged `Human decision` section.

## Decision vocabulary

The canonical case records one human decision status using the repository rubric:

- **Green** — Approved / Ready / Proceed;
- **Amber** — Approved with conditions / Ready with constraints;
- **Red** — Not approved / Not ready / Stop;
- **More evidence required** — Undetermined.

Amber cases require an explicit permitted scope, conditions, due date, prohibited actions, monitoring requirements, required retests, and expiration/review boundary. A blank field is not treated as proof that nothing exists.

For list-valued decision fields such as conditions and missing evidence, record an explicit state:

- `items_recorded`;
- `none_identified`;
- `not_assessed`;
- `not_applicable`;
- `unknown`.

This preserves the distinction between an affirmative negative and missing or unassessed information.

## Evidence classes

Use the repository evidence classes exactly:

- **Observed**
- **Tested**
- **Reported**
- **Inferred**
- **Unknown**

Confidence is separate from evidence class. If confidence is stated, record the basis.

## Relationship, authority, and chronology invariants

The validator enforces typed references between claims, evidence, findings, controls, decisions, corrective actions, retests, and identities.

Nonhuman identities require an accountable human identity reference. The bounded case decision requires named human authority. Corrective actions preserve decision linkage. Closed findings require completed corrective action, successful retest, non-Unknown closure evidence, and matching finding relationships. Retests record whether they were independent; non-independent retests require a rationale.

Material claims, risks, controls, and findings require statements so a structurally valid case cannot silently render blank material sections.

Dates are validated as ISO dates. Evidence cannot post-date the review cutoff; finding, corrective-action, retest, closure, and review-history dates must preserve a coherent chronology within the bounded case.

## Currency

Historical records remain structurally valid after they expire, but currency is reported separately as:

- `CURRENT`;
- `EXPIRED`;
- `NOT_YET_CURRENT`.

Use `--require-current` when a current decision depends on the case still being within its review window.

## Validation boundary

`validate_assurance_case.py` checks structural consistency, typed relationship integrity, material statement presence, date/chronology fields, required authority fields, evidence-class discipline, decision-state semantics, and closure preconditions.

A validation pass does **not** establish that evidence is authentic or sufficient, that a control is effective in a real environment, that a system is secure or compliant, or that deployment or operation is authorized.

The JSON Schema documents the case envelope and material local field constraints. The standard-library Python validator is the executable authority for cross-object relational, chronology, and policy invariants, with regression tests checking schema/validator parity for the material contract.

## Public and private boundary

Public examples in this repository are synthetic and fictional.

For real work, create a private or access-controlled partner package outside this public repository. Keep real architecture, evidence, telemetry, supplier information, vulnerabilities, regulated data, credentials, and proprietary material in that controlled location.

Start with [Partner Start Here](partner-kit/START_HERE.md), read the [Confidentiality Boundary](partner-kit/confidentiality-boundary.md), then use the [Assurance Case Intake Template](partner-kit/intake-template.md).

## Commands

Validate a case:

```bash
python scripts/validate_assurance_case.py path/to/assurance-case.json --as-of YYYY-MM-DD
```

Require the review to be current for that date:

```bash
python scripts/validate_assurance_case.py path/to/assurance-case.json --as-of YYYY-MM-DD --require-current
```

Render safe deterministic views:

```bash
python scripts/render_assurance_outputs.py path/to/assurance-case.json --as-of YYYY-MM-DD
```

The renderer validates the case before producing output and refuses to overwrite an existing generated set unless `--force` is supplied deliberately.

## Synthetic proofs

- [AI-agent assurance case](../10-examples/synthetic-ai-agent-assurance/) — identity authority, logging, corrective action, retest, and conditional bounded operation.
- [Cryptographic assurance case](../10-examples/synthetic-cryptographic-assurance-case/) — a distinct non-AI domain proving generic rendering and relational validation.

## Navigation

- Partner use: [Partner Start Here](partner-kit/START_HERE.md)
- Decision semantics: [Decision Rubric](../DECISION_RUBRIC.md)
- Full toolkit: [START_HERE.md](../START_HERE.md)
