**Subject:** Re: AccuKnox AI Security Comparative Matrix, Criteria and Maturity

Xue-san,

Thank you for the good questions. Our answers are below, current as of 14 October 2026.

**1. How we rate Supported and Partial**

Every vendor gets the same test, AccuKnox included. Each of the 8 modules has a benchmark of 3 parts, listed in section 2.

- **Supported:** the vendor's public pages show all 3 parts.
- **Partial:** the pages show 1 or 2 parts.
- **No evidence:** we found nothing after two or more searches.

Supported scores 1, Partial scores 0.5 and No evidence scores 0. AccuKnox scores 7.5 of 8.

The ratings show what each vendor publishes. They do not measure product depth, and a vendor may have features it does not publish. Page 7 of the matrix links each vendor's own source page, and each cell explains its rating. If a cell looks wrong to you, tell us and we will re-check it.

**2. Which Supported features are GA**

In the matrix, BETA marks a module with a part that is not yet generally available (GA). The Supported tick counts only the GA parts. Here is the status of each module.

**AI-SPM** (Supported). Covers AI inventory, shadow AI and pipeline posture.
GA: [cloud onboarding](https://help.accuknox.com/how-to/aiml-overview/) for AWS, Azure and GCP, [managed agent inventory](https://help.accuknox.com/getting-started/3.5-release/) for Copilot Studio, Microsoft 365 Agents, Azure AI Foundry and Bedrock AgentCore, [VM and Kubernetes scanning](https://help.accuknox.com/use-cases/shadow-ai-discovery/), and [model scans in CI/CD](https://help.accuknox.com/how-to/model-scan-cicd/).
Not yet GA: macOS host scanning and the desktop telemetry app are Beta. Windows host scanning is in progress.

**Agentic AI Security** (Supported). Covers managed agents, MCP and agent sandbox.
GA: the [ModelArmor](https://help.accuknox.com/use-cases/modelarmor/) runtime sandbox and [managed agent visibility](https://help.accuknox.com/getting-started/3.5-release/).
Not yet GA: [AgentZ](https://help.accuknox.com/agentz/) launched in August 2026, and its Coding workspace type is [Preview](https://docs.agentzharness.ai/faq/).

**AI-DR** (Supported). Covers detect, respond and block at runtime.
GA: all of it. [AI-DR](https://help.accuknox.com/use-cases/aidr/) reads AWS CloudTrail, Azure Event Hub and GCP logging, then raises alerts and tickets and can auto-remediate.
One limit: AI-DR does not block in the request path. Prompt Firewall and ModelArmor do the blocking, see the [architecture](https://help.accuknox.com/getting-started/ai-security-arch/).

**Prompt Guardrails & AI Gateway** (Supported, BETA). Covers inline firewall, injection and PII, and unsafe output.
GA: [Prompt Firewall](https://help.accuknox.com/use-cases/prompt-firewall-overview/) in the [browser extension](https://help.accuknox.com/getting-started/3.5-release/) for Chrome, Firefox, Safari, Brave and Edge, at the gateway, and with [LiteLLM and Bifrost](https://help.accuknox.com/integrations/ai-overview/).
Not yet GA: the AI Gateway.

**Compliance and AI-GRC** (Supported). Covers AIBOM, framework mapping and audit trail.
GA: [AIBOM generation](https://help.accuknox.com/getting-started/xbom-setup/), the [compliance module](https://help.accuknox.com/support-matrix/compliance-matrix/) with the EU AI Act and ISO/IEC 42001, and the Prompt Firewall request log for the audit trail.
Not yet GA: the dedicated AI-GRC module is coming soon, see the [architecture](https://help.accuknox.com/getting-started/ai-security-arch/).

**Red Team + AI DAST** (Supported, BETA). Covers attack library, live multi-turn attacks and CI/CD.
GA: [AI red teaming](https://help.accuknox.com/use-cases/red-teaming/) with scheduled scans and multi-turn attacks, mapped to OWASP LLM Top 10 and MITRE ATLAS, plus [DAST with 4 scan types](https://help.accuknox.com/how-to/dast-scan-types/) and [scans behind MFA](https://help.accuknox.com/getting-started/3.6-release/).
Not yet GA: AI DAST is coming soon.

**Model, Dataset + AI-SAST** (Supported, BETA). Covers model files, datasets and AI code scanning.
GA: [model file scans](https://help.accuknox.com/how-to/ml-static-scan/) for Pickle, HDF5/H5, TensorFlow SavedModel, checkpoints and ONNX, a [CI/CD gate](https://help.accuknox.com/how-to/model-scan-cicd/) for model scans, and [opt-in AI analysis](https://help.accuknox.com/getting-started/3.4-release/) of SAST findings.
Not yet GA: IDE-based AI SAST is coming soon.

**AI & Agent Identity Security** (Partial, BETA). Covers agent identity, least privilege and non-human identity (NHI).
GA: none as a module.
Not yet GA: the AI Identity Security module is coming soon, see the [overview](https://help.accuknox.com/how-to/aiml-overview/).

If it helps, we can send a feature-by-feature breakdown for the modules that matter most to your Guardian Agent review. Just tell us which ones.

Best regards,
John Kirch
