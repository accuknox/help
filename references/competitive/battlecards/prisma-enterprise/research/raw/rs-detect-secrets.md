> For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.prismacloud.io/content-collections/runtime-security/compliance/operations/detect-secrets.md).

# Detect Secrets

Prisma Cloud can detect sensitive information that is improperly secured inside images and containers. Scans can detect embedded passwords, login tokens, and other types of secrets. To detect improperly secured secrets, add the following checks to your [compliance policy](/content-collections/runtime-security/compliance/operations/manage-compliance.md).

## Defender Secrets Detection

Your deployed defenders detect sensitive information inside images and containers. Select **Monitor > Compliance > Compliance Explorer** and search the results using the following compliance check IDs.

### Compliance Check ID 424

This check detects sensitive information provided in environment variables of image. The data so provided can be easily exposed by running `docker inspect` on the image and thus compromising privacy.

**Example**

```
$ docker --tlsverify -H :9998 build -t secret:v1 .
```

**Response**

```
Sending build context to Docker daemon 2.048 kB
Step 1/2 : FROM alpine:latest
 ---> 88e169ea8f46
Step 2/2 : ENV PASSWORD = secret
 ---> Using cache
 ---> 8f3627bc339b
Error: [Prisma Cloud] Image operation blocked by policy: (No secrets attached), violates: The environment variable PASSWORD contains sensitive data
```

### Compliance Check ID 425

This check detects private keys stored in an image.

**Example**

Select to **Runtime Security > Defend > Compliance**. Add a new compliance rule to block running an image with private key in it.

**Test**

```
$ docker --tlsverify -H  user.c.cto-sandbox.internal:9998 build -t user:secretv1
```

**Response**

```
Sending build context to Docker daemon 5.632 kB
Step 1/2 : FROM alpine:latest
 ---> 88e169ea8f46
Step 2/2 : ADD private_key /root/.ssh/id_rsa
 ---> Using cache
 ---> c6e8e2496663
Error: [Prisma Cloud] Image operation blocked by policy: (No secrets attached), violates: Private keys stored in image /root/.ssh/id_rsa
```

Set the action to **ALERT** instead of **BLOCK**, then go to **Runtime Security > Monitor > Compliance** after running the image. Click on the image under **Images** tab.

### Compliance Check ID 597

This check detects sensitive information provided in environment variables of container.

## Agentless Secrets Detection

Agentless scanning detects sensitive information inside files in your hosts and container images filesystem.

### Compliance Check ID 456

This check detects secrets inside your container images' filesystem. By default, Prisma Cloud alerts you that a secret was detected in a container image. Select **Monitor > Compliance > Compliance Explorer** and search the results using the compliance check ID.

### Compliance Check ID 457

This check detects secrets inside your hosts' filesystem. By default, Prisma Cloud alerts you that a secret was detected in a host. Select **Monitor > Compliance > Compliance Explorer** and search the results using the compliance check ID.

### Detected Secrets

When agentless scanning detects a secret in a host or container image, only the following information is sent to the Prisma Cloud console.

* The [secret type](#secret-types)
* The time when the file with the detected secret was last modified
* A redacted snippet of the secret with a length of less than 10 characters
  * A maximum of 10% of the visible characters for secrets above 30 characters up to a maximum of 10 characters
  * A maximum of 3 visible characters for secrets under 30 characters
* The path to the file where the secret was detected
* The line and offset in the file where the secret was detected in the `line:offset` format

This information provides you with enough context to find the detected secret and take any needed action.

### Secret Types

Agentless scanning detects the following secret types.

* AWS
  * AWS Access Key ID
  * AWS Secret Key
  * AWS MWS Auth Token
* Azure
  * Azure Storage Account access key
  * Azure Service Principal
* GCP Service Account Auth Key
* DB Connection String
  * MongoDB
  * .Net SQL Server
* SaaS API keys
  * Artifactory API Token
  * Artifactory Password
  * Mailchimp Access Key
  * NPM tokens
  * Slack Token
  * Slack Webhook
  * Square OAuth Secret
  * Notion Integration Token
  * Airtable API Key
  * Atlassian Oauth2 Keys
  * CircleCI Personal Token
  * Databricks Authentication
  * GitHub Token
  * GitLab Token
  * Google API key
  * Grafana Token
  * Python Package Index Key (PYPI)
  * Typeform API Token
  * Scalr token
  * Braintree Access Token
  * Braintree Payments Key
  * Braintree Payments ID
  * Datadog Client Token
  * ClickUp Personal API Token
  * OpenAI API Key
  * Jira Token


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.prismacloud.io/content-collections/runtime-security/compliance/operations/detect-secrets.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
