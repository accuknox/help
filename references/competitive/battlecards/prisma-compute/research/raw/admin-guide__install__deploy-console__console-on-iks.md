For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-iks.md).

Use the following procedure to install Prisma Cloud in an IKS cluster. IKS uses dynamic PersistentVolumeClaim provisioning (`ibmc-file-bronze` is the default StorageClass) as well as automatic LoadBalancer configuration for the Prisma Cloud Console. You can optionally specify a StorageClass for premium [file](https://cloud.ibm.com/docs/containers?topic=containers-file_storage) or [block](https://cloud.ibm.com/docs/containers?topic=containers-block_storage) storage options. Use a [retain](https://cloud.ibm.com/docs/containers?topic=containers-file_storage#existing-file-1) storage class (not default) to ensure your storage is not destroyed even if you delete the PVC.

When installing Defenders the IKS Kubernetes version you use matters. [IKS Kubernetes version 1.10 uses Docker, and 1.11+ uses containerd](https://www.ibm.com/cloud/blog/ibm-cloud-kubernetes-service-supports-containerd) as the container runtime.

- If using `containerd`, pass the `--container-runtime containerd` flag to `twistcli`.

- Or select the **Container Runtime type** as `containerd` in the Console UI when generating the Defender `YAML` or `Helm` chart.


1. Use _twistcli_ to generate the Prisma Cloud Console YAML configuration file, where <PLATFORM> can be linux or osx. Optionally set the storage class to premium storage class. For IKS with Kubernetes 1.10, use our standard Kubernetes instructions. Here is an example with a premium StorageClass with the retain option.

















AskCopy



```
     $ <PLATFORM>/twistcli console export kubernetes \
       --storage-class ibmc-file-retain-silver \
       --service-type LoadBalancer
```

2. Deploy the Prisma Cloud Console in the IBM Kubernetes Service cluster.

















AskCopy



```
     $ kubectl create -f ./twistlock_console.yaml
```

3. Wait for the service to come up completely.

















AskCopy



```
     $ kubectl get service -w -n twistlock
```

4. Configure the console as described in [Configure the Prisma Cloud Console](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-kubernetes#configure-console-k8s).


[PreviousDeploy the Prisma Cloud Console on EKS](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-eks) [NextDeploy the Prisma Cloud Console on Openshift](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-openshift)

Last updated 3 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
