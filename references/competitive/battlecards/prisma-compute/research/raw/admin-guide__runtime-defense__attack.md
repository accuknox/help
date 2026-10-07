For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/runtime-defense/attack.md).

Prisma Cloud’s monitoring section includes an Att&CK Explorer dashboard providing a framework that helps you to contextualize runtime audits, manage them, and generate risk reports.

ATT&CK Explorer is a knowledge base of tactics and techniques that adversaries use to attack applications and infrastructure. It’s a useful framework for threat-informed defense, where a deep understanding of adversary tradecraft can help protect against attacks.

The ATT&CK framework has two key concepts:

- **Tactics** \- An adversary’s technical goals.

- **Techniques** \- How those goals are achieved or What they acheive


The relationship between tactics and techniques is presented as a matrix. One tactic in the matrix is called _Persistence_. After establishing a foothold in your environment, adversaries want to reliably return to it. Adversaries use a number of techniques to achieve persistence, such as _Account Manipulation_ and _Event Triggered Execution_.

## Cloud Native threat matrix[Direct link to heading](https://docs.prismacloud.io/admin-guide/runtime-defense/attack\#cloud-native-threat-matrix)

Prisma Cloud protects cloud native applications running in Kubernetes clusters, serverless functions, Containers-as-a-Service offerings, and virtual machines. The Cloud Native threat matrix covers the different techniques that impact cloud native applications across all these environments. It’s composed from ATT&CK for Linux, recent community efforts around ATT&CK for Containers and Kubernetes, and a few techniques from Prisma Labs. The Cloud Native threat matrix is the foundation for the ATT&CK dashboard.

## ATT&CK dashboard[Direct link to heading](https://docs.prismacloud.io/admin-guide/runtime-defense/attack\#att-and-ck-dashboard)

The ATT&CK dashboard serves as a portal to the raw events in the **Monitor > Events** view. All Prisma Cloud audits are mapped to the tactics and techniques in the ATT&CK framework. For example, when Defender detects a crypto miner in your environment, we map the audit to the _Resource Hijacking_ technique under the _Impact_ tactic.

The ATT&CK dashboard collates audits, maps them to the tactics and techniques, and presents the data visually in the ATT&CK matrix. Each card in the matrix shows a count of events. Higher counts represent a higher severity issues. Filters let you slice and dice the data to inspect specific segments of your environment. The dashboard:

- Presents a real-time view of tactics and techniques being employed by adversaries.

- Identifies weaknesses in your defenses. Use the counts to prioritize work to fortify defenses for the techniques favored by adversaries.

- Provides raw data for risk reports for management.


Audits from the following subsystems flow into the ATT&CK dashboard:

- Container runtime audits.

- Host runtime audits.

- Serverless runtime audits.

- App-Embedded runtime audits.

- WAAS audits.

- Kubernetes audits.

- Admission (OPA) audits.

- Custom runtime rule audits for builtin system checks only. Currently, you cannot specify tactic and technique for user-defined custom runtime rules.


To see the ATT&CK dashboard, open Console, and go to **Monitor > ATT&CK**. The following screenshot highlights the main components in the dashboard:

![attack dashboard](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-6e771eded350d5d6375cb0f27d27c77666f79111%252Fattack_dashboard.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=3d3304538fce24333bc17524f4f0ad91&sv=3)

**1\. Filter** \- Filter data in the dashboard by:

- **Impacted technique**.

- **Date**: View events that occurred in the past 24 hours, 7 days, 30 days, or 3 months.

- **Collection**: View data for just some segment of your environment (e.g., a production cluster).


**2\. Tactics** \- Tactics are listed across the top row of the matrix. A count shows the sum of all events for all corresponding techniques in the category. Each column lists the techniques that can be used to achieve the tactic.

