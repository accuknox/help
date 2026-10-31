> For the complete documentation index, see [llms.txt](https://cortex-docs.paloaltonetworks.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://cortex-docs.paloaltonetworks.com/cortex-cloud-runtime-security/onboard-and-configure/deployment-steps-and-checklist/activate-cortex-cloud/cortex-cloud-supported-regions.md).

# Cortex Cloud supported regions

Explore Cortex Cloud hosting regions and data residency locations across the Americas, EMEA, and Asia-Pacific.

The following table lists the regions available to host Cortex Cloud and any associated Cortex services:

#### Americas

| Country            | Description                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| US (United States) | All Cortex Cloud logs and ingested data remain hosted within the boundaries of the United States.                                                                                                                                                                                                                                                                                                                                 |
| Brazil (BR)        | All Cortex Cloud logs and ingested data remain hosted within the boundaries of Brazil.                                                                                                                                                                                                                                                                                                                                            |
| Canada (CA)        | <p>All Cortex Cloud logs and ingested data remain hosted within the boundaries of Canada. However, if you have a WildFire Canada cloud subscription, consider the following:</p><ul><li>You cannot send file submissions for bare-metal analysis.</li><li>You will not be protected against macOS-borne zero-day threats. However, you will receive protection against other macOS malware in regular WildFire updates.</li></ul> |

#### EMEA (Europe, the Middle East, Africa)

| Country             | Description                                                                                        |
| ------------------- | -------------------------------------------------------------------------------------------------- |
| Finland (FI)        | All Cortex Cloud logs and ingested data remain hosted within the boundaries of Finland.            |
| France (FA)         | All Cortex Cloud logs and ingested data remain hosted within the boundaries of France.             |
| Germany (DE)        | All Cortex Cloud logs and ingested data remain hosted within the boundaries of Germany.            |
| Israel (IL)         | All Cortex Cloud logs and ingested data remain hosted within the boundaries of Israel.             |
| Italy (IT)          | All Cortex Cloud logs and ingested data remain hosted within the boundaries of Italy.              |
| Netherlands         | All Cortex Cloud logs and ingested data remain hosted within the boundaries of Netherlands.        |
| Poland (PL)         | All Cortex Cloud logs and ingested data remain hosted within the boundaries of Poland.             |
| Qatar (QT)          | All Cortex Cloud logs and ingested data remain hosted within the boundaries of Qatar.              |
| Saudi Arabia (SA)   | All Cortex Cloud logs and ingested data remain hosted within the boundaries of Saudi Arabia.       |
| South Africa (ZA)   | All Cortex Cloud logs and ingested data remain hosted within the boundaries of South Africa.       |
| Spain (ES)          | All Cortex Cloud logs and ingested data remain hosted within the boundaries of Spain.              |
| Switzerland (CH)    | All Cortex Cloud logs and ingested data remain hosted within the boundaries of Switzerland.        |
| UK (United Kingdom) | All Cortex Cloud logs and ingested data remain hosted within the boundaries of the United Kingdom. |

#### JAPAC (Asia-Pacific)

| Country          | Description                                                                                 |
| ---------------- | ------------------------------------------------------------------------------------------- |
| Australia (AU)   | All Cortex Cloud logs and ingested data remain hosted within the boundaries of Australia.   |
| Delhi (DL)       | All Cortex Cloud logs and ingested data remain hosted within the boundaries of Delhi.       |
| India (IN)       | All Cortex Cloud logs and ingested data remain hosted within the boundaries of India.       |
| Indonesia (ID)   | All Cortex Cloud logs and ingested data remain hosted within the boundaries of Indonesia.   |
| Japan (JP)       | All Cortex Cloud logs and ingested data remain hosted within the boundaries of Japan.       |
| Singapore (SG)   | All Cortex Cloud logs and ingested data remain hosted within the boundaries of Singapore.   |
| South Korea (KR) | All Cortex Cloud logs and ingested data remain hosted within the boundaries of South Korea. |
| Taiwan (TW)      | All Cortex Cloud logs and ingested data remain hosted within the boundaries of Taiwan.      |


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation by asking a question.

Perform an HTTP GET request on the following URL with the `ask` and `goal` query parameters:

```
GET https://cortex-docs.paloaltonetworks.com/cortex-cloud-runtime-security/onboard-and-configure/deployment-steps-and-checklist/activate-cortex-cloud/cortex-cloud-supported-regions.md?ask=<question>&goal=<user_goal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is what the user is ultimately trying to achieve, the reason they need the answer. Sharing it helps GitBook give you a better, more relevant answer. A goal is most helpful when it describes the outcome the user wants rather than restating the question. For example, with `ask=how do I create an API token`, a goal like `automate deployments from our CI pipeline` lets GitBook tailor the answer to that use case.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
