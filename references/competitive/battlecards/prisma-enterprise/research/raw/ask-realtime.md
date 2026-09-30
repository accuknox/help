# How quickly does Prisma Cloud Enterprise Edition alert on an audit event such as an AWS IAM user created without MFA? Is it near real-time and can it auto-remediate?

## Alert timing for an AWS IAM “user created without MFA” audit event

Prisma Cloud **creates audit event records** (audits) and you can review them in **Monitor → Events** or query them via the API: \[Audit]\(/spaces/tDEn1KUsV8KwFzyJgBk4/pages/h3P1YgtkAapYBVdxAtmY “mention”).

For the actual **alert** surfaced from policy violations, Prisma Cloud states that the **time to alert varies by alert type** and can **occasionally take a few hours**, depending on factors like **ingestion frequency** and **detection mechanism**: \[View and Respond to Prisma Cloud Alerts]\(/spaces/yqPwsbMSaogAot23rTIu/pages/213gZrbzle8M5tCesjJj “mention”).

So it’s **not guaranteed near real-time**; plan for **up to hours** in some cases.

## Auto-remediation

For **IAM Security** alerts, the docs distinguish two things:

* The **IAM module itself does not support enabling “automatic remediation.”** You must either remediate manually or use automation you configure: \[Remediate Alerts for IAM Security]\(/spaces/yqPwsbMSaogAot23rTIu/pages/lku2X6SfzCc3xB2gJ547 “mention”).
* For **AWS IAM alerts specifically**, you can set up **automatic remediation using a custom Python script** that consumes alerts via **AWS SQS**, calls the IAM remediation API, and runs the returned CLI commands: \[Remediate Alerts for IAM Security]\(/spaces/yqPwsbMSaogAot23rTIu/pages/lku2X6SfzCc3xB2gJ547 “mention”).

For **GCP IAM alerts**, automatic remediation via this approach is **not supported**.

# Suggested Follow-up Questions:

If you need more information, consider asking one of these follow-up questions by performing an HTTP GET request on the URL:

- [How real-time is alerts latency?](https://docs.prismacloud.io?ask=How%20real-time%20is%20alerts%20latency%3F)
- [Can I auto-remediate AWS IAM alerts?](https://docs.prismacloud.io?ask=Can%20I%20auto-remediate%20AWS%20IAM%20alerts%3F)
- [Where to view IAM alert timing?](https://docs.prismacloud.io?ask=Where%20to%20view%20IAM%20alert%20timing%3F)

# Sources:

- [Alerts and Notifications on Prisma Cloud](https://docs.prismacloud.io/content-collections/alerts/alert-notifications.md)
- [Alerts](https://docs.prismacloud.io/admin-guide/32/alerts/alerts.md)
- [Remediate Alerts for IAM Security](https://docs.prismacloud.io/content-collections/administration/configure-iam-security/remediate-alerts-for-iam-security.md)
- [Alerts](https://docs.prismacloud.io/admin-guide/33/alerts/alerts.md)
- [Prisma Cloud Enterprise Edition vs Compute Edition](https://docs.prismacloud.io/content-collections/runtime-security/pcee-vs-pcce.md)
- [Alerts](https://docs.prismacloud.io/admin-guide/alerts/alerts.md)
- [Prisma Cloud Enterprise Edition vs Compute Edition](https://docs.prismacloud.io/admin-guide/33/welcome/pcee-vs-pcce.md)
- [Audit](https://docs.prismacloud.io/admin-guide/32/audit/audit.md)
- [Prisma Cloud Enterprise Edition vs Compute Edition](https://docs.prismacloud.io/admin-guide/32/welcome/pcee-vs-pcce.md)
- [Audit](https://docs.prismacloud.io/admin-guide/33/audit/audit.md)
- [Audit Event Queries](https://docs.prismacloud.io/content-collections/search-and-investigate/audit-event-queries.md)
- [Alerts](https://docs.prismacloud.io/content-collections/runtime-security/alerts.md)
- [View and Respond to Prisma Cloud Alerts](https://docs.prismacloud.io/content-collections/alerts/view-respond-to-prisma-cloud-alerts.md)

