For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/install/getting-started.md).

Console is Prisma Cloud’s management interface. It lets you define policy and monitor your environment.

Defender protects your environment according to the policies set in Console. There are a number of [Defender types](https://docs.prismacloud.io/admin-guide/install/deploy-defender/defender-types), each designed to protect a specific resource type.

The primary concern for most customers getting started with Prisma Cloud is securing their container environment. To do this, install Container Defender on every host that runs containers. Container orchestrators typically provide native capabilities for deploying an agent, such as Defender, to every node in the cluster. Prisma Cloud leverages these capabilities to install Defender. For example, Kubernetes and OpenShift, offer DaemonSets, which guarantee that an agent runs on every node in the cluster. Prisma Cloud Defender, therefore, is deployed in Kubernetes and OpenShift clusters as a DaemonSet.

In this section, you’ll find dedicated install guides for all popular container platforms. Each guide shows how to install Prisma Cloud for that given platform.

As you adopt other cloud-native technologies, Prisma Cloud can be extended to protect those environments too. Deploy the Defender type best suited for the job. For example, today you might use Amazon EKS (Kubernetes) clusters to run your apps. This part of your environment would be protected by Container Defender. Later you might adopt AWS Lambda functions. This part of your environment would be secured by Serverless Defender. Extending Prisma Cloud to protect other types of cloud-native technologies calls for deploying the right Defender type.

![getting started resource classes](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-430273f1c5277baf5ccf5e53c42d9e3335a4ebca%252Fgetting-started-resource-classes.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=3a7b0c571045cd5ef3e09207434351ed&sv=3)

All Defenders, regardless of their type, report back to Console, letting you secure hybrid environments with a single tool. The main criteria for installing Defender is that it can connect to Console. Defender connects to Console via websocket to retrieve policies and send data.

## Install guides[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/getting-started\#install-guides)

Start your install with one of our dedicated guides.

Install procedure

Description

[Kubernetes](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/compute-edition/34/admin-guide/install/deploy-defender/orchestrator/orchestrator.md)

Prisma Cloud runs on any implementation of Kubernetes, whether you build the cluster from scratch or use a managed solution (also known as Kubernetes as a service). We’ve tested and validated the install on:

- [Amazon Elastic Kubernetes Service (Amazon EKS)](https://docs.aws.amazon.com/eks/latest/userguide/getting-started.html)

- [Azure Kubernetes Service (AKS)](https://docs.microsoft.com/en-us/azure/aks/)

- [Google Kubernetes Engine (GKE)](https://cloud.google.com/kubernetes-engine/docs/)

- [IBM Kubernetes Service (IKS)](https://cloud.ibm.com/docs/containers?topic=containers-getting-started)

- [Alibaba Cloud Container Service for Kubernetes](https://www.alibabacloud.com/help/product/85222.htm)


In some cases, there is a dedicated section for installing on a specific cloud provider’s managed solution. When there is no dedicated section, use the generic install method.

[OpenShift 4](https://docs.prismacloud.io/admin-guide/install/deploy-defender/orchestrator/openshift)

Prisma Cloud offers native support for OpenShift.

[Amazon ECS](https://docs.prismacloud.io/admin-guide/install/deploy-defender/orchestrator/install-amazon-ecs)

[Windows](https://docs.prismacloud.io/admin-guide/install/deploy-defender/host/windows-host)

Install Defender on Windows hosts running containers. Defender is installed using a PowerShell script.

## Encryption[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/getting-started\#encryption)

All network traffic is encrypted with TLS (https) for user to Console communication. Likewise, all Defender to Console communication is encrypted with TLS (WSS).

[PreviousInstall](https://docs.prismacloud.io/admin-guide/install/install) [NextSystem requirements](https://docs.prismacloud.io/admin-guide/install/system-requirements)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
