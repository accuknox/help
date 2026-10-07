For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/audit/review-debug-logs.md).

Console and Defender generate logs as they run. These logs, also known as debug data, are designed to help troubleshoot operational issues. They are different from audits, which are designed to report significant security events.

If you contact Prisma Cloud Support with an issue, you will be asked to collect debug data from your setup and send it to us. Debug data helps us find the root cause of problems, and provide timely resolutions.

## Collect Console debug logs[Direct link to heading](https://docs.prismacloud.io/admin-guide/audit/review-debug-logs\#collect-console-debug-logs)

The simplest way to view Console’s debug logs is from **Manage > Logs > Console** and **Download Logs**.

### Send Debug Logs to Syslog[Direct link to heading](https://docs.prismacloud.io/admin-guide/audit/review-debug-logs\#send-debug-logs-to-syslog)

You can also send console logs directly to a syslog server. This can be an efficient way to manage logs, especially when consolidating data for analysis.

- Secure Transmission with TLS Certificate: If you provide a TLS certificate on **Manage > Alerts > Logging** and **Syslog** is set to **Enabled**, the logs will be sent securely over HTTPS, ensuring that your data is encrypted during transit and protected from unauthorized access. See [Sending syslog messages to a network endpoint](https://docs.prismacloud.io/admin-guide/audit/logging) for more information.

- Standard Transmission without TLS Certificate: Without a TLS certificate, the logs will be sent over HTTP, which is not secured. This method is faster but does not encrypt the data.


## Collect Defender debug logs[Direct link to heading](https://docs.prismacloud.io/admin-guide/audit/review-debug-logs\#collect-defender-debug-logs)

To view debug logs of Defender , access **Manage > Defenders > Deployed Defenders**. Select the Defender from the table and then select **Actions > Logs** and **Download Logs**.

[PreviousKubernetes auditing](https://docs.prismacloud.io/admin-guide/audit/kubernetes-auditing) [NextTools](https://docs.prismacloud.io/admin-guide/tools/tools)

Last updated 3 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
