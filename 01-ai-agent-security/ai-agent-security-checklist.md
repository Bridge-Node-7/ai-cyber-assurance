# AI Agent Security Checklist

## Purpose

Use this checklist before deploying an AI agent, copilot, workflow automation, or tool-using model that can access systems, files, APIs, code, cloud environments, email, financial data, customer data, mission data, or operational workflows.

## 1. Identity and Access

- [ ] The agent has a documented owner.
- [ ] The agent has a unique service identity where applicable.
- [ ] Access is scoped to least privilege.
- [ ] Privileged actions are separated from routine actions.
- [ ] Human approval is required for high-impact actions.
- [ ] Credentials are stored outside prompts and model context.
- [ ] Secrets are protected from retrieval, logging, and output exposure.
- [ ] Access is reviewed on a recurring schedule.

## 2. Tool Use

- [ ] Approved tools are documented.
- [ ] Disallowed tools are documented.
- [ ] The agent cannot call arbitrary or unknown tools.
- [ ] Destructive actions are blocked or approval-gated.
- [ ] Tool outputs are validated before downstream use.
- [ ] Rate limits and budget limits are enforced.
- [ ] External tool results are treated as untrusted until validated.

## 3. Prompt and Instruction Security

- [ ] System instructions are separated from user-provided content.
- [ ] Retrieved documents are treated as data, not instructions.
- [ ] Prompt-injection risks are documented.
- [ ] Untrusted content is clearly labeled.
- [ ] The agent is instructed not to reveal hidden prompts, secrets, credentials, or private policies.
- [ ] Output is reviewed when used for high-impact decisions.

## 4. Data Protection

- [ ] Data classification is documented.
- [ ] Sensitive data is minimized.
- [ ] Logs are redacted where appropriate.
- [ ] Outputs are checked for accidental disclosure.
- [ ] Training, fine-tuning, and retrieval data sources are reviewed.
- [ ] Retention and deletion expectations are documented.

## 5. Human Oversight

- [ ] A responsible human owner is assigned.
- [ ] High-impact decisions require human review.
- [ ] Financial, legal, safety, medical, HR, security, or mission-impacting actions are approval-gated.
- [ ] Escalation paths are documented.
- [ ] A disable path or kill switch exists.
- [ ] Operators understand the agent's limits.

## 6. Monitoring and Evidence

- [ ] Agent actions are logged.
- [ ] Tool calls are logged.
- [ ] Failed actions are logged.
- [ ] Decision rationale is captured where appropriate.
- [ ] Anomalies are escalated.
- [ ] Review evidence is preserved.
- [ ] Metrics are documented.

## 7. Deployment Decision

- [ ] Green — deployable
- [ ] Amber — deploy with constraints
- [ ] Red — not deployable
- [ ] More evidence required

Reviewer:

Date:

Version:

Notes:
