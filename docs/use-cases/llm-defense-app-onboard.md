---
title: Onboard LLM Defense App
description: Learn how to onboard your application with AccuKnox LLM Defense using the Python SDK. This guide covers steps from application registration to scanning prompts and responses for sensitive information.
---

## Steps to Get Started

### 1. Add Application

Click on **"Add Application"** as shown below.

![image-20250114-184710.png](./images/llm-defense-app-onboard/1.png)
Click the "Add Application" button.


Enter the **Application Name** and **Tags**, then click the **Add** button.

![image-20250114-184710.png](./images/llm-defense-app-onboard/2.png)
Enter the application details.

### 2. Save Your Token

Copy the **Accuknox_token** and store it securely for later use.

![image-20250114-184710.png](./images/llm-defense-app-onboard/3.png)
Copy the API token shown on the screen.

### 3. Install the SDK

Inside the environment where your application is running, install the package:

```bash
pip install accuknox-llm-defense
```

For more details, see the [PyPI project page](https://pypi.org/project/accuknox-llm-defense/).

### 4. Initialize the Client

Import the package and initialize the client with the token you obtained earlier:

```python
from accuknox_llm_defense import LLMDefenseClient

accuknox_client = LLMDefenseClient(
    llm_defense_api_key="<Accuknox_token>",
    user_info="<Enter your email/name>"
)
```

**Parameters:**

  * `llm_defense_api_key`: Your Accuknox token
  * `user_info`: User information (e.g., email)

### 5. Prompt Scanning

Scan a prompt before sending it to your LLM:

```python
prompt = "<Pass the prompt to be sent to LLM>"
sanitized_prompt = accuknox_client.scan_prompt(content=prompt)
```

**Parameters:**

  * `content`: The prompt to be scanned before sending to the LLM.

### 6. Response Scanning

Scan the response received from your LLM:

```python
response = "<Response received from LLM>"
accuknox_client.scan_response(
    content=response,
    prompt=sanitized_prompt.get("sanitized_content"),
    session_id=sanitized_prompt.get("session_id")
)
```

**Parameters:**

  * `content`: The response obtained from the LLM.
  * `prompt`: The sanitized prompt used to generate the response.
  * `session_id`: The session ID obtained during prompt scanning.

!!! note "Important"
    The `session_id` is used to link a prompt and its corresponding response. If you don't provide it, prompts and responses will be treated as separate findings.