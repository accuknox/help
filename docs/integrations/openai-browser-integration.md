---
title: Prompt Firewall OpenAI Browser Integration
description: A step-by-step guide to configuring the AccuKnox Prompt Firewall browser plugin for real-time prompt and response filtering in ChatGPT.
---

# OpenAI Browser Integration for Prompt Security

The AccuKnox Prompt Firewall browser plugin intercepts prompts and responses directly in ChatGPT before they leave your browser session. Blocked prompts show a red banner. Allowed ones pass through silently.

## Prerequisites

- An active AccuKnox account with AI Security enabled
- Access to the Integrations section (to generate a token)
- A Chromium-based browser (Chrome, Brave, or Edge)

## Step 1: Create a new integration

![New Integration modal](image-61.png)

Go to **AI Security > Integrations** and click **New Integration**.

Fill in the following fields:

| Field | Value |
|---|---|
| Integration Name | Any descriptive name (e.g. `openai-browser-prod`) |
| Tags | Add relevant tags (e.g. `llmguard`) |

Click **Add** to save.

## Step 2: Copy your token

![Token Created Successfully modal](image-62.png)

After saving, the token is displayed once in a confirmation modal.

!!! warning "Save your token now"
    This token will not be shown again after you close the modal. Copy it immediately and store it in a secure location such as a password manager.

## Step 3: Download and install the browser plugin

[Download Chrome plugin](https://promptfirewall-plugin-extension.s3.ap-south-1.amazonaws.com/Prompt-firewall-plugin-v2.zip) and extract the ZIP file to a folder on your machine.

To install in Chrome:

1. Go to `chrome://extensions`
2. Enable **Developer mode** (top-right toggle)
3. Click **Load unpacked** and select the extracted plugin folder

## Step 4: Configure the extension

![AccuKnox Prompt Firewall Settings panel](image-69.png){ align=right width="400" }

Click the AccuKnox icon in your browser toolbar and open **Settings**.

Fill in the two fields:

| Field | Value |
|---|---|
| API Key | Paste the token from Step 2 |

Click **Save Settings**, then **Test Connection**.

## Step 5: Verify the connection

![Extension popup showing connected status and scan counts](image-66.png){ align=right width="360" }

Once connected, the extension popup shows a green status dot next to **AccuKnox Prompt Firewall** along with a running count of scanned, allowed, blocked, and warned prompts. Click **View Logs** to see the full request log.

Open ChatGPT and send a test prompt. Depending on your active policy, you will see one of the following:


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