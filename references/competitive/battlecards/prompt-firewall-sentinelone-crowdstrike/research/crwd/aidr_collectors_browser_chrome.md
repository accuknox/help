Scrape ID: 01a1361d-76fb-759e-ad47-05bb53df7cba
[Skip to main content](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/chrome#__docusaurus_skipToContent_fallback)

AI Detection and Response reaches end of support on November 30, 2026. AIDR capabilities continue in [Falcon Guardian](https://docs.crowdstrike.com/access?ft:originId=dt55byd3) with expanded AI security.

On this page

## Chrome Collector [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/chrome\#chrome-collector "Direct link to Chrome Collector")

The AIDR Chrome collector monitors and controls AI usage in managed Chrome browsers.
You can install the extension from the CrowdStrike update server.

### Requirements [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/chrome\#requirements "Direct link to Requirements")

- **Subscription:** AIDR for Workforce

- **Default roles:** AIDR Admin role explicitly assigned to your Falcon user for the current customer account

- **Permissions required for custom roles:**
  - Manage AIDR findings and workforce collectors
  - Read AIDR data from LogScale
  - Read AIDR findings and workforce collectors
- **CrowdStrike clouds:** Available in US-1, US-2, and EU-1

- **Network:** HTTP access to
[AIDR origins](https://aidr-docs.crowdstrike.com/docs/aidr#cloud-origins)


- **Supported operating system:**
  - Windows
  - macOS
- **System access:** Admin privileges on user machines to update system-level configuration:
  - Registry on Windows
  - Configuration profile on macOS

- **Enterprise management:** The browser collector is intended to be used and supported in enterprise-managed environments. The CrowdStrike-hosted browser extension version **1.x.x** requires an enterprise-managed machine:
  - Enrolled in MDM, such as Intune or Jamf
  - Joined to an Active Directory domain
  - Registered with Microsoft Entra ID

### Get started [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/chrome\#get-started "Direct link to Get started")

1. [Register](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/chrome/register) \- Register a Chrome browser collector in the AIDR console and configure policy rules.
2. [Deploy](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/chrome/deploy) \- Deploy the extension using Chrome Enterprise, Group Policy, Jamf, Intune, or self-service installation.
3. [Verify deployment](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/chrome/verify) \- Confirm the extension status and data flow to the AIDR console.

- [Chrome Collector](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/chrome#chrome-collector)
  - [Requirements](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/chrome#requirements)
  - [Get started](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/chrome#get-started)
