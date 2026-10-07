For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/log-scrubbing.md).

There may be sensitive data captured when WAAS events take place, such as access tokens, session cookies, PII, or other information considered to be personal by various laws and regulations.

By using WAAS sensitive data rules, users can mark **Sensitive data** and enable **Log scrubbing** based on regex patterns or its location in the HTTP request. The data marked as sensitive will be flagged in API discovery, but will not be automatically scrubbed in the Logs. To scrub the sensitive data in addition to marking it as sensitive, enable **Log scrubbing**, the data is scrubbed and replaced with placeholders in the logs before events are recorded.

- The data from HTTP responses that appear in WAAS audits will not be scrubbed and replaced by the placeholder.

- To optimize the CPU utilization when using WAAS sensitive data, Prisma Cloud scanner samples only a subset of the mirrored data to discover just the APIs and the scanner does not inspect the request body field, the sensitive request, and the response data. We sample the API traffic to limit the sensitive data body response size to less than 128k.


## Add/Edit WAAS Scrubbing Rule[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/log-scrubbing\#add-edit-waas-scrubbing-rule)

1. Open the Console, and go to **Defend > WAAS > Sensitive data**.















![waas sensitive data](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-5576fe3cf9bdd8be4f670e47041ab5df8cef525e%252Fwaas-sensitive-data.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=a09fcdc60c2f6cc9269aade8b5ca4382&sv=3)

2. Click on **Add rule** or select an existing rule.

3. Enter a rule **Name**.

4. Select the rule **Type** as **Pattern-based** or **Location-based**.

5. The pattern-based rule will match the given regex pattern by either "Request Parameter keys", "Request Parameter Values", or "Response (Keys + Values)".















![cwp 42645 waas sensitive data new rule](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-083742eaa6111bb1b736c1a76e991da7f9066796%252Fcwp-42645-waas-sensitive-data-new-rule.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=63fff4af650b33f07d8e13d852a6d1f9&sv=3)









1. Provide the pattern name to be matched in the form of a regular expression ([re2](https://github.com/google/re2/wiki/Syntax)), e.g. `^sessionID$`, `key-[a-zA-Z]{8,16}`.

2. Provide a placeholder string, e.g. `[scrubbed sessionID]`.











      Placeholder strings indicating the nature of the scrubbed data should be used as users will not be able to see the underlying scrubbed data.


6. For Location-based rules















![waas log scrubbing new rule dialog location](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-c37c88dfe9dda336c2cfca0c474038d6f65cb6d1%252Fwaas_log_scrubbing_new_rule_dialog_location.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=e2967253a0021ae066d1c67bf636c9d6&sv=3)









1. Select the location of the data to be scrubbed.

2. Provide location details:









      1. For `query` / `cookie` / `header` / `form/multipart` \- provide a match pattern in the form of a regular expression ([re2](https://github.com/google/re2/wiki/Syntax)), e.g. `^SCookie.*$`, `item-[a-zA-Z]{8,16}`.

      2. For `XML (body)` / `JSON (body)` \- provide the path using Prisma Cloud’s custom format e.g. `/root/nested/id`.


3. Provide a placeholder string to indicate the nature of the scrubbed data, for example: `[Scrubbed Session Cookie]`.


7. Click **Save**.











**Sensitive Data & Log Scrubbing**











The location-based rule for sensitive data works by searching for the key value in the location, for example, query, cookie, header, form/multipart, XML, and JSON body. For log scrubbing, WAAS replaces the value with the placeholder that you enter. Data will now be scrubbed from any WAAS event before it is written (either to the Defender log or syslog) and sent to the console.











For example, the email ID is redacted in the below WAAS event audit.















![waas events email redacted](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-a760d8b97f6f2e6713e2f9a17441580213d93579%252Fwaas-events-email-redacted.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=31998e1f7bb97d8975df738c5af11eb1&sv=3)















![waas log scrubbing scrubbed event](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-db608387adf8fb497c1c99b93f9a1a8f5893e09f%252Fwaas_log_scrubbing_scrubbed_event.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=af75efa118a8f5d16cb349f31c71a246&sv=3)











If sensitive data triggers events, both the forensic message and the recorded HTTP request are scrubbed.















![waas log scrubbing scrubbed payload](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-9c0841f7033630f2e326a43c969eea9281643c70%252Fwaas_log_scrubbing_scrubbed_payload.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=1e1efd603dfca3d2c4b3b245328182a1&sv=3)


[PreviousUnprotected web apps](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/unprotected-web-apps) [NextFirewalls](https://docs.prismacloud.io/admin-guide/firewalls/firewalls)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
