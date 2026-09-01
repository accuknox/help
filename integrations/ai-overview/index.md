---
title: AI Security Integrations
description: Overview of AI Security capabilities and supported integrations.
hide:
  - toc
---

<style>
h2 {
  color: #000025;
  font-size: 1.5rem !important;
}
.nt-card .nt-card-image{
  color: #005BFF;

}

 .nt-card-title {
    text-align: -webkit-center;
}
</style>

# AI Security Integrations

<div class="ak-dia" role="img" aria-label="Four deployment shapes mapped to four prompt firewall integration modes. A SaaS chat app in a browser uses the browser plugin. A developer CLI tool uses a gateway proxy. A local AI agent uses the SDK or a gateway. A cloud AI agent uses the cloud SDK or an API gateway.">
<svg viewBox="0 0 940 330" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="m1" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="7" markerHeight="7" orient="auto">
      <path class="head" d="M0 0 L8 4 L0 8 z"/>
    </marker>
  </defs>

  <text class="t-s" x="16" y="22">Where the prompt starts</text>
  <text class="t-s" x="306" y="22">Integration mode</text>
  <text class="t-s" x="596" y="22">What you set up</text>

  <rect class="p" x="16" y="30" width="250" height="62" rx="8"/>
  <text class="t-h" x="32" y="54">SaaS chat app in a browser</text>
  <text class="t-s" x="32" y="72">ChatGPT, Claude, Gemini, Copilot</text>
  <path class="ln" d="M266 61 H300" marker-end="url(#m1)"/>
  <rect class="acc" x="306" y="30" width="250" height="62" rx="8"/>
  <text class="t-acc t-h" x="322" y="66">Browser plugin</text>
  <path class="ln" d="M556 61 H590" marker-end="url(#m1)"/>
  <rect class="p" x="596" y="30" width="328" height="62" rx="8"/>
  <text class="t-b" x="612" y="66">Extension for Chrome, Edge or Firefox</text>

  <rect class="p" x="16" y="102" width="250" height="62" rx="8"/>
  <text class="t-h" x="32" y="126">Developer CLI tool</text>
  <text class="t-s" x="32" y="144">Coding agents run from a terminal</text>
  <path class="ln" d="M266 133 H300" marker-end="url(#m1)"/>
  <rect class="acc" x="306" y="102" width="250" height="62" rx="8"/>
  <text class="t-acc t-h" x="322" y="138">Gateway proxy</text>
  <path class="ln" d="M556 133 H590" marker-end="url(#m1)"/>
  <rect class="p" x="596" y="102" width="328" height="62" rx="8"/>
  <text class="t-b" x="612" y="138">Proxy configuration on the tool</text>

  <rect class="p" x="16" y="174" width="250" height="62" rx="8"/>
  <text class="t-h" x="32" y="198">Local AI agent</text>
  <text class="t-s" x="32" y="216">LangGraph, n8n, your own service</text>
  <path class="ln" d="M266 205 H300" marker-end="url(#m1)"/>
  <rect class="acc" x="306" y="174" width="250" height="62" rx="8"/>
  <text class="t-acc t-h" x="322" y="204">SDK, or gateway mode</text>
  <text class="t-s" x="322" y="222">Pick one, not both</text>
  <path class="ln" d="M556 205 H590" marker-end="url(#m1)"/>
  <rect class="p" x="596" y="174" width="328" height="62" rx="8"/>
  <text class="t-b" x="612" y="198">Python SDK in the app,</text>
  <text class="t-b" x="612" y="220">or LiteLLM or Bifrost in front of it</text>

  <rect class="p" x="16" y="246" width="250" height="62" rx="8"/>
  <text class="t-h" x="32" y="270">Cloud AI agent</text>
  <text class="t-s" x="32" y="288">Bedrock AgentCore, Copilot Studio</text>
  <path class="ln" d="M266 277 H300" marker-end="url(#m1)"/>
  <rect class="acc" x="306" y="246" width="250" height="62" rx="8"/>
  <text class="t-acc t-h" x="322" y="282">Cloud SDK, or API gateway</text>
  <path class="ln" d="M556 277 H590" marker-end="url(#m1)"/>
  <rect class="p" x="596" y="246" width="328" height="62" rx="8"/>
  <text class="t-b" x="612" y="270">Azure APIM, AWS API Gateway,</text>
  <text class="t-b" x="612" y="292">Apigee, or the platform integration</text>
