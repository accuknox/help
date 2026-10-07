For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/install/deploy-defender/app-embedded/config-app-embedded-fs-mon.md).

This procedure is intended for security teams that want to set a global recommendation for whether file system monitoring should be enabled when teams deploy App-Embedded Defenders.

By default, file system monitoring is disabled in App-Embedded Defenders. Security teams can turn it on by default so that the teams that build and manage apps will deploy Defender according to your organization’s best practices. Individual teams can optionally override the default setting at embed-time, and they may want to do so if file system monitoring interferes with their workload’s operation.

1. Log into Console.

2. Go to **Manage > Defenders > Manage > Defenders**.

3. Click **Advanced settings**.

4. Set **Default app-embedded file system monitoring** to **On** or **Off**.

5. Validate the global setting has been properly applied by inspecting the Defender embed flow.









1. Go to **Manage > Defenders > Deploy > Defenders**.

2. In **Deployment method**, select **Single Defender**.

3. In **Choose the Defender type**, select **Container Defender - App-Embedded**.

4. Verify that the value for **Monitor file system events** matches the value you set in **Advanced settings**.


[PreviousDeploy App-Embedded Defender in GCR](https://docs.prismacloud.io/admin-guide/install/deploy-defender/app-embedded/deploy-app-embedded-defender-gcr) [NextDefault Setting for App-Embedded Defender File System Protection](https://docs.prismacloud.io/admin-guide/install/deploy-defender/app-embedded/config-app-embedded-fs-protection)

Last updated 3 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
