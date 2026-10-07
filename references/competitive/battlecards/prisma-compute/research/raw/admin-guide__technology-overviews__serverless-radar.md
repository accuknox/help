For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/technology-overviews/serverless-radar.md).

Serverless Radar helps you to visualize and inspect the attack surface of the serverless functions in your environment. Although Prisma Cloud supports multiple serverless environments, currently serverless radar supports AWS Lambda only.

Serverless functions use different interconnect patterns than containers. Serverless apps are highly decomposed and interact with services using cloud provider-specific gateways, rather than directly with each other or through service meshes. Security teams can have difficulty conceptualizing these interactions, identifying which functions interface with which high value assets, and pinpointing unacceptable exposure.

Even though cloud providers secure the underlying infrastructure that enables Functions as a Service (including isolating functions from each other), it’s still easy to deploy functions with vulnerabilities, insecure configurations, and overly permissive roles. The underlying platform might be secure, but sensitive data can still be lost when an insecure function with read access to an S3 bucket is compromised.

Prisma Cloud offers a serverless-specific view in Radar. Serverless Radar uses a three panel view to show the invocation methods for each function, the services they use, and the permissions granted to access those services.

## Layout[Direct link to heading](https://docs.prismacloud.io/admin-guide/technology-overviews/serverless-radar\#layout)

Serverless Radar shows you how functions interface with other services in their environment.

![serverless radar flow](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-c02bd9e050b8a1031b53b8dec6d39cc74faa715c%252Fserverless_radar_flow.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=41925e64a088cd2304f4c69602c4873a&sv=3)

The left-most column shows how functions are invoked. This is known as the _trigger_ or _event source_. Triggers publish events, and Lambda functions are the custom code that process those events.

The middle column shows all the functions in your environment. Functions are colored maroon, red, orange, yellow, or green to let you quickly assess their security posture. By default, functions are colored by their most severe vulnerabilities, but you can view functions by highest severity compliance issue or runtime events. For vulnerability results, you must configure Prisma Cloud to scan your functions. For runtime issues, you must embed [Serverless Defender](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/compute-edition/34/admin-guide/install/deploy-defender/serverless/serverless.md) into your functions.

The right-most column shows the services with which each function interfaces. Drilling into the function data reveals the permissions each function has been granted to access those services.

Lines connect triggers to functions to services, letting security teams to visualize the entire connectivity flow and access rights. Clicking on individual functions highlights their interconnects in the radar, and opens a pop-up that lets you drill into the details.

## Exploring the data[Direct link to heading](https://docs.prismacloud.io/admin-guide/technology-overviews/serverless-radar\#exploring-the-data)

Prisma Cloud finds, scans, and displays the $LATEST version and all published versions of your functions. Clicking a node in Serverless Radar lets you inspect a function’s configuration and explore all the security-related data that Prisma Cloud has indexed about it.

For example, clicking on the or-test2:$LATEST function opens a popup with summary findings. This particular function has two high risk compliance issues. Clicking on the compliance link takes you to a list of compliance issues for the function.

![serverless radar explore](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-75da27b7aa8c453927a31a2e0d3660e563daf6b6%252Fserverless_radar_explore.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=0c9c1c31549c901aae3dc14c947234e1&sv=3)

Compliance issue 437 indicates overly permissive access to one or more services. Expanding the issue reveals the reason why this compliance issue was raised, with a list of non-compliant service access configurations. One of the misconfigured access policy is for S3.

![serverless radar explore compliance](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-5c1e29396390175805e5a9ace239275810d60ee8%252Fserverless_radar_explore_compliance.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=72123d353332c3388e5cc580ea65cc69&sv=3)

Returning to the first pop-up window, and clicking into the S3 service, you can see that all the actions for the function’s execution role are tightly scoped, except for the last one. It allows all actions on all resources, and could easily be an erroneous configuration overlooked when it was pushed into production.

![serverless radar explore permissions](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-fddd450f62453cb814caf0b8062a9c197c23cd6c%252Fserverless_radar_explore_permissions.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=2b17e8f8e42a3854764ab357a7896213&sv=3)

## Icons and colors[Direct link to heading](https://docs.prismacloud.io/admin-guide/technology-overviews/serverless-radar\#icons-and-colors)

Nodes are color coded based on the highest severity vulnerability or compliance issue they contain, and reflect the currently defined vulnerability and compliance policies. Color coding lets you quickly spot trouble areas in your deployment. Use the drop-down list at the top of the view to choose how you want nodes colored.

- Maroon -- High risk. One or more critical severity issues detected.















![serverless radar critical](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-25eda6ef61958f7ecce751c557fba436c0bace1b%252Fserverless_radar_critical.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=7e99a3f65cc235a35a98b1b0219af673&sv=3)

- Red -- High severity issues detected.















![serverless radar high](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-69c2a4f129e9a71bf4d79f969b1c280196aaab4e%252Fserverless_radar_high.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=4ced2824ce305dddf26c555e0e519e42&sv=3)

- Orange -- Medium severity issues detected.















![serverless radar medium](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-6ded79700259872280baf6f1ef15366f109168df%252Fserverless_radar_medium.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=4a7b5645f5817eb8a36c828f140fca86&sv=3)

- Yellow — Low severity issues detected.

- Green -- Denotes no issues detected.















![serverless radar clean](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-1246d2fb350eb7a230977cbc807943d091b067a7%252Fserverless_radar_clean.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=cbecb3ad4db990615c2de841480c3535&sv=3)

- Gray — Prisma Cloud hasn’t been configured to scan this function for vulnerability and compliance issues.















![serverless radar configure scan](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-9db83361bf9d08bbe8d7a5ec6f4eb46b155280a8%252Fserverless_radar_configure_scan.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=7d3e4e8c0e5d8111efa220f70c9387bf&sv=3)











To configure Prisma Cloud to scan the function, click on the node, and then click **Protect** in the pop-up.















![serverless radar configure scan2](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-b96a3e1d905eb7867b950738153c1ef58b11dcb0%252Fserverless_radar_configure_scan2.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=fc23039503e48c648da71877018f6a1b&sv=3)

- Alias annotation — AWS lets you create [aliases](https://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html) to manage the process of promoting new function versions into production. They’re conceptually similar to symbolic links in the UNIX file system. Prisma Cloud uses a marker to indicate that an alias points to a specific version of a function.















![serverless radar alias](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-a36a093013af1a53db174822b17d62ff3d75b478%252Fserverless_radar_alias.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=8052089bc4a1ed22318f3d31c9e51023&sv=3)











Clicking on the node reveals the aliases that point to the function.















![serverless radar alias detail](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-d58b77e23299373f1d32a9672eecbe263bb4c661%252Fserverless_radar_alias_detail.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=84d84bc9ce36c611b0d31699bd3fa957&sv=3)


## Notes[Direct link to heading](https://docs.prismacloud.io/admin-guide/technology-overviews/serverless-radar\#notes)

There can be a discrepancy between what the AWS Lambda designer shows your function can do and its effective permissions when [IAM permission boundaries](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html) are considered.

For example, if a role is set with permission boundary for DynamoDB, then even though the function’s execution role has permission to access DynamoDB, it still might be blocked by the permission boundary. The function designer in AWS’s console shows that the function has permission to DyanmoDB, but it might not be accurate.

![serverless radar permission boundary](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-4466d9f49cafe40e8a06171c2823ef9f7f9e42b9%252Fserverless_radar_permission_boundary.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=3eb838f88a476e4a598acfe8622975bd&sv=3)

## Setting up Serverless Radar[Direct link to heading](https://docs.prismacloud.io/admin-guide/technology-overviews/serverless-radar\#setting-up-serverless-radar)

Serverless Radar uses the AWS APIs to discover and inspect the functions in your environment. Create an IAM user or role for Prisma Cloud, provide the credentials to Console, and then enable Serverless Radar. With this basic setup, Prisma Cloud will show the triggers, services, and permissions for each function.

**Prerequisites:**

- Prisma Cloud needs an AWS service account to scan your serverless functions. In AWS, you’ve created an IAM user or role with the following permission policy:

















AskCopy



```
{
      "Version": "2012-10-17",
      "Statement": [\
          {\
              "Sid": "PrismaCloudComputeServerlessRadar",\
              "Effect": "Allow",\
              "Action": [\
                  "apigateway:GET",\
                  "cloudfront:ListDistributions",\
                  "cloudwatch:GetMetricData",\
                  "cloudwatch:DescribeAlarms",\
                  "elasticloadbalancing:DescribeListeners",\
                  "elasticloadbalancing:DescribeRules",\
                  "elasticloadbalancing:DescribeTargetGroups",\
                  "elasticloadbalancing:DescribeListenerCertificates",\
                  "events:ListRules",\
                  "iam:GetPolicy",\
                  "iam:GetPolicyVersion",\
                  "iam:GetRole",\
                  "iam:GetRolePolicy",\
                  "iam:ListAttachedRolePolicies",\
                  "iam:ListRolePolicies",\
                  "lambda:GetFunction",\
                  "lambda:GetPolicy",\
                  "lambda:ListAliases",\
                  "lambda:ListEventSourceMappings",\
                  "lambda:ListFunctions",\
                  "logs:DescribeSubscriptionFilters",\
                  "s3:GetBucketNotification",\
                  "kms:Decrypt"\
              ],\
              "Resource": "*"\
          }\
      ]
}
```


1. Open Console.

2. Go to **Manage > Cloud accounts**.

3. Click **Add account**, and configure an xref:~/authentication/credentials-store/AWS-credentials.adoc\[AWS account\].

4. Select the checkbox for the credential.

5. Click **Add**.

6. For the account just added, select the **Serverless Radar** checkbox.















![serverless radar configure](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-5bda81875029c72a35652e9fbad3c1bba208a961%252Fserverless_radar_configure.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=69caf8182c03e38726c516dd43d789b8&sv=3)

7. Click the "Add account" button.











After Prisma Cloud finishes scanning your environment, you should see your functions in Serverless Radar.


## What’s next?[Direct link to heading](https://docs.prismacloud.io/admin-guide/technology-overviews/serverless-radar\#whats-next)

To see vulnerability and compliance information in Serverless Radar, configure Prisma Cloud to [scan](https://docs.prismacloud.io/admin-guide/vulnerability-management/serverless-functions) the contents of each function.

[PreviousRadar](https://docs.prismacloud.io/admin-guide/technology-overviews/radar) [NextPrisma Cloud rules guide for Docker](https://docs.prismacloud.io/admin-guide/technology-overviews/twistlock-rules-guide-docker)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
