For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/install/deploy-defender/orchestrator/install-tas-defender.md).

Prisma Cloud deploys the Defender on the VMware Tanzu Application Service (TAS) as add-on software, which works similarly to a Daemon set in Kubernetes. This approach co-locates the Defender on every Diego cell VM. The "Prisma Cloud for TAS" tile in the Tanzu Ops Manager allows you to configure the Defender across your TAS environment. When you deploy full coverage Defenders for TAS, they perform blobstore scanning alongside compliance, vulnerability, and runtime protection. If you have a large-scale environment, you can choose to deploy blobstore scanning Defenders as dedicated VMs that focus exclusively on scanning your blobstores.

Tanzu Application Service (TAS) Defender supports the following functions:

- Vulnerability scanning for running apps.

- Vulnerability and compliance scanning for the underlying Diego cell hosts.

- Blobstore scanning for Linux droplets.

- Runtime protection: Linux TAS Defenders support runtime protection for process, networking, and file system. Windows TAS Defenders support runtime protection for process.


The Prisma Cloud Console lets you deploy Defender to multiple TAS environments. TAS Defender supports the prevent action because it doesn’t require controlling the app lifecycle. The TAS Defenders don’t support the block action for runtime rules, vulnerability rules, and compliance rules because the Defenders cannot block running apps. The TAS framework controls the app lifecycle, including stopping the containers as required by the block action.

## Install the TAS Defender[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/orchestrator/install-tas-defender\#install-the-tas-defender)

1. Get the Prisma Cloud tile.









1. Log in to the Prisma Cloud console.

2. Select **Manage > Defender > Deployed Defenders**.

3. Click **Manual deploy**.

4. Select the **Orchestrator** deployment method.

5. Under **Orchestrator type**, select one of the following options:









      - Tanzu Application Service Defender - Linux

      - Tanzu Application Service Defender - Windows


6. On the sidebar, click the **Download** button to get the TAS tile.











      Alternatively, you can download the **VMWare Tanzu tile** from under **Manage > System > Utilities**.


2. Import the Prisma Cloud tile.









1. Go to the **Tanzu Ops Manager > Installation Dashboard**.

2. Click the **Import a Product** button.

3. Select the downloaded tile.

4. On the left sidebar, the Prisma Cloud for TAS appears.

5. Click the **plus sign** beside the version number to stage the tile.

6. Click the tile that was added.


3. Configure the Defenders.









1. Return to the Prisma Cloud Console.

2. Under **The name that Defender will use to connect to this Console**, select the IP address or URL that your TAS environment can reach.

3. If you selected the **Tanzu Application Service Defender - Windows** as the **Orchestrator type**, enable or disable **Runtime protection**.

4. Enable the **Assign globally unique names to Hosts** in the **Advanced Settings** as needed.

5. Copy the installation scripts from the sidebar. You can deploy Prisma Cloud Defenders on Linux and Windows.


4. Configure the Prisma Cloud tile.









01. Return to the Tanzu Ops Manager.

02. Under **Assign AZs and Networks**, select the **TAS network** and select **Save**.

03. Under **Prisma Cloud Component Configuration**, paste the installation scripts for the operating systems you are using.











       If you don’t provide an installation script, Tanzu doesn’t deploy Defenders for that operating system.











       Enter a **Foundation** name (optional). If you don’t enter a Foundation name, you will not be able to use **tas-foundation** label in **Manage > Collections**.











       Select **Save**.

04. Under **Prisma Cloud Proxy configuration**, configure your Proxy as needed if you are using Linux.











       Select **Save**.











       The Defender on Windows doesn’t support a proxy.

05. Under **Credentials**, provide your Prisma Cloud credentials for Linux and Windows. Select **Save**. You can use certificates for authentication if you only use Linux. Provide your username and password credentials instead to authenticate the Defender if you use Windows Defenders by themselves or together with Linux Defenders.

06. Under **Resource configuration**, you can add dedicated Linux VMs to serve exclusively as Linux blobstore scanners. Select **Save**.

07. Go back to the **Installation Dashboard**.

08. Click Review Pending Changes.

09. Select the following products.









       - Prisma Cloud for TAS

       - VMWare Tanzu Application Service

       - Every TAS Isolation segment in your environment.


10. Apply the changes and wait for the tile to become active.











       It can take an hour or longer for the changes to apply and your deployment to complete.


5. Verify the deployment on Prisma Cloud under **Manage > Defenders**.











After the deployment is complete, the deployed Defenders will appear in the table. The **Host** column shows **Agent ID** of the defended Linux Diego cells and **VM CID** of the defended Windows Diego cells.











You can search and filter your TAS Defenders based on the hostnames.









1. To fetch the **Agent ID** of your Diego cells:









      1. Log into a Diego cell.

      2. The `/var/vcap/instance/dns/records.json` file shows how the **Agent ID** maps to a host IP address.


2. To fetch the **VM CID** of your Diego cells, run `bosh vms` in the **ops-manager** VM.


## Deploy Blobstore Scanners for TAS[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/orchestrator/install-tas-defender\#deploy-blobstore-scanners-for-tas)

Prisma Cloud for TAS can perform blobstore scanning on Linux VMs. Defenders deployed as dedicated blobstore scanners still scan the host where they run for vulnerabilities, compliance issues, and runtime protection. Prisma Cloud periodically discovers and scans the droplets in your blobstores for vulnerabilities using pattern matching.

01. Go to the **Tanzu Ops Manager > Installation Dashboard**.

02. Click the **Prisma Cloud for TAS** tile.

03. Under **Prisma Cloud Component Configuration**, paste the Linux installation script. If you don’t provide an installation script, Tanzu doesn’t deploy Defenders.











    If you are deploying only TAS Linux blobstore scanners you can unselect the **Install TAS Defender on all Linux Diego cells in the cluster** checkbox.











    Select **Save**.

04. Go to **Resource Configuration**.











    Specify the number of instances of blobstore scanners you want in your environment.

05. Select the **VM TYPE**.

06. Select the **PERSISTENT DISK TYPE**.

07. Provide any load balancing configuration needed.

08. Select whether an internet connection is allowed by the Blobstore scanner VM.











    Select **Save**.

09. Under **Assign AZs and Networks**, select the TAS network and specify the preferred AZs for placing the blobstore scanners.











    Select **Save**.

10. Return to the **Installation Dashboard**.

11. Click **Review Pending Changes**, and select **Prisma Cloud for TAS**.











    Apply the changes. Wait for Tanzu to finish deploying the Defenders. This process can take a long time.

12. Configure Prisma Cloud to [scan a blobstore](https://docs.prismacloud.io/admin-guide/vulnerability-management/vmware-tanzu-blobstore).


[PreviousDeploy Defenders as DaemonSets](https://docs.prismacloud.io/admin-guide/install/deploy-defender/orchestrator/install-kubernetes-cri) [NextDeploy Defender on Google Kubernetes Engine (GKE)](https://docs.prismacloud.io/admin-guide/install/deploy-defender/orchestrator/install-gke)

Last updated 3 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
