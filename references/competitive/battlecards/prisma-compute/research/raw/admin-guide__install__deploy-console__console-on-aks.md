For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-aks.md).

Use the following procedure to install Prisma Cloud in an AKS cluster. This setup uses dynamic PersistentVolumeClaim provisioning using Premium Azure Disk. When creating your Kubernetes cluster, be sure to specify a [VM size](https://docs.microsoft.com/en-us/azure/virtual-machines/windows/premium-storage#supported-vms) that supports premium storage.

Prisma Cloud doesn’t support Azure Files as a storage class for persistent volumes. Use Azure Disks instead.

**Prerequisites**

- You have deployed an [Azure Container Service (AKS) cluster](https://docs.microsoft.com/en-us/azure/aks/tutorial-kubernetes-deploy-cluster). Use the [--node-vm-size](https://docs.microsoft.com/en-us/cli/azure/aks?view=azure-cli-latest#az-aks-create) parameter to specify a VM size that supports Premium Azure Disks.

- You have installed [Azure CLI 2.0.22](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest) or later.

- You have [downloaded the Prisma Cloud command-line utility](https://docs.prismacloud.io/admin-guide/tools/twistcli-console-install).


1. Use `twistcli` to generate the Prisma Cloud Console YAML configuration file, where <PLATFORM> can be `linux` or `osx`. Set the storage class to Premium Azure Disk.

















AskCopy



```
     $ <PLATFORM>/twistcli console export kubernetes \
       --storage-class managed-premium \
       --service-type LoadBalancer
```

2. Deploy the Prisma Cloud Console in the Azure Kubernetes Service cluster.

















AskCopy



```
     $ kubectl create -f ./twistlock_console.yaml
```

3. Wait for the service to come up completely.

















AskCopy



```
     $ kubectl get service -w -n twistlock
```

4. Change the `reclaimPolicy` of the `PersistentVolumeClaim`.

















AskCopy



```
     $ kubectl get pv
     $ kubectl patch pv <pvc-name> -p '{"spec":{"persistentVolumeReclaimPolicy":"Retain"}}'
```

5. Next, [configure the Prisma Cloud console](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-kubernetes#configure-console-k8s).


[PreviousDeploy the Prisma Cloud Console on ACS](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-acs) [NextDeploy the Prisma Cloud Console on EKS](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-eks)

Last updated 3 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
