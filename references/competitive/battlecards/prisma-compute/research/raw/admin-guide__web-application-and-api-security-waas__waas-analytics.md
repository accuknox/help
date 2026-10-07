For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-analytics.md).

WAAS analytics provide users a way to investigate events and rule triggers.

![waas analytics](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-aa37864cca3a02d45351ee8721a78ccb933b3f54%252Fwaas_analytics.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=dfabfb76317a2030faf18dd88a46f9af&sv=3)

- For container WAAS events go to **Monitor > Events > WAAS for containers**

- For host WAAS events go to **Monitor > Events > WAAS for hosts**

- For App-Embedded WAAS events go to **Monitor > Events > WAAS for App-Embedded**

- For serverless WAAS events go to **Monitor > Events > WAAS for Serverless**


WAAS retains up to 200,000 events for each type (container, hosts, app-embedded and serverless) or or a total of 200MB in log size. Once the limit is reached, oldest events will get over-written by new ones.

Similar audits are aggregated and grouped into a single event when received in close succession (less than 5 minutes apart). Audits are aggregated by a combination of IP, HTTP hostname, path, HTTP method, User-Agent and attack type.

## Analytics workflow[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-analytics\#analytics-workflow)

![waas analytics cycle](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-0c257bab715d09e635175bf7617d5963bfed09b8%252Fwaas_analytics_cycle.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=40d998f7dc0aeedd213e7d62e5010651&sv=3)

WAAS analytics allows for the review of incidents by analyzing events across various dimensions, inspecting individual requests, and applying filtering to focus on common characteristics or trends.

## Event graph[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-analytics\#event-graph)

![waas timeline](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-72e86d65c0bc8e3b18d165149670bede6227b6cb%252Fwaas_timeline.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=d9207d7d6175f4db0b7ce0a51d5d88a0&sv=3)

A timeline graph shows the total number of events. Each column on the timeline graph represents a dynamic period - hover over a column to reveal its start, end and event count.

The date filter can be adjusted by holding and selecting sections on the timeline graph.

## Filters[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-analytics\#filters)

Filter can be adjusted by using the filtering line:

![waas analytics filters](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-5cfbdad1958affcb39dbfaaca3a8a65b0dd4e2a7%252Fwaas_analytics_filters.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=cb98a411a91d13e2744033806af1896b&sv=3)

The filter line uses auto-complete for filter names and filter values. Once set, the filters would apply on the graph and aggregation view.

You can dynamically update the date filter by selecting an area in the chart. Click in the chart area, hold the mouse button down, and draw a rectangle over the time frame of interest. The date filter is automatically updated to reflect your selection.

## Aggregation view[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-analytics\#aggregation-view)

![waas analytics aggregated view](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-41a11aa376203ce74c1d9b69305f2706d893d7df%252Fwaas_analytics_aggregated_view.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=95b0ce88fec6d723ede6dd044190292f&sv=3)

The aggregation view can be altered to group audits based on various data dimensions by clicking on the button.

Users can add up to 6 dimensions to the aggregation and the Total column will be updated dynamically.

By default, aggregation view is sorted by the "Total" column. Sorting can be changed by clicking a column name.

Click on a line in the aggregation view to inspect the requests group by it.

## Request view[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-analytics\#request-view)

![waas analytics sample view](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-215369912595c5687f4b6e515582111e897ffb19%252Fwaas_analytics_sample_view.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=2310bfb2493847cf3b6208fc8cfd24c1&sv=3)

Request view details all of the requests group by each line of the aggregated view.

Clicking on a column name will sort the table in the upper section and using the button will add/remove columns.

For each request the following data points are available:

**Audit data:**

- **Time** \- timestamp of the audit.

- **Effect** \- effect set by policy.

- **Request Count** \- If audits are received in close succession (less than 5 minutes apart) they are aggregated and grouped into one event. This field specifies the number of aggregated requests.

- **Rule Name** \- name of the WAAS rule that matched the request and generated the event. Navigate to the configuration of the rule by clicking on the link.

- **Rule app ID** \- corresponding app ID in the WAAS rule which triggered the event. Navigate to the configuration of the app ID by clicking on the link.

- **Attack Type** \- attack type.

- **ATT&CK technique** \- mapping to the techniques in the ATT&CK framework.

- **Container / Host / App / Function Details** \- These fields include the id and name of the protected entity.


**Forensics:**

- **Forensic Message** \- details on what caused the rule to trigger - payload content, location and additional relevant information.

- **Add as exception** \- By clicking on the link, you can add an exception in the rule app ID for the attack type that triggered. The exception will be based on the location of the matched payload.















![waas analytics add exception](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-efbfe6c060c06dd64e0eb034e2d8307a59bfd5cd%252Fwaas_analytics_add_exception.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=514602d768528b81e1ce3e70656e996b&sv=3)


The "Add as exception" link may not be available for events created by rules and apps that no longer exist, as well as for events created in releases earlier than 21.08.

For App-Embedded WAAS events, the **Add as exception" button does not allow you to add an exception directly from an event. You can manually add exceptions to rules. Click the \*Rule app ID** on the "Aggregated WAAS Events" page and edit the relevant detection.

![cwp 44743 app embedded add exception](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-0a40d6d697a8f73806d71f20d6e55e1d0dbe7ad7%252Fcwp-44743-app-embedded-add-exception.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=042443c59cde8f4c60cff961c984176d&sv=3)

**HTTP request:**

- **Method** \- HTTP method used in the request.

- **User-Agent** \- value of the User-Agent HTTP header.

- **Host** \- hostname specified in the `Host` HTTP header or the host part of the URL.

- **URL** \- full request urls (host and path) shown in a URL decoded or encoded form.

- **Path** \- path element from the request URI.

- **Query** \- query string.

- **Header Names** \- list of the HTTP header names included in the request (sorted alphabetically).


**Attacker:**

- **Add IPs to Network List** \- Adds the attacker IP either to a new network list or to an existing one. To access **Network Lists**, open Console, go to **Defend > WAAS** and select the **Network List** tab.

- **Source IP** \- IP address from which the request originated. If an `X-Forwarded-For` header was included in the HTTP headers, source IP field will detail the first IP listed in the header value (true client IP).

- **Source Country** \- source country associated with the source IP.

- **Connecting IPs** \- entire connectivity chain, including true client IP and any transparent proxies listed in the HTTP request.


Users can user the `Raw` button to view the HTTP request in it’s raw form:

![waas analytics raw demo](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-b41dd1cd03f33f0111263ed86cfcb62e5d620a52%252Fwaas_analytics_raw_demo.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=11dd81f21fdde60d2443eaa32606ec36&sv=3)

[PreviousAdvanced settings](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-advanced-settings) [NextAPI Discovery](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-api-discovery)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
