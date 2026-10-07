For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/install/deploy-defender/serverless/install-serverless-defender-layer.md).

Prisma Cloud Serverless Defenders protect serverless functions at runtime. Currently, Prisma Cloud supports AWS Lambda functions.

Lambda layers are ZIP archives that contain libraries, custom runtimes, or other dependencies. Layers let you add reusable components to your functions, and focus deployment packages on business logic. They are extracted to the _/opt_ directory in the function execution environment. For more information, see the [AWS Lambda layers documentation](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html).

Prisma Cloud delivers Serverless Defender as a Lambda layer. Deploy Serverless Defender to your function by wrapping the handler and setting an environment variable.

## Secure the Serverless Functions[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/serverless/install-serverless-defender-layer\#secure-the-serverless-functions)

To secure an AWS Lambda function with the Serverless Defender layer:

1. Download the Serverless Defender Lambda layer ZIP file.

2. Upload the layer to AWS.

3. Define a serverless protection runtime policy.

4. Define a serverless WAAS policy.

5. Add the layer to your function, update the handler, and set an environment variable. After completing this integration, Serverless Defender runs when your function is invoked.


## Download the Serverless Defender Layer[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/serverless/install-serverless-defender-layer\#download-the-serverless-defender-layer)

Download the Serverless Defender layer from Compute Console.

1. Open Console, then go to **Manage > Defenders > Deploy> Defenders > Single Defender**.

2. Choose the DNS name or IP address that Serverless Defender uses to connect to Console.

3. Set the Defender type to **Serverless Defender**.

4. Select a runtime.











Prisma Cloud supports Lambda layers for **Node.js**, **Python**, **Ruby**, **C#**, and **Java**. See [system requirements](https://docs.prismacloud.io/admin-guide/install/system-requirements#serverless-runtimes) for the runtimes that are supported for Serverless Defender as a Lambda layer.

5. For **Deployment Type**, select **Layer**.

6. Download the Serverless Defender layer. A ZIP file is downloaded to your host.


## Upload the Serverless Defender layer to AWS[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/serverless/install-serverless-defender-layer\#upload-the-serverless-defender-layer-to-aws)

Add the layer to the AWS Lambda service as a resource available to all functions.

1. In the AWS Management Console, go to the Lambda service.

2. Select **Layers > Create Layer**.















![serverless layer layers](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-a71d0ad7eda5a3a73ba04dd80d8d19fbc0a90155%252Fserverless_layer_layers.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=20c83c99ca5f05abc3e5f2a58807a79c&sv=3)

3. In **Name**, enter **twistlock**.

4. Click **Upload**, and select the file you just downloaded, _twistlock\_defender\_layer.zip_









1. Select the compatible runtimes: **Python**, **Node.js**, **\*Ruby**, **C#**, or **Java**.

2. Click **Create**.















      ![serverless layer create](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-edef636bd7978112cb522ccbf2488899dede96ae%252Fserverless_layer_create.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=f344173ecd56a50f47e04b2f3f033d91&sv=3)


## Define your Runtime Protection Policy[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/serverless/install-serverless-defender-layer\#define-your-runtime-protection-policy)

By default, Prisma Cloud ships with an empty serverless runtime policy. An empty policy disables runtime defense entirely.

You can enable runtime defense by creating a rule. By default, new rules:

- Apply to all functions (`*`), but you can target them to specific functions by function name.

- Block all processes from running except the main process. This protects against command injection attacks.


When functions are invoked, they connect to Compute Console and retrieve the latest policy. To ensure that functions start executing at time=0 with your custom policy, you must predefine the policy. Predefined policy is embedded into your function along with the Serverless Defender by way of the `TW_POLICY` environment variable.

1. Log into Prisma Cloud Console.

2. Go to **Defend > Runtime > Serverless Policy**.

3. Click **Add rule**.

4. In the **General** tab, enter a rule name.

5. (Optional) Target the rule to specific functions.

6. Set the rule parameters in the **Processes**, **Networking**, and **File System** tabs.

7. Click **Save**.


## Define your Serverless WAAS Policy[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/serverless/install-serverless-defender-layer\#define-your-serverless-waas-policy)

