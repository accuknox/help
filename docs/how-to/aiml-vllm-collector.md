---
title: vLLM Model Red Teaming using AccuKnox Collector method
description: Red team a model served by vLLM with the AccuKnox Custom Model collector, using either the OpenAI-compatible chat API or the completions API.
---

# vLLM Model Red Teaming using AccuKnox Collector method

[vLLM](https://docs.vllm.ai/) serves models behind an OpenAI-compatible HTTP API. The AccuKnox **Custom Model** collector red teams any model exposed over HTTP, so you point it at your vLLM server and run the AccuKnox prompt corpus against the loaded model.

The flow is the same as any Custom Model onboarding. Only the **endpoint URL** and **request template** change for vLLM. This guide covers both shapes vLLM exposes: the OpenAI-compatible **chat** API and the plain **completions** API.

!!! warning "Custom models need a token only if your endpoint requires one"
    Custom-model targets such as vLLM, NVIDIA Triton, or Ollama have **no default secret token** configured. A vLLM server started without `--api-key` accepts requests without auth, so leave **Secret Token** empty. If you launched vLLM with `--api-key <key>`, put that key in **Secret Token**.

## Prerequisites

* A running **vLLM** server reachable from AccuKnox over HTTP, with the target model loaded.
* The **model id** that vLLM serves, for example `meta-llama/Llama-3-8b-instruct`. This is the value passed to `--model` when you started vLLM.
* Access to the AccuKnox tenant with permission to create Collectors.

## Step 1: Start a new LLM Red Teaming collector

1. Go to **Settings** > **Collectors** in the AccuKnox console and click **Add Collector**.
2. Under **AI Security**, find the **LLM Red Teaming** card, open its dropdown, and select **Custom Model**.

![AI Security collectors with the LLM Red Teaming card](images/vllm-collector/01-add-collector-ai-security.png)

3. On the **Basic Information** step, enter a **Collector Name** and an optional **Description**, then click **Next**.

![Basic information for the vLLM collector](images/vllm-collector/02-basic-information.png)

## Step 2: Pick the endpoint and request template

vLLM exposes two compatible APIs. Use the one that matches how your model is served.

### Method 1: OpenAI-compatible chat API

Use this for instruction or chat models. The endpoint is `/v1/chat/completions`:

```text
http://<vllm-host>:8000/v1/chat/completions
```

Request template (replace the `model` value with your loaded model):

```json
{
  "model": "meta-llama/Llama-3-8b-instruct",
  "messages": [
    { "role": "user", "content": "$INPUT" }
  ],
  "temperature": 0.7,
  "max_tokens": 512
}
```

### Method 2: Completions API

Use this for base or text-completion models. The endpoint is `/v1/completions`:

```text
http://<vllm-host>:8000/v1/completions
```

Request template:

```json
{
  "model": "meta-llama/Llama-3-8b-instruct",
  "prompt": "$INPUT",
  "temperature": 0.7,
  "max_tokens": 512
}
```

In both templates, `$INPUT` is where AccuKnox injects each red teaming prompt.

## Step 3: Configure the target

Fill in the parameters on the **Configure Target** step.

| Parameter | Description |
|-----------|-------------|
| **Endpoint URL** | The vLLM URL from Step 2, for example `http://<vllm-host>:8000/v1/chat/completions` |
| **Secret Token** | Leave empty unless vLLM was started with `--api-key`. If so, use that key. |
| **Model Name** | A display name used inside AccuKnox, for example `Llama-3-8b-instruct` |
| **Model ID** | The model id vLLM serves, for example `meta-llama/Llama-3-8b-instruct`. This must match the `model` value in the request template. |
| **Model Type** | Set to `custom` |
| **Request Template** | The chat or completions JSON body from Step 2, with `$INPUT` as the prompt placeholder |
| **Scan Category** | One or more of **Code**, **SentimentAnalysis**, **Hallucination**, **PromptInjection**, or **All** |
| **Pre-defined Prompts** | **Scan with Default Prompts** uses the built-in AccuKnox corpus. **Upload Custom Prompts File** lets you supply your own JSON list. |

!!! info "Keep the model id consistent"
    vLLM rejects a request whose `model` field does not match a loaded model. Make sure **Model ID** and the `model` value inside the request template are identical, and that both match the `--model` you started vLLM with.

## Step 4: Test the connection

Click **Test Connection**. AccuKnox sends a sample request built from your template to the vLLM endpoint. A successful response confirms the endpoint, request template, and any token are correct before you save.

## Step 5: Schedule and submit

Enter a notification **Email**, then set up the scan trigger under **Setup Cron**. Leave the cron fields to run once, or set a schedule. AccuKnox previews the next run time in both UTC and your local timezone. Click **Submit** to create the collector.

## Step 6: Trigger the scan and view findings

The collector appears in the **Collectors** list with its type, tags, deployment status, and findings count. For an on-demand collector, open the row menu and click **Trigger Scan**.

Once the scan completes, click the **Findings** count to open the **AI Red Teaming** findings view. Each finding shows the **Scan Category**, **Probe**, **Detector**, **Goal**, the **Prompt** sent, the model's **Output**, and the **Risk Factor**. Click any row for the full detail pane with compliance mapping (OWASP Top 10 for LLM, AVID), **Ask AI** remediation, and ticketing.

!!! tip "Same findings view across custom models"
    The collectors list, findings table, and detail pane are identical for every Custom Model target. For a step-by-step visual of these screens, see [NVIDIA Triton Model Red Teaming](aiml-triton-collector.md#view-the-findings).

!!! tip "Probes and subprompts"
    For the full catalog of probes and categories used during scanning, see [Categories and Probes](https://help.accuknox.com/use-cases/subprompts-categories/).
