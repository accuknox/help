For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/continuous-integration/jenkins-plugin.md).

The Jenkins plugin for Prisma Cloud enables you to scan container images, code repositories, and serverless functions for security vulnerabilities and compliance issues within your continuous integration pipeline.

We support the current and previous two major releases with our defenders and plugins. Please note, the Prisma Cloud console is backward compatible with up to two (N-2) major releases (including all minor versions) with the Jenkins plugin.

- The Jenkins plugin is built for Jenkins on Linux. To scan images with Jenkins on other operating systems, use a platform-specific [twistcli binary](https://docs.prismacloud.io/admin-guide/tools/twistcli-scan-images).


While the Jenkins plugin doesn’t support scanning Windows images for vulnerability and compliance issues on hosts with the ``containerd``` runtime, however, the Jenkins plugin does support scanning when running on hosts with Docker Engine and Podman.

## Build and scan flow[Direct link to heading](https://docs.prismacloud.io/admin-guide/continuous-integration/jenkins-plugin\#build-and-scan-flow)

After Jenkins builds a container image or serverless function package, the Prisma Cloud Jenkins plugin scans it for vulnerabilities and compliance issues.

Prisma Cloud can pass or fail builds, depending on the types of issues discovered, and the policies you have defined in Console. By incorporating scanning into the build phase of the development workflow, developers get immediate feedback about what needs to be fixed. The scan report provides all the information required to fix the vulnerabilities that were identified in the scan.

The sequence of events is described below:

1. A developer commits a change, which triggers a build.

2. Jenkins builds the container image.

3. Jenkins calls the Prisma Cloud plugin for scanning. The plugin collects data about the image, including the packages and binaries in the image, and submits it to console for analysis.

4. The console returns a list of vulnerabilities and compliance issues.

5. The Prisma Cloud plugin passes or fails the build, depending on your policy.











For more information about configuring a scan, see: [Setting up a Freestyle project](https://docs.prismacloud.io/admin-guide/continuous-integration/jenkins-freestyle-project), [Setting up a Maven project](https://docs.prismacloud.io/admin-guide/continuous-integration/jenkins-maven-project), or [Setting up a Pipeline project](https://docs.prismacloud.io/admin-guide/continuous-integration/jenkins-pipeline-project).











For more information about targeting rules created in Console to the Jenkins plugin, see [Set policy in the CI plugins](https://docs.prismacloud.io/admin-guide/continuous-integration/set-policy-ci-plugins).

6. You can view the scan results in:









   - The Jenkins tool, including the project/job page and dashboard view.

   - Prisma Cloud Console, in the **Monitor > Vulnerabilities > {Images \| Functions} > CI** pages.


When scanning multiple images in a single build, results do not appear correctly in the Jenkins dashboard view or vulnerability trends table/graph. Only trend data for the last image scanned is shown. Instead, go to the Console to see scan results for all images in the build.

## Installing the Prisma Cloud Jenkins plugin[Direct link to heading](https://docs.prismacloud.io/admin-guide/continuous-integration/jenkins-plugin\#installing-the-prisma-cloud-jenkins-plugin)

**Prerequisites:**

- Your version of Jenkins meets the minimum [system requirements for Prisma Cloud Jenkins plugin](https://docs.prismacloud.io/admin-guide/install/system-requirements#jenkins).

- To implement a Jenkins plugin, install the [Matrix project](https://plugins.jenkins.io/matrix-project/) plugin.

- You have installed Prisma Cloud Console on a host in your environment.

- Your Jenkins host can reach Prisma Cloud Console over the network.

- We recommend adding a Prisma Cloud user with the _CI User_ role to minimize privileges on Console. For more information, see [user roles](https://docs.prismacloud.io/admin-guide/authentication/user-roles).


1. Open the Jenkins top page.

2. Install the Prisma Cloud Jenkins plugin.











The Jenkins plugin can be downloaded directly from Console ( **Manage > System > Utilities**).









1. Click **Manage Plugins** (in the left menu bar) and then click the **Advanced** tab.

2. Scroll down to **Upload Plugin**, and click **Choose File**.

3. Navigate to the folder where you unpacked the Prisma Cloud download and select _prisma-cloud-jenkins-plugin.hpi_.

4. Click **Upload**.


3. Configure the Prisma Cloud plugin.









1. Go to the Jenkins top page, and then click **Manage Jenkins** \> **Configure System**.

2. Scroll down to the Prisma Cloud section.















      ![Prisma Cloud plugin config](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-e253da5a40b42d6c886644bd973ac8e58e34040f%252Fprisma_cloud_plugin_config.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=41eea22621cfef96fe610ca87cf81383&sv=3)











      Configuring a proxy:















      ![jenkins proxy 23722](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-25d8c4892f639d421f057ada61f6b066a50dd1f8%252Fjenkins_proxy_23722.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=bf8324be3049bd4fc30c2396e6febf8e&sv=3)

3. In **Choose Proxy Protocol Type**, select the proxy option that is to be used for the plugin to communicate with Console.











      Choose either the default global Jenkins proxy, configure a separate one, or choose to skip any Proxy communication with the 'No Proxy' option. If you choose to configure a separate proxy, fill in the proxy’s address URL, port, username, password, and CA certificate (if any).

4. In **Proxy Address**, enter the URL for Prisma Cloud Console.

5. Enter the Prisma Cloud **Proxy Port**.

6. In **Proxy Username**, enter the **CI role**.

7. Enter the **Proxy Password** with the user’s credentials for Prisma Cloud Console.











      The username is the access key ID and the password is the access key secret of the user with the CI role (Build and Deploy Security permission group with the option to create an access key on Prisma Cloud).

8. Click **Test Connection** to validate that the Jenkins plugin can communicate with Prisma Cloud Console.

9. Select **Save**.


## Scan artifacts[Direct link to heading](https://docs.prismacloud.io/admin-guide/continuous-integration/jenkins-plugin\#scan-artifacts)

When a build completes, you can view the scan results directly in Jenkins. To support integration with other processes and applications in your organization, Prisma Cloud scan reports can be retrieved from several locations.

Full scan reports for the latest build can be retrieved from:

- The scan results file in the project’s workspace (by the name configured in the scan steps).

- The Prisma Cloud API. For more information, see the [`/api/v<VERSION>/scans`](https://pan.dev/compute/api/get-scans/) endpoint for downloading Jenkins scan results.


For example, if you use [ThreadFix](https://threadfix.it/) to maintain a consolidated view of vulnerabilities across all your organization’s applications, you could create a post-build action that triggers ThreadFix’s Jenkins plugin to grab Prisma Cloud Compute’s scan report from the project workspace and upload it to the ThreadFix server. Contact your ThreadFix support team for details on how to ingest this output.

To download the scan report from Console using the Prisma Cloud API, use the following command:

AskCopy

```
$ curl -k \
  -u <COMPUTE_CONSOLE_USER> \
  https://<COMPUTE_CONSOLE>/api/v1/scans/download?search=<IMAGE_NAME> \
  > scan_report.csv
```

=== If you see the following error in the build console output in Jenkins: "No CA certificate was specified, using insecure connection".

This is becasue, by default, the `twistcli` binary checks the trust chain of the Prisma console.

**Solution**: To establish the trust between the Jenkins plugin and Prisma Console, run `twistlcli` binary with `--tlscacert PATH` flag to specify the path to the Prisma Cloud CA certificate file.

Although, Jenkins plugin doesn’t provide an option to pass the CA certificate path, however, the connection between Jenkins and Console is still encrypted with TLS. ===

## Ignore image creation time[Direct link to heading](https://docs.prismacloud.io/admin-guide/continuous-integration/jenkins-plugin\#ignore-image-creation-time)

A common stumbling point is the "Ignore Image Build Time" option. This option checks the time the image was created against the time your Jenkins build started. If the image was not created after the start of your current build, the scan is bypassed. The plugin, by default, scans any image generated as part of your build process but ignores images not created or updated as part of the build.

As per the Docker’s creation time for images, if the image is not changed, the creation time isn’t updated. This could lead to a scenario where an image is built and scanned in one job, but not scanned in subsequent jobs because the creation time wasn’t updated as the image didn’t change.

## Post-build cleanup[Direct link to heading](https://docs.prismacloud.io/admin-guide/continuous-integration/jenkins-plugin\#post-build-cleanup)

Most of the CI pipelines push images to the registry after passing vulnerability and compliance scan steps of Prisma Cloud. Pipelines also have a final cleanup step that removes images from the local Docker cache. If your build fails, and the pipeline is halted, use a **post** section to clean up the Docker cache. The **post** section of a pipeline is guaranteed to run at the end of a pipeline’s execution.

For more information, see the [Jenkins documentation](https://jenkins.io/doc/pipeline/tour/post/).

## What’s next?[Direct link to heading](https://docs.prismacloud.io/admin-guide/continuous-integration/jenkins-plugin\#whats-next)

Set up a build job and configure Prisma Cloud to scan the Docker image generated from the job.

For more information, see:

- [Jenkins Freestyle project](https://docs.prismacloud.io/admin-guide/continuous-integration/jenkins-freestyle-project)

- [Jenkins Maven project](https://docs.prismacloud.io/admin-guide/continuous-integration/jenkins-maven-project)

- [Jenkins Pipeline project](https://docs.prismacloud.io/admin-guide/continuous-integration/jenkins-pipeline-project)


Notifications of build failures can be enabled using existing Jenkins plugins, for example:

- [Mailer plugin](https://plugins.jenkins.io/mailer)

- [Jira plugin](https://plugins.jenkins.io/jira)

- [Slack plugin](https://plugins.jenkins.io/slack)


[PreviousContinuous integration](https://docs.prismacloud.io/admin-guide/continuous-integration/continuous-integration) [NextJenkins Freestyle project](https://docs.prismacloud.io/admin-guide/continuous-integration/jenkins-freestyle-project)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
