> For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.prismacloud.io/release-notes/look-ahead-planned-updates-on-prisma-cloud/look-ahead-secure-the-infrastructure.md).

# Look Ahead Updates to Secure the Infrastructure

Learn more about planned Prisma Cloud updates.

Read this section to learn about what is planned in the 26.8.1 CSPM Platform, Agentless Container Host, Agentless Host Security, CIEM, Data Security, and CDEM releases.

The Look Ahead announcements are for an upcoming release and is not a cumulative list of all announcements.

The details and functionalities listed below are a preview and the actual release date is subject to change.

* [Changes in Existing Behavior](#change-in-behavior)
* [Deprecation Notices](#deprecation-notices)

### Changes in Existing Behavior

#### Config APIs Moving to Limited Availability (LGA)

Starting at the end of October 2026, ingestion for the following config APIs will transition from default general availability to Limited General Availability (LGA). These APIs capture short-lived, transient execution workloads rather than persistent cloud infrastructure configurations:

* gcloud-dataproc-cluster-job
* aws-transcribe-transcription-job
* gcloud-vertex-ai-aiplatform-custom-job

**Impact** - No impact for existing custom policy users. Ingestion will remain enabled for tenants with active custom policies referencing these APIs.

* All other tenants: Ingestion for these APIs will be turned off by default.
* If your organization requires ingestion for any of these APIs, please contact your Palo Alto Networks Customer Support Representative or account team to have them enabled for your tenant.

#### Alerts Endpoint Deprecation

The legacy `alerts/job` API endpoint will be deprecated in the 26.10.1 release.

To improve reliability, system stability, and performance, we are transitioning all alert extraction workflows to the `v2/alert` API.

**Key Improvements**

* Paginated Data Retrieval: Fetch large volumes of alerts incrementally without running into timeout errors.
* Backend Efficiency: Reduces load on backend infrastructure, resulting in faster and more predictable response times.
* High Scalability: Built specifically to handle high-throughput workloads seamlessly.

**Impact** - We strongly encourage all customers utilizing the alerts/job endpoint to migrate their integrations to the v2/alert API.

***

### Deprecation Notices

| **Deprecated Endpoints**                                                                        | **Deprecated** | **Sunset** | **Replacement Endpoints**                                                                                                                                                                                                          |
| ----------------------------------------------------------------------------------------------- | -------------- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Deprecation of alerts/job endpoint**                                                          | 26.10.1        | -          | To improve reliability, system stability, and performance, all alert extraction workflows are transitioning to the **v2/alert** API.                                                                                               |
| <mark style="background-color:orange;">**Deprecation of End Timestamp in Config Search**</mark> | -              | -          | The end timestamp in the date selector for Config Search will soon be deprecated after which it will be ignored for all existing RQLs. You will only need to choose a start timestamp without having to specify the end timestamp. |


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.prismacloud.io/release-notes/look-ahead-planned-updates-on-prisma-cloud/look-ahead-secure-the-infrastructure.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
