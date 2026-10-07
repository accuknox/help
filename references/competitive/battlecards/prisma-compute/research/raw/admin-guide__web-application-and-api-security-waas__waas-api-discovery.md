For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-api-discovery.md).

WAAS can automatically learn the API endpoints in your app, show an endpoint usage report, and let you export all discovered endpoints as an OpenAPI 3.0 spec file.

When API discovery is enabled, the Defender inspects API traffic routed to the protected app. Defenders learn the endpoints in your API by analyzing incoming requests and generating a tree of API paths. Every 30 minutes, Defender sends the Console a diff of what it has learned since its last update. The Console merges the update with what it already knows about the API.

The API discovery subsystem attempts to ignore all HTTP traffic that doesn’t resemble an API call. The Defender uses some criteria for identifying which requests to inspect:

- Requests must have non-error response codes.

- Requests must not have extensions (like .css, and .html).

- Requests Content-Type must be textual (`text/`), application (`application/`), or empty.


On the API discovery database, when new path entries for images or API endpoints are added, the Console uses the 'Last Observed' date to delete the older entries to optimize the available resources. When an image or API endpoint is deleted from the database, an alert is generated, and the details are written to the Console logs.

## Enable API Discovery[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-api-discovery\#enable-api-discovery)

API discovery is enabled by default when you create a WAAS policy. To enable API discovery for a protected app after the rule is created:

1. Log in to the Console, and go to **Defend > WAAS > {Container (Inline/Out-Of-Band) \| Host (Inline/Out-Of-Band) \| App-Embedded \| Serverless \| Agentless}**.

2. Select an existing rule and enable **API endpoint discovery**.


## Inspect discovered endpoints[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-api-discovery\#inspect-discovered-endpoints)

The endpoint report under **Monitor** \> **WAAS** \> **API discovery** \> enumerates discovered APIs per path, HTTP method, app, and on an image basis. It shows information such as Path, HTTP method, Hits, API protection status, Path risks, Workload that’s running these resources, Image Risk factors, Resource Vulnerabilities, App ID, and last seen date.

![waas api discovery](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-b5797715350bd1e0bbd501c0c32526dc10241d1f%252Fwaas-api-discovery.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=988f386b20c6bb22c3620152fef261c6&sv=3)

**Path risks profiling**

The **Path risks** indicate critical path risks identified in the endpoints:

- Endpoints accessible from the internet.

- Endpoints that do not require authentication to be accessed.

- Endpoints with sensitive data such as Credit card, PII, ID query parameter, Session cookies, and so on. The [sensitive data](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/log-scrubbing) is defined under **Defend > WAAS > Sensitive data**.

- Endpoints with OWASP risks.


For example, some of the path risks detect the resource path with vulnerable API endpoints that are exposed to the internet, APIs with sensitive data, and APIs that allow unauthenticated access to them.

Select an endpoint to view the sidecar with additional statistics in the `JSON` structure, such as request and response size ranges, the sum of each specific returned status code, and the API change history.

The statistics also show the `JSON` payload that was sent with the API request.

![waas api discovery sidecar1](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-4c22db276219c6a794edc4e9b339fac08ae3640e%252Fwaas-api-discovery-sidecar1.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=9b40933d881c65e1975c2c88b785fdb3&sv=3)

API **Change History** logs detect changes in API observations such as authentication, query parameters, path risks, or any new sensitive data matches, but not changes to the body of API messages.

![waas api discovery api change history](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-d99088c356a9d8e1729703c286fdc86d6b2dd273%252Fwaas-api-discovery-api-change-history.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=304bfd726ed53c2a29166e4ba3e07fa0&sv=3)

Under **Actions**, you can protect a path in an app, export the discovered endpoints for an app as an OpenAPI spec file, and also delete what WAAS has learned about the API for an app so far.

If a rule with an app is deleted from the WAAS policy, its learned endpoints are also deleted.

**Protecting endpoints**

Select **Protect** next to a resource to protect a path, set effects for all API endpoints discovered in the App, and select **Protect all**. This enables you to protect all the API endpoints in the resource path identified within an app to the WAAS policy rule, not just the selected path. When there is an event generated from a new endpoint, you have to explicitly **Protect** it.

![waas protecting policy](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-de08a1a63ef6065697fc67daa4a68b635692110a%252Fwaas-protecting-policy.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=ff038cf0efe6a6ccd051ad9eba4db3e1&sv=3)

**Export API specifications**

Select **Export OpenAPI** next to the resource path to export all the API endpoints, HTTP method, and the Server name discovered by the app for the given WAAS policy rule as OpenAPI 3.0 JSON.

![export api specifications](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-1427971be1239236c4860b41073897a2f9206302%252Fexport-api-specifications.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=9da14390c35bad39580f50b666329959&sv=3)

The export of API endpoints in OpenAPI format does not support custom HTTP methods. The following HTTP methods specified in RFC-7231 section 4.3 are supported:

- GET

- POST

- PUT

- DELETE

- OPTIONS

- HEAD

- PATCH

- TRACE

- CONNECT


For more details, refer to the [RFC-7231 documentation](https://datatracker.ietf.org/doc/html/rfc7231#section-4.3).

## Limitations[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-api-discovery\#limitations)

- Click to Protect/Delete/Download openAPI actions apply to all paths in the app, and not possible to select individual paths.

- The amount of APIs that we can discover per image is limited to a size < 1k, and query parameters size is < 20k.

- Filtering/sorting the API discovery endpoints by **API Protection** status is not applicable, as the protection status is calculated at the time of fetch (based on current policy).


## Troubleshooting[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-api-discovery\#troubleshooting)

- If a path is not learned on the **API discovery** page, it could be because the endpoint is not a valid path (the endpoint didn’t return a status code of '200 OK'). The request had a WAF violation in it (The requests that trigger firewall rules are not learned).

- Public API flagged as an error. If the source IP of an endpoint does not belong to a known internet IP address, the API containing this endpoint is flagged as an error. This is because the IP addresses are stored in a static database, which could be outdated.

- Some of the endpoints are not flagged as unauthenticated. This is because for authentication we use a list of known headers and replies (401 response code) to learn, so if you are using some non-standard header for authentication, your endpoint will not be flagged.


[PreviousAnalytics](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-analytics) [NextAPI definition scan](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/api-def-scan)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
