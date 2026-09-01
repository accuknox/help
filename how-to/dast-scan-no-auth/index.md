---
title: DAST Unauthenticated Scan
description: Configure an unauthenticated (No Auth) DAST scan in AccuKnox to test publicly accessible pages without supplying login credentials.
---

# DAST Unauthenticated Scan

AccuKnox Dynamic Application Security Testing (DAST) supports **unauthenticated scans**, which crawl and test publicly accessible pages without requiring login credentials. This is the simplest way to get started with DAST and is ideal for scanning APIs, marketing sites, or any endpoint that does not sit behind a login wall.

!!! tip "Authenticated scans"
    If your application requires login credentials to reach protected content, see [DAST Authenticated Scan](dast-authenticated-scans.md).

---

## Configuration Steps

**Step 1:** Log in to the AccuKnox Platform.

**Step 2:** Navigate to **Settings** > **Collectors**.

![Navigate to Settings > Collectors](./images/dast-auth/image14.png)

**Step 3:** Click **Add Collector**.

![Add Collector](./images/dast-auth/image15.png)

**Step 4:** Click **Web Application DAST Scan**.

![Web Application DAST Scan](./images/dast-auth/image10.png)

**Step 5:** Add the collector name and proceed to configure the following fields:

### Target URL

**Enter Target URL** — Primary target URL to scan.

### Scan Type

**Scan Type** — Select **Baseline** (quick scan) or **Full** (detailed scan).

See the difference between scan modes here: [Baseline vs Full Scan](https://help.accuknox.com/how-to/dast-baseline-vs-full/)

### Authentication

**Authentication** — Select **No Auth**.

No login page, credentials, or session indicators are required. All authentication-related fields are skipped.

### Include Path

**Include Path** *(Optional)* — Defines the specific URLs or URL patterns to include in the scan scope.

Example: `https://example.com/app/`

![Include Path](./images/dast-auth/image2.png)

### Exclude Path

**Exclude Path** *(Optional)* — URLs or URL patterns that should be excluded from the scan to avoid scanning specific pages or actions.

Example: `https://example.com/scoreboard/`

![Exclude Path](./images/dast-auth/image8.png)

### Label & Tags

**Label** — Create one using these steps: [Create Labels](https://help.accuknox.com/how-to/how-to-create-labels/)

**Tags** *(Optional)* — Add any relevant tags.

---

**Step 6:** Enter your email address where you would like to receive scan notifications and press **Enter**.

![Email Notification](./images/dast-auth/image12.png)

**Step 7:** After submitting, the scan will be triggered. You can check the scan results on the same page.

![Scan Results](./images/dast-auth/image3.png)

**Step 8:** Once the **Findings** column is populated, click on it to be redirected to the findings page with all necessary details.

![Findings Page](./images/dast-auth/image5.png)
