For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/runtime-defense/incident-types/port-scanning.md).

Port scans are a method for finding which ports on a network are open and listening. It is a reconnaissance technique that gives attackers a map of where they can further probe for weaknesses.

Port scanning incidents indicate that a container is attempting to make an unusual number of outbound network connections to hosts and ports to which it does not normally connect. Port scanning could be a post-compromise attempt to use the container to find other resources on the network as a precursor to lateral movement.

Prisma Cloud performs two types of checks for port scanning:

- The first type specifically identifies scans done by 'nmap.' This is triggered by a process event, which can be blocked (both alert/block).

- The second type of check is triggered by a network event, which cannot be blocked but can only generate an alert. This type of check doesn’t depend on the binary. The scan can be initiated by processes such as a Java process, which would be classified as an alert triggered by raw socket events. This means that even if port scans are done using tools other than 'nmap', they will be alerted as raw socket events. Incidents of this type will show all the target IPs and ports involved in the scan.


## Investigation[Direct link to heading](https://docs.prismacloud.io/admin-guide/runtime-defense/incident-types/port-scanning\#investigation)

The following screenshot shows a port scanning incident.

![port scanning incident](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-bac6c641d998edeae34db4b47f5b4cc165943b94%252Fport_scanning_incident.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=6d6c02bcaa27d3850a0b39bc31e082ef&sv=3)

The first step in an investigation is to determine whether the source of the outbound network activity was an otherwise-valid process that was misused or a newly introduced process. Prisma Cloud forensics are a great place to start. In Incident Explorer, click **View Live Forensics**. It shows that _bin/bash_ was launched immediately before the port scan, and that the shell was used to launch nmap. Nmap is a popular network scanning tool.

![port scanning forensics](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-8f4759afa0480f2d05babce6ab8cf12ac741e49a%252Fport_scanning_forensics.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=ea1bb053c00c401708ec381021a03629&sv=3)

The next step in the investigation is to determine how nmap was introduced and executed. Some plausible scenarios include:

- A user account was used to execute nmap via a Docker command from the host. If enabled, Prisma Cloud access logs would show which user ran the command and when it was run.

- A remote code execution vulnerability was used to run nmap remotely. If the Prisma Cloud Web Application and API Security (WAAS) was configured to protect this container’s inbound traffic, the WAAS logs may help with your investigation. Additionally, logs from the services in the container, such as Apache access logs, may shed additional light on the incident.


Once the cause has been identified, the next step in the investigation is to review the services that the actor may have discovered via port scanning and to inspect those containers to ensure that there hasn’t been additional lateral movement. Container runtime audits may show specific connection attempts.

## Mitigation[Direct link to heading](https://docs.prismacloud.io/admin-guide/runtime-defense/incident-types/port-scanning\#mitigation)

Mitigation and remediation for a port scanning incident should focus on resolving the issue that allowed execution of the responsible process.

## Blocking port scanning attempts when using tools such as nmap, hping3, and masscan[Direct link to heading](https://docs.prismacloud.io/admin-guide/runtime-defense/incident-types/port-scanning\#blocking-port-scanning-attempts-when-using-tools-such-as-nmap-hping3-and-masscan)

Prisma Cloud Runtime Policy supports detecting and blocking port scanning only for the nmap tool. The nmap tool is detected and blocked as a process, whereas other port scanning tools such as hping3 or masscan are detected as raw socket events.

The following examples help validate these scenarios.

**Example 1**

![port detection event 1](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-f06738ccbcd14289fbaae6f97491ec6ec46b7af1%252Fport-detection-event-1.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=744d4d9f65a78eff2f8de291e54374bf&sv=3)

- Message: Process /usr/bin/nmap performed suspicious raw network activity

- Event type: Network / Suspicious Network Activity

- ATT&CK technique: Network Service Scanning

- Details: Here, Prisma Cloud detects the "nmap -F -Pn 192.168.10.200" event as port scanning and blocks the event.


**Example 2**

![port detection event 2](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-ed85bcb3188a427a82b848e2573cdf6c5c9e7041%252Fport-detection-event-2.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=7c5f19e93de5bc7e455def54dbaeec04&sv=3)

- Message: /usr/bin/nmap launched and is identified as a process used for port scanning

- Event type: Processes / Port Scan Process

- ATT&CK technique: Network Service Scanning

- Details: The message "/usr/bin/nmap launched and is identified as a process used for port scanning" helps Prisma Cloud to block the event.


**Example 3**

![port detection event 3](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-4e571fbf53bd45aa40188b55d57cd03b39c5481f%252Fport-detection-event-3.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=7ff2fe7cb120aee848d58515dea225c8&sv=3)

- Message: Process /usr/sbin/hping3 performed suspicious raw network activity

- Event type: Network / Suspicious Network Activity

- ATT&CK technique: Network Service Scanning

- Details: Prisma Cloud detects "hping3 -8 1-1023 192.168.10.200" as a raw network activity, but it does not block it. Prisma Cloud generates a raw socket event.


**Example 4**

![port detection event 4](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-1471d43b49035e8f2ecfd7048c29912e4ae10781%252Fport-detection-event-4.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=35f0fb6859c8865ddad4ca10e256bd25&sv=3)

- Message: Process /usr/bin/masscan performed suspicious raw network activity

- Event type: Network / Suspicious Network Activity

- ATT&CK technique: Man-in-the-Middle

- Details: Prisma Cloud detects "masscan 192.168.100.201 -p 1-1023" as a raw network activity, but it does not block it.


**Workaround**: You can block the events generated by port scanning tools such as Hping3 and Masscan by using the "Explicitly Denied Processes" option under the Runtime Rule. You can also add processes such as "/usr/bin/masscan" or "/usr/sbin/hping3" for block action.

[PreviousMalware](https://docs.prismacloud.io/admin-guide/runtime-defense/incident-types/malware) [NextReverse shell](https://docs.prismacloud.io/admin-guide/runtime-defense/incident-types/reverse-shell)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
