# AI Security Stack Ranking v3: research framework

Scratch dir: C:\Users\ATHARV~1\AppData\Local\Temp\claude\D--AccuKnox-help\b6d28038-e992-4a24-8ffc-dfdf8a0bec1a\scratchpad\rank
(In bash: "C:/Users/ATHARV~1/AppData/Local/Temp/claude/D--AccuKnox-help/b6d28038-e992-4a24-8ffc-dfdf8a0bec1a/scratchpad/rank")

## Use the Firecrawl Helper for Every Lookup

Firecrawl via the helper in the scratch dir. Run from that dir:

    python fc.py search "<query>" --limit 6
    python fc.py scrape "<url>" --max 12000
    python fc.py map "<site root>" --search "<term>"

The helper rotates API keys by itself. Do not use WebFetch unless Firecrawl fails for a URL.

## Score Each Vendor on the 8 Modules

| # | Module | Sub-features that define it |
|---|---|---|
| 1 | AI Security Posture Management (AI-SPM) | 1.1 AI asset inventory across clouds / on-prem. 1.2 Shadow AI detection (unsanctioned models, AI apps, notebooks, SaaS AI use). 1.3 AI pipeline and supply-chain posture (CI/CD, IaC, registries, AI misconfig). |
| 2 | Agentic AI Security | 2.1 Security for agents on managed platforms (Bedrock AgentCore, Copilot Studio, Agentforce, Azure AI Foundry, ServiceNow). 2.2 MCP server security (discovery, vetting, MCP gateway/proxy). 2.3 Agent runtime controls: sandboxing, tool-call policy, egress control, secure agent build/run platform. |
| 3 | AI Detect and Respond (AI-DR) | 3.1 Detection of attacks/anomalies on AI apps or agents at runtime or from logs. 3.2 Incident response, auto-remediation, SIEM/SOAR/ITSM (ServiceNow, Jira, Splunk). 3.3 Runtime enforcement on AI workloads (block, not just alert). |
| 4 | AI Guardrails, Prompt Firewall and AI Gateway | 4.1 Inline enforcement point: AI gateway / LLM proxy, SDK, API, browser extension. 4.2 Prompt injection, jailbreak, PII / data-leak blocking. 4.3 Unsafe output filtering: toxicity, hallucination, off-topic, code. |
| 5 | AI Compliance and Governance | 5.1 AIBOM / model inventory records. 5.2 Framework mapping (NIST AI RMF, ISO 42001, OWASP LLM Top 10, EU AI Act, MITRE ATLAS). 5.3 Audit trails, evidence, reports, policy workflows. |
| 6 | AI Red Teaming and AI DAST | 6.1 Automated adversarial attack library (jailbreak, injection, leakage). 6.2 Multi-turn / agentic attack simulation against live AI endpoints or apps (this is "AI DAST"). 6.3 Continuous / CI/CD red teaming with framework-mapped findings. |
| 7 | AI Identity Security | 7.1 Agent / workload identity. 7.2 Fine-grained authorization and least privilege for agents and tools. 7.3 Non-human identity (NHI) discovery and governance: service accounts, API keys, tokens, OAuth grants. |
| 8 | AI Model, Dataset and Code Security (AI SAST) | 8.1 Model file scanning (pickle, safetensors, GGUF, ONNX; malware, backdoors). 8.2 Dataset security: PII / sensitive data in training/RAG data, data poisoning. 8.3 AI SAST: scanning source code for AI/LLM risks (LLM calls, prompts, agent code, AI-generated code) or AI-assisted static analysis. |

## Pick One Status per Module

- `yes`  (tick): GA today, documented on the vendor's own site or docs, and covers at least 2 of the 3 sub-features, or covers the module's core clearly.
- `partial` (dash): covers 1 sub-feature, or a narrower version, or beta / preview / roadmap, or only posture where the row asks for enforcement.
- `no` (cross): after at least TWO targeted searches for that module (e.g. "<vendor> MCP security", "<vendor> red teaming") and a look at their product pages and docs, there is no public evidence.

Accuracy rule, the most important rule. Never mark a competitor `no` when they do support the capability. A false `no` is a legal risk and makes AccuKnox look dishonest. When in doubt between `no` and `partial`, search again. When you find real evidence, give the credit.

## Cite the Vendor Page That Proves the Claim

1. First choice: the vendor's own product page, docs, or release notes/blog. The `url` field must be the page that proves the claim.
2. Second choice: a named third-party page (press release, analyst report, G2/Gartner Peer Insights review, partner marketplace listing). Mark it with `"url_type": "third-party"`.
3. Read reviews (G2, Gartner Peer Insights, Reddit if reachable) only for context in `notes`. Do not base a `yes` on a review alone.

For a `no`, set `url` to the vendor's product/platform overview page you checked, and say what the page covers instead.

## Write One JSON File per Vendor

Write one JSON file per vendor to `<scratch dir>/vendors/<slug>.json`. Exact shape:

```json
{
  "vendor": "Display name, e.g. Noma Security",
  "slug": "noma-security",
  "website": "https://noma.security",
  "what_it_is": "One line, max 15 words, what the company sells.",
  "identity_note": "Only if the name was ambiguous: how you resolved it.",
  "modules": {
    "1": {"status": "yes|partial|no", "sub": {"1.1": "yes|partial|no", "1.2": "...", "1.3": "..."},
          "reason": "Max 18 words. Name the product or feature. Plain words.",
          "url": "https://...", "url_type": "vendor|third-party",
          "evidence": "Short verbatim phrase (max 20 words) from the page that proves it, or what you searched for a no."},
    "2": {...}, "3": {...}, "4": {...}, "5": {...}, "6": {...}, "7": {...}, "8": {...}
  },
  "notes": "Anything a reviewer should know: acquisitions, rebrands, beta items, review sentiment."
}
```

Writing rules for `reason`: short, plain, active. No em dashes, no semicolons. Never use: leverage, robust, seamless, ensure, comprehensive, cutting-edge, delve, streamline. Never attack the vendor. State what they ship, e.g. "MCP gateway discovers and scans MCP servers, but no agent sandbox."

When all vendors are done, reply with a 1-line status per vendor (8 statuses in order) and any vendor you could not identify.
