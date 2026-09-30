> For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.prismacloud.io/content-collections/runtime-security/audit/host-activity.md).

# Host Activity

Prisma Cloud lets you audit security-related activity on hosts protected by Defender.

Runtime rules specify the type of activity to capture. The default host runtime rule, *Default - alert on suspicious runtime behavior*, assesses interactive user activity. You can create additional runtime rules to control which type of events are captured on which hosts.

The following types of activity can be assessed and captured.

* **Docker** — Docker commands that alter state: create, run, exec, commit, save, push, login, export, kill, start, stop, and tag.
* **Read-only Docker events** — When you configure Prisma Cloud to capture Docker commands, you can optionally capture commands that simply read state. These include *docker ps* and *docker images*.
* **New sessions spawned by sshd** — Self-explanatory.
* **Commands run with sudo or su** — Self-explanatory.
* **Log activity from background apps** — Processes run by services on the host that could raise security concerns. Activities include: service restart, service install, service modified, cron modified, system update, system reboot, package source modified, package source added, iptables changed, secret modified, accounts modified, and sensitive files modified.

Whereas Defender’s runtime system surfaces suspect activity by sifting through events, Defender’s [forensics](/content-collections/runtime-security/runtime-defense/incident-explorer.md#forensics) system presents a raw list of all spawned processes.

## Enabling audits for local events

To enable audits for host activity, create a new host runtime rule. After making your changes, you can view all audits in **Monitor > Events** with the **Host Activities** filter.

Auditing begins after a rule is created. Any events that occurred before the rule was created are not recorded.

1. Open Console.
2. Go to **Defend > Runtime > Host Policy**.
3. Click **Add rule**, and give it a name.
4. In **Hosts**, specify the hosts for which this rule applies.
5. In the **Activities** tab, enable the events for which you want audits.
6. Click **Save**.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.prismacloud.io/content-collections/runtime-security/audit/host-activity.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
