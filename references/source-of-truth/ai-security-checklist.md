# AI Security Checklist

Markdown copy of the Google Sheet "AI Security Checklist" (owner gaurav.mishra@accuknox.com, last modified 2026-09-22). Source: https://docs.google.com/spreadsheets/d/1IajfllcBXQXcaqruI-kXEXlwiFRnRIZeivJs3t9AIS8/edit. The `.xlsx` beside this file is the exact export. Refresh both from the sheet when it changes.

## AI Security Checklist

| Stage | Category | Topic | Objective | Technical Capability | Implementation Method | Required for the POC | PCI Compliant |
|---|---|---|---|---|---|---|---|
| STAGE - I | Discovery | Models on Cloud/Onprem | Model Disocvery on Cloud- ML, LLMs, Custom | Discover models on Platform(AI Foundry, Bedrock, Model Garden, Vertex AI) | Cloud API/Collector | Must for POC |  |
|  |  |  | Model Discovery on On Prem - ML, LLMs, Custom | Discover models on VLLMs, Hugging Face, Run AI etc | Cloud API/Collector | Must for POC |  |
|  |  | Agents on Cloud/Onprem | Agent Discovery on Cloud | Discover agents on Platform(AI Foundry, Bedrock, Model Garden, Vertex AI) | Cloud API/Collector | Must for POC |  |
|  |  |  | Agent Discovery on Managed Services | Discover agents on Bedrock AgentCore, CP Studio, Power APps, M365, Agent Engine | Cloud API/Collector | Must for POC |  |
|  |  |  | Agent Discovery on Unmanaged Services | Discover agents on Kubernetes and VMs. | Endpoint Agent (EDR-like) | Must for POC |  |
|  |  |  | Agent Discovery on Unmanaged AI Assets | Discover of AI Libraries, Frameworks, Binaries | Endpoint Agent (EDR-like) | Must for POC |  |
|  |  | AI-related Assets | Dataset & Compute Discovery | AI- related Asset Discovery - Datasets, Computes | Cloud API/Collector | Must for POC |  |
|  |  | Blast Radius | Piepline Visisbility | Discover Security Graph of LLMOps/MLOps journey | Cloud API/Collector | Must for POC |  |
|  | Misconfigurations | Cloud/Onprem Misconfigurations | Dataset Issues | Detect Dataset for public exposure, PII or PHI  scanning | Cloud API/Collector based PII/PHI Scanning | Must for POC |  |
|  |  |  | Compute Issues | Detect Compute for public exposure and vulnerabilities | Cloud API/Scanning Vulnerabilities | Must for POC |  |
| STAGE - II | Compliance | AI Cloud Compliance | Detect Compliance against AI/ML Assets | OWASPM Top10 for LLM, ISO27001, AVID | Cloud API/Collector | Must for POC |  |
|  | Red Teaming | Model Red Teaming | Perform Red Teaming on Cloud & Onprem Models | Automated adversarial testing (prompt injection, jailbreaks) | Cloud API/Collector | Good to Have |  |
|  |  | Agents Red Teaming | Perform Red Teaming on Agents (Managed/Unmanaged) | Automated adversarial testing (prompt injection, jailbreaks) | Cloud API/Collector | Good to Have |  |
|  | Model Supply Chain & Provenance | AI-BOM | Shift Left Vulnerabilities and BOM for AI | Discover Model supply chain, provenance and vulnerabilities | Cloud API/Collector | Good to Have |  |
|  | Discovery + Prompt Firewall | GenAI Browser Integration | Browser Plugin Discovery | Detect prompts and response for ChatGPT, Gemini, Claude like application usage | Cloud API/Collector | Must for POC |  |
|  |  | Agents behind AI Gateway | Bi-Frost, LiteLLM, Kong AI | Discover Agents and enforce Prompt Firewall | AI Gateway (Proxy) | Must for POC |  |
|  |  | Agents running on Managed Agents Platform | Power Apps | Discover Agents and enforce Prompt Firewall | Application SDK Integration | Must for POC |  |
|  |  | Runtime Security | Prompt Firewall - Inline | Inspect prompts/responses using policy + semantic analysis | AI Gateway (Proxy) | Must for POC |  |
|  |  |  | Prompt Firewall - SDK | Embed prompt inspection into applications | Application SDK Integration | Must for POC |  |
|  |  |  | API Gateway | Central routing of LLM traffic (APIM, AWS API GW, APIGEE) | Reverse Proxy / API Gateway | Must for POC |  |
|  | Sandboxing AI Agents on Kubernetes | Sandboxing AI Agents | Sandboxing AI Agents on Kubernetes/VMs | Discover real-time behaviour of Agents and prevent any drift in the AI Agents | Daemons-set/systemd Mode | Must for POC |  |
|  | Discovery + Prompt Firewall | Runtime Security | Traffic Observability | Capture request/response telemetry | Gateway Logging / Collector | Must for POC |  |
| STAGE - III | Discovery + Prompt Firewall | Copilot Integration | Integrate with GitHub OpenClaw, Claude CLI or Co-Pilot, Agentforce etc. | Shadow AI Discovery & Runtime Guardrailing | SDK | Not Applicable |  |
|  | Sandboxing AI Agents on Kubernetes | Sandboxing AI Agents | AI agents Behaviour Discovery | AI Agents discovery on K8s/VMs | Daemons-set/systemd Mode | To be checked later |  |
|  | Endpoint Security | AI Agents Discovery on VMs | Shadow AI Detection | Detect unauthorized AI tools via process/network monitoring | Endpoint Agent (EDR-like) | To be checked later |  |
|  |  |  | Local Prompt Inspection | Monitor local LLM tools and CLI usage | Agent-based Interception | Not Applicable |  |
|  | DevSecOps |  | AIBOM Generation | Generate AI component inventory (models, datasets, libs) | Repo Scanner | Not Applicable |  |
|  |  |  | Policy Enforcement | Block builds based on AI risk policies | CI/CD Pipeline Integration | Not Applicable |  |
|  |  |  | Model Security Scanning | Scan models during build phase | Pipeline Plugin | Not Applicable |  |
|  |  |  | Scheduled Scans | Periodic AI security scans | Scheduler / Cron | Not Applicable |  |
|  | Governance |  | Prompt Logging | Store prompt/response logs | Central Logging System | To be checked later |  |
|  |  |  | Policy Engine | Define and enforce AI security policies | Policy-as-Code Engine | To be checked later |  |
|  |  |  | Compliance Support | Support for ISO27001, ISO42001, OWASP, EU AI ACT, NIST AI RMF | Compliance mapping witht he regulaorty requirements | To be checked later |  |

