For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/continuous-integration/set-policy-ci-plugins.md).

Prisma Cloud lets you centrally define your CI policy in Console. These policies establish security gates at build-time. Use policies to pass or fail builds, and surface security issues early during the development process.

There are two types of policies you can use to target your CI tool: vulnerability policies and compliance policies. CI rules have the same parameters as the rules for registries and deployed components, letting you evenly enforce policy in all phases of the app lifecycle.

Prisma Cloud offers the following components for integrating with CI tools:

- A native Jenkins plugin.

- A stand-alone, statically compiled binary, called _twistcli_, that can be integrated with any CI tool.


## Vulnerability policy[Direct link to heading](https://docs.prismacloud.io/admin-guide/continuous-integration/set-policy-ci-plugins\#vulnerability-policy)

For more information about the parameters in vulnerability management rules, see [here](https://docs.prismacloud.io/admin-guide/vulnerability-management/vuln-management-rules).

Vulnerability rules that target the build tool can allow specific vulnerabilities by creating an exception and setting the effect to 'ignore'. Block them by creating an exception and setting the effect to 'fail'. For example, you could create a vulnerability rule that explicitly allows CVE-2018-1234 to suppress warnings in the scan results.

Rules take effect as soon as they are saved.

### Create CI Policy for Vulnerabilities[Direct link to heading](https://docs.prismacloud.io/admin-guide/continuous-integration/set-policy-ci-plugins\#create-ci-policy-for-vulnerabilities)

Vulnerability CI policies let you raise alerts or fail builds when images/functions scanned in the CI process have vulnerabilities.

1. Open Console.

2. Go to **Defend > Vulnerabilities > {Images \| Functions} > CI**.

3. Select **Add rule**.















![vulnerabilities ci policy image](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-c3388cd36411b70ce835c8073c22392414bd43a5%252Fvulnerabilities-ci-policy-image.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=b9a57ba1c40f204f9b9dc09635c58acb&sv=3)















![vulnerabilities ci policy functions](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-0b1db058f4e08fb070204c7589364fdcbca99c85%252Fvulnerabilities-ci-policy-functions.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=d399c7cb8adffb7355d7f5456748e9d3&sv=3)

4. Enter a **Rule name** and [configure the rule](https://docs.prismacloud.io/admin-guide/vulnerability-management/vuln-management-rules).

5. Select **Save**.

6. View the scan report under **Monitor > Vulnerabilities > {Images \| Functions} > CI**.


## Compliance policy[Direct link to heading](https://docs.prismacloud.io/admin-guide/continuous-integration/set-policy-ci-plugins\#compliance-policy)

The compliance checks in Prisma Cloud are based on the Center for Internet Security (CIS) Docker Benchmarks. We also provide numerous checks from our [lab](https://docs.prismacloud.io/admin-guide/compliance/prisma-cloud-compliance-checks). You can also implement your own checks using [custom checks](https://docs.prismacloud.io/admin-guide/compliance/custom-compliance-checks).

Compliance rules that target the CI tool can permit specific compliance issues by setting the action to 'ignore'.

Rules take effect as soon as they are saved.

### Create CI Policy for Compliance[Direct link to heading](https://docs.prismacloud.io/admin-guide/continuous-integration/set-policy-ci-plugins\#create-ci-policy-for-compliance)

Compliance CI policies let you monitor, audit, and enforce security and configuration settings for your CI images and functions.

1. Open Console.

2. Go to **Defend > Compliance > {Containers and images \| Functions} > CI**.

3. Select **Add rule**.















![compliance ci policy](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-fa557c697068ae4b5f4707caa401e9276d09b395%252Fcompliance-ci-policy.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=2d5c44838b47fd997b0bc084cd56aaab&sv=3)

4. Enter a **Rule name** and configure the rule to [enforce compliance checks](https://docs.prismacloud.io/admin-guide/compliance/manage-compliance).

5. Select **Save**.

6. View the scan report under **Monitor > Compliance > {Images \| Functions} > CI**.


## Alert Profiles[Direct link to heading](https://docs.prismacloud.io/admin-guide/continuous-integration/set-policy-ci-plugins\#alert-profiles)

To surface critical compliance and vulnerabilities events, you can create [alert profiles](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/compute-edition/34/admin-guide/alerts/alerts.md) for forwarding the alerts to various integrations.

[PreviousJenkins pipeline on K8S](https://docs.prismacloud.io/admin-guide/continuous-integration/jenkins-pipeline-k8s) [NextCode repo scanning](https://docs.prismacloud.io/admin-guide/continuous-integration/code-repo-scanning)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
