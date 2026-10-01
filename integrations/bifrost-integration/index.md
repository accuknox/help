---
title: Bifrost Integration Guide
description: Guide to integrate AccuKnox Prompt Firewall with Bifrost using a custom plugin.
---

# Bifrost Integration Guide
Learn how to integrate AccuKnox Prompt Firewall with Bifrost using a custom plugin to monitor and filter prompts and responses via the AccuKnox API.

!!! note "Important"
    Since this integration hooks into API calls, it currently **only logs and categorizes** prompts and responses (e.g., Prompt Injection, Toxic, Code) for observability. It does not actively block requests at this stage.

<p align="center">
  <img src="https://i.ibb.co/NnW7Nwsz/Screenshot-2025-11-28-123545.png" alt="alt text" />
</p>

## Step 1: Prerequisites

We expect you to have the `bifrost-http` binary in-place. You can download it from the [Bifrost Releases](https://github.com/maximhq/bifrost/releases).

This integration guide uses the `bifrost-http` binary to test the configuration. You can use this config with any Bifrost deployment method.


## Step 2: Download AccuKnox Plugin

Download the latest AccuKnox plugin for Bifrost:

### Using wget

```bash
wget https://github.com/accuknox/bifrost-accuknox-integration/releases/latest/download/accuknox-plugin.so
```

### Using curl

```bash
curl -LO https://github.com/accuknox/bifrost-accuknox-integration/releases/latest/download/accuknox-plugin.so
```

!!! tip "Source Code"
    The plugin source code is available at [github.com/accuknox/bifrost-accuknox-integration](https://github.com/accuknox/bifrost-accuknox-integration) for reference.


## Step 3: Configure Bifrost

Create or update your Bifrost configuration file with the following settings:

```json
{
    "log_level": "debug",
    "server": {
      "port": 8080,
      "host": "0.0.0.0"
    },
    "plugins": [
      {
        "enabled": true,
        "name": "accuknox-logger",
        "path": "./accuknox-plugin.so",
        "config": {
          "enabled": true,
          "api_key": "<YOUR_ACCUKNOX_JWT_TOKEN>",
          "user_info": "<username@accuknox.com>"
        }
      }
    ],
    "providers": {
      "openai": {
        "keys": [
          {
            "value": "<YOUR_OPENAI_API_KEY>",
            "models": ["gpt-3.5-turbo"],
            "weight": 1.0
          }
        ]
      }
    }
}
```

## Step 4: Configuration Details

### Plugin Configuration

- **`enabled`**: Set to `true` to activate the plugin
- **`name`**: Plugin identifier (must match the name returned by `GetName()`)
- **`path`**: Path to the compiled `.so` file
- **`api_key`**: Your AccuKnox Prompt Firewall JWT token (obtained from AccuKnox dashboard)
- **`user_info`**: Your email or username for tracking

<!-- ### AccuKnox API Endpoint

The plugin automatically determines the AccuKnox API endpoint by decoding the JWT token's `iss` field:

- **dev**: `https://cwpp.dev.accuknox.com/llm-defence/application-query`
- **stage**: `https://cwpp.stage.accuknox.com/llm-defence/application-query`
- **demo**: `https://cwpp.demo.accuknox.com/llm-defence/application-query`
- **prod**: `https://cwpp.prod.accuknox.com/llm-defence/application-query` -->

### Provider Configuration

- Add your LLM provider credentials (OpenAI, Anthropic, etc.)
- Each key can be restricted to specific models
- Use `weight` for load balancing across multiple keys

## Step 5: Run Bifrost Server

### Copy the Plugin

```bash
cp accuknox-plugin.so /path/to/bifrost/
cd /path/to/bifrost/
```

### Start the Server

```bash
./bifrost-http -app-dir . -log-level debug -log-style pretty
```

## Step 6: Test the Integration

Send a test request using curl:

```bash
curl -X POST http://localhost:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "openai/gpt-3.5-turbo",
    "messages": [{"role": "user", "content": "Say hello"}],
    "max_tokens": 50
  }'
```
