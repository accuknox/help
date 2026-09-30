# -*- coding: utf-8 -*-
"""AccuKnox AI Security vs Netskope Skylight AI Security, the single data file.

The XLSX, the markdown draft and the PPTX all read this file, so the three can
never disagree. Every cell cites a source key from SOURCES.

AccuKnox facts come from help.accuknox.com (the docs in this repo) and, for the
two Beta modules, from accuknox.com. Netskope facts come from docs.netskope.com
and netskope.com, pulled with Firecrawl on 24 September 2026. The scrapes sit in
.firecrawl/netskope/ (gitignored), and evidence-log.md lists what each one says.
"""

READ_ON = "24 September 2026"
AK_NAME = "AccuKnox AI Security"
NS_NAME = "Netskope Skylight AI Security"

H = "https://help.accuknox.com/"
W = "https://accuknox.com/"
N = "https://docs.netskope.com/en/"

SOURCES = {
    # ---- AccuKnox, help docs --------------------------------------------
    "ak-arch": ("AccuKnox", "AI security architecture", H + "getting-started/ai-security-arch/"),
    "ak-overview": ("AccuKnox", "AI-SPM overview", H + "how-to/aiml-overview/"),
    "ak-aws": ("AccuKnox", "AWS AI/ML onboarding", H + "how-to/aiml-aws-onboard/"),
    "ak-azure": ("AccuKnox", "Azure AI/ML onboarding", H + "how-to/aiml-azure-onboard/"),
    "ak-gcp": ("AccuKnox", "GCP AI/ML onboarding", H + "how-to/aiml-gcp-onboard/"),
    "ak-matrix": ("AccuKnox", "AI/ML support matrix", H + "support-matrix/aiml-support-matrix/"),
    "ak-shadow": ("AccuKnox", "Shadow AI discovery", H + "use-cases/shadow-ai-discovery/"),
    "ak-v35": ("AccuKnox", "v3.5 release notes", H + "getting-started/3.5-release/"),
    "ak-v36": ("AccuKnox", "v3.6 release notes", H + "getting-started/3.6-release/"),
    "ak-chrome": ("AccuKnox", "Chrome browser plugin", H + "integrations/chrome-browser-integration/"),
    "ak-edge": ("AccuKnox", "Edge browser plugin", H + "integrations/edge-browser-integration/"),
    "ak-intune": ("AccuKnox", "Browser plugin rollout with Intune", H + "integrations/intune-browser-plugin-deployment/"),
    "ak-mlscan": ("AccuKnox", "ML model static scans", H + "how-to/ml-static-scan/"),
    "ak-llmscan": ("AccuKnox", "LLM static scans", H + "how-to/llm-static-scan/"),
    "ak-cicd": ("AccuKnox", "Model scan in CI/CD", H + "how-to/model-scan-cicd/"),
    "ak-xbom": ("AccuKnox", "xBOM setup", H + "getting-started/xbom-setup/"),
    "ak-redteam": ("AccuKnox", "AI red teaming", H + "use-cases/red-teaming/"),
    "ak-probes": ("AccuKnox", "Red team categories and probes", H + "use-cases/subprompts-categories/"),
    "ak-collectors": ("AccuKnox", "Red team custom models", H + "how-to/aiml-custom-model-redteaming/"),
    "ak-pf": ("AccuKnox", "Prompt Firewall overview", H + "use-cases/prompt-firewall-overview/"),
    "ak-sdk": ("AccuKnox", "SDK LLM defense", H + "how-to/llm-defense-app-onboard/"),
    "ak-api": ("AccuKnox", "Runtime defense API method", H + "how-to/aiml-runtime-onboard/"),
    "ak-aiint": ("AccuKnox", "AI security integrations", H + "integrations/ai-overview/"),
    "ak-apim": ("AccuKnox", "Azure APIM with AI Foundry", H + "getting-started/azure-ai-foundry/"),
    "ak-modelarmor": ("AccuKnox", "ModelArmor", H + "use-cases/modelarmor/"),
    "ak-agentz": ("AccuKnox", "AgentZ", H + "agentz/"),
    "ak-intmx": ("AccuKnox", "Integration support matrix", H + "integrations/support-matrix/"),
    "ak-aidr": ("AccuKnox", "AI detection and response", H + "use-cases/aidr/"),
    "ak-azaidr": ("AccuKnox", "Azure AI-DR setup", H + "how-to/azure-aidr/"),
    "ak-comp": ("AccuKnox", "Compliance matrix", H + "support-matrix/compliance-matrix/"),
    "ak-onprem": ("AccuKnox", "SaaS vs on-prem for AI security", H + "how-to/aiml-saas-vs-onprem/"),
    "ak-deploy": ("AccuKnox", "Deployment models", H + "getting-started/deployment-models/"),
    "ak-faq": ("AccuKnox", "AI security FAQ", H + "faqs/ai-security/"),
    # ---- AccuKnox, website, for the two Beta modules --------------------
    "ak-web-ai": ("AccuKnox", "AI Security platform page", W + "platform/ai-security"),
    "ak-web-agentic": ("AccuKnox", "Agentic AI Security page", W + "solutions/agentic-ai-security"),
    "ak-web-grc": ("AccuKnox", "AI Governance and Compliance page", W + "platform/ai-governance-compliance"),
    # ---- Netskope, docs --------------------------------------------------
    "ns-aisec": ("Netskope", "AI Security (docs index)", N + "ai-security"),
    "ns-aicc": ("Netskope", "AI Command Center", N + "ai-command-center"),
    "ns-inventory": ("Netskope", "AI Inventory", N + "ai-inventory"),
    "ns-platforms": ("Netskope", "AI Platforms discovery and posture", N + "ai-platforms-discovery-and-security-posture-management"),
    "ns-client": ("Netskope", "Netskope Client AI Discovery", N + "netskope-client-ai-discovery"),
    "ns-claude": ("Netskope", "Anthropic Claude support for AICC", N + "anthropic-claude-support-for-ai-discovery"),
    "ns-guardrails": ("Netskope", "AI Guardrails", N + "ai-guardrails"),
    "ns-profile": ("Netskope", "AI Guardrails profile", N + "ai-security-guardrails-profile"),
    "ns-topics": ("Netskope", "AI Guardrails custom topics", N + "ai-guardrails-custom-topics"),
    "ns-rtp": ("Netskope", "AI Guardrails policy for Real-time Protection", N + "creating-an-ai-security-guardrails-policy-for-real-time-protection"),
    "ns-gw": ("Netskope", "AI Gateway", N + "ai-gateway"),
    "ns-gwov": ("Netskope", "AI Gateway overview", N + "ai-gateway-overview"),
    "ns-gwpol": ("Netskope", "AI Gateway guardrails policy", N + "ai-guardrails-policy"),
    "ns-gw18": ("Netskope", "AI Gateway 1.8 release notes", N + "new-features-and-enhancements-in-ai-gateway-1-8"),
    "ns-gwprov": ("Netskope", "Register a custom AI provider", N + "add-or-register-a-custom-ai-provider"),
    "ns-gwlic": ("Netskope", "AI Gateway licensing terms", N + "ai-gateway-licensing-terms"),
    "ns-aicclic": ("Netskope", "AI Command Center licensing terms", N + "ai-command-center-licensing-terms"),
    "ns-redteam": ("Netskope", "AI Red Teaming", N + "ai-red-teaming"),
    "ns-target": ("Netskope", "Creating a red team target", N + "creating-a-target"),
    "ns-prompts": ("Netskope", "Red team prompt library", N + "prompt-library"),
    "ns-drift": ("Netskope", "Model Drifting", N + "model-drifting"),
    "ns-aac": ("Netskope", "Agent Action Control", N + "agent-action-control"),
    "ns-broker": ("Netskope", "Agentic Broker", N + "agentic-broker"),
    "ns-mcpvis": ("Netskope", "Visibility into MCP usage", N + "visibility-into-mcp-usage"),
    "ns-mcprtp": ("Netskope", "Real-time Protection for MCP", N + "real-time-protection-policies-for-mcp-security"),
    "ns-mcpcat": ("Netskope", "MCP catalog and risk assessment", N + "app-catalog-and-risk-assessment"),
    "ns-mcpgw": ("Netskope", "MCP Gateway overview", N + "mcp-gateway-overview"),
    "ns-mcpgwcfg": ("Netskope", "Configuring MCP Gateway", N + "configuring-mcp-gateway"),
    "ns-mcpdlp": ("Netskope", "MCP granular control and DLP", N + "granular-control-and-data-loss-prevention-dlp"),
    "ns-incidents": ("Netskope", "AI Guardrails incidents", N + "viewing-ai-security-incidents"),
    "ns-aisecops": ("Netskope", "AI Security Ops, August 2026 release", N + "ai-security-ops-release-notes-version-august-2026"),
    "ns-dspm": ("Netskope", "DSPM overview", N + "netskope-dspm-overview"),
    "ns-deployvm": ("Netskope", "Deploy AI Gateway on Netskope portal", N + "deploy-ai-gateway-on-netskope-portal"),
    # ---- Netskope, website -----------------------------------------------
    "ns-web-products": ("Netskope", "Netskope Skylight AI Security", "https://www.netskope.com/products/ai-products"),
    "ns-web-aisec": ("Netskope", "AI Security product page", "https://www.netskope.com/products/ai-security"),
}

