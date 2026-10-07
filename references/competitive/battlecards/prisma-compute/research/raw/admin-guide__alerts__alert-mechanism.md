For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/alerts/alert-mechanism.md).

Prisma Cloud generates alerts to help you focus on the significant events that need your attention. Because alerts surface policy violations, you need to put them in front of the right audience and on time.

To meet this need, you can create alert profiles that send events/notifications to the alert notification providers your internal teams use to triage and address these violations.

Alert profiles are built on the following constructs:

Alert provider
Specifies the notification provider or channel to which you want to send alerts. Prisma Cloud supports multiple options such as email, JIRA, Cortex, and PagerDuty.

You can create any number of alert profiles, where each profile gives you granular control over who should receive the notifications and for what types of alerts.

Alert settings
Specifies the configuration settings required to send the alert to the alert provider or messaging medium.

Alert triggers
Specifies what alerts you want to send to the provider included in the profile. Alerts are generated when the rules included in your policy are violated, and you can choose whether you want to send a notification for the detected issues. For example, on runtime violations, compliance violations, cloud discovery, or WAAS.

Not all triggers are available for all alert providers.

## Frequency[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/alert-mechanism\#frequency)

### Vulnerability Alerts[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/alert-mechanism\#vulnerability-alerts)

Image vulnerabilities are checked for images in the registry and deployed images. The number of known vulnerabilities in a resource is not static over time.

As the Prisma Cloud Intelligence Stream is updated with new data, new vulnerabilities might be uncovered in resources that were previously considered clean. The first time a resource (image, container, host, etc.) enters the environment, Prisma Cloud assesses it for vulnerabilities. Thereafter, every resource is periodically rescanned.

Daily vulnerability alerts report is sent once in 24 hours and uses alerts of similar asset types (such as code repos, registries, images, hosts, and functions) that can be sent to a single profile in batches of 50. The limit is designed to optimize Console resource consumption in large environments.

- **Immediate alerts** — You can configure sending alerts immediately when the number of vulnerabilities for the resource increases, which can happen in one of the following scenarios:









  - Deploy a new image/host with vulnerabilities.

  - Detect new vulnerabilities when re-scanning existing image/host/registry images, in that case, an immediate alert is dispatched again for this resource with all its vulnerabilities.











    Immediate alerts are not supported for registry scan vulnerabilities.















    ![alert trigger profile](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-377cf93c03ff8b65234396dd27a7e1e7779f0388%252Falert-trigger-profile.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=69b299ff6b5805f8dc3601d8508a3561&sv=3)











    The ability to send immediate vulnerability alerts is configurable for each alert profile and is disabled by default.











    Immediate alerts do not affect the vulnerabilities report that is generated every 24 hours. The report will include all vulnerabilities that were detected in the last 24 hours, including those sent as an immediate alert.


### Compliance Alerts[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/alert-mechanism\#compliance-alerts)

Compliance alerts are sent in one of two ways. Each alert channel that has compliance alert triggers ("Container and image compliance", "Host compliance"), only uses one of these ways.

#### Compliance Reports[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/alert-mechanism\#compliance-reports)

This form of compliance alert works under the idea that resources in your system can only be in one of two states: compliant or non-compliant. When your system is non-compliant, Prisma Cloud sends an alert only when the number of compliance issues in the current scan is larger than the number of issues in the previous scan. The default scan interval is 24 hours.

Compliance reports list each failed check, and the number of resources that failed the check in the latest scan and the previous scan. For detailed information about exactly which resources are non-compliant, use [Compliance Explorer](https://docs.prismacloud.io/admin-guide/compliance/compliance-explorer).

For example:

- Scan period 1: You have a non-compliant container named _crusty\_pigeon_.


You’ll be alerted about the container compliance issues.

- Scan period 2: Container _crusty\_pigeon_ is still running. It’s still non-compliant. You’ll be alerted about the same container compliance issues.


The following screenshot shows an example compliance email alert:

![alerts compliance email](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-9795c9980b22b9a0e62ceebb2af17770fb37ba34%252Falerts_compliance_email.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=8bd0216e47c1301f18b416b83afbc3bd&sv=3)

This method applies to the following alert channels: email and Cortex XSOAR.

#### Compliance Scans[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/alert-mechanism\#compliance-scans)

This form of compliance alert is emitted whenever there is an increment in the number of compliance issues detected on a resource.

The first time a resource (image, container, host, etc) enters the environment, Prisma Cloud assesses it for compliance issues. If a compliance issue violates a rule in the policy, and the rule has been configured to trigger an alert, an alert is dispatched. Thereafter, every time a resource is rescanned (periodically or manually), and there is an increase in the resource’s compliance issues, an alert is dispatched again for this resource with all its compliance issues.

This method applies to the following alert channels: Webhook, Splunk, and ServiceNow.

### Cloud Discovery Alerts[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/alert-mechanism\#cloud-discovery-alerts)

Cloud discovery alerts warn you when new cloud-native resources are discovered in your environment so that you can inspect and secure them with Prisma Cloud. Cloud discovery alerts are available on the email and XSOAR channels only.

For each new resource discovered in a scan, Prisma Cloud lists the cloud provider, region, project, service type (for example, AWS Lambda and Azure AKS), and resource name (such as `my-aks-cluster`).

### WAAS Alerts[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/alert-mechanism\#waas-alerts)

WAAS alerts are generated for the following—WAAS Firewall (App-Embedded Defender), WAAS Firewall (container), WAAS Firewall (host), WAAS Firewall (serverless), WAAS Firewall (Out-of-band), and WAAS health.

### Management[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/alert-mechanism\#management)

When you set up alerts for Defender health events. These events tell you when Defender unexpectedly disconnects from Console. Alerts are sent when a Defender has been disconnected for more than 6 hours.

### Runtime[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/alert-mechanism\#runtime)

Runtime alerts are generated for the following categories: Container runtime, App-Embedded Defender runtime, Host runtime, Serverless runtime, and Incidents.

For runtime audits, there’s a limit of 50 runtime audits per aggregation period (seconds, minutes, hours, days) for all alert providers.

### Access[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/alert-mechanism\#access)

Access alerts are for the audits of users who accessed the management console (Admission audits) and Kubernetes audits.

### Code Repository[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/alert-mechanism\#code-repository)

Code repository vulnerabilities

[PreviousAlerts](https://docs.prismacloud.io/admin-guide/alerts/alerts) [NextAWS Security Hub](https://docs.prismacloud.io/admin-guide/alerts/aws-security-hub)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
