Scrape ID: 01a1361f-0a1d-7775-a7e2-5823ed620244
[Skip to main content](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/falcon-endpoint/network-inspection#__docusaurus_skipToContent_fallback)

AI Detection and Response reaches end of support on November 30, 2026. AIDR capabilities continue in [Falcon Guardian](https://docs.crowdstrike.com/access?ft:originId=dt55byd3) with expanded AI security.

On this page

## Network Inspection [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/falcon-endpoint/network-inspection\#network-inspection "Direct link to Network Inspection")

AIDR integrates with Network Inspection, a Falcon sensor capability that intercepts network-layer traffic on endpoints.
Through this integration, AIDR monitors user prompts and provider responses for

[supported AI applications](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/falcon-endpoint/network-inspection#supported-ai-applications) regardless of the client type - desktop applications, CLIs, or any web browser.

Considerations:

- Report-only mode - AIDR logs detections for network events but doesn't apply blocking or content transformations.
- Payload limit - Events exceeding 1 MiB are not sent to AIDR.
- No file attachments - AIDR doesn't process file attachments from network events.

## Requirements [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/falcon-endpoint/network-inspection\#requirements "Direct link to Requirements")

**Requires all of these subscriptions:**

- AIDR for Workforce
- Falcon Insight XDR

**Sensor:**

- Falcon sensor for Windows version **7.40** and later

- Falcon sensor for Windows version **8.10** and later adds these capabilities:
  - Provider response visibility
  - Coverage for additional AI applications
  - Windows 11 Arm64 support

**Default roles:**

- AIDR Admin
- Falcon Administrator
- Endpoint Manager

**AIDR permissions required for custom roles:**

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

**CrowdStrike clouds:** Available in US-1, US-2, and EU-1

**System requirements:**

- Windows 11 version 23H2 and later





note:





Network Inspection support on Windows 11 Arm64 hosts requires Falcon sensor for Windows version **8.10** and later.

- Supported 64-bit versions of Windows 10

For more info, see
[Windows OS versions supported by the Falcon Sensor](https://supportportal.crowdstrike.com/s/article/Supported-Operating-Systems-Windows).


For more info, see [Network Inspection](https://docs.crowdstrike.com/access?ft:originId=njxpgsbo).

## Supported AI applications [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/falcon-endpoint/network-inspection\#supported-ai-applications "Direct link to Supported AI applications")

### Anthropic [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/falcon-endpoint/network-inspection\#anthropic "Direct link to Anthropic")

| Application | Surface type | Sensor version |
| --- | --- | --- |
| Claude.ai website | Website | 7.40+ |
| Claude Desktop | Windows desktop app | 7.40+ |
| Claude Code | CLI | 7.40+ |
| Anthropic Console | Website or developer console | 7.40+ |
| Claude Cowork | Windows desktop app | 7.40+ |
| Claude Microsoft Excel Plugin | Microsoft Excel plugin | 7.40+ |
| Claude Powerpoint Plugin | Microsoft PowerPoint plugin | 7.40+ |

### AWS [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/falcon-endpoint/network-inspection\#aws "Direct link to AWS")

| Application | Surface type | Sensor version |
| --- | --- | --- |
| Kiro | Windows desktop app | 8.10+ |

### DeepSeek [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/falcon-endpoint/network-inspection\#deepseek "Direct link to DeepSeek")

| Application | Surface type | Sensor version |
| --- | --- | --- |
| DeepSeek website | Website | 7.40+ |

### GitHub [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/falcon-endpoint/network-inspection\#github "Direct link to GitHub")

| Application | Surface type | Sensor version |
| --- | --- | --- |
| GitHub Copilot | IDE extension | 8.10+ |
| GitHub Copilot extension | IDE extension | 8.10+ |

### Google [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/falcon-endpoint/network-inspection\#google "Direct link to Google")

| Application | Surface type | Sensor version |
| --- | --- | --- |
| Gemini | Website | 7.40+ |

### Microsoft 365 Copilot [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/falcon-endpoint/network-inspection\#microsoft-365-copilot "Direct link to Microsoft 365 Copilot")

| Application | Surface type | Sensor version |
| --- | --- | --- |
| Microsoft 365 Copilot app for Windows | Windows desktop app | 7.40+ |
| Microsoft 365 Copilot in Word for Windows | Windows Office desktop app | 7.40+ |
| Microsoft 365 Copilot in Excel for Windows | Windows Office desktop app | 7.40+ |
| Microsoft 365 Copilot in Outlook for Windows | Windows Office desktop app | 7.40+ |
| Microsoft 365 Copilot in Teams for Windows | Windows Teams desktop app | 7.40+ |
| Microsoft 365 Copilot in OneNote for Windows | Windows Office desktop app | 7.40+ |

### Microsoft Copilot [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/falcon-endpoint/network-inspection\#microsoft-copilot "Direct link to Microsoft Copilot")

| Application | Surface type | Sensor version |
| --- | --- | --- |
| Microsoft Copilot | Windows desktop app | 7.40+ |
| Microsoft Copilot entry point in Windows taskbar or Copilot key | Windows OS integration | 7.40+ |
| Microsoft Copilot in Microsoft Edge | Windows browser integration | 7.40+ |
| Microsoft Copilot website | Website | 7.40+ |
| Microsoft Copilot Studio | Website | 7.40+ |

### OpenAI [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/falcon-endpoint/network-inspection\#openai "Direct link to OpenAI")

| Application | Surface type | Sensor version |
| --- | --- | --- |
| ChatGPT website | Website | 7.40+ |
| ChatGPT Desktop (Chat tab) | Windows desktop app | 7.40+ |
| ChatGPT Desktop (Work tab / Codex) | Windows desktop app | 8.10+ |
| OpenAI Codex | CLI | 8.10+ |

note:

- All browsers are supported.
Network Inspection operates at the network layer, so the AIDR integration monitors any browser accessing the supported applications.

- If your internal AI gateway matches a supported provider's API request structure, you can open a [Support](https://aidr-docs.crowdstrike.com/docs/aidr/support) case to add the gateway's custom FQDN and path to monitoring.


## Next steps [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/falcon-endpoint/network-inspection\#next-steps "Direct link to Next steps")

- [Deploy the Falcon Endpoint collector](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/falcon-endpoint/deploy)

- [Network Inspection](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/falcon-endpoint/network-inspection#network-inspection)
- [Requirements](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/falcon-endpoint/network-inspection#requirements)
- [Supported AI applications](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/falcon-endpoint/network-inspection#supported-ai-applications)
  - [Anthropic](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/falcon-endpoint/network-inspection#anthropic)
  - [AWS](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/falcon-endpoint/network-inspection#aws)
  - [DeepSeek](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/falcon-endpoint/network-inspection#deepseek)
  - [GitHub](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/falcon-endpoint/network-inspection#github)
  - [Google](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/falcon-endpoint/network-inspection#google)
  - [Microsoft 365 Copilot](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/falcon-endpoint/network-inspection#microsoft-365-copilot)
  - [Microsoft Copilot](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/falcon-endpoint/network-inspection#microsoft-copilot)
  - [OpenAI](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/falcon-endpoint/network-inspection#openai)
- [Next steps](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/falcon-endpoint/network-inspection#next-steps)
