For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/compliance/serverless.md).

Prisma Cloud Labs has developed compliance checks for serverless functions.

In AWS Lambda, every function has an execution role. Execution roles are identities with permission policies that control what functions can and cannot do in AWS. When you create a function, you specify an execution role. When the function is invoked, it assumes this role.

When Prisma Cloud scans the functions in your environment, it inspects the execution role for overly permissive access to AWS services and resources. Two fields are inspected: _resource_ and _action_.

## Resource[Direct link to heading](https://docs.prismacloud.io/admin-guide/compliance/serverless\#resource)

Specifies the objects to which the permission policy applies. Resources are specified with ARNs. ARNs let you unambiguously specify a resource across all of AWS. ARNs have the following format:

AskCopy

```
arn:partition:service:region:account-id:resource
```

Where:

- `service` — Identifies the AWS product, such as Amazon S3, IAM, or CloudWatch Logs.

- `resource` — Identies the objects in the service. It often includes the resource type, followed by the resource name itself. For example, the following ARN uniquely identifies the user Francis in the IAM service:

















AskCopy



```
arn:aws:iam::586975633310:user/Francis
```


## Action[Direct link to heading](https://docs.prismacloud.io/admin-guide/compliance/serverless\#action)

Describes the tasks that can be performed on the service. For example, ec2:StartInstances, iam:ChangePassword, and s3:GetObject. Wildcards can be used to grant access to all the actions of a given AWS service. For example, s3:\* applies to all S3 actions.

## Types of issues[Direct link to heading](https://docs.prismacloud.io/admin-guide/compliance/serverless\#types-of-issues)

The following permission policy is tightly scoped. It grants read-write only access to the Books table. Prisma Cloud would not flag an execution role with this type of permissions policy.

AskCopy

```
{
  "Version": "2012-10-17",
  "Statement": {
    "Effect": "Allow",
    "Action": [\
      "dynamodb:GetItem",\
      "dynamodb:BatchGetItem"\
    ],
    "Resource": "arn:aws:dynamodb:us-east-1:125643784111:table/Books"
  }
}
```

The following permissions policy has been implemented carelessly. It allows all DyanmoDB operations on all tables owned by the AWS account in the current region, including dynamodb:DeleteTable, which has serious implications for the integrity and availability of your data. This type of configuration would raise compliance check 437 because the execution role permits all DyanmoDB operations, and it’s unlikely a function actually needs this range of capabilities.

AskCopy

```
{
  "Version": "2012-10-17",
  "Statement": {
    "Sid": "AllAPIActionsOnBooks",
    "Effect": "Allow",
    "Action": "dynamodb:*",
    "Resource": "*"
  }
}
```

## Compliance check details[Direct link to heading](https://docs.prismacloud.io/admin-guide/compliance/serverless\#compliance-check-details)

The following checks are supported:

**434: Sensitive information provided in environment variables**
Detects when functions contain environment variables (such as MYSQL\_PASSWORD) that expose sensitive information.

**435: Private keys stored in function**
Detects private keys in functions.

**436: Unbounded service access**
Detects functions with permission to run all actions on all services and their resources.

**437: Overly permissive service access**
Detects functions with permission to run all actions on one or more services.

**438: Broad resource access**
Detects functions that granted access to all resources in one or more services.

**439: Suspicious function actions**
Detects functions with permission to run actions that are used in exploits and attacks. Includes things like cloudtrail:StopLogging, cloudtrail:UpdateTrail that allow disabling and changing the output of CloudTrail logging.

**440: Unused service API with information disclosure risk**
Detects functions with permissions to unused APIs that could allow information disclosure.

**441: Unused service API with data leakage risk**
Detects functions with permissions to unused APIs that could leak data.

**442: Unused service API with data tampering risk**
Detects functions with permissions to unused APIs that could allow data tampering.

**443: Unused service API with lateral movement risk**
Detects functions with permissions to unused APIs that could allow an attacker to move laterally.

**444: Unused service API with denial of service risk**
Detects functions with permissions to unused APIs that could facilitate a denial of service attack.