</svg>
</div>

!!! danger "Two limits before you choose"
    - **The browser plugin sees only browser traffic.** A prompt sent to the same model from a desktop client or a terminal is invisible to it.
    - **The SDK sees only the app you instrument.** It covers that one app completely and tells you nothing about the next one.

## AI Guardrails (Prompt Firewall)

::cards:: cols=4

- title: SDK Integration (Python)
  image: https://media.istockphoto.com/id/1163870054/vector/sdk-icon-software-development-kit-icon.jpg?s=612x612&w=0&k=20&c=-eBNBnt5zg7i3fS_vOV8RganMSJbdDvkmvwtFlg9c2E=
  url: ../how-to/llm-defense-app-onboard.md
  description: Integrate AccuKnox SDK with your AI applications for prompt scanning and security.

- title: Power Apps
  image: https://www.dynamicssquare.com/img/Power-Apps.png
  url: ../integrations/powerapps-integration.md
  description: Secure Microsoft Power Apps with AccuKnox AI Security

- title: Bifrost AI
  image: ./image-15.png
  url: ../integrations/bifrost-integration.md
  description: Monitor and secure AIs running on AWS AI Gateway

- title: Azure APIM
  image: https://learn.microsoft.com/en-us/media/logos/logo_azure.svg
  url: ../getting-started/azure-ai-foundry.md
  description: Integrate with Azure API Management for AI security

- title: AWS API Gateway
  image: https://raw.githubusercontent.com/pulumi/pulumi-aws-apigateway/main/assets/logo.png
  url: ../how-to/aws-apim.md
  description: Integrate with AWS API Gateway as a secure proxy in front of Bedrock and other LLM backends

- title: Apigee
  image: https://cdn.worldvectorlogo.com/logos/apigee.svg
  url: ../integrations/apigee-integration.md
  description: Configure an Apigee proxy as an LLM security gateway with prompt validation and resilient error handling

- title: LiteLLM
  image: ./image-16.png
  url: ../integrations/litellm.md
  description: Integrate with LiteLLM Prompt Firewall for AI security

::/cards::

!!! tip "Browser-based Guardrails"
    For prompt protection directly in the browser, see the GenAI Browser Plugins for [Chrome](../integrations/chrome-browser-integration.md), [Edge](../integrations/edge-browser-integration.md), and [Firefox](../integrations/firefox-browser-integration.md).

## Agentic AI Security

::cards:: cols=4

- title: Azure Copilot Studio
  image: https://trulysmb.com/wp-content/uploads/2025/06/copilot-studio-header.png
  url: ../integrations/copilot-studio.md
  description: Integrate with Azure Copilot Studio for AI security

- title: Bedrock-Agentcore
  image: https://www.missioncloud.com/hubfs/AgentCore-icon3-1.png
  url: ../integrations/bedrock-agentcore.md
  description: Integrate Bedrock-Agentcore with AccuKnox for AI asset scanning

::/cards::

!!! tip "**Support Matrix and Use Cases**"
    - Refer to the **[AI Security Support Matrix](https://help.accuknox.com/support-matrix/aiml-support-matrix/)** for detailed information on supported platforms, versions, and configurations.
    - Refer to the **[AI Security Use Case](https://help.accuknox.com/use-cases/aiml-usecases/)** to learn how to view your AI inventory, create collections, upload OpenAI specifications, and scan for security findings.