Scrape ID: 01a1361e-efed-747b-82a1-e67ef5540a7a
[Skip to main content](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/falcon-endpoint/falcon-browser-extension#__docusaurus_skipToContent_fallback)

AI Detection and Response reaches end of support on November 30, 2026. AIDR capabilities continue in [Falcon Guardian](https://docs.crowdstrike.com/access?ft:originId=dt55byd3) with expanded AI security.

On this page

## Falcon Browser Extension [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/falcon-endpoint/falcon-browser-extension\#falcon-browser-extension "Direct link to Falcon Browser Extension")

With the Falcon browser extension integration, you can monitor AI activity in web browsers through the Falcon sensor.
Instead of deploying a standalone AIDR browser extension, you can enable AIDR capabilities on the Falcon browser extension.

You can monitor input and output events.
For input events, you can apply enforcement actions, such as block and transform.

Considerations:

- The Falcon browser extension supports only Google Chrome and Microsoft Edge.
If you deployed the standalone AIDR browser extension on Firefox, continue to use it for Firefox coverage.
- This collector runs output rules in report-only mode.
It logs detections but doesn't block or redact LLM responses.


## Requirements [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/falcon-endpoint/falcon-browser-extension\#requirements "Direct link to Requirements")

**Requires all of these subscriptions:**

- AIDR for Workforce
- Falcon Insight XDR

**Sensor:**

- Falcon sensor for Windows versions **7.39** and later
- Falcon sensor for Mac versions **7.40** and later

**Falcon browser extension:**

- Windows x64: **v2** and later
- Windows Arm64: **v2.0.27** and later
- Mac: **v2.0.27** and later

**Default roles:**

- AIDR Admin
- Falcon Administrator
- Falcon Host Administrator

**Permissions required for custom roles:**

- Manage AIDR findings and workforce collectors
- Manage AIDR policy settings of workforce collectors
- Manage AIDR workforce collectors
- Read AIDR data from LogScale
- Read AIDR data from LogScale via AIDR
- Read AIDR findings and workforce collectors
- Read AIDR metadata from LogScale
- Read AIDR metadata from LogScale via AIDR
- Read AIDR policy settings of workforce collectors
- Read AIDR workforce collectors
- Read permissions for Browser Extension UI
- Write permissions for Browser Extension UI
- View browser extension policies
- Write browser extension policies
- View advanced fields for browser extension policies
- Write advanced fields for browser extension policies

**CrowdStrike clouds:** Available in US-1, US-2, and EU-1

**System requirements:**

- Windows:


  - x64: Supported 64-bit versions of Windows 10 or later.
    For more information, see [Windows OS versions supported by the Falcon sensor](https://supportportal.crowdstrike.com/s/article/Supported-Operating-Systems-Windows).
  - Arm64: Windows 11 version 23H2 or later.
  - Windows Server 2016 or later.

Your Windows instance must meet one of these conditions:
  - Joined to a Microsoft Active Directory domain
  - Joined to a Microsoft Entra ID domain
  - Managed through MDM
  - Enrolled in Chrome Browser Cloud Management
- Mac:
  - macOS Sonoma 14 or later.
    For more information, see [macOS versions supported by the Falcon sensor](https://supportportal.crowdstrike.com/s/article/Supported-Operating-Systems-macOS).

**Supported browsers:**

Your organization must manage all browsers.

- Google Chrome - Latest three major release versions
- Microsoft Edge - Latest three major release versions

## Next steps [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/falcon-endpoint/falcon-browser-extension\#next-steps "Direct link to Next steps")

[Deploy the Falcon Endpoint collector](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/falcon-endpoint/deploy) to start monitoring AI activity with the browser extension.

- [Falcon Browser Extension](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/falcon-endpoint/falcon-browser-extension#falcon-browser-extension)
- [Requirements](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/falcon-endpoint/falcon-browser-extension#requirements)
- [Next steps](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/falcon-endpoint/falcon-browser-extension#next-steps)
