For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/install/deploy-defender/orchestrator/install-kubernetes-cri.md).

Kubernetes lets you set up a cluster with the container runtime of your choice. Prisma Cloud supports Docker Engine, CRI-O, and cri-containerd.

When generating the YAML file or Helm chat to deploy the Defender DaemonSet, you can select the **Container Runtime type** on Prisma Cloud console from **Manage > Defenders > Defenders: Deployed > Manual deploy**.

Since Defenders need to have a view of other containers, this option is necessary to guide the communication.

If you use _containerd_ on GKE, and you install Defender without selecting the `CRI-O` **Container Runtime type**, everything will appear to work properly, but you’ll have no images or container scan reports in **Monitor > Vulnerability** and **Monitor > Compliance pages** and you’ll have no runtime models in **Monitor > Runtime**. This happens because the Google Container Optimized Operating system (GCOOS) nodes have Docker Engine installed, but Kubernetes doesn’t use it. Defender thinks everything is OK because all of the integrations succeed, but the underlying runtime is actually different.

![container runtime type ui](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-0cd393b9eb679ad1e547c83eb2af865d8b10f5fe%252Fcontainer-runtime-type-ui.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=713d761a5493e431df99a0a43b380c8a&sv=3)

If you’re deploying Defender DaemonSets with twistcli, use the following flag with one of the container runtime types:

- `--container-runtime docker`

- `--container-runtime crio`

- `--container-runtime containerd`


When generating YAML from Console or twistcli, there is a simple change to the _yaml_ file as seen below.

In this abbreviated version DEFENDER\_TYPE:daemonset will use the Docker interface.

To change the default containerd data directory from `/var/lib/containerd` to a custom directory (for example: `/var/lib/kubelet/containerd`), modify the `volumeMounts` and `volumes` sections. Here is an example:

To change the default containerd data directory from `/var/lib/containerd` to a custom directory (for example: `/var/lib/kubelet/containerd`), modify the `volumeMounts` and `volumes` sections. Here is an example:

In this abbreviated version DEFENDER\_TYPE:cri will use the CRI.

Similar to the Defenders, to customize the containerd data directory, modify the paths in the `volumeMounts` and `volumes` sections accordingly.

[PreviousDeploy Prisma Cloud Defender from the GCP Marketplace](https://docs.prismacloud.io/admin-guide/install/deploy-defender/orchestrator/install-defender-gcp-marketplace) [NextVMware Tanzu Application Service (TAS) Defender](https://docs.prismacloud.io/admin-guide/install/deploy-defender/orchestrator/install-tas-defender)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
