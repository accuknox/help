> For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.prismacloud.io/content-collections/runtime-security/audit/kubernetes-auditing.md).

# Kubernetes Auditing

The Kubernetes auditing system records the activities of users, administrators, and other components, that have affected the cluster. Prisma Cloud can ingest, analyze, and alert on security-relevant events. Write custom rules or leverage Prisma Cloud Labs prewritten rules to assess the incoming audit stream and surface suspicious activity.

Audits types are limited to the ones been configured by the audit policy of the cloud provider.

## Rule library

Custom rules are stored in a central library, where they can be reused. Besides your own rules, Prisma Cloud Labs also distributes rules via the Intelligence Stream. These rules are shipped in a disabled state by default. You can review, and optionally apply them at any time.

Your Kubernetes audit policy is defined in **Defend > Access > Kubernetes**, and formulated from the rules in your library. There are four types of rules, but the only one relevant to the audit policy is the `kubernetes-audit` type. Custom rules are written and managed in Console under **Defend > Custom rules > Runtime** with an online editor. The compiler checks for syntax errors when you save a rule.

## Expression grammar

Expressions let you examine contents of a Kubernetes audit. Expressions have the following grammar:

`expression: term (op term | in )*`

term\
integer | string | keyword | event | '(' expression ')' | unaryOp term

in\
'(' integer | string (',' integer | string)\*)?

op\
and | or | > | < | >= | ⇐ | = | !=

unaryOp\
not

keyword\
startswith | contains

string\
Strings must be enclosed in double quotes

integer\
int

event\
process, file system, or network

## Kubernetes audit events

When Prisma Cloud receives an audit, it is assessed against your policy. Like all policies in Prisma Cloud, rule order is important. Rules are processed top to bottom, and processing stops at the first match. When a rule matches, an alert is raised.

Write rules to surface audits of interest. Rules are written with the jpath function. The jpath function extracts fields from JSON objects, which is the format of a Kubernetes audit. The extracted string can then be compared against strings of interest. The primary operators for jpath expressions are '=', 'in', and 'contains'. For non-trivial examples, look at the Prisma Cloud Lab rules.

The argument to jpath is a single string. The right side of the expression must also be a string. A basic rule with a single jpath expression has the following form:

```
jpath("path.in.json.object") = "something"
```

Let’s look at some examples using the following JSON object as our example audit.

Example Kubernetes audit

```json
{
   "user":{
      "uid":"1234",
      "username":"some-user-name",
      "groups":[
         "group1",
         "group2"
      ]
   },
   "stage":"ResponseComplete"
}
```

To examine a user’s UID, use the following syntax. This expression evaluates to true.

```
jpath("user.uid") = "1234"
```

To examine the username, use the following syntax:

```
jpath("user.username") = "some-user-name"
```

To examine the stage field, use the following syntax:

```
jpath("stage") = "ResponseComplete"
```

To examine the groups list field, use the following syntax:

```
jpath("user.groups") contains "group1"
```

Or alternatively:

```
jpath("user.groups") in ("group1","group2")
```

## Integrating with self-managed clusters

Prisma Cloud supports self-managed clusters. See [here](/content-collections/runtime-security/install/system-requirements.md) for supported Kubernetes versions. You can deploy clusters with any number of tools, including kubeadm.

**Prerequisites:** You’ve already deployed a Kubernetes cluster.

### Configure the API server

Configure the API server to forward audits to Prisma Cloud.

To configure the audit webhook backend:

* Create an audit policy file that specifies the events to record and the data events should contain.
* Create a configuration file that defines the backend details and configurations.
* Update the API server config file to point to your audit policy and configuration files.

If your API server runs as a pod, then the audit policy and configuration files must be placed in a directory mounted by the API server pod. Either place the files in an already mounted directory, or create a new one.

If flags/objects related to AuditSink/dynamic auditing were previously added to your API server configuration, remove them. Otherwise, this setup won’t work.

