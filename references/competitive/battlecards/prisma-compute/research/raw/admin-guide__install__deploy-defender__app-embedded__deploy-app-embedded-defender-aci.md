For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/install/deploy-defender/app-embedded/deploy-app-embedded-defender-aci.md).

Deploy an App-Embedded Defender in ACI to provide runtime protection to App-Embedded applications installed in ACI. The App-Embedded Defender enforces runtime policy on the application entrypoint and any child processes created by this entrypoint. To learn when to use App-Embedded Defenders, see [Defender types](https://docs.prismacloud.io/admin-guide/install/deploy-defender/defender-types).

To learn more about App-Embedded Defender’s capabilities, see:

- [Vulnerability scanning for App-Embedded](https://docs.prismacloud.io/admin-guide/vulnerability-management/app-embedded-scanning)

- [Compliance scanning for App-Embedded](https://docs.prismacloud.io/admin-guide/compliance/app-embedded-scanning)

- [Runtime defense for App-Embedded](https://docs.prismacloud.io/admin-guide/runtime-defense/runtime-defense-app-embedded)

- Protecting front-end containers at runtime with [WAAS](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/compute-edition/34/admin-guide/waas/waas.md)


## System Requirements[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/app-embedded/deploy-app-embedded-defender-aci\#system-requirements)

- ACI supports Linux containers

- App-Embedded Defender image is supported on Linux (x86) architecture

- Any Docker image with Prisma Cloud App-Embedded Defender binary.

- Azure Container Registry (ACR) (recommended)


## Configure App-Embedded Defender in Prisma Console UI[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/app-embedded/deploy-app-embedded-defender-aci\#configure-app-embedded-defender-in-prisma-console-ui)

Prisma Console provides you with an App-Embedded Defender bundle that contains the Dockerfile with App-Embedded configurations and the Defender installation binary file.

You can select one of the **Deployment types**: Dockerfile or Manual.

- **Dockerfile**: Creates a new Dockerfile based on your Dockerfile and embeds the App-Embedded parameters.

- **Manual**: Select the manual method to customize the required Dockerfile parameters in the Console UI and directly download the App-Embedded Defender binary file.


**Prerequisites**

- You can connect to Azure Container Registry(ACR) or any other registry used to pull your images.

- The container where you are embedding App-Embedded Defender can reach Console’s port 8084 over the network.

- You have the Dockerfile for your image if you choose the **Deployment type** as Dockerfile.


### Embed App-Embedded Defender with Dockerfile[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/app-embedded/deploy-app-embedded-defender-aci\#embed-app-embedded-defender-with-dockerfile)

Upload your Dockerfile and Prisma Cloud creates a new Dockerfile with App-Embedded Defender parameters and the Defender binary file.

1. Log in to Prisma Cloud Console.

2. Go to **Manage > Defenders > Defenders: Deployed > Manual deploy**.















![deploy app embedded defender aci](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-fb6afcf3f0abbc28ed93fd59f83ebea88c546ecf%252Fdeploy-app-embedded-defender-aci.gif%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=75419d8ca24c160065cdb37621977965&sv=3)

3. In Deployment method, select **Single Defender**.

4. Select the Defender type as **Container Defender - App-Embedded**.

5. Select the DNS name configured in **Manage > Defenders > Names (SAN)** or public IP address that Defender will use to connect to Prisma Console.

6. **Enable file system runtime protection** to allow the sensors to monitor file system events regardless of how your runtime policy is configured, and could impact the underlying workload’s performance.

7. Select Deployment type as **Dockerfile**.









1. In **App ID**, enter a unique identifier for the App-Embedded Defender. All vulnerability, compliance, and runtime findings for the container will be aggregated under this App ID. In Console, the App ID is presented as the image name. Be sure to specify an App ID that lets you easily trace findings back to the image.

2. In **Data folder**, enter the path that the Defender will use to write files and store information.

3. **Dockerfile**: Upload the Dockerfile for your container image. Set up the task’s entrypoint in the Dockerfile. The embed process modifies the container’s entrypoint to run the App-Embedded Defender first, which in turn starts the original entrypoint process. The Defender starts defending the app from the entrypoint and the thread/child process created by this entrypoint.


8. **Download** the App-embedded bundle that contains the Dockerfile with Defender deployment configurations appended to your Dockerfile and the App-Embedded Defender binary file.

9. Rebuild the image and embed the Defender in ACI.


### Embed App-Embedded Defender Manually[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/app-embedded/deploy-app-embedded-defender-aci\#embed-app-embedded-defender-manually)

Embed App-Embedded Defender into a container image manually. Modify your Dockerfile with the given configurations, download the App-Embedded Defender binaries into the image’s build context, then rebuild the image.

**Prerequisites**

- At runtime, the container where you’re embedding App-Embedded Defender can reach Console over the network. For Enterprise Edition, Defender talks to Console on port 443. For Compute Edition, Defender talks to Console on port 8084.

- The host where you are rebuilding your container image with App-Embedded Defender can reach Console over the network on port 8083.

- You have the Dockerfile for your image.


1. Log in to Prisma Cloud Console.

2. Go to **Manage > Defenders > Defenders: Deployed > Manual deploy**.

3. In Deployment method, select **Single Defender**.

4. Select the Defender type as **Container Defender - App-Embedded**.

5. Select the DNS name (configured in **Manage > Defenders > Names (SAN)** or public IP address that Defender will use to connect to Prisma Console.

6. **Enable file system runtime protection** to allow the sensors to monitor file system events regardless of how your runtime policy is configured, and could impact the underlying workload’s performance.

7. Select **Deployment type** as **Manual**











Follow the instructions for embedding App-Embedded Defender into your image.









1. Download the App-Embedded bundle using the command or download the file directly.

2. Configure your Dockerfile and set the following environment variables:

















      AskCopy



      ```
      DEFENDER_TYPE="appEmbedded"
      ENV DEFENDER_APP_ID="Unique identifier for the App-Embedded Defender in Prisma Cloud Console"
      FILESYSTEM_MONITORING="true/false"
      WS_ADDRESS="Websocket address the Defender is communicating to"
      DATA_FOLDER="The path that Defender uses to store its metadata"
      INSTALL_BUNDLE="The access key for the Prisma Console, copy this from the Console"
      FIPS_ENABLED="true/false"
      ENTRYPOINT="Modify the entrypoint for the app to start the app under the control of App-Embedded Defender"
      ```

3. Add the App-Embedded Defender to Dockerfile.

















      AskCopy



      ```
      ADD twistlock_defender_app_embedded.tar.gz <DATA_FOLDER>
      ```

4. Modify the entrypoint so that your app starts under the control of App-Embedded Defender.

5. Rebuild your image and embed the Defender in Cloud instance.


## Embed App-Embedded Defender in Azure ACI[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/app-embedded/deploy-app-embedded-defender-aci\#embed-app-embedded-defender-in-azure-aci)

Prisma Cloud uses the updated Dockerfile to deploy the Defender in your containers running in ACI. Use the updated Dockerfile to build the image for App-Embedded Defender, push it to Azure Container Registry, and then run the container instance.

**Prerequisite**:

- Log in to Azure

- Create an Azure resource group

- Create an Azure ACI context

- You have an image of the Defender binary from the download App-Embedded zipped bundle from Prisma Cloud Console.

- You have the modified Dockerfile with App-Embedded Defender deployment configurations.


1. Log in to your Azure instances

















AskCopy



```
az login
```

2. Copy the App-Embedded zipped bundle and unzip it to get the Dockerfile and App-Embedded Defender binary.

3. Build the Dockerfile:

















AskCopy



```
docker build -t <Azure_Container_Registry>:<docker_image_name> <local_path_host_dockerfile>
```









If your Dockerfile is in the current directory, use **.** for <local\_path\_host-Dockerfile>

4. Start an Azure container instance from this image:









1. Go to **Azure Portal > Azure Container Registry > Repositories**. Right-click on the App-Embedded image and select **Run Instance**.

2. Create a container instance and edit the following:









      1. Enter the **Container name** to be the same as the container image name in Azure.

      2. Select the **OS type** as Linux (as Prisma Cloud only supports Linux x86 App-Embedded Defenders).

      3. Select **Public IP address** if you need routable IPs to establish communication between Prisma Console and Defender installed in Azure.

      4. Enter the **Port** defined for the APP in Dockerfile.


3. Select **Create**.


5. In Azure Container instances, verify that your application shows a **running** status.











This App-Embedded Defender running in ACI is now recognized in Prisma Console under **Manage > Defenders > Defenders: Deployed**.


## Embed App-Embedded Defender with twistcli[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/app-embedded/deploy-app-embedded-defender-aci\#embed-app-embedded-defender-with-twistcli)

Use the `twistcli` command line tool to embed an App-Embedded Defender in your Cloud Container Registries.

**Prerequisites**:

- Running tasks can connect to Prisma Cloud Console over the network.

- Prisma Cloud Defender connects to Console to retrieve runtime policies and send audits.

- The container where you’re embedding App-Embedded Defender can reach Console’s port 8084 over the network.

- You have Dockerfile for you image.

- Cloud CLI, such as Azure CLI, or Google Cloud CLI.


1. Log in to Prisma Cloud Console.

2. Download `twistcli`

3. Run `twistcli` to embed Defender in your Cloud Registry (such as Azure, or Google Run).











A file named _app\_embedded\_embed_ <app\_id>.zip\_ is created, that has the Dockerfile for App-Embedded Defender and App-Embedded Defender binary file.









   - <user> — Name of a Prisma Cloud user with a minimum [role](https://docs.prismacloud.io/admin-guide/authentication/user-roles) of Defender Manager.

   - <password> — For Prisma Cloud Enterprise Edition, you can also specify the secret key that you configured under **Prisma > Settings > Access Control > Access Keys**.

   - <token> — API Token for authenticating with Prisma Cloud Console. (For Enterprise Edition only)

   - <CONSOLE> — DNS name or IP address for Console.

   - <APP-ID> — Unique identifier.











     When setting `<APP-ID>`, specify a value that lets you easily trace findings back to the image. All vulnerability, compliance, and runtime findings for the container will be aggregated under this App ID.











     In Console, the App ID is presented as the image name.

   - <DATA-FOLDER> — Readable and writable directory in the container’s filesystem.

   - To enable file system protection, add the `--filesystem-monitoring` flag to the `twistcli` command.


4. Unpack _app\_embedded\_embed\_help.zip_.

5. Create and push the docker image to ACR

















AskCopy



```
$ az login
$ docker login <Azure-ID> -u <Azure_username> -p <Access_key_password>
$ docker build -t <Azure-ID>/REPO:TAG <DockerfileTwistlock_Destination_file>
$ docker images
$ docker push <Registry>/REPO:TAG
```







1. Check the image exists in Azure repo

















      AskCopy



      ```
      $ az acr repository show-tags \
      --name <registry> \
      --repository <repository> \
      --top 10 \
      --orderby time_desc \
      --detail
      ```

2. Create a container instance (ACI)

















      AskCopy



      ```
      $ az container create -g <MyResourceGroup> \
      --name <APP-EMBEDDED_NAME>  \
      --image <myAcrRegistry.azurecr.io/myimage:latest> \
      --registry-username <username> \
      --registry-password <password> \
      --location <location> \
      --ip-address Public \
      --os-type Linux \
      --ports 8080 \
      --cpu 1 \
      --memory 1.5
      ```


### Delete a Container Instance[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/app-embedded/deploy-app-embedded-defender-aci\#delete-a-container-instance)

AskCopy

```
$ az container delete -g <MyContainerGroup> --name <Container-name> -y
```

## View Deployed Defenders[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/app-embedded/deploy-app-embedded-defender-aci\#view-deployed-defenders)

To narrow the list to just App-Embedded Defenders, filter the table by type `Type: Container Defender - App-Embedded`.

![connected app embedded defenders](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-9a49fe83c9410f7fa25f321ade00e82f4ff4f746%252Fconnected_app_embedded_defenders.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=7f9eafed4355993183fd563ef24da477&sv=3)

By default, Prisma Cloud removes disconnected App-Embedded Defenders from the list after an hour. As part of the cleanup process, data collected by the disconnected Defender is also removed from **Monitor > Runtime > App-Embedded observations**.

## Trigger Events for App-Embedded[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/app-embedded/deploy-app-embedded-defender-aci\#trigger-events-for-app-embedded)

Refer to [Runtime defense for App-Embedded](https://docs.prismacloud.io/admin-guide/runtime-defense/runtime-defense-app-embedded).

## Monitor App-Embedded Events[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/app-embedded/deploy-app-embedded-defender-aci\#monitor-app-embedded-events)

You can view the [App-Embedded runtime events](https://docs.prismacloud.io/admin-guide/runtime-defense/runtime-defense-app-embedded) by app ID under **Monitor > Events > App-Embedded audits**, and view the [App-Embedded incidents](https://docs.prismacloud.io/admin-guide/runtime-defense/incident-explorer) under **Monitor > Runtime > Incident Explorer**.

You can also [deploy WAAS for Containers Protected By App-Embedded Defender](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/deploy-waas/deployment-app-embedded), create a WAAS rule policy, add an app, enable protections, run WAAS sanity tests, and monitor the events under **Monitor > Events > WAAS for App-Embedded**.

[PreviousDeploy App-Embedded Defender for Fargate](https://docs.prismacloud.io/admin-guide/install/deploy-defender/app-embedded/install-app-embedded-defender-fargate) [NextDeploy App-Embedded Defender in GCR](https://docs.prismacloud.io/admin-guide/install/deploy-defender/app-embedded/deploy-app-embedded-defender-gcr)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
