
# Decision Rubric

## Purpose

Use this rubric to make bounded, evidence-backed decisions consistently across AI Cyber Assurance.

A decision applies only to the reviewed scope, configuration, evidence, time, and stage. It is not a universal statement about the system.

## Decision Spine

| Common Decision | Equivalent Language | Meaning |
|---|---|---|
| Green | Approved / Ready / Proceed | Evidence is sufficient for the current stage and no unresolved critical blocker is known |
| Amber | Approved with conditions / Ready with constraints | Proceed only within documented limits, owners, deadlines, and retest requirements |
| Red | Not approved / Not ready / Stop | Do not proceed until critical issues are resolved |
| More evidence required | Undetermined | The available evidence does not support a defensible decision |

## Green Criteria

Use **Green** only when all applicable conditions are true:

- Mission, scope, version, owner, and decision owner are identified.
- System boundary and critical dependencies are defined.
- Human, service, workload, supplier, and AI-agent authority is bounded.
- Material threats and failure modes are mapped to requirements and controls.
- Critical controls have supporting evidence.
- Validation scope, method, results, and limitations are recorded.
- Required human approval gates exist and prohibit inappropriate self-approval.
- Monitoring, incident handling, rollback, and recovery responsibilities are defined.
- Material recovery claims have executed evidence where required.
- No unresolved critical security, privacy, safety, mission, legal, or public-release blocker is known.
- Residual risk has an authorized owner and review date.
- Public claims do not exceed the evidence.

## Amber Criteria

Use **Amber** when the current stage may proceed safely only with explicit conditions, such as:

- A noncritical evidence gap remains.
- A control is partially validated.
- Recovery is planned but not fully exercised.
- A dependency or assumption requires monitoring.
- A pilot is limited in users, data, tools, duration, or authority.
- Human review compensates for bounded automation risk.
- Corrective action has a named owner and due date.
- A retest or reassessment is required before expansion.

An Amber decision must state:

- Permitted scope
- Conditions
- Owner
- Due date
- Prohibited actions
- Required monitoring
- Required retest
- Expiration or next review

## Red Criteria

Use **Red** when any applicable critical condition exists, including:

- Unclear or unauthorized system boundary
- Missing accountable owner
- Unknown or excessive privileged authority
- Consequential automation without required human approval
- Critical control absent, failed, or unsupported by evidence
- Unacceptable risk without authorized acceptance
- No safe rollback or recovery path where required
- Active secret, credential, or private-key exposure
- Unauthorized testing or access
- Malware code, weaponization instructions, exploit-enabling operational detail, harmful deployment procedures, persistence or evasion guidance, or credential-theft workflows
- Real sensitive findings or infrastructure exposed publicly
- Unsupported claims of certification, authorization, independent validation, compliance, or production maturity
- Safety or mission consequence that cannot be acceptably bounded

## More Evidence Required

Use **More evidence required** when the reviewer cannot distinguish among Green, Amber, or Red because:

- The version or configuration is unclear.
- The evidence source or integrity is unknown.
- A material identity or dependency is missing.
- A control is asserted but not evidenced.
- Test coverage or success criteria are undefined.
- Observed fact and inference are mixed.
- Recovery or rollback has not been evaluated.
- Conflicting evidence has not been reconciled.
- A current authoritative reference is needed.

## Evidence Quality

Evaluate evidence using:

| Dimension | Question |
|---|---|
| Relevance | Does it support the exact requirement or claim? |
| Provenance | Is the source and collection method known? |
| Integrity | Can alteration be detected where material? |
| Currency | Does it represent the reviewed version and time? |
| Coverage | Does it cover the critical scope and condition? |
| Repeatability | Can the result be reproduced or rechecked? |
| Independence | Is it self-produced, second-party, or independent? |
| Limitation | Are gaps, assumptions, and uncertainty visible? |

## Maturity Anchors

| Level | Description |
|---:|---|
| 0 | Undefined |
| 1 | Documented |
| 2 | Implemented |
| 3 | Observed operating |
| 4 | Tested for defined conditions |
| 5 | Continuously evidenced and independently assessed where required |

Do not infer a higher level from documentation alone.

## Public-Release Decision

A public release additionally requires:

- Public-safe and source-integrity review
- No secrets, private data, real vulnerabilities, or sensitive architecture
- Accurate maturity and limitation language
- Valid internal links, manifest, hashes, and automated checks
- Clearly synthetic examples
- Verified private vulnerability-reporting path
- Recorded usability walkthrough
- Authorized human release approval

## Decision Record

Every final decision should state:

- Reviewed system and version
- Scope
- Evidence considered
- Decision
- Conditions
- Residual risk
- Decision owner
- Reviewer
- Expiration or next review
- Corrective action
- Retest requirement
