For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/configure/log-scrubbing.md).

Prisma Cloud Compute Runtime events may include sensitive information that’s found in commands that are run by protected workloads, such as secrets, tokens, PII, or other information considered to be personal by various laws and regulations.

Using the Runtime log scrubbing capabilities, you can filter such sensitive information and ensure that it is not included in the Runtime findings (such as Forensics, Incidents, audits, and so on.).

You can filter your Runtime sensitive data out using the automatic scrubbing capability, as well as using custom scrubbing rules. Follow the documentation instructions to learn more about these two options.

Sensitive information from WAAS logs can be scrubbed as well, see [WAAS Log Scrubbing](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/log-scrubbing) to learn more.

## Automatically scrub secrets from runtime events[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/log-scrubbing\#automatically-scrub-secrets-from-runtime-events)

You can enable the automatic scrubbing of known sensitive phrases (such as "secrets", "passwords", "tokens", and so on.) from your runtime events. The detected sensitive data will be replaced in the events by `"[*****]"`.

### Enable/Disable the automatic scrubbing:[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/log-scrubbing\#enable-disable-the-automatic-scrubbing)

1. Open the Console, and go to **Manage > System > General**.

2. Enable/Disable **Automatically scrub secrets from runtime events**.


## Add/Edit custom scrubbing rule[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/log-scrubbing\#add-edit-custom-scrubbing-rule)

Create or edit log scrubbing rules.

1. Open the Console, and go to **Manage > System > General**.

2. In the **Custom log scrubber** section select **Runtime** or **WAAS**.

3. Click on **Add rule** or select an existing rule.

4. Enter the rule **Name**.

5. Provide a matching **Pattern** in the form of a regular expression ([re2](https://github.com/google/re2/wiki/Syntax)), e.g. `^sessionID$`, `key-[a-zA-Z]{8,16}`.

6. Provide a **Placeholder** string e.g. `[scrubbed email]`.









1. Placeholder strings indicating the nature of the scrubbed data should be used as users will not be able to see the underlying scrubbed data.


7. Click **Save**.









   - Data will now be scrubbed from any Runtime and WAAS event before it is written (either to the Defender log or syslog) and sent to the console.

   - The automatic scrubbing and custom scrubbing are independent, meaning that you can choose to use each one of them separately.

   - Data will be scrubbed only in messages that are generated while the scrubbing toggle or scrubbing rule is **enabled**. Messages that were generated **before** enabling one of the scrubbing configurations above or **after** disabling them, won’t be scrubbed.

   - The WAAS scrubbing rules are synced with the rules in **Defend > WAAS > Sensitive data**.

   - Serverless Runtime events are not scrubbed.


![runtime log scrubbing](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-349d739956c1e329c37d7311e79f4ff51ae751ea%252Fruntime_log_scrubbing.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=b9859d53c399f9444ea42e346956a811&sv=3)

[PreviousWildFire settings](https://docs.prismacloud.io/admin-guide/configure/wildfire) [NextClustered-DB](https://docs.prismacloud.io/admin-guide/configure/clustered-db)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
