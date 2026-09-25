---
title: Red Teaming Amazon Bedrock Models via AccuKnox Collector method
description: Red team a specific Amazon Bedrock model with the AccuKnox Custom Model collector, without onboarding the full AWS account or organization.
---

# Red Teaming Amazon Bedrock Models via AccuKnox Collector method

AccuKnox supports cloud-based onboarding to scan and red team every model deployed across an AWS Bedrock account. The Collector method is a lighter alternative for targeting a specific model on Bedrock without onboarding the entire cloud account or organization.

## Why use the Collector method

* **Targeted scope:** Red team a single Bedrock model instead of every model in the account.
* **No account onboarding needed:** Works directly against the model's inference endpoint using a Bedrock API key.
* **Fast setup:** A single Custom Model collector covers the connection, prompts, and schedule.
* **Flexible:** The same flow works for any LLM exposed over an HTTP endpoint, not just Bedrock.

!!! tip "Prefer full-account coverage?"
    To scan every Bedrock model in an account automatically, use the [AWS AI/ML Onboard](aiml-aws-onboard.md) flow instead.

## Prerequisites

* An AWS account with access to **Amazon Bedrock** and the model you want to red team.
* Permission to generate a **Bedrock API key** (short-term or long-term) in the target region.
* Access to the AccuKnox tenant with permission to create Collectors.

## Step 1: Start a new LLM Red Teaming collector

1. Go to **Settings** > **Collectors** in the AccuKnox console.
2. On the **LLM Red Teaming** card, open the dropdown and select **Custom Model**.

![Select Custom Model under LLM Red Teaming](images/bedrock-collector/01-collectors-custom-model.png)

3. Enter a **Collector Name** and **Description**, then click **Next**.

![Basic information for the Bedrock collector](images/bedrock-collector/02-basic-information.png)

## Step 2: Gather the Bedrock model details

The Configure Target step requires four values from the AWS console: **Model Name**, **Model ID**, **Endpoint URL**, and **Secret Token**.

### Find the Model ID and inference region

1. In the AWS console, open **Amazon Bedrock** > **Model catalog**.
2. Select the model you want to red team (for example, **Claude Haiku 4.5**).

![Browse the Bedrock model catalog](images/bedrock-collector/03-model-catalog.png)

3. On the model card, copy the **Model ID**. Also note the inference region, as it is part of the endpoint URL.

![Model details with the Model ID](images/bedrock-collector/04-model-details.png)

### Generate a Bedrock API key

![Setup paths for making API calls to Amazon Bedrock](images/bedrock-collector/aws-bedrock-steps.png)

Bedrock supports two key types. A short-term key expires after 12 hours (tied to your console session). A long-term key has a custom expiry and is recommended for repeated or scheduled scans.

1. In the Bedrock console, open **API keys**.

![Bedrock API keys page](images/bedrock-collector/05-api-keys.png)

2. Click **Generate long-term API keys**, set an **API key expiration**, and click **Generate**. Copy the key; this is your **Secret Token**.

![Generate a long-term Bedrock API key](images/bedrock-collector/06-long-term-key.png)

### Build the Endpoint URL

Use this template, replacing `<region>` and `<model-id>` with your values:

```text
https://bedrock-runtime.<region>.amazonaws.com/model/<model-id>/invoke
```

Example for Claude Haiku 4.5 in `us-east-1`:

```text
https://bedrock-runtime.us-east-1.amazonaws.com/model/anthropic.claude-haiku-4-5-20251001-v1:0/invoke
```

See the [AWS guide on using Bedrock API keys](https://docs.aws.amazon.com/bedrock/latest/userguide/api-keys-use.html) for additional invocation options.

## Step 3: Configure the target

Fill in the parameters on the **Configure Target** step.

![Configure Target for the Bedrock model](images/bedrock-collector/07-configure-target.png)

| Parameter | Description |
|-----------|-------------|
| **Endpoint URL** | The Bedrock runtime URL built above, for example `https://bedrock-runtime.us-east-1.amazonaws.com/model/anthropic.claude-haiku-4-5-20251001-v1:0/invoke` |
| **Secret Token** | The Bedrock API key generated above |
| **Model Name** | A display name used inside AccuKnox, for example `Claude Haiku 4.5` |
| **Model ID** | The Bedrock Model ID, for example `anthropic.claude-haiku-4-5-20251001-v1:0` |
| **Model Type** | Set to `custom` |
| **Request Template** | JSON payload sent to the model. Place `$INPUT` where the red teaming prompt should be injected. |
| **Scan Category** | One or more of **Code**, **SentimentAnalysis**, **Hallucination**, **PromptInjection**, or **All** |
| **Pre-defined Prompts** | **Default Prompts** uses the built-in AccuKnox corpus. **Custom Prompts** lets you upload your own JSON list. |

### Request template for Anthropic models on Bedrock

Anthropic models on Bedrock require an `anthropic_version` field in the request body. Use this template:

```json
{
  "anthropic_version": "bedrock-2023-05-31",
  "max_tokens": 1024,
  "messages": [
    {
      "role": "user",
      "content": [
        { "type": "text", "text": "$INPUT" }
      ]
    }
  ]
}
```

!!! info "Other providers"
    Bedrock hosts models from Anthropic, Meta, Amazon Titan, Mistral, and others. Each provider expects a different request shape. Copy the **Code example** from the model card for your specific model and replace the prompt value with `$INPUT`.

### Pick scan categories

Select the categories to exercise against the model. You can pick more than one.

![Choose one or more scan categories](images/bedrock-collector/08-scan-category.png)

## Step 4: Test the connection

Click **Test Connection**. A successful response confirms the endpoint, key, and request template are correct before saving.

![Test Connection succeeded for the Bedrock model](images/bedrock-collector/09-test-connection.png)

## Step 5: Schedule and submit

Add **Labels** and **Tags** to organize the collector. Then pick a trigger type:

* **On-Demand:** Trigger the scan manually from the Collectors list.
* **Scheduled:** Set a cron expression. AccuKnox previews the next run time in both UTC and your local timezone.

Enter the notification email and click **Submit**.

![Configure schedule and notification](images/bedrock-collector/10-schedule-cron.png)

## Step 6: Trigger the scan

The collector appears in the **Collectors** list with its trigger type, deployment status, and findings count. For an **On-Demand** collector, open the row menu and click **Trigger Scan**.

![Trigger an on-demand scan](images/bedrock-collector/11-trigger-scan.png)

A confirmation appears once the scan starts.

![Scan triggered successfully](images/bedrock-collector/12-scan-triggered.png)

## View the findings

Once the scan completes, click the **Findings** count on the collector row to open the **AI Red Teaming** findings view.

![Bedrock red teaming findings](images/bedrock-collector/13-findings.png)

Each finding shows:

* **Scan Category** and **Probe** that produced the result.
* **Detector** and **Goal** the probe was checking.
* **Prompt** sent to the model and the model's **Output**.
* **Risk Factor**, **Detector Safety Score**, and **Category Safety Score**.

Click any row to open the detail pane with the full prompt, model response, AVID mapping, and recommended remediation. You can also use **Ask AI** for assisted remediation or raise a ticket directly from the pane to track the fix in your ticketing system.

!!! tip "Probes and subprompts"
    For the full catalog of probes and categories used during scanning, see [Categories and Probes](https://help.accuknox.com/use-cases/subprompts-categories/).
