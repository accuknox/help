---
title: DAST Authenticated Scan
description: Configure authenticated scans in AccuKnox DAST to test protected content behind login pages using credentials, session indicators, and a fallback URL.
---

# DAST Authenticated Scan

AccuKnox Dynamic Application Security Testing (DAST) supports **authenticated scans**, enabling the crawler to access and test content behind login pages. The system visualises the session state with **Logged In**, **Logged Out**, and **Fallback** indicators — preventing false negatives where crawlers fail to reach protected content.

!!! tip "Unauthenticated scans"
    If you only need to scan publicly accessible pages without supplying credentials, see [DAST Unauthenticated Scan](dast-scan-no-auth.md).

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

### Authentication

**Authentication** — Select **Auth-based**.

### Login Page URL

**Login Page URL** — The URL of the application's login page where the user enters credentials.

Example: `https://ctflearn.com/`

![Login Page URL](./images/dast-auth/image11.png)

### Login Credentials

**Login Credentials** — Valid username and password used to authenticate the scan against the application.

Example: Username: `admin`, Password: `admin`

![Login Credentials](./images/dast-auth/image16.png)

### Include Path

**Include Path** *(Optional)* — Defines the specific URLs or URL patterns to include in the scan scope.

Example: `https://ctflearn.com/lab/`

![Include Path](./images/dast-auth/image2.png)

### Exclude Path

**Exclude Path** *(Optional)* — URLs or URL patterns that should be excluded from the scan to avoid scanning specific pages or actions.

Example: `https://ctflearn.com/1/scoreboard/0`

![Exclude Path](./images/dast-auth/image8.png)

### Logged In Indicator

**Logged In Indicator** — Keyword or phrase used to confirm a successful login during the scan.

Example: `Dashboard`, `Get Started`

![Logged In Indicator](./images/dast-auth/image4.png)

### Logged Out Indicator

**Logged Out Indicator** — Keyword or phrase indicating the user is logged out or the session has expired.

Example: `Login`, `Learn`

![Logged Out Indicator](./images/dast-auth/image1.png)

### Login Fallback URL

**Login Fallback URL** — Post-login page used to verify a successful login.

Example: `https://ctflearn.com/dashboard`

![Login Fallback URL](./images/dast-auth/image13.png)

### Label & Tags

**Label** — Create one using these steps: [Create Labels](https://help.accuknox.com/how-to/how-to-create-labels/)

**Tags** *(Optional)* — Add any relevant tags.

See the difference between Baseline and Full scan modes here: [Baseline vs Full Scan](https://help.accuknox.com/how-to/dast-scan-types/)

Here is an example of how it looks after you have added everything:

![Configuration Example](./images/dast-auth/image6.png)

![Configuration Example continued](./images/dast-auth/image7.png)

**Step 6:** Enter your email address where you would like to receive scan notifications and press **Enter**.

![Email Notification](./images/dast-auth/image12.png)

**Step 7:** After submitting, the scan will be triggered. You can check the scan results on the same page.

![Scan Results](./images/dast-auth/image3.png)

**Step 8:** Once the **Findings** column is populated, click on it to be redirected to the findings page with all necessary details.

![Findings Page](./images/dast-auth/image5.png)