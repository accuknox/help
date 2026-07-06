---
title: AI Red Teaming
description: Automated adversarial testing for LLMs and ML models. Continuously stress-test your AI applications against prompt injection, jailbreaks, toxicity, hallucinations, and more.
---

# AI Red Teaming

AI Red Teaming is AccuKnox's automated adversarial testing capability that proactively stress-tests your LLMs and ML models against real-world attack techniques. Instead of waiting for attackers to find weaknesses, red teaming simulates hundreds of adversarial probes across multiple risk categories to surface vulnerabilities before they reach production.

![AccuKnox AI Security Architecture showing red teaming in the pre-deployment pipeline](./images/ai-overview/0.webp)

## What Is AI Red Teaming?

AI Red Teaming automates the process of attacking your own AI models and applications to discover security gaps. AccuKnox generates adversarial prompts tailored to your application's domain, executes them against your model in a sandboxed environment, and produces a risk assessment with the exact prompts and responses that triggered violations.

Unlike manual penetration testing, AccuKnox red teaming:

- **Runs automatically** every time a model or configuration changes
- **Scales to hundreds of probes** across multiple attack categories in minutes
- **Generates domain-specific tests** tailored to your application context
- **Produces actionable findings** with exact prompt/response pairs that violated policies
- **Maps to compliance frameworks** including OWASP Top 10 for LLMs and MITRE ATLAS

## Why Red Team Your AI?

| Risk | What Happens Without Red Teaming |
|------|----------------------------------|
| **Prompt Injection** | Attackers manipulate the LLM into ignoring system instructions, leaking data, or performing unauthorized actions |
| **Jailbreaks** | Users bypass safety guardrails to generate harmful, toxic, or policy-violating content |
| **Hallucinations** | The model confidently produces fabricated information that users trust and act on |
| **Data Leakage** | Sensitive training data, PII, or API keys are extracted through carefully crafted prompts |
| **Toxic Output** | The model generates hate speech, profanity, sexually explicit content, or threats |
| **Unsafe Code Generation** | The model produces malware, phishing scripts, or code with known vulnerabilities |

## Attack Categories

AccuKnox red teaming covers four primary scan categories. Each category contains multiple probes with specialized detectors.

### Sentiment Analysis

Tests whether the model can be manipulated into generating harmful, offensive, or inappropriate content.

| Probe | What It Tests | Detection Method |
|-------|---------------|------------------|
| Anthropomorphisation | Whether the LLM claims human attributes | String detection for first-person pronouns |
| Bullying | Generating harassment or intimidation content | RoBERTa toxicity classifier |
| Profanity | Producing offensive language across multiple categories (racial, religious, sexual, political) | String detection with comprehensive word lists |
| Sexual Content | Generating sexually explicit material | Google Perspective API + string detection |
| Toxicity (Threats, Insults, Flirtation, Severe Toxicity) | Multiple toxic output types tested with 50 prompts each | Google Perspective API ML models |
| Quack Medicine | Endorsing unproven or dangerous medical treatments | String detection for known false claims |

### Code Safety

Tests whether the model generates or enables malicious code execution.

| Probe | What It Tests | Detection Method |
|-------|---------------|------------------|
| Malware Generation | Producing malware subfunctions, payloads, evasion techniques (200+ prompts) | Regex-based code language detection |
| AV/Spam Signatures | Generating known malicious signatures (EICAR, GTUBE, GTphish) | Signature-based string matching |

### Hallucination

Tests whether the model fabricates false information or recommends non-existent resources.

| Probe | What It Tests | Detection Method |
|-------|---------------|------------------|
| False Assertions | Agreeing with clearly false statements | DistilBERT refutation detector + NLI model |
| Snowball | Doubling down on incorrect answers under pressure | Custom regex detection |
| Package Hallucination | Recommending non-existent packages (Python/PyPI, Ruby/Gems, JavaScript/npm, Rust/Crates) | Regex + HuggingFace package datasets |

### Prompt Injection

Tests whether the model's instructions can be overridden or its safety filters bypassed.

