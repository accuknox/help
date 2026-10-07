---
title: "How to Find Sensitive Data in Your Cloud With AccuKnox DSPM"
seo_title: "Find Sensitive Data in Your Cloud With AccuKnox DSPM"
meta_description: "Find sensitive data in your cloud with AccuKnox DSPM. Follow a credit card finding from the risk dashboard to its evidence files, then set up an S3 scan."
slug: "dspm-find-sensitive-data-in-your-cloud"
url: "https://accuknox.com/blog/dspm-find-sensitive-data-in-your-cloud"
date: 2026-10-07
primary_keyword: "find sensitive data in your cloud"
secondary_keywords: ["AccuKnox DSPM", "data security posture management", "sensitive data discovery", "S3 bucket scanning"]
excerpt: "A step-by-step tour of AccuKnox DSPM, from the risk dashboard to a credit card finding, an exposed AWS key and Amazon S3 setup."
category: "DSPM"
author: "Atharva Shah"
reading_time: "5 minutes"
word_count_target: 1000
audience: "security engineer | cloud engineer"
cover_image_prompt_claude: >
  Not used. The cover is the YouTube thumbnail for video 8foYZBdQtDQ.
cover_image_prompt_midjourney: >
  Not used. The cover is the YouTube thumbnail for video 8foYZBdQtDQ.
---

# How to Find Sensitive Data in Your Cloud With AccuKnox DSPM