**3\. Techniques** \- Lists of techniques that can be used to achieve a tactic. The color of the card is based on the event count for a technique. If there is one or more events for a technique, the card is colored red. Otherwise, if there are no events, the card is gray. All techniques are fully described [here](https://cdn.twistlock.com/docs/attachments/full_attack_explorer_matrix.pdf).

Clicking on an impacted technique card opens a dialog that shows all relevant audits for the technique.

The following screenshot shows the dialog for the _Privileged Container_ card. The dialogs are organized as follows:

- Description.

- Audit source filter (pick from the drop-down list).

- Table of relevant audits.


![attack explore card](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-2db3b01e6ffaf74747a9189f920875c2a6bd67d1%252Fattack_explore_card.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=09dfb37bfe3f37c8e2bf296e0f31ad61&sv=3)

Syslog messages contain tactic and technique information for all relevant audits.

## Investigating incidents[Direct link to heading](https://docs.prismacloud.io/admin-guide/runtime-defense/attack\#investigating-incidents)

As you monitor your environment, you’ll see tactics and techniques are applied consistently across views. Tactics and techniques are shown in **Monitor > ATT&CK**, **Monitor > Events**, and **Monitor > Runtime > Incident explorer**.

![attack tactics techniques](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-ffb7b578142e4389df383999112a098e9ffb4680%252Fattack_tactics_techniques.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=546ccfbd48fae5b8443f933ed4b037db&sv=3)

## Surfacing impacted techniques[Direct link to heading](https://docs.prismacloud.io/admin-guide/runtime-defense/attack\#surfacing-impacted-techniques)

When investigating an incident, you’ll want to focus on the segment of your environment that has been impacted. Use the filter box to focus your view of the data.

One important filter is **Impacted techniques**. Without the filter, all technique cards are displayed.

![attack unfiltered dashboard](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-9731b465446655112edca671d75d4b107477dcfb%252Fattack_unfiltered_dashboard.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=21eac9d08d904365d09eab53d51e7f32&sv=3)

With the filter, only techniques that have been detected are displayed. In the following screenshot, we’ve narrowed the data to:

- Audits within the past seven days.

- Containers in the frontend collection, which are exposed to the Internet, and likely where the attack started.

- Attack techniques used by the adversary.


![attack filtered dashboard](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-e4bd151dc757a32cebcdf8a47660f94aa971e73c%252Fattack_filtered_dashboard.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=2ef31aa960a23743d95b98395b140ad0&sv=3)

## Mapping audits to techniques[Direct link to heading](https://docs.prismacloud.io/admin-guide/runtime-defense/attack\#mapping-audits-to-techniques)

Every audit (for example, runtime, admission, and so on) maps to one or more techniques. The following table shows the mappings.

The **Techniques** column shows the technique to which an audit is always mapped.

The **Possible Additional Techniques** column shows the techniques that to which an audit can be optionally mapped, depending on changing information from the audit. For example, for some audits, on new files being created, we will check if the process that created the files is a compiler. If so, we also map the audit to the **Compile After Delivery** technique.

Category

Audit Type

Techniques (techniques that the audit is always mapped to)

Possible Additional Techniques (techniques that the audit can optionally be mapped to, depending on changing information from the audit)

Cloud

cloudMetadataProbing

Cloud Instance Metadata API

-

Kubernetes

kubeletAPIAccess

Access Kubelet Main API

-

Kubernetes

kubeletReadonlyAccess

Query Kubelet Readonly API

-

Kubernetes

kubectlSpawned

Access the Kubernetes API Server
Software Deployment Tools

Lateral Tool Transfer
Exec Into Container
Create Container
Kubernetes Secrets

Kubernetes

kubectlDownloaded

Ingress Tool Transfer
Software Deployment Tools,

-

Network

horizontalPortScanning

Network Service Scanning

-

Network

verticalPortScanning

Network Service Scanning

-

Network

explicitlyDeniedIP

-

-

Network

customFeedIP

-

-

Network

feedIP

Command and Control / General
Resource Hijacking

-

Network

unexpectedOutboundPort

Exfiltration
Command and Control / General

-

Network

suspiciousNetworkActivity

-

Man In The Middle
Network Service Scanning

Network

unexpectedListeningPort

-

-

Network

explicitlyDeniedListeningPort

-

-

Network

explicitlyDeniedOutboundPort

-

-

Network

listeningPortModifiedProcess

Command and Control / General

-

Network

outboundPortModifiedProcess

Exfiltration
Command and Control / General

-

DNS

feedDNS

Command and Control / General
Resource Hijacking

DNS

explicitlyDeniedDNS

-

-

DNS

dnsQuery

-

-

Processes

unexpectedProcess

Native Binary Execution

Processes

portScanProcess

Network Service Scanning

Processes

explicitlyDeniedProcess

Native Binary Execution

Processes

modifiedProcess

Foreign Binary Execution

Processes

cryptoMinerProcess

Resource Hijacking

Processes

lateralMovementProcess

-

-

Processes

tmpfsProcess

-

-

Processes

policyHijacked

Impair Defences

-

Processes

reverseShell

Native Binary Execution

-

Processes

SuidBinaries

Abuse Elevation Control Mechanisms

-

Processes

ProcUnknownOriginBinary

Foreign Binary Execution

-

Filesystem

administrativeAccount

-

Account Manipulation
Create Account
Abuse Elevation Control Mechanisms

Filesystem

sshAccess

-

Account Manipulation

Filesystem

explicitlyDeniedFile

-

-

Filesystem

malwareFileCustom

-

-

Filesystem

malwareFileFeed

-

-

Filesystem

execFileAccess

-

Masquerading
IngressToolTransfer
Compile After Delivery

Filesystem

elfFileAccess

-

IngressToolTransfer
Compile After Delivery

Filesystem

secretFileAccess

-

-

Filesystem

regFileAccess

-

-

Filesystem

fileIntegrity

-

-

Filesystem

alteredBinary

Supply Chain Compromise

-

Filesystem

malwareDownloaded

Ingress Tool Transfer

Filesystem

suspiciousELFHeader

Obfuscated Files

Filesystem

executionFlowHijackAttempt

Hijack Execution Flow

Filesystem

RuntimeAttackTypeFSEncryptedBinary

Obfuscated Files

Filesystem

WildFireMalware

-

Masquerading
IngressToolTransfer
Compile After Delivery

Filesystem

webShell

Web Shell
Ingress Tool Transfer

-

Filesystem

FSUnknownOriginBinary

-

Masquerading
IngressToolTransfer
Compile After Delivery

Processes

Running privileged process within container

Software Deployment Tools

-

Processes

Running cron app

Scheduled Task / Job

-

Processes

Database app spawned process

Application Exploit (RCE)
Exploitation Of Remote Services

-

Processes

Suspicious networking tool

-

-

Processes

Suspicious networking scaning tool

Network Service Scanning

-

Processes

User creation (Container)

Create Account

-

Processes

User deletion (Container)

Account Access Removal

-

Processes

User modification (Container)

Account Manipulation

-

filesystem

Bash shell tampering

Event Triggered Execution

-

filesystem

Linux user management files

CreateAccount
Account Manipulation

-

filesystem

Configuration file changes (Host)

-

-

filesystem

Configuration file changes (Container)

-

-

network-outgoing

Common data exfiltration ports

Exfilitration

-

network-outgoing

Common crypto mining pool ports

Resource Hijacking

-

network-outgoing

Cloud platform metadata API access (Container)

Cloud Instance Metadata API

-

-

xss

ExploitationForPrivilegeEscalation

-

sqli

Exploit Public-Facing Application
Application Exploit (RCE)

-

cmdi

Exploit Public-Facing Application
Application Exploit (RCE)

-

lfi

Exploit Public-Facing Application
Application Exploit (RCE)

-

codeInjection

Exploit Public-Facing Application
Application Exploit (RCE)

-

deniedIP

-

-

-

deniedCountry

-

-

-

header

-

-

-

-

attackTools

NetworkServiceScanning

-

-

shellshock

Exploit Public-Facing Application
Application Exploit (RCE)

-

disallowedFile

-

-

-

malformedRequest

-

-

-

informationLeak

Exfilitration

System Credential Dumping
System Account Discovery
File And Directory Discovery
System Unsecured Credentials
Network Configuration Discovery
Software Discovery

-

unexpectedAPI

-

-

-

dos

Endpoint Denial-of-Service

-

-

searchEngineCrawler

-

-

-

businessAnalyticsBot

-

-

-

educationalBot

-

-

-

newsBot

-

-

-

financialBot

-

-

-

contentFeedClient

-

-

-

archivingBot

-

-

-

careerSearchBot

-

-

-

mediaSearchBot

-

-

-

genericBot

-

-

-

webAutomationTool

-

-

-

webScraper

-

-

-

apiLibrary

-

-

-

httpLibrary

-

-

-

sessionValidation

-

-

-

javascriptTimeout

-

-

-

missingCookie

-

-

-

browserImpersonation

-

-

-

requestAnomalies

-

-

-

userDefinedBot

-

-

-

GKE - pod created in host process namespace

Privileged Container

-

GKE - pod created with host file system mount

-

-

-

GKE - pod created without security context

-

-

-

GKE - pod created on host network

Privileged Container

-

-

GKE - privileged pod creation

Privileged Container

-

-

GKE - Forbidden request

-

-

-

GKE - exec or attach to a pod

Exec Into Container

-

-

Twistlock Labs - GKE - Tampering with Twistlock configuration

Impair Defences

-

-

Pod created in host process namespace

Privileged Container

-

-

Pod created with host file system mount

-

-

-

Pod created without security context

-

-

-

Pod created on host network

Privileged Container

-

-

Privileged pod creation

Privileged Container

-

-

Forbidden request

-

-

-

Exec or attach to a pod

Exec Into Container

-

-

Twistlock Labs - Tampering with Twistlock configuration

Impair Defences

-

-

CIS - Privileged pod created

Privileged Container

-

-

CIS - Pod created in host process ID namespace

Privileged Container

-

-

CIS - Pod created on host IPC namespace

Privileged Container

-

-

CIS - Pod created on host network

Privileged Container

-

-

CIS - Privilege escalation pod created

Privileged Container

-

-

Pod created with sensitive host file system mount

Writable Volumes

-

-

Exec or attach to a pod

Exec Into Container

-

[PreviousImport and export individual rules](https://docs.prismacloud.io/admin-guide/runtime-defense/import-export-individual-rules) [NextRuntime audits](https://docs.prismacloud.io/admin-guide/runtime-defense/runtime-audits)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
