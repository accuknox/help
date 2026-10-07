For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/install/deploy-defender/defender-types.md).

To take advantage of the agent-based security features of Prisma Cloud, you must deploy Defenders. Defenders enforce the policies you set in the Prisma Cloud console.

Generally, you should deploy Defenders whenever you can. It offers the most features, it can simultaneously protect both containers and host, and nothing needs to be embedded inside your containers for Defenders to protect them. Specific types of assets require specific Defender types to protect them, to ensure optimal deployment into the environment, and to fully support for automated workflows.

You must decide how to deploy the Defenders based on the type of asset you want to protect.

![defender decision tree](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-f1e1a32d18b7c63f307b66e4b0dc80d69e7a3654%252Fdefender-decision-tree.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=b1e5ab9ced0a363a034f17dc0966c665&sv=3)

- Single Container Defenders: [Deploy a single Defender to a single container](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/compute-edition/34/admin-guide/install/deploy-defender/container/container.md).

- Single Host Defenders: [Deploy a single Defender to a single bare-metal or virtual host](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/compute-edition/34/admin-guide/install/deploy-defender/host/host.md).

- Orchestrator Defenders: [Deploy Defenders on an entire cluster at the orchestration level](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/compute-edition/34/admin-guide/install/deploy-defender/orchestrator/orchestrator.md).

- Serverless Defenders: [Deploy a single Defender to protect serverless functions at runtime](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/compute-edition/34/admin-guide/install/deploy-defender/serverless/serverless.md).

- App-embedded Defenders: [Deploy a single Defender to protect containers that run on container-on-demand services](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/compute-edition/34/admin-guide/install/deploy-defender/app-embedded/app-embedded.md).


