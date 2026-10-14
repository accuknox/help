Scrape ID: 01a1361e-ba8a-72f1-b8b3-6f30fd931c78
[Skip to main content](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/cloud#__docusaurus_skipToContent_fallback)

AI Detection and Response reaches end of support on November 30, 2026. AIDR capabilities continue in [Falcon Guardian](https://docs.crowdstrike.com/access?ft:originId=dt55byd3) with expanded AI security.

On this page

## AWS Collector [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/cloud\#aws-collector "Direct link to AWS Collector")

You can register and deploy an AIDR **AWS** collector to ingest Amazon Bedrock model invocation logs.

## Requirements [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/cloud\#requirements "Direct link to Requirements")

- **Subscription:** AIDR for Agents

- **Default roles:** AIDR Admin role explicitly assigned to your Falcon user for the current customer account

- **Permissions required for custom roles:**
  - Manage AIDR findings and agent collectors
  - Read AIDR data from LogScale
  - Read AIDR findings and agent collectors
- **CrowdStrike clouds:** Available in US-1, US-2, and EU-1

- **Network:** HTTP access to
[AIDR origins](https://aidr-docs.crowdstrike.com/docs/aidr#cloud-origins)


- **AWS:**Account with the necessary permissions for these actions:
  - Enable Amazon Bedrock model invocation logging in each region.
  - Create and manage IAM roles and policies.
  - Create and configure a Lambda function.
  - Pass the Lambda execution role during function creation (`iam:PassRole` permission).
    The Lambda function runs with a minimal execution role that writes CloudWatch Logs, reads S3 objects, and writes temporary data files to the log bucket.
  - Create and configure S3 buckets and bucket notifications.

## Register collector [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/cloud\#register-cloud-collector "Direct link to Register collector")

1. On the **Collectors** page, click **\+ Collector**.

2. Click **Logging**, then click **AWS**, then click **Next**.
3. On the **Add a Collector** screen:
   - **Collector Name:** Enter a descriptive name for the collector. This name appears in dashboards and reports.
   - **Logging:** Select whether to log prompt data and model responses, or only metadata sent to AIDR. You can also exclude prompt content in [access rule action settings](https://aidr-docs.crowdstrike.com/docs/aidr/policies/access-rules#exclude-prompt-content).
   - **Optional. Policy:** Assign a policy to analyze incoming data and model responses.

The assigned policy determines which detections run on data sent to AIDR.
Policies define rules for detecting malicious activity, sensitive data exposure, topic violations, and other risks in AI interactions.

     - Select an existing policy available for this collector type.

       The selected policy name appears under the drop-down list. After you save the collector registration, this label becomes a link to the corresponding policy page.

       You can create a policy on the **Policies** page.

     - You can select `No Policy, Log Only`. Without a policy, AIDR records activity for visibility and analysis without applying detection rules.

4. Click **Save** to complete collector registration.

This opens the collector details page, where you can:

- Update the collector name, logging preference, and policy assignment.
- Click the policy link to view the policy details.
- Copy credentials and AIDR base URL from the **Config** tab to call AIDR APIs.
- View installation instructions for the collector type on the **Install** tab.
- View the collector configuration activity logs.

To open the collector details later, select your collector from the list on the **Collectors** page.

## Deploy collector [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/cloud\#deploy-collector "Direct link to Deploy collector")

To deploy an AWS collector, follow the instructions in the collector’s **Install** tab.
These sections describe additional setup details.

In the AWS integration, a Lambda function generates presigned URLs for Amazon Bedrock model invocation log files stored in Amazon S3.
The Lambda function sends these URLs to AIDR, which retrieves and processes the logs.
Some log entries reference externally stored payload data, such as prompts or responses that exceed a size threshold.
The Lambda function resolves these references and sends AIDR the full content.
The resulting event data appears in AIDR event logs.

The collector's **Install** tab includes `aws` CLI commands to perform these actions:

1. Enable Amazon Bedrock model invocation logging to an S3 bucket.
2. Create and configure a Lambda function that forwards log references to AIDR.
3. Add an S3 trigger to invoke the Lambda function when new log files are written.

You can run these commands in environments where the `aws` CLI is installed and configured with the necessary permissions, or in automation workflows such as Terraform.

You can also complete this setup in the AWS Management Console.

### Enable Amazon Bedrock model invocation logging to S3 [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/cloud\#enable-amazon-bedrock-model-invocation-logging-to-s3 "Direct link to Enable Amazon Bedrock model invocation logging to S3")

1. Create an S3 bucket to store Amazon Bedrock model invocation logs.

2. Add a bucket policy that allows Amazon Bedrock to write log files to the bucket.

In the AWS Management Console, open the bucket's **Permissions** tab and edit the **Bucket policy**.
Replace the placeholders with your S3 bucket name, AWS account ID, and region:





```json
{
     "Version": "2012-10-17",
     "Statement": [\
       {\
         "Effect": "Allow",\
         "Principal": {\
           "Service": "bedrock.amazonaws.com"\
         },\
         "Action": "s3:PutObject",\
         "Resource": "arn:aws:s3:::<S3-bucket>/*",\
         "Condition": {\
           "StringEquals": {\
             "aws:SourceAccount": "<AWS-account-id>"\
           },\
           "ArnLike": {\
             "aws:SourceArn": "arn:aws:bedrock:<AWS-region>:<AWS-account-id>:*"\
           }\
         }\
       }\
     ]
}
```

3. In the AWS Management Console, open **Amazon Bedrock** and click **Settings** under **Configure and learn**.

4. Enable **Model invocation logging**.

5. For the logging destination, select **S3 only**.

6. In the **S3 location** field, enter the bucket name and optional prefix.

7. Click **Save settings**.


### Create Lambda function to forward events to AIDR [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/cloud\#create-lambda-function-to-forward-events-to-aidr "Direct link to Create Lambda function to forward events to AIDR")

1. On the collector page in the AIDR console, click **Install** and download the `lambda_function.zip` file from the **Download Lambda Function (ZIP)** link.
2. In the AWS Management Console, open the **Lambda** service and click **Create function**.
3. On the **Create function** page:
   - Select **Author from scratch**.
   - Enter a **Function name**, for example: `aidr-<aidr-organization-name>-<aidr-collector-name>-<aws-region>`.
   - Select `Python <version>` as the **Runtime**.
   - Under **Permissions**, leave the default setting. Lambda creates an execution role with permissions to write logs to CloudWatch.
   - Click **Create function**.
4. On the function details page, under **Code source**:
   - Upload the `lambda_function.zip` file.
   - Add these environment variables using values from the collector page in the AIDR console:
     - `AIDR_BASE_URL` \- AIDR API base URL, shown in the **Set Environment Variables** section of the **Install** tab. For example, `https://api.crowdstrike.com/aidr/aiguard`.
     - `API_KEY` \- Current token from the **Config** tab.

### Add permissions to Lambda function role [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/cloud\#add-permissions-to-lambda-function-role "Direct link to Add permissions to Lambda function role")

With the default execution role setting, Lambda performs these actions during function creation:

- Create an IAM role and assign it to the Lambda function.
- Add a trust policy for `lambda.amazonaws.com` to the role, allowing the Lambda service to assume it.
- Attach the `AWSLambdaBasicExecutionRole` managed policy to the role, allowing the function to write execution logs to CloudWatch.

To grant the Lambda function's presigned URLs access to the log bucket, add a policy to the Lambda role.
Grant these permissions on the Bedrock log bucket and prefix:

- `s3:GetObject` \- Read from the bucket.
- `s3:PutObject` \- Create temporary data files when bundling externally stored payload content.

On the Lambda function page:

1. Click the **Configuration** tab, then click **Permissions** in the left sidebar.

2. Click the role name to open its configuration in the IAM console.

3. Under **Permissions**, click **Add permissions** and create an inline policy using this template in the JSON editor.
Replace the placeholders with your S3 bucket name and prefix:





```json
{
     "Version": "2012-10-17",
     "Statement": [\
       {\
         "Effect": "Allow",\
         "Action": ["s3:GetObject"],\
         "Resource": ["arn:aws:s3:::<S3-bucket>/<S3-prefix>/*"]\
       },\
       {\
         "Effect": "Allow",\
         "Action": ["s3:PutObject"],\
         "Resource": ["arn:aws:s3:::<S3-bucket>/<S3-prefix>/*.data.tar"]\
       }\
     ]
}
```

4. Click **Next**.

5. Enter **Policy name**.

6. Click **Create policy**.


note:

You can also create an IAM role in advance with the required trust and permission policies.
Assign this role to the Lambda function during creation.
The trust policy must allow `lambda.amazonaws.com` as the principal so that the Lambda service can assume the role.

Example trust policy

```json
{
  "Version": "2012-10-17",
  "Statement": [\
    {\
      "Effect": "Allow",\
      "Principal": {\
        "Service": "lambda.amazonaws.com"\
      },\
      "Action": "sts:AssumeRole"\
    }\
  ]
}
```

Instead of defining permissions inline, you can create customer-managed policies and attach them to the role.

Example CloudWatch permission policy

```json
{
  "Version": "2012-10-17",
  "Statement": [\
    {\
      "Effect": "Allow",\
      "Action": "logs:CreateLogGroup",\
      "Resource": "arn:aws:logs:<AWS-region>:<AWS-account-id>:*"\
    },\
    {\
      "Effect": "Allow",\
      "Action": ["logs:CreateLogStream", "logs:PutLogEvents"],\
      "Resource": [\
        "arn:aws:logs:<AWS-region>:<AWS-account-id>:log-group:/aws/lambda/<Lambda-function-name>:*"\
      ]\
    }\
  ]
}
```

Example S3 access permission policy

```json
{
  "Version": "2012-10-17",
  "Statement": [\
    {\
      "Effect": "Allow",\
      "Action": ["s3:GetObject"],\
      "Resource": ["arn:aws:s3:::<S3-bucket>/<S3-prefix>/*"]\
    },\
    {\
      "Effect": "Allow",\
      "Action": ["s3:PutObject"],\
      "Resource": ["arn:aws:s3:::<S3-bucket>/<S3-prefix>/*.data.tar"]\
    }\
  ]
}
```

### S3 buckets with KMS encryption [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/cloud\#kms-encryption "Direct link to S3 buckets with KMS encryption")

If the S3 bucket that stores Amazon Bedrock model invocation logs is encrypted with an AWS KMS customer-managed key:

- Allow Amazon Bedrock to generate data keys when writing encrypted log files to the bucket.
- Allow the Lambda function's execution role to decrypt log files when reading them.

In the AWS Management Console:

1. Open the **KMS** service and select the S3 bucket's encryption key.

2. Click **Key policy**, then click **Edit**.

3. Add these statements to the `Statement` array in the key policy.
Replace the placeholders with your AWS account ID, region, and Lambda function's execution role name:





```json
{
     "Effect": "Allow",
     "Principal": {
       "Service": "bedrock.amazonaws.com"
     },
     "Action": "kms:GenerateDataKey",
     "Resource": "*",
     "Condition": {
       "StringEquals": {
         "aws:SourceAccount": "<AWS-account-id>"
       },
       "ArnLike": {
         "aws:SourceArn": "arn:aws:bedrock:<AWS-region>:<AWS-account-id>:*"
       }
     }
},
{
     "Effect": "Allow",
     "Principal": {
       "AWS": "arn:aws:iam::<AWS-account-id>:role/service-role/<Lambda-function-role>"
     },
     "Action": [\
       "kms:Decrypt",\
       "kms:DescribeKey"\
     ],
     "Resource": "*"
}
```

4. Save the key policy.


### Add trigger to Lambda function [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/cloud\#add-trigger-to-lambda-function "Direct link to Add trigger to Lambda function")

On the Lambda function page:

1. Click the **Configuration** tab, then click **Triggers** in the left sidebar.
2. Click **Add trigger**.
3. Select **S3** as the trigger source.
4. In the **Bucket** field, select the S3 bucket you configured for Amazon Bedrock model invocation logs.
5. In the **Event type** field, select `All object create events`.
6. In the **Prefix** field, enter the prefix you configured for Bedrock logs; for example: `bedrock-logs/`.
7. In the **Suffix** field, enter `.gz`.
8. Select the checkbox under **Recursive invocation** to acknowledge the warning.
9. Click **Add**.

## Test collector [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/cloud\#test-collector "Direct link to Test collector")

To test the collector deployment, open the **Amazon Bedrock** service in the AWS Management Console. Invoke a model in **Test** \> **Playground**.
If the configuration is correct, events appear in the AIDR logs within a few minutes.

You can view the Lambda function’s invocation metrics and logs in its **Monitor** tab.

## Troubleshooting [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/cloud\#troubleshooting "Direct link to Troubleshooting")

If new events don't appear in the AIDR console, go to the Lambda function's **Monitor** tab and click **View CloudWatch logs**.

The CloudWatch logs show the Lambda function sending a presigned URL to AIDR and receiving a `202 Accepted` response.
If you see `403 Forbidden` responses, verify the API key and AIDR API base URL in the Lambda function's environment variables.

To check the status of an asynchronous request, send a `GET` request to the URL returned in the `result.location` field of the `202` response.
Authorize the request with the collector's API key as a Bearer token.

Example cURL to check request status

```bash
curl --location 'https://api.crowdstrike.com/aidr/aiguard/request/prq_dioqsgbojz5rg3xkqydahqer3vupl74i' \
--header 'Authorization: Bearer pts_xx7rw2o...iaq63oo'
```

Example successful response

```output
{
  "request_id": "prq_dioqsgbojz5rg3xkqydahqer3vupl74i",
  "request_time": "2025-09-23T17:34:04.118110Z",
  "response_time": "2025-09-23T17:34:04.333419Z",
  "status": "Success",
  "summary": "Successfully processed the CSP logs",
  "result": {}
}
```

A `Success` status confirms that AIDR retrieved the logs from the presigned URL.

- [AWS Collector](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/cloud#aws-collector)
- [Requirements](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/cloud#requirements)
- [Register collector](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/cloud#register-cloud-collector)
- [Deploy collector](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/cloud#deploy-collector)
  - [Enable Amazon Bedrock model invocation logging to S3](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/cloud#enable-amazon-bedrock-model-invocation-logging-to-s3)
  - [Create Lambda function to forward events to AIDR](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/cloud#create-lambda-function-to-forward-events-to-aidr)
  - [Add permissions to Lambda function role](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/cloud#add-permissions-to-lambda-function-role)
  - [S3 buckets with KMS encryption](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/cloud#kms-encryption)
  - [Add trigger to Lambda function](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/cloud#add-trigger-to-lambda-function)
- [Test collector](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/cloud#test-collector)
- [Troubleshooting](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/cloud#troubleshooting)
