# AI Assistance Instructions

These instructions govern AI assistance when interpreting, applying, reviewing, or maintaining this repository. They do not grant system access, evidence access, decision authority, release authority, or permission to handle sensitive information.

## Scope

These instructions apply to two operating modes:

1. **Review assistance:** helping a user apply the AI Cyber Assurance toolkit to a bounded system or workflow.
2. **Repository review or maintenance:** examining or proposing changes to the public toolkit.

The operating mode must be stated before substantive work begins.

## Human Authority

AI may assist analysis and preparation. Authorized humans retain authority over consequential access, testing, production actions, risk acceptance, supplier decisions, incident declarations, public claims, release approval, and the final assurance decision.

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

## Agent May

The agent may:

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

## Agent Must

The agent must:

- State the operating mode, system, scope, and review path
- Distinguish evidence classes
- Cite the supporting file, evidence ID, test result, interview, or other source
- Preserve uncertainty, dissent, and limitations
- Mark missing information as Unknown
- Ask rather than guess when a material fact is unavailable
- Identify all required human decisions
- Stop before consequential authority gates
- Keep conclusions bounded by scope, evidence date, and expiration
- State what the repository validator does and does not prove

## Agent Must Not

The agent must not:

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
- Publish repository changes without explicit authorization

## Required Output

A substantive AI-assisted review should present:

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
