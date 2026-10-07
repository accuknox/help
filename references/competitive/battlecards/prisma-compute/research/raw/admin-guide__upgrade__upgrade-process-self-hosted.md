For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/upgrade/upgrade-process-self-hosted.md).

Prisma Cloud Console is backward compatible with up to two (n-2) major releases back (including all minor versions) for the following:

- All types of Defenders.

- Twistcli/Jenkins plugin.


When using projects, the same versions of `master` and `tenant` consoles are required.

## Upgrade and Notifications[Direct link to heading](https://docs.prismacloud.io/admin-guide/upgrade/upgrade-process-self-hosted\#upgrade-and-notifications)

The currently installed version of the Console is displayed in the bell menu. The Console notifies you when new versions of Prisma Cloud are available, and these notifications are displayed in the top right corner of the Console.

![upgrade compute version](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-2edf3ebec8b1e9887183351307241cbd3bc30bfc%252Fupgrade_compute_version.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=d85e9a40de19800304f73a35e19d569a&sv=3)

The versions of your deployed Defenders are listed under **Manage > Defenders > Defenders: Deployed**:

![upgrade defender version](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-4dfb016f46c5bb6bf8c353fee8170c8f14198126%252Fupgrade_defender_version.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=c916ee9135d8cc82df4888342b119ca2&sv=3)

## Upgrade Process[Direct link to heading](https://docs.prismacloud.io/admin-guide/upgrade/upgrade-process-self-hosted\#upgrade-process)

The release images for Console and Defender are built from the UBI8-minimal base image, the upgrade is a full container image upgrade and the old container is replaced with a new container. You can upgrade the Console without losing any of your data or configurations because Prisma Cloud stores state information outside the container, all your rules and settings are immediately available to the upgraded Prisma Cloud containers.

Prisma Cloud state information is stored in a database in the location specified by DATA\_FOLDER, which is defined in _twistlock.cfg_. By default, the database is located in the _/var/lib/twistlock_ path.

The steps in the upgrade process are:

1. Upgrade Console.











When upgrading Console, if you are on two versions previous (n-2) to the latest (n), you must first upgrade to the most recent (n-1) version, and then upgrade to the latest version.











If you are on (n-1) version, then you can upgrade to the latest (n) version.

2. Go to **Manage > Defenders > Defenders: Deployed** and filter by **Upgrade Required** to upgrade all the listed Defenders.











After you upgrade Console, upgrade Defenders that have reached the end of the support lifecycle. You must first

3. Validate that all deployed Defenders have been upgraded.

4. Upgrade the Jenkins plugin, if required.











To download the latest version of all other Prisma Cloud Compute components (such as the Jenkins plugin), either go to **Manage > System > Utilities** to download the latest versions or retrieve them using the API.


## Upgrading Console when Using Projects[Direct link to heading](https://docs.prismacloud.io/admin-guide/upgrade/upgrade-process-self-hosted\#upgrading-console-when-using-projects)

When you have one or more [tenant projects](https://docs.prismacloud.io/admin-guide/deployment-patterns/projects), upgrade all Supervisor Consoles before upgrading the Central Console. During the upgrade process, there may be times when the supervisors appear disconnected. This is normal because supervisors are disconnected while the upgrade occurs and the central console will try to reestablish connectivity every 10 minutes. Within 10 minutes of upgrading all supervisors and the Central Console, all supervisors should appear healthy.

Except during the upgrade process, the Central Console and all Supervisor Consoles must run the same product version. Having different product versions is not supported and may lead to instability and connectivity problems.

Upgrade each Supervisor and then the Central Console using the appropriate procedure:

- [Console - Onebox](https://docs.prismacloud.io/admin-guide/upgrade/upgrade-onebox)

- [Console - Kubernetes](https://docs.prismacloud.io/admin-guide/upgrade/upgrade-kubernetes)

- [Console - OpenShift](https://docs.prismacloud.io/admin-guide/upgrade/upgrade-openshift)

- [Console - Helm](https://docs.prismacloud.io/admin-guide/upgrade/upgrade-helm)

- [Console - Amazon ECS](https://docs.prismacloud.io/admin-guide/upgrade/upgrade-amazon-ecs)


[PreviousSupport lifecycle](https://docs.prismacloud.io/admin-guide/upgrade/support-lifecycle) [NextOnebox](https://docs.prismacloud.io/admin-guide/upgrade/upgrade-onebox)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
