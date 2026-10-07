For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-ack.md).

[Alibaba Cloud Container Service for Kubernetes (ACK)](https://www.alibabacloud.com/product/kubernetes) is a managed Kubernetes service. Use the standard Kubernetes install procedure to deploy Prisma Cloud to Alibaba ACK, but specify an Alibaba Cloud-specific StorageClass when configuring the deployment.

This procedure shows you how to use Helm charts to install Prisma Cloud, but all other install methods are supported.

**Prerequisites**

- You have provisioned an ACK cluster.


1. Download the release tarball to the system where you administer your cluster (where you run your kubectl commands).

















AskCopy



```
     $ wget <LINK_TO_CURRENT_RECOMMENDED_RELEASE_LINK>
```

2. Unpack the Prisma Cloud release tarball.

















AskCopy



```
     $ mkdir twistlock
     $ tar xvzf twistlock_<VERSION>.tar.gz -C prisma_cloud/
```

3. Create a Helm chart for Prisma Cloud Console.

















AskCopy



```
     $ <PLATFORM>/twistcli console export kubernetes \
       --storage-class <alicloud-StorageClass> \
       --service-type LoadBalancer \
       --helm
```









(Use a valid Alibaba Cloud StorageClass for `<alicloud-StorageClass>`. For more information, see the Alibaba Cloud documentation for [StorageClass](https://www.alibabacloud.com/help/en/ack/ack-managed-and-ack-dedicated/user-guide/use-dynamically-provisioned-disk-volumes#a7d035fc3cijx).)

4. Install Console.

















AskCopy



```
     $ helm install twistlock-console \
       --namespace twistlock \
       ./twistlock-console-helm.tar.gz
```

5. Change the PersistentVolumeClaim’s reclaimPolicy.

















AskCopy



```
     $ kubectl get pv
     $ kubectl patch pv <pvc-name> -p '{"spec":{"persistentVolumeReclaimPolicy":"Retain"}}'
```

6. Get the public endpoint address for Console. When the service is fully up, the LoadBalancer’s IP address is shown.

















AskCopy



```
     $ kubectl get service -w -n twistlock
```

7. Open a browser window, and navigate to Console. By default, Console is served on HTTPS on port 8083 of the `LoadBalancer`:

















AskCopy



```
https://<LOADBALANCER_IP_ADDR>:8083
```

8. Configure the console as described in [Configure the Prisma Cloud Console](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-kubernetes#configure-console-k8s).


[PreviousDeploy the Prisma Cloud Console on Onebox](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-onebox) [NextDeploy the Prisma Cloud Console on ACS](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-acs)

Last updated 3 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
