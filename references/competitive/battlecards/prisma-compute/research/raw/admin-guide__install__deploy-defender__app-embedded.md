For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/install/deploy-defender/app-embedded.md).

App-Embedded Defenders monitor and protect your applications from the entrypoint script and all the entrypoint child processes to ensure they execute as designed. Deploy App-Embedded Defender anywhere you can run a container, but can’t deploy [Container Defender](https://docs.prismacloud.io/admin-guide/install/deploy-defender/defender-types#container-defender). App-Embedded Defenders are typically used to protect the entrypoint in applications in containers that run on container-on-demand services, such as Google Cloud Run (GCR) and Azure Container Instances (ACI).

To learn when to use App-Embedded Defenders, see [Defender types](https://docs.prismacloud.io/admin-guide/install/deploy-defender/defender-types).

To learn more about App-Embedded Defender’s capabilities, see:

- [Vulnerability scanning for App-Embedded](https://docs.prismacloud.io/admin-guide/vulnerability-management/app-embedded-scanning)

- [Compliance scanning for App-Embedded](https://docs.prismacloud.io/admin-guide/compliance/app-embedded-scanning)

- [Runtime defense for App-Embedded](https://docs.prismacloud.io/admin-guide/runtime-defense/runtime-defense-app-embedded)

- Protecting front-end containers at runtime with [WAAS](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/compute-edition/34/admin-guide/waas/waas.md)


App-Embedded Defender is the only supported option for securing containers at runtime when you’re using nested virtualization, also known as _Docker-in-Docker_. Docker-in-Docker is a setup where you have a Docker container that itself has Docker installed, and from within the container you use Docker to pull images, build images, run containers, and so on. To secure the applications inside a container, use App-Embedded Defender.

Using an app-embedded Defender requires the ability to interact with other processes. However, in containerized environments like Azure Container Instances (ACI), containers are often run with restricted permissions for enhanced security. For example, ACI places specific limitations, such as:

- Restricted support for certain system calls.

- Limited operations involving process access.


Furthermore, ACI does not allow for the granting of additional capabilities or the running of containers with elevated privileges. Consequently, the app-embedded Defender is most effective for straightforward applications and might not be suitable for more complex applications that require a database or have other advanced functionalities, such as digininja and DVWA.

## Securing Containers[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/app-embedded\#securing-containers)

To secure a container, embed the App-Embedded Defender into it. You can embed App-Embedded Defenders with the Console UI, twistcli, or Prisma Cloud API. App-Embedded Defender has been tested on Azure Container Instances, Google Cloud Run, and Fargate on EKS.

The steps are:

1. Define your policy in Prisma Cloud Console.











App-Embedded Defenders dynamically retrieve rules from Console as they are updated. You can embed the App-Embedded Defender into a task with a simple initial policy, and then refine it later, as needed.

2. Embed the App-Embedded Defender into the container.

3. Start the service that runs your container.


The embed process takes a Dockerfile as input, and returns a ZIP file with an augmented Dockerfile and App-Embedded Defender binaries. Rebuild your container image with the new Dockerfile to complete the embedding process. The embed process modifies the container’s entrypoint to run App-Embedded Defender. The App-Embedded Defender, in turn, runs the original entrypoint program under its control.

When embedding App-Embedded Defender, specify a unique identifier for your container image. This gives you a way to uniquely identify the App-Embedded Defender in the environment.

When securing your apps with runtime rules, target rules to apps using the App ID. (Because the App-Embedded Defender runs inside the container, it can’t reliably get information such as image and container names.)

![install app embedded defender scope app id](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-4d4f3bad993492602357121803c6b4faef4c7ad0%252Finstall_app_embedded_defender_scope_app_id.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=87576d930d701f230eca586f6e66ed9e&sv=3)

## App ID[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/app-embedded\#app-id)

When you deploy an App-Embedded Defender, it is embedded inside the container. The embed process modifies the container’s entrypoint to run App-Embedded Defender first, which in turn starts the original entrypoint program.

When App-Embedded Defender sends scan data back to Console, it must correlate it to an image. Because App-Embedded Defender runs inside the container, it can’t retrieve any information about the image, specifically the image name and image ID. As such, the deployment flow sets an image name and image ID, and embeds this information alongside the App-Embedded Defender.

During the embed flow, you must specify a value for App ID (or more accurately, app name, which becomes part of the final App ID). In the Console, this value is presented as the image name. When specifying App ID, choose a value you can easily trace back to the image when reviewing and mitigating security findings.

As part of the embed flow, Prisma Cloud automatically generates a universally unique identifier (UUID) to represent the image ID. The image ID is a primary key in the Prisma Cloud Compute database, so it’s essential that it is defined.

Together, the app name plus the generated UUID form the final App ID. The final App ID has the following format:

AskCopy

```
<app-name>:<uuid>
```

The following screenshot shows how images protected by App-Embedded Defender are listed under **Monitor > Vulnerabilities**. The **Repository** column, which represents the image name, shows two images: ian-app1 and ian-app2. Both ian-app1 and ian-app2 were specified as the App IDs when embedding Defenders into the images.

![install app embedded defender app id1](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-2743d5f9e483a5dde2af58306d663cf5ad6623fe%252Finstall_app_embedded_defender_app_id1.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=ffe3ce16f33576f2997d18347278a53c&sv=3)

The next screenshot shows the scan report for ian-app1. Notice that **Image** is set to **ian-app1**, which was the App ID specified when embedding Defender. Also notice that the value for **Image ID** is a UUID.

![install app embedded defender app id2](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-e228299d7800792b456fa5daef71ebc5b6778379%252Finstall_app_embedded_defender_app_id2.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=340959f66353bbbe1b3ed59ed0798d98&sv=3)

Finally, back in **Monitor > Vulnerabilities**, notice that the **Apps** column shows the final App ID, which is the combination of the app name (specified as App ID in the embed flow) plus the internally generated UUID.

![install app embedded defender app id3](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-3dbdfae7f1fc073e29c25bd220aeac8c541cf2f4%252Finstall_app_embedded_defender_app_id3.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=16ff3d42b261f89e4849dafe51a6d4c6&sv=3)

## Embed App-Embedded Defender[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/app-embedded\#embed-app-embedded-defender)

Embed App-Embedded Defender into a container image from Prisma Console UI.

**Prerequisites:**

- At runtime, the container where you’re embedding App-Embedded Defender can reach Console over the network. For Enterprise Edition, Defender talks to Console on port 443. For Compute Edition, Defender talks to Console on port 8084.

- You have the Dockerfile for your image.


01. Open Console, and go to **Manage > Defenders > Defenders: Deployed > Manual deploy**.

02. In **Deployment method**, select **Single Defender**.

03. Select the DNS name or IP address that App-Embedded Defender uses to connect to Console.

04. In **Choose the Defender type**, select **Container Defender - App-Embedded Defender**.

05. **Enable file system runtime protection** if your runtime policy requires it.











    If App-Embedded Defender is deployed with this setting enabled, the sensor will monitor file system events, regardless of how your runtime policy is configured, and could impact the underlying workload’s performance.











    If you later decide you want to disable the sensor completely, you must re-embed App-Embedded Defender with this setting disabled.











    Conversely, if you deploy App-Embedded Defender with this setting disabled, and later decide you want file system protection, you’ll need to re-embed App-Embedded with this setting enabled.











    You can set a [default file system protection state](https://docs.prismacloud.io/admin-guide/install/deploy-defender/app-embedded/config-app-embedded-fs-protection) for all App-Embedded Defender deployments.

06. In **Deployment type**, select **Dockerfile**.

07. In **App ID**, enter a unique identifier for the App-Embedded Defender.











    All vulnerability, compliance, and runtime findings for the container will be aggregated under this App ID In Console, the App ID is presented as the image name. Be sure to specify an App ID that lets you easily trace findings back to the image.

08. In **Dockerfile**, click **Choose File**, and upload the Dockerfile for your container image.











    **NOTE:** If your Dockerfile is based on a .NET image (example, `mcr.microsoft.com/dotnet/aspnet:8.0`) and you require filesystem monitoring, you must add the following environment variable to your Dockerfile: `ENV DOTNET_EnableDiagnostics=0`. This is necessary to resolve a conflict between the defender filesystem monitoring module and the .NET diagnostics component.

09. Click **Create embedded ZIP**.











    A file named _app\_embedded\_embed\_help.zip_ is created and downloaded to your system.

10. Unpack app\_embedded\_embed\_help.zip.

















    AskCopy



    ```
    $ mkdir tmp
    $ unzip app_embedded_embed_help.zip -d tmp/
    ```

11. Build the modified Docker image.

















    AskCopy



    ```
    $ cd tmp/
    $ docker build .
    ```

12. Tag and push the updated image to your repository.


## Embed App-Embedded Defender manually[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/app-embedded\#embed-app-embedded-defender-manually)

Embed App-Embedded Defender into a container image manually. Modify your Dockerfile with the supplied information, download the App-Embedded Defender binaries into the image’s build context, then rebuild the image.

**Prerequisites:**

- At runtime, the container where you’re embedding App-Embedded Defender can reach Console over the network. For Enterprise Edition, Defender talks to Console on port 443. For Compute Edition, Defender talks to Console on port 8084.

- The host where you’re rebuilding your container image with App-Embedded Defender can reach Console over the network on port 8083.

- You have the Dockerfile for your image.


1. Open Console, and go to **Manage > Defenders > Defenders: Deployed > Manual**.

2. In **Deployment method**, select **Single Defender**.

3. Select the DNS name or IP address that App-Embedded Defender uses to connect to Console.

4. In **Choose the Defender type**, select **Container Defender - App-Embedded Defender**.

5. Enable **Monitor file system events**, if your runtime policy requires it.











If App-Embedded Defender is deployed with this setting enabled, the sensor will monitor file system events, regardless of how your runtime policy is configured, and could impact the underlying workload’s performance.











If you later decide to disable the sensor completely, you must re-embed App-Embedded Defender with this setting disabled.











Conversely, if you deploy App-Embedded Defender with this setting disabled, and later decide you want file system protection, you’ll need to re-embed App-Embedded with this setting enabled.











You can set a [default file system protection state](https://docs.prismacloud.io/admin-guide/install/deploy-defender/app-embedded/config-app-embedded-fs-protection) for all App-Embedded Defender deployments.

6. In **Deployment Type**, select **Manual**.











A set of instructions for embedding App-Embedded Defender into your images is provided.









1. Using the provided curl command, download the App-Embedded Defender binary into your image’s build context directory.

2. Open your Dockerfile for editing.

3. Add the App-Embedded Defender to the image.

















      AskCopy



      ```
      ADD twistlock_defender_app_embedded.tar.gz /twistlock/
      ```

4. Add the specified environment variables.











      When setting `DEFENDER_APP_ID`, specify a value that lets you easily trace findings back to the image. All vulnerability, compliance, and runtime findings for the container will be aggregated under this App ID In Console, the App ID is presented as the image name.

5. Modify the entrypoint so that your app starts under the control of App-Embedded Defender.











      For example, to start the hello-world program under the control of App-Embedded Defender, specify the following entrypoint.

















      AskCopy



      ```
      ENTRYPOINT ["/twistlock/defender", "app-embedded", "hello-world"]
      ```


7. Rebuild your image.

















AskCopy



```
$ docker build .
```

8. Tag and push the updated image to your repository.


## Embed App-Embedded Defender with twistcli[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/app-embedded\#embed-app-embedded-defender-with-twistcli)

Prisma Cloud supports automation for embedding App-Embedded Defender into container images with either twistcli or the API. This section shows you how to use twistcli. To learn how to use the API, see the API docs.

**Prerequisites:**

- The container where you’re embedding App-Embedded Defender can reach Console’s port 8084 over the network.

- You have the Dockerfile for your image.


1. Download twistcli.









1. Log into Console, and go to **Manage > System > Utilities**.

2. Download the twistcli binary for your platform.


2. Generate the artifacts for an updated container with twistcli.











A file named _app\_embedded\_embed_ <app\_id>.zip\_ is created.

















AskCopy



```
$ ./twistcli app-embedded embed \
     --user <USER>
     --address "https://<CONSOLE>:8083" \
     --console-host <CONSOLE> \
     --app-id "<APP-ID>"  \
     --data-folder "<DATA-FOLDER>"  \
     Dockerfile
```







   - <USER> — Name of a Prisma Cloud user with a minimum [role](https://docs.prismacloud.io/admin-guide/authentication/user-roles) of Defender Manager.

   - <CONSOLE> — DNS name or IP address for Console.

   - <APP-ID> — Unique identifier. When setting `<APP-ID>`, specify a value that lets you easily trace findings back to the image. All vulnerability, compliance, and runtime findings for the container will be aggregated under this App ID. In Console, the App ID is presented as the image name. For example, _my-app_.

   - <DATA-FOLDER> — Readable and writable directory in the container’s filesystem. For example, _/tmp_.

   - To enable file system protection, add the `--filesystem-monitoring` flag to the twistcli command.


3. Unpack _app\_embedded\_embed\_help.zip_.

















AskCopy



```
$ mkdir tmp
$ unzip app_embedded_embed_help.zip -d tmp/
```

4. Build the updated image.

















AskCopy



```
$ cd tmp/
$ docker build .
```

5. Tag and push the updated image to your repository.


## Connected Defenders[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/app-embedded\#connected-defenders)

You can review the list of all Defenders connected to Console under **Manage > Defenders > Manage > Defenders**. To see just App-Embedded Defenders, filter the table by type, `Type: Container Defender - App-Embedded`.

![connected app embedded defenders](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-9a49fe83c9410f7fa25f321ade00e82f4ff4f746%252Fconnected_app_embedded_defenders.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=7f9eafed4355993183fd563ef24da477&sv=3)

By default, Prisma Cloud removes disconnected App-Embedded Defenders from the list after an hour. As part of the cleanup process, data collected by the disconnected Defender is also removed from **Monitor > Runtime > App-Embedded observations**.

There is an advanced settings dialog under **Manage > Defenders > Manage > Defenders**, which lets you configure how long Prisma Cloud should wait before cleaning up disconnected Defenders. This setting doesn’t apply to App-Embedded Defenders. Disconnected App-Embedded Defenders are always removed after one hour.

[PreviousAuto-defend serverless functions](https://docs.prismacloud.io/admin-guide/install/deploy-defender/serverless/auto-defend-serverless) [NextDeploy App-Embedded Defender for Fargate](https://docs.prismacloud.io/admin-guide/install/deploy-defender/app-embedded/install-app-embedded-defender-fargate)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
