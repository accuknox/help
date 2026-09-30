> For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.prismacloud.io/content-collections/data-security-posture-management/welcome/platform-overview/compliance.md).

# Compliance

The Compliance page in Prisma DSPM is designed to offer an at-a-glance view of your organization’s alignment with various compliance standards. The Compliance page enables you to monitor risks across supported cloud platforms and measure how well your security practices are performing against established compliance criteria.

The built-in standards cover a broad range of regulatory and industry requirements, enabling you to assess security across multiple dimensions.

For each compliance standard, the Compliance page provides the following information:

* **Standard Description**: A summary of the compliance standard’s purpose and scope.
* **Compliance Check Results**: A count of the unique resources monitored for compliance against the standard.
* **Assets at Risk**: The number of assets potentially at risk according to each compliance standard.
* **Risk Findings**: The total number of findings at risk, detected during compliance checks.

![](https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-2f301987f0f66fd296a4215ada1ff143ca2b8c6d%2Fmedia_1e0a660a5b03a744bd16ace2445b27b42c3618ac7.png?alt=media)

### How to Use the Compliance Page

The Compliance page in Prisma DSPM offers a user-friendly way to explore compliance details for each supported standard.

1. **Navigate to the Compliance Page**:
   * From the top menu, select **Compliance** to access the Compliance dashboard.

     ![](https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-bcd75f7acf5002d26c38c94446107bda86da35f6%2Fmedia_160137022260b48a58bf84792ff579263096b84f7.png?alt=media)
2. **Explore Supported Compliance Standards**:
   * Each standard, such as SOC 2, ISO 27001, or NIST 800-53, appears as a separate entry with a clear display of compliance statistics. This includes a progress bar showing the percentage of checks passed, the total checks performed, and specific metrics for assets at risk and risk findings.
3. **View Risk Findings**:
   * Click **View Risk Findings** next to a standard compliance to open the **Risks Findings** tab, and view detailed risk data. Identify specific assets that may not meet the standard and explore remediation steps. For further information, see the [Risks](https://docs.prismacloud.io/en/enterprise-edition/content-collections/data-security-posture-management/welcome/platform-overview/risks) article.
4. **Filter Standards**:
   * Use the **Search and Filter** field to narrow down the standards displayed. This helps in focusing on a particular compliance standard or filtering based on specific risk factors relevant to your organization.
5. **Analyze Compliance Status**:
   * Review the **Assets at Risk** and **Risk Findings** metrics for each standard. The **Assets at Risk** number represents resources potentially vulnerable under the standard, while **Risk Findings** indicate the total number of findings at risk, detected during compliance checks.
6. View a Breakdown of the Risks
   * Click on each standard to view a breakdown of all the risks associated with the standard.\
     ![](https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-582f5eecf95d1aa627630aca585f60841938834c%2Fmedia_190d44b9c257e8d65fa64584afe7f8f7387024534.png?alt=media)
   * View the amount of checks passed for each risk.
   * Click each risk to open the Risks Findings tab, and view detailed risk data. For further information, see the [Risks](https://docs.prismacloud.io/en/enterprise-edition/content-collections/data-security-posture-management/welcome/platform-overview/risks) article.\
     ![](https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-8dc7334b4e82d139b0f2b5a83c30c7776db6f27b%2Fmedia_1ce2aaee0208dc67350564573092fcde072c47658.png?alt=media)


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.prismacloud.io/content-collections/data-security-posture-management/welcome/platform-overview/compliance.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
