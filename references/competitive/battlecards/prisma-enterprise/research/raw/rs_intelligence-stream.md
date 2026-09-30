> For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.prismacloud.io/content-collections/runtime-security/runtime-security-components/intelligence-stream.md).

# Intelligence Stream

The Prisma Cloud Intelligence Stream is a real-time feed that contains vulnerability data and threat intelligence from a variety of certified upstream sources. Prisma Cloud continuously pulls data from known vulnerability databases, official vendor feeds and commercial providers to provide the most accurate vulnerability detection results.

In addition to the information collected from official feeds, Prisma Cloud feeds are enriched with vulnerability data curated by a dedicated research team. Our security researchers monitor cloud and open source projects to identify security issues through automated and manual means. As a result, Prisma Cloud can detect new vulnerabilities that were only recently disclosed, and even vulnerabilities that were quietly patched.

The Prisma Cloud console automatically connects to the Intelligence Stream server and downloads updates without requiring any special configuration. The Intelligence Stream is updated several times per day, with consoles continuously checking for updates.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.prismacloud.io/content-collections/runtime-security/runtime-security-components/intelligence-stream.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
