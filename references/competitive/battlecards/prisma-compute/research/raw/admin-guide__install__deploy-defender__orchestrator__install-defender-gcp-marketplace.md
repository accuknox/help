For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/install/deploy-defender/orchestrator/install-defender-gcp-marketplace.md).

**Prerequisites:** You need access to a Prisma Cloud SaaS Console. You can sign up for a free trial of Prisma Cloud on the Google Cloud Marketplace.

01. Find Prisma Cloud - Kubernetes Security Defender in the GCP Marketplace. Click Configure.















    ![gcp1](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-fe2b9a384c0e0110a7d2914f1778d38f85fe14ce%252Fgcp1.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=14cf80560e0c6c77d8e83abf037a2025&sv=3)

02. Create Cluster, if you don’t have an existing Kubernetes cluster. Otherwise, continue to the next step.















    ![gcp2](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-a30e51bc2f0a2fe7d2d3a9229cdf264ee2f070d7%252Fgcp2.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=8ff9362f94bb206d26715ed8e74dc946&sv=3)

03. Select an existing namespace to install Defender, or Create a namespace (recommended). The default new namespace is "twistlock".















    ![gcp3](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-4f1d57f2a1e51fa4a3379a2ec5e86f4f0b10ebf3%252Fgcp3.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=3e08729067937a80c9d62b2a8c8f18b1&sv=3)

04. Enter the App instance name for the Defender the installation. This name displays on the Application section of the GKE portal:















    ![gcp4](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-3b4ec9f835a96235ef8320d795a01b277d072e4c%252Fgcp4.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=d7cd1508ed9fe6471978b1e31e2e2a82&sv=3)

05. Specify the following information about your Prisma Cloud SaaS Console (go through steps 6-8 to get these info):















    ![gcp5](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-18202410b4a833d01d392d120e5f3bbd15de25c1%252Fgcp5.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=1a4ea234dfbc25fe4ef014beff63066b&sv=3)

06. To get the URL for your Prisma Cloud Console:









    1. Log into your Prisma Cloud portal (e.g., https://app.prismacloud.io/).

    2. Navigate to **Compute > System**.

    3. Copy the URL in Path to Console. GCP uses this URL to get all the setup artifacts from your Prisma Cloud Console. In this example, it’s https://us-east1.cloud.twistlock.com/us-1-111573360.















       ![gcp6](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-dceffb32f4137bde199404085ab743566caaf7c9%252Fgcp6.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=a96c82cf7889e1bbb1946ae5ebe2863c&sv=3)


07. To get a token for your Prisma Cloud Compute Console.









    1. Go to Compute > Authentication.

    2. Copy the API token. and paste it into the GCP Marketplace form.















       ![gcp7](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-98d21b1ff007c8cdf15a88b8e9afbaa76b9ebdbc%252Fgcp7.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=962ac41a384103ad2ab2ad86e7840209&sv=3)


08. Specify the IP address or domain name of your Prisma Cloud Compute Console.











    The Defenders that you are deploying will use this IP address to communicate with Prisma Cloud. It’s almost the same as the URL, but remove the protocol (https://) and the path (everything trailing the first "/"). In this example, us-east1.cloud.twistlock.com.















    ![gcp8](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-114f21880a494d4ef71f30ae07b3bcb7c8de4cba%252Fgcp8.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=d3a7bf2ca33705fffeb4ef3da0dbe313&sv=3)

09. When the form is filled out, click Deploy.















    ![gcp9](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-382999c51d1e7dca959c293008db8d200dbbb808%252Fgcp9.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=6052c570e0501ef230979e47ac6dd6e4&sv=3)

10. Go to Prisma Cloud SaaS Console to confirm the deployment is successful.









    1. In the GKE console, review the status of your deployment:















       ![gcp10](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-ecd31d1fff6698373c8b6c618cf449e2ab7627d5%252Fgcp10.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=2a9b445a8cad4391413c6d95bf61a82b&sv=3)

    2. In Prisma Cloud Console, go to Compute > Defender to review the status of your deployment:















       ![gcp11](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-e2dd8481b14d1331e38ddde1f99657849784da73%252Fgcp11.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=a8e3d1612799d6631923ee3dc0826c2b&sv=3)


[PreviousAutomatically Install Container Defender in a Cluster](https://docs.prismacloud.io/admin-guide/install/deploy-defender/orchestrator/install-cluster-container-defender) [NextDeploy Defenders as DaemonSets](https://docs.prismacloud.io/admin-guide/install/deploy-defender/orchestrator/install-kubernetes-cri)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
