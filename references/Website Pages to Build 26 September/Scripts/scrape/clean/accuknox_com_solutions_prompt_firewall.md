Cloud Compliances]
Linux/Windows Scanning]
K8s Risk Assessment]
Serverless & Fargate]
AI-Accelerated SAST Scanning]
Threat Detection]
AI Identity Security]
Cloud Infrastructure Entitlement Management (CIEM)BETA]
Attack Surface Management (ASM)BETA]
SaaS Security Posture Management (SSPM)BETA]
Cloud Compliances]
Linux/Windows Scanning]
K8s Risk Assessment]
Serverless & Fargate]
AI-Accelerated SAST Scanning]
Threat Detection]
AI Identity Security]
Cloud Infrastructure Entitlement Management (CIEM)BETA]
Attack Surface Management (ASM)BETA]
SaaS Security Posture Management (SSPM)BETA]
# AI Guardrails & Prompt Firewall for LLM Traffic
## Inspect every prompt and response. Block injection, jailbreaks, data leaks at inference time.
## How The Prompt Firewall Works
A transparent proxy that inspects every prompt and response against your configured policies before allowing them through.
### Traffic Controller
The transparent proxy entry point. Users never talk directly to the LLM — all traffic routes through AccuKnox first.
IN
User prompt → scan against policies
OUT
LLM response → validate before delivery
ACT
Block · Sanitize · Monitor
### Policy Governance
Evaluates every prompt and response against your configured policies. Customizable per application.
IN
14 built-in policy types
IN
Custom regex + domain-specific rules
ACT
Global or per-app policy scope
### Audit & Compliance
Every request and response is recorded for compliance, investigation, and forensic analysis.
LOG
Full conversation history
LOG
Per-policy risk scores
LOG
Block/monitor/pass status + threshold
## See The Firewall In Action
From policy configuration to violation forensics — everything in one dashboard.
- ### AI-Security Dashboard
Query volumes, violations, and active policies at a glance.
- ### Policy Configuration
Add and customize local policies per application.
- ### Applied Policies
View all active policies enforcing on an application.
- ### Violation Analysis
Breakdown by policy type with severity and action taken.
## One Firewall, Four Ways to Deploy (Browser · Gateway/Proxy · SDK · Cloud API Gateway)
## AccuKnox Stateful Prompt Firewall and Why Per Prompt Inspection Fails Against Multi Turn Attacks
Multi turn attacks reach 96.2% success against frontier AI models. A firewall that scores messages in isolation never sees the session. Here is what stateful inspection changes.
[Read Blog]
## Integrate In Minutes
Wrap your existing LLM calls with prompt and response scanning. One import, two function calls.
- pip install accuknox-llm-defense
- Session linking for full audit trails
- BLOCK, MONITOR, PASS, or SANITIZE responses
- Per-policy risk scores for debugging
## Every Model. Every Platform.
Cloud, managed, or self-hosted — the Prompt Firewall works with your stack.
CLOUD LLM PROVIDERS
MANAGED AI SERVICES
ON-PREMISE MODELS
ENTERPRISE
## Set Up In Five Steps
From onboarding your application to monitoring violations in real time.
### Add Your Application
Navigate to AI/ML → Applications → Add Application. Name and tag your AI app.
### Configure Policies
Apply global policies for org-wide rules or local policies per application. Choose Block, Monitor, or Allow.
### Set Policy Scope
Global policies apply to all apps. Local policies let you customize — ban code in support bots but allow it in dev assistants.
### Monitor the Dashboard
Real-time visibility into total queries, policy violations, and active enforcement.
### Investigate & Audit
Click any violation for full conversation history, per-policy risk scores, and block/monitor status.
## Prompt Firewall + Red Teaming
**Red teaming finds the gaps. The Prompt Firewall enforces the rules to close them. Both work together.**
| CAPABILITY | RED TEAMING | PROMPT FIREWALL |
| When | Pre-deployment and scheduled scans | Runtime — every live request |
| What it does | Simulates adversarial attacks against models | Enforces policies on real user traffic |
| Action | Generate findings and risk reports | Block, sanitize, or monitor in real-time |
| Purpose | Discover vulnerabilities before attackers | Prevent attacks from succeeding |
| Coverage | Point-in-time assessment | Continuous, always-on protection |
| PII protection | Identifies potential exposure risks | Masks PII in real-time before LLM processes it |
| Prompt injection defense | Tests known injection patterns | ML-based detection on every request |
| Compliance | Audit reports | Continuous audit trail with full conversation logging |
## Prompt Firewall FAQs
1 **What is the AccuKnox Prompt Firewall?**
The AccuKnox Prompt Firewall is a transparent proxy that sits between users and the LLM. Every prompt and response routes through AccuKnox first, gets scanned against configured policies, and is then blocked, sanitized, monitored, or passed. Users never talk directly to the model. AccuKnox is one of the few platforms enforcing this inline on live traffic in both directions.
How does the Prompt Firewall stop prompt injection attacks?
It uses ML based detection to catch instruction overrides, roleplay exploits, and jailbreak attempts on every request. A prompt like "Ignore all previous instructions" is blocked before it reaches the model. Detection runs continuously on live traffic rather than as a one time scan, so new attack variants get caught at runtime.
3 **What types of threats does the AccuKnox Prompt Firewall block?**
AccuKnox enforces 14 built in policy types covering prompt injection, toxicity, secrets and API key leakage, PII and PHI exposure, banned topics, competitor mentions, gibberish, token limit abuse, relevance drift, and unapproved languages or code. Custom regex and domain specific rules layer on top. This breadth of runtime coverage sets the AccuKnox firewall apart from single purpose filters.
Does the Prompt Firewall protect PII and PHI?
Yes. The Anonymize policy detects and masks names, SSNs, emails, credit cards, and medical records in real time. An input like "My SSN is 123-45-6789" becomes "My SSN is \[REDACTED\]" before the LLM ever processes it. The Regex policy handles any custom format such as internal IDs or account numbers.
What is the difference between input and output policies?
Input policies inspect prompts before they reach the LLM. Output policies inspect responses before they reach the user. Both run on every interaction. This two way enforcement blocks a malicious prompt going in and catches sensitive data or policy violations in the model's reply coming back out.
How does the Prompt Firewall differ from model level safety filters?
Model level filters are baked into the LLM and cannot be tuned per application. The AccuKnox Prompt Firewall enforces custom policies outside the model, in both directions, with a full audit trail the model never provides. Enforcement can differ for a banking bot versus a developer assistant. That per application control is core to why teams pick AccuKnox over native filters.
7 **What actions can the Prompt Firewall take on a flagged request?**
Four actions. BLOCK stops the request entirely, SANITIZE masks the sensitive content and lets the rest through, MONITOR logs the event without interrupting flow, and PASS allows it. Each policy returns a per policy risk score, so thresholds are configurable and every action is traceable.
Can the AccuKnox Prompt Firewall run on premise or air gapped?
Yes. AccuKnox supports cloud, managed, and self hosted deployments, including on premise and air gapped environments. It works with cloud LLM providers, managed AI services, on premise open models, and enterprise stacks. This deployment flexibility makes AccuKnox a strong fit for federal, defense, and regulated teams that cannot send traffic to a vendor cloud.
How are global and local policies different?
Global policies apply org wide across every application. Local policies apply to a single app for customized enforcement. Code can be banned in a customer support bot while allowed in a developer assistant, all from the same dashboard.
10 **Which LLM providers and platforms does the Prompt Firewall support?**
It works across cloud LLM providers, managed AI services, on premise open source models, and enterprise platforms. Because the AccuKnox firewall operates as a transparent proxy wrapping existing LLM calls, it stays model agnostic and platform agnostic. Traffic points through it without swapping out the model.
11 **How long does it take to integrate the Prompt Firewall?**
Minutes. One package installs with pip install accuknox-llm-defense, then existing LLM calls get wrapped with two function calls for prompt and response scanning. Session linking ties requests together for full audit trails, and per policy risk scores help with debugging during setup.
How is the Prompt Firewall different from AI red teaming?
Red teaming finds gaps. The Prompt Firewall closes them. Red teaming runs pre deployment and on scheduled scans to simulate attacks and produce risk reports. The firewall enforces policies on every live request at runtime, blocking and sanitizing in real time. AccuKnox ships both together, so vulnerabilities get discovered and prevented from the same platform.
Does the AccuKnox Prompt Firewall help with compliance?
Yes. Every request and response is recorded with full conversation history, per policy risk scores, and block, monitor, or pass status. This continuous audit trail supports compliance, investigation, and forensic analysis, mapping directly to evidence requirements under SOC2, HIPAA, and NIST. AccuKnox gives compliance teams a defensible record of every AI interaction.
14 **How does the Prompt Firewall detect toxicity?**
It combines a RoBERTa classifier with the Perspective API to catch hate speech, threats, and explicit content. Racial slurs and death threats get blocked. A separate Sentiment policy flags aggressive or hostile inputs against configurable thresholds, allowing tone monitoring without hard blocking every heated message.
How do I set up the AccuKnox Prompt Firewall?
Five steps. Add the application under AI/ML, configure policies and choose Block, Monitor, or Allow, then set policy scope to global or local. The dashboard shows queries and violations in real time, and clicking any violation reveals full conversation history and per policy risk scores. Setup runs entirely from the AccuKnox dashboard.