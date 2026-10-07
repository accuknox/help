For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/compliance/detect-secrets.md).

Prisma Cloud can detect sensitive information that is improperly secured inside images and containers. Scans can detect embedded passwords, login tokens, and other types of secrets. To detect improperly secured secrets, add the following checks to your [compliance policy](https://docs.prismacloud.io/admin-guide/compliance/manage-compliance).

## Defender Secrets Detection[Direct link to heading](https://docs.prismacloud.io/admin-guide/compliance/detect-secrets\#defender-secrets-detection)

Your deployed defenders detect sensitive information inside images and containers. Select **Monitor > Compliance > Compliance Explorer** and search the results using the following compliance check IDs.

### Compliance Check ID 424[Direct link to heading](https://docs.prismacloud.io/admin-guide/compliance/detect-secrets\#compliance-check-id-424)

This check detects sensitive information provided in environment variables of image. The data so provided can be easily exposed by running `docker inspect` on the image and thus compromising privacy.

**Example**

AskCopy

```
$ docker --tlsverify -H :9998 build -t secret:v1 .
```

**Response**

AskCopy

```
Sending build context to Docker daemon 2.048 kB
Step 1/2 : FROM alpine:latest
 ---> 88e169ea8f46
Step 2/2 : ENV PASSWORD = secret
 ---> Using cache
 ---> 8f3627bc339b
Error: [Prisma Cloud] Image operation blocked by policy: (No secrets attached), violates: The environment variable PASSWORD contains sensitive data
```

### Compliance Check ID 425[Direct link to heading](https://docs.prismacloud.io/admin-guide/compliance/detect-secrets\#compliance-check-id-425)

This check detects private keys stored in an image.

**Example**

Navigate to **Defend > Compliance**. Add a new compliance rule to block running an image with private key in it.

**Test**

AskCopy

```
$ docker --tlsverify -H  user.c.cto-sandbox.internal:9998 build -t user:secretv1
```

**Response**

AskCopy

```
Sending build context to Docker daemon 5.632 kB
Step 1/2 : FROM alpine:latest
 ---> 88e169ea8f46
Step 2/2 : ADD private_key /root/.ssh/id_rsa
 ---> Using cache
 ---> c6e8e2496663
Error: [Prisma Cloud] Image operation blocked by policy: (No secrets attached), violates: Private keys stored in image /root/.ssh/id_rsa
```

Set the action to **ALERT** instead of **BLOCK**, then go to **Monitor > Compliance** after running the image. Click on the image under **Images** tab.

### Compliance Check ID 597[Direct link to heading](https://docs.prismacloud.io/admin-guide/compliance/detect-secrets\#compliance-check-id-597)

This check detects sensitive information provided in environment variables of container.

## Agentless Secrets Detection[Direct link to heading](https://docs.prismacloud.io/admin-guide/compliance/detect-secrets\#agentless-secrets-detection)

Agentless scanning detects sensitive information inside files in your hosts and container images filesystem.

### Compliance Check ID 456[Direct link to heading](https://docs.prismacloud.io/admin-guide/compliance/detect-secrets\#compliance-check-id-456)

This check detects secrets inside your container images' filesystem. By default, Prisma Cloud alerts you that a secret was detected in a container image. Select **Monitor > Compliance > Compliance Explorer** and search the results using the compliance check ID.

### Compliance Check ID 457[Direct link to heading](https://docs.prismacloud.io/admin-guide/compliance/detect-secrets\#compliance-check-id-457)

This check detects secrets inside your hosts' filesystem. By default, Prisma Cloud alerts you that a secret was detected in a host. Select **Monitor > Compliance > Compliance Explorer** and search the results using the compliance check ID.

### Detected Secrets[Direct link to heading](https://docs.prismacloud.io/admin-guide/compliance/detect-secrets\#detected-secrets)

When agentless scanning detects a secret in a host or container image, only the following information is sent to the Prisma Cloud console.

- The [secret type](https://docs.prismacloud.io/admin-guide/compliance/detect-secrets#secret-types)

- The time when the file with the detected secret was last modified

- A redacted snippet of the secret with a length of less than 10 characters









  - A maximum of 10% of the visible characters for secrets above 30 characters up to a maximum of 10 characters

  - A maximum of 3 visible characters for secrets under 30 characters


- The path to the file where the secret was detected

- The line and offset in the file where the secret was detected in the `line:offset` format


This information provides you with enough context to find the detected secret and take any needed action.

### Secret Types[Direct link to heading](https://docs.prismacloud.io/admin-guide/compliance/detect-secrets\#secret-types)

Agentless scanning detects the following secret types.

- AWS









  - AWS Access Key ID

  - AWS Secret Key

  - AWS MWS Auth Token


- Azure









  - Azure Storage Account access key

  - Azure Service Principal


- GCP Service Account Auth Key

- Private encryption keys

- DB Connection String









  - Java Database Connectivity (JDBC)

  - MongoDB

  - .Net SQL Server


- SaaS API keys









  - Artifactory API Token

  - Artifactory Password

  - Mailchimp Access Key

  - NPM tokens

  - Slack Token

  - Slack Webhook

  - Square OAuth Secret

  - Notion Integration Token

  - Airtable API Key

  - Atlassian Oauth2 Keys

  - CircleCI Personal Token

  - Databricks Authentication

  - GitHub Token

  - GitLab Token

  - Google API key

  - Grafana Token

  - Python Package Index Key (PYPI)

  - Typeform API Token

  - Scalr token

  - Braintree Access Token

  - Braintree Payments Key

  - Braintree Payments ID

  - Datadog Client Token

  - ClickUp Personal API Token

  - OpenAI API Key

  - Jira Token


[PreviousApp-Embedded scanning](https://docs.prismacloud.io/admin-guide/compliance/app-embedded-scanning) [NextRuntime defense](https://docs.prismacloud.io/admin-guide/runtime-defense/runtime-defense)

Last updated 3 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
