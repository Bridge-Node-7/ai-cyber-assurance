# Partner Start Here

> **Artifact type:** PARTNER GUIDE  
> **Completion status:** Reference document  
> **Operational authority:** None

Start with the decision that needs to be made, not with the repository structure.

Before recording any real evidence, read the [Confidentiality Boundary](confidentiality-boundary.md). Then use the [Assurance Case Intake Template](intake-template.md) to scope one bounded decision.

## Pilot fit gate

Before building a case, confirm that all of the following are true:

- there is one bounded decision or assurance question;
- an accountable human decision owner exists;
- relevant evidence can be accessed in an authorized controlled workspace;
- the review can state important Unknowns without forcing a premature conclusion.

If there is no material decision to make or no authorized evidence path, stop rather than manufacture a review.

## 1. Define the decision

Record:

- the bounded decision question;
- the system or workflow in scope;
- the accountable human decision owner;
- the review path: Quick Review or Full Assurance Lifecycle;
- the evidence cutoff date and review expiration.

Use the [intake template](intake-template.md) to capture this without putting real sensitive material into the public repository.

## 2. Create a controlled workspace

Create a private or access-controlled working package outside this public repository.

Keep real evidence and sensitive context there. Reference controlled evidence by stable IDs rather than copying it into the public toolkit. Follow the [confidentiality boundary](confidentiality-boundary.md) before collecting or sharing material.

## 3. Build the case

Use the canonical Assurance Case to connect:

```text
Claims
→ Evidence
→ Findings
→ Controls
→ Human Decision
→ Corrective Action
→ Retest
```

Mark unavailable or unresolved information as **Unknown**. Use explicit state fields to distinguish `items_recorded`, `none_identified`, `not_assessed`, `not_applicable`, and `unknown`; absence of input is not treated as proof that nothing exists.

## 4. Validate structure and currency

Run the assurance-case validator before human review. Treat validation failures as structural blockers.

```bash
python scripts/validate_assurance_case.py path/to/assurance-case.json --as-of YYYY-MM-DD --require-current
```

A structurally valid historical case may be retained after expiration, but `--require-current` prevents an expired or not-yet-current review from being treated as current for a new decision.

## 5. Human review

Authorized humans remain responsible for material fact validation, consequential actions, residual-risk acceptance, supplier decisions, release or deployment approval, and the final assurance decision.

Decision status uses the repository vocabulary: **Green**, **Amber**, **Red**, or **More evidence required**. Amber requires explicit scope, conditions, owner/authority, due date, prohibited actions, monitoring, retest requirements, and expiration/review boundary.

## 6. Generate views

After the case validates, generate the Decision Receipt, Assurance Passport, and Executive Summary from the same canonical record.

```bash
python scripts/render_assurance_outputs.py path/to/assurance-case.json --as-of YYYY-MM-DD
```

Generated views escape case-controlled Markdown/HTML so externally supplied text cannot create forged decision sections. Existing generated files are not overwritten unless `--force` is supplied deliberately.

Generated views are communication artifacts. The canonical case remains the source of truth for the bounded review.

## Pilot outputs

A bounded partner pilot should leave behind:

- one scoped Assurance Case;
- explicit evidence gaps and Unknowns;
- named finding and action owners;
- a human Decision Receipt;
- an Assurance Passport for the stated scope;
- an Executive Summary;
- retest and closure evidence when corrective action is part of the case;
- a review date or reversal trigger for any continuing decision.

## Pilot success measures

Useful measures include:

- whether material evidence gaps were discovered early;
- whether technical and executive outputs stayed consistent;
- whether manual reconciliation work was reduced;
- whether the accountable decision owner could see what was known, unknown, required next, and reversible;
- whether the case produced a reusable record for later review.

## Completion

A partner case is ready for bounded review when the decision question is clear, material claims have traceable evidence or explicit Unknowns, findings have owners, consequential decisions name human authority, and closed findings have successful retest evidence.

## Navigation

- Previous: [Assurance Intelligence](../README.md)
- Supporting boundary: [Confidentiality Boundary](confidentiality-boundary.md)
- Next: [Assurance Case Intake Template](intake-template.md)
- Back to toolkit: [START_HERE.md](../../START_HERE.md)
