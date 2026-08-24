---
title: "Spain's AI Act Guidance Asks for Evidence, Not Intentions. A Runtime AI Control Produces It"
seo_title: "Spain AI Act Compliance: Runtime Evidence for AESIA"
meta_description: "Spain AI Act compliance means proving risks are controlled. See how a runtime prompt firewall and red teaming produce the evidence AESIA and the EU AI Act expect."
slug: "spain-ai-act-runtime-evidence-prompt-firewall"
url: "https://accuknox.com/blog/spain-ai-act-runtime-evidence-prompt-firewall"
primary_keyword: "Spain AI Act compliance"
secondary_keywords: ["AESIA guidelines", "EU AI Act high-risk", "Esquema Nacional de Seguridad", "prompt firewall compliance evidence"]
excerpt: "AESIA's guides and the EU AI Act ask high-risk AI providers to prove risks are controlled, continuously. A runtime prompt firewall and automated red teaming produce that proof."
category: "AI-SPM"
author: "Atharva Shah"
reading_time: "5 minutes"
word_count_target: 1100
audience: "security lead | CISO"
cover_image_prompt_claude: >
  An isometric illustration of a policy-enforcement layer sitting between a user, an
  application, and an AI model, with an audit-log ribbon flowing out to a compliance
  checklist. AccuKnox navy #11206D on white with #003BF6 accents, flat vector, generous
  negative space, no text in the image.
cover_image_prompt_midjourney: >
  isometric policy enforcement layer between user app and AI model, audit log ribbon to a
  compliance checklist, navy #11206D white #003BF6, flat vector, negative space
  --ar 16:9 --style raw --v 6 --no text
---

# Spain's AI Act guidance asks for evidence, and a runtime control is how you produce it

> **Cover image prompt:** A policy-enforcement layer between a user, an application, and an AI model, with an audit-log ribbon flowing to a compliance checklist. AccuKnox navy `#11206D` on white with `#003BF6` accents, flat vector, no text.

## TL;DR