## Prompt Firewall Use Cases

| Stage | Category | Topic | Objective | Technical Capability | Implementation Method | Required for the POC |
|---|---|---|---|---|---|---|
| STAGE - II | Enterprise GenAI / Browser Prompt Firewall | Identity & Tenant Enforcement | Prevent users from accessing ChatGPT/Claude-like applications with personal or unmanaged identities | Detect AI application login identity, corporate SSO, email domain, tenant/workspace/org ID and block personal accounts such as Gmail | Browser Plugin / Identity Provider / Cloud API | Must for POC |
|  |  | Shadow AI / AI Application Discovery | Discover sanctioned and unsanctioned GenAI applications used from enterprise browsers | Detect ChatGPT, Claude, Gemini and other AI applications, extensions and browser sessions; classify approved vs unapproved usage | Browser Plugin / Endpoint Agent / Cloud Collector | Must for POC |
|  |  | Prompt PII/PHI & Sensitive Data Inspection | Prevent sensitive information from being submitted to GenAI applications | Inspect prompts for PII, PHI, PCI, secrets, credentials, source code, confidential data and organization-defined sensitive information | Browser Plugin / Inline Proxy / AI Gateway | Must for POC |
|  |  | AI Security Taxonomy Enforcement | Detect unsafe or adversarial prompts before they reach the model | Classify prompt-injection, prompt-extraction, jailbreak, system-prompt override, RAG poisoning, data exfiltration, malicious-code and harmful-content categories | Browser Plugin / AI Gateway / Semantic Classifier | Must for POC |
|  |  | Prompt Policy Actions | Apply configurable enforcement based on detected risk | Allow, warn, redact, block or require business justification based on data classification, AI-risk category, user/group and application | Policy Engine / Browser Plugin / AI Gateway | Must for POC |
|  |  | Attachment Upload Control | Prevent unauthorized document and file transfer into GenAI applications | Intercept file upload, drag-and-drop and attachment events; support global block, file-type allowlist and application-specific policies | Browser Plugin / Endpoint Agent | Must for POC |
|  |  | Purview Sensitivity Label Enforcement | Prevent classified enterprise documents from being uploaded to consumer or unapproved AI services | Read Microsoft Purview sensitivity labels and allow only configured labels such as General; block Confidential, Highly Confidential and custom restricted labels | Browser Plugin / Purview Integration / Endpoint DLP | Must for POC |
|  |  | Attachment PII/PHI Scanning | Detect sensitive content in documents even when the document classification label appears permissible | Extract document content and scan for PII, PHI, PCI, secrets and other sensitive information before upload | Document Parser / DLP Classifier / Browser Plugin | Must for POC |
|  |  | Response PII/PHI & Sensitive Data Filtering | Prevent sensitive information from being exposed to the user through AI-generated responses | Inspect model responses for PII, PHI, PCI, secrets, confidential information and policy violations; redact, warn or block | Inline Proxy / AI Gateway / SDK | Must for POC |
|  |  | Clipboard & Paste Protection | Prevent users from bypassing file controls by pasting sensitive data into AI prompts | Inspect clipboard paste and form submission events for PII, PHI, secrets, source code and confidential data | Browser Plugin / Endpoint DLP | Good to Have |
|  |  | Source Code & Intellectual Property Protection | Prevent proprietary code and intellectual property from leaving the organization | Detect source code, proprietary libraries, architecture, credentials and confidential IP in prompts or attachments and enforce enterprise AI-only policies | Browser Plugin / DLP Classifier / Policy Engine | Good to Have |
|  |  | AI Response Threat Filtering | Prevent harmful or security-sensitive model output from reaching end users | Inspect responses for malicious links, malware/exploit assistance, unsafe content, secrets and other organization-defined risk categories | Inline Proxy / AI Gateway / Semantic Classifier | Good to Have |
|  |  | AI Interaction Telemetry & Risk Scoring | Provide security teams with visibility into GenAI usage and policy violations | Capture user, application, tenant, prompt/response risk category, data classification, attachment metadata, action and outcome; calculate session/user risk | Gateway Logging / SIEM / Analytics | Must for POC |