**445: Unused service API with information exfiltration risk**
Detects functions with permissions to unused APIs that could allow data exfiltration.

**446: Unused service API with persistent access risk**
Detects functions with permissions to unused APIs that allow persistent access.

**447: Unused service API with privilege elevation risk**
Detects functions with permissions to unused APIs that allow privilege elevation.

## Scanning serverless functions[Direct link to heading](https://docs.prismacloud.io/admin-guide/compliance/serverless\#scanning-serverless-functions)

Configure Prisma Cloud to periodically scan your serverless functions. Function scanning is handled by Console.

1. Open Console.

2. Go to **Defend > Compliance > Functions**.

3. Click on **Add scope**. In the dialog, enter the following settings:









1. Specify a cap for the number of functions to scan.











      Prisma Cloud scans the X most recent functions, where X is the cap value. Set this value to '0' to scan all functions.

2. (AWS only) Specify which regions to scan. By default, the scope is applied to **Regular regions**. Other options include **China regions** or **Government regions**.

3. (AWS only) Select **Scan only latest versions** to only scan the latest version of each function. Otherwise, the scanning will cover all versions of each function up to the specified **cap** value.

4. (AWS only) Select **Scan Lambda Layers** to enable scanning the function’s Layers as well.

5. Select the accounts to scan by credential. If you wish to add an account, click on **Add credential**.

6. Click **Add**.


4. Verify that you have assigned the [correct permissions](https://docs.prismacloud.io/admin-guide/vulnerability-management/serverless-functions#authenticating-with-aws) required to scan.

5. To view the scan report, go to **Monitor > Compliance > Functions**.











All compliance issues identified in the latest serverless scan report can be exported to a CSV file by clicking on the CSV button in the top right of the table.


## View AWS Lambda Layers scan report[Direct link to heading](https://docs.prismacloud.io/admin-guide/compliance/serverless\#view-aws-lambda-layers-scan-report)

Prisma Cloud can scan the AWS Lambda Layers code as part of the Lambda function’s code scanning. This capability can help you determine whether the Compliance checks are associated with the function or function Layers. Follow the steps below to view the Lambda Layers compliance scan results:

1. Open Console.

2. Make sure you selected the **Scan Lambda layers** in the Defend > Compliance > Functions > Functions > Serverless Accounts > **Function scan scope**















![function scan scope](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-fd32db48009d5dcf56ceabb19183e688615095e4%252Ffunction_scan_scope.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=220d2c9143a391dada8c700fe8c253e9&sv=3)

3. Go to **Monitor > Compliance > Functions > Scanned functions**.

4. Filter the table to include functions with the desired Layer by adding the **Layers** filter.











You can also filter the results by a specific layer name or postfix wildcards. Example: `Layers:* OR Layers:arn:aws:lambda:*`















![comp layers filter](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-add98bcc766731f37fe265492b59b1ca564a2ee0%252Fcomp_layers_filter.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=a96a8d3056a77ad53725acd675f5acaf&sv=3)

5. Open the **Function details** dialog to view the details about the Layers and the Compliance issues associated with them:









1. Click on a specific function

2. See the Function’s vulnerabilities, compliance issues and package info in the related tabs. Use the **Found in** column to determine if the component is associated with the Function or with the Function’s Layers.















      ![comp function details](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-b7218a33b6752b12a17c9dd6d3c4a18d9e5b423b%252Fcomp_function_details.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=75c7e9f8772a524e9ca1d12e006b45eb&sv=3)

3. Use the **Layers info** tab to see the full list of the function’s the Layers.















      ![vuls functions layers info](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-fa6e8a8d9265a0ac4043c7886dd30ce8a3cfa96d%252Fvuls_functions_layers_info.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=5801abd84edb70970d19d9ff04a4dda8&sv=3)


[PreviousPrisma Cloud compliance checks](https://docs.prismacloud.io/admin-guide/compliance/prisma-cloud-compliance-checks) [NextWindows compliance checks](https://docs.prismacloud.io/admin-guide/compliance/windows)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