- Spain AI Act compliance now has a concrete playbook: on 16 December 2025, [AESIA](https://aesia.digital.gob.es/en/present/20251216-guidelines-published-to-support-compliance-with-the-ai-act), Spain's AI supervision agency, published 16 practical guides, including 13 on technical requirements and a per-obligation checklist for providers and deployers of high-risk AI systems.
- The [EU AI Act](https://artificialintelligenceact.eu/high-level-summary/) requires high-risk providers, under Articles 8 to 17, to run a lifecycle risk-management system, automatically log events, and design for accuracy, robustness, and cybersecurity. Annex III high-risk obligations apply 24 months after entry into force.
- Both ask for evidence that identified risks are being controlled, not a statement of intent. A runtime AI control produces that evidence as it enforces.
- AccuKnox's prompt firewall analyzes prompts and responses, blocks sensitive data, restricts out-of-scope interactions, and keeps a complete audit trail. Automated red teaming supplies the adversarial-testing record the guidance expects.
- For the Spanish public sector, the same platform should map to the Esquema Nacional de Seguridad (ENS), which is mandatory for public bodies and their suppliers.

## What the Spanish guidance actually requires

AESIA is the Spanish Agency for the Supervision of Artificial Intelligence, a national market-surveillance authority. Its December 2025 release is not abstract policy. It is 16 guides built out of the Spanish AI regulatory sandbox, the first of its kind in Europe, which tested 12 high-risk AI systems across six sectors including biometrics, employment, healthcare, and critical infrastructure. The guides cover risk management, data governance, transparency, and cybersecurity, and each comes with a checklist tied to a specific obligation.

The guides are not binding and do not replace the regulation. What they do is make the AI Act operational: they tell a provider what a conformity assessment and an impact assessment look like in practice, and what evidence a supervisor will expect. In applicable high-risk scenarios, an organisation has to show that identified risks are effectively controlled. That word, show, is where most AI deployments fall short, because they have a policy document and no runtime proof.

## The EU AI Act asks for controls that run continuously

The AI Act's requirements for high-risk providers sit in Articles 8 to 17. Four of them describe a runtime control almost exactly.

- **Risk management system** across the full lifecycle, not a one-time assessment.
- **Record-keeping**, where the system automatically logs events relevant to identifying risks and substantial modifications.
- **Accuracy, robustness, and cybersecurity** by design.
- **Human oversight**, so a person can intervene in the system's operation.

General-purpose models with systemic risk, trained above 10^25 FLOPs, carry an extra duty to run model evaluations and adversarial testing and to report serious incidents. The compliance clock is real: Annex III high-risk obligations apply 24 months after the Act's entry into force, and prohibited-practice rules already applied at six months. A provider who waits for a supervisor to ask is starting the evidence trail too late.

## A prompt firewall turns an assessment finding into a running control

A red-teaming assessment tells you a model can be pushed off-topic or made to leak data. That is a finding. The AI Act wants the finding closed and the closure evidenced, continuously. A [stateful prompt firewall](https://accuknox.com/blog/llm-prompt-firewall-accuknox) is the layer that does both.

It sits between users, applications, and the model as a policy-enforcement point. It analyses prompts and responses, blocks sensitive information such as personal data from leaving, restricts out-of-scope interactions, and records every decision. Consider the failure the frameworks are built to prevent: a public-sector chatbot meant for tax questions, manipulated by prompt injection into producing political statements far outside its purpose. A firewall enforcing the chatbot's functional boundaries refuses that response and logs the attempt, which is both the control the AI Act's robustness requirement asks for and the evidence its record-keeping requirement asks for.

> **Image prompt (inline 1):** A policy-enforcement layer between a user, an application, and an AI model, one prompt blocked at the layer, an audit-log ribbon flowing to a compliance checklist. AccuKnox navy `#11206D` on white with `#003BF6` accents, flat vector, no text in the image.
>
> *Caption: The firewall enforces the model's boundaries inline and logs each decision, which is both the control and the evidence.*

| AI Act / AESIA obligation | What it demands | The AccuKnox control that produces the evidence |
| --- | --- | --- |
| Risk management (Art. 9) | Lifecycle identification and control of risks | [AI-SPM](https://accuknox.com/platform/aispm) inventory plus continuous policy enforcement |
| Record-keeping (Art. 12) | Automatic logging of risk-relevant events | Prompt firewall audit trail of every prompt, response, and block |
| Robustness and cybersecurity (Art. 15) | Resilience to manipulation and attack | Out-of-scope and injection guardrails enforced inline |
| Adversarial testing (GPAI, systemic risk) | Evidence of adversarial evaluation | [AI red teaming](https://accuknox.com/solutions/ai-red-teaming) run on every model change |

> **Existing screenshot (inline 2):** Use the prompt firewall dashboard from the PRODUCT UI library, `4_AI ML security/Agentic AI - Mar 6/dashboard_promptfirewall.png`. Crop the browser chrome and redact any tenant name before publishing.
>
> *Caption: The prompt firewall console, where each blocked prompt is both the enforced control and the logged evidence.*

The distinction that matters for a Spanish deployer: this evidence is generated as the control operates, not assembled by an analyst the week before an audit. The [EU AI Act compliance tooling](https://accuknox.com/blog/eu-ai-act-compliance-tools) overview covers the wider mapping.

## Add ENS mapping for the Spanish public sector

If the Spanish public-sector market matters to a vendor, the Esquema Nacional de Seguridad (ENS) is the framework to support. The ENS applies to the entire public sector and to the private companies that supply it, and it sets requirements for access control, confidentiality, integrity, traceability, authenticity, and availability. It was last updated by [Royal Decree 311/2022](https://ens.ccn.cni.es/en/what-is-the-ens), with detailed measures in the CCN-STIC 800-series guides.

Traceability and integrity are the ENS controls a runtime AI layer supports directly. The audit trail that satisfies the AI Act's record-keeping duty is the same evidence an ENS assessment wants for traceability. A platform that already carries ENS mappings removes a procurement blocker for any Spanish public body and its suppliers.

## Where to start in the Spanish market

For go-to-market, the [Red Nacional de SOC](https://www.first.org/members/teams/ccn-cert), the national network of security operations centres led by CCN-CERT, is a public map of mature security organisations. Since April 2024 it admits SOCs serving the private sector alongside public ones, and its accredited members include large operators such as Vodafone España and T-Systems Iberia. That roster is an initial list of partners and customers with the security maturity to adopt a runtime AI control.

The requirement across all three frameworks is the same. Prove the risk is controlled, and prove it continuously. Assessment finds the gap. A runtime control closes it and leaves the record that a supervisor, an ENS auditor, or a bank's risk team can read. Start with the assessment, then put the finding under enforcement.

## See why a prompt firewall belongs inline

This walkthrough covers what a prompt firewall enforces between users, applications, and the model, and why an enterprise needs one at runtime.

```html
<iframe width="560" height="315" src="https://www.youtube.com/embed/tlSplOfDFu4" title="Why Every Enterprise Needs a Prompt Firewall NOW" frameborder="0" allowfullscreen></iframe>
```

[Watch it on the AccuKnox YouTube channel](https://www.youtube.com/watch?v=tlSplOfDFu4).

## FAQs

### What did AESIA publish in December 2025?

Sixteen practical guides for EU AI Act compliance: two informative, 13 on technical requirements, and a checklist per obligation. They are guidance, not a replacement for the regulation.

### Does the EU AI Act require runtime controls specifically?

It names no product, but its high-risk requirements in Articles 8 to 17, lifecycle risk management, event logging, and robustness, describe controls that run continuously. A prompt firewall and red teaming satisfy them in practice.

### What is the ENS and who does it apply to?

Spain's national security framework, regulated by Royal Decree 311/2022. It is mandatory for the entire public sector and for private companies that supply it.

### How does a prompt firewall help with compliance evidence?

It enforces the model's boundaries in real time and logs every prompt, response, and block. The enforcement closes the gap, and the log is the record-keeping evidence an audit asks for.
