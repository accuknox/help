# AI security cheat sheet v4, research

Opened on 2026-10-07. Every number below was read on the page named in its row. A number that could
not be read on a primary page was dropped.

## Data Points From Public Sources

| # | Number | Exact wording on the page | Publisher, year | URL opened |
|---|---|---|---|---|
| 1 | More than 20% | "More than 20% of organizations reported a breach targeting AI models or applications." | IBM and Ponemon Institute, Cost of a Data Breach 2026 | https://newsroom.ibm.com/2026-07-29-ibm-study-one-in-four-malicious-breaches-are-ai-enabled,-costing-companies-6-million-on-average |
| 2 | 27% and 27% | "The most common causes were weaknesses in surrounding systems: compromised APIs, applications, or plug-ins (27%) and cloud misconfigurations affecting AI workloads (27%)." | IBM, 2026 | same as row 1 |
| 3 | 97% | "Of those compromised, 97% report not having AI access controls in place." | IBM, Cost of a Data Breach 2025 | https://newsroom.ibm.com/2025-07-30-ibm-report-13-of-organizations-reported-breaches-of-ai-models-or-applications,-97-of-which-reported-lacking-proper-ai-access-controls |
| 4 | One in five | "One in five organizations reported a breach due to shadow AI" | IBM, 2025 | same as row 3 |
| 5 | 37% | "only 37% have policies to manage AI or detect shadow AI" | IBM, 2025 | same as row 3 |
| 6 | $670,000 | "Organizations that used high levels of shadow AI observed an average of $670,000 in higher breach costs" | IBM, 2025 | same as row 3. Kept in research only |
| 7 | No number | "it is unclear if there are fool-proof methods of prevention for prompt injection" | OWASP Gen AI Security Project, LLM01:2025 | https://genai.owasp.org/llmrisk/llm01-prompt-injection/ |
| 8 | No number | Root causes of Excessive Agency: "Excessive functionality", "Excessive permissions", "Excessive autonomy" | OWASP, LLM06:2025 | https://genai.owasp.org/llmrisk/llm062025-excessive-agency/ |
| 9 | No number | "Vulnerable pre-trained models can contain hidden biases, backdoors, or other malicious features" | OWASP, LLM03:2025 | https://genai.owasp.org/llmrisk/llm032025-supply-chain/ |

Dropped: the "shadow AI incidents rose from 20% to 43%" figure for 2026. Only secondary blogs state
it, and the IBM report page renders its counters as zero in a scrape, so the number stays unconfirmed.

## Product Facts, Tier D

| Fact | Source under `docs/` |
|---|---|
| The Prompt Firewall has 14 policy types, and it can block, sanitize or monitor | `use-cases/prompt-firewall-overview.md` |
| The Prompt Firewall is stateful and links a prompt to its response by `session_id` | `use-cases/prompt-firewall-overview.md` |
| Gateways include LiteLLM, Bifrost, Azure APIM and AWS API Gateway | `integrations/ai-overview.md` |
| The browser plugin covers ChatGPT, Claude, GitHub Copilot and Gemini on Chrome, Edge and Firefox | `integrations/chrome-browser-integration.md` |
| v3.5 discovers managed agents in Copilot Studio, Microsoft 365 Agents, Azure AI Foundry, Bedrock AgentCore and Bedrock Agent | `getting-started/3.5-release.md` |
| ModelArmor applies process, file system, network and domain isolation with eBPF and LSM, for Ollama, vLLM, Triton, LangGraph, n8n and MCP servers | `use-cases/modelarmor.md` |
| ML Static Scans check supply chain, adversarial robustness, data and privacy risk and model file security | `how-to/ml-static-scan.md` |
| The CI/CD model gate runs on a `/scan` pull request comment, with no weights in the repo | `how-to/model-scan-cicd.md` |
| Red teaming scan categories are Sentiment Analysis, Code, Hallucination and Prompt Injection | `use-cases/red-teaming.md` |

## Proof Row, accuknox.com

| Fact | Source |
|---|---|
| Featured in KuppingerCole's 2026 CNAPP Leadership Compass, which names GenAI security | https://accuknox.com/analyst-recognition |
| A 2026 Best Practices recognition for Technology Innovation Leadership in cybersecurity solutions to secure the AI stack | https://accuknox.com/analyst-recognition |

## Screenshots

| File | Source | Pixels | Edit |
|---|---|---|---|
| `v4-arch.webp` | `docs/assets/images/ai-security/enforcement-points.webp` | 1920 x 993 | None |
| `v4-shadow.png` | `docs/use-cases/images/shadow-ai/unmanaged-asset-categories.png` | 1916 x 790 | None |
| `v4-aidr.png` | `docs/getting-started/image-11.png` | 2190 x 1361 | Black border trimmed, image generator mark painted out |
| `v4-agents.png` | `references/PRODUCT UI/4_AI ML security/Agentic AI - Mar 6/agent_list.png` | 2880 x 1010 | Cropped to the table |
| `v4-mlscan.png` | `docs/how-to/image-6.png` | 3047 x 1150 | Border trimmed, Model Path cells redacted because they show a GitHub user name |
| `v4-redteam.png` | `docs/how-to/images/bedrock-collector/13-findings.png` | 2400 x 838 | Tenant name redacted, cropped to seven rows |
| `v4-promptfw.png` | `references/PRODUCT UI/4_AI ML security/LLM Defense 1.png` | 5760 x 1872 | Cropped to the summary, endpoint hostname redacted |

Every image renders at its natural aspect ratio. No `object-fit:cover` frame remains.
