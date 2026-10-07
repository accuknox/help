For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/how-to-guides/openshift-provision-tenant-projects.md).

This guide shows you how to set up tenant projects on Openshift clusters. If you try to provision tenant projects using the [normal provisioning flow](https://docs.prismacloud.io/admin-guide/deployment-patterns/projects), Central Console cannot reach the host where Supervisor Console runs. Failing to follow these steps can lead an 'Internal Server Error', even when everything seems to be set up properly.

![openshift provision tenant projects error](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-b2ce684d539ce64e66dac7f913acd170311b5953%252Fopenshift_provision_tenant_projects_error.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=fe68389b066cc6781ed3850fbfaab2b8&sv=3)

In this example provisioning flow, the DNS names for Central Console and Supervisor Console are:

- Central Console — [https://console.apps.jonathan.lab.twistlock.com](https://console.apps.jonathan.lab.twistlock.com/)

- Supervisor Console to be provisioned — [https://console.39apps.jonathan.lab.twistlock.com](https://console.39apps.jonathan.lab.twistlock.com/)


**Prerequisites:**

- Two fully operational Prisma Cloud Consoles are already deployed. For more information, see the [OpenShift 4](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-openshift) deployment.

- OpenShift external routes to both Consoles' TCP port 8083 (Prisma Cloud UI and API), with the TLS termination type set to passthrough, already exist.

- The to-be Central and Supervisor Consoles are already licensed and you’ve created initial admin users.


1. Designate one Console to be Supervisor and the other to be Central.

2. Log into the Supervisor Console with your admin user.

3. Add the FQDN of the Supervisor Console to the Subject Alternative Name field of the Supervisor Console’s certificate.









1. In the Supervisor Console, go to **Manage > Defenders > Names**.

2. Click **Add SAN**.

3. Add the Supervisor Console’s FQDN. In this example, it is **console.39apps.jonathan.lab.twistlock.com**.

4. Click **Add**.















      ![openshift provision tenant projects san](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-2251e6aa35d41fc138525bb40c2a7528d64ac31d%252Fopenshift_provision_tenant_projects_san.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=7fcc8fc24b7c593c3987c58c970cf6f8&sv=3)


4. Log into the Central Console with your admin user.

5. Enable Projects by going to **Manage > Projects > Manage** and setting **Use Projects** to **On**.

6. Click the **Provision** tab and to provision a tenant Console.









1. Under **Select Project type**, choose **Tenant**.

2. In **Project name**, give your project a name.

3. In **Supervisor address**, add the FQDN of the Supervisor. In this example, it is [https://console.39apps.jonathan.lab.twistlock.com](https://console.39apps.jonathan.lab.twistlock.com/).

4. Add the **Admin credentials for Supervisor**.

5. Click **Provision**.











      Your Supervisor Console should be successfully provisioned.















      ![openshift provision tenant projects provisioned](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-84d9f66e843ae718cf05c42fa391dd5fba6dbcad%252Fopenshift_provision_tenant_projects_provisioned.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=908b05e0d88698036e3b94cf5a3e7bad&sv=3)


[PreviousConfigure Console's listening ports](https://docs.prismacloud.io/admin-guide/how-to-guides/configure-listening-ports) [NextDisable automatic learning](https://docs.prismacloud.io/admin-guide/how-to-guides/disable-automatic-learning)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