# status labels used in both columns
GA, BETA, PREVIEW, ROADMAP, NOTDOC, ADDON = (
    "GA", "Beta", "Preview", "Roadmap", "Not documented", "GA, separate license")

# edge values
AK, NS, PAR, NA = "AccuKnox", "Netskope", "Parity", "Not scored"

CATEGORIES = [
    ("A", "Discovery and AI Posture (AI-SPM)"),
    ("B", "Model Security and Red Teaming"),
    ("C", "Runtime Guardrails"),
    ("D", "Agentic AI and MCP"),
    ("E", "Detection, Response and Governance"),
    ("F", "Deployment and Licensing"),
]

# the claim each category proves, used as the H2 and the slide title
HEADLINES = {
    "A": "AccuKnox Finds AI on Servers and Clouds, Netskope Finds It on Laptops",
    "B": "AccuKnox Scans the Model File Before It Loads",
    "C": "The AccuKnox SDK Enforces Guardrails Without Rerouting Traffic",
    "D": "AccuKnox Sandboxes the Agent Host, Netskope Controls MCP Messages",
    "E": "AccuKnox Watches AI Control Plane Logs and Maps AI Frameworks",
    "F": "AccuKnox Runs Fully Air-Gapped With No Cloud Tenant",
}

# Each row:
#   id, cat, capability
#   ak / ak_short / ak_status / ak_src
#   ns / ns_short / ns_status / ns_src
#   edge, why
ROWS = [
    # ================================================================ A
    dict(
        id="A1", cat="A", capability="Cloud AI service inventory",
        ak=("Agentless read-only roles on AWS, Azure and GCP inventory managed AI services. "
            "The support matrix names SageMaker, Bedrock, Azure OpenAI, Azure AI Studio, Vertex AI and Google AI Studio. "
            "v3.5 adds managed agents from Copilot Studio, Microsoft 365 Agents, Azure AI Foundry, Bedrock AgentCore and Bedrock Agent. "
            "A pipeline graph shows each asset with its linked services and exposure."),
        ak_short="Agentless roles on AWS, Azure, GCP. SageMaker, Bedrock, Azure OpenAI, Vertex AI, plus 5 managed agent sources. Pipeline graph.",
        ak_status=GA, ak_src=["ak-aws", "ak-matrix", "ak-v35", "ak-shadow"],
        ns=("AI Command Center discovers 13 AI platforms: 5 on AWS, 4 on Azure and 4 on GCP. "
            "It runs static configuration checks on custom agents, enterprise chatbots and model serving. "
            "Findings trace IAM, network, storage and encryption controls. "
            "Netskope marks this capability as a preview feature."),
        ns_short="AI Command Center covers 13 AI platforms on AWS, Azure, GCP with configuration checks. Marked preview.",
        ns_status=PREVIEW, ns_src=["ns-platforms"],
        edge=AK, why="Both inventory the same clouds. The AccuKnox inventory is GA, and the Netskope one is a preview feature."),
    dict(
        id="A2", cat="A", capability="Self-hosted and shadow AI discovery",
        ak=("A VM snapshot scan, an agent-based VM scan and an in-cluster Kubernetes scanner find AI packages on servers. "
            "Packages fall into 7 types, including inference engines (vLLM, TGI, Triton, llama.cpp, Ollama), AI SDKs, AI gateways and MCP. "
            "Cloud assets show as Managed and on-prem assets show as Unmanaged."),
        ak_short="VM snapshot, VM agent and Kubernetes scanners. 7 package types: vLLM, TGI, Triton, llama.cpp, Ollama, SDKs, MCP.",
        ak_status=GA, ak_src=["ak-shadow", "ak-arch"],
        ns=("The Netskope Client scans managed endpoints for AI agents, local LLMs (Ollama, LM Studio, Jan AI, GPT4All), MCP servers and IDE or browser AI extensions. "
            "It runs on Windows and macOS with Client 138 or later. "
            "Netskope states it misses AI assets in VMs or containers that do not run the Client. "
            "It detects only assets in the Netskope signature file."),
        ns_short="Netskope Client on Windows and macOS laptops. Signature based. Misses VMs and containers without the Client.",
        ns_status=GA, ns_src=["ns-client", "ns-aicc"],
        edge=AK, why="AccuKnox scans servers and clusters where models are served. Netskope scans employee laptops. Pick by where your models run."),
    dict(
        id="A3", cat="A", capability="Workforce GenAI app visibility and control",
        ak=("A browser plugin runs on Chrome, Edge and Firefox, and the v3.5 notes add Safari and Brave. "
            "It records GenAI use with user, time and domain. "
            "It applies the Prompt Firewall on ChatGPT, Claude, Gemini, GitHub Copilot and, from v3.6, Microsoft Copilot. "
            "Intune can force-install the plugin on Windows and macOS."),
        ak_short="Browser plugin on Chrome, Edge, Firefox (plus Safari, Brave in v3.5). 5 GenAI apps. Intune rollout.",
        ak_status=GA, ak_src=["ak-chrome", "ak-edge", "ak-intune", "ak-v35", "ak-v36"],
        ns=("The Next Gen Secure Web Gateway identifies 3,300+ Gen AI apps. "
            "Admins apply activity-based and instance-based policies, app tags and real-time user coaching. "
            "The traffic must be steered through Netskope."),
        ns_short="Secure Web Gateway identifies 3,300+ Gen AI apps. Activity and instance policies. User coaching.",
        ns_status=GA, ns_src=["ns-aisec", "ns-rtp"],
        edge=NS, why="Netskope sees every web app because its proxy carries all user traffic. AccuKnox covers the named apps through the plugin."),

    # ================================================================ B
    dict(
        id="B1", cat="B", capability="Model file static scanning",
        ak=("AccuKnox scans model files pulled from GitHub or Hugging Face in a sandbox evaluator. "
            "The formats are Pickle, HDF5/H5, TensorFlow SavedModel, model checkpoints and ONNX. "
            "Checks cover supply chain and provenance, adversarial robustness, data and privacy risks and model file security. "
            "A finding can open a Jira ticket."),
        ak_short="Sandbox scan of Pickle, HDF5/H5, TF SavedModel, checkpoints, ONNX from GitHub or Hugging Face.",
        ak_status=GA, ak_src=["ak-mlscan"],
        ns=("The Netskope AI Security docs list six modules: Access Control, AI Gateway, AI Red Teaming, AI Guardrails, Agent Action Control and Agentic Broker. "
            "None of the six pages describes a scan of model artifacts. "
            "AI Gateway 1.8 adds TSS Fast Scan, which checks files in transit for malware."),
        ns_short="No model artifact scan in the AI Security docs. AI Gateway 1.8 scans files in transit for malware.",
        ns_status=NOTDOC, ns_src=["ns-aisec", "ns-gw18"],
        edge=AK, why="AccuKnox inspects the model file before it loads. Netskope inspects traffic around the model."),
    dict(
        id="B2", cat="B", capability="AI supply chain in CI/CD and AIBOM",
        ak=("xBOM emits CycloneDX 1.6 SBOM, CBOM and AIBOM files. "
            "The AIBOM source is Hugging Face or Bedrock. "
            "It runs from knoxctl, GitHub Actions, Azure DevOps or Jenkins. "
            "A pull request comment of /scan triggers a model scan and posts the report back to the pull request."),
        ak_short="CycloneDX 1.6 AIBOM from Hugging Face or Bedrock. knoxctl, GitHub Actions, Azure DevOps, Jenkins.",
        ak_status=GA, ak_src=["ak-xbom", "ak-cicd", "ak-v35"],
        ns=("The Netskope AI Security docs and product pages describe no AIBOM output and no model scan step for a CI/CD pipeline."),
        ns_short="No AIBOM and no pipeline model scan in the AI Security docs.",
        ns_status=NOTDOC, ns_src=["ns-aisec", "ns-web-products"],
        edge=AK, why="AccuKnox puts the model into the same bill of materials as the code."),
    dict(
        id="B3", cat="B", capability="LLM red teaming",
        ak=("Probes come in 14 families, including prompt injection, encoding, latent injection, TAP, malware generation, package hallucination and XSS. "
            "You can upload custom prompts as JSON, and Intelligent Scan builds prompts from a model purpose. "
            "Collectors reach Ollama, vLLM, NVIDIA Triton and Bedrock endpoints, plus any OpenAI-compatible API. "
            "Scans run on demand or on a cron schedule. Findings map to OWASP LLM Top 10, MITRE ATLAS and AVID."),
        ak_short="14 probe families, custom JSON prompts, Intelligent Scan. Collectors for Ollama, vLLM, Triton, Bedrock. OWASP, ATLAS, AVID.",
        ak_status=GA, ak_src=["ak-probes", "ak-redteam", "ak-collectors", "ak-llmscan", "ak-v36"],
        ns=("AI Red Teaming sends adversarial prompts to targets that you register by REST API, LLM or OpenAI-compatible API. "
            "Named foundation models are OpenAI, Azure OpenAI and Amazon Bedrock, and custom models can run locally or in a public cloud. "
            "Results show attack success rate by prompt set, technique and OWASP category. "
            "Model Drifting charts the rate across the 10 most recent test rounds."),
        ns_short="REST, LLM or OpenAI-compatible targets. Attack success rate by OWASP category. Drift chart over 10 rounds.",
        ns_status=GA, ns_src=["ns-redteam", "ns-target", "ns-prompts", "ns-drift"],
        edge=PAR, why="Both ship automated red teaming. Netskope adds a drift chart. AccuKnox adds code, hallucination and package hallucination probes."),

    # ================================================================ C
    dict(
        id="C1", cat="C", capability="Guardrail enforcement points",
        ak=("The Prompt Firewall runs in 4 modes. The Python SDK accuknox-llm-defense calls scan_prompt and scan_response inside your app. "
            "A REST API serves any language. Azure APIM blocks with 403 Forbidden in front of Azure AI Foundry. "
            "Apigee inspects each prompt and forwards on error. Bifrost and LiteLLM log and categorize. The browser plugin covers employee use."),
        ak_short="4 modes: in-app Python SDK, REST API, AI gateways (Azure APIM blocks), browser plugin.",
        ak_status=GA, ak_src=["ak-sdk", "ak-api", "ak-aiint", "ak-apim", "ak-pf"],
        ns=("AI Guardrails run inline in Real-time Protection for 20 listed Gen AI apps, with actions Alert, Allow, Block and User Alert. "
            "The AI Gateway appliance guards app-to-LLM traffic for OpenAI-compatible, Gemini and Claude schemas, with Monitor, Block and Replace. "
            "Traffic must be steered to the gateway. Other schemas get access control and rate limits without content inspection."),
        ns_short="Inline proxy for 20 Gen AI apps. AI Gateway appliance for OpenAI-compatible, Gemini, Claude traffic.",
        ns_status=GA, ns_src=["ns-guardrails", "ns-rtp", "ns-gwov", "ns-gwpol", "ns-gwprov"],
        edge=AK, why="The AccuKnox SDK enforces inside the application with no network steering. Netskope needs traffic sent to its proxy or appliance."),
    dict(
        id="C2", cat="C", capability="Guardrail detection policies",
        ak=("14 policy classes include Prompt Injection, Toxicity, Secrets, Anonymize (PII and PHI), Ban Topics, Ban Code, Regex, Language, Token Limit and Relevance. "
            "v3.6 adds an Attachment Type scanner. "
            "The engine is stateful and scores the whole exchange for a session_id, which catches a jailbreak split across turns. "
            "Policies apply to all apps or to one app."),
        ak_short="14 policy classes incl. injection, secrets, PII/PHI, code, token limit. Stateful per session_id.",
        ak_status=GA, ak_src=["ak-pf", "ak-sdk", "ak-v36"],
        ns=("10 predefined categories include prompt injection and jailbreak, malicious URLs, newly registered domains and 7 content harm categories. "
            "Each category takes a low, medium or high confidence level. "
            "Admins add up to 256 keywords, 10 semantic match phrases and up to 30 custom topics, which Netskope marks Beta. "
            "The docs list 29 supported languages."),
        ns_short="10 categories incl. injection, malicious URLs. 256 keywords, 30 custom topics (Beta). 29 languages.",
        ns_status=GA, ns_src=["ns-profile", "ns-topics", "ns-guardrails"],
        edge=AK, why="AccuKnox adds code, secrets and token-limit policies and multi-turn state. Netskope adds URL reputation and a longer language list."),
    dict(
        id="C3", cat="C", capability="Sensitive data protection in prompts",
        ak=("The Anonymize policy masks PII and PHI with pattern matching and named entity recognition. "
            "The Secrets policy blocks API keys, tokens and credentials before the LLM processes them. "
            "The Regex policy matches custom patterns."),
        ak_short="Anonymize masks PII and PHI. Secrets policy for keys and credentials. Custom regex.",
        ak_status=GA, ak_src=["ak-pf"],
        ns=("Netskope DLP profiles, such as PII and PCI, apply to Gen AI prompts, AI Gateway traffic and MCP tool calls. "
            "They are the same profiles used for SaaS, email and endpoint. "
            "DLP is an add-on license for AI Gateway and Agentic Broker."),
        ns_short="Enterprise DLP profiles on prompts, gateway and MCP traffic. Add-on license.",
        ns_status=ADDON, ns_src=["ns-gw", "ns-gwlic", "ns-mcpdlp", "ns-claude"],
        edge=NS, why="Netskope reuses one DLP policy set across AI, SaaS, email and endpoint."),

    # ================================================================ D
    dict(
        id="D1", cat="D", capability="Agent runtime sandbox",
        ak=("ModelArmor runs on KubeArmor with eBPF and LSM. "
            "It enforces process, file, network and domain policy for Ollama, vLLM, Triton, LangGraph, n8n, CrewAI, OpenClaw, Strands and MCP servers. "
            "It needs no code change and works on VMs, containers and Kubernetes. "
            "AgentZ runs agents in a default-deny sandbox with RBAC per tool call."),
        ak_short="ModelArmor: eBPF and LSM on the host for agents and MCP servers. AgentZ default-deny sandbox.",
        ak_status=GA, ak_src=["ak-modelarmor", "ak-agentz", "ak-arch"],
        ns=("Agent Action Control applies intent, risk and access policies to agent traffic. "
            "It covers 79 SaaS and cloud apps and 70 named agents, including Claude Code, Cursor and ChatGPT Desktop. "
            "Netskope marks it Beta, and support must enable it per tenant."),
        ns_short="Agent Action Control on agent traffic to 79 apps, 70 agents. Beta.",
        ns_status=BETA, ns_src=["ns-aac"],
        edge=AK, why="AccuKnox blocks the system call on the host where the agent runs. Netskope controls the API action in agent traffic."),
    dict(
        id="D2", cat="D", capability="MCP visibility and control",
        ak=("The shadow AI scanners classify MCP packages on VMs and clusters. "
            "ModelArmor sandboxes the MCP server process, and AgentZ adds per-tool MCP sandbox controls. "
            "Protocol-level MCP policies are on the AccuKnox roadmap."),
        ak_short="MCP discovery and process sandbox. Protocol-level MCP policy is roadmap.",
        ak_status=GA + ", policies on " + ROADMAP, ak_src=["ak-shadow", "ak-modelarmor", "ak-agentz", "ak-v35"],
        ns=("Agentic Broker logs MCP messages such as CallToolRequest and ReadResourceRequest in Skope IT. "
            "Real-time Protection blocks by server, tool or activity, and a catalog risk-scores public MCP servers. "
            "MCP Gateway applies access control, DLP, guardrails and rate limits for up to 100 MCP providers per tenant. "
            "Agentic Broker needs its own license."),
        ns_short="Agentic Broker and MCP Gateway inspect and block MCP messages by server, tool, activity. Separate license.",
        ns_status=ADDON, ns_src=["ns-broker", "ns-mcpvis", "ns-mcprtp", "ns-mcpcat", "ns-mcpgw", "ns-mcpgwcfg"],
        edge=NS, why="Netskope reads MCP protocol messages today. AccuKnox isolates the MCP server process on the host."),
    dict(
        id="D3", cat="D", capability="AI agent identity",
        ak=("AI Identity Security is Beta. "
            "It gives every agent its own SPIFFE identity with cryptographic attestation. "
            "Per-agent permissions are enforced through OpenFGA, and the full upstream caller chain is checked before access."),
        ak_short="Beta. SPIFFE identity per agent, OpenFGA permissions, caller chain check.",
        ak_status=BETA, ak_src=["ak-web-ai", "ak-web-agentic", "ak-arch"],
        ns=("AI Command Center inventories identities as IdP-authenticated users, and it identifies unknown sources by IP address. "
            "The Claude integration, a preview feature, lists API keys with scopes and age. "
            "The docs describe no per-agent workload identity."),
        ns_short="Identities are IdP users and unknown IPs. Claude API key inventory (preview).",
        ns_status=GA, ns_src=["ns-aicc", "ns-claude"],
        edge=AK, why="AccuKnox issues an identity to the agent itself. Netskope attributes AI use to the human user."),

    # ================================================================ E
    dict(
        id="E1", cat="E", capability="AI detection and response on cloud logs",
        ak=("AI-DR reads AWS CloudTrail, Azure Event Hub and GCP logs out of band. "
            "It detects events such as an insecure SageMaker notebook, a Bedrock customization job or an Azure OpenAI deletion. "
            "A webhook and GitHub Actions can set a public Azure OpenAI asset back to private. "
            "Alerts route to Jira, ServiceNow, Slack and PagerDuty."),
        ak_short="CloudTrail, Event Hub, GCP logs. Detects AI control plane changes. Auto-remediation to private.",
        ak_status=GA, ak_src=["ak-aidr", "ak-azaidr", "ak-faq"],
        ns=("AISecOps agents triage DLP alerts, including Microsoft Purview alerts, and rank insider-risk users with EDR device data. "
            "AI Guardrails incidents appear in Skope IT with a false-positive report. "
            "The AI Security docs describe no detection on AI cloud control-plane logs."),
        ns_short="AISecOps agents triage DLP and insider alerts. No AI control-plane log detection documented.",
        ns_status=GA, ns_src=["ns-aisecops", "ns-incidents", "ns-aisec"],
        edge=AK, why="AccuKnox watches who changed the AI service. Netskope watches what users send to it."),
    dict(
        id="E2", cat="E", capability="Compliance mapping and AI GRC",
        ak=("Findings map to OWASP LLM Top 10 v2025, MITRE ATLAS, NIST AI RMF and AVID today. "
            "AI GRC is Beta. It classifies the EU AI Act risk tier of each model and tags findings to 12+ frameworks, including ISO 42001. "
            "It generates audit reports in SaaS or air-gapped installs."),
        ak_short="OWASP LLM Top 10, ATLAS, NIST AI RMF, AVID today. AI GRC Beta: EU AI Act tiers, ISO 42001, 12+ frameworks.",
        ak_status=GA + ", AI GRC " + BETA, ak_src=["ak-comp", "ak-onprem", "ak-web-grc", "ak-arch"],
        ns=("AI Guardrails and AI Red Teaming map findings to OWASP Top 10 LLM and MITRE ATLAS. "
            "The Claude integration, a preview feature, checks configurations against GDPR, HIPAA and AICPA."),
        ns_short="OWASP LLM and MITRE ATLAS mapping. Claude posture to GDPR, HIPAA, AICPA (preview).",
        ns_status=GA, ns_src=["ns-aisec", "ns-guardrails", "ns-claude"],
        edge=AK, why="AccuKnox maps to the AI-specific frameworks an auditor asks for. Netskope maps its guardrail and red team findings."),

    # ================================================================ F
    dict(
        id="F1", cat="F", capability="Deployment model",
        ak=("SaaS, or self-hosted on your Kubernetes or a 3-node VM cluster. "
            "The self-hosted install runs air-gapped and gets updates as tar.gz images. "
            "The docs state full feature parity with SaaS, except the AskADA assistant. "
            "The documented VM size is 8 vCPU, 32 GB memory and 256 GB storage."),
        ak_short="SaaS or self-hosted, air-gapped. Feature parity except AskADA. 8 vCPU, 32 GB, 256 GB.",
        ak_status=GA, ak_src=["ak-onprem", "ak-deploy"],
        ns=("The management console runs in the Netskope cloud tenant. "
            "The AI Gateway appliance runs on AWS, GCP, Azure or VMware ESXi with 16 vCPU, 32 GB memory and 200 GB disk. "
            "The appliance enrolls with the tenant and needs egress to Netskope URLs. "
            "AI Guardrails is available in FedRAMP and PBMM tenants."),
        ns_short="Cloud tenant console. Gateway appliance on AWS, GCP, Azure, ESXi. FedRAMP and PBMM tenants.",
        ns_status=GA, ns_src=["ns-gwov", "ns-deployvm", "ns-guardrails"],
        edge=AK, why="AccuKnox runs the whole platform with no internet link. Netskope keeps policy and logs in its cloud."),
    dict(
        id="F2", cat="F", capability="Licensing model",
        ak=("One platform carries AI-SPM, model scanning, red teaming, the Prompt Firewall and AI-DR. "
            "The architecture page lists six modules as generally available. "
            "[confirm the AccuKnox AI Security licensing unit and tiers with AccuKnox sales]"),
        ak_short="Six GA modules on one platform. [confirm licensing unit with AccuKnox sales]",
        ak_status=GA, ak_src=["ak-arch"],
        ns=("AI Command Center bills per AI asset over a rolling 90 days, and it stops showing new assets past the quota. "
            "AI Gateway bills per gateway plus monthly transactions, and service suspends until month end past the limit. "
            "DLP and Agentic Broker are separate licenses."),
        ns_short="Per AI asset (AICC) and per gateway plus monthly transactions. DLP and Agentic Broker extra.",
        ns_status=GA, ns_src=["ns-aicclic", "ns-gwlic", "ns-broker"],
        edge=NA, why="Netskope publishes its units. Compare quotes once AccuKnox confirms its unit."),
]