1. Specify the audit policy.

   Create a file called *audit-policy.yaml* with the following recommended policy:

   ```
   apiVersion: audit.k8s.io/v1 # This is required.
   kind: Policy
   # Generate audit events only for ResponseComplete or panic stages of a request.
   omitStages:
     - "RequestReceived"
     - "ResponseStarted"
   rules:
     # Audit on pod exec/attach events
     - level: Request
       resources:
       - group: ""
         resources: ["pods/exec", "pods/attach"]

     # Audit on pod creation events
     - level: Request
       resources:
       - group: ""
         resources: ["pods"]
       verbs: ["create"]

     # Audit on changes to the twistlock namespace (defender daemonset)
     - level: Request
       verbs: ["create", "update", "patch", "delete"]
       namespaces: ["twistlock"]

     # Default catch all rule
     - level: None
   ```

   More details can be found [here](https://kubernetes.io/docs/tasks/debug-application-cluster/audit/#audit-policy).
2. Create a configuration file.

   Create a configuration file named *audit-webhook.yaml*.

   For the server address, `<console_url_webhook_suffix>`, do the following

   Step 1. Perform GET /api/v1/settings/kubernetes-audit and get the suffix. example response: { "webhookUrlSuffix": "Rov4TLMx1UiaJuP99OyulwQVUT0=", "lastPollingTime": null }

   Step 2. Append the suffix to your console URL

   For example : <https://1.1.1.1:8083/api/v1/kubernetes/webhook/Rov4TLMx1UiaJuP99OyulwQVUT0=>

   ```
   apiVersion: v1
   kind: Config
   preferences: {}
   clusters:
   - name: <cluster_name>
     cluster:
       server: <console_url_webhook_suffix> # compute console endpoint as stated above
   contexts:
   - name: webhook
     context:
       cluster: <cluster_name>
       user: kube-apiserver
   current-context: webhook
   ```
3. Move the config files into place.

   Move both *audit-policy.yaml* and *audit-webhook.yaml* to a directory that holds your API server config files. If the API server runs as a pod, move the files to a directory that is accessible to the pod. Accessible directories can be found in the API server config file under `mounts`.

   Alternatively, create a new directory and add it to `mounts`. For more information, see [here](https://kubernetes.io/docs/tasks/debug-application-cluster/audit/#log-backend).
4. Add flags.

   Configure the API server to use the policy and configuration files you just created. Add the following flags to the API server config file:

   ```
   spec:
     containers:
     - command:
       # Existing flags
       ...
       # New flags for Prisma Cloud:
       - --audit-policy-file=<PATH-TO-API-SERVER-CONFIG-FILES>/audit-policy.yaml
       - --audit-webhook-config-file=<PATH-TO-API-SERVER-CONFIG-FILES>/audit-webhook.yaml
   ```

   When changing the kube-apiserver config file, the API server automatically restarts. It can take a few minutes for the API server to resume operations.

## Integrating with Google Kubernetes Engine (GKE)

On GKE, Prisma Cloud retrieves audits from Stackdriver, polling it every 10 minutes for new data.

Note that there can be some delay between the time an event occurs in the cluster and when it appears in Stackdriver. Due to Twistock’s polling mechanism, there’s another delay between the time an audit arrives in Stackdriver and when it appears in Prisma Cloud.

See [our system requirements](/content-collections/runtime-security/install/system-requirements.md) for GKE cluster versions supported by Prisma Cloud.

**Prerequisites:** You’ve created a service account with one of the following authorization scopes:

* <https://www.googleapis.com/auth/logging.read>
* <https://www.googleapis.com/auth/logging.admin>
* <https://www.googleapis.com/auth/cloud-platform.read-only>
* <https://www.googleapis.com/auth/cloud-platform>

1. Open Console.
2. Go to **Defend > Access > Kubernetes**.
3. Set **Kubernetes auditing** to **Enabled**.
4. Click **Add settings** to configure how Prisma Cloud connects to your cloud provider’s managed Kubernetes service.
   1. Set **Provider** to **GKE**.
   2. Select your GKE credential.

      If there are no accounts to select, add one to the [credentials store](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/enterprise-edition/content-collections/runtime-security/authentication/credentials-store/credentials-store.md).
   3. (Optional) Specify clusters to collect audit data, allows to limit the collected data
   4. Specify project IDs. If unspecified, the project ID where the service account was created is used
   5. (Optional) Specify Advanced filter - specify a filter to reduce the amount of data transferred

      Do not use the `resource.type` or `timestamp` filters because Prisma Cloud uses them internally.
   6. Click **Add**.
5. Click **Save**.

## CA bundle

If you’re sending audit data to Prisma Cloud’s webhook over HTTPS, you must specify a CA bundle in the AuditSink object.

If you’ve customized Console’s certificate, you can get a copy from **Manage > Authentication > System-certificates > TLS certificate for Console**. Paste the certificate into a file named *server-cert.pem*, then run the following command:

```
$ openssl base64 -in server-cert.pem -out base64-output -A
```

In the AuditSingle object, set the value of caBundle to the contents of the base64-output file.

## Testing your setup

Write a new rule, or select a prewritten rule from the inventory, and add it your audit policy. This setup installs a rule that fires when privileged pods are created in the cluster.

1. Open Console, and go to **Defend > Access > Kubernetes**.
2. Add a Prisma Cloud Labs prewritten rule.
   1. Click **Select rules**.
   2. If you’re integrated with a managed cluster, select **Prisma Cloud Labs - Privileged pod creation**. If you’re integrated with GKE, select **Prisma Cloud Labs - GKE - privileged pod creation**.

      There are separate rules for standard Kubernetes and GKE because the structure of the audits are different. Therefore, the logic for parsing the audit JSON is different.
   3. Click **Save**.
3. Create a pod deployment file named *priv-pod.yaml*, and enter the following contents.

   ```yaml
   apiVersion: v1
   kind: Pod
   metadata:
     name: nginx
     labels:
       app: nginx
   spec:
     containers:
     - name: nginx
       image: nginx
       ports:
       - containerPort: 80
       securityContext:
         privileged: true
   ```
4. Create the privileged pod.

   ```
   $ kubectl apply -f priv-pod.yaml
   ```
5. Verify an audit was created.

   Go to **Monitor > Events**, and select the **Kubernetes Audits** filter.

   <figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-102b825293f767c4c1c7060e73655f2bc685ef7a%2Fkubernetes-auditing.png?alt=media" alt="kubernetes auditing"><figcaption></figcaption></figure>

## Integrating with Azure Kubernetes Service (AKS)

With AKS, Prisma Cloud retrieves audits from "Log Analytics workspace", polling it every 10-15 minutes for new data.

You will have to enable exporting AKS logs into Azure Workspace, and Prisma Cloud will extract the logs from there. You only need to export AKS resource logs of the category `kube-audit` (see [here](https://docs.microsoft.com/en-us/azure/aks/monitor-aks#collect-resource-logs)). Also, there can be some delay between the time an event occurs in the cluster and when it appears in Workspace. Due to Prisma Cloud’s polling mechanism, there’s another delay between the time an audit arrives in the Workspace and when it appears in Prisma Cloud.

Prisma Cloud supports only AKS cluster versions that allow log exporting.

<figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-5ed660ba1b3c815fb4ebc5241e4268357ab8abb8%2Fkubernetes-aks-diagram-audit.png?alt=media" alt="kubernetes aks diagram audit"><figcaption></figcaption></figure>

1. Open Console.
2. Go to **Defend > Access > Kubernetes**.
3. Set **Kubernetes auditing** to **Enabled**.
4. Click **Add settings** to configure how Prisma Cloud connects to your cloud provider’s managed Kubernetes service.
   1. Set **Provider** to **AKS**.
   2. Select your AKS credential.

      If there are no accounts to select, add one to the [credentials store](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/enterprise-edition/content-collections/runtime-security/authentication/credentials-store/credentials-store.md).
   3. (Optional) specify clusters to collect audit data, allows to limit audit data.
   4. Specify the Workspace Name.

      We recommend that you use the free 7 day retention period workspace.
   5. Specify a list of resource groups.

      If unspecified, all resource groups will be used to retrieve the audits.
   6. (Optional) Specify Advanced filter to reduce the amount of data transferred.

      Use this [reference](https://docs.microsoft.com/en-us/azure/azure-monitor/logs/get-started-queries) for help with the query syntax.
   7. Click **Add**.
5. Click **Save**.

## Integrating with Elastic Kubernetes Service (EKS)

On EKS, Prisma Cloud retrieves audits from AWS "Cloud watch", polling it every 10-15 minutes for new data.

You will have to enable exporting EKS logs into AWS Cloud Watch, and Prisma Cloud will extract the logs from there. You only need to enable exporting Kubernetes audits (logs of type `audit`), see [here](https://docs.aws.amazon.com/eks/latest/userguide/control-plane-logs.html). Also, there can be some delay between the time an event occurs in the cluster and when it appears in CloudWatch.

Due to Prisma Cloud’s polling mechanism, there’s another delay between the time an audit arrives in the CloudWatch and it appears in Prisma Cloud.

Prisma Cloud supports only EKS cluster versions that allow log exporting.

<figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-491f564ac52111981a405ae6f8110d9cd68876e9%2Fkubernetes-eks-diagram-audit.png?alt=media" alt="kubernetes eks diagram audit"><figcaption></figcaption></figure>

1. Open Console.
2. Go to **Defend > Access > Kubernetes**.
3. Set **Kubernetes auditing** to **Enabled**.
4. Click **Add settings** to configure how Prisma Cloud connects to your cloud provider’s managed Kubernetes service.
   1. Set **Provider** to **EKS**.
   2. Select your EKS credential.

      If there are no accounts to select, add one to the [credentials store](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/enterprise-edition/content-collections/runtime-security/authentication/credentials-store/credentials-store.md).
   3. Specify the cluster region.
   4. (Optional) Specify Advanced filter to reduce the amount of data transferred.

      Use [AWS Log Insights syntax](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax.html).
   5. Click **Add**.
5. Click **Save**.

## Custom rules

A custom rule is made up of one or more conditions. Configure custom rules policy in order to trigger audits and match them. Prisma Cloud supports GKE, EKS, and AKS clusters.

## Write a Kubernetes custom rule

Expression syntax is validated when you save a custom rule.

1. Open Console, and go to **Defend > Access > Kubernetes**.
2. Click **Add rule**.
3. Enter a name for the rule.
4. In **Message**, enter an audit message to be emitted when an event matches the condition logic in this custom rule.
5. Enter your expression logic.

   You can filter by cluster name (applies to all cloud providers), project ID (GCP), account ID (AWS), resource group (only capital letters, GCP), and subscription ID (Azure)
6. Click **Add**.

   Your expression logic is validated before it’s saved to the Console’s database.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.prismacloud.io/content-collections/runtime-security/audit/kubernetes-auditing.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
