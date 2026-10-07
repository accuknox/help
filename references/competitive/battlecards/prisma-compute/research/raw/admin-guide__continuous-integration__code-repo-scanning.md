For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/continuous-integration/code-repo-scanning.md).

Both twistcli and the Jenkins plugin can evaluate package dependencies in your code repositories for vulnerabilities.

The runtimes supported are:

- Go

- Java

- Node.js

- Python

- Ruby


## Integrate code scanning into CI builds[Direct link to heading](https://docs.prismacloud.io/admin-guide/continuous-integration/code-repo-scanning\#integrate-code-scanning-into-ci-builds)

Point the Jenkins plugin to your code repo in the build directory.

**Prerequisites:** You’ve [installed and configured the Prisma Cloud Jenkins plugin](https://docs.prismacloud.io/admin-guide/continuous-integration/jenkins-plugin).

1. In your Jenkins job configuration, click **Add build step**, and select **Scan Prisma Cloud Code Repositories**.

2. Configure the repo scan.















![code repo scanning config scan](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-95a88e65d7f07b1ab12821b58e1ceb290bab7025%252Fcode_repo_scanning_config_scan.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=95d71fd506db34bea3da26ea8502ebb8&sv=3)









1. In **Repository Name**, specify the name to be used when reporting the results in Console.

2. In **Repository path**, specify the path to the repo in the build directory.











      For example, it could simply be the current working directory (`.`) or some relative directory.


3. Click **Save**, and then execute a build job.











To see the scan results, log into Console, and go to **Monitor > Vulnerabilities > Code repositories > CI**. Prisma Cloud evaluates the contents of the repo according to the policy you’ve specified in **Defend Vulnerabilities > Code repositories > CI**. Prisma Cloud ships with a single default rule that alerts on all vulnerabilities.















![code repo scanning results](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-8ce5bac3d64b09a914980b7824fb69940bf1d448%252Fcode_repo_scanning_results.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=7b05141f5e0e35c76f74aa38d81f661d&sv=3)


[PreviousSet policy in the CI plugins](https://docs.prismacloud.io/admin-guide/continuous-integration/set-policy-ci-plugins) [NextWeb-Application and API Security (WAAS)](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
