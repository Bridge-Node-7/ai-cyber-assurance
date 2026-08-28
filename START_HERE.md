# Start Here

> **Artifact type:** NAVIGATOR  
> **Completion status:** Reference document  
> **Required for:** Quick Review and Full Assurance Lifecycle

AI Cyber Assurance helps teams organize evidence and make accountable human decisions about AI-enabled and high-impact systems.

> **Safety boundary:** Create a private or access-controlled working package outside this public repository before adding real evidence. Do not place secrets, customer information, private infrastructure, vulnerabilities, regulated data, proprietary material, or sensitive operational evidence in this repository or a public fork.

## What You Will Produce

A completed review package connects:

```text
Scope
→ Applicable records
→ Evidence
→ Findings
→ Corrective actions
→ Assurance recommendation
→ Final human decision
```

Start every review with the [Review Package Index](02-evidence-manifests/review-package-index-template.md).

## 1. Choose a Review Path

### Quick Review

Use a Quick Review for one bounded workflow, product change, pilot, supplier decision, incident, or release.

Minimum path:

1. [Review Package Index](02-evidence-manifests/review-package-index-template.md)
2. [Evidence Manifest](02-evidence-manifests/evidence-manifest-template.md)
3. Applicable specialist records
4. [Decision Rubric](DECISION_RUBRIC.md)
5. [Review Decision](02-evidence-manifests/review-decision-template.md)

### Full Assurance Lifecycle

Use the [Full Assurance Lifecycle](ASSURANCE_LIFECYCLE.md) when the system is high-impact, operational, multi-party, dependent on external services, able to change external state, or expected to support consequential decisions.

### Cryptographic Change Assurance

Use [Cryptographic Change Assurance](12-cryptographic-change-assurance/README.md) when approved cryptography may need to be replaced, withdrawn, or revalidated. Keep the change trigger, affected dependencies, persistent state, Unknowns, substitution evidence, verification, and final human authority explicit.

### Optional Structured Assurance Case

After selecting Quick Review or Full Assurance Lifecycle, use [Assurance Intelligence](13-assurance-intelligence/README.md) when one machine-readable evidence-to-decision record would reduce reconciliation or reporting drift.

The Assurance Case is a representation of the bounded review. It does not create a separate decision hierarchy.

## 2. Create the Private Package

1. Create a private or access-controlled folder outside this repository.
2. Copy the Review Package Index into that folder.
3. Assign a package ID.
4. Record the system, scope, owners, decision authority, review date, expiration, and sensitivity.
5. Reference sensitive evidence by controlled location or evidence ID. Do not copy sensitive evidence into the public toolkit.

For a structured case, the private package may include `assurance-case.json` and generated views. Keep the real underlying evidence in the approved controlled location.

## 3. Select Applicable Records

For each record, use one applicability value:

- **Required**
- **Conditional**
- **Not Applicable**

For each applicable record, use one status value:

- **Not Started**
- **Draft**
- **Blocked**
- **Ready for Review**
- **Complete**

Document the reason for every **Not Applicable** decision.

## 4. Gather and Classify Evidence

Record facts, sources, owners, dates, integrity methods, limitations, and evidence gaps.

When AI assists, use the evidence classes and operating rules in [AGENTS.md](AGENTS.md):

- Observed
- Tested
- Reported
- Inferred
- Unknown

AI must not silently convert reported or inferred information into observed or tested evidence.

## 5. Use AI Safely

AI may organize, draft, map, question, summarize, check, and validate structural relationships.

Authorized humans remain responsible for:

- Granting access or privileges
- Approving intrusive or consequential actions
- Validating material facts
- Accepting residual risk
- Approving suppliers, releases, deployments, or operations
- Declaring incident closure
- Making the final assurance decision

## 6. Apply the Decision Hierarchy

1. **Module assessment:** local conclusion within a specialist record.
2. **Assurance recommendation:** package-level recommendation prepared by the review team, with AI assistance where appropriate.
3. **Final assurance decision:** bounded decision made by the authorized human decision owner.

Only the final assurance decision grants the disposition recorded for the stated scope and period.

Generated Decision Receipts, Assurance Passports, and Executive Summaries communicate the decision; they do not create authority independently.

## 7. Validate

Run the public repository validator from the repository root:

```bash
python scripts/validate_repo.py --root .
```

For a structured Assurance Case:

```bash
python scripts/validate_assurance_case.py path/to/assurance-case.json
```

The repository validator checks the controlled public toolkit. The Assurance Case validator checks structural consistency, evidence-class discipline, reference integrity, required human authority fields, and closure preconditions.

The validator does not prove that a private completed review is factually correct, that evidence is authentic or sufficient, that a control works in a real environment, or that a system is authorized. The Assurance Case validator has the same factual boundary.

## 8. Generate Consistent Views

After a case validates:

```bash
python scripts/render_assurance_outputs.py path/to/assurance-case.json
```

The renderer produces a Decision Receipt, Assurance Passport, and Executive Summary from the same canonical case.

## 9. Complete and Preserve the Review

A package is complete only when:

- Every Required record is Complete.
- Every Conditional record is Complete or justified as Not Applicable.
- Blocking gaps are resolved or explicitly accepted by an authorized decision owner.
- Corrective actions and retest status are recorded where applicable.
- The final assurance decision is recorded with scope, conditions, owner, date, expiration, and limitations.
- If an Assurance Case is used, it passes structural validation and its generated views remain consistent with the canonical record.

Preserve the completed package and supporting evidence in the approved private location.
