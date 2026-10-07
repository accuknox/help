For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/runtime-defense/event-aggregation-categorization-table.md).

This table categorizes various events, their corresponding APIs, and how Defender aggregates the events within Prisma Cloud.

Module

API

Defender Aggregation by

container-events

audits/runtime/container

None

security-events

cloud-security-agent/alerts/container

None

CNNS for containers

audits/firewall/network/container

NetworkFirewallAttackType

WAAS for containers

audits/firewall/app/container

None

Trust audits

audits/trust

Image repo tag

Kubernetes audits

audits/kubernetes

None

Admission audits

audits/admission

None

Docker audits

audits/access

None

App-Embedded audits

audits/runtime/app-embedded

RuntimeAttackType

WAAS audits for App-Embedded

audits/firewall/app/app-embedded

Different mechanism

Host audits

audits/runtime/host

RuntimeAttackType

Security events

cloud-security-agent/alerts/host

None

CNNS for hosts

audits/firewall/network/host

NetworkFirewallAttackType

WAAS for hosts

audits/firewall/app/host

None

Host log inspection audits

audits/runtime/log-inspection

None

Host file integrity

audits/runtime/file-integrity

FileIntegrityEventType

Host activities

forensic/activities

ActivityType

Serverless audits

audits/runtime/serverless

C code

WAAS audits for serverless

audits/firewall/app/serverless

C code

WAAS audits for agentless

audits/firewall/app/agentless

None

[PreviousEvent Aggregation](https://docs.prismacloud.io/admin-guide/runtime-defense/runtime-defense-aggregation) [NextDetailed Aggregation Event Types](https://docs.prismacloud.io/admin-guide/runtime-defense/event-aggregation-event-types-table)

Last updated 3 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
