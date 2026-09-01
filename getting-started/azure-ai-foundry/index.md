---
title: Azure APIM Automated Deployment with LLM Prompt & Response Firewall
description: AccuKnox documentation to set up LLM Defense for Azure AI Foundry
---

# Azure APIM Automated Deployment with LLM Prompt & Response Firewall

!!! note "Github Repository"
    Find all deployment scripts and configs in the [GitHub repository](https://github.com/accuknox/Azure-APIM-Integration-with-Prompt-Firewall/).

The solution acts as a **secure proxy** in front of Azure AI Foundry / OpenAI-compatible models with **minimal onboarding effort** and **no manual APIM configuration**.

## How It Works

**Security Flow:**

- All user prompts are scanned by AccuKnox LLM Defence via Azure API Management (APIM) before reaching Azure AI Foundry.
- Unsafe prompts or responses are blocked; only approved requests and responses reach the client and Foundry.
- Clients never connect directly to Foundry; only the endpoint and API key need to be updated in client code.
- Secrets are managed securely in APIM.

**Deployment Actions:**

- Deploys API and operation using Bicep.
- Applies APIM policies for prompt and response scanning.
- Extracts and scans user prompts and model responses.
- Forwards only safe requests to Azure AI Foundry and safe responses to clients.

## Runtime Security Flow

![AccuKnox LLM Defence runtime security flow diagram](image-57.png)

## Prerequisites

Before running this project, ensure you have:

| Requirement                              | Details                                                                                                                                                                                                                  |
|-------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Azure Subscription**                    | Active subscription with billing enabled.                                                                                                                                                                                |
| **Azure API Management (APIM) Instance**  | Must already exist.<br>Recommended SKU: Developer (non-production) or Premium (production).<br>Must be reachable from Azure AI Foundry endpoints.                                                                        |
| **Azure AI Foundry Model**                | Model deployed and accessible via an OpenAI-compatible endpoint.<br>Endpoint must support Bearer token authentication.                                                                                                   |
| **AccuKnox LLM Defence Access Token**     | Obtain from onboarding an application on the AccuKnox platform:<br>AI/ML Security → Applications → Prompt Firewall → Add Application.<br>Store as an APIM Named Value (do not store in code).                            |
| **Azure CLI**                             | Version 2.50+ recommended.<br>Must be installed and logged in (`az login`).                                                                                                                                              |

## Configuration (`.env`)

Create a `.env` file in the repository root.
Each variable must be filled by the user. **Do not commit real values to source control.**

### `.env` (Single-Line, Commented)

```env
SUBSCRIPTION_ID=        # Azure subscription ID (example: 69e37648-d32f-46a0-a45e-e983eb816225)
RESOURCE_GROUP=         # Existing resource group name (example: ai-runtime-firewall-test)
LOCATION=               # Azure region, wrap in quotes if needed (example: "East US")

APIM_SERVICE_NAME=      # Existing API Management service name (example: prompt-firewall-apim)

API_ID=                 # Unique API identifier, no spaces (example: foundry-proxy-api)
API_DISPLAY_NAME=       # Display name shown in APIM, use quotes (example: "Foundry Proxy API")
API_PATH=               # Public base path for the API (example: foundry)


OPERATION_ID=           # Unique operation identifier (example: chat-completions)
OPERATION_DISPLAY_NAME= # Operation display name, use quotes (example: "Chat Completions")
OPERATION_METHOD=       # HTTP method for the operation (example: POST)
OPERATION_URL_TEMPLATE= # Operation URL template (example: /models/chat/completions)
```

## Mandatory Policy Changes (User Action Required)

Before running the deployment, you **must update two values** in the following file:

```
policies/policy.xml
```

These values are **environment- and deployment-specific** and **must be updated manually**.

## Change 1: AccuKnox LLM Defence Endpoint

### Lines to Update

- **Line ~45** – Prompt scan (Inbound)
- **Line ~135** – Response scan (Outbound)

> You must update **both occurrences**

### Default Value (As Shipped)

```xml
<set-url>https://cwpp.dev.accuknox.com/llm-defence/application-query</set-url>
```

### Required Change

Replace the URL with your **AccuKnox environment-specific endpoint**:

```text
https://cwpp.<your-environment>.accuknox.com/llm-defence/application-query
```

### Environment Examples

| Environment | URL                                                             |
| ----------- | --------------------------------------------------------------- |
| Development | `https://cwpp.dev.accuknox.com/llm-defence/application-query`   |
| Staging     | `https://cwpp.stage.accuknox.com/llm-defence/application-query` |
| Production  | `https://cwpp.prod.accuknox.com/llm-defence/application-query`  |

## Change 2: Azure AI Foundry Backend URL

### Line to Update

- **Line ~100** – Backend forwarding configuration

### Default Value (As Shipped)

```xml
<set-backend-service base-url="https://ai-prompt-firewall-openai.services.ai.azure.com" />
```

### Required Change

Replace the `base-url` with **your Azure AI Foundry / OpenAI deployment endpoint**:

```xml
<set-backend-service base-url="https://<your-foundry-resource>.services.ai.azure.com" />
```

### Example

```xml
<set-backend-service base-url="https://my-foundry-openai.services.ai.azure.com" />
```

> This URL **must exactly match** the endpoint of your deployed model and must support **Bearer token authentication**.

## Summary of Required Policy Edits

| Change              | File         | Line(s)   | Description                        |
| ------------------- | ------------ | --------- | ---------------------------------- |
| AccuKnox endpoint   | `policy.xml` | ~45, ~135 | Set correct AccuKnox environment   |
| Foundry backend URL | `policy.xml` | ~100      | Set your model deployment endpoint |

## Important Notes

- Line numbers may vary slightly if comments are added or removed
- Always verify both **prompt** and **response** scan URLs
- Deployment will **fail or block traffic** if these values are incorrect

## Secrets Handling (Mandatory)

Secrets **must not** be placed in `.env` or committed to source control.

This deployment requires the following **APIM Named Value**:

| Name                | Purpose                        |
| ------------------- | ------------------------------ |
| `LLM_DEFENCE_TOKEN` | AccuKnox LLM Defence API token |

The AccuKnox token is **requested securely during execution of `deploy.sh`** (input is hidden).
The script automatically creates or updates the required **APIM Named Value** as part of the deployment process.

## Deployment

Make the deployment script executable:

```bash
chmod +x deploy.sh
```

Run the deployment:

```bash
./deploy.sh
```

This will:

- Set the Azure subscription
- Deploy the API and operation via Bicep
- Apply the operation-level policy
- Bind the backend service
- Enable prompt and response scanning

## Policy Behavior Summary

### Inbound Processing

- Extracts and validates `Authorization: Bearer` token
- Extracts `messages[0].content` from request body
- Calls AccuKnox LLM Defence (prompt scan)
- Blocks unsafe prompts (`403 Forbidden`)
- Forwards safe requests to Azure AI Foundry

### Outbound Processing

- Extracts model response content
- Calls AccuKnox LLM Defence (response scan)
- Blocks unsafe responses before returning to client
