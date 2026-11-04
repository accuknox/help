---
title: API Security Scan Onboarding
description: Run an API security scan in AccuKnox two ways. Upload an OpenAPI specification and scan it from API Security, or run an API Scan collector against a live target URL, then open the findings.
---

# API Security Scan Onboarding

AccuKnox scans your APIs by two paths, and both start from an OpenAPI file you upload. This page runs
each one from the upload to the findings page.

---

## Choose a path

| Path | Where you start | What it needs | What it reports |
| --- | --- | --- | --- |
| Specification scan | **API Security** > **Scan** | An OpenAPI file in JSON or YAML | Shadow API, Orphan API and Zombie API classification against the specification |
| API Scan collector | **Settings** > **Collectors** | A reachable target URL, plus a specification, a collection or a specification URL | Active security test results against the running API |

Run both if you have a live target. One path finds undocumented endpoints, the other finds vulnerable ones.

## Prerequisites

- An OpenAPI or Swagger file in `.json`, `.yaml` or `.yml` format, up to 3 MB.
- A label. Create one with [Create Labels](how-to-create-labels.md).
- For the collector path, a target URL that the AccuKnox scanner can reach.

!!! tip "Live traffic is optional"
    Neither path needs a traffic connector. A connector adds continuous endpoint discovery on top of
    the scans. See [Watch live API traffic](#watch-live-api-traffic).

---

## Path 1: Scan an uploaded specification

### Step 1: Upload the specification

**1.** Go to **API Security** > **API Specification**.

![Left navigation with API Specification selected under API Security](./images/api-sec-onboarding/01-nav-api-specification.png)

**2.** Click **Upload** at the top right of the page.

![API Specification page with the Upload button at the top right](./images/api-sec-onboarding/02-api-specification-upload-button.png)

**3.** Click **Click to upload**, or drag the file into the dashed area. Then click **DONE**.

![Upload Specifications dialog showing the accepted formats JSON, YAML and YML up to 3MB, with openapi3.yml staged](./images/api-sec-onboarding/03-upload-specifications-dialog.png)

!!! warning "A same-name upload overwrites"
    A file uploaded with the name of an existing file replaces that file. Rename the new file first if
    you want to keep both versions.

### Step 2: Create the scan

**1.** Go to **API Security** > **Scan**.

![Left navigation with Scan selected under API Security](./images/api-sec-onboarding/04-nav-api-scan.png)

**2.** Click **NEW SCAN** at the top right.

![Scan page listing earlier scans, with the NEW SCAN button at the top right](./images/api-sec-onboarding/05-scan-new-scan-button.png)

**3.** Fill in the form:

| Field | Required | What to enter |
| --- | --- | --- |
| **Scan Name** | Yes | A name you can find later in the scan list |
| **Description** | No | Free text about the scan target |
| **Label** | Yes | The label that groups the findings |
| **Files** | Yes | Select the specification you uploaded, or upload one here |
| **Select Endpoints** | Yes | **All Endpoints**, or **Specific Collections** to scan one collection |

![New Scan form with Scan Name, Description, Label, the Files selector holding openapi3.yml, and the Select Endpoints choice](./images/api-sec-onboarding/06-new-scan-form.png)

**4.** Scroll down, set the scan type to **On-demand** or **Scheduled**, then submit the form.

### Step 3: Open the findings

**1.** Watch the **Status** column on the **Scan** page. Wait for **Complete**.

**2.** Click the arrow icon at the right of the scan row.

![Scan list with the Status column reading Complete and the open arrow at the right of the row](./images/api-sec-onboarding/07-scan-status-complete.png)

The arrow opens **Issues** > **Findings**, filtered to **API Security Findings**. Each row names the
vulnerability, the asset such as `PUT /users/v1/test1/email`, the risk factor, and the scan that found it.

![API Security Findings list showing Shadow API and Orphan API rows with risk factor, scan config name and occurrence count](./images/api-sec-onboarding/08-api-security-findings.png)

---

## Path 2: Scan with the API Scan collector

This collector runs active security tests against a running API. To scan against a file, upload it
first with [Step 1](#step-1-upload-the-specification).

### Step 1: Add the collector

**1.** Go to **Settings** > **Collectors**.

![Left navigation with Collectors selected under Settings](./images/api-sec-onboarding/11-nav-settings-collectors.png)

**2.** Click **Add Collector**.

**3.** Scroll to **Web Security**. In the **Web Application DAST Scan** card, set the dropdown to
**API Scan**, then click the arrow.

![Web Security section of the Add Collector page with API Scan selected in the Web Application DAST Scan card](./images/api-sec-onboarding/12-add-collector-web-security.png)

### Step 2: Configure the target

**1.** Enter the **Target URL** of the API you want to test.

**2.** Choose the **API Spec Source**:

| Source | Use it when |
| --- | --- |
| **OpenApi Spec File** | You uploaded the specification under **API Security** > **API Specification** |
| **Collection** | You want to scan an existing API collection instead of a file |
| **OpenApi Spec File URL** | The specification is served at a URL the scanner can reach |

**3.** For **OpenApi Spec File**, pick the file from the dropdown.

**4.** Under **Identifiers**, select a **Label**. Add **Tags** if you want to filter on them later.

![Configure Target step with Target URL, the three API Spec Source options, the spec file dropdown, and the Label and Tags fields](./images/api-sec-onboarding/13-collector-configure-target.png)

**5.** Click **Next**, set the schedule and the notification email, then save the collector.

### Step 3: Open the findings

**1.** Go back to **Settings** > **Collectors**.

**2.** Wait for the **Findings** column of your collector row to show a count.

**3.** Click that count.

![Collectors list with the Findings column highlighted and a count of 154 on one Web Application DAST Scan row](./images/api-sec-onboarding/14-collectors-findings-column.png)

The count opens **Issues** > **Findings**, filtered to **API Security Findings**.

![Collector findings filtered to API Security Findings, listing session management, source code disclosure and information leak results per endpoint](./images/api-sec-onboarding/15-collector-findings.png)

!!! info "The two paths report different things"
    A specification scan reports endpoints that do not match the specification. A collector scan
    reports weaknesses in a live response, such as a source code disclosure or a missing cache header.

---

## Watch live API traffic

A traffic connector adds continuous discovery to either scan path. Once logs reach the control plane,
endpoints appear on their own.

**1.** Connect a source. See [API Security Integrations](../integrations/api-overview.md) for
AWS API Gateway, the Kubernetes API proxy, Istio, NGINX Ingress, Kong and F5.

**2.** Go to **API Security** > **Inventory**.

![Left navigation with Inventory selected under API Security](./images/api-sec-onboarding/09-nav-api-inventory.png)

**3.** Click any endpoint to open its telemetry.

![Endpoint detail panel showing domain name, namespace, cluster, protocol, hit count, status code, port and the sensitive parameters found in the request and the response](./images/api-sec-onboarding/10-inventory-endpoint-telemetry.png)

---

## Related

- [API Security Use Case](../use-cases/api-security.md), collections, finding types and rate limiting
- [API Security Integrations](../integrations/api-overview.md), the traffic connectors
- [DAST Scan Types](dast-scan-types.md), the scan depth options for web application targets
- [Create Labels](how-to-create-labels.md), the label a scan and a collector both need
