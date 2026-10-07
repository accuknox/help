For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-advanced-settings.md).

Advanced settings control various aspects of WAAS features.

![waas advanced settings](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-2fcae5253935e33ee849463d851225c318ceacbd%252Fwaas_advanced_settings.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=469607128a1069ff5ed0b45d7ee97fdd&sv=3)

## Prisma Sessions[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-advanced-settings\#prisma-sessions)

![waas prisma sessions](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-93438a9f9715fbf673e612df19f32c014c9799aa%252Fwaas_prisma_sessions.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=e5291865259679a5544e4f937d92bb9c&sv=3)

Prisma sessions are intended to address the problem of "Cookie Droppers" by validating clients support of cookies and Javascript before allowing them to reach the origin server.

Once enabled, WAAS serves an interstitial page for any request that does not include a valid Prisma Session Cookie. The interstitial page sets a cookie and redirects the client to the requested page using Javascript.

A client that doesn’t support cookies and Javascript will keep receiving the interstitial page. Browsers can easily proceed to the requested page, and once they possess a valid cookie they will not encounter the interstitial page.

When you enable Prisma Session Cookies along with WAAS API protection, remember that APIs are often accessed by "primitive" automation clients. Avoid enabling Prisma Session Cookies on such endpoints unless you are certain all clients accessing the protected API endpoints support both cookies and Javascript. You can allow "primitive" clients by adding them as [user-defined bots](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-bot-protection#user-defined-bot) and setting the bot action to `Allow`. Allowed [user-defined bots](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-bot-protection#user-defined-bot) will not be served with an interstitial page and their requests will be forwarded to the protected application.

Prisma Session Cookies set by WAAS are encrypted and signed to prevent cookie tampering. In addition, cookies include advanced protections against cookie replay attacks where cookies are harvested and re-used in other clients.

## Ban[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-advanced-settings\#ban)

![waas ban settings](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-11bb18d9cd563094412ad73fbcfa7d7a3323f180%252Fwaas_ban_settings.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=325f88835a52aeb2df1da47fefb5bbd5&sv=3)

Ban action is available in the `App firewall`, `DoS protection` and `Bot protection` tabs. If triggered the ban action prevents access to the protected endpoints of the app for a time period set by you (the default is set to 5 minutes).

If Prisma Session Cookies are enabled, you can apply the `ban` action by either `Prisma Session Id` or by IP address.

When the X-Forwarded-For HTTP header is included in the request headers, actions will apply based on the first IP listed in the header value (true client IP).

## Body Inspection[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-advanced-settings\#body-inspection)

![waas body inspection](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-00c08e2b1b4f3987ba730ce19efa2b040024050e%252Fwaas_body_inspection.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=08c891ca8f45ef37b1b5ecf3cc5a7f6e&sv=3)

Body inspection can be disabled or limited up to a configurable size (in Bytes).

WAAS body inspection limit is 131,072 Bytes (128Kb). WAAS protection is subject to one of the following actions when the body inspection limit exceeds:

- **Disable** \- The request is passed to the protected application.

- **Alert** \- The request is passed to the protected application and an audit is generated for visibility.

- **Prevent** \- The request is denied from reaching the protected application, an audit is generated and WAAS responds with an HTML page indicating the request was blocked.

- **Ban** \- Can be applied on either IP or Prisma Session IDs. All requests originating from the same IP/Prisma Session to the protected application are denied for the configured time period (default is 5 minutes) following the last detected attack.


To enable ban by Prisma Session ID, enable the Prisma Session Cookies in WAAS Advanced Settings.

## Remote Host[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-advanced-settings\#remote-host)

![waas remote proxy](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-789e10152be5760353e550912e609319a02b87f0%252Fwaas_remote_proxy.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=98ccc8def8ec780fc9436b6bdc79e234&sv=3)

This option is intended to defend web applications running on remote hosts which can not be protected directly by WAAS (for example, Windows Servers).

Remote host option is only available for WAAS host rules.

Use-case scenario:

1. A "middle-box" host instance with WAAS supported OS should be set up.

2. Traffic to the web application should be directed to the "middle-box" host.

3. Ports on the "middle-box" host to which traffic is directed to should be unused (WAAS will listen on these ports for incoming requests).

4. WAAS host rule with `Remote host` settings should be deployed to protect the "middle-box" host.

5. Incoming traffic to the "middle-box" host will be forwarded to the specified address (resolvable hostname or IP address) by WAAS.


WAAS sets the original `Host` HTTP header value in the `X-Forwarded-Host` HTTP header of the forwarded request. The `Host` header is set to the hostname or IP mentioned in the WAAS settings.

Use of TLS and destination port is determined by the endpoint configuration in the `App definition` tab.

Example:

The following protected endpoints are defined in the `App definition` tab:

![waas forward example](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-c6a09b3131b453d66e2c7d3b2ce35d4148d62c68%252Fwaas_forward_example.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=0463f16934f7d2a751ad96a079d3bfeb&sv=3)

Remote host has been configured as follows:

![waas remote proxy example](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-92363825585396d526bf63ac70addf05c95a6c3a%252Fwaas_remote_proxy_example.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=bbf8c37e6ca54fea99f516d8520fdadb&sv=3)

Expected result is as follows:

- HTTPS traffic to www.example1.com on port 443 would be forwarded via HTTPS to www.remotehost.com

- HTTP traffic to www.example1.com on port 80 would be forwarded via HTTP to www.remotehost.com


Protected endpoints with TLS enabled will not forward non-TLS HTTP requests.

Enter the host address without 'http' or 'https' string. For example, enter `www.example.com` and not [http://www.example.com](http://www.example.com/).

Enter the host address without 'http' or 'https' string. For example, enter "www.example.com" and not "http://www.example.com". Enter the host address without 'http' or 'https' string. For example, enter "www.example.com" and not "http://www.example.com".

## Customize WAAS Response Message[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-advanced-settings\#customize-waas-response-message)

![waas custom response](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-f07d73d8bfded8b61d640a263bbb9ca7a5eb664c%252Fwaas_custom_response.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=9650a389ac1310ef9357928ec7f32d58&sv=3)

You can customize the response HTML and HTTP status code that are returned by WAAS when a `Prevent` or `Ban` effect occurs:

- **Prevent response code** \- HTTP response code

- **Custom WAAS response message** \- HTML code to be served. Click on image::waas\_preview\_HTML.png\[scale=10\] for a preview of the rendered HTML code.


You can include Prisma Event IDs as part of customized responses by adding the following placeholder in user-provided HTML: `#eventID`.

User-provided HTML must start and end with HTML tags.

Javascript code will not be rended in the preview window.

## Prisma Event IDs[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-advanced-settings\#prisma-event-ids)

By default, responses sent to end users by WAAS are assigned an Event ID that may later be searched in the event monitor. An event ID is included in the response header **X-Prisma-Event-Id** and is also included in the default WAAS block message:

![waas eventid response](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-a6a6cba23d31f2b5d041cf80fc30c3141c64ad44%252Fwaas_eventid_response.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=94c3b737f030048cccd216a985eec1b5&sv=3)

You can include Prisma Event IDs as part of customized responses by adding the following placeholder in user-provided HTML: `#eventID`.

Prisma Event IDs can be referenced in WAAS Event Analytics using the `Event ID` filter:

![waas eventid filter](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-3584c8cba55a017effa90e43702b4189dbbbd467%252Fwaas_eventid_filter.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=7386bd2582e251f90aca076ef7a4105f&sv=3)

[PreviousAccess control](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-access-control) [NextAnalytics](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-analytics)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
