> For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.prismacloud.io/content-collections/runtime-security/runtime-defense/incident-types/others.md).

# Others

* **Cloud Provider:** Indicates attempts to abuse a provider’s service to extract sensitive information.

  For example: Container `A` queried provider API at `<IP_ADDRESS>`.
* **Data Exfiltration:** Indicates a potential compromise on a container because of a modified binary listening on a port. This typically leads with a DNS suspicious activity.

  For example: Container process `/bin/bash` is listening on unexpected port `50000`.
* **Hijacked Process:** Indicates that an allowed process was used in a way that is inconsistent with its expected behavior. This can be a sign that a process has been used to compromise a container.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.prismacloud.io/content-collections/runtime-security/runtime-defense/incident-types/others.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
