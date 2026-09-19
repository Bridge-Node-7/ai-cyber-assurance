# Automated Review Assistance

Use this guide when automated assistance supports interpretation or application of the AI Cyber Assurance toolkit. This guide does not grant system access, evidence access, decision authority, release authority, or permission to handle sensitive information.

## Scope

Automated assistance may help a user apply the toolkit to a bounded system or workflow. The system, scope, review path, and decision authority must be stated before substantive work begins.

## Human Authority

Automated assistance may support analysis and preparation. Authorized humans retain authority over consequential access, testing, production actions, risk acceptance, supplier decisions, incident declarations, public claims, release approval, and the final assurance decision.

## Evidence Classes

Use one evidence class for every material statement:

| Class | Meaning |
|---|---|
| **Observed** | Directly seen in an authorized source or system |
| **Tested** | Produced by an executed and documented test |
| **Reported** | Supplied by an identified person or organization |
| **Inferred** | Analytical conclusion supported by stated evidence |
| **Unknown** | Missing, inaccessible, conflicting, stale, or unverified |

Reported or Inferred information must not be silently presented as Observed or Tested.

## Automated Assistance May

Automated assistance may:

- Explain the toolkit and its limitations
- Recommend Quick Review or Full Assurance Lifecycle
- Select potentially applicable records
- Ask structured questions
- Draft records from supplied evidence
- Map risks, requirements, controls, evidence, findings, and corrective actions
- Identify contradictions and missing evidence
- Suggest authorized validation or test activities
- Run authorized local repository validation
- Prepare a bounded assurance recommendation
- Summarize required human decisions

## Automated Assistance Must

Automated assistance must:

- State the system, scope, decision authority, and review path
- Distinguish evidence classes
- Cite the supporting file, evidence ID, test result, interview, or other source
- Preserve uncertainty, dissent, and limitations
- Mark missing information as Unknown
- Ask rather than guess when a material fact is unavailable
- Identify all required human decisions
- Stop before consequential authority gates
- Keep conclusions bounded by scope, evidence date, and expiration
- State what the repository validator does and does not prove

## Automated Assistance Must Not

Automated assistance must not:

- Invent evidence, sources, tests, approvals, or access
- Claim access it did not have
- Assume a documented control is implemented, operating, tested, or effective
- Place sensitive information in this public repository or a public fork
- Access systems, accounts, evidence stores, or tools without authorization
- Execute intrusive, destructive, or consequential tests without approval
- Accept residual risk
- Approve a supplier, release, deployment, or operation
- Grant or remove privileges
- Declare an incident closed
- Close a corrective action without supporting retest evidence
- Sign or issue the final assurance decision

## Required Output

A substantive automated review should present:

1. Scope
2. Review path
3. Applicable records
4. Observed and Tested evidence
5. Reported information
6. Inferences
7. Unknowns and evidence gaps
8. Findings
9. Corrective actions
10. Assurance recommendation
11. Required human decisions
12. Limitations and expiration

## Stop Conditions

Stop and request authorized human direction when:

- Scope or decision authority is unclear
- Required evidence is inaccessible
- Evidence conflicts materially
- Sensitive information may be exposed
- A proposed action changes access, production, data, supplier, incident, or release state
- Residual risk acceptance is required
- A final decision or public claim is requested

## Validation Boundary

The repository validator checks the controlled public toolkit. It does not independently establish the truth, sufficiency, authenticity, or operational effectiveness of evidence in a private completed review.
