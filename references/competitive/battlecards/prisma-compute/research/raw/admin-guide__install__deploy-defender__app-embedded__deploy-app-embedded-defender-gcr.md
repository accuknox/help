For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/install/deploy-defender/app-embedded/deploy-app-embedded-defender-gcr.md).

Deploy an App-Embedded Defender in GCR to provide runtime protection to App-Embedded applications installed in GCR.

The App-Embedded Defender enforces runtime policy on the application entrypoint and any child processes created by this entrypoint. To learn when to use App-Embedded Defenders, see [Defender types](https://docs.prismacloud.io/admin-guide/install/deploy-defender/defender-types).

To learn more about App-Embedded Defender’s capabilities, see:

- [Vulnerability scanning for App-Embedded](https://docs.prismacloud.io/admin-guide/vulnerability-management/app-embedded-scanning)

- [Compliance scanning for App-Embedded](https://docs.prismacloud.io/admin-guide/compliance/app-embedded-scanning)

- [Runtime defense for App-Embedded](https://docs.prismacloud.io/admin-guide/runtime-defense/runtime-defense-app-embedded)

- Protecting front-end containers at runtime with [WAAS](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/compute-edition/34/admin-guide/waas/waas.md)


## System Requirements[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/app-embedded/deploy-app-embedded-defender-gcr\#system-requirements)

- GCR supports Linux (X86) containers

- Any Docker image with Prisma Cloud App-Embedded Defender binary

- Google Cloud Registry (recommended)


## Prerequisites[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/app-embedded/deploy-app-embedded-defender-gcr\#prerequisites)

- You can connect to GCR and DockerHub


**Configure GCP to authenticate Prisma Cloud**

- Sign in to your Google Cloud account.

- Log in to Google Cloud Registry.

- In the Google Cloud Console, on the project selector page, select or create a Google Cloud project.









  - Set "private" visibility for your GCP container registry host under **GCP project > Home > Container Registry > Settings**.


- Configure GCloud authentication using any of the following options:









  - Authenticate using GCP user credentials:

















    AskCopy



    ```
    $ gcloud auth login ### Type the User GCP credentials
    $ cat ~/.docker/config.json  ### Check that GCP has gcloud users configured
    ```

  - Authenticate using GCP Service Account:

















    AskCopy



    ```
    $ gcloud auth activate-service-account ACCOUNT --key-file=KEY-FILE
    ### KEY-FILE is the Service Account key file under *GCP > Service Accounts > Actions > Manage keys*
    ```


**Configure Docker for GCP in your localhost**

AskCopy

```
$ gcloud auth configure-docker
$ cat ~/.docker/config.json.  ### check that GCP has gcloud users configured
```

## Configure App-Embedded Defender in Prisma Console UI[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/app-embedded/deploy-app-embedded-defender-gcr\#configure-app-embedded-defender-in-prisma-console-ui)

Prisma Console provides you with an App-Embedded Defender bundle that contains the Dockerfile with App-Embedded configurations and the Defender installation binary file.

You can select one of the **Deployment types**: Dockerfile or Manual.

- **Dockerfile**: Creates a new Dockerfile based on your Dockerfile and embeds the App-Embedded parameters.

- **Manual**: Select the manual method to customize the required Dockerfile parameters in the Console UI and directly download the App-Embedded Defender binary file.


### Embed App-Embedded Defender with Dockerfile[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/app-embedded/deploy-app-embedded-defender-gcr\#embed-app-embedded-defender-with-dockerfile)

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

9. Rebuild the image and embed the Defender in GCR.


### Embed App-Embedded Defender Manually[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/app-embedded/deploy-app-embedded-defender-gcr\#embed-app-embedded-defender-manually)

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


## Embed App-Embedded Defender in GCR[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/app-embedded/deploy-app-embedded-defender-gcr\#embed-app-embedded-defender-in-gcr)

Prisma Cloud uses the updated Dockerfile to deploy the Defender in your containers running in GCR. Use the updated Dockerfile to build the image for App-Embedded Defender, push it to Google Container Registry, and then run the Google Container instance.

**Prerequisite**:

- Create a new [GCR repository](https://cloud.google.com/artifact-registry/docs/repositories/create-repos), if not already exists.


1. Log in to Docker

















AskCopy



```
docker login
```

2. Copy the App-Embedded zipped bundle and unzip it to get the Dockerfile and App-Embedded Defender binary.

3. Build the Dockerfile:

















AskCopy



```
docker build -t <GCP_Container_Registry>:<docker_images_name>  <local_path_host_dockerfile>
```









If your Dockerfile is in the current directory, use **.** for <local\_path\_host-Dockerfile>

4. **Push the docker image to GCR**:

















AskCopy



```
docker push HOSTNAME/PROJECT-ID/IMAGE:TAG
```







1. Verify the docker image exists in your **GCP project > Container Registry > Images** under your relevant repository.


5. **Deploy Docker image in Google Cloud Run using Google Console**:









1. Select your **Container Registry > Images**, and select **Actions > Deploy to Cloud Run**.

2. Enter a **Service name** or select the default value.

3. Set the **CPU allocation and pricing** to **CPU is always allocated**.

4. Select the **Ingress** traffic to allow **All** requests, including requests directly from the internet to the **run**.


6. In the **Container, Networking, Security** section, enter the **Container port** as 8080.

7. Select **CREATE**.

8. Go to **Cloud Run** and verify the Docker Container service running in GCP.











This App-Embedded Defender running in GCR is now recognized in Prisma Console under **Manage > Defenders > Defenders: Deployed**.


## Embed App-Embedded Defender with twistcli[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/app-embedded/deploy-app-embedded-defender-gcr\#embed-app-embedded-defender-with-twistcli)

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

5. Create and push the docker image to GCR









1. Authenticate using GCP credentials:

















      AskCopy



      ```
      $ gcloud auth login
      ```

2. Or, Authenticate using GCP Service Account key (KEY-FILE): (Get the KEY-FILE from **GCP > Service Accounts > Actions > Manage keys**)

















      AskCopy



      ```
      $ gcloud auth activate-service-account ACCOUNT --key-file=KEY-FILE
      ```

3. Configure Docker for GCP in your localhost

















      AskCopy



      ```
      $ glcoud auth configure-docker
      ```

4. Build the Dockerfile

















      AskCopy



      ```
      $ docker build -t <GCP_Container_Registry>:<docker_images_name>  <local_path_host_dockerfile>
      $ docker images ### Verify the image built
      ```

5. Push the image to GCR

















      AskCopy



      ```
      $ docker push HOSTNAME/PROJECT-ID/IMAGE:TAG
      ```

6. Check the image exists in GCR repo under **GCP project > Container Registry > Images**

7. Deploy Docker image in Google Cloud Run using `gcloud`

















      AskCopy



      ```
      $ gcloud run deploy [SERVICE] \
      --image <IMAGE_URL> \
      --service-account <SERVICE_ACCOUNT> \
      --no-cpu-throttling \
      --platform managed \
      --ingress <all> \
      --port <port-exposed-in-dockerfile> \
      --region <REGION> \
      --project <PROJECT_NAME>
      ```









      If there is no port exposed in Dockerfile, GCP Cloud Run will use 8080 port as the default.


### Delete a Container Instance[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/app-embedded/deploy-app-embedded-defender-gcr\#delete-a-container-instance)

AskCopy

```
$ az container delete -g <MyContainerGroup> --name <Container-name> -y
```

## Trigger Events for App-Embedded[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/app-embedded/deploy-app-embedded-defender-gcr\#trigger-events-for-app-embedded)

Refer to [Runtime defense for App-Embedded](https://docs.prismacloud.io/admin-guide/runtime-defense/runtime-defense-app-embedded).

To trigger the App Server logs, get the GCP URL from GCP Docker Container service.

AskCopy

```
$ curl -k -X POST -H "Authorization: Bearer $(gcloud auth print-identity-token)" <app_emb_gcp_URL>/runsee -d $(echo 'ldd --help'|base64)
```

## Monitor App-Embedded Events[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/app-embedded/deploy-app-embedded-defender-gcr\#monitor-app-embedded-events)

You can view the [App-Embedded runtime events](https://docs.prismacloud.io/admin-guide/runtime-defense/runtime-defense-app-embedded) by app ID under **Monitor > Events > App-Embedded audits**, and view the [App-Embedded incidents](https://docs.prismacloud.io/admin-guide/runtime-defense/incident-explorer) under **Monitor > Runtime > Incident Explorer**.

You can also [deploy WAAS for Containers Protected By App-Embedded Defender](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/deploy-waas/deployment-app-embedded), create a WAAS rule policy, add an app, enable protections, run WAAS sanity tests, and monitor the events under **Monitor > Events > WAAS for App-Embedded**.

[PreviousDeploy App-Embedded Defender in ACI](https://docs.prismacloud.io/admin-guide/install/deploy-defender/app-embedded/deploy-app-embedded-defender-aci) [NextDefault Setting for App-Embedded Defender File System Monitoring](https://docs.prismacloud.io/admin-guide/install/deploy-defender/app-embedded/config-app-embedded-fs-mon)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
