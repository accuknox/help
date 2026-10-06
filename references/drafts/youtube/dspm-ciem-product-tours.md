---
title: YouTube Publish Sheet for the DSPM and CIEM Product Tours
videos:
  - references/video-edits/dspm-tour/output/accuknox-dspm-tour.mp4
  - references/video-edits/ciem-tour/output/accuknox-ciem-tour.mp4
sources:
  - docs/getting-started/dspm-overview.md
  - docs/getting-started/dspm-onboarding.md
  - docs/getting-started/ciem-overview.md
  - docs/getting-started/ciem-onboarding.md
  - references/video-edits/*/output/timeline.json
posted: false
---

# YouTube Publish Sheet for the DSPM and CIEM Product Tours

Chapter times come from each render's `timeline.json`. Every chapter runs 12 seconds or more.

## Upload Settings Are the Same for Both Videos

| Setting | Value |
|---|---|
| Channel | `accuknox` |
| Category | Science & Technology |
| Audience | No, not made for kids |
| Language | English, for the video and the captions |
| Captions | Upload the `output/narration.srt` file beside each MP4 |
| Playlist | AccuKnox Product Tours |
| Visibility | Unlisted first. Switch to Public after Q1 to Q3 below are answered |

## The DSPM Video Leads With Card Data and Leaked Keys

**File:** `references/video-edits/dspm-tour/output/accuknox-dspm-tour.mp4`, 1:52

**Title**

```text
Find Sensitive Data in Your Cloud With AccuKnox DSPM
```

Alternates for the YouTube Studio title test:

- `Find Card Data and Leaked Keys in Your S3 Buckets`
- `Data Security Posture Management in 2 Minutes`

**Thumbnail text:** "Card data in your S3?" over the evidence tab, with the Credit Card and Aadhar Card chips in view.

**Description**

```text
AccuKnox DSPM finds card numbers, national IDs and cloud keys in your cloud data stores, with 283 data classes. A 2-minute tour.

Product page: https://accuknox.com/platform/dspm
How DSPM works: https://help.accuknox.com/getting-started/dspm-overview/
Setup guide: https://help.accuknox.com/getting-started/dspm-onboarding/

Data Security Posture Management (DSPM) shows where sensitive data sits in your buckets, databases and SaaS apps. This tour follows one finding in the demo data. Credit card data sits in five assets, and one S3 bucket holds 92.2k sensitive records under PCI DSS, SOC 2 and HIPAA.

What you will see:
- The risk dashboard: data alerts by severity, findings trends, and the accounts with the most sensitive records
- Sensitive data findings ranked by country
- A credit card finding with its evidence files and compliance frameworks
- An AWS access key stored in plain text, flagged as critical
- Amazon S3 setup: pick buckets by tag or name, scan every public bucket, and let AccuKnox AI review results for false positives

The scanner runs in your own cloud account, in the region that holds the data, with read-only access. It classifies data in memory, and only a findings file goes to the AccuKnox console.

Chapters:
0:00 Why sensitive data hides in cloud storage
0:13 Data risk dashboard and findings by country
0:32 Credit card data finding and compliance frameworks
0:51 Evidence files and asset details
1:06 AWS access key found in plain text
1:18 Set up DSPM for Amazon S3

Screens come from a preview build of the AccuKnox console.
```

**Tags**

```text
DSPM, data security posture management, AccuKnox, AccuKnox DSPM, sensitive data discovery, data classification, PII detection, PCI DSS, HIPAA, GDPR, AWS S3 security, S3 bucket scanning, secrets detection, cloud data security, data security, cloud security
```

## The CIEM Video Leads With Who Holds Cloud Access

**File:** `references/video-edits/ciem-tour/output/accuknox-ciem-tour.mp4`, 1:46

**Title**

```text
See Who Can Access Your Cloud With AccuKnox CIEM
```

Alternates for the YouTube Studio title test:

- `Find Risky Cloud Identities in AWS, Azure, GCP and Oracle`
- `Map Every Cloud User, Role and Policy in One View`

**Thumbnail text:** "Who can touch your cloud?" over the access graph, with the user, its groups and its policies in view.

**Description**

```text
AccuKnox CIEM lists every user, group and role across AWS, GCP, Azure and Oracle, and shows the access each one holds. A 2-minute tour.

How CIEM works: https://help.accuknox.com/getting-started/ciem-overview/
Setup guide: https://help.accuknox.com/getting-started/ciem-onboarding/
AccuKnox: https://accuknox.com

Cloud Infrastructure Entitlement Management (CIEM) reads the users, groups, roles and policies in your cloud accounts. The organization graph in this tour shows one AWS account with 77 users, 22 groups, 637 roles and 504 policies.

What you will see:
- The identity list, with risk classes such as privilege escalation, data exfiltration and credentials exposure
- Each identity marked human or machine, with the days since it was last used
- An identity's attached policies, with the JSON policy document
- The access graph, from an identity through its groups to the policies they grant
- Setup for a standalone AWS account with a Terraform script

CIEM releases soon in a newer version of AccuKnox. The screens come from the current build and can change before release.

Chapters:
0:00 Why cloud access gets out of hand
0:13 Every identity, its risk class and its last use
0:38 Identity details, policies and the access graph
1:00 Organization graph of a whole AWS account
1:12 Turn on CIEM for a cloud account
```

**Tags**

```text
CIEM, cloud infrastructure entitlement management, AccuKnox, AccuKnox CIEM, cloud identity security, IAM, AWS IAM, least privilege, cloud entitlements, identity risk, privilege escalation, multi-cloud security, Azure, GCP, Oracle Cloud, cloud security, CNAPP
```

## Answer Three Questions Before You Set Either Video to Public

- **Q1.** Are the DSPM preview screens ready to show? The DSPM description says they come from a preview build.
- **Q2.** Does the DSPM console setup match the scanner that runs in your account? The description states both.
- **Q3.** Is CIEM still unreleased? If it has shipped, delete the "releases soon" paragraph from the CIEM description.
