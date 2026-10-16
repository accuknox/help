---
title: Direct SDK and REST API Integration
description: Read a secret from AccuKnox Secrets Manager inside your application code, so the value never lands in a Kubernetes secret or an environment variable.
---

# Direct SDK and REST API Integration

Your application calls AccuKnox Secrets Manager itself, reads the secret when it needs it, and keeps the value in memory. No Kubernetes secret, environment variable or config file holds a copy. This is the most secure way to connect an application, and it takes a few lines of code.

Secrets Manager is API-compatible with HashiCorp Vault, so any Vault client library works. Any language that can make an HTTPS call can use the REST API directly.

## Before You Start

You need three things in Secrets Manager.

| Item | Example used on this page |
| --- | --- |
| A secret | Path `demo/mysql` in the KV version 2 engine mounted at `secret`, key `password` |
| A policy that reads only that path | `demo-access` |
| An auth method the application can use | Kubernetes auth mounted at `k8s-demo-cluster`, with role `demo-access` |

See [Storing Secrets in the KV Engine](kv-secrets.md) to create the secret, and [Sharing Secrets Within an Organisation](sharing-secrets.md) to write a policy.

## The Application Proves Who It Is First

Pick the auth method by where the application runs.

| Where the application runs | Auth method | What the application presents |
| --- | --- | --- |
| A Kubernetes pod | Kubernetes | The pod's service account token |
| A virtual machine, a batch job or a script | AppRole | A role ID and a secret ID |
| A workload that already holds a certificate | TLS certificate | Its client certificate |

The Kubernetes method needs no stored credential, because the cluster gives every pod its own service account token. Prefer it for anything that runs in a pod.

## Read the Secret in Python

This example runs in a pod and uses the `hvac` client.

```python
import os
import hvac

TOKEN_PATH = "/var/run/secrets/kubernetes.io/serviceaccount/token"

client = hvac.Client(url=os.environ["VAULT_ADDR"])

# Log in as the pod's service account
with open(TOKEN_PATH) as f:
    jwt = f.read()
client.auth.kubernetes.login(role="demo-access", jwt=jwt, mount_point="k8s-demo-cluster")

# Read the password into memory
secret = client.secrets.kv.v2.read_secret_version(path="demo/mysql", mount_point="secret")
db_password = secret["data"]["data"]["password"]
```

Set `VAULT_ADDR` to the address of your Secrets Manager. Read the secret when the application starts or when it opens a connection, and never write the value to a log.

## Use the Client for Your Language

These samples log in with AppRole, the usual method off Kubernetes. On Kubernetes, swap the AppRole login for the Kubernetes login shown above.

=== "Java"

    Library: `io.github.jopenlibs:vault-java-driver`

    ```java
    VaultConfig cfg = new VaultConfig()
        .address(addr).engineVersion(2).build();
    String token = Vault.create(cfg).auth()
        .loginByAppRole(roleId, secretId)
        .getAuthClientToken();
    Vault vault = Vault.create(cfg.token(token));
    String pwd = vault.logical()
        .read("secret/demo/mysql")
        .getData().get("password");
    ```

    A Spring Boot application can use Spring Cloud Vault, which fills existing properties through configuration alone.

=== ".NET"

    Library: `VaultSharp`

    ```csharp
    var auth = new AppRoleAuthMethodInfo(roleId, secretId);
    var client = new VaultClient(new VaultClientSettings(addr, auth));
    Secret<SecretData> s = await client.V1.Secrets.KeyValue.V2
        .ReadSecretAsync(path: "demo/mysql", mountPoint: "secret");
    var pwd = s.Data.Data["password"].ToString();
    ```

=== "Node.js"

    Library: `node-vault`

    ```javascript
    const vault = require("node-vault")({ endpoint: process.env.VAULT_ADDR });
    const login = await vault.approleLogin({ role_id: roleId, secret_id: secretId });
    vault.token = login.auth.client_token;
    const { data } = await vault.read("secret/data/demo/mysql");
    const dbPassword = data.data.password;
    ```

=== "REST API"

    Log in, then read the secret with the token from the login response.

    ```bash
    curl -s --request POST \
      --data '{"role_id": "<role-id>", "secret_id": "<secret-id>"}' \
      "$VAULT_ADDR/v1/auth/approle/login"
    ```

    ```bash
    curl -s --header "X-Vault-Token: <client-token>" \
      "$VAULT_ADDR/v1/secret/data/demo/mysql"
    ```

    The password sits at `.data.data.password` in the response.

!!! note "Open-source clients"
    These libraries are open-source Vault clients, not AccuKnox software. [Confirm the client versions tested against Secrets Manager v2.5.4.]

## Deliver the AppRole Credentials Safely

The role ID identifies the application and can ship with it. The secret ID works like a password. Hand it to the application at deploy time through your pipeline, never through source code.

## What This Method Does Not Do

- It does not update a value the application already holds. Read the secret again, or restart, to pick up a new version.
- It needs a code change. When you cannot change the code, use the [External Secrets Operator](external-secrets.md).

AccuKnox professional services can review your application and make the code change.

- - -
[SCHEDULE DEMO](https://www.accuknox.com/contact-us){ .md-button .md-button--primary }
