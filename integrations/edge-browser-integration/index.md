---
title: Prompt Firewall Gen AI Browser Integration (Edge)
description: A step-by-step guide to configuring the AccuKnox Prompt Firewall browser plugin for Microsoft Edge and real-time prompt and response filtering in ChatGPT, Claude, GitHub Copilot, and Gemini.
---

# Gen AI Browser Integration for Prompt Security (Edge)

The AccuKnox Prompt Firewall browser plugin intercepts prompts and responses directly in ChatGPT, Claude, GitHub Copilot, and Gemini before they leave your browser session. This includes blocking prompt injection attacks, where a malicious input tries to override the model's behavior. Blocked prompts show a red banner. Allowed ones pass through silently.

![Red banner - Prompt blocked](prompt-block-1.png)

The same plugin covers all four apps at once, no separate install needed per app. This guide covers installation for **Microsoft Edge**. For Chrome, see the [Chrome integration guide](chrome-browser-integration.md). For Firefox, see the [Firefox integration guide](firefox-browser-integration.md).

## Prerequisites

- An active AccuKnox account with AI Security enabled
- Access to the Integrations section (to generate a token)
- Microsoft Edge browser

## Step 1: Create a new integration

![New Integration modal](image-61.png)

Go to **AI Security > Integrations** and click **New Integration**.

Fill in the following fields:

| Field | Value |
|---|---|
| Integration Name | Any descriptive name (e.g. `edge-browser-prod`) |
| Tags | Add relevant tags (e.g. `llmguard`) |

Click **Add** to save.

## Step 2: Copy your token

![Token Created Successfully modal](image-62.png)

After saving, the token is displayed once in a confirmation modal.

!!! warning "Save your token now"
    This token will not be shown again after you close the modal. Copy it immediately and store it in a secure location such as a password manager.

## Step 3: Download and install the browser plugin

[Download the plugin](https://drive.google.com/file/d/1Sn4LoZDT-q8vyF9vMsNkL7WvQpb9GHg7/view?usp=sharing), download the ZIP file from Google Drive, and extract it to a folder on your machine.

To install in Edge:

1. Go to `edge://extensions`
2. Enable **Developer mode** (toggle in the left sidebar)
3. Click **Load unpacked** and select the extracted plugin folder

## Step 4: Configure the extension

![AccuKnox Prompt Firewall Settings panel](image-69.png){ align=right width="400" }

Click the AccuKnox icon in your browser toolbar and open **Settings**.

Fill in the following field:

| Field | Value |
|---|---|
| API Key | Paste the token from Step 2 |

Click **Save Settings**, then **Test Connection**.

## Step 5: Verify the connection

![Extension popup showing connected status and scan counts](image-66.png){ align=right width="360" }

Once connected, the extension popup shows a green status dot next to **AccuKnox Prompt Firewall** along with a running count of scanned, allowed, blocked, and warned prompts. Click **View Logs** to see the full request log.

Open ChatGPT, Claude, GitHub Copilot, or Gemini and send a test prompt. Depending on your active policy, you will see one of the following:

![Red banner - Prompt blocked](image-63.png)
![Green banner - Prompt cleared](image-64.png)

## Request log

All intercepted prompts and responses are visible under **AI Security > Request Log**.

Each entry shows:

- Timestamp
- Direction (PROMPT or RESPONSE)
- Verdict (ALLOW or BLOCK)
- Content preview
- Latency

You can filter by verdict or direction, search by content or reason, and export the full log as JSON.

![Request Log table](image-65.png)
