For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-eks.md).

[Amazon Kubernetes Service (EKS)](https://aws.amazon.com/eks/#) lets you deploy Kubernetes clusters on demand. Use our standard Kubernetes install method to deploy Prisma Cloud to EKS.

If using Bottlerocket OS-based nodes for your EKS Cluster:

- Pass the `--container-runtime containerd` flag to `twistcli`.

- Or select the **Container Runtime type** as `containerd` in the Console UI when generating the Defender `YAML` or `Helm` chart.


Follow the instructions to [deploy Defenders as DaemonSet](https://docs.prismacloud.io/admin-guide/install/deploy-defender/orchestrator/install-kubernetes-cri) for more details.

**Prerequisites**

- You have deployed an Amazon EKS cluster.

- You have [downloaded the Prisma Cloud software](https://docs.prismacloud.io/admin-guide/tools/twistcli).


1. Generate the Prisma Cloud Compute Console deployment file.

















AskCopy



```
$ twistcli console export kubernetes \
     --service-type LoadBalancer \
     --storage-class gp2
```

2. Deploy Console.

















AskCopy



```
$ kubectl create -f twistlock_console.yaml
```

3. Wait for the service to come up completely.

















AskCopy



```
$ kubectl get service -w -n twistlock
```

4. Continue with the rest of the [installation for Kubernetes clusters](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-kubernetes).


[PreviousDeploy the Prisma Cloud Console on AKS](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-aks) [NextDeploy the Prisma Cloud Console on IKS](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-iks)

Last updated 3 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