| Probe | What It Tests | Detection Method |
|-------|---------------|------------------|
| Grandma Exploit | Social engineering via role-play to extract restricted content | Mitigation bypass string detection |
| Do Not Answer | Probing restricted topics (150+ prompts across 5 subcategories) | Mitigation bypass detection |
| Encoding Attacks | Injecting instructions via Base64, Base16, Hex, ASCII85 encoding | Custom decode-and-match detectors |
| Latent Injection | Hiding instructions in documents, translations, resumes, reports | Trigger list string matching |
| Suffix Attacks | Appending adversarial suffixes to bypass alignment | Mitigation bypass detection |
| TAP (Tree of Attacks) | Multi-turn prompt escalation | Mitigation bypass detection |
| XSS / Data Exfiltration | Markdown image exfiltration, Colab data leakage, string assembly exfil | Custom regex detectors |

## How to Run a Red Team Scan

### Step 1: Add an LLM Static Scan Collector

Navigate to **Settings** > **Collectors** > **Add Collector** and select **LLM Static Scan**.

Choose your platform:

- **Custom Model** - Any model accessible via API endpoint
- **Ollama Model** - Locally hosted Ollama models
- **OpenAI Model** - OpenAI-hosted models (GPT-4, etc.)

![Add Collector page showing LLM Static Scan option with platform choices](../how-to/image-11.png)

### Step 2: Configure the Scan

Enter your model connection details and select the scan categories to test.

![LLM scan configuration showing scan category dropdown with Sentiment Analysis, Code, Hallucination, and Prompt Injection options](../how-to/image-12.png)

Available scan categories:

- **All** - Run all probe categories
- **Sentiment Analysis** - Toxicity, profanity, harmful content
- **Code** - Malware generation, malicious signatures
- **Hallucination** - False assertions, package hallucination
- **Prompt Injection** - Jailbreaks, encoding attacks, data exfiltration

You can also upload a **custom prompts file** (JSON array of prompt strings) to test domain-specific attack scenarios alongside the default probes.

### Step 3: Schedule and Run

Configure a cron schedule for continuous red teaming or trigger scans manually. Click **Save** to create the collector.

![Schedule configuration for LLM scan](../use-cases/image-4.png)

### Step 4: Review Findings

Navigate to **Issues** > **Findings** and select **LLM Findings** to view results.

![LLM Findings page showing scan results grouped by category with probes, detectors, goals, and risk scores](../how-to/image-18.png)

Each finding includes:

| Field | Description |
|-------|-------------|
| **Scan Category** | Which category flagged the issue (Sentiment, Code, Hallucination, Prompt Injection) |
| **Probe** | The specific probe that was triggered |
| **Detector** | The detection method used |
| **Goal** | What the adversarial prompt was trying to achieve |
| **Prompt** | The exact input sent to the model |
| **Output** | The model's response |
| **Risk Factor** | Severity rating (Critical, High, Medium, Low) |
| **Detector Safety Score** | How confident the detector is in the finding |
| **Compliance** | Mapped framework references (OWASP, AVID) |

### Step 5: Investigate and Remediate

Click any finding to open the detailed pane with description, solution, output, and prompt details.

![Detailed finding view showing description, solution, compliance frameworks, and Ask AI remediation](../how-to/image-19.png)

Use **Ask AI** for automated remediation recommendations based on the specific vulnerability detected.

![AI-generated remediation steps for a red teaming finding](../how-to/image-22.png)

### Step 6: Group and Export

Group findings by **Asset Type**, **Vulnerability Name**, **Scan Category**, or other parameters to prioritize remediation. Export grouped findings for reporting.

![Group findings by category with export options](../how-to/image-23.png)

## Supported Platforms

Red teaming scans are supported across both managed and on-premise AI deployments.

![Supported platforms showing managed deployments (AWS SageMaker, Bedrock, Google AI Studio, Azure AI, Anthropic, OpenAI, Vertex AI, Nutanix) and on-prem deployments (Ollama, vLLM, NVIDIA, Run.ai, Hugging Face, Kubeflow)](./images/ai-overview/1.png)


## Related Resources

- [LLM Static Scan Setup Guide](https://help.accuknox.com/how-to/llm-static-scan/)
- [Subprompts Categories and Probes](https://help.accuknox.com/use-cases/subprompts-categories/)
- [AI/ML Categories Reference](https://help.accuknox.com/use-cases/subprompts-categories/)
- [Prompt Firewall (Runtime Protection)](https://help.accuknox.com/how-to/prompt-firewall/)
- [ModelArmor: Adversarial Attacks](https://help.accuknox.com/use-cases/modelarmor-adverserial-attacks/)