# where Netskope leads, stated plainly, used on the XLSX summary and a slide
NETSKOPE_LEADS = [
    ("Workforce coverage", "The Secure Web Gateway identifies 3,300+ Gen AI apps across all user traffic.", "ns-aisec"),
    ("Enterprise DLP", "One DLP profile set covers AI prompts, SaaS, email and endpoint.", "ns-mcpdlp"),
    ("MCP protocol control", "Agentic Broker and MCP Gateway inspect and block MCP messages today.", "ns-mcpgw"),
    ("Regulated tenants", "AI Guardrails runs in FedRAMP and PBMM tenants.", "ns-guardrails"),
]

# where AccuKnox leads, used for Better, Faster, Cheaper
BETTER_FASTER_CHEAPER = [
    ("Better", "AccuKnox secures the model and the host, not only the traffic. "
               "It scans model files, emits a CycloneDX AIBOM and sandboxes agents with eBPF and LSM.",
     ["ak-mlscan", "ak-xbom", "ak-modelarmor"]),
    ("Faster", "Agentless roles on AWS, Azure and GCP fill the AI inventory with no proxy and no endpoint client. "
               "A self-hosted install takes 30 minutes to 4 hours.",
     ["ak-aws", "ak-onprem"]),
    ("Cheaper", "Six GA modules sit on one platform, with no separate gateway appliance to size. "
                "Netskope bills AI Gateway per instance plus monthly transactions, and DLP is extra.",
     ["ak-arch", "ns-gwlic"]),
]

