For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/install/deploy-defender/orchestrator/install-gke-autopilot.md).

You can now install the Prisma Cloud DaemonSet Defender on your GKE Autopilot cluster. GKE Autopilot clusters use [COS](https://cloud.google.com/kubernetes-engine/docs/concepts/using-containerd) (Container-Optimized OS) with Containerd nodes, therefore the DaemonSet must be configured with **Containerd**. Defenders deployed on GKE Autopilot clusters only support the official Prisma Cloud registry, and you cannot use a custom registry. The DaemonSet image must adhere to the following regex to ensure it comes from the official repository:

AskCopy

```
^registry-auth\\.twistlock\\.com/.*/twistlock/defender.*.
```

To ensure a successful deployment, do not modify the volume mounts or capabilities from the YAML generated. Any changes may cause issues with GCP allow list and deployment in GKE Autopilot.

## Prerequisites[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/orchestrator/install-gke-autopilot\#prerequisites)

GKE Autopilot does not natively support DaemonSet scaling. In case of resource exhaustion or insufficient resources, Defender pods may not start. To mitigate this, consider configuring a **PriorityClass** to prioritize Defender pods. Here are the steps for mitigation:

1. Create a PriorityClass YAML to prioritize the Defender pods:

















AskCopy



```
apiVersion: scheduling.k8s.io/v1
kind: PriorityClass
metadata:
     name: pcc-defender-ds
value: 1000000000
globalDefault: false
description: "Deploy defender daemonset"
```









Apply it to your cluster:

















AskCopy



```
kubectl apply -f pc.yaml
```

2. Reference the PriorityClass in the DaemonSet YAML under `/spec/template/spec`:

















AskCopy



```
priorityClassName: pcc-defender-ds
```


This will prioritize the Defender pods over other workloads in the cluster.

Here are the steps to deploy the Prisma Cloud DaemonSet Defender on a Google Kubernetes Engine (GKE) Autopilot.

## Deploy Google Kubernetes Engine (GKE) Autopilot.[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/orchestrator/install-gke-autopilot\#deploy-google-kubernetes-engine-gke-autopilot)

Here are the steps to deploy the Prisma Cloud DaemonSet Defender on a Google Kubernetes Engine (GKE) Autopilot.

1. Review the prerequisites and the procedure in the Google Kubernetes Engine (GKE) and the Install Prisma Cloud on a CRI (non-Docker) cluster sections.

2. Use the following twistcli command to generate the YAML file for the GKE Autopilot deployment.

















AskCopy



```
      $ <PLATFORM>/twistcli defender export kubernetes \
       --gke-autopilot \
       --container-runtime containerd \
       --cluster-address <console address> \
       --address https://<console address>:443
```







   - The `--gke autopilot flag` adds the ’autopilot.gke.io/no-connect: "true"’ \`annotation to the YAML file.

   - The `--container-runtime containerd` flag ensures compatibility with GKE Autopilot clusters by using the Container-Optimized OS with the containerd node image (instead of Docker). This also removes the `/var/lib/containers` mount, which is not required for GKE Autopilot.


If you are on Prisma Cloud console, from **Runtime Security > Manage > Defenders > Deployed Defenders > Manual deploy** ensure that the orchestrator type is **Kubernetes**, select the **Container Runtime type** as Containerd and from **Advanced Settings** enable **GKE Autopilot deployment**.

![deploy gke](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-c78a95b12c383a7c0a992054388d13b7d57a1418%252Fdeploy-gke.gif%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=74dae3c4744fbc2b225f7d6d5bf39f4b&sv=3)

1. Create the twistlock namespace on your cluster by running the following command:

















AskCopy



```
$ kubectl create namespace twistlock
```

2. Deploy the updated YAML or the Helm chart on your GKE Autopilot cluster.

3. Verify that the Defenders are deployed.


After a few minutes, verify that the Defenders are deployed. You should observe the nodes and running containers in the Console, confirming that Prisma Cloud Compute is now protecting your cluster.

[PreviousDeploy Defender on Google Kubernetes Engine (GKE)](https://docs.prismacloud.io/admin-guide/install/deploy-defender/orchestrator/install-gke) [NextDeploy Defender on OpenShift v4](https://docs.prismacloud.io/admin-guide/install/deploy-defender/orchestrator/openshift)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
