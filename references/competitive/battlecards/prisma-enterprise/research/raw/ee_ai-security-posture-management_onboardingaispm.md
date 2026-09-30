> For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.prismacloud.io/content-collections/ai-security-posture-management/onboardingaispm.md).

# Onboarding AI-SPM

#### **Prerequisite to Onboarding AI-SPM**

[Onboarding DSPM](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/en/enterprise-edition/content-collections/data-security-posture-management/prisma-cloud-dspm-deployment/prisma-cloud-dspm-deployment/README.md) is a prerequisite to onboarding AI-SPM. This is because understanding and managing data exposure is fundamental to ensuring AI protection. By deploying DSPM first, you gain visibility into your data security posture, which is essential for the effective deployment and functioning of AI-SPM.

#### **Integrated Security Approach**

By integrating DSPM and AI-SPM, Prisma Cloud offers a unified approach to security. This integration helps in identifying potential threats and vulnerabilities across both data and AI systems, enabling a more robust and holistic security posture.

To ensure a smooth onboarding process, please refer to the detailed steps for onboarding DSPM.

When you onboard DSPM, AI-SPM is also automatically onboarded and starts running by default.

If you want to disable AI-SPM, disable scanning for your AI services in the ‘[Scanning Settings](https://docs.prismacloud.io/en/enterprise-edition/content-collections/data-security-posture-management/how-to-articles/configure-the-scanning-settings-for-supported-services)’ section of the projects page.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.prismacloud.io/content-collections/ai-security-posture-management/onboardingaispm.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