To avoid manually deploying Defenders on each container, VM, or host, you can use [auto-Defend](https://docs.prismacloud.io/admin-guide/install/deploy-defender/host/auto-defend-host) to deploy Defenders automatically on AWS, Azure, or GCP.

## Container Defender (Linux and Windows)[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/defender-types\#container-defender-linux-and-windows)

[Deploy a container Defender](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/compute-edition/34/admin-guide/install/deploy-defender/container/container.md) on any host that runs a container workload. Container Defender protects both your containers and the underlying host. Docker or Podman (for Linux Container Defender) must be installed on the host because this Defender type runs as a container.

Container Defender offers the richest set of capabilities. The deployment is also the simplest. After deploying a container Defender to a host, it can immediately protect and monitor your containers and host. No additional steps are required to rebuild your containers with an agent inside. Container Defender should always be your first choice whenever possible.

There are some minimum requirements to run container Defender. You should have full control over the host where container Defender runs. It must be able to run alongside the other containers on the host with [select kernel capabilities](https://docs.prismacloud.io/admin-guide/install/system-requirements#kernel). And it must be able to run in the host’s network and process namespace.

Deploy single container Defenders when containers and the host running them that are not part of a cluster.

## Host Defender (Linux and Windows)[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/defender-types\#host-defender-linux-and-windows)

[Host Defender](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/compute-edition/34/admin-guide/install/deploy-defender/host/host.md) uses Prisma Cloud’s model-based approach for protecting hosts that do not run containers. This Defender type lets you extend Prisma Cloud to protect all the hosts in your environment, regardless of their purpose. Defender runs as a systemd service on Linux and a Windows service on Windows. If Docker is deployed on your host, deploy a container Defender to protect the containers and the underlying host.

Deploy one Host Defender per host. Do not deploy Host Defender if you’ve already deployed Container Defender to a host. Container Defender offers the same host protection capabilities as Host Defender.

## Orchestrator Defenders (Kubernetes)[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/defender-types\#orchestrator-defenders-kubernetes)

Container orchestrators provide native capabilities for deploying agents, such as Defender, to every node in the cluster. Prisma Cloud leverages these capabilities to install Defender. Kubernetes and OpenShift, for example, offer DaemonSets As such, Container Defender is deployed as a DaemonSet on Kubernetes

You can also [deploy container Defenders automatically in an entire cluster using kubeconfig](https://docs.prismacloud.io/admin-guide/install/deploy-defender/orchestrator/install-cluster-container-defender).

You can deploy an orchestrator Defender to protect assets in these orchestrators.

- [ECS](https://docs.prismacloud.io/admin-guide/install/deploy-defender/orchestrator/install-amazon-ecs)

- [Kubernetes](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/compute-edition/34/admin-guide/install/deploy-defender/orchestrator/orchestrator.md)

- [GKE](https://docs.prismacloud.io/admin-guide/install/deploy-defender/orchestrator/install-gke)

- [GKE Autopilot](https://docs.prismacloud.io/admin-guide/install/deploy-defender/orchestrator/install-gke-autopilot)

- [Openshift](https://docs.prismacloud.io/admin-guide/install/deploy-defender/orchestrator/openshift)

- [Tanzu Application Service](https://docs.prismacloud.io/admin-guide/install/deploy-defender/orchestrator/install-tas-defender)


## Serverless Defender[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/defender-types\#serverless-defender)

Serverless Defenders offer runtime protection for [AWS Lambda functions](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) and [Azure Functions](https://azure.microsoft.com/en-us/services/functions/). Serverless Defender must be [embedded inside your functions](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/compute-edition/34/admin-guide/install/deploy-defender/serverless/serverless.md). [Deploy one Serverless Defender](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/compute-edition/34/admin-guide/install/deploy-defender/serverless/serverless.md) per function.

## App-Embedded Defender[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/defender-types\#app-embedded-defender)

If you use services providing containers on demand, you can run containers, but the service abstracts away the underlying cluster, host, operating system, and software modules. Without access to those hooks, container Defenders can’t monitor and protect resources in those environments. Instead, embed an app-embedded Defender directly inside your workload running in the container to establish a point of control. You can manually embed the Defenders or use automated workflows to embed Defenders using Fargate or Dockerfile.

Using Dockerfile, you [deploy one app-embedded Defender per container](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/compute-edition/34/admin-guide/install/deploy-defender/app-embedded/app-embedded.md). Using Fargate, you [deploy one app-embedded Defender per task](https://docs.prismacloud.io/admin-guide/install/deploy-defender/app-embedded/install-app-embedded-defender-fargate).

### Fargate[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/defender-types\#fargate)

If you have an AWS Fargate task, deploy App-Embedded Fargate Defender.

A key attribute of the App-Embedded Fargate Defender is that you don’t need to change how the container images in the task are built. The process of embedding the App-Embedded Defender simply manipulates the task definition to inject a Prisma Cloud sidecar container, and start existing task containers with a new entry point, where the entry point binary is hosted by the Prisma Cloud sidecar container. The transformation of an unprotected task to a protected task takes place at the task definition level only. The container images in the task don’t need to be manually modified. This streamlined approach means that you don’t need to maintain two versions of an image (protected and unprotected). You simply maintain the unprotected version, and when you protect a task, Prisma Cloud dynamically injects App-Embedded Defender into it.

The Prisma Cloud sidecar container has a couple of jobs:

- Hosts the Defender binary that gets injected into containers in the task.

- Proxies all communication to Console. Even if you have multiple containers in a task, it appears as a single entity in Console’s dashboard.

- Synchronizes policy with Console and sends alerts to Console.


### Dockerfile[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/defender-types\#dockerfile)

The Docker image format, separate from the runtime, is becoming a universal runnable artifact. If you’re not using Fargate, but something else that runs a Docker image, such as Azure Container Instances, use the App-Embedded Defender with the Dockerfile method.

Provide a Dockerfile, and Prisma Cloud returns a new version of the Dockerfile in a bundle. Rebuild the new Dockerfile to embed Prisma Cloud into the container image. When the container starts, Prisma Cloud App-Embedded Defender starts as the parent process in the container, and it immediately invokes your program as its child.

There are two big differences between this approach and the Fargate approach:

- With the Fargate approach, you don’t change the actual image. With the Dockerfile approach, you have the original image and a new protected image. You must modify the way your containers are built to embed App-Embedded Defender into them. You need to make sure you tag and deploy the right image.

- Each Defender binary makes it’s own connection to the prisma Cloud console. In the Console dashboard, they are each counted as unique applications.


Nothing prevents you from protecting a Fargate task using the Dockerfile approach, but it’s inefficient.

### Manual[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/defender-types\#manual)

Use the manual approach to protect almost any type of runtime. If you’re not running a Docker image, but you still want Prisma Cloud to protect it, deploy App-Embedded Defender with the manual method. Download the App-Embedded Defender, set up the required environment variables, then start your program as an argument to the App-Embedded Defender.

If you choose the manual approach, you have to figure out how deploy, maintain, and upgrade your app on your own. While the configuration is more complicated, it’s also the most universal option because you can protect almost any executable.

## Tanzu Application Service Defender[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/defender-types\#tanzu-application-service-defender)

[Tanzu Application Service (TAS) Defenders](https://docs.prismacloud.io/admin-guide/vulnerability-management/vmware-tanzu-blobstore) run on your TAS infrastructure. TAS Defenders provide nearly all the same capabilities as Container Defenders, as well as the ability to scan droplets in your blobstores for vulnerabilities. For specific differences between TAS Defenders and Container Defenders, see the [TAS Defender install article](https://docs.prismacloud.io/admin-guide/install/deploy-defender/orchestrator/install-tas-defender).

The TAS Defender is delivered as a tile that can be installed from your TAS Ops Manager Installation Dashboard.

[PreviousDeploy the Prisma Cloud Defender](https://docs.prismacloud.io/admin-guide/install/deploy-defender) [NextManage your Defenders](https://docs.prismacloud.io/admin-guide/install/deploy-defender/manage-defender)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