Prisma Cloud lets you protect your serverless functions against application layer attacks by utilizing the serverless [Web Application and API Security (WAAS)](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/compute-edition/34/admin-guide/waas/waas.md).

By default, the serverless WAAS is disabled. To enable it, add a new serverless WAAS rule.

1. Log into Prisma Cloud Console.

2. Go to **Defend > WAAS > Serverless**.

3. Click **Add rule**.

4. In the **General** tab, enter a rule name.

5. (Optional) Target the rule to specific functions.

6. Set the protections you want to apply ( **SQLi**, **CMDi**, **Code injection**, **XSS**, **LFI**).

7. Click **Save**.


## Embed the Serverless Defender[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/serverless/install-serverless-defender-layer\#embed-the-serverless-defender)

Embed the Serverless Defender as a layer, and run it when your function is invoked. If you are using a deployment framework such as [SAM](https://aws.amazon.com/blogs/compute/working-with-aws-lambda-and-lambda-layers-in-aws-sam/) or [Serverless Framework](https://serverless.com/framework/docs/providers/aws/guide/layers#using-your-layers) you can reference the layer from within the configuration file.

**Prerequisites:**

- You already have a Lambda function.

- Your Lambda function is written for Node.js, Python, or Ruby.

- Your function’s execution role grants it permission to write to CloudWatch Logs. Note that the **AWSLambdaBasicExecutionRole** grants permission to write to CloudWatch Logs.


1. Go to the function designer in the AWS Management Console.

2. Click on the **Layers** icon.















![serverless layer function designer layers](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-4a643672f3af30f0b44fa8b6273afcd56a2c417d%252Fserverless_layer_function_designer_layers.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=7930fbcd9ca905cd8de059b0f1853465&sv=3)

3. In the **Referenced Layers** panel, click **Add a layer**.















![serverless layer add a layer](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-7537c0a59397652f726687bfece9557a88691aca%252Fserverless_layer_add_a_layer.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=81a2b2aa289068c55e03d9ecf561f8ba&sv=3)









1. In the **Select from list of runtime compatible layers**, select **twistlock**.

2. In the **Version** drop-down list, select **1**.

3. Click **Add**.















      ![serverless layer add a layer2](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-0b198a57c6b7eb38bac86f54b2f4de29e8a9969a%252Fserverless_layer_add_a_layer2.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=77dfee20c6844f92424d010b60c0adeb&sv=3)











      When you return to the function designer, you’ll see that your function now uses one layer.















      ![serverless layer function designer layers2](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-db20f745e042958851658d5f956963982751138e%252Fserverless_layer_function_designer_layers2.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=e8eceee56b4b432be2e73a000a2773f6&sv=3)


4. Update the handler for your function to be _twistlock.handler_.















![lambda handler](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-c4f94b05f77b49939caaf273fbfddbb29fba5a98%252Flambda_handler.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=dbf5bbde0ec93952cd10f58a3495a8a6&sv=3)

5. Set the _TW\_POLICY_ and _ORIGINAL\_HANDLER_ environment variable, which specifies how your function connects to Compute Console to retrieve policy and send audits.









1. In Compute Console, go to **Manage > Defenders > Deploy > Single Defender**.

2. For **Defender type**, select **Serverless**.

3. In **Set the Twistlock environment variable**, enter the function name and region.

4. Copy the generated **Value**.

5. In AWS Console, open your function in the designer, and scroll down to the **Environment variables** panel.

6. For **Key**, enter TW\_POLICY.

7. For **Value**, paste the rule you copied from Compute Console.

8. For _ORIGINAL\_HANDLER_, this is the original value of handler for your function before your modification.


6. Click **Save** to preserve all your changes.















![lambda env variables](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-e7f62758ff71f2c44f8ffceb7bfa6ab391d9ae26%252Flambda_env_variables.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=f0023fb93d67af9b55607b6e2885ba15&sv=3)


[PreviousDeploy Serverless Defender](https://docs.prismacloud.io/admin-guide/install/deploy-defender/serverless) [NextAuto-defend serverless functions](https://docs.prismacloud.io/admin-guide/install/deploy-defender/serverless/auto-defend-serverless)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