![Cover image from the AccuKnox DSPM product tour video, titled Find Sensitive Data in Your Cloud With AccuKnox DSPM](https://img.youtube.com/vi/8foYZBdQtDQ/maxresdefault.jpg)

*Caption: The thumbnail of the two-minute AccuKnox DSPM product tour.*

## TL;DR

- You can find sensitive data in your cloud with [AccuKnox Data Security Posture Management (DSPM)](https://accuknox.com/platform/dspm), which ranks findings by severity and by country.
- The scanner detects 283 data classes, including card numbers, national IDs and cloud keys.
- In the demo data, credit card data sits in five assets, and one S3 bucket holds 92.2k sensitive records under PCI DSS, SOC 2 and HIPAA.
- The scanner runs in your own cloud account with read-only access, and only a findings file goes to the AccuKnox console.
- Setup for Amazon S3 is one data source on a connected AWS account.
- DSPM shows where regulated data sits. It does not assess the controls around that data.

## Start at the Risk Dashboard to See Where Sensitive Data Sits

The risk dashboard counts every data alert by severity and tracks how findings change over time. It also names the assets and cloud accounts that hold the most sensitive records. A second view maps findings to the country that holds the data and ranks the countries from most to fewest.

![The DSPM risk dashboard with data alerts by severity, findings trends, top assets and accounts with sensitive records](https://media.zernio.com/temp/1791272878799_rud6y0x3_d01-dashboard.jpg)

*Caption: The risk dashboard shows data alerts by severity, how findings change over time, and the assets and accounts with the most sensitive records.*

![The DSPM sensitive data by region view, with a world map and a ranked country table](https://media.zernio.com/temp/1791272880981_k15vu0g5_d02-country.jpg)

*Caption: Findings map to the country that holds the data, ranked from most to fewest.*

> **Note.** The DSPM screens in this post come from a preview build of the AccuKnox console. The numbers are demo data.

## Open a Credit Card Finding to See Its Asset and Frameworks

The scanner groups findings by what it found. In the demo data, credit card data sits in five assets, and each asset has its own count of sensitive records. To follow one, open the finding **PCI_Credit Card data detected** in the findings list.

![The DSPM findings list with the Card data, 5 assets group and a records per asset column](https://media.zernio.com/temp/1791272882812_g62wwa46_d03-findings.jpg)

*Caption: The findings list groups results by what the scanner found. Here, credit card data sits in five assets, each with its own record count.*

The Overview tab names the impacted asset, its sensitive record count and the compliance frameworks the finding falls under. Here the asset is the S3 bucket `customer_salesrecords` in an AWS account called sandbox. It holds 92.2k sensitive records. The frameworks include PCI DSS, SOC 2 and HIPAA, with three more behind the +3 chip.

![The Overview tab of the PCI_Credit Card data detected finding, showing the customer_salesrecords asset, 92.2k sensitive records and the compliance frameworks PCI DSS, SOC 2 and HIPAA](https://media.zernio.com/temp/1791272884941_qab40i9p_d04-finding-overview.jpg)

*Caption: One finding shows its asset, 92.2k sensitive records and its compliance frameworks in a single view.*

The framework chips come from the data classes. The scanner maps 282 of its 283 data classes to the regulation clauses they fall under, as the [DSPM overview](https://help.accuknox.com/getting-started/dspm-overview/) lists.

## Check the Evidence Tab and the Asset Before You Triage

The Evidences tab lists every file behind the finding, with its file type, its path and the sensitive data types found in each one. In the demo, each file row carries chips such as Aadhar Card, Credit Card and Bank Account Number, with a count for each type.

![The Evidences tab of the credit card finding, listing each file with its type, path and sensitive data chips such as Aadhar Card and Credit Card](https://media.zernio.com/temp/1791272886652_ay3sotbi_d05-evidence.jpg)

*Caption: The evidence tab ties the finding to named files and the data types inside each one.*

Next, open the asset. The asset page shows sensitive records by data type, plus security settings such as encryption and public access.

![The asset page for customer_salesrecords with 230 total risks, 92.2k sensitive records by data type, and a security configuration block](https://media.zernio.com/temp/1791272888320_bh9n3e9y_d06-asset.jpg)

*Caption: The asset page lists sensitive records by data type and shows its encryption and public access settings.*

## The Same Scan Flags an AWS Access Key Stored in Plain Text

Secrets show up in the same scan. In the tour, an AWS access key stored in plain text is flagged as Critical. The finding shows the file location, and you can raise a ticket from the same panel with **Create Ticket**.

![The AWS access key ID in plain text finding, marked Critical, with a 10-day SLA, a Create Ticket button and an Ask AI button](https://media.zernio.com/temp/1791272889943_lj0p94j4_d07-aws-key.jpg)

*Caption: A Critical secret finding carries its remediation window, its status and a ticket button.*

The Critical severity sets a 10-day SLA, which is the remediation window. The finding keeps the status Active until you fix the data. If you confirm a value as public or test data, turn on **Ignored**. Then add that value to the scanner's allow list, so the next nightly run does not report it again. The **Solution** tab holds the remediation steps.

![The Location field of the AWS access key finding, which names the bucket and object key that hold the secret](https://media.zernio.com/temp/1791272891986_66mp429t_d08-key-location.jpg)

*Caption: The Location field names where the key sits, so you know which file to fix.*

## Set up Amazon S3 With One Data Source

The tour ends with setup. You turn on the data security scan for a connected cloud account and add a data source.

1. Open the connected AWS cloud account for editing.
2. Under **Scan Type**, select **Data Security**.
3. Select **Add Source**, then choose **AWS S3**.
4. In **Include S3 Buckets**, pick buckets by tag or by name. Enter one pattern per row, such as `env=prod` or `*customer`.
5. Select **Scan Publicly Exposed buckets** to include every publicly exposed bucket. The console states these buckets are scanned even when they do not match your name or tag patterns.
6. Select **Allow Accuknox AI to scan results to reduce false postives**, so AccuKnox AI reviews the results for false positives. The console prints that label with the typo.
7. Select **Submit**, then select **Save** on the cloud account page.

![The Configure Data Security panel for AWS S3, with bucket selection by tag and by name, the public bucket scan option and the AccuKnox AI false-positive option](https://media.zernio.com/temp/1791272893542_isb77cm1_d09-s3-config.jpg)

*Caption: The S3 source form scopes the scan by tag, by name, by public exposure and by AI review.*

The scanner runs in your own account, in the region that holds the data, with read-only access. It reads a sample, classifies it in memory and sends only a findings file to the AccuKnox console. Per the [onboarding guide](https://help.accuknox.com/getting-started/dspm-onboarding/), the asset and its findings appear in the console within minutes of the first run.

> **Limitation.** The scanner does not support Google Cloud Storage, SMB or NFS file shares, Oracle Database, or data warehouses such as Snowflake. The [DSPM overview](https://help.accuknox.com/getting-started/dspm-overview/) lists the supported stores.

## Watch the DSPM Tour From Dashboard to S3 Setup

```html
<iframe width="560" height="315" src="https://www.youtube.com/embed/8foYZBdQtDQ" title="Find Sensitive Data in Your Cloud With AccuKnox DSPM" frameborder="0" allowfullscreen></iframe>
```

Watch it on YouTube: [Find Sensitive Data in Your Cloud With AccuKnox DSPM](https://www.youtube.com/watch?v=8foYZBdQtDQ).

## FAQs

### Does AccuKnox DSPM copy my data out of my cloud account?

The scanner does not keep your data. It discards every row and file after classification. The findings file holds each matched value cut at 200 characters, and the console shows that value masked to its last four characters.

### Which data stores can DSPM scan?

DSPM scans object storage such as Amazon S3, Azure Blob Storage and ADLS Gen2, plus relational and document databases, Google Workspace Drive and Salesforce. The [DSPM overview](https://help.accuknox.com/getting-started/dspm-overview/) has the full table and the stores it does not support.

### Can I run DSPM so that nothing leaves my network?

You can. AccuKnox can run the scanner, the findings and the console together on-premises or air-gapped. With the on-premises console, nothing leaves your boundary.
