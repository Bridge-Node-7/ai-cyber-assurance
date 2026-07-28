# LLM and Generative AI Risk Register
> **Artifact type:** TEMPLATE  
> **Completion status:** Blank for reuse  
> **Required for:** Conditional: LLM, retrieval, model, or generated-output use

## Purpose

Track public-safe cybersecurity risks in LLM-enabled systems, AI agents, copilots, chatbots, workflow automations, and retrieval-augmented generation systems.

This register uses the public OWASP 2025 risk names as an organizing aid. It is not an exploit guide, compliance checklist, or proof that a system is secure.

## Review identity

- **System:**
- **Owner:**
- **Model / provider / version:**
- **Review date:**
- **Related Evidence Manifest:**

## Risk register

| OWASP ID | Risk | Example condition | Potential impact | Preventive controls | Detective controls | Corrective / recovery controls | Evidence ID | Owner | Status |
|---|---|---|---|---|---|---|---|---|---|
| LLM01:2025 | Prompt Injection | User, retrieved document, tool output, or external content attempts to change instructions | Unauthorized behavior, unsafe output, policy bypass, or tool misuse | Separate instructions from data; constrain tools; validate sources; require approval | Log injection attempts; monitor policy violations and unusual tool paths | Quarantine content; revoke session; disable tool; review evidence and prompts | | | Open |
| LLM02:2025 | Sensitive Information Disclosure | Model reveals private, internal, regulated, credential, or mission-sensitive data | Privacy, security, legal, or mission harm | Least privilege; data minimization; secret isolation; output rules | Output scanning; access and disclosure monitoring | Revoke access; contain disclosure; preserve evidence; notify authorized responders | | | Open |
| LLM03:2025 | Supply Chain | Model, dependency, plugin, dataset, tool, or service is compromised or unreviewed | System compromise, unsafe output, integrity loss, or unavailable service | Vendor review; provenance; dependency inventory; version pinning | Change detection; provider and dependency monitoring | Roll back; replace dependency; restrict provider; reassess evidence | | | Open |
| LLM04:2025 | Data and Model Poisoning | Training, fine-tuning, embedding, memory, or retrieval data is manipulated | Misleading output, hidden behavior, or poor decisions | Source approval; integrity checks; segregation; change control | Drift, anomaly, provenance, and integrity monitoring | Remove poisoned source; rebuild index/model; retest | | | Open |
| LLM05:2025 | Improper Output Handling | Model output is trusted, rendered, executed, or forwarded without validation | Downstream compromise, injection, or unsafe action | Validate, sanitize, encode, constrain interpreters, require human review | Monitor execution and downstream rejection | Block action; contain affected system; correct integration | | | Open |
| LLM06:2025 | Excessive Agency | Agent can take actions beyond intended purpose or authority | Operational, financial, legal, security, or mission harm | Scoped identity; tool allowlist; approval gates; budgets; separation of duties | Tool-call, privilege, and policy-decision monitoring | Revoke session; disable agent; roll back action; review authority | | | Open |
| LLM07:2025 | System Prompt Leakage | System instructions or private policy content are exposed | Policy bypass, reverse engineering, or sensitive process leakage | Minimize sensitive prompt content; keep secrets out of prompts | Output review; leakage tests and monitoring | Rotate affected secrets; revise prompt and boundary | | | Open |
| LLM08:2025 | Vector and Embedding Weaknesses | Retrieval returns poisoned, unauthorized, irrelevant, or sensitive content | Bad decisions, privacy exposure, or unsafe grounding | Source access control; provenance; tenancy isolation; filtering | Retrieval quality and cross-boundary monitoring | Remove source; rebuild index; correct access; retest | | | Open |
| LLM09:2025 | Misinformation | Model produces incorrect, misleading, or unsupported output | Decision error, reputational harm, or operational risk | Evidence requirements; citations; bounded use; human review | Quality evaluation; contradiction and unsupported-claim checks | Correct output; withdraw claim; update workflow and evidence | | | Open |
| LLM10:2025 | Unbounded Consumption | Agent or user triggers excessive inference, tool calls, cost, or load | Cost spike, denial of service, model theft, or degradation | Quotas; rate and budget limits; request validation | Cost, volume, latency, and abuse monitoring | Throttle, suspend, investigate, and restore service | | | Open |

## Risk decision

- [ ] Accept risk within stated authority and expiration
- [ ] Mitigate before launch or expanded use
- [ ] Transfer or share risk through an authorized arrangement
- [ ] Reject deployment or use
- [ ] More evidence required

Decision maker:

Authority basis:

Evidence reviewed:

Conditions:

Expiration / revisit date:

Notes:
