For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/compliance/app-embedded-scanning.md).

App-Embedded Defenders can scan their workloads for compliance issues.

App-Embedded Defender support the following types of compliance checks:

- Image compliance checks.

- Custom compliance checks.


To see compliance scan reports, go to **Monitor > Compliance > Images > Deployed**. You can filter the table by:

- **App-Embedded: Select** — Narrows the results to just images protected by App-Embedded Defenders.

- **App ID** — Narrows the list to specific images. App IDs are listed under the table’s **Apps** column.











For ECS Fargate tasks, the [App ID](https://docs.prismacloud.io/admin-guide/install/deploy-defender/app-embedded/install-app-embedded-defender-fargate#app-id-fargate) is partially constructed from the task name. AWS Fargate tasks can run multiple containers. All containers in a Fargate task have the same App ID.











For all other workloads protected by App-Embedded Defender, the [App ID](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/compute-edition/34/admin-guide/install/deploy-defender/app-embedded/app-embedded.md#app-id) is partially constructed from app name, which is a deploy-time configuration set in the App ID field of the embed workflow.


You can use wildcards to filter the table by app/image name. For example, if the app name is `dvwa`, then you could find all deployments with `Repository: dvwa*`. This filter would show `dvwa:0438dc81a9144fab8cf09320b0e1922b` and `dvwa:538359b5f7f54559ab227375fe68cd7a`.

## Create compliance rules[Direct link to heading](https://docs.prismacloud.io/admin-guide/compliance/app-embedded-scanning\#create-compliance-rules)

Create a compliance rules for workloads protected by App-Embedded Defender.

1. Login to the Console.

2. Go to **Defend > Compliance > Containers and images > Deployed**.

3. Click **Add rule**.

4. Enter a rule name.

5. Click on **Scope** to select a relevant collection, or create a new collection.











Workloads are scoped by App ID. App ID is specified when you embed the App-Embedded Defender into a workload, and represents a unique identifier for the Defender/workload pair.









1. If creating a collection, click **Add collection**.

2. Enter collection name.

3. In the **App ID** field, enter one or more App IDs.











      Postfix wildcards are supported.

4. Click **Save**.

5. Select the new collection.

6. Click **Select collection**.


6. Click **Save**.











The block action doesn’t apply to App-Embedded workloads.


## Supported compliance checks[Direct link to heading](https://docs.prismacloud.io/admin-guide/compliance/app-embedded-scanning\#supported-compliance-checks)

App-Embedded Defenders support the following built-in image compliance checks:

- **448: Package binaries should not be altered** — Checks the integrity of package binaries in an image. During an image scan, every binary’s checksum is compared with its package info.

- **424: Sensitive information provided in environment variables** — Checks if images contain sensitive information in their environment variables.

- **425: Private keys stored in image** — Searches for private keys stored in an image or serverless function.

- **426: Image contains binaries used for crypto mining** — Detects when there are crypto miners in an image. Attackers have been quietly poisoning registries and injecting crypto mining tools into otherwise legitimate images.


App-Embedded Defenders also support [custom compliance checks](https://docs.prismacloud.io/admin-guide/compliance/custom-compliance-checks). Custom compliance checks let you write and run your own compliance checks to assess, measure, and enforce your own security baselines. Custom checks only work for workloads that allow users with root privileges.

## Deploy an example Fargate task[Direct link to heading](https://docs.prismacloud.io/admin-guide/compliance/app-embedded-scanning\#deploy-an-example-fargate-task)

Deploy the `fargate-vulnerability-compliance-task` Fargate task. Follow the steps in [Embed App-Embedded Defender into Fargate tasks](https://docs.prismacloud.io/admin-guide/install/deploy-defender/app-embedded/install-app-embedded-defender-fargate).

You can use the following task definition to test Prisma Cloud’s App-Embedded Defender. It’s based on an Ubuntu 18.04 image. On start up, it runs the `/bin/sh -c 'cp /bin/sleep /tmp/xmrig` command to trigger the compliance check that detects crypto miners in images.

AskCopy

```
{
  "containerDefinitions": [\
     {\
        "command": [\
           "/bin/sh -c 'cp /bin/sleep /tmp/xmrig && echo \"[+] Sleeping...\" && while true; do sleep 1000 ; done'"\
        ],\
        "entryPoint": [\
           "sh",\
           "-c"\
        ],\
        "essential": true,\
        "image": "ubuntu:18.04",\
        "logConfiguration": {\
           "logDriver": "awslogs",\
           "options": {\
              "awslogs-group" : "/ecs/fargate-task-definition",\
              "awslogs-region": "us-east-1",\
              "awslogs-stream-prefix": "ecs"\
           }\
        },\
        "name": "Fargate-vul-comp-test",\
        "portMappings": [\
           {\
              "containerPort": 80,\
              "hostPort": 80,\
              "protocol": "tcp"\
           }\
        ]\
     }\
  ],
  "cpu": "256",
  "executionRoleArn": "arn:aws:iam::012345678910:role/ecsTaskExecutionRole",
  "family": "fargate-vulnerability-compliance-task",
  "memory": "512",
  "networkMode": "awsvpc",
  "requiresCompatibilities": [\
      "FARGATE"\
   ]
}
```

## Review compliance scan reports[Direct link to heading](https://docs.prismacloud.io/admin-guide/compliance/app-embedded-scanning\#review-compliance-scan-reports)

Review the scan results in Console.

For Fargate version 1.3.0 and older, Prisma Cloud shows only a single scan report if the same image is run simultaneously as:

- A task on ECS Fargate, protected by App-Embedded Defender.

- A container on a host, protected by Container Defender.


In this case, the image is categorized as "App-Embedded". As a result, when the scan report table is filtered by **App-Embedded: Select**, a scan report will be shown. When the table is filtered by **App-Embedded: Exclude**, it will be hidden. And when filtering by **Hosts**, it will be hidden, even if the host matches, because the image is considered as App-Embedded.

For Fargate version 1.4.0, two separate scan reports are shown, one for App-Embedded and one for Container Defender.

1. Navigate to **Monitor > Compliance > Images > Deployed** and validate that the deployed image appears with an alerted compliance check.

2. To see all images protected by App-Embedded Defender, filter the table by **App-Embedded: Select**.

3. If you deployed the example Fargate task, search for `fargate-vulnerability-compliance-task`.

4. Click on the image to view image details:











The **Apps** column shows a count of the number of running containers protected by App-Embedded Defender.











The **Layers**, **Process info**, **Labels**, **Runtime**, and **Trust groups** tabs aren’t supported for images scannned by App-Embedded Defenders.









1. Click the **Compliance** tab to review compliance issues.











      You should seen an issue for **Image contains binaries used for crypto mining**.















      ![fargate image comp scan result](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-b61ed7fb9bef3e1cefa761059bf768403139f418%252Ffargate_image_comp_scan_result.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=8f6577ddc1adce11e7737412c89249c0&sv=3)

2. Review runtime information for the container.











      Go to the **Environment > Apps** tab, and then click on the app in the table to open the App-Embedded observations. You can bring up the same view by going directly to **Monitor > Runtime > App-Embedded observations**, and clicking on the same app.















      ![app embedded scanning observations](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-d4dce0674c9e90fe1453fc7f1346e9e24dee634e%252Fapp_embedded_scanning_observations.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=1e9df73d83b1d354198cb270f5ff8cd5&sv=3)











      The **Environment** tab shows cloud-provider metadata that App-Embedded Defender collected about the running container. For more information about the type of cloud-provider metadata App-Embedded Defender can collect, see [Monitoring workloads at runtime](https://docs.prismacloud.io/admin-guide/runtime-defense/runtime-defense-app-embedded#cloud-metadata).















      ![app embedded scanning metadata](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-8dd0bb6d25483a49e5b3eafdbf889c6d4a39471f%252Fapp_embedded_scanning_metadata.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=68bf657411ee7aba712740c662ea1b26&sv=3)


[PreviousVM image scanning](https://docs.prismacloud.io/admin-guide/compliance/vm-image-scanning) [NextDetect secrets](https://docs.prismacloud.io/admin-guide/compliance/detect-secrets)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
