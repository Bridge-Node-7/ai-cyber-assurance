# Example AI Workflow Cyber Review

## Example Status

This is a synthetic, public-safe example. It does not describe a real customer, employer, system, proprietary workflow, or operational implementation.

## System / Workflow

Example AI-assisted document review workflow connected to a file repository, an approval queue, and a reporting output.

## Purpose

Demonstrate how a team might organize cyber readiness evidence before piloting an AI-enabled workflow.

## System Boundary

### In Scope

- User access to the workflow
- Tool permissions
- Document retrieval
- Output review
- Approval gates
- Logging and evidence capture

### Out of Scope

- Real customer data
- Real credentials
- Production infrastructure
- Proprietary implementation details

## Key Risks

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Prompt injection from uploaded documents | Medium | Medium / high | Treat retrieved content as untrusted data; require output review |
| Sensitive information disclosure | Medium | High | Minimize data access; redact logs; restrict outputs |
| Excessive agency | Medium | High | Limit tools; require approval for high-impact actions |
| Unverified output | Medium | Medium | Add evidence checks and human review |
| Unclear rollback path | Low / medium | Medium | Document disable path and fallback process |

## Framework Mapping

| Area | Example Evidence |
|---|---|
| Zero Trust | Unique user identity, scoped tool access, least privilege |
| LLM risk | Prompt injection, disclosure, improper output handling, excessive agency |
| Secure by design | Approval gates, logging, transparent limitations |
| Supply chain | Documented model/provider/tool dependencies |
| Cyber survivability | Disable path, fallback review process, recovery notes |

## Review Decision

- [ ] Green
- [x] Amber
- [ ] Red
- [ ] More evidence required

## Conditions

1. Complete data classification review.
2. Add human approval gate for external sharing.
3. Confirm log redaction.
4. Document tool permissions and disable path.

## Notes

This example shows the public-safe method: define the boundary, identify risks, map evidence, and make a decision without exposing sensitive implementation details.
