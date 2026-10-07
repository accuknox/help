For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/secrets/inject-secrets-example.md).

This article presents a step-by-step guide for testing Prisma Cloud’s secret manager. You will set up HashiCorp Vault, store a secret in it, inject the secret into a running container, then validate that it can be seen from within the container.

## Setting up Vault[Direct link to heading](https://docs.prismacloud.io/admin-guide/secrets/inject-secrets-example\#setting-up-vault)

Set up HashiCorp Vault in development mode.

1. Download Vault from [https://www.vaultproject.io/downloads.html](https://www.vaultproject.io/downloads.html).

2. Unzip the package, then copy the vault executable to a directory in your `PATH`.

3. Verify that vault is installed. Run the following command:

















AskCopy



```
$ vault -help
```

4. Start Vault in development mode.

















AskCopy



```
$ vault server -dev -dev-listen-address='<VAULT_HOST_IPADDR>:8200'

==> WARNING: Dev mode is enabled!

In this mode, Vault is completely in-memory and unsealed.
Vault is configured to only have a single unseal key. The root
token has already been authenticated with the CLI, so you can
immediately begin using the Vault CLI.

The only step you need to take is to set the following
environment variables:

       export VAULT_ADDR='http://10.240.0.53:8200'

The unseal key and root token are reproduced below in case you
want to seal/unseal the Vault or play with authentication.

Unseal Key: Hb0dBfYh3ieHRmf28ohu5xh0DKfmP4aNa8JS5/jNsWQ=
Root Token: 29e3e12b-09b4-af6c-6e87-cbd9fbcb51bd
```


## Storing a secret in HashiCorp Vault[Direct link to heading](https://docs.prismacloud.io/admin-guide/secrets/inject-secrets-example\#storing-a-secret-in-hashicorp-vault)

Store a secret in Vault.

1. Open a shell and ssh to the host running Vault.

2. Set the Vault address in your environment.

















AskCopy



```
$ export VAULT_ADDR='http://<VAULT_HOST_IPADDR>:8200'
```

3. Create a secret.











For Vault 0.10 or later:

















AskCopy



```
vault kv put secret/mySecret1 "pass=1234567"
```









For Vault 0.9.x or older:

















AskCopy



```
$ vault write secret/mySecret1 "pass=1234567"
```

4. Read the secret back to validate it was properly stored.











For Vault 0.10 or later:

















AskCopy



```
$ vault kv get secret/mySecret1
```









For Vault 0.9.x or older:

















AskCopy



```
$ vault read secret/mySecret1
```


## Integrating Prisma Cloud and Vault[Direct link to heading](https://docs.prismacloud.io/admin-guide/secrets/inject-secrets-example\#integrating-prisma-cloud-and-vault)

Follow the steps in [Integrating Prisma Cloud with HashiCorp Vault](https://docs.prismacloud.io/admin-guide/secrets/secrets-stores/hashicorp-vault).

## Creating a rule in Console[Direct link to heading](https://docs.prismacloud.io/admin-guide/secrets/inject-secrets-example\#creating-a-rule-in-console)

Follow the steps in [Injecting secrets into containers](https://docs.prismacloud.io/admin-guide/secrets/inject-secrets).

## Validating the secret is injected[Direct link to heading](https://docs.prismacloud.io/admin-guide/secrets/inject-secrets-example\#validating-the-secret-is-injected)

Start a container and verify that your secret is properly injected.

\+ The same procedure can be followed for injecting secrets in Kubernetes cluster. Make sure Kubernetes uses dockerd and Prisma Cloud runs in local socket mode.

**Prerequisites:** Defender must be running on the machine where you start your container.

1. Start a container:

















AskCopy



```
$ docker run -ti ubuntu /bin/bash
```

2. Validate your secrets have been injected into this container.











If you injected your secrets as environment variables, run:

















AskCopy



```
# printenv
```









If you injected your secrets as files, run:

















AskCopy



```
# ls /run/secrets
# cat /run/secrets/<SECRET_NAME>
```

3. Exit the shell inside the container.

















AskCopy



```
# exit
```

4. If your secrets are injected as environment variables, validate that they are encrypted when you run docker inspect.











Start a container, and run it in the background:

















AskCopy



```
$ docker run -dit ubuntu /bin/bash
<CONTAINER_ID>

$ docker inspect <CONTAINER_ID>
```


[PreviousInject secrets into containers](https://docs.prismacloud.io/admin-guide/secrets/inject-secrets) [NextAlerts](https://docs.prismacloud.io/admin-guide/alerts/alerts)

Last updated 3 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
