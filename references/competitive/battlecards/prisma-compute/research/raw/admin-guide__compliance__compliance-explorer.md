For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/compliance/compliance-explorer.md).

Compliance Explorer is a reporting tool for compliance rate. Metrics present the compliance rate for resources in your environment on a per-check, per-rule, and per-regulation basis. Report data can be exported to CSV files for further investigation.

The key pivot for Compliance Explorer is failed compliance checks. Compliance Explorer tracks each failed check, and the resources impacted by each failed check. From there, you can further slice and dice the data by secondary facets, such as collection, benchmark, and issue severity.

Compliance Explorer helps you answer these types of questions:

- What is the compliance rate for the entire estate?

- What is the compliance rate for some segment of the estate?

- What is the compliance rate relative to the checks that you consider important?









  - Segment by benchmark.

  - Segment by specific compliance policy rules. Prisma Cloud supports compliance policies for containers, images, hosts, and serverless functions.


- Which resources (containers, images, hosts, serverless functions) are failing the compliance checks you care about?


To view Compliance Explorer, go to **Monitor > Compliance > Compliance Explorer**.

## Page organization[Direct link to heading](https://docs.prismacloud.io/admin-guide/compliance/compliance-explorer\#page-organization)

The Compliance Explorer view is organized into three main areas:

![compliance explorer overview](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-14403ed484bf8d6006938f69a00d4338ec06cce1%252Fcompliance_explorer_overview.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=5efac0db21b7714cc20d9ae67543ed1e&sv=3)

**1\. Collection filter.** Collections group related resources together. Use them to filter the data in Compliance Explorer. For example, you might want to see how all the entities in the sock-shop namespace in your production cluster comply to the checks in the PCI DSS template.

**2\. Roll-up charts.** Configurable charts that summarize compliance data for the perspectives you care about. They report the following data:

- Total compliance rate for your entire estate.

- Compliance rate by regulation. Click **Select regulations** to configure which benchmarks and templates are shown on the page. Benchmarks are industry-standard checklists, such as the CIS Docker Benchmark. Templates are Prisma Cloud-curated checklists Checks are selected from the universe of checks provided in the product that pertain to directives in a regulatory regime, such as the Payment Card Industry Data Security Standard (PCI DSS).

- Compliance rate by rule. Provides another mechanism to surface specific segments of your environment when scrutinizing compliance. Click **Add rule** to configure the card.

- Historical trend chart for compliance rate. Shows how the compliance rate has changed over time.


The lists in the regulation and rule cards are sorted by compliance rate (the lowest compliance rate first).

**3\. Results table.** Shows a detailed view of all compliance checks and their associated compliance rates. These checks are displayed relative to the following factors:

- **Policies**: Compliance checks that are enabled according to your configured policies.

- **Collection**: The specific collection if selected on **Filter by collection** at the top of the page.

- **Filters**: Any applied filters, such as displaying only critical severity issues.


Each compliance check is identified by a unique ID and can be either enabled or disabled. The **Compliance rate** column indicates the percentage of resources passed or failed the corresponding compliance check, along with the **Benchmark ID**. The table includes the following columns:

- **ID**: Unique identifier for the compliance check.

- **Benchmark ID**: The ID associated with the benchmark or standard against which the compliance check is evaluated.

- **Description**: A brief explanation of the compliance check.

- **Severity**: The level of severity associated with the check, such as Critical, High, Medium, or Low.

- **Category**: The category or type of compliance check, such as Security, Configuration, or Identity.

- **Type**: Specifies whether the check is associated with a specific policy, rule, or standard.

- **Compliance Rate**: The percentage of resources that passed the compliance check.

- **Failed Resources**: The number of resources that did not pass the compliance check.

- **Total Resources**: The total number of resources evaluated in the check.


**Tabs and Views**

- **Tabs**: The tabs organize results by Benchmark or Template. The visibility of these tabs depends on how you configure the corresponding **Compliance Rate for Regulations Roll-Up card**.

- **Rules View**: If you switch to the **Rules** view, the tabs will display the rules selected in the **Compliance Rate for Policy Rules Roll-Up card**.


![compliance explorer tabs](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-2049bd09e99baafbe86919a975b9903e338b8178%252Fcompliance-explorer-tabs.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=2fb8c3ec1b0a4331d8e669707cf62eda&sv=3)

**Sorting and Filtering**

- **Sorting**: By default, the table is sorted by Severity (primary sort key) and then by Compliance Rate (secondary sort key). If no parameters are specified, Compliance Explorer shows all IDs by default. Use the **Category:Prisma Cloud Labs** filter in the table to show the [malware scanning](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/compute-edition/34/admin-guide/operations/malware.md) results obtained using Advanced WildFire after an [agentless scan](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/compute-edition/34/agentless-scanning/agentless-scanning.md).

- **Filtering**: You can filter the table to display only failed checks by setting the **Status** to **Failed**.


![compliance explorer filter](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-b31af2bb8c3a18f01eaba5cc9235e0b9e40458e1%252Fcompliance-explorer-filter.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=74b61eb46921752049f265689a4c6e23&sv=3)

**Exporting Data**

You can export the data to a CSV file for further analysis. The exported data reflects any applied filters and collections, allowing you to narrow down and customize the data before exporting.

![compliance explorer csv](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-6ffdfcde5af6dafa0964d671ad23e1cb89d18701%252Fcompliance-explorer-csv.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=24d16c26782002961b7d7d45a7d00a85&sv=3)

## Statistics[Direct link to heading](https://docs.prismacloud.io/admin-guide/compliance/compliance-explorer\#statistics)

The data in Compliance Explorer is calculated every time the page is loaded, and it’s based on data from the latest scan. Data in the trend graph is based on snapshots taken every 24 hours.

You can force Console to recalculate statistics from the latest scan data by clicking the **Refresh** button. The **Refresh** button displays a red indicator when there’s a change in the following resources in your environment:

- Containers.

- Images.

- Hosts.

- Serverless functions.


For example, the refresh indicator is shown when new containers are detected. It’s also shown when containers are deleted.

No red refresh indicator is shown if you simply change the compliance policy. If you change the compliance policy, manually force Prisma Cloud to rescan your environment (or wait for the next periodic scan), and then refresh the Compliance Explorer.

[PreviousCompliance](https://docs.prismacloud.io/admin-guide/compliance/compliance) [NextManage compliance](https://docs.prismacloud.io/admin-guide/compliance/manage-compliance)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
