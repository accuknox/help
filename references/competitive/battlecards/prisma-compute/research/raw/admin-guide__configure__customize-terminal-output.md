For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/configure/customize-terminal-output.md).

Prisma Cloud lets you create rules that block access to resources or block the deployment of non-compliant containers.

For example, you might create a rule that blocks the deployment of any image that has critical severity vulnerabilities. By default, when you try to run non-compliant image, Prisma Cloud returns a terse response:

AskCopy

```
# docker -H :9998 --tls run -ti morello/docker-whale
docker: Error response from daemon: [Prisma Cloud] operation blocked by policy: (test-compliance), host has 19 compliance issues.
```

To help the operator better understand how to handle a blocked action, you can enhance Prisma Cloud’s default response by

- Appending a custom message to the default message. For example, you could tell operators where to go to open a ticket.

- Configuring Prisma Cloud to return an itemized list of compliance issues rather than just a summary. This way, the operator does not need to contact the security team to determine which issues are preventing deployment. They are explicitly listed in the response.


Enhanced terminal output is available for rules created under:

- **Defend > Vulnerabilities > Policy**

- **Defend > Compliance > Policy**

- **Defend > Access** (Kubernetes access control rules)


## Specify a Custom Message[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/customize-terminal-output\#specify-a-custom-message)

You can create custom rules to audit your Kubernetes cluster and alert when a rule is violated. Refer to the [Kubernetes auditing](https://docs.prismacloud.io/admin-guide/audit/kubernetes-auditing) documentation.

## Output itemized list of compliance issues[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/customize-terminal-output\#output-itemized-list-of-compliance-issues)

You can configure vulnerability and compliance rules to return a detailed list of issues when Prisma Cloud blocks a deployment.

In this procedure, you create a vulnerability rule that prevents the deployment of any image that contains any type of vulnerable package.

Although this procedure is specific to vulnerability rules, the process for compliance rules is the same.

1. Open Console.

2. Create a new vulnerability rule ( **Defend > Vulnerabilities > Policy**) or compliance rule ( **Defend > Compliance > Policy**).

3. In the new rule dialog, enter the following information:









1. Enter a rule name.

2. Specify conditions that trigger a block action.











      For example, for the **Image contains vulnerable OS packages** condition in a vulnerability rule, set the **Action** to **Block** and set the **Severity** threshold to **Low**.

3. Set **Terminal output verbosity for blocked requests** to **Detailed**.

4. Click **Save**.


4. Test your setup by deploying an image with vulnerabilities.











On a host protected by Prisma Cloud, run an image with vulnerabilities.

















AskCopy



```
$ docker run --rm -it ubuntu:14.04 sh
docker: Error response from daemon: [Prisma Cloud] Image operation blocked by policy: (sdf), has 44 vulnerabilities, [low:25 medium:19].
Image          ID       CVE             Package   Version             Severity   Status
=====          ==       ===             =======   =======             ========   ======
ubuntu:14.04   4333f1   CVE-2017-2518   sqlite3   3.8.2-1ubuntu2.1    medium     deferred
ubuntu:14.04   4333f1   CVE-2017-6512   perl      5.18.2-2ubuntu1.1   medium     needed
     .
     .
     .
```


[PreviousConfigure custom certs from a predefined directory](https://docs.prismacloud.io/admin-guide/configure/custom-certs-predefined-dir) [NextCollections](https://docs.prismacloud.io/admin-guide/configure/collections)

Last updated 3 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
