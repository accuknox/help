For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/audit/host-activity.md).

Prisma Cloud lets you audit security-related activity on hosts protected by Defender.

Runtime rules specify the type of activity to capture. The default host runtime rule, _Default - alert on suspicious runtime behavior_, assesses interactive user activity. You can create additional runtime rules to control which type of events are captured on which hosts.

The following types of activity can be assessed and captured.

- **Docker** — Docker commands that alter state: create, run, exec, commit, save, push, login, export, kill, start, stop, and tag.

- **Read-only Docker events** — When you configure Prisma Cloud to capture Docker commands, you can optionally capture commands that simply read state. These include _docker ps_ and _docker images_.

- **New sessions spawned by sshd** — Self-explanatory.

- **Commands run with sudo or su** — Self-explanatory.

- **Log activity from background apps** — Processes run by services on the host that could raise security concerns. Activities include: service restart, service install, service modified, cron modified, system update, system reboot, package source modified, package source added, iptables changed, secret modified, accounts modified, and sensitive files modified.


Whereas Defender’s runtime system surfaces suspect activity by sifting through events, Defender’s [forensics](https://docs.prismacloud.io/admin-guide/runtime-defense/incident-explorer#forensics) system presents a raw list of all spawned processes.

## Enabling audits for local events[Direct link to heading](https://docs.prismacloud.io/admin-guide/audit/host-activity\#enabling-audits-for-local-events)

To enable audits for host activity, create a new host runtime rule. After making your changes, you can view all audits in **Monitor > Events** with the **Host Activities** filter.

Auditing begins after a rule is created. Any events that occurred before the rule was created are not recorded.

1. Open Console.

2. Go to **Defend > Runtime > Host Policy**.

3. Click **Add rule**, and give it a name.

4. In **Hosts**, specify the hosts for which this rule applies.

5. In the **Activities** tab, enable the events for which you want audits.

6. Click **Save**.


[PreviousEvent viewer](https://docs.prismacloud.io/admin-guide/audit/event-viewer) [NextAdmin activity](https://docs.prismacloud.io/admin-guide/audit/audit-admin-activity)

Last updated 3 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
