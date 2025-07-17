---
title: AIML Runtime Security Onboarding
description: A guide to onboard AIML Runtime Security using ModelArmor, including API usage and integration examples.
---

# Onboard Custom Applications

## Step 1: Understand the API Purpose

The endpoint `https://app.mod.accuknox.com/modelknox_runtime/application-query` acts as a proxy server that receives and processes user queries. It supports LLM Runtime Defense, which monitors and optionally blocks suspicious queries/responses when interacting with your application.

## Step 2: Prepare Required Fields

- **Authorization:**
  `Bearer <Bearer-Token>`
  (Used to authenticate the request with AccuKnox — do not change this token.)

- **User:**
  `<ENTER USER INFO>`
  (Specify the user identity — e.g., email — to trace who initiated the query.)

- **Secret-Token:**
  `<ENTER SECRET TOKEN>`
  (This is a credential/token tied to your application instance.)

- **Request Payload:**
  (Include relevant parameters in JSON format. Example below.)

## Step 3: Choose Your Integration Method

### Python (with requests library)

```python
import requests

url = "https://app.mod.accuknox.com/modelknox_runtime/application-query"

headers = {
    "Authorization": "Bearer <YOUR_JWT_TOKEN>",
    "Content-Type": "application/json",
    "User": "<ENTER USER INFO>",
    "Secret-Token": "<ENTER SECRET TOKEN>"
}

payload = {
    "asset_id": "abc123",
    "cloud": "aws",
    "region": "us-west-2"
}

response = requests.post(url, headers=headers, json=payload)

print("Status Code:", response.status_code)
print("Response:", response.json())

```

### Terminal (using curl)

```bash
curl -X POST 'https://app.mod.accuknox.com/modelknox_runtime/application-query' \
  -H 'Authorization: Bearer <YOUR_JWT_TOKEN>' \
  -H 'Content-Type: application/json' \
  -H 'User: <ENTER USER INFO>' \
  -H 'Secret-Token: <ENTER SECRET TOKEN>' \
  -d '{
        "asset_id": "abc123",
        "cloud": "aws",
        "region": "us-west-2"
      }'
```

### JavaScript (Node.js / Fetch API / Express)

```javascript
const fetch = require("node-fetch"); // npm install node-fetch if needed

const url = "https://app.mod.accuknox.com/modelknox_runtime/application-query";

const headers = {
  Authorization: "Bearer <YOUR_JWT_TOKEN>",
  "Content-Type": "application/json",
  User: "<ENTER USER INFO>",
  "Secret-Token": "<ENTER SECRET TOKEN>",
};

const payload = {
  asset_id: "abc123",
  cloud: "aws",
  region: "us-west-2",
};

fetch(url, {
  method: "POST",
  headers: headers,
  body: JSON.stringify(payload),
})
  .then((res) => res.json())
  .then((data) => console.log("Response:", data))
  .catch((err) => console.error("Error:", err));
```
