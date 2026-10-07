For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/install/deploy-defender/app-embedded/config-app-embedded-fs-protection.md).

Because App-Embedded Defender’s file system protection could affect workload performance, you can enable or disable it.

This procedure is intended for security teams that want to set a global recommendation for whether file system protection should be enabled when teams deploy App-Embedded Defenders.

By default, file system protection is disabled in App-Embedded Defenders. Security teams can turn it on by default so that teams that build and manage apps will deploy Defender according to your organization’s best practices. Individual teams can optionally override the default setting at embed-time, and they may want to do so if file system protection interferes with their workload’s operation.

1. Log into Console.

2. Go to **Manage > Defenders > Manage > Defenders**.

3. Click **Advanced settings**.

4. Set **Default file system protection statefor App-Embedded Defenders** to **On** or **Off**.















![config app embedded fs protection global](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-8c1ef50c34ba5ee890707f6fbce8eb8212200948%252Fconfig_app_embedded_fs_protection_global.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=c9964e9bbbb93d9e8dd28b278eae1774&sv=3)

5. Validate the global setting has been properly applied by inspecting the Defender embed flow.









1. Go to **Manage > Defenders > Deploy > Defenders**.

2. In **Deployment method**, select **Single Defender**.

3. In **Choose the Defender type**, select **Container Defender - App-Embedded**.

4. Verify that the value for **Monitor file system events** matches the value you set in **Advanced settings**.















      ![config app embedded fs protection deploy](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-b7213b7a5e5baa47586d632d0cf4183ea8b23567%252Fconfig_app_embedded_fs_protection_deploy.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=1e9a74e9033ec3fa21ef4e83fd69600a&sv=3)


[PreviousDefault Setting for App-Embedded Defender File System Monitoring](https://docs.prismacloud.io/admin-guide/install/deploy-defender/app-embedded/config-app-embedded-fs-mon) [NextUpgrade](https://docs.prismacloud.io/admin-guide/upgrade/upgrade)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
