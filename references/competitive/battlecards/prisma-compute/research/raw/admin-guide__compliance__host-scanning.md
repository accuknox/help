For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/compliance/host-scanning.md).

Prisma Cloud scans all hosts for compliance issues, provided that a defender is installed or the host is covered by an agentless scan. Among these, the following compliance issues are covered.

- **Host configuration**: Compliance issues in the host setup.

- **Docker daemon configuration**: Compliance issues that stem from misconfiguring your Docker daemons. Docker daemon derives its configuration from various files, including /etc/sysconfig/docker or /etc/default/docker. Misconfigured daemons affect all container instances on a host.

- **Docker daemon configuration files**: Compliance issues that arise from improperly securing critical configuration files with the correct permissions.

- **Docker security operations**: Recommendations and reminders for extending your current security best practices to include containers.











Prisma Cloud implements the checks from:

- CIS Distribution Independent Linux v2.0.0.

- CIS Amazon Linux 2 Benchmark v1.0.0 (for AL 2)

- CIS Amazon Linux Benchmark v2.1.0 (for AL 1)









  - Compliance - For Linux hosts that have Defenders installed, you can also ensure adherence to specific application versions. Agentless scanning on hosts does not support this functionality.


## Enforce Application Control[Direct link to heading](https://docs.prismacloud.io/admin-guide/compliance/host-scanning\#enforce-application-control)

If you want to ensure that Linux hosts in your deployment are running versions of an application that you have allowed or cannnot run versions of applications that you want to deny, you can use the Application Control checks. Application control checks can generate alerts if a non-compliant version of the application is detected on a host.

The most common uses are for : \* Enforce dedicated rules by application type. For example, control what versions of mysql can be running on a DB Server. \* Specify which applications you want to make sure are not allowed to run on hosts (for example, detect any version of mongodb and deny it) \* Create host profiles from a host that has the approved list of applications and apply the rule on all other hosts, so you are alerted when a version is changed.

To enforce application control, the host must have a Defender installed. The Host Defender scans periodically for the application control checks, and matches against the application control list attached to a compliance policy rule to allow or deny applications on the hosts in your environment.

The application control checks are evaluated only for the list of applications and the versions you have specified for match. When an application is not matched, there is no compliance enforcement for it.

Application control is supported for services with an open TCP port. You can view the list of applications for which you can enforce compliance on "Monitor > Compliance > Hosts> Hosts", and on the "Host Details > Package Info", the **App control** column lists the application running on the host and indicates Yes if it is supported for application control.

1. Add an application control list.









1. Select "Defend > Compliance > Hosts > Application control".

2. Enter a Name and optionally a Description for the application control rule.

3. Assign a Severity for the rule. The severity of the alert helps you triage issues when a compliance violation occurs.

4. Pick one of the following options to add the applications.











      This rule defines the match criteria for verifying the list of applications that are running on Linux hosts with Defenders installed.









      1. Option 1 - **Add application**.









         1. Enter the name for this application.

         2. Add the match criteria for the versions you want to allow (this is an allow list).











            Create distinct rules that are specific to an application. For example, a database application or a web application that you want to monitor on the hosts in your inventory and trigger an alert when a compliance violation occurs. You can use `>`, `==` or `⇐`, or something like `>=2 AND ⇐5` to indicate a range between 2 and 5 (including 2 and 5). Alternatively, select **Deny all versions**, if you want to ensure that no version of the application should run on hosts in your environment.















            ![scale:30](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-90066c00b24330a2e425bbf60b6d0606beeddec8%252Fapplication-host-control-add1.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=05afbdfd282c593a7f590c1570a10af0&sv=3)















            ![scale:30](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-ab679875e05f0d0456f33144ae033495273e11e1%252Fapplication-host-control-add2.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=78ac0135eabdbf68d9457507248840c4&sv=3)


      2. Option 2 - **Import from host**.











         If you have a standard image on a specific host and the applications running on that host are what you want to monitor and verify compliance for, you do not have to create the rules manually. Users can import the list of applications along with the versions that are running on the host and automatically create the application control rules.









         1. Select the Host from the list.











            Ensure that you select Linux Hosts with Defenders installed.















            ![scale:30](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-64b8ff4d3d42548397b90f3886be5ae6bb6cbd79%252Fapplication-host-control-import.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=b7df76b0a6d2ac4af3cd192578646bc1&sv=3)


2. Attach the application control list to a Compliance rule.









1. Select "Defend > Compliance > Hosts > Hosts".

2. Enter a **Rule name**.

3. Select the **Scope**, which are the hosts to which this rule applies.

4. Select the Compliance action.









      1. Select **Application control** as the type of control,















         ![scale:30](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-f8d6b01fe67a367b9602ecc9a2afd4d9ab079791%252Fapplication-host-control-compliance-rule.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=bd2c9229f91339a39188adfc28b0b5e7&sv=3)

      2. Choose the new app control rule you created earlier.

      3. Select the action.











         You can choose alert or block to enforce the criteria in the application control list and generate alerts.











         Do not select **Ignore** as an option, if you want to generate alerts for compliance violations.











         Block does not block the non-compliant application from running on the host, but rather it blocks new containers for the specified application and version from being deployed on that host. So, when a rule is matched and the action is set to block, any new container will be blocked from running on that host.


3. View the scan results.









1. Select "Monitor > Compliance > Hosts".

2. Select a host to view the alerts in the host details section.


## Review host scan reports[Direct link to heading](https://docs.prismacloud.io/admin-guide/compliance/host-scanning\#review-host-scan-reports)

Prisma Cloud lets you filter the displayed hosts by searching for specific hosts or by [collection](https://docs.prismacloud.io/admin-guide/configure/collections). Collections support AWS tags. When creating new collections, specify the tags you want to use for filtering in the **Labels** field.

You can filter the displayed hosts by searching for specific hosts or by choosing a [collection](https://docs.prismacloud.io/admin-guide/configure/collections). Collections support AWS tags. When creating a new collection, add the tags you want to use for filtering to the **Labels** field.

1. Open Console, then go to **Monitor > Compliance > Hosts > Hosts**.











Select **PDF** or **CSV** to export all the compliance issues identified in the latest scans to a PDF or a CSV file respectively.

2. Click on a host in the list.











A report for the compliance issues on the host is shown.


[PreviousTrusted images](https://docs.prismacloud.io/admin-guide/compliance/trusted-images) [NextVM image scanning](https://docs.prismacloud.io/admin-guide/compliance/vm-image-scanning)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