# claims on the live accuknox.com/comparisons/accuknox-vs-netskope page that
# the sources contradict or do not support
LIVE_PAGE_FIXES = [
    ("Netskope AI security is SaaS-only.",
     "The Netskope AI Gateway runs as a virtual appliance on AWS, GCP, Azure or VMware ESXi.", "ns-gwov"),
    ("Netskope uses inline proxy with no dedicated AI gateway connectors.",
     "Netskope ships AI Gateway for app-to-LLM traffic and MCP Gateway for MCP traffic.", "ns-mcpgw"),
    ("Netskope limited to basic DLP pattern matching (session abuse).",
     "Netskope AI Guardrails detects prompt injection and jailbreak, with semantic matching and 29 languages.", "ns-profile"),
    ("Netskope uses DLP-based inline inspection only (prompt firewalling).",
     "AI Guardrails is a separate inspection engine mapped to MITRE ATLAS and OWASP LLM Top 10.", "ns-guardrails"),
    ("Netskope tracks SaaS AI app usage via CASB (shadow AI).",
     "The Netskope Client also finds local LLMs, agents and MCP servers on Windows and macOS endpoints.", "ns-client"),
    ("Netskope lacks native depth in agentic AI.",
     "Netskope ships Agentic Broker (GA, licensed) and Agent Action Control (Beta).", "ns-broker"),
    ("Netskope limited to alert-based notifications.",
     "Netskope AISecOps agents auto-investigate DLP and insider-risk alerts.", "ns-aisecops"),
    ("AccuKnox gateway list: Azure AI Foundry, AWS API Management, Apigee, Bifrost, LiteLLM.",
     "Azure APIM sits in front of Azure AI Foundry and blocks. Apigee forwards the request when validation fails. Bifrost and LiteLLM log and categorize only.", "ak-aiint"),
    ("AccuKnox browser plugin: Chrome and Firefox.",
     "The docs also cover Edge, and the v3.5 notes add Safari and Brave.", "ak-edge"),
    ("AI Agent Sandboxing, MCP Sandboxing and Untrusted Model Sandboxing marked Beta.",
     "The architecture page lists Agentic AI Security among six GA modules, and ModelArmor sandboxes MCP servers today.", "ak-arch"),
]


