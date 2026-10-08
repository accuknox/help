---
title: DAST Authenticated Scan
description: Configure and run authenticated DAST scans in AccuKnox to detect security vulnerabilities in protected application areas that require login credentials.
---

# Authenticated Dynamic Application Security Testing (DAST)

**AccuKnox DAST** now supports **authenticated scans**, enabling comprehensive security testing of protected application areas that require user authentication. This feature ensures thorough vulnerability detection by allowing the scanner to access content behind login pages, preventing false negatives that occur when crawlers cannot reach authenticated endpoints.

??? note "Why Authenticated DAST?"

    Authenticated DAST scans provide enhanced security testing capabilities by:

    - **Toggling between authentication modes**: Switch between authenticated and unauthenticated scan modes based on your testing needs.

    - **Supporting credential-based authentication**: Input username and password for applications requiring login.

    - **Visualizing scan states**: Real-time indicators show scan status as "Logged In," "Logged Out," or "Fallback."

    - **Preventing false negatives**: Access protected content that unauthenticated crawlers would miss, ensuring comprehensive vulnerability coverage.

## Configuration Steps

Follow these steps to configure and run an authenticated DAST scan in AccuKnox:

### 1. Access the AccuKnox Platform

1. Log into the **AccuKnox Platform**.

2. Navigate to **Settings → Collectors**.
![Authenticated DAST Scan](./images/dast-authenticated/1.png)

3. Click on **"Add Collector"**.
![Authenticated DAST Scan](./images/dast-authenticated/2.png)

4. Select **"Web Application DAST Scan"**.
![Authenticated DAST Scan](./images/dast-authenticated/3.png)

### 2. Configure Basic Settings

1. **Collector Name**: Provide a descriptive name for your DAST collector.

2. Click **Next** to proceed to the configuration parameters.

### 3. Configure Scan Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| **Target URL** | The primary target URL to scan. | `https://example.com` |
| **Scan Type** | Choose the scan depth: **Baseline** (quick scan) or **Full** (comprehensive scan). | Baseline or Full |
| **Authentication Mode** | Select authentication type: **No Auth** (default) or **Auth Based** (requires login). | No Auth / Auth Based |
| **Login Page URL** | The URL of the application's login page. | `https://example.com/login` |
| **Login Credentials - Username** | The username for authentication. | — |
| **Login Credentials - Password** | The password for authentication. | — |
| **Include Path** | URLs or patterns to include in scan scope (supports wildcards). | `https://api.example.com/*` |
| **Exclude Path** | URLs or patterns to exclude from scan (e.g., logout endpoints). | `https://example.com/logout` |
| **Logged In Indicator** | Keyword/phrase indicating successful login (e.g., Welcome, Dashboard, My Account). | `Welcome` |
| **Logged Out Indicator** | Keyword/phrase indicating logout or session expiration (e.g., Login, Sign In, Session Expired). | `Login` |
| **Login Fallback URL** | Post-login page URL to verify successful authentication. | `https://example.com/dashboard` |
| **Label** | Label for organizing scan results. See [AccuKnox Labels](../how-to/how-to-create-labels.md). | — |
| **Tags** | (Optional) Tags for categorization and filtering. | — |

![Authenticated DAST Scan](./images/dast-authenticated/4.png)
![Authenticated DAST Scan](./images/dast-authenticated/5.png)
### 4. Configure Notifications

Enter your email address where you would like to receive scan notifications and press **Enter**.
![Authenticated DAST Scan](./images/dast-authenticated/6.png)

### 5. Submit and Monitor Scan

1. After submitting the configuration, the scan will be **automatically triggered**.

2. You can monitor the scan progress on the same page.
![Authenticated DAST Scan](./images/dast-authenticated/7.png)

3. Once the **"Findings"** column is populated, click on it to view detailed results.
![Authenticated DAST Scan](./images/dast-authenticated/8.png)

### 6. View Findings

Clicking on the findings count will redirect you to the **Findings page** with:

- **Detected Vulnerabilities**: List of security issues discovered during the scan.

- **Severity Ratings**: Critical, High, Medium, and Low classifications.

- **Detailed Evidence**: Request/response details, affected endpoints, and remediation guidance.

??? note "Best Practices"

    - **Use descriptive indicators**: Choose logged-in and logged-out indicators that are unique and consistent across your application.

    - **Test credentials separately**: Verify that login credentials work before configuring the scan to avoid authentication failures.

    - **Review exclude paths carefully**: Ensure that logout endpoints and sensitive areas are properly excluded to maintain session stability.

    - **Monitor scan notifications**: Enable email notifications to stay informed about scan completion and critical findings.

## Frequently Asked Questions

???+ question "What is not supported for DAST auth scan?"
    We support only Username Password flow. This method does not support 2FA/MFA enabled sites (like, OTP based login etc).

???+ question "Why there can be findings count mismatch for same scan?"
    Scans can yield inconsistent results even when the target remains unchanged. This variability is often attributed to how the application is explored, with factors like network speed impacting the traditional and AJAX spiders.

    **Minor Variations**: Small differences, such as the number of requests made or variations in specific header values (like "Age" in cache alerts), are considered normal and not problematic.

    This can occur even when:

    - Configurations are identical.
    - The target environment and routing are consistent.
    - No security devices (like WAFs) are interfering.
    - The target isn't changing due to the scan itself (e.g., storing attack payloads).
