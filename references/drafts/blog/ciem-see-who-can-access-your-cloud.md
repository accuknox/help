---
title: "How to See Who Can Access Your Cloud With AccuKnox CIEM"
seo_title: "See Who Can Access Your Cloud With AccuKnox CIEM"
meta_description: "AccuKnox CIEM lists every user, group and role in your cloud accounts with risk classes and last use. Follow the tour from identity list to onboarding."
slug: "ciem-see-who-can-access-your-cloud"
url: "https://accuknox.com/blog/ciem-see-who-can-access-your-cloud"
date: "2026-10-08"
primary_keyword: "ciem"
secondary_keywords: ["cloud infrastructure entitlement management", "cloud identity access graph", "aws iam risk classes", "cloud entitlements"]
excerpt: "AccuKnox CIEM lists every user, group and role in your cloud accounts, shows the policies each one holds, and draws the access chain as a graph."
category: "CIEM"
author: "Atharva Shah"
reading_time: "5 minutes"
word_count_target: 1000
audience: "security engineer | cloud engineer"
cover_image_prompt_claude: >
  Not used. The cover is the YouTube thumbnail of the CIEM product tour,
  https://img.youtube.com/vi/5RnjnIauJow/maxresdefault.jpg
cover_image_prompt_midjourney: >
  Not used. The cover is the YouTube thumbnail of the CIEM product tour --ar 16:9
---

# How to See Who Can Access Your Cloud With AccuKnox CIEM

