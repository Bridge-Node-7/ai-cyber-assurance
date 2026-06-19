# Decision Rubric

## Purpose

Use this rubric to make review decisions more consistent across the repository.

The templates use different words depending on context, but they share one decision spine:

| Common Decision | Other Template Language | Meaning |
|---|---|---|
| Green | Approved / Ready / Proceed | Evidence is sufficient for the current stage |
| Amber | Approved with conditions / Ready with conditions / Proceed with constraints | Proceed only with documented constraints, owners, and follow-up |
| Red | Not approved / Not ready / Stop | Do not proceed until critical issues are resolved |
| More evidence required | More evidence required | The reviewer cannot make a defensible decision yet |

## Green Criteria

Use **Green** only when all of the following are true for the current review stage:

- System or asset boundary is defined.
- Owner and reviewer are identified.
- Critical data, access, tool use, and connected systems are documented.
- Critical controls have supporting evidence.
- No unresolved critical safety, security, privacy, mission, or public-release issue is present.
- Human approval gates exist for high-impact actions.
- Logs, monitoring, rollback, recovery, or escalation expectations are documented where relevant.
- Known risks are either mitigated or explicitly accepted by the correct owner.
- No secrets, credentials, private data, offensive instructions, or sensitive operational procedures are exposed.

## Amber Criteria

Use **Amber** when the system can proceed only with constraints:

- Scope is mostly clear, but some assumptions remain open.
- One or more non-critical controls need follow-up.
- A critical gap exists but has a temporary mitigation, owner, and deadline.
- Human approval gates exist, but need refinement.
- Evidence is sufficient for limited review, pilot, tabletop, or non-production use.
- Reviewers can name the constraints required to proceed safely.

Amber decisions must include:

- Conditions
- Risk owner
- Due date or revisit date
- Evidence needed to move to Green

## Red Criteria

Use **Red** when one or more of the following is true:

- System boundary is unclear.
- No accountable owner is identified.
- Critical access, data, tool, or command paths are unknown.
- High-impact actions can occur without approval.
- Secrets, credentials, private data, or sensitive operational details are exposed.
- Offensive cyber content, malware behavior, unauthorized access instructions, or credential theft workflows are present.
- Logging, recovery, rollback, or disable path is missing for a high-impact system.
- The system creates unacceptable safety, mission, legal, privacy, or security risk.
- The reviewer cannot identify a safe constraint set.

## More Evidence Required

Use **More evidence required** when a reviewer cannot responsibly choose Green, Amber, or Red.

Typical causes:

- Missing architecture information
- Missing access-control evidence
- Missing data classification
- Missing test results
- Missing owner or decision-maker
- Missing tool inventory
- Missing AI/model/provider information
- Missing rollback or recovery assumptions

## 0–5 Scoring Anchors

Use these anchors when a template asks for a 0–5 score.

| Score | Meaning |
|---:|---|
| 0 | Not present / unknown |
| 1 | Informal, undocumented, or ad hoc |
| 2 | Partially documented, but not repeatable |
| 3 | Documented and repeatable for limited scope |
| 4 | Documented, evidenced, reviewed, and mostly complete |
| 5 | Fully documented, evidenced, reviewed, tested, and operationally maintained |

## Zero Trust Scoring Guidance

For Zero Trust readiness:

- **0:** Trust is assumed; no evidence.
- **1:** Some controls exist, but are informal or incomplete.
- **2:** Controls are partially documented; major gaps remain.
- **3:** Controls are documented and repeatable for a defined scope.
- **4:** Controls are evidenced, reviewed, and tied to operational decisions.
- **5:** Controls are continuously monitored, tested, and improved.

## Public Release Decision Add-On

For anything intended for public GitHub, website, proposal, or investor review:

- Green requires no secrets, no private data, no sensitive operational details, no unsupported claims, and no unnecessary speculative content.
- Amber requires specific edits before publication.
- Red means do not publish.
