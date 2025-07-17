# Onboarding for AIML Runtime Security

## Using Postman for AIML Runtime Onboarding

- Open Postman.

- Click "Import" (top-left).

- Select "Raw Text", then paste the following curl:

  ```bash
  curl --location '
  https://app.mod.accuknox.com/modelknox_runtime/application-query' \
  --header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9....' \
  --header 'Content-Type: application/json' \
  --header 'User: <ENTER USER INFO>' \
  --header 'Secret-Token: <ENTER SECRET TOKEN>' \
  --data '<ENTER REQUEST DATA>'
  ```

- Click "Continue", then "Import".

- User Header – `<ENTER USER INFO>`
  Replace with your registered email address in the system. For example:

  ```sh
  User:
  tempuser1@product.com
  ```

- Secret-Token Header – `<ENTER SECRET TOKEN>`

  Replace with your application's secret token (this is unique to you). Example:

  ```sh
  Secret-Token: 12345abcde67890
  ```

- `--data` – `<ENTER REQUEST DATA>`

  This should be a JSON object describing the application you want to query. Example:

  ```json
  {
    "cloud": "aws",
    "account": "accuknox-dev",
    "region": "us-west-1",
    "application": "my-ml-app"
  }
  ```

- Paste this JSON into the

- Body tab → raw → select JSON.

!!! NOTE "Authorization Token"
    Do NOT modify the Authorization: Bearer ... token. It's fixed and required for access.

### Final Checklist Before Sending

To make a cURL POST request, you'll need to set the URL, which should already be filled from your cURL command.

- Choose `POST` as the method.
- For headers, include `Authorization`, `User`, `Secret-Token`
- `Content-Type: application/json`.
- The request body should be in raw JSON format, containing `cloud`, `account`, `region`, and `application_name`. After you've got all these details ready, simply click **"Send"** to transmit your request.

## Using Python for AIML Runtime Onboarding

You can use the requests library in Python. Below is the template you can follow:

```python
import requests

url = "https://app.mod.accuknox.com/modelknox_runtime/application-query"

headers = {
    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9....",  # Bearer token – do not change
    "Content-Type": "application/json",
    "User": "<ENTER USER INFO>",         # Replace with the user's email
    "Secret-Token": "<ENTER SECRET TOKEN>"  # Replace with the user's secret token
}

payload = {
    # Replace with the actual request data template
    # Example:
    # "application_id": "app-123",
    # "query_type": "vulnerability_scan"
}

response = requests.post(url, headers=headers, json=payload)

print("Status Code:", response.status_code)
print("Response Body:", response.json())
```

!!! NOTE "Authorization Token"
    Do not modify the Authorization Bearer token — it is fixed and managed by us.

### User Input Requirements

- Your user email in the "User" header.
- Your application secret token in the "Secret-Token" header.
- A valid request body JSON in the payload section.
