Scrape ID: 01a1361d-717a-74df-a7cd-0775edcb89e9
[Skip to main content](https://aidr-docs.crowdstrike.com/docs/aidr#__docusaurus_skipToContent_fallback)

AI Detection and Response reaches end of support on November 30, 2026. AIDR capabilities continue in [Falcon Guardian](https://docs.crowdstrike.com/access?ft:originId=dt55byd3) with expanded AI security.

On this page

You can use AI detection and response (AIDR) to gain visibility into generative AI usage, detect threats, and enforce policies in enterprise environments.

## Requirements [​](https://aidr-docs.crowdstrike.com/docs/aidr\#requirements "Direct link to Requirements")

- **Requires one or more of these subscriptions:**


  - AIDR for Workforce
  - AIDR for Agents

note:

AIDR subscriptions integrate with

[Next-Gen SIEM](https://docs.crowdstrike.com/r/f090d800).

- **Default roles:**


  - AIDR Metadata Viewer
    View findings and AI usage metadata. Prompt content and sensitive values are excluded. No access to collectors, policies, or settings.

  - AIDR Data Viewer
    All Metadata Viewer access, plus full event data including prompt content and entity values.

  - AIDR Viewer
    All Data Viewer access, plus read access to collectors, policies, and settings.

  - AIDR Admin
    All Viewer access, plus write access to collectors, policies, and settings.


The Falcon Administrator role grants full access to AIDR collectors, policies, and settings, plus metadata-only event access.

For more information, see [User management](https://docs.crowdstrike.com/access?ft:originId=c31605ec).

- **Permissions required for custom roles:**
  - Manage AIDR agent collectors
  - Manage AIDR findings and agent collectors
  - Manage AIDR findings and workforce collectors
  - Manage AIDR policy settings of agent collectors
  - Manage AIDR policy settings of workforce collectors
  - Manage AIDR workforce collectors
  - Read AIDR agent collectors
  - Read AIDR agent events
  - Read AIDR data from LogScale
  - Read AIDR data from LogScale via AIDR
  - Read AIDR findings and agent collectors
  - Read AIDR findings and workforce collectors
  - Read AIDR metadata from LogScale
  - Read AIDR metadata from LogScale via AIDR
  - Read AIDR policy settings of agent collectors
  - Read AIDR policy settings of workforce collectors
  - Read AIDR workforce collectors
- **AIDR permission assignments:**



| Name | Description | AIDR Metadata Viewer | AIDR Data Viewer | AIDR Viewer | AIDR Admin |
| --- | --- | --- | --- | --- | --- |
| Manage AIDR agent collectors | Manage AI Detection and Response agent collectors | ❌ | ❌ | ❌ | ✅ |
| Manage AIDR findings and agent collectors | Manage AI Detection and Response findings and agent collectors | ❌ | ❌ | ❌ | ✅ |
| Manage AIDR findings and workforce collectors | Manage AI Detection and Response findings and workforce collectors | ❌ | ❌ | ❌ | ✅ |
| Manage AIDR policy settings of agent collectors | Manage AI Detection and Response agent collector policy settings | ❌ | ❌ | ❌ | ✅ |
| Manage AIDR policy settings of workforce collectors | Manage AI Detection and Response workforce collector policy settings | ❌ | ❌ | ❌ | ✅ |
| Manage AIDR workforce collectors | Manage AI Detection and Response workforce collectors | ❌ | ❌ | ❌ | ✅ |
| Read AIDR agent collectors | Read AI Detection and Response agent collectors | ❌ | ❌ | ✅ | ✅ |
| Read AIDR agent events | Read AI Detection and Response agent events | ❌ | ❌ | ✅ | ✅ |
| Read AIDR data from LogScale | Read AI Detection and Response data from LogScale directly | ❌ | ✅ | ✅ | ✅ |
| Read AIDR data from LogScale via AIDR | Read AI Detection and Response data from LogScale via AIDR | ❌ | ✅ | ✅ | ✅ |
| Read AIDR findings and agent collectors | Read AI Detection and Response findings and agent collectors | ❌ | ❌ | ✅ | ✅ |
| Read AIDR findings and workforce collectors | Read AI Detection and Response findings and workforce collectors | ❌ | ❌ | ✅ | ✅ |
| Read AIDR metadata from LogScale | Read AI Detection and Response metadata from LogScale directly | ✅ | ✅ | ✅ | ✅ |
| Read AIDR metadata from LogScale via AIDR | Read AI Detection and Response metadata from LogScale via AIDR | ✅ | ✅ | ✅ | ✅ |
| Read AIDR policy settings of agent collectors | Read AI Detection and Response agent collector policy settings | ❌ | ❌ | ✅ | ✅ |
| Read AIDR policy settings of workforce collectors | Read AI Detection and Response workforce collector policy settings | ❌ | ❌ | ✅ | ✅ |
| Read AIDR workforce collectors | Read AI Detection and Response workforce collectors | ❌ | ❌ | ✅ | ✅ |

- **CrowdStrike clouds:** Available in US-1, US-2, and EU-1


- **Network:** HTTP access to AIDR origins

## Cloud origins [​](https://aidr-docs.crowdstrike.com/docs/aidr\#cloud-origins "Direct link to Cloud origins")

You can access the AIDR console via the **AI detection and response** link in the CrowdStrike Falcon console using the CrowdStrike cloud-specific URL.
The AIDR collectors on your hosts use fully qualified domain names (FQDNs) to call AIDR APIs over port 443.

Add these public DNS names to your allowlists if your organization blocks these network communications:

### US-1 [​](https://aidr-docs.crowdstrike.com/docs/aidr\#us-1 "Direct link to US-1")

#### Falcon console [​](https://aidr-docs.crowdstrike.com/docs/aidr\#falcon-console "Direct link to Falcon console")

```text
https://falcon.crowdstrike.com
```

```text
https://assets.falcon.crowdstrike.com
```

#### AIDR APIs and UI [​](https://aidr-docs.crowdstrike.com/docs/aidr\#aidr-apis-and-ui "Direct link to AIDR APIs and UI")

```text
https://api.crowdstrike.com
```

### US-2 [​](https://aidr-docs.crowdstrike.com/docs/aidr\#us-2 "Direct link to US-2")

#### Falcon console [​](https://aidr-docs.crowdstrike.com/docs/aidr\#falcon-console-1 "Direct link to Falcon console")

```text
https://falcon.us-2.crowdstrike.com
```

```text
https://assets.falcon.us-2.crowdstrike.com
```

#### AIDR APIs and UI [​](https://aidr-docs.crowdstrike.com/docs/aidr\#aidr-apis-and-ui-1 "Direct link to AIDR APIs and UI")

```text
https://api.us-2.crowdstrike.com
```

### EU-1 [​](https://aidr-docs.crowdstrike.com/docs/aidr\#eu-1 "Direct link to EU-1")

#### Falcon console [​](https://aidr-docs.crowdstrike.com/docs/aidr\#falcon-console-2 "Direct link to Falcon console")

```text
https://falcon.eu-1.crowdstrike.com
```

```text
https://assets.falcon.eu-1.crowdstrike.com
```

#### AIDR APIs and UI [​](https://aidr-docs.crowdstrike.com/docs/aidr\#aidr-apis-and-ui-2 "Direct link to AIDR APIs and UI")

```text
https://api.eu-1.crowdstrike.com
```

### AIDR documentation [​](https://aidr-docs.crowdstrike.com/docs/aidr\#aidr-documentation "Direct link to AIDR documentation")

AIDR documentation is shared across all clouds:

```text
https://aidr-docs.crowdstrike.com
```

## Capabilities [​](https://aidr-docs.crowdstrike.com/docs/aidr\#capabilities "Direct link to Capabilities")

### Visibility into AI activity [​](https://aidr-docs.crowdstrike.com/docs/aidr\#visibility-into-ai-activity "Direct link to Visibility into AI activity")

You can use AIDR collectors to capture AI interactions across browsers, applications, gateways, and cloud platforms.
The collected telemetry includes prompts, responses, and metadata (user identities, device information, application context).
You can correlate this data in dashboards and detailed logs to gain visibility into AI usage patterns across the organization.
You can also view it in CrowdStrike Falcon Next-Gen SIEM for correlation with endpoint, network, and identity data.

### LLM threat detection [​](https://aidr-docs.crowdstrike.com/docs/aidr\#llm-threat-detection "Direct link to LLM threat detection")

With AIDR, you can detect these risks in generative AI interactions, with optional policy enforcement:

- **Malicious Prompt** \- Adversarial prompts designed to manipulate AI behavior, including prompt injection and jailbreak attempts
- **Malicious Entity** \- Known malicious IP addresses, URLs, and domains
- **MCP Validation** \- Tool poisoning and security issues in MCP tool definitions, such as malicious instructions in tool descriptions, and conflicting tool names and descriptions
- **Confidential and PII Entity** \- Personally identifiable information and confidential data, such as email addresses, social security numbers, credit card numbers, and passports
- **Secret and Key Entity** \- Sensitive credentials, such as API keys and encryption keys
- **Language** \- Language detection with optional allowlist or denylist filtering
- **Code** \- Executable code in AI interactions
- **Competitors** \- Mentions of competing brands or entities
- **Custom Entity** \- Custom text patterns defined by rules with keyword and regex matchers
- **Topic** \- Content related to restricted topics, such as politics, health, legal, toxicity, and self-harm
- **Emoji** \- Potentially unsafe Unicode characters that can obfuscate prompt injection attacks, including emojis, invisible characters, mixed scripts, and modifier sequences

For more information, see

[Prompt Rules](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules)

## How AIDR works [​](https://aidr-docs.crowdstrike.com/docs/aidr\#how-aidr-works "Direct link to How AIDR works")

### Collectors [​](https://aidr-docs.crowdstrike.com/docs/aidr\#collectors "Direct link to Collectors")

Collectors gather AI telemetry from different parts of the enterprise environment.
Each collector category captures AI activity from a specific layer:

- **Falcon Endpoint** \- Monitor and control AI activity through the Falcon sensor. Supports two data sources: the Falcon browser extension (Chrome and Edge) and Network Inspection for desktop AI apps and coding assistants.
- **Browser** \- Monitor AI activity in managed web browsers (Chrome, Edge, Firefox). Apply security policies to data submitted to AI services and capture AI-generated responses.
- **Application** \- Monitor and control AI data flows within your application through CrowdStrike SDKs or direct calls to AIDR APIs.
- **Gateway** \- Apply AIDR policies to data flowing through supported API gateways (Apigee, Azure API Management, Kong, LiteLLM, Portkey, TrueFoundry, JetStream).
- **Agentic** \- Monitor and enforce policies on AI agent activity, including MCP tool interactions (Claude Code, Copilot Studio, MCP Proxy).
- **Logging** \- Monitor AI data flows through cloud and infrastructure integrations (AWS, OpenTelemetry).

For more information, see [Collectors Overview](https://aidr-docs.crowdstrike.com/docs/aidr/collectors).

### Policies [​](https://aidr-docs.crowdstrike.com/docs/aidr\#policies "Direct link to Policies")

You can use AIDR policies to define what to detect and how to respond, then assign policies to collectors.
Each policy contains two types of rules:

- **Access rules** \- Attribute-based conditions that control how requests are processed based on metadata (user identity, device, application ID, and other attributes)
- **Prompt rules** \- Content-based detectors that inspect prompts and responses for security risks

Each detector can be configured with an action:

- **Report** \- Record the detection in AIDR logs without modifying content.
- **Transform** \- Redact, mask, encrypt, or defang detected content before returning it to the collector.
- **Block** \- Flag the request as blocked. The collector decides how to enforce the block.

You can configure policies in the AIDR console.

For more information, see [Policy configuration](https://aidr-docs.crowdstrike.com/docs/aidr/policies/).

### Visibility and analysis [​](https://aidr-docs.crowdstrike.com/docs/aidr\#visibility-and-analysis "Direct link to Visibility and analysis")

You can access logs of all collected telemetry, including:

- Original prompts and AI responses
- Request metadata (timestamp, user ID, device ID, application ID, collector ID, etc.)
- Detection results (identified risks, applied actions, redacted content)

You can access logs in the AIDR console through:

- **[Data flows and dashboards](https://aidr-docs.crowdstrike.com/docs/aidr/visibility/data-flows-and-dashboards/)** \- Visualizations of AI usage patterns, relationships, detection trends, and policy enforcement outcomes
- **[Logs and Findings](https://aidr-docs.crowdstrike.com/docs/aidr/visibility/logs-and-findings/)** \- Detailed logs of individual AI interactions with detection context and enforcement actions
- **[Next-Gen SIEM integration](https://docs.crowdstrike.com/r/f090d800)** \- AIDR logs in CrowdStrike Falcon Next-Gen SIEM for correlation with other security telemetry

## Use cases [​](https://aidr-docs.crowdstrike.com/docs/aidr\#use-cases "Direct link to Use cases")

### Employee workforce monitoring [​](https://aidr-docs.crowdstrike.com/docs/aidr\#employee-workforce-monitoring "Direct link to Employee workforce monitoring")

Security teams can deploy AIDR to monitor employee use of AI tools in managed enterprise environments.
This use case applies to organizations with managed endpoints (via MDM or enterprise tools) and controlled network access (via proxies, secure web gateways, or zero trust solutions).

With AIDR, you can gain visibility into employee AI activity, detect sensitive data exposure and policy violations, and enforce content policies across managed browsers and gateways.
Collector deployments may include Browser collectors on managed browsers, Gateway collectors at network proxies, and Cloud collectors for sanctioned cloud AI platforms.

### AI application development [​](https://aidr-docs.crowdstrike.com/docs/aidr\#ai-application-development "Direct link to AI application development")

Application developers can integrate AIDR into AI-powered applications to implement inline security controls.
This use case applies to internally developed AI systems, autonomous agents, customer-facing chatbots, and other AI applications requiring threat detection and policy enforcement.

With AIDR, you can instrument AI-powered applications for logging AI interactions, detecting threats in prompts and responses, and enforcing policies before data reaches AI models or users.
Collector deployments may include Application collectors (via SDKs or APIs), Agentic collectors (MCP proxy), Gateway collectors at API boundaries, Cloud collectors for cloud-based AI services, and OpenTelemetry instrumentation for standardized telemetry collection.

## Contact us [​](https://aidr-docs.crowdstrike.com/docs/aidr\#contact-us "Direct link to Contact us")

To learn more, [contact us](https://www.crowdstrike.com/en-us/contact-us/).

## Next steps [​](https://aidr-docs.crowdstrike.com/docs/aidr\#next-steps "Direct link to Next steps")

- [Get started with AIDR](https://aidr-docs.crowdstrike.com/docs/aidr/get-started/) \- Choose between employee monitoring (Workforce) or AI application development (Agents)
- [Deploy a collector](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/)
- [Configure a policy](https://aidr-docs.crowdstrike.com/docs/aidr/policies/)
- [View dashboards and logs](https://aidr-docs.crowdstrike.com/docs/aidr/visibility/data-flows-and-dashboards/)

- [Requirements](https://aidr-docs.crowdstrike.com/docs/aidr#requirements)
- [Cloud origins](https://aidr-docs.crowdstrike.com/docs/aidr#cloud-origins)
  - [US-1](https://aidr-docs.crowdstrike.com/docs/aidr#us-1)
    - [Falcon console](https://aidr-docs.crowdstrike.com/docs/aidr#falcon-console)
    - [AIDR APIs and UI](https://aidr-docs.crowdstrike.com/docs/aidr#aidr-apis-and-ui)
  - [US-2](https://aidr-docs.crowdstrike.com/docs/aidr#us-2)
    - [Falcon console](https://aidr-docs.crowdstrike.com/docs/aidr#falcon-console-1)
    - [AIDR APIs and UI](https://aidr-docs.crowdstrike.com/docs/aidr#aidr-apis-and-ui-1)
  - [EU-1](https://aidr-docs.crowdstrike.com/docs/aidr#eu-1)
    - [Falcon console](https://aidr-docs.crowdstrike.com/docs/aidr#falcon-console-2)
    - [AIDR APIs and UI](https://aidr-docs.crowdstrike.com/docs/aidr#aidr-apis-and-ui-2)
  - [AIDR documentation](https://aidr-docs.crowdstrike.com/docs/aidr#aidr-documentation)
- [Capabilities](https://aidr-docs.crowdstrike.com/docs/aidr#capabilities)
  - [Visibility into AI activity](https://aidr-docs.crowdstrike.com/docs/aidr#visibility-into-ai-activity)
  - [LLM threat detection](https://aidr-docs.crowdstrike.com/docs/aidr#llm-threat-detection)
- [How AIDR works](https://aidr-docs.crowdstrike.com/docs/aidr#how-aidr-works)
  - [Collectors](https://aidr-docs.crowdstrike.com/docs/aidr#collectors)
  - [Policies](https://aidr-docs.crowdstrike.com/docs/aidr#policies)
  - [Visibility and analysis](https://aidr-docs.crowdstrike.com/docs/aidr#visibility-and-analysis)
- [Use cases](https://aidr-docs.crowdstrike.com/docs/aidr#use-cases)
  - [Employee workforce monitoring](https://aidr-docs.crowdstrike.com/docs/aidr#employee-workforce-monitoring)
  - [AI application development](https://aidr-docs.crowdstrike.com/docs/aidr#ai-application-development)
- [Contact us](https://aidr-docs.crowdstrike.com/docs/aidr#contact-us)
- [Next steps](https://aidr-docs.crowdstrike.com/docs/aidr#next-steps)
