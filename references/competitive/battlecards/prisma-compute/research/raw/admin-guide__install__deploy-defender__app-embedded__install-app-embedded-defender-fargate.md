For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/install/deploy-defender/app-embedded/install-app-embedded-defender-fargate.md).

App-Embedded Defenders for Fargate monitor and protect your Fargate tasks to ensure they execute as designed.

To learn when to use App-Embedded Defenders, see [Defender types](https://docs.prismacloud.io/admin-guide/install/deploy-defender/defender-types).

To learn more about App-Embedded Defender’s capabilities, see:

- [Vulnerability scanning for App-Embedded](https://docs.prismacloud.io/admin-guide/vulnerability-management/app-embedded-scanning)

- [Compliance scanning for App-Embedded](https://docs.prismacloud.io/admin-guide/compliance/app-embedded-scanning)

- [Runtime defense for App-Embedded](https://docs.prismacloud.io/admin-guide/runtime-defense/runtime-defense-app-embedded)

- Protecting front-end containers at runtime with [WAAS](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/compute-edition/34/admin-guide/waas/waas.md)


For front-end Fargate tasks, deploy the [WAAS](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/compute-edition/34/admin-guide/waas/waas.md) application firewall for additional runtime protection.

## Architecture[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/app-embedded/install-app-embedded-defender-fargate\#architecture)

When you embed the App-Embedded Defender into your Fargate task, Prisma Cloud modifies the task definition. The updated task definition includes a Prisma Cloud sidecar container. The sidecar container handles all communication with Console, including retrieving policies and sending audits. It also hosts the App-Embedded Defender binaries, which are shared with the task’s other containers through a shared volume. The embed process modifies each containerDefinition to:

- Mount the Prisma Cloud sidecar container’s shared volume to gain access to the App-Embedded Defender binaries.

- Start the original entrypoint command under the control of App-Embedded Defender.


App-Embedded Defenders do not communicate directly with Console. All communication is proxied through the Prisma Cloud sidecar container.

## App ID[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/app-embedded/install-app-embedded-defender-fargate\#app-id)

Each App-Embedded Defender deployed in an ECS Fargate task has an App ID that’s automatically generated during the embed flow. For ECS Fargate tasks, the App ID is constructed from the task name and an internally generated UUID. The format is:

AskCopy

```
<task-name>:<UUID>
```

This App ID is used throughout the Console UI. In particular, it’s listed in the **Apps** column of the vulnerability and compliance scan reports under **Monitor > Vulnerabilities > Images > Deployed** and **Monitor > Compliance > Images > Deployed**.

## WAAS for Fargate[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/app-embedded/install-app-embedded-defender-fargate\#waas-for-fargate)

All the capabilities of standard WAAS are available for Fargate tasks. The only difference is that Fargate Defenders run as a reverse proxies to all other containers in the task. As such, when you set up WAAS for Fargate, you must specify the exposed external port where Fargate Defender can listen, and the port (not exposed to the Internet) where your web application listens. WAAS for Fargate forwards the filtered traffic to your application port - _unless an attack is detected and you chose_ **Prevent** _in your WAAS for Fargate rule_.

For more information on the type of attacks that Prisma Cloud detects and prevents, see [Prisma Cloud WAAS](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/compute-edition/34/admin-guide/waas/waas.md).

## Securing Fargate tasks[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/app-embedded/install-app-embedded-defender-fargate\#securing-fargate-tasks)

To secure a Fargate task, embed the Prisma Cloud Fargate Defender into it. The steps are:

1. Define your policy in Prisma Cloud Console.











App-Embedded Defenders dynamically retrieve rules from Console as they are updated. You can embed the App-Embedded Defender into a task with a simple initial policy, and then refine it later, as needed.

2. Embed the Fargate Defender into your task definition.

3. Start the service.


When securing Fargate tasks with runtime rules and WAAS, target rules to tasks using the **Scope** fields. For runtime, create new collections or use already defined collections scoped by image and container name, as shown in the image below. Policy is applied per-container in the task.

![install app embedded defender fargate runtime rule scope](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-4070cdc9d8b9bc6e81e0356fecaa5ad87e71a1df%252Finstall_app_embedded_defender_fargate_runtime_rule_scope.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=1331a45f12c588a4559caeea282dc37b&sv=3)

For WAAS, scope rules by App ID. Policy is applied per-task. The WAAS firewall listens on a specific port, and since all containers run in the same network namespace, it applies to the entire task.

![install app embedded defender fargate waas scope](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-1efa196a05b8b29c66dbd47f47ba3458bc517e79%252Finstall_app_embedded_defender_fargate_waas_scope.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=27858e0f7ec01db1852025a635485623&sv=3)

## Task entrypoint[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/app-embedded/install-app-embedded-defender-fargate\#task-entrypoint)

When Prisma Cloud generates a protected task definition, it needs to know the container image’s `entryPoint` and/or `command` instructions. We override these values to first run the App-Embedded Defender, and then run the original `entryPoint`/`command` under Defender’s watch.

Setting the entrypoint in a task definition is optional. It’s only required when you want to override the image’s entrypoint as specified in its Dockerfile. As such, many task definitions don’t explicitly specify it. However, Prisma Cloud needs to know what it is, so it can run the original app under Defender’s control. To aid in embedding Defender into Fargate tasks without any manual intervention (i.e. updating task definitions to explicitly specify entrypoints), Prisma Cloud can automatically find the image’s entrypoint and set it up in the protected task definition.

Prisma Cloud can find the image’s entrypoint from:

- Registry scans. When Prisma Cloud scans an image from a registry, it saves the `entryPoint` and `command` parameters to the database. When embedding Defender into a task, Prisma Cloud searches the database to see if it’s seen the task’s image before. If so, it extracts the original entrypoint, and sets it up in the new protected task definition.

- Querying the registry directly. If the image hasn’t been scanned by the registry scanner, then you can point Prisma Cloud to the registry where the image lives, and Prisma Cloud can find and extract the entrypoint. Prisma Cloud supports the following registries:









  - AWS Elastic Container Registry (ECR).

  - Docker Registry v2.

  - JFrog Artifactory.


Automatically extracting the entrypoint using one of the methods described above is optional. It can be enabled or disabled when embedding Defender in a task definition.

The twistcli tool also supports entrypoint extraction when generating protected task definitions. For more information, see the help menu:

AskCopy

```
twistcli app-embedded generate-fargate-task --help
```

## Embedding App-Embedded Defender into Fargate tasks[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/app-embedded/install-app-embedded-defender-fargate\#embedding-app-embedded-defender-into-fargate-tasks)

Prisma Cloud cleanly separates the code developers produce from the Fargate containers we protect. Developers don’t need to change their code to accommodate Prisma Cloud. They don’t need to load any special libraries, add any files, or change any manifests. When a container is ready to be deployed to test or production, run your task definition through our transform tool to automatically embed the Fargate Defender, then load the new task definition into AWS.

The method for embedding the Fargate Defender was designed to seamlessly integrate into the CI/CD pipeline. You can call the Prisma Cloud API to embed the Fargate Defender into your task definition.

Prisma Cloud doesn’t support [Intrinsic functions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference.html) in AWS CloudFormation template.

**Prerequisites:**

- The task where you’re embedding the App-Embedded Defender can reach Console over the network.

- You have a task definition.

- You have already created an ECS cluster.

- Cluster VPC and subnets.

- Task role.

- Your image has a shell.


You can optionally run the Fargate Defender sidecar as a non-essential container. This configuration isn’t recommended because Defender’s goal is to ensure that tasks are always protected.

If you’ve configured Defender as a non-essential container and you’re having issues with your setup, first validate that Defender is running as expected before contacting Palo Alto Networks customer support. By setting Defender as non-essential, there is no guarantee that Defender is running, and validating that it’s running is the first step in debugging such issues.

## Supported task definition formats[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/app-embedded/install-app-embedded-defender-fargate\#supported-task-definition-formats)

Prisma Cloud supports the following task definition formats:

- Standard JSON format, as described [here](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definition_parameters.html).

- CloudFormation templates for `AWS::ECS::TaskDefinition` in JSON and YAML formats, as described [here](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskdefinition.html). You can use either just the task definition part of the CloudFormation template, or a full CloudFormation template.


**Example of a standard JSON format task definition:**

AskCopy

```
{
    "containerDefinitions": [\
        {\
            "name": "web",\
            "image": "nginx",\
            "entryPoint": [\
                "/http_server"\
            ]\
        }\
    ],
    "cpu": "256",
    "executionRoleArn": "arn:aws:iam::112233445566:role/ecsTaskExecutionRole",
    "family": "webserver",
    "memory": "512",
    "networkMode": "awsvpc",
    "requiresCompatibilities": [\
        "FARGATE"\
    ]
}
```

**Example of the equivalent task definition as a JSON CloudFormation template:**

AskCopy

```
{
  "Type" : "AWS::ECS::TaskDefinition",
  "Properties": {
      "ContainerDefinitions": [\
        {\
          "Name": "web",\
          "Image": "nginx",\
          "EntryPoint": [\
              "/http_server"\
          ]\
        }\
      ],
      "Cpu" : 256,
      "ExecutionRoleArn": "arn:aws:iam::112233445566:role/ecsTaskExecutionRole",
      "Family": "webserver",
      "Memory" : 512,
      "NetworkMode" : "awsvpc",
      "RequiresCompatibilities" : [\
          "FARGATE"\
      ]
    }
}
```

**Example of a full JSON CloudFormation template that includes a Fargate task definition:**

AskCopy

```
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Resources": {
    "fargateTaskDefinition": {
      "Type": "AWS::ECS::TaskDefinition",
      "Properties": {
        "ExecutionRoleArn": "arn:aws:iam::1234567891234:role/ecsTaskExecutionRole",
        "ContainerDefinitions": [\
          {\
            "Name": "test-server",\
            "Image": "1234567891234.dkr.ecr.us-east-1.amazonaws.com/user:ubuntu-test-server",\
            "MemoryReservation": "",\
            "Essential": true,\
            "PortMappings": [],\
            "Cpu": 256,\
            "Memory": 512,\
            "EntryPoint": [\
              "/http_server"\
            ],\
            "EnvironmentFiles": [],\
            "LogConfiguration": {\
              "LogDriver": "awslogs",\
              "Options": {\
                "awslogs-group": "/ecs/user-tracer-test",\
                "awslogs-region": "us-east-1",\
                "awslogs-stream-prefix": "ecs"\
              }\
            }\
          }\
        ],
        "Memory": "512",
        "TaskRoleArn": "arn:aws:iam::1234567891234:role/ecsTaskExecutionRole",
        "Family": "TASK-NAME",
        "RequiresCompatibilities": [\
          "FARGATE"\
        ],
        "NetworkMode": "awsvpc",
        "Cpu": "256",
        "InferenceAccelerators": [],
        "Volumes": [],
        "Tags": []
      }
    },
    "HelloLambdaRole": {
      "Type": "AWS::IAM::Role",
      "Properties": {
        "RoleName": "HelloLambdaRole1",
        "AssumeRolePolicyDocument": {
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
      }
    }
  }
}
```

**Example of a full YAML CloudFormation template that includes a Fargate task definition:**

AskCopy

```
AWSTemplateFormatVersion: "2010-09-09"
Resources:
  fargateTaskDefinition:
    Type: 'AWS::ECS::TaskDefinition'
    Properties:
      ExecutionRoleArn: 'arn:aws:iam::1234567891234:role/ecsTaskExecutionRole'
      ContainerDefinitions:
        - Name: test-server
          Image: >-
            1234567891234.dkr.ecr.us-east-1.amazonaws.com/user:ubuntu-test-server
          MemoryReservation: ''
          Essential: true
          PortMappings: []
          Cpu: 256
          Memory: 512
          EntryPoint:
            - /http_server
          EnvironmentFiles: []
          LogConfiguration:
            LogDriver: awslogs
            Options:
              awslogs-group: /ecs/user-tracer-test
              awslogs-region: us-east-1
              awslogs-stream-prefix: ecs
      Memory: '512'
      TaskRoleArn: 'arn:aws:iam::1234567891234:role/ecsTaskExecutionRole'
      Family: TASK-NAME
      RequiresCompatibilities:
        - FARGATE
      NetworkMode: awsvpc
      Cpu: '256'
      InferenceAccelerators: []
      Volumes: []
      Tags: []
  HelloLambdaRole:
    Type: 'AWS::IAM::Role'
    Properties:
      RoleName: HelloLambdaRole2
      AssumeRolePolicyDocument:
        Statement:
          - Effect: Allow
            Principal:
              Service: lambda.amazonaws.com
            Action: 'sts:AssumeRole'
```

## Embed App-Embedded Defender from the Console UI[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/app-embedded/install-app-embedded-defender-fargate\#embed-app-embedded-defender-from-the-console-ui)

You can create a protected task definition in the Console UI.

**Prerequisites:**

- You’ve already created an ECS cluster, cluster VPC, and subnets.

- You’ve already created a task role.

- You have a task definition.

- At runtime, your tasks can connect to Prisma Cloud Console over the network. Prisma Cloud Defender connects to Console to retrieve runtime policies and send audits.


1. Log into Prisma Cloud Console.

2. In **Deployment method**, select **Single Defender**.

3. Select the DNS name or IP address that App-Embedded Defender uses to connect to Console.











A list of IP addresses and hostnames is pre-populated in the drop-down list. If none of the items are valid, select the **Names** tab and add a new subject alternative name (SAN) using **Add SAN** button. After adding a SAN, your IP address or hostname will be available in the drop-down list in the **Deploy** tab.











Selecting an IP address in an evaluation setup is acceptable, but using a DNS name is more resilient. If you select Console’s IP address, and Console’s IP address changes, your Defenders will no longer be able to communicate with Console.

4. In **Defender type**, select **Container Defender - App-Embedded**.

5. In **Enable file system runtime protection**, set the toggle to **On** if your runtime policy requires it.











If App-Embedded Defender is deployed with this setting turned on, the sensor will monitor file system events, regardless of how your runtime policy is configured, and could impact the underlying workload’s performance.











If you later decide you want to disable the sensor completely, you must re-embed App-Embedded Defender with this setting turned off.











Conversely, if you deploy App-Embedded Defender with this setting disabled, and later decide you want file system protection, you’ll need to re-embed App-Embedded with this setting enabled.











You can specify the [default setting](https://docs.prismacloud.io/admin-guide/install/deploy-defender/app-embedded/config-app-embedded-fs-protection) for this toggle so it’s set the same way for all App-Embedded Defender deployments.

6. In **Deployment type**, select **Fargate task**.

7. Set up the task’s entrypoint.











If your task definition doesn’t explicitly specify an entrypoint, Prisma Cloud can automatically determine how to set it to start the image’s app under App-Embedded Defender’s control.











If you don’t enable any of the following options and your task definition doesn’t specify an entrypoint, you must update your task definition to include matching `entryPoint` and `command` parameters from the Dockerfile(s) of the image(s) in your task. Because Prisma Cloud won’t see the actual images as part of the embedding flow, it depends on having these parameters present to insert the App-Embedded Defender into the task startup flow.









1. Enable **Automatically extract entrypoint**.











      Prisma Cloud finds the image and its entrypoint in the registry scan results.











      If you have enabled **Automatically extract entrypoint**, you must remove the `command` and `entryPoint` fields in your task definition or CloudFormation template for each of the containers that you prefer, for the auto entrypoint extraction to take effect.

2. (Optional) Tell Prisma Cloud where it can find the image.











      If Prisma Cloud hasn’t scanned the image, you can point it to the registry where the image resides. Prisma Cloud will find the image and extract its entrypoint.











      Specify the registry type and pick the credential Prisma Cloud can use to access the registry.


8. Embed the Fargate Defender into your task definition.









1. Set **Template type** according to the format used to specify your task definition.









      - **Native Fargate** — Standard JSON format, as described [here](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definition_parameters.html).

      - **CloudFormation** — CloudFormation template for `AWS::ECS::TaskDefinition`, as described [here](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskdefinition.html).


2. Copy and paste your task definition into the left-hand box.

3. Click **Generate protected task**.

4. Copy the updated task definition from the right-hand box, and use it to create a new task definition in AWS.











      The newly generated task definition always uses the version of Defender that matches the Console from which you are generating the task definition. The task definition includes a complete configuration, such as volumes, startup dependencies, entrypoint, healthchecks for its successful execution. Therefore, manually changing the Defender version label in the task is not supported.


## Embed App-Embedded Defender with twistcli[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/app-embedded/install-app-embedded-defender-fargate\#embed-app-embedded-defender-with-twistcli)

The twistcli command line tool lets you embed App-Embedded Defender into Fargate task definitions.

**Prerequisites:**

- You’ve already created an ECS cluster, cluster VPC, and subnets.

- You’ve already created a task role.

- You have a task definition.

- Running tasks can connect to Prisma Cloud Console over the network. Prisma Cloud Defender connects to Console to retrieve runtime policies and send audits.


1. Log into Prisma Cloud Console.

2. Run twistcli to embed Defender into the task definition.

















AskCopy



```
$ twistcli app-embedded generate-fargate-task \
     --user <USER> \
     --address "<CONSOLE_URL>" \
     --console-host "<CONSOLE_ADDR>" \
     --output-file "protected_taskdef.json" \
     taskdef.json
```









If your task definition file is specified as a CloudFormation template, then add the `--cloud-formation` option to the twistcli command. You can use JSON or YAML formats in CloudFormation template.









   - `<USER>` — Prisma Cloud user with the role of Defender Manager or higher.

   - `<CONSOLE_URL>` — [RFC 1808 scheme and netloc](https://www.rfc-editor.org/rfc/rfc1808.html#section-2.1) for Console. twistcli uses this value to connect to Console to submit the task definition for embedding Defender. Example: https://127.0.0.1:8083

   - `<CONSOLE_ADDR>` — [RFC 1738 host](https://www.rfc-editor.org/rfc/rfc1738#section-3.1) where Console runs. This value will be the fully qualified domain name of the network host, or IP address, where Console runs. This value configures how the embedded Defender connects to Console.


## Creating a task definition in AWS[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/app-embedded/install-app-embedded-defender-fargate\#creating-a-task-definition-in-aws)

Create a new task definition in AWS with the output from the previous section. If you already have an existing task definition, create a new revision.

1. Log into the AWS Management Console.

2. Go to **Services > ECS**.

3. Click **Task Definitions**, then click **Create new Task Definition**.









1. Select **Fargate**, then click **Next step**.

2. Scroll to the bottom of the page, and click **Configure via JSON**.

3. Delete the prepopulated JSON, then paste the JSON generated for task from the previous section.

4. Click **Save**.


4. Validate task content.









1. Task name should be as described in the JSON.

2. Select the **Task Role**.

3. The task should include the **TwistlockDefender** container.

4. Click **Create**.

5. Click **View task definition**.


## Testing the task[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/app-embedded/install-app-embedded-defender-fargate\#testing-the-task)

1. Log into the AWS Management Console.

2. Go to **Services > ECS**.

3. Click **Clusters**, then select one of your Fargate cluster.

4. Click the **Services** tab, then click **Create**.









1. For **Launch type**, select **Fargate**.

2. For **Task Definition**, select your pre-defined task.

3. Enter a **Service name**.

4. For **Number of tasks**, enter **1**.

5. Click **Next step**.

6. Select a **Cluster VPC** and **Subnets**, then click **Next step**.

7. For **Service Auto Scaling**, select **Do not adjust the service’s desired count**, then click **Next step**.

8. Review your settings, then click **Create Service**.


5. Validate the results.









1. Click **View Service**.

2. When Last status is Running, your Fargate task is running.

3. The containers are running.


## Connected Defenders[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/app-embedded/install-app-embedded-defender-fargate\#connected-defenders)

To narrow the list to just App-Embedded Defenders, filter the table by type `Type: Container Defender - App-Embedded`. To see the list of Fargate tasks protected by App-Embedded Defender, filter the table by `Type: Fargate`.

![connected app embedded defenders](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-9a49fe83c9410f7fa25f321ade00e82f4ff4f746%252Fconnected_app_embedded_defenders.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=7f9eafed4355993183fd563ef24da477&sv=3)

By default, Prisma Cloud removes disconnected App-Embedded Defenders from the list after an hour. As part of the cleanup process, data collected by the disconnected Defender is also removed from **Monitor > Runtime > App-Embedded observations**.

## Jenkins Fargate example[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/app-embedded/install-app-embedded-defender-fargate\#jenkins-fargate-example)

Passing the Fargate task definition to your Prisma Cloud Console’s API returns the Prisma Cloud protected Fargate task definition. Use this task definition to start Prisma Cloud protected Fargate containers. This example demonstrates using the Jenkins Pipeline build process to:

- Call the Prisma Cloud Console’s API endpoint for Fargate task creation.

- Pass the Fargate task definition to the API.

- Capture the returned Prisma Cloud protected Fargate task definition.

- Save the Prisma Cloud protected Fargate task definition within the Pipeline’s archive https://<jenkins>/job/<pipeline\_name>/<job#>/artifact/tw\_fargate.json


In this example, a simple task _fargate.json_ and _Jenkinsfile_ have been placed in a GitHub repository.

![fargate jenkins repo](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-89200e3c3e0d5c534995a5b8f5aa50f73d26d070%252Ffargate_jenkins_repo.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=6c5eb0f9b6f9f2ca754d43870b51a775&sv=3)

AskCopy

```
{
  node {

      stage('Clone repository') {
          checkout scm
      }

      stage('Fargate Task call') {
          withCredentials([usernamePassword(credentialsId: 'twistlockDefenderManager', passwordVariable: 'TL_PASS', usernameVariable: 'TL_USER')]) {
              sh 'curl -s -k -u $TL_USER:$TL_PASS https://$TL_CONSOLE/api/v1/defenders/fargate.json?consoleaddr=$TL_CONSOLE -X POST -H "Content-Type:application/json" --data-binary "@fargate.json" | jq . > tw_fargate.json'
              sh 'cat tw_fargate.json'
          }
      }

      stage('Publish Function') {
          archiveArtifacts artifacts: 'tw_fargate.json'}
  }
}
```

1. Create an account in Prisma Cloud with the Defender Manager role.

2. Create a Jenkins username/password credential for this account called **twistlockDefenderManager**.

3. The **$TL\_Console** Jenkins global variable was defined when the Prisma Cloud Jenkins plugin was installed.

4. Create a Jenkins Pipeline.









1. Definition: **Pipeline script from SCM**.

2. SCM: **Git**.

3. Repository URL: <path to repository that contains both the Jenkinsfile and fargate.json>.

4. Credentials: <credentials for repository>.

5. Script path: **Jenkinsfile**.

6. Save.


5. Run **Build Now**.















![fargate jenkins stage](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-58dbbd74edb0cdf7dbf8937a869e8fa16656b710%252Ffargate_jenkins_stage.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=b133f15e60f15a2ec8b5afe20fbbc63d&sv=3)

6. The tw\_fagate.json file will be within the archive of this build https://<jenkins>/job/<pipeline\_name>/<job#>/artifact/tw\_fargate.json.















![fargate jenkins archive](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-18a4afd13e66b656bbc6866c5109eef9fe0e18c7%252Ffargate_jenkins_archive.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=e63f462123c5bb42e1222423128d70dc&sv=3)


[PreviousDeploy App-Embedded Defender](https://docs.prismacloud.io/admin-guide/install/deploy-defender/app-embedded) [NextDeploy App-Embedded Defender in ACI](https://docs.prismacloud.io/admin-guide/install/deploy-defender/app-embedded/deploy-app-embedded-defender-aci)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