![Thumbnail of the AccuKnox CIEM product tour video, See Who Can Access Your Cloud With AccuKnox CIEM](https://img.youtube.com/vi/5RnjnIauJow/maxresdefault.jpg)

*Caption: The two-minute product tour, from the identity list to onboarding.*

## TL;DR

- AccuKnox CIEM lists every user, group and role in your AWS, GCP, Azure and Oracle cloud accounts in one table.
- The demo AWS account in the product tour holds 77 users, 22 groups, 637 roles and 504 policies.
- Each identity shows its risk classes, a human or machine tag and the days since its last use.
- The access graph traces an identity through its groups to the policies those groups grant.
- The entitlement toggle is on by default in step 2 of 3 of onboarding, and it supports standalone cloud accounts only.
- The feature releases soon in a newer version of AccuKnox, and the screens come from the current build.

## One List Shows Every Identity and the Access It Holds

Open **Identities > CIEM** in the left navigation. The list view opens by default and holds every user, group and role in your connected cloud accounts. The demo AWS account in the tour holds 637 roles, so the first question is who can actually use them.

> **Note.** CIEM releases soon in a newer version of AccuKnox. The screens in this post come from the current build and can change before the release. All counts in this post are demo data from the tour.

Each identity carries the risk classes that its attached policies create. Examples are privilege escalation, data exfiltration and credentials exposure. A chip marked **+1** or **+2** hides more classes, and you open the chip to see them all. Every identity also carries a human or machine tag, and a CI/CD pipeline account counts as a machine.

![The CIEM identity list for a demo AWS account, with the risk class column highlighted](https://media.zernio.com/temp/1791272855138_s5kykjdl_c01-identity-list.jpg)

*Caption: The identity list for a demo AWS account, with a risk class chip on every row.*

![The CIEM identity list with the human or machine classification column highlighted](https://media.zernio.com/temp/1791272856891_gf8t3f22_c02-human-machine.jpg)

*Caption: The classification column tags every identity as human or machine.*

Scroll the table to the right for the lifecycle columns. Filter the list by name, cloud provider, identity type or date range.

![The CIEM identity list scrolled right, with the Created By, Last Used and Days Since Last Used columns highlighted](https://media.zernio.com/temp/1791272858780_du0fz0wf_c03-lifecycle.jpg)

*Caption: The lifecycle columns show who created each identity, when it was last used and how many days ago.*

| Column | What it shows | Question it answers |
| --- | --- | --- |
| Created By | The user or account that created the identity | Who made this identity? |
| Last Used | The last time the identity was active | When was it last active? |
| Days Since Last Used | The days since the last use, where 0 days means used today | How long has it sat idle? |
| Age In Days | The days since the identity was created | How old is it? |

## Open an Identity to Read Its Findings and Its Policies

Select an identity in the list. A panel opens with 4 tabs: **Overview**, **Access Graph**, **Related Identities** and **Raw Information**. The **Overview** tab holds the identity details and **Total Findings**, which counts the findings on that identity by severity: Critical, High, Medium and Low.

![The identity details panel with the Overview tab, identity details, findings by severity and the attached policy](https://media.zernio.com/temp/1791272860606_y7jnefy5_c04-identity-details.jpg)

*Caption: The Overview tab shows the identity details, its findings by severity and the policies attached to it.*

Below the counts, **Policy Attached** lists every policy with its name, type, resource ID and creation time. Expand a policy row to read the policy document as JSON. You read the exact statements instead of guessing from the policy name.

![An expanded attached policy in the CIEM identity panel, with its JSON policy document](https://media.zernio.com/temp/1791272862629_pww89ld1_c05-policy-doc.jpg)

*Caption: Expanding a policy row shows its JSON policy document.*

A policy has one of three types.

- **Cloud managed.** The cloud provider maintains the policy.
- **Inline policy.** The policy is embedded in one identity, and the console shows it as `inline_policy`.
- **User managed.** Your team created the policy.

## The Access Graph Shows Which Group Grants Which Policy

Open the **Access Graph** tab. The graph reads from top to bottom. The identity sits at the top, its groups sit in the middle, and the policies each group grants sit at the bottom. A policy attached straight to the identity sits in the same row as the groups.

The graph shows which permissions reach the identity and through which group. Controls at the lower left zoom, fit, reset and expand the graph.

![The CIEM access graph of one demo AWS user, with the identity at the top, its groups in the middle and the policies granted at the bottom](https://media.zernio.com/temp/1791272864624_5muzm5uq_c06-access-graph.jpg)

*Caption: The access graph of one demo AWS user. The identity sits at the top, its groups in the middle and the policies those groups grant at the bottom.*

**Related Identities** lists the other identities in the same cloud account. **Raw Information** shows the full identity record as JSON.

## The Organization Graph Shows a Whole Account at Once

Select the graph icon at the top right of **Identities > CIEM**, then filter by **Cloud Providers** and **Cloud Account Name**. The cloud account node sits at the top, with one node each for users, groups, roles and policies. A badge on each node shows the count.

The demo AWS account in the tour shows 77 users, 22 groups, 637 roles and 504 policies. Select a node to expand its members, and select a member to open that identity's access graph.

![The CIEM organization graph of the demo AWS account with badges for 77 users, 22 groups, 637 roles and 504 policies](https://media.zernio.com/temp/1791272868055_dr3naqcy_c07-org-graph.jpg)

*Caption: The organization graph of the demo AWS account, with count badges for 77 users, 22 groups, 637 roles and 504 policies.*

## Turn on CIEM While You Onboard a Standalone Account

Onboarding a standalone AWS, GCP, Azure or Oracle Cloud Infrastructure (OCI) account turns the feature on. Before you start, finish the cloud-side setup in the [AWS onboarding guide](https://help.accuknox.com/how-to/aws-onboarding/) or the guide for your cloud, and install Terraform on your workstation.

1. Go to **Settings > Cloud Accounts** and select **Onboard Account**.
2. In **Step 1 of 3**, choose your cloud provider and **Standalone Account**, then select **Next**.
3. In **Step 2 of 3, Configure Scanning**, keep the **Cloud infrastructure entitlement management (CIEM)** toggle on. It is on by default.
4. In **Step 3 of 3, Account Setup**, on AWS, install Terraform from the **Install Terraform Guidelines** link.
5. Download the Terraform script and save it as a file, for example `accuknox_aws_onboard.tf`.
6. In the folder that holds the file, run the command below.

```bash
terraform init && terraform plan && terraform apply
```

7. Open the `credentials.txt` file that Terraform creates, and paste the access key into **Access Key ID** and the secret key into **Secret Access Key**.
8. Select the **Region**, then select **Verify & Connect**.

![Step 2 of 3, Configure Scanning, in AWS onboarding, with the CIEM toggle on by default](https://media.zernio.com/temp/1791272870923_btsnl2xq_c08-onboard-toggle.jpg)

*Caption: Step 2 of 3 in onboarding, with the CIEM toggle on by default.*

![Step 3 of 3, Account Setup, with the Terraform command and the access key and secret key fields](https://media.zernio.com/temp/1791272872696_enbequxq_c09-terraform.jpg)

*Caption: Step 3 of 3 gives you the Terraform command, then asks for the keys from the credentials.txt file.*

To onboard an account without CIEM, turn the toggle off in step 2 of 3. For GCP, Azure and OCI, follow the **Account Setup** in the console and the onboarding guide for your cloud.

To check the result, go to **Settings > Cloud Accounts**. The **CIEM** column shows **Active** for the new account, and in the tour it shows active on AWS, Oracle, GCP and Azure accounts. Then open **Identities > CIEM** and pick your cloud in the **Cloud Providers** filter. The [CIEM onboarding guide](https://help.accuknox.com/getting-started/ciem-onboarding/) has the full steps.

![The Cloud Accounts list with the CIEM column showing Active for AWS, Oracle, GCP and Azure accounts](https://media.zernio.com/temp/1791272876085_6ecqtjqv_c10-cloud-accounts.jpg)

*Caption: The Cloud Accounts list shows CIEM as Active for AWS, Oracle, GCP and Azure accounts.*

## CIEM Is Unreleased and Covers Standalone Accounts Only

> **Limitation.** Only standalone cloud accounts work today. Organization accounts are not supported yet.

CIEM is not generally available yet, and the screens can change before the release.

For what each screen shows, read the [CIEM overview](https://help.accuknox.com/getting-started/ciem-overview/). AccuKnox also covers posture on the same accounts through [Cloud Security Posture Management](https://accuknox.com/platform/cspm).

## Watch the CIEM Tour From Identity List to Onboarding

The tour takes about 2 minutes and follows the same order as this post.

```html
<iframe width="560" height="315" src="https://www.youtube.com/embed/5RnjnIauJow" title="See Who Can Access Your Cloud With AccuKnox CIEM" frameborder="0" allowfullscreen></iframe>
```

Watch it on YouTube: [See Who Can Access Your Cloud With AccuKnox CIEM](https://www.youtube.com/watch?v=5RnjnIauJow).

## FAQs

### Which clouds does AccuKnox CIEM cover?

It covers 4 clouds: AWS, GCP, Azure and Oracle Cloud Infrastructure. It lists 3 identity types: users, groups and roles. In the tour, the cloud accounts list shows entitlement management active on all four clouds.

### Does CIEM work with organization accounts?

No, organization accounts are not supported yet. Only standalone cloud accounts work today, so choose **Standalone Account** in step 1 of onboarding.

### Can I onboard a cloud account without CIEM?

You can. The CIEM toggle in **Step 2 of 3, Configure Scanning** is on by default. Turn it off to onboard the account without CIEM.
