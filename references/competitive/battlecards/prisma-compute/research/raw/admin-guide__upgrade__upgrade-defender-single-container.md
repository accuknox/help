For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/upgrade/upgrade-defender-single-container.md).

The Console user interface lets you upgrade all Defenders in a single shot. This method minimizes the effort required to upgrade all your deployed Defenders.

Alternatively, you can select whisch Defenders to upgrade. Use this method when you have different maintenance windows for different deployments. For example, you might have an open window on Tuesday to upgrade thirty Defenders in your development environment, but no available window until Saturday to upgrade the remaining twenty Defenders in your production environment. In order to give you sufficient time to upgrade your environment, older versions of Defender can coexist with the latest version of Defender and the latest version of Console.

**Prerequisites:** You have already upgraded Console.

1. Open Console.

2. On **Manage > Defender > Manage** and select **Defenders** to see a list of all your deployed stand-alone Container Defenders.

3. Upgrade your stand-alone Defenders. You can either:









   - Select **Upgrade all** to upgrade all Defenders at the same time.

   - On **Actions** select **Upgrade** corresponding to individual Defenders to upgrade a subset of your Defenders.











     The **Restart** and **Decommission** buttons are not available for DaemonSet Defenders. They are only available for stand-alone Defenders.


[PreviousAmazon ECS](https://docs.prismacloud.io/admin-guide/upgrade/upgrade-amazon-ecs) [NextManually upgrade Defender DaemonSets](https://docs.prismacloud.io/admin-guide/upgrade/upgrade-defender-daemonset)

Last updated 3 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