def src(key):
    return SOURCES[key]


def urls(keys):
    return [SOURCES[k][2] for k in keys]


def score():
    out = {AK: 0, NS: 0, PAR: 0, NA: 0}
    for r in ROWS:
        out[r["edge"]] += 1
    return out


# ---- icons, shared by the Sheet and the deck -----------------------------
TICK, PART, CROSS = "✅", "➖", "❌"
STATUS_LABEL = {
    "GA": TICK + " GA",
    "Beta": PART + " Beta",
    "Preview": PART + " Preview",
    "Roadmap": PART + " Roadmap",
    "Not documented": CROSS + " Not documented",
    "GA, separate license": TICK + " GA, separate license",
    "GA, policies on Roadmap": PART + " GA, MCP policies on roadmap",
    "GA, AI GRC Beta": TICK + " GA, AI GRC " + PART + " Beta",
}
EDGE_LABEL = {
    AK: TICK + " AccuKnox",
    NS: TICK + " Netskope",
    PAR: "⚖️ Parity",
    NA: PART + " Not scored",
}
LEGEND = [
    (TICK, "Supported and generally available (GA)."),
    (PART, "Partial. The vendor marks it Beta, Preview or Roadmap."),
    (CROSS, "Not documented in the vendor's AI Security docs or product pages."),
]


def status_label(s):
    return STATUS_LABEL[s]
