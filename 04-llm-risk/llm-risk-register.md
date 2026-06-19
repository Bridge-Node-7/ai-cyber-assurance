# LLM Risk Register

## Purpose

Track risks in LLM-enabled systems, AI agents, copilots, chatbots, workflow automations, and retrieval-augmented generation systems.

This register maps to the public OWASP Top 10 for LLM Applications and Generative AI 2025 risk names. It is a public-safe governance artifact, not an exploit guide.

| OWASP ID | Risk | Example | Impact | Mitigation | Status |
|---|---|---|---|---|---|
| LLM01:2025 | Prompt Injection | User or retrieved document attempts to override instructions | Unauthorized behavior, unsafe output, or policy bypass | Treat external content as untrusted data; enforce instruction hierarchy; add output checks | Open |
| LLM02:2025 | Sensitive Information Disclosure | Model reveals private, internal, regulated, credential, or mission-sensitive data | Privacy, security, legal, or mission harm | Access controls, redaction, data minimization, output review | Open |
| LLM03:2025 | Supply Chain | Model, dependency, plugin, dataset, tool, or service is compromised or unreviewed | System compromise, unsafe output, or integrity loss | Vendor review, dependency scanning, SBOM/AIBOM, source validation | Open |
| LLM04:2025 | Data and Model Poisoning | Training, fine-tuning, embedding, or retrieval data is manipulated | Misleading output, hidden behavior, or poor decisions | Dataset review, source scoring, monitoring, change control | Open |
| LLM05:2025 | Improper Output Handling | Model output is trusted or executed without validation | Downstream compromise, injection, or unsafe action | Validate, sanitize, encode, test, and require human review for high-impact use | Open |
| LLM06:2025 | Excessive Agency | Agent can take actions beyond intended scope | Operational, financial, legal, or security harm | Tool limits, approval gates, scoped identity, logging | Open |
| LLM07:2025 | System Prompt Leakage | System instructions or hidden policies are exposed | Policy bypass, reverse engineering, or sensitive process leakage | Minimize sensitive prompt content; avoid secrets in prompts; monitor outputs | Open |
| LLM08:2025 | Vector and Embedding Weaknesses | Retrieval or embedding pipeline returns poisoned, irrelevant, or sensitive content | Bad decisions, privacy exposure, or unsafe grounding | Source validation, retrieval filtering, access controls, provenance | Open |
| LLM09:2025 | Misinformation | Model produces incorrect, misleading, or unsupported output | Decision error, reputational harm, or operational risk | Evidence checks, citations, human review, confidence notes | Open |
| LLM10:2025 | Unbounded Consumption | Agent or user triggers excessive inference, tool calls, cost, or load | Cost spike, denial of service, model theft, or service degradation | Quotas, rate limits, budget caps, monitoring, abuse controls | Open |

## Risk Decision

- [ ] Accept risk
- [ ] Mitigate before launch
- [ ] Transfer risk
- [ ] Reject deployment
- [ ] More evidence required

Reviewer:

Date:

Notes:
