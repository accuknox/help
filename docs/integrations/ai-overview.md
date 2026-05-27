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

The **AI Security** module provides prompt firewalling, threat detection, and risk assessment for your AI models and AI application deployments.

## SDK and Platform Integrations

::cards:: cols=4

- title: SDK Integration (Python)
  image: https://media.istockphoto.com/id/1163870054/vector/sdk-icon-software-development-kit-icon.jpg?s=612x612&w=0&k=20&c=-eBNBnt5zg7i3fS_vOV8RganMSJbdDvkmvwtFlg9c2E=
  url: ../use-cases/llm-defense-app-onboard.md
  description: Integrate AccuKnox SDK with your AI applications for prompt scanning and security.

- title: Azure Copilot Studio
  image: https://trulysmb.com/wp-content/uploads/2025/06/copilot-studio-header.png
  url: ../integrations/copilot-studio.md
  description: Integrate with Azure Copilot Studio for AI security

- title: Bedrock-Agentcore
  image: https://www.missioncloud.com/hubfs/AgentCore-icon3-1.png
  url: ../integrations/bedrock-agentcore.md
  description: Integrate Bedrock-Agentcore with AccuKnox for AI asset scanning

- title: Power Apps
  image: https://www.dynamicssquare.com/img/Power-Apps.png
  url: ../integrations/powerapps-integration.md
  description: Secure Microsoft Power Apps with AccuKnox AI Security

::/cards::

## AI Gateway Integrations

::cards:: cols=4

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
  description: Integrate with LiteLLM Prompt Firewall for AI security -->
::/cards::

!!! tip "**Support Matrix and Use Cases**"
    - Refer to the **[AI Security Support Matrix](https://help.accuknox.com/support-matrix/aiml-support-matrix/)** for detailed information on supported platforms, versions, and configurations.
    - Refer to the **[AI Security Use Case](https://help.accuknox.com/use-cases/aiml-usecases/)** to learn how to view your AI inventory, create collections, upload OpenAI specifications, and scan for security findings.