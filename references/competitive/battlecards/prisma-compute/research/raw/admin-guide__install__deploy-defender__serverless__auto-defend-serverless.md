For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/install/deploy-defender/serverless/auto-defend-serverless.md).

Serverless auto-defend lets you automatically add the Serverless Defender to the AWS Lambda functions deployed in your account. Prisma Cloud uses the AWS API to deploy the Serverless Defender as a Lambda layer based on the auto-defend rules.

It is an additional option for deploying the Serverless Defender, on top of manually adding it [as a dependency](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/compute-edition/34/admin-guide/install/deploy-defender/serverless/serverless.md) or adding it [as a Lambda layer](https://docs.prismacloud.io/admin-guide/install/deploy-defender/serverless/install-serverless-defender-layer).

Serverless auto-defend supports the following runtimes:

Platform

Runtime

AWS

- Node.js: 16.x/18.x/20.x

- Python: 3.1/3.8/3.9/3.11

- Ruby: 3.2

- Java: 17.0

- C#: 6.0

- G0: 1.x


Azure

- Node.js: 20.x

- Python: 3.9

- Java: 17


GCP

- Node.js: 20.x

- Python: 3.7/3.9

- Java: 17


## Limitations[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/serverless/auto-defend-serverless\#limitations)

- Auto-protect is implemented with a layer.









  - AWS Lambda has a limit of [five layers](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html) per function. If your functions have multiple layers, and they might exceed the layer limit with auto-defend, consider protecting them with the [embedded](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/compute-edition/34/admin-guide/install/deploy-defender/serverless/serverless.md) option.


- Prisma Cloud doesn’t support defending (or scanning) AWS Lambda functions that are [deployed as container images](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-images.html) at the time of creating a function in your AWS account.


## Required permissions[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/serverless/auto-defend-serverless\#required-permissions)

Prisma Cloud needs the following permissions to automatically protect Lambda functions in your AWS account. Add the following policy to an IAM user or role:

AskCopy

```
{
    "Version": "2012-10-17",
    "Statement": [\
        {\
            "Sid": "PrismaCloudComputeServerlessAutoProtect",\
            "Effect": "Allow",\
            "Action": [\
                "lambda:PublishLayerVersion",\
                "lambda:UpdateFunctionConfiguration",\
                "lambda:GetLayerVersion",\
                "lambda:GetFunctionConfiguration",\
                "iam:SimulatePrincipalPolicy",\
                "lambda:GetFunction",\
                "lambda:ListFunctions",\
                "iam:GetPolicyVersion",\
                "iam:GetRole",\
                "iam:ListRolePolicies",\
                "iam:ListAttachedRolePolicies",\
                "iam:GetRolePolicy",\
                "iam:GetPolicy",\
                "lambda:ListLayerVersions",\
                "lambda:ListLayers",\
                "lambda:DeleteLayerVersion",\
                "kms:Decrypt",\
                "kms:Encrypt",\
                "kms:CreateGrant"\
            ],\
            "Resource": "*"\
        }\
    ]
}
```

## Serverless auto-defend rules[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/serverless/auto-defend-serverless\#serverless-auto-defend-rules)

To secure one or multiple AWS Lambda functions using serverless auto-defend:

1. Define a serverless protection runtime policy.

2. Define a serverless WAAS policy.

3. Add a serverless auto-defend rule.


## Defining your runtime protection policy[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/serverless/auto-defend-serverless\#defining-your-runtime-protection-policy)

By default, Prisma Cloud ships with an empty serverless runtime policy. An empty policy disables runtime defense entirely.

You can enable runtime defense by creating a rule. By default, new rules:

- Apply to all functions (`*`), but you can target them to specific functions by function name.

- Block all processes from running except the main process. This protects against command injection attacks.


When functions are invoked, they connect to Compute Console and retrieve the latest policy. To ensure that functions start executing at time=0 with your custom policy, you must predefine the policy. Predefined policy is embedded into your function along with the Serverless Defender by way of the `TW_POLICY` environment variable.

1. Log into Prisma Cloud Console.

2. Go to **Defend > Runtime > Serverless Policy**.

3. Click **Add rule**.

4. In the **General** tab, enter a rule name.

5. (Optional) In **Scope**, target the rule to specific functions.











Create a new collection.

6. Set the rule parameters in the **Processes**, **Networking**, and **File System** tabs.

7. Click **Save**.


## Defining your serverless WAAS policy[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/serverless/auto-defend-serverless\#defining-your-serverless-waas-policy)

Prisma Cloud lets you protect your serverless functions against application layer attacks by utilizing the serverless [Web Application and API Security (WAAS)](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/compute-edition/34/admin-guide/waas/waas.md).

By default, the serverless WAAS is disabled. To enable it, add a new serverless WAAS rule.

1. Log into Prisma Cloud Console.

2. Go to **Defend > WAAS > Serverless**.

3. Click **Add rule**.

4. In the **General** tab, enter a rule name.

5. (Optional) In **Scope**, target the rule to specific functions.











Create a new collection. In the **Functions** field, enter a function name. Use [pattern matching](https://docs.prismacloud.io/admin-guide/configure/rule-ordering-pattern-matching) to refine how it’s applied.

6. Set the protections you want to apply ( **SQLi**, **CMDi**, **Code injection**, **XSS**, **LFI**).

7. Click **Save**.


## Add a serverless auto-defend rule[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/serverless/auto-defend-serverless\#add-a-serverless-auto-defend-rule)

The serverless auto-defend rules let you specify which functions you want to protect. When defining a specific rule you can reference the relevant credential, regions, tags, function names and runtimes. Each auto-defend rule is evaluated separately.

1. Open Compute Console, and go to **Manage > Defenders > Deploy > Serverless auto-defend**.

2. Click on **Add rule**.

3. In the dialog, enter the following settings:









1. Enter a rule name.

2. In **Provider** \- only AWS is supported.

3. Specify the scope.











      The available resources for scope are:









      - **Functions** \- either specific names or prefix.

      - **Labels** \- allows specifying either regions (format - region:REGION\_NAME) or AWS tags (format - KEY:VALUE).


4. Specify the Console name.

5. Specify the runtimes.

6. Select or [create credentials](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/compute-edition/34/admin-guide/authentication/credentials-store/credentials-store.md) so that Prisma Cloud can access your account.

7. (Optional) Specify a proxy for the Defenders to use when communicating with the Console.

8. Click **Add**.


4. The new rule appears in the table of rules.

5. Click **Apply Defense**.











By default, the serverless auto-defend rules are evaluated every 24 hours.











When a rule is deleted, the new set of rules is evaluated and applied **immediately**.


[PreviousDeploy Serverless Defender as a Lambda Layer](https://docs.prismacloud.io/admin-guide/install/deploy-defender/serverless/install-serverless-defender-layer) [NextDeploy App-Embedded Defender](https://docs.prismacloud.io/admin-guide/install/deploy-defender/app-embedded)

Last updated 3 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
