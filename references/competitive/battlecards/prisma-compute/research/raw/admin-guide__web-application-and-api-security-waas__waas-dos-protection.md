For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-dos-protection.md).

WAAS is able to enforce rate limit on IPs or sessions to protect against high-rate and "low and slow" application layer DoS attacks.

![waas dos protection](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-088004304f69cdd66081959d08d8940421e76436%252Fwaas_dos_protection.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=271d27a57950dacd5dee8ce37738f2f0&sv=3)

## DoS protection Overview[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-dos-protection\#dos-protection-overview)

WAAS is able to limit the rate of requests to the protected endpoints within each app based on two configurable request rates:

- **Burst Rate** \- Average rate of requests per second calculated over a 5 seconds period

- **Average Rate** \- Average rate of requests per second calculated over a 120 seconds period


Users are able to specify match conditions for qualifying requests to be included in the count. Match conditions are based on HTTP methods, File Extensions and HTTP response codes.

Users are also able to specify [Network lists](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-access-control#network-lists) to be excluded from the DoS protection rate accounting.

If no match conditions are specified - all requests to the protected endpoints would be included in the rate accounting.

## Enabling DoS protection[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-dos-protection\#enabling-dos-protection)

1. Enter **DoS Protection** tab and set the `DoS Protection` toggle to `On`















![waas dos protection toggle](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-42a850ab631e1d2444d3103dab99befb2409fe7b%252Fwaas_dos_protection_toggle.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=4bf497bdf4187b65a5587c82848fd13c&sv=3)

2. Set the effect with the [action](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-dos-protection#dos-actions) to apply once a threshold is reached.















![waas dos action](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-6b0a3c0455fce087fdbd0e418a50e2c12946fd0c%252Fwaas_dos_action.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=c04e6398ffbff4344a582e4dee8cea89&sv=3)











A message at the top of the page indicates the entity by which the ban will be applied (IP or Prisma Session ID).











To enable ban by Prisma Session ID, [Prisma Session Cookies](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-advanced-settings#prisma-session) has to be enabled in the Advanced Settings tab. for more information please refer to the [Advanced Settings](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-advanced-settings#prisma-session) help page.

3. Apply rate limitation thresholds (requests per second) for `Burst rate` (calculated over 5 seconds) and for `Average rate` (calculated over 120 seconds)

4. To apply the rate limitation on a subset of requests click on button.















![waas dos new condition](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-a1e2f5b84746969173d90fd1992ed8303f99c3fd%252Fwaas_dos_new_condition.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=d56426a4d89170a39f7c078cef609f04&sv=3)











Conditions can be specified as a combination ( **AND**) of the following:









   - **HTTP Methods**

   - **File Extensions** \- multiple extensions are allowed (e.g. `.jpg, .jpeg, .png`).

   - **HTTP Response Codes** \- specify either a single response code, a range or a combination of them (e.g. `302, 400-410, 500-599`).


5. Multiple match conditions are allowed ( **OR** relation between them).















![waas dos multi](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-d02bbaa5e18c0fdd34b06cb544f22a9a65574522%252Fwaas_dos_multi.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=bb741df7aae85765c350119199dbaa65&sv=3)











In the above example the following request would be counted against the rate limitation thresholds:









   - `HEAD` HTTP requests

   - `POST` HTTP requests with file extension of `.tar.gz`

   - `GET` or `PUT` HTTP requests with file extension of `.jpg, .jpeg, .png` to which the origin responded with and HTTP response code of `302` or in the range of `400-410` or in the range of `500-599`


6. Specify [Network lists](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-access-control#network-lists) of IP addresses to be excluded from the rate accounting.















![waas dos excluded](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-83e7f2223a0b0805ec8da869d692d4e5a5439078%252Fwaas_dos_excluded.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=e0d8095a3659081a3da6ca9cb8d93c6c&sv=3)


## DoS actions[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-dos-protection\#dos-actions)

Requests that exceed the rate limitation thresholds are subject to one of the following actions:

- **Alert** \- The request is passed to the protected application and an audit is generated for visibility.

- **Ban** \- Can be applied on either IP or Prisma Session. All requests originating from the same IP/Prisma Session to the protected application are denied for the configured time period (default is 5 minutes) following the last detected attack.


A message at the top of the page indicates the entity by which the ban will be applied (IP or Prisma Session ID). When the X-Forwarded-For HTTP header is included in the request headers, ban will apply based on the first IP listed in the header value (true client IP).

For more information on enabling Prisma Sessions and configuring ban definitions please refer to the [Advanced Settings](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-advanced-settings#ban-settings) help page.

WAAS implements state, which is required for banning user sessions by IP address or Prisma Sessions. Because Defenders do not share state, any application that is replicated across multiple nodes must enable IP stickiness on the load balancer.

[PreviousAPI protection](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-api-protection) [NextBot protection](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-bot-protection)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
