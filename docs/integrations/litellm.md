---
title: LiteLLM Integration
description: Integrate AccuKnox LLM Defense with LiteLLM to scan prompts and responses for security threats and log AI interactions for visibility.
---

# LiteLLM Integration

Follow these instructions to integrate AccuKnox LLM Defense with LiteLLM. This setup will enable scanning of prompts and resp for potential threats and logging interactions to enhance security and visibility for your LLM applications.

1. Install `litellm` python package, `litellm` proxy cli package and `accuknox-llm-defense` package using:

    ```bash
    pip install litellm 'litellm[proxy]' accuknox-llm-defense
    ```

2. Create the following file (`custom_callbacks.py`) in your project directory:

    <div class="gist-embed" data-gist-id="Vishal-42/561e08a7693f4feb38fa01c572cdf93c"></div>

3. Also create the following config file for the litellm proxy server (`config.yaml`):

    ```yaml
    model_list:
      - model_name: gpt-3.5-turbo
        litellm_params:
          model: gpt-3.5-turbo
          api_key: <your open-ai key>

    litellm_settings:
      callbacks: ["custom_callbacks.accuknox_handler"]

    accuknox_settings:
      env_token: <accuknox token you get when onboarding application>
      user_info: <user name/email>
      client_info: <optional client info>
      base_url: <accuknox base url, option for onprem only>
    ```

4. Run the proxy server using:

    ```bash
    litellm --config <path to yaml file>
    ```

    CURL for using openai proxy, other proxies can be found [here](https://docs.litellm.ai/docs/supported_endpoints).

    ```bash
    curl --location 'http://0.0.0.0:4000/chat/completions' \
    --header 'Content-Type: application/json' \
    --data '{
      "model": "gpt-3.5-turbo",
      "messages": [
        {
          "role": "user",
          "content": "today is 4th november"
        }
      ],
      "user": "<your-app-name>",
      "temperature": 0.2
    }'
    ```

### Findings

![LiteLLM findings in AccuKnox security dashboard](image-56.png)

### Chat

![LiteLLM chat interaction monitored by AccuKnox](image-57.png)

This integration secures your LLM interactions by routing them through the LiteLLM proxy with AccuKnox's defense mechanisms. You can now monitor usage, detect vulnerabilities, and ensure compliance in real-time.