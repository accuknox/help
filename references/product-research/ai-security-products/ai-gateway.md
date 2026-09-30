---
title: AccuKnox AI Gateway, Product Notes
updated: 2026-09-26
tier: A unless a row says otherwise
---

# AccuKnox AI Gateway

The AccuKnox AI Gateway is one routing and governance layer for all AI model traffic in an
organization. The prompt firewall runs natively on the traffic that passes through the gateway.
Tier A.

## The Value Comes in Three Steps, Visibility First

1. **Visibility.** Route every model call through the gateway. The gateway then holds a full
   inventory of the models in use and who calls them.
2. **Governance.** Apply policies, rate limits and access controls per model, team or application.
3. **Prompt firewall.** Inspect every prompt and response inline, with the same policies the
   Prompt Firewall applies elsewhere.

The sales line is "before you can govern AI, you need to see it." Tier A.

## Two Routing Options Serve Two Kinds of Buyer

| Option | What it is | When it fits |
| --- | --- | --- |
| LiteLLM | An open-source, interoperable wrapper. It speaks the OpenAI interface and serves models behind vLLM, [confirm, heard as "OpenLLM"] and similar servers | The customer already runs LiteLLM, or wants an open-source path |
| AccuKnox AI Gateway | A proprietary gateway with deeper policy and governance controls | The customer wants one control plane for model access, rate limits and firewall policy |

Tier D today. AccuKnox integrates with the Bifrost and LiteLLM gateways. Source:
`docs/integrations/ai-overview.md`. Kong AI is tier I. The AccuKnox AI Gateway itself has no doc
yet, so it is tier A.

## Air-Gapped Buyers Need the On-Premises Mode

| Mode | Notes |
| --- | --- |
| Cloud-hosted | Multi-cloud across AWS, Azure and GCP |
| On-premises or private cloud | Bifrost and Kong AI Gateway are the comparable on-premises options |
| Air-gapped | A cloud-hosted gateway cannot reach the environment, so the gateway must run on premises |

For a BYOM customer with local models, the gateway is the control plane that makes those local
model deployments governable. Tier A.

## API Gateways and AI Gateways Are Converging

The competitor set is Kong AI Gateway, Bifrost, the NVIDIA AI gateway and
[confirm, heard as "DeepSeek AI Gateway"]. Large enterprises now put the AI gateway beside or inside
their API management layer. An airline's APIM architecture is the reference example the product
team gave. Do not name that customer on a public page. Tier A.

AccuKnox already reads API gateway traffic from Azure APIM, AWS API Gateway and Apigee. Tier D.
Source: `docs/integrations/ai-overview.md`.

## The Gateway Enforces, and Shadow AI Discovery Detects

Shadow AI Discovery finds the AI that nobody approved. The gateway is where the approved traffic
goes and where policy applies to it. The two products work as a pair. The CLI agent surface in
`shadow-ai-discovery.md` already uses a gateway proxy configuration to send coding agent traffic
through the Prompt Firewall. Tier I, from `references/source-of-truth/shadow-ai-coverage.pdf`.

## Four Lines Answer the AE Questions on the AI Gateway

- Lead with "before you can govern AI, you need to see it. The gateway is that visibility layer."
- Name the use cases. Model traffic monitoring, prompt firewall enforcement, rate limiting and
  policy-based model access.
- For an on-premises BYOM buyer, the gateway is the control plane for local models.
- Bridge to Shadow AI. Discovery is the detection layer and the gateway is the enforcement layer.
