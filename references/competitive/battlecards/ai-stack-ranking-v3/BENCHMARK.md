# Pass 4: Benchmark Every Competitor Against the AccuKnox Bar

AccuKnox is the best-in-class reference. It meets every bar below. A competitor earns `yes` on a
sub-feature only when it matches the bar, with evidence from its own site or docs. Having the basics
of a capability earns `partial`. Having nothing earns `no`.

Accuracy still rules. Never write `no` when the vendor has the capability. Never write `yes` when the
vendor has only a basic version. Beta, preview and early access are `partial`.

## The AccuKnox Bar per Sub-Feature

| Sub | `yes` only when the vendor matches this bar |
|---|---|
| 1.1 | AI asset inventory across at least two of AWS, Azure and GCP, plus on-prem hosts or Kubernetes. Network, browser or endpoint discovery alone is `partial`. |
| 1.2 | Shadow AI found on at least two surfaces: browser, endpoint or desktop, servers and clusters, CLI coding agents. |
| 1.3 | Posture and misconfiguration checks on AI cloud resources, and CI/CD or supply-chain checks. One of the two is `partial`. |
| 2.1 | Three or more named managed agent platforms (Copilot Studio, M365 Agents, Azure AI Foundry, Bedrock AgentCore, Bedrock Agents, Agentforce, Power Apps, Vertex). One or two is `partial`. |
| 2.2 | MCP server discovery plus MCP policy enforcement. Discovery only, or a proxy only, is `partial`. |
| 2.3 | Agent sandbox that isolates process, file and network egress at the host or kernel, or an isolated runtime. A tool-call allowlist at a proxy is `partial`. |
| 3.1 | Detection from both AI cloud control-plane logs and runtime signals. One source is `partial`. |
| 3.2 | A named SIEM or ITSM integration and automated remediation. One of the two is `partial`. |
| 3.3 | Blocking on the workload or agent host (process, file, network). Blocking only prompts or tool calls is `partial`. |
| 4.1 | Three or more enforcement modes: browser extension, gateway or proxy, SDK or API, third-party gateway integration (LiteLLM, APIM, Kong and others). Two modes is `partial`. |
| 4.2 | Blocks prompt injection, jailbreak and PII in both prompts and responses. Missing one is `partial`. |
| 4.3 | Filters at least two of toxicity, hallucination and harmful code in output. |
| 5.1 | Exportable AIBOM in a standard format such as CycloneDX. An inventory with no export is `partial`. |
| 5.2 | Three or more named frameworks mapped in the product (NIST AI RMF, ISO 42001, OWASP LLM Top 10, EU AI Act, MITRE ATLAS). |
| 5.3 | Audit trail plus exportable compliance reports. |
| 6.1 | Automated attack library across at least three categories: injection, jailbreak, data leakage, toxicity. |
| 6.2 | Multi-turn or purpose-generated attacks against live AI endpoints or agents. |
| 6.3 | Scheduled or CI/CD red-team runs with findings mapped to a framework. |
| 7.1 | A distinct cryptographic identity per agent or workload (SPIFFE or an equivalent per-agent credential). Delegating the human user's identity is `partial`. |
| 7.2 | Fine-grained, per-agent and per-tool authorization with least privilege. Coarse role or group access is `partial`. |
| 7.3 | Discovery and governance of non-human identities: API keys, service accounts, tokens, OAuth grants. |
| 8.1 | Model file scanning for malware or backdoors in at least three formats (Pickle, safetensors, GGUF, ONNX). |
| 8.2 | Dataset scans for PII and for poisoning. One of the two is `partial`. |
| 8.3 | AI SAST: scans source code for AI or LLM risks, or AI-assisted static analysis. |

## The Module Status Follows From the Subs

- `yes` (tick): all three subs are `yes`. The vendor matches AccuKnox across the module.
- `partial` (dash): at least one sub is `yes` or `partial`, but not all three are `yes`.
- `no` (cross): all three subs are `no`.

## Write the Two Lines

For every module write two plain fields. Each one has 14 words or fewer.

- `has`: what the vendor ships, with the product name. Example: "Agent Mission Control blocks risky tool calls. MCP Security Gateway."
- `lacks`: what the vendor does not ship against the bar. Example: "No kernel sandbox. Two managed agent platforms, not three."
- For a `yes` module, set `lacks` to "".
- For a `no` module, set `has` to "".

No em dashes, no semicolons. Never use: leverage, robust, seamless, ensure, comprehensive,
cutting-edge, delve, streamline. State facts flatly and never attack the vendor.

## Inputs, Tools and Output

- Input: `vendors_v2/<slug>.json` in this folder. Each module has `sub`, `reason`, `url`, `evidence`
  and `verify_note`.
- Research: run `python fc.py search "..."` and `python fc.py scrape "<url>" --max 20000` from this
  folder. The helper rotates the Firecrawl keys. Search only where the bar needs a fact that the
  input does not hold, such as how many clouds, how many managed agent platforms, or whether a sandbox
  isolates at the host. Budget: about 6 to 10 calls per vendor.
- Output: write `vendors_v3/<slug>.json`. Copy the v2 file, update `sub` and `status` per the bar,
  add `has` and `lacks` to every module, and update `url` when a better page proves the claim.
  Leave `vendors_v2/` unchanged.

Reply with a per-vendor line of the 8 new statuses and a count of modules that moved from `yes` to
`partial`.
