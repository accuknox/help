For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/compliance/manage-compliance.md).

Prisma Cloud can monitor and enforce compliance settings across your environment. Out of the box, Prisma Cloud supports hundreds of discrete checks that cover images, containers, hosts, clusters, and clouds.

Prisma Cloud provides predefined checks that are based on industry standards, such as the CIS benchmarks, as well as research and recommendations from Prisma Cloud Labs. Your security teams can review these best practices and enable the ones that align with your organization’s security mandate and consistently enforce them across your environment. Additionally, you can implement your own compliance checks with [scripts](https://docs.prismacloud.io/admin-guide/compliance/custom-compliance-checks).

## Enforcement[Direct link to heading](https://docs.prismacloud.io/admin-guide/compliance/manage-compliance\#enforcement)

Compliance rules are defined and applied in the same way as vulnerability rules. When there is no matching rule for compliance checks on specific resources, Prisma Cloud generates alerts on all violations that are found. For checks that can be performed on static images, those checks are performed as images are scanned (either in the registry or on local hosts). Results are then displayed in the compliance reports under **Monitor > Compliance** on the Console.

When compliance rules are configured with block actions, they are enforced when a container is created. If the instantiated container violates your policy, Prisma Cloud prevents the container from being created.

Note that compliance enforcement is only one part of a defense in depth approach. Because compliance enforcement is applied at creation time, it is possible that a user with appropriate access could later change the configuration of a container, making it non-compliant after deployment. In these cases, the runtime layers of the defense-in-depth model provide protection by detecting anomalous activity, such as unauthorized processes.

Assume that you want to block any container that runs as root. The flow for blocking such a container is:

1. Prisma Cloud admin creates a new compliance rule that blocks containers from running as root.

2. The admin optionally targets the rule to a specific resources, such as a set of hosts, images, or containers.

3. Someone with rights to create containers attempts to deploy a container to the environment.

4. Prisma Cloud compares the image being deployed to the compliance state that it detected when it scanned the image. For deploy-time parameters, the specific Docker client commands sent are also analyzed.









1. If the comparison determines that the image is compliant with the policy, the 'docker run' command is allowed to proceed as normal, and the return message from Docker Engine is sent back to the user.

2. If the comparison determines that the image is not compliant, the container\_create command is blocked and Prisma Cloud returns an error message back to the user describing the violation.


5. In both success and failure cases, all activities are centrally logged in Console and (optionally) syslog.


## Supported runtimes[Direct link to heading](https://docs.prismacloud.io/admin-guide/compliance/manage-compliance\#supported-runtimes)

The supported runtimes for compliance are:

- Docker

- CRIO

- Containerd


## Surveying Prisma Cloud compliance checks[Direct link to heading](https://docs.prismacloud.io/admin-guide/compliance/manage-compliance\#surveying-prisma-cloud-compliance-checks)

As you configure your compliance policy, you might want more details for the built-in checks. Teams that address compliance issues might also need more information about why checks fail, so that they can resolve the underlying issues.

As you explore the built-in checks, consider the following points.

### CIS[Direct link to heading](https://docs.prismacloud.io/admin-guide/compliance/manage-compliance\#cis)

Most built-in checks are based on the [CIS benchmarks](https://docs.prismacloud.io/admin-guide/compliance/cis-benchmarks). For full details about what a check does, and why, refer to the CIS benchmark documentation. Prisma Cloud check IDs map to CIS benchmark IDs. For example, Prisma Cloud check ID 51 maps to CIS Docker Benchmark 5.1

### Check IDs[Direct link to heading](https://docs.prismacloud.io/admin-guide/compliance/manage-compliance\#check-ids)

When creating compliance rules, there’s a drop-down menu that lets you filter checks by type. Each type has a heading, which indicates the origin of the checks. Checks from the CIS benchmarks are clearly labeled.

![manage compliance dropdown](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-1751122119ba4ae9236979959df01c144e290c34%252Fmanage_compliance_dropdown.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=9b1282038ee1ed144bb6bf256fbd4777&sv=3)

### CRI checks[Direct link to heading](https://docs.prismacloud.io/admin-guide/compliance/manage-compliance\#cri-checks)

All CRI checks are direct analogs of the Docker CIS checks, but repurposed for CRI environments.

### Twistlock Labs checks[Direct link to heading](https://docs.prismacloud.io/admin-guide/compliance/manage-compliance\#twistlock-labs-checks)

For all other checks, including those from Twistlock Labs, we provide documentation.

- Twistlock Labs compliance checks for [containers, images, Istio, and Linux hosts](https://docs.prismacloud.io/admin-guide/compliance/prisma-cloud-compliance-checks).

- Twistlock Labs compliance checks for [serverless functions](https://docs.prismacloud.io/admin-guide/compliance/serverless).

- Twistlock Labs compliance checks for [Windows](https://docs.prismacloud.io/admin-guide/compliance/windows).


## Creating compliance rules[Direct link to heading](https://docs.prismacloud.io/admin-guide/compliance/manage-compliance\#creating-compliance-rules)

This procedure shows you how to set up a container compliance rule to block any containers running as root.

1. Open Console, then go to **Defend > Compliance > Containers and Images**.

2. Click **Add rule**.









1. Enter a rule name, such as **my-rule**.

2. In the search field under **Compliance actions**, enter **Container is running as root**.











      As you type, the available checks are filtered to match your search query.

3. For check 599 (Container is running as root), set the action to **Block**.











      The "Block" effect for the unsupported compliance policies is disabled in the UI and set to "Ignore" and "Alert" only.

4. In **Scope**, accept the default collection, **All**. The default collection applies the rule to all containers in your environment.

5. Click **Save**.











      Your rule is now activated.


3. Verify that your rule is being enforced.









1. Connect to a host running Defender, then run the following command, which starts an Ubuntu container with a root user (uid 0).

















      AskCopy



      ```
      $ docker run -u 0 -ti library/ubuntu /bin/sh
      ```









      Defender should block the command with the following message:

















      AskCopy



      ```
      docker: Error response from daemon: oci runtime error: [Prisma Cloud] Container operation blocked by policy: my-rule, has 1 compliance issues.
      ```


## Reporting full results[Direct link to heading](https://docs.prismacloud.io/admin-guide/compliance/manage-compliance\#reporting-full-results)

By default, Prisma Cloud reports only the compliance checks that fail. Sometimes you need both negative and affirmative results to prove compliance. You can configure Prisma Cloud to report checks that both pass and fail.

The contents of a full compliance report (both passed and failed checks) is the sum of all applied rules. If your compliance policy raises an alert for only two checks, your compliance report will show the results of two checks. To report on _all_ compliance checks, set all compliance checks to either alert or block.

1. Open Console, then go to **Defend > Compliance > {Containers and Images \| Hosts}**.

2. Click **Add rule**.









1. Enter a rule name.

2. Under **Reported results**, click **Passed and Failed Checks**.

3. Click **Save**.











      Your rule is now activated.


3. Verify that the compliance reports show both passed and failed checks.









1. Go to **Defend > Compliance**, select any tab, then click on a resource in the table to open its scan report. You will see a list of checks that have both passed and failed.















      ![manage compliance pass fail](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-bc60935e08313ab3a1ee7dba6cc02fd7f66e6bf0%252Fmanage_compliance_pass_fail.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=54fdc7a51ef5d01881f19ef1e8165b3d&sv=3)


[PreviousCompliance Explorer](https://docs.prismacloud.io/admin-guide/compliance/compliance-explorer) [NextCIS Benchmarks](https://docs.prismacloud.io/admin-guide/compliance/cis-benchmarks)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
