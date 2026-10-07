For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/runtime-defense/runtime-defense-hosts.md).

Without secure hosts, you cannot have secure containers. Host machines are a critical component in the container environment, and the hosts must also be secured like containers. Prisma Cloud defender collects data about your hosts for monitoring and analysis.

Runtime host protection is designed to continuously report an up-to-date context for your hosts. You can set detection for malware, network, log inspection, file integrity, activities, and custom events. Some detected events can only be alerted on, while others can be prevented.

## Host runtime policy[Direct link to heading](https://docs.prismacloud.io/admin-guide/runtime-defense/runtime-defense-hosts\#host-runtime-policy)

By default, Prisma Cloud ships with an empty host runtime policy. An empty policy disables runtime defense entirely.

To enable runtime defense, create a new rule.

**Prerequisites:** Install a [host defender](https://docs.prismacloud.io/admin-guide/install/deploy-defender/defender-types).

1. Go to **Defend > Runtime > Host Policy** and select **Add rule**.















![host runtime rule](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-b8ee4831b6ad08ec59ae5839aa24b25f27e88847%252Fhost_runtime_rule.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=cbd6999d2b5b88e7a28a6adf388731b6&sv=3)

2. Enter a **Rule name** to indicate the target of each rule.

3. The **Scope** of each rule is determined by the [collection](https://docs.prismacloud.io/admin-guide/configure/collections) assigned to that rule.











Prisma Cloud uses [rule order and pattern matching](https://docs.prismacloud.io/admin-guide/configure/rule-ordering-pattern-matching) to determine which rule to apply for each workload.











The **Prevent** action for detection of file system events requires a Linux kernel version 4.20 or later.


### Anti-malware[Direct link to heading](https://docs.prismacloud.io/admin-guide/runtime-defense/runtime-defense-hosts\#anti-malware)

Anti-malware provides a set of capabilities that let you alert or prevent malware activity and exploit attempts.

#### Global settings[Direct link to heading](https://docs.prismacloud.io/admin-guide/runtime-defense/runtime-defense-hosts\#global-settings)

- **Alert/prevent processes by path** — Provides the ability to alert on or prevent execution of specific processes based on the processes name or the full path of binary from which the process is executed. Some of the common tools are available for easy addition by selecting their category.

- **Allow processes by path** — Provides the ability to mark processes as safe to use based on the process name or full path. Processes added to this list will not be alerted on or prevented by any of the Malware runtime capabilities.











If a process is included in both the allow list and in the deny list, the process will still be allowed by the host runtime policy.


#### Anti-malware and exploit prevention settings[Direct link to heading](https://docs.prismacloud.io/admin-guide/runtime-defense/runtime-defense-hosts\#anti-malware-and-exploit-prevention-settings)

- **Crypto miners** — Apply specific techniques for detection of crypto miners, alert on file creation, and alert or prevent their execution.

- **Non-packaged binaries created or run by service** — Detect binaries created by a service without a package manager. Alert on file creation, and alert or prevent their execution.











You need a running Defender, to detect the source when there is a `write` operation on a file.











To detect binaries that have been deployed without a package manager, Prisma Cloud depends on the package manager on the host. Currently, the `apt`, `yum`, and `dnf` package managers are supported.

- **Non-packaged binaries created or run by user** — Detect binaries created by a user without a package manager. Alert on file creation, and alert or prevent their execution.

- **Processes running from temporary storage** — Detect processes running from temporary storage (unexpected behavior for legitimate processes). Alert/prevent on file creation or execution.

- **Webshell attacks** — Detect abuse of web servers vulnerabilities to create a webshell. Alert on webshell creation and alert or prevent execution of linux command line tools from web servers.

- **Reverse shell attacks** — Detect usage of [reverse shell](https://docs.prismacloud.io/admin-guide/runtime-defense/incident-types/reverse-shell) and generate an alert.

- **Execution flow hijack** — Detect [execution flow hijack attempt](https://docs.prismacloud.io/admin-guide/runtime-defense/incident-types/execution-flow-hijack-attempt) and generate an alert.

- **Encrypted/packed binaries** — Detect usage of encrypted/packed binaries and generate an alert. Such files are alerted on as encrypted and packed binaries may be used as a method to deploy malware undetected.

- **Binaries with suspicious ELF headers** — Detect suspicious binaries for ELF headers and generate an alert.

- **Malware based on custom feeds** — Generate alerts for files classified as malware by their MD5.

- **Malware based on Prisma Cloud Advanced Threat Protection** — Generate alerts for files classified as malware by Prisma Cloud advanced intelligence feed.


-

On operating systems where the defender supports identifying files of unknown origin (a file that wasn’t installed by a known OS package manager) and an intercepted filesystem operation was performed on a file of a known origin, the following host runtime protection rules are skipped:

- Writes of a crypto miner binary to disk

- Webshell attacks

- Execution flow hijacking

- Encrypted/packed binaries

- Binaries with suspicious ELF headers

- WildFire malware analysis


#### Advanced malware analysis[Direct link to heading](https://docs.prismacloud.io/admin-guide/runtime-defense/runtime-defense-hosts\#advanced-malware-analysis)

- **Malware based on WildFire analysis** — Use WildFire, the malware analysis engine of Palo Alto Networks, to detect malware and generate alerts. Currently Wildfire analysis is provided without additional costs, but this may change in future releases. To use Wildfire, enable it under [Wildfire settings](https://docs.prismacloud.io/admin-guide/configure/wildfire).


#### Host observations[Direct link to heading](https://docs.prismacloud.io/admin-guide/runtime-defense/runtime-defense-hosts\#host-observations)

- **Track SSH events** — As part of the host observation capability, you can completely track all the SSH activities on the host. This feature is enabled by default in new rules and you can choose to disable this feature under host observations.


### Networking[Direct link to heading](https://docs.prismacloud.io/admin-guide/runtime-defense/runtime-defense-hosts\#networking)

Networking provides a high level of granularity in controlling network traffic based on IP, port, and DNS. You can use your custom rules or use Prisma Cloud Advanced Threat Protection to alert on or prevent access to malicious sites.

#### IP connectivity[Direct link to heading](https://docs.prismacloud.io/admin-guide/runtime-defense/runtime-defense-hosts\#ip-connectivity)

- **Allowed IPs**: — create an approved list of IPs which when accessed, will not generate an alert.

- **Denied IPs and ports** — Create a list of listening ports, outbound internet ports, and outbound IPs which when accessed will generate an alert.

- **Suspicious IPs based on custom feed** — Generate alerts based on entries added to the list of suspicious or high-risk IP endpoints under **Manage > System > Custom feeds > IP reputation lists**

- **Suspicious IPs based on Prisma Cloud advanced threat protection** — Generate alerts based on the Prisma Cloud advanced threat protection intelligence stream.


#### DNS[Direct link to heading](https://docs.prismacloud.io/admin-guide/runtime-defense/runtime-defense-hosts\#dns)

When DNS monitoring is enabled, Prisma Cloud filters DNS lookups. By default, DNS monitoring is disabled in new rules.

- **Allowed domains** — Create an approved list of domains which when accessed will not generate an alert or be prevented.

- **Denied domains** — Create a list of denied domains which when accessed will be alerted or prevented.

- **Suspicious domains based on Prisma Cloud Advanced Threat Protection** — Generate alerts or prevent access to domains based on Prisma Cloud Advanced Threat Protection Intelligence Stream.


### Log inspection[Direct link to heading](https://docs.prismacloud.io/admin-guide/runtime-defense/runtime-defense-hosts\#log-inspection)

Prisma Cloud lets you collect and analyze logs from operating systems and applications for security events. For each inspection rule, specify the log file to parse and any number of inspection expressions. Inspection expressions support the [RE2 regular expression syntax](https://github.com/google/re2/wiki/Syntax).

A number of predefined rules are provided for apps such as `sshd`, `mongod`, and `nginx`.

Regardless of the specified inspection expression, log inspection has the following boundaries.

- The maximum amount of bytes read per second is `100`.

- The maximum amount of bytes in a chunk read per second is `2048`.


These boundaries are non-customizable.

### File integrity management (FIM)[Direct link to heading](https://docs.prismacloud.io/admin-guide/runtime-defense/runtime-defense-hosts\#file-integrity-management-fim)

Changes to critical files can reduce your overall security posture, and they can be the first indicator of an attack in progress. The Prisma Cloud FIM from Prisma Cloud continuously monitors your files and directories for changes. You can configure FIM to detect:

- Read or write operations on sensitive files, such as certificates, secrets, and configuration files.

- Binaries written to the file system.

- Abnormally installed software. For example, FIM can detect files written to a file system by programs other than `apt-get`.


A monitoring profile consists of rules, where each rule specifies the path to monitor, the file operation, and the exceptions to the rule.

![runtime defense hosts fim rule](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-dae3bff29916cfdd6707e888e392e75be3b671df%252Fruntime_defense_hosts_fim_rule.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=95a54453456a415a4e5540902810f2e1&sv=3)

The file operations supported are:

- Writes to files or directories When you specify a directory, recursive monitoring is supported.

- Read When you specify a directory, recursive monitoring isn’t supported.

- Attribute changes The attributes watched are permissions, ownership, timestamps, and links. When you specify a directory, recursive monitoring isn’t supported.


### Activities[Direct link to heading](https://docs.prismacloud.io/admin-guide/runtime-defense/runtime-defense-hosts\#activities)

Set up rules to audit [host events](https://docs.prismacloud.io/admin-guide/audit/host-activity).

### Custom rules[Direct link to heading](https://docs.prismacloud.io/admin-guide/runtime-defense/runtime-defense-hosts\#custom-rules)

For details on the custom rules policy refer to [this](https://docs.prismacloud.io/admin-guide/runtime-defense/custom-runtime-rules) section.

## Monitoring[Direct link to heading](https://docs.prismacloud.io/admin-guide/runtime-defense/runtime-defense-hosts\#monitoring)

To view the data collected about each host, go to **Monitor > Runtime > Host observations**, and select a host from the list.

### Apps[Direct link to heading](https://docs.prismacloud.io/admin-guide/runtime-defense/runtime-defense-hosts\#apps)

The **Apps** tab lists the running programs on the host. New apps are added to the list only on a network event.

Prisma Cloud automatically adds some important apps to the monitoring table even if they don’t have any network activity, including `cron` and `systemd`.

![host runtime apps](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-efdc7f667df7ba901b845017c6de29767250685f%252Fhost_runtime_apps.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=701ad95611cdab2db3b8ad10d789db5c&sv=3)

For each app, Prisma Cloud records the following details:

- Running processes (limited to 15).

- Outgoing ports (limited to 5).

- Listening ports (limited to 5).


Prisma Cloud keeps a sample of spawned processes and network activity for each monitored app, specifically:

- Spawned process — Processes spawned by the app, including observation timestamps, username, process (and parent process) paths, and the executed command line (limited to 15 processes).

- Outgoing ports — Ports used by the app for outgoing network activity, including observation timestamps, the process that triggered the network activity, IP address, port, and country resolution for public IPs (limited to 5 ports).

- Listening ports — Ports used by the app for incoming network activity, including the listening process and observation timestamps (limited to 5 ports).


Proc events will add the proc only to existing apps in the profile. The defender will cache the runtime data, saving timestamps for each of the 15 processes' last spawn time.

Limitations:

- Maximum of 50 apps.

- Last 10 spawned processes for each app.


### SSH session history[Direct link to heading](https://docs.prismacloud.io/admin-guide/runtime-defense/runtime-defense-hosts\#ssh-session-history)

The **SSH events** tab shows `ssh` commands run in interactive sessions, limited to 100 events per hour.

![host runtime ssh history](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-8cc89a4783365b7317f22417731eb22cb567ee36%252Fhost_runtime_ssh_history.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=3a0e003a899211099aab770c4a1731ce&sv=3)

### Security updates[Direct link to heading](https://docs.prismacloud.io/admin-guide/runtime-defense/runtime-defense-hosts\#security-updates)

Prisma Cloud periodically checks for security updates. It’s implemented as a compliance check. This feature is supported only for Ubuntu/Debian distributions with the "apt-get" package installer.

Prisma Cloud probes for security updates every time the scanner runs (every 24 hours, by default). The check is enabled by default in **Defend > Compliance > Hosts** in the **Default - alert on critical and high** rule.

![host runtime update compliance check](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-7295284ea49c24bcdb91afe0ea700c0c642dbc2a%252Fhost_runtime_update_compliance_check.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=fce477cb36698a0721901bc1d526f170&sv=3)

The **Security Updates** show the pending security updates (based on a new compliance check that was added for this purpose). Supported for Ubuntu and Debian.

On each host scan, Prisma Cloud checks for available package updates marked as security updates and lists such updates under **Security Updates**.

## Audits[Direct link to heading](https://docs.prismacloud.io/admin-guide/runtime-defense/runtime-defense-hosts\#audits)

You can view audits about host runtime events under **Monitor > Events > Host audits**.

[PreviousRuntime defense for containers](https://docs.prismacloud.io/admin-guide/runtime-defense/runtime-defense-containers) [NextRuntime defense for serverless](https://docs.prismacloud.io/admin-guide/runtime-defense/runtime-defense-serverless)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
