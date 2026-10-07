For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/deployment-patterns/caps.md).

Prisma Cloud restricts the size of some data collections to prevent misconfigured or noisy systems from consuming all available disk space and compromising the availability of the Console service.

## Registry Scanning[Direct link to heading](https://docs.prismacloud.io/admin-guide/deployment-patterns/caps\#registry-scanning)

Prisma Cloud scans a maximum of 1,000,000 registry images, ordered by most recently published. Publish date is the time an image is pushed to the registry.

## Data Collections Limits[Direct link to heading](https://docs.prismacloud.io/admin-guide/deployment-patterns/caps\#data-collections-limits)

The following limits are currently enforced in Console’s database.

For audits: if you must retain all audits, consider configuring Console to send audits to syslog, and then forward the audits to a log management system for long term storage.

Collection

Cap

Registry specifications

19,999 entries

[Jenkins plugin and twistcli scan reports](https://docs.prismacloud.io/admin-guide/vulnerability-management/scan-reports)

5000 scan reports or 500 MB (whichever limit is reached first)

[Container runtime audits](https://docs.prismacloud.io/admin-guide/audit/event-viewer)

25K audits or 50 MB (whichever limit is reached first)

[Container network firewall audits](https://docs.prismacloud.io/admin-guide/audit/event-viewer)

25K audits or 50 MB (whichever limit is reached first)

[Image sandbox analysis reports](https://docs.prismacloud.io/admin-guide/runtime-defense/image-analysis-sandbox)

5000 scan reports or 500 MB (whichever limit is reached first)

[Kubernetes audits](https://docs.prismacloud.io/admin-guide/audit/kubernetes-auditing)

100K audits or 50 MB (whichever limit is reached first)

[Admission audits](https://docs.prismacloud.io/admin-guide/access-control/open-policy-agent)

100K audits or 50 MB (whichever limit is reached first)

[Log inspection events](https://docs.prismacloud.io/admin-guide/runtime-defense/runtime-defense-hosts)

100K audits or 50 MB (whichever limit is reached first)

[File integrity events](https://docs.prismacloud.io/admin-guide/runtime-defense/runtime-defense-hosts)

100K audits or 50 MB (whichever limit is reached first)

[Host activities](https://docs.prismacloud.io/admin-guide/audit/host-activity)

100K audits or 50 MB (whichever limit is hit first)

[Host history](https://docs.prismacloud.io/admin-guide/audit/audit-admin-activity)

100K audits or 50 MB (whichever limit is reached first)

[Host runtime audits](https://docs.prismacloud.io/admin-guide/audit/event-viewer)

25K audits or 50 MB (whichever limit is reached first)

[Host network firewall audits](https://docs.prismacloud.io/admin-guide/audit/event-viewer)

25K audits or 50 MB (whichever limit is reached first)

[Serverless runtime audits](https://docs.prismacloud.io/admin-guide/audit/event-viewer)

25K audits or 50 MB (whichever limit is reached first)

[App-Embedded runtime audits](https://docs.prismacloud.io/admin-guide/audit/event-viewer)

25K audits or 50 MB (whichever limit is reached first)

[Trust audits](https://docs.prismacloud.io/admin-guide/audit/event-viewer)

25K audits or 50 MB (whichever limit is reached first)

[WAAS for containers events](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-analytics)

200K audits or 200 MB (whichever limit is reached first)

[WAAS for hosts events](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-analytics)

200K audits or 200 MB (whichever limit is reached first)

[WAAS for serverless events](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-analytics)

200K audits or 200 MB (whichever limit is reached first)

[WAAS for app-embedded events](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-analytics)

200K audits or 200 MB (whichever limit is reached first)

[Incidents](https://docs.prismacloud.io/admin-guide/runtime-defense/incident-explorer)

25K incidents or 50 MB (which limit is reached first)

[Registry specifications](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/compute-edition/34/admin-guide/vulnerability-management/registry-scanning/registry-scanning.md)

19,999 entries

[PreviousDNS and certificate management](https://docs.prismacloud.io/admin-guide/deployment-patterns/best-practices-dns-cert-mgmt) [NextMigrate to SaaS Console](https://docs.prismacloud.io/admin-guide/deployment-patterns/migrate-to-saas)

Last updated 3 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
