For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/alerts/aws-security-hub.md).

AWS Security Hub aggregates, organizes, and prioritizes security alerts from multiple AWS services and AWS Partner Network solutions, including Prisma Cloud, to give you a comprehensive view of security across your environment.

## Permissions[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/aws-security-hub\#permissions)

The minimum required permissions policy to integrate Prisma Cloud with AWS Security Hub is **AWSSecurityHubFullAccess**. Whether using IAM users, groups, or roles, be sure the entity Prisma Cloud uses to access AWS Security Hub has this minimum permissions policy.

This procedure shows you how to set up integration with an IAM user (configured as a service account). In AWS IAM, create a service account that has the **AWSSecurityHubFullAccess** permissions policy. You will need the service account’s access key ID and secret access key to integrate with Prisma Cloud.

## Enabling AWS Security Hub[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/aws-security-hub\#enabling-aws-security-hub)

1. Log into your AWS tenant and enter **Security Hub** in the **Find services** search, then select **Security Hub**.

2. Click **Enable Security Hub**.

3. Enable the Prisma Cloud integration.









1. Choose Integrations from the Security Hub menu.

2. Accept findings from Palo Alto Networks: Prisma Cloud Compute.











      See [AWS documentation](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-integrations-managing.html)


Note: Prisma Cloud integration with AWS Security Hub is not supported for US Gov Cloud regions.

## Configuring alert frequency[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/aws-security-hub\#configuring-alert-frequency)

You can configure the rate at which alerts are emitted. This is a global setting that controls the spamminess of the alert service. Alerts received during the specified period are aggregated into a single alert. For each alert profile, an alert is sent as soon as the first matching event is received. All subsequent alerts are sent once per period.

1. Open Console, and go to **Manage > Alerts**.

2. In **General settings**, select the default frequency for all alerts.











You can specify the following frequencies.









   - **10 Minutes**

   - **1 Hour**

   - **1 Day**.


## Sending alerts to Security Hub[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/aws-security-hub\#sending-alerts-to-security-hub)

Alert profiles specify which events should trigger the alert machinery, and to which channel alerts are sent. You can send alerts to any combination of channels by creating multiple alert profiles.

Alert profiles consist of two parts:

**(1) Alert settings — Who should get the alerts, and on what channel?** Configure Prisma Cloud to integrate with your messaging service and specify the people or places where alerts should be sent. For example, configure the email channel and specify a list of all the email addresses where alerts should be sent. Or for JIRA, configure the project where the issue should be created, along with the type of issue, priority, assignee, and so on.

**(2) Alert triggers — Which events should trigger an alert to be sent?** Specify which of the rules that make up your overall policy should trigger alerts.

![aws security hub config](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-cc8fd0304082548ffd1daa8c68e1132347befccd%252Faws_security_hub_config.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=8f5f8b0bb83134cb36d02db3cfed89c0&sv=3)

If you use multi-factor authentication, you must create an exception or app-specific password to allow Console to authenticate to the service.

## Create a new alert profile[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/aws-security-hub\#create-a-new-alert-profile)

1. In **Manage > Alerts**, click **Add profile**.

2. Enter a **Profile name**.

3. In **Provider**, select **AWS Security Hub**.

4. Click **Next**.


## Configure the triggers[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/aws-security-hub\#configure-the-triggers)

1. In **Select triggers**, select the events that should trigger an alert to be sent.

2. To specify specific rules that should trigger an alert, deselect **All rules**, and then select any individual rules.















![frag config triggers](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-f044b74e7910113b8b2440284017fa0fc2fcd3ae%252Ffrag_config_triggers.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=01361751c2394c9197d566bd8cc47ebc&sv=3)

3. Click **Next**.


## Configure the channel[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/aws-security-hub\#configure-the-channel)

After completing the steps in this procedure, you can use the AWS SQS integration configured in the Prisma platform to send compute workload alerts to AWS SQS.

1. In **Region**, select your region.

2. Enter your **Account ID**, which can be found in the AWS Management Console under **My Account > Account Settings**.

3. Select or create [credentials](https://docs.prismacloud.io/admin-guide/authentication/credentials-store/aws-credentials), which Prisma Cloud uses to integrate with AWS Security Hub.











You can use an IAM user, IAM role, or AWS STS.

4. Click **Next**.

5. Review the **Summary** and test the configuration by selecting **Send test alert**.

6. Click **Save**.


## Configure AWS SQS Integration[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/aws-security-hub\#configure-aws-sqs-integration)

Add AWS SQS integration in the Prisma Platform.

1. Create an [AWS SQS queue](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-setting-up.html).

2. Go to Prisma **SaaS > Settings > Integrations > Add Integration**.

3. Select **Amazon SQS**.









1. Enter the **Integration Name**.

2. Enter the **Queue URL** that you copied from the AWS SQS queue.

3. Under **More Options**, enter the credentials for **IAM Role** or **IAM Access Keys**.


4. **Test** to make sure that Prisma Cloud was successfully able to post a test message to your AWS SQS queue.















![add aws sqs integration](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-1b5e62bb9f249955109502f4ae268893a82b7c11%252Fadd-aws-sqs-integration.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=7be24e06ae31eb320e0b79cb1c5152a7&sv=3)


### Create an alert profile for AWS SQS in Prisma Console[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/aws-security-hub\#create-an-alert-profile-for-aws-sqs-in-prisma-console)

1. Go to **Compute > Manage > Alerts > Add profile**.

2. Enter the profile **Name**.

3. Select the **Provider** as **Prisma Cloud**.

4. Select your AWS SQS **Integration** that you created under **SaaS > Settings > Integrations > Add Integration**.

5. Select the **Triggers**.

6. Under **Settings** enter the custom JSON for the message payload.

7. You can **Send test alert** message and verify that the message was sent to the AWS queue.

8. Click **Save**.















![alert profile aws sqs](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-f788ff32b529654e1e75008d3e3800f4ed3a7fcc%252Falert-profile-aws-sqs.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=e93f557e79b03346abb4903489d9e413&sv=3)











This alert will be triggered based on your runtime policy settings under **Compute > Defend** policy settings, and the JSON payload message will be sent to the AWS SQS queue.















![alert message in aws sqs](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-5935b861125c8a96e0a888819ff8e8d1f3f89159%252Falert-message-in-aws-sqs.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=2bc3f585e01d9619d7e5abcab091a579&sv=3)















![alert message awssqs json body](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-7f931a461ef9e75fef504f5c6876dffa85b7ed70%252Falert-message-awssqs-json-body.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=d6805281b14c24225be213e7de1c60d0&sv=3)











**Limitations**









   - Additional SQS features such as associating attributes with the message, etc. can not be used as these capabilities are not supported by Prisma. In the case of SQS, Compute sends the SQS message payload through Prisma API.

   - Maximum allowed SQS message is 256kb. Messages larger than this limit won’t be sent to Prisma, instead a specific error will be written to the Compute console log.


[PreviousAlert mechanism](https://docs.prismacloud.io/admin-guide/alerts/alert-mechanism) [NextCortex XDR](https://docs.prismacloud.io/admin-guide/alerts/xdr)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
