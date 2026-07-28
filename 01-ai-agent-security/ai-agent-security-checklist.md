# AI Agent Security Checklist
> **Artifact type:** TEMPLATE  
> **Completion status:** Blank for reuse  
> **Required for:** Conditional: systems using AI agents or tool-performing automation

## What this document is

A focused checklist for AI agents, copilots, workflow automations, and tool-using models.

## Who should complete it

The system owner, agent owner, security reviewer, and operator responsible for approving deployment or use.

## When to use it

Use when an AI component can access systems, files, APIs, code, cloud services, email, financial data, customer data, mission data, or operational workflows.

## Related records

- [Evidence Manifest](../02-evidence-manifests/evidence-manifest-template.md)
- [Human Approval Gates](human-approval-gates.md)
- [Identity and Authority Register](../11-assurance-lifecycle/identity-and-authority-register.md)
- [LLM Risk Register](../04-llm-risk/llm-risk-register.md)
- [Review Decision](../02-evidence-manifests/review-decision-template.md)

## 1. Ownership and lifecycle

- [ ] The agent has a documented human owner.
- [ ] The agent has a stated purpose and approved operating context.
- [ ] A unique agent, service, or workload identity is used where applicable.
- [ ] Creation, review, expiration, suspension, and revocation are documented.
- [ ] A disable path or kill switch exists and has an owner.
- [ ] Replacement, rollback, or manual fallback is documented.

## 2. Identity and access

- [ ] Access is scoped to least privilege and need-to-know.
- [ ] Privileged actions are separated from routine actions.
- [ ] Credentials are short-lived where feasible.
- [ ] Credentials are stored outside prompts, memory, and model context.
- [ ] Secrets are protected from retrieval, logging, and output exposure.
- [ ] Access is reviewed on a defined schedule.
- [ ] Dormant, orphaned, or excessive access can be detected and removed.

## 3. Tool use and external action

- [ ] Approved tools and APIs are documented.
- [ ] Disallowed tools and actions are documented.
- [ ] The agent cannot call arbitrary or unknown tools.
- [ ] Tool permissions are bound to the agent's purpose.
- [ ] Destructive, irreversible, public, financial, legal, security, or mission-impacting actions are blocked or approval-gated.
- [ ] Tool inputs and outputs are validated before downstream use.
- [ ] Rate, cost, time, and resource limits are enforced.
- [ ] External tool results are treated as untrusted until validated.

## 4. Prompt, retrieval, and memory security

- [ ] System instructions are separated from user-provided and retrieved content.
- [ ] Retrieved documents and tool output are treated as data, not authority.
- [ ] Prompt-injection and indirect-injection risks are documented.
- [ ] Retrieval sources have provenance, access control, and update ownership.
- [ ] Long-term memory is bounded, reviewable, and revocable.
- [ ] The agent is instructed not to reveal hidden prompts, secrets, credentials, or private policy content.
- [ ] Output is independently reviewed for high-impact use.

## 5. Data protection

- [ ] Data classification and handling rules are documented.
- [ ] Sensitive data access is minimized.
- [ ] Cross-user and cross-tenant boundaries are tested where applicable.
- [ ] Logs are redacted where appropriate.
- [ ] Outputs are checked for accidental disclosure.
- [ ] Training, fine-tuning, retrieval, and evaluation sources are reviewed.
- [ ] Retention, deletion, correction, and legal-hold expectations are documented.

## 6. Human oversight

- [ ] High-impact decisions require an authorized human.
- [ ] The agent cannot approve its own privileged actions.
- [ ] Approvers receive the evidence necessary to make a decision.
- [ ] Approval has a defined scope and expiration.
- [ ] Escalation and emergency-override paths are documented.
- [ ] Operators understand the agent's capabilities, limits, and failure modes.
- [ ] Post-action verification confirms that approved actions occurred as intended.

## 7. Monitoring and evidence

- [ ] Agent identity, session, model, configuration, and version are traceable.
- [ ] Prompts, tool calls, decisions, failures, and exceptions are logged at an appropriate level.
- [ ] Logs preserve source, time, integrity, and access restrictions.
- [ ] Anomalies and policy violations have escalation thresholds.
- [ ] Evidence supports both successful and failed control operation.
- [ ] Metrics include false positives, false negatives, unsafe attempts, approval delays, failures, and recovery performance where relevant.

## 8. Validation and recovery

- [ ] Critical controls have expected and observed results.
- [ ] Prompt-injection, excessive-agency, disclosure, and tool-misuse scenarios are tested safely.
- [ ] Revocation and session termination are tested.
- [ ] Disable, rollback, and manual fallback paths are tested.
- [ ] Corrective actions have owners and retest criteria.

## Deployment decision

Use [DECISION_RUBRIC.md](../DECISION_RUBRIC.md).

- [ ] Green — evidence sufficient for current scope and stage
- [ ] Amber — proceed with documented constraints
- [ ] Red — do not proceed
- [ ] More evidence required

Reviewer:

Date:

Version / configuration reviewed:

Decision expiration / revisit date:

Evidence references:

Notes:
