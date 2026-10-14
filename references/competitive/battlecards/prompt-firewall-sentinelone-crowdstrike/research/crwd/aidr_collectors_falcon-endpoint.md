Scrape ID: 01a1361e-d590-70c5-8b1d-73baf1fc8f5d
[Skip to main content](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/falcon-endpoint#__docusaurus_skipToContent_fallback)

AI Detection and Response reaches end of support on November 30, 2026. AIDR capabilities continue in [Falcon Guardian](https://docs.crowdstrike.com/access?ft:originId=dt55byd3) with expanded AI security.

On this page

## Falcon Endpoint Collector [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/falcon-endpoint\#falcon-endpoint-collector "Direct link to Falcon Endpoint Collector")

The Falcon Endpoint collector monitors AI activity on endpoints through the Falcon sensor's built-in integrations.

The Falcon Endpoint collector supports two data sources:

- [Falcon Browser Extension](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/falcon-endpoint/falcon-browser-extension) \- Monitors AI activity in Chrome and Edge web browsers through the Falcon browser extension.
- [Network Inspection](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/falcon-endpoint/network-inspection) \- Monitors AI activity in desktop applications, CLIs, and any browser through network-layer traffic inspection at the sensor level.

Deploy the Falcon Endpoint collector when:

- Your endpoints run the Falcon sensor.
- You prefer sensor-managed integrations instead of standalone browser extensions and collectors.
- You want to assign AIDR policies to Falcon host groups for consistent security coverage.

If your endpoints don't run the Falcon sensor, you can use AIDR collectors that don't require it.
For more information, see [Collectors Overview](https://aidr-docs.crowdstrike.com/docs/aidr/collectors).

## Comparison [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/falcon-endpoint\#comparison "Direct link to Comparison")

|  | Browser Extension | Network Inspection |
| --- | --- | --- |
| **Monitors** | Web browsers (Chrome, Edge) | Desktop applications, CLIs, and any browser |
| **Platform** | Windows (x64, Arm64), Mac | Windows |
| **Sensor version** | 7.39+ (Windows), 7.40+ (Mac) | 7.40+ |
| **Input enforcement** | Block, Transform, Report | Report |
| **Output enforcement** | Report | Not captured |

## Next steps [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/falcon-endpoint\#next-steps "Direct link to Next steps")

- See overview and requirements:
  - [Falcon Browser Extension](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/falcon-endpoint/falcon-browser-extension)
  - [Network Inspection](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/falcon-endpoint/network-inspection)
- [Deploy Falcon Endpoint Collector](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/falcon-endpoint/deploy)

- [Falcon Endpoint Collector](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/falcon-endpoint#falcon-endpoint-collector)
- [Comparison](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/falcon-endpoint#comparison)
- [Next steps](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/falcon-endpoint#next-steps)
