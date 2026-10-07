For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/tools/twistcli-console-install.md).

When twistcli installs Console into a Kubernetes or OpenShift cluster, it executes a series of steps. To help you troubleshoot issues when twistcli fails, the steps in the install flow are described here:

When you run `twistcli console install`, it:

01. Loads the Console image on localhost, and tags it with the registry address.

02. Deletes the old Console replication controller, if it exists, and waits for Console deletion.

03. Deletes the config map, if it exists.

04. Creates Prisma Cloud namespace, if it does not exist.

05. If the service does not exist, twistcli resolves the service template to a file and creates a new service.

06. If persistent volume claim (PVC) does not exist, twistcli resolves the PVC template to a file and creates a new PVC.

07. Waits to the PVC to bind to a persistent volume resource. twistcli expects that the persistent volume has already been created by the user. Note that the PVC is not deleted and recreated because once the PVC is be deleted, it cannot bind again to the persistent volume without recreating the persistent volume.

08. Retrieves the service IPs (Cluster IPs, and adds them to the SAN.

09. Creates a config map.

10. Resolves Console template to a file, and creates a Console replication controller.

11. Deletes the working directory.


[PreviousScan code repos with twistcli](https://docs.prismacloud.io/admin-guide/tools/twistcli-scan-code-repos) [NextUpdate offline environments](https://docs.prismacloud.io/admin-guide/tools/update-intel-stream-offline)

Last updated 3 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
