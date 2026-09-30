> For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.prismacloud.io/content-collections/runtime-security/waas/waas-api-discovery.md).

# API Discovery

WAAS can automatically learn the API endpoints in your app, show an endpoint usage report, and let you export all discovered endpoints as an OpenAPI 3.0 spec file.

When API discovery is enabled, the Defender inspects API traffic routed to the protected app. Defenders learn the endpoints in your API by analyzing incoming requests and generating a tree of API paths. Every 30 minutes, Defender sends the Console a diff of what it has learned since its last update. The Console merges the update with what it already knows about the API.

The API discovery subsystem attempts to ignore all HTTP traffic that doesn’t resemble an API call. The Defender uses some criteria for identifying which requests to inspect:

* Requests must have non-error response codes.
* Requests must not have extensions (like .css, and .html).
* Requests Content-Type must be textual (`text/`), application (`application/`), or empty.

On the API discovery database, when new path entries for images or API endpoints are added, the Console uses the 'Last Observed' date to delete the older entries to optimize the available resources. When an image or API endpoint is deleted from the database, an alert is generated, and the details are written to the Console logs.

## Enable API Discovery

API discovery is enabled by default when you create a WAAS policy. To enable API discovery for a protected app after the rule is created:

1. Log in to the Console, and go to **Runtime Security > Defend > WAAS > {Container (Inline/Out-Of-Band) | Host (Inline/Out-Of-Band) | App-Embedded | Serverless | Agentless}**.
2. Select an existing rule and enable **API endpoint discovery**.

## Inspect Discovered Endpoints

The endpoint report under **Runtime Security > Monitor** > **WAAS** > **API discovery** > enumerates discovered APIs per path, HTTP method, app, and on an image basis. It shows information such as Path, HTTP method, Hits, API protection status, Path risks, Workload that’s running these resources, Image Risk factors, Resource Vulnerabilities, App ID, and last seen date.

<figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-b5797715350bd1e0bbd501c0c32526dc10241d1f%2Fwaas-api-discovery.png?alt=media" alt="waas api discovery"><figcaption></figcaption></figure>

**Path risks profiling**

The **Path risks** indicate critical path risks identified in the endpoints:

* Endpoints accessible from the internet.
* Endpoints that do not require authentication to be accessed.
* Endpoints with sensitive data such as Credit card, PII, ID query parameter, Session cookies, and so on. The [sensitive data](/content-collections/runtime-security/waas/log-scrubbing.md) is defined under **Runtime Security > Defend > WAAS > Sensitive data**.
* Endpoints with OWASP risks.

For example, some of the path risks detect the resource path with vulnerable API endpoints that are exposed to the internet, APIs with sensitive data, and APIs that allow unauthenticated access to them.

Select an endpoint to view the side panel with additional statistics in the `JSON` structure, such as request and response size ranges, the sum of each specific returned status code, and the API change history.

The statistics also show the `JSON` payload that was sent with the API request.

<figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-4c22db276219c6a794edc4e9b339fac08ae3640e%2Fwaas-api-discovery-sidecar1.png?alt=media" alt="waas api discovery sidecar1"><figcaption></figcaption></figure>

API **Change History** logs detect changes in API observations such as authentication, query parameters, path risks, or any new sensitive data matches, but not changes to the body of API messages.

<figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-d99088c356a9d8e1729703c286fdc86d6b2dd273%2Fwaas-api-discovery-api-change-history.png?alt=media" alt="waas api discovery api change history"><figcaption></figcaption></figure>

Under **Actions**, you can protect a path in an app, export the discovered endpoints for an app as an OpenAPI spec file, and also delete what WAAS has learned about the API for an app so far.

If a rule with an app is deleted from the WAAS policy, its learned endpoints are also deleted.

**Protecting endpoints**

Select **Protect** next to a resource to protect a path, set effects for all API endpoints discovered in the App, and select **Protect all**. This enables you to protect all the API endpoints in the resource path identified within an app to the WAAS policy rule, not just the selected path. When there is an event generated from a new endpoint, you have to explicitly **Protect** it.

<figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-de08a1a63ef6065697fc67daa4a68b635692110a%2Fwaas-protecting-policy.png?alt=media" alt="waas protecting policy"><figcaption></figcaption></figure>

**Export API specifications**

Select **Export OpenAPI** next to the resource path to export all the API endpoints, HTTP method, and the Server name discovered by the app for the given WAAS policy rule as OpenAPI 3.0 JSON.

The export of API endpoints in OpenAPI format does not support custom HTTP methods. The following HTTP methods specified in RFC-7231 section 4.3 are supported:

* GET
* POST
* PUT
* DELETE
* OPTIONS
* HEAD
* PATCH
* TRACE
* CONNECT

For more details, refer to the [RFC-7231 documentation](https://datatracker.ietf.org/doc/html/rfc7231#section-4.3).

## Limitations

* Click to Protect/Delete/Download openAPI actions apply to all paths in the app, and not possible to select individual paths.
* The amount of APIs that we can discover per image is limited to a size < 1k, and query parameters size is < 20k.
* Filtering/sorting the API discovery endpoints by **API Protection** status is not applicable, as the protection status is calculated at the time of fetch (based on current policy).

## Troubleshooting

* If a path is not learned on the **API discovery** page, it could be because the endpoint is not a valid path (the endpoint didn’t return a status code of '200 OK'). The request had a WAF violation in it (The requests that trigger firewall rules are not learned).
* Public API flagged as an error. If the source IP of an endpoint does not belong to a known internet IP address, the API containing this endpoint is flagged as an error. This is because the IP addresses are stored in a static database, which could be outdated.
* Some of the endpoints are not flagged as unauthenticated. This is because for authentication we use a list of known headers and replies (401 response code) to learn, so if you are using some non-standard header for authentication, your endpoint will not be flagged.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.prismacloud.io/content-collections/runtime-security/waas/waas-api-discovery.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
