---
title: Red Teaming vLLM Models via AccuKnox Collector method
description: Red team a model served by vLLM with the AccuKnox Custom Model collector, using either the OpenAI-compatible chat API or the completions API.
---

# Red Teaming vLLM Models via AccuKnox Collector method

[vLLM](https://docs.vllm.ai/) serves models behind an OpenAI-compatible HTTP API. The AccuKnox **Custom Model** collector points at your vLLM server and runs the AccuKnox prompt corpus against the loaded model. The flow is the same as any Custom Model onboarding; only the **endpoint URL** and **request template** change, covered in the tabs below for vLLM's chat and completions APIs.

!!! warning "Custom models have no default secret token"
    A vLLM server started without `--api-key` accepts requests without auth, so leave **Secret Token** empty. If you launched vLLM with `--api-key <key>`, put that key in **Secret Token**.

## Prerequisites

* A running **vLLM** server reachable from AccuKnox over HTTP, with the target model loaded.
* The **model id** vLLM serves (the `--model` value), for example `meta-llama/Llama-3-8b-instruct`.
* An AccuKnox tenant with permission to create Collectors.

## Step 1: Start a new LLM Red Teaming collector

1. Go to **Settings > Collectors** and click **Add Collector**.
2. Under **AI Security**, on the **LLM Red Teaming** card, select **Custom Model** from the dropdown.

![AI Security collectors with the LLM Red Teaming card](images/vllm-collector/01-add-collector-ai-security.png)

3. Enter a **Collector Name** and optional **Description**, then click **Next**.

![Basic information for the vLLM collector](images/vllm-collector/02-basic-information.png)

## Step 2: Configure the target

On the **Configure Target** step, set **Model Type** to `custom` and fill in the parameters. Pick the tab that matches how your model is served; `$INPUT` is where AccuKnox injects each prompt.

| Parameter | Description |
|-----------|-------------|
| **Endpoint URL** | The vLLM URL for your API (see tabs below) |
| **Secret Token** | Leave empty unless vLLM was started with `--api-key` |
| **Model Name** | Display name used inside AccuKnox, for example `Llama-3-8b-instruct` |
| **Model ID** | The model id vLLM serves, for example `meta-llama/Llama-3-8b-instruct`. Must match the `model` value in the request template. |
| **Model Type** | `custom` |
| **Request Template** | The chat or completions JSON body (see tabs below), with `$INPUT` as the prompt placeholder |
| **Scan Category** | One or more of **Code**, **SentimentAnalysis**, **Hallucination**, **PromptInjection**, or **All** |
| **Pre-defined Prompts** | **Scan with Default Prompts** uses the built-in corpus; **Upload Custom Prompts File** takes your own JSON list |

=== "Chat API (instruction / chat models)"

    ```text
    http://<vllm-host>:8000/v1/chat/completions
    ```

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

=== "Completions API (base / text models)"

    ```text
    http://<vllm-host>:8000/v1/completions
    ```

    ```json
    {
      "model": "meta-llama/Llama-3-8b-instruct",
      "prompt": "$INPUT",
      "temperature": 0.7,
      "max_tokens": 512
    }
    ```

!!! info "Keep the model id consistent"
    vLLM rejects a request whose `model` field does not match a loaded model. Make **Model ID**, the `model` value in the template, and the `--model` you started vLLM with all identical.

## Step 3: Test the connection

Click **Test Connection**. AccuKnox sends a sample request from your template and a successful response confirms the endpoint, template, and any token before you save.

## Step 4: Schedule and submit

Enter a notification **Email** and set the trigger under **Setup Cron**. Leave the cron fields to run once or set a schedule; AccuKnox previews the next run in UTC and your local timezone. Click **Submit**.

![Schedule and notification for the vLLM collector](images/vllm-collector/04-schedule-cron.png)

## Step 5: Trigger the scan and view findings

The collector appears in the **Collectors** list. For an on-demand collector, open the row menu and click **Trigger Scan**.

![Collectors list with the custom model red teaming collector](images/vllm-collector/05-collectors-list.png)

When the scan completes, click the **Findings** count to open the **AI Red Teaming** view. Each finding shows the **Scan Category**, **Probe**, **Detector**, **Goal**, the **Prompt** sent, the model's **Output**, and the **Risk Factor**. Click any row for the detail pane with compliance mapping (OWASP Top 10 for LLM, AVID), **Ask AI** remediation, and ticketing.

![AI Red Teaming findings table](images/vllm-collector/06-findings-table.png)

!!! tip "Same flow across custom models"
    The collectors list, findings table, and detail pane are identical for every Custom Model target. For a visual of the detail pane, see [NVIDIA Triton Model Red Teaming](aiml-triton-collector.md#step-5-trigger-the-scan-and-view-findings). For the full catalog of probes and categories, see [Categories and Probes](https://help.accuknox.com/use-cases/subprompts-categories/).
