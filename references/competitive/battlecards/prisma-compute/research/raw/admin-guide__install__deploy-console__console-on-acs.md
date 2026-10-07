For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-acs.md).

Use the following procedure to install Prisma Cloud in an ACS Kubernetes cluster.

[Microsoft will retire ACS](https://azure.microsoft.com/en-us/updates/azure-container-service-will-retire-on-january-31-2020/) as a standalone service on January 31, 2020.

**Prerequisites**

- You have deployed an [Azure Container Service with Kubernetes](https://docs.microsoft.com/en-us/azure/container-service/kubernetes/) cluster.

- You have installed [Azure CLI 2.0.22](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest) or later on a Linux system.

- You have [downloaded the Prisma Cloud software](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-acs#download-twistlock).


01. Create a persistent volume for your Kubernetes cluster. ACS uses Azure classic disks for the persistent volume. Within the same Resource Group as the ACS instance, create a classic storage group.

02. On a Windows based system use Disk Manager to create an unformatted, 100GB Virtual Hard Disk (VHD).

03. Use [Azure Storage Explorer](https://azure.microsoft.com/en-us/features/storage-explorer/) to upload the VHD to the classic storage group.

04. Make sure the disk is 'released' from a 'lease'.

05. On your Linux host with Azure CLI installed, attach to your ACS Kubernetes Master.

















    AskCopy



    ```
    $ az acs kubernetes get-credentials --resource-group pfoxacs --name pfox-acs
    Merged "pfoxacsmgmt" as current context in /Users/paulfox/.kube/config

    $ kubectl config use-context pfoxacsmgmt
    ```

06. Confirm connectivity to the ACS Kubernetes cluster.

















    AskCopy



    ```
    $ kubectl get nodes
    NAME                    STATUS    ROLES     AGE       VERSION
    k8s-agent-e32fd1a6-0    Ready     agent     4m        v1.7.7
    k8s-agent-e32fd1a6-1    Ready     agent     5m        v1.7.7
    k8s-master-e32fd1a6-0   Ready     master    4m        v1.7.7
    ```

07. Create a file named _persistent-volume.yaml_, and open it for editing.

















    AskCopy



    ```
    apiVersion: v1
    kind: PersistentVolume
    metadata:
      name: twistlock-console
      labels:
        app: twistlock-console
      annotations:
        volume.beta.kubernetes.io/storage-class: default
    spec:
      capacity:
        storage: 100Gi
      accessModes:
    - ReadWriteOnce
azureDisk:
    diskName: pfox-classic-tl-console.vhd
    diskURI: https://pfoxacs.blob.core.windows.net/twistlock-console/pfox-classic-tl-console.vhd
    cachingMode: ReadWrite
    fsType: ext4
    readOnly: false
```

`diskName`

Name of the persistent disk created in the previous steps.

`labels`

Label for the persistent volume.

`diskURI`

Azure subscription path to the disk created in the previous steps.

08. Create the persistent volume:

















    AskCopy



    ```
      $ kubectl create -f ./persistent-volume.yaml
    ```

09. Generate the Console YAML configuration file:

















    AskCopy



    ```
      $ /linux/twistcli console export kubernetes \
        --persistent-volume-labels app:twistlock-console \
        --storage-class default
    ```



























    `--persistent-volume-labels`



















    _app:twistlock-console_ label defined in the persistent-volume.yaml.























    `--storage-class`



















    _default_ must match the storage class of the Azure Disk.

10. Deploy the Prisma Cloud Console in your cluster.

















    AskCopy



    ```
      $ kubectl create -f ./twistlock-console.yaml
    ```

11. Wait for the service to come up completely.

















    AskCopy



    ```
      $ kubectl get service -w -n twistlock
    ```

12. Configure the console as described in [Configure the Prisma Cloud Console](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-kubernetes#configure-console-k8s).


[PreviousDeploy the Prisma Cloud Console on ACK](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-ack) [NextDeploy the Prisma Cloud Console on AKS](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-aks)

Last updated 3 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
