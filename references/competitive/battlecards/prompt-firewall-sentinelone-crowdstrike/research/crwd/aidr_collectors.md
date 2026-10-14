Scrape ID: 01a1361d-71ac-742f-bbab-3e2d907055cf
[Skip to main content](https://aidr-docs.crowdstrike.com/docs/aidr/collectors#__docusaurus_skipToContent_fallback)

AI Detection and Response reaches end of support on November 30, 2026. AIDR capabilities continue in [Falcon Guardian](https://docs.crowdstrike.com/access?ft:originId=dt55byd3) with expanded AI security.

On this page

## Collectors Overview [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors\#collectors-overview "Direct link to Collectors Overview")

You can monitor AI activity across your environment by deploying AIDR collectors.
Configure and enable a collector to capture telemetry in AIDR event logs.

Some collectors also enforce AIDR policies by blocking requests and redacting or defanging sensitive or malicious content.

To register a collector, click the **\+ Collector** button on the **Collectors** page in the AIDR console.

## Collector categories and types [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors\#collector-types "Direct link to Collector categories and types")

In **Add a Collector**, select a category:

- [Falcon Endpoint](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/falcon-endpoint/) \- Monitor and control AI activity through the Falcon sensor. Supports two data sources: the Falcon browser extension (Chrome and Edge) and Network Inspection for desktop AI apps and coding assistants.
- Browser - Monitor AI activity in managed web browsers.
Apply security policies to data submitted to AI services. Capture AI-generated responses.

  - [Chrome](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/chrome)
  - [Edge](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/edge)
  - [Firefox](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/firefox)
- [Application](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/application/) \- Monitor and control AI data flows within your application through CrowdStrike SDKs or direct calls to AIDR APIs.

- Gateway - Apply AIDR policies to data flowing through supported API gateways.

  - [Apigee](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/gateway/apigee)
  - [Azure API Management](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/gateway/azure-api-management)
  - [Kong Gateway and Kong AI Gateway](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/gateway/kong)
  - [LiteLLM AI Gateway](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/gateway/litellm)
  - [Portkey AI Gateway](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/gateway/portkey)
  - [TrueFoundry AI Gateway](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/gateway/truefoundry)
  - [JetStream AI Hub](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/gateway/jetstream)
- Agentic - Monitor and enforce policies on AI agent activity.

  - [Claude Code](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/agentic/claude-code) \- Enforce AIDR policies on Claude Code sessions through native hooks. Intercept prompts and tool calls, and block actions that violate security rules.
  - [Microsoft Copilot Studio](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/agentic/copilot-studio) \- Monitor and enforce policies on tool invocations made by Copilot Studio agents. Gain visibility into agent actions.

  - [MCP Proxy](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/agentic/) \- Integrate with MCP servers and apply AIDR policies to tool descriptions, agent inputs, and MCP server responses.
- Logging - Monitor AI data flows through cloud and infrastructure integrations.

  - [Cloud](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/cloud/) \- Ingest AI-related telemetry from AWS.
  - [OTel Collector](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/otel/) \- Ingest AI-related events from applications, services, or cloud workloads through the OpenTelemetry collector.

## Capabilities and limitations [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors\#capabilities-and-limitations "Direct link to Capabilities and limitations")

### Deployment scope [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors\#deployment-scope "Direct link to Deployment scope")

| Platforms | Protects | Subscription | Category | Collector |
| --- | --- | --- | --- | --- |
| Windows, Mac (Chrome, Edge) | Web-based AI tools (ChatGPT, Claude, Gemini, etc.) | AIDR for Workforce + Falcon Insight XDR | Falcon Endpoint | [Falcon Browser Extension](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/falcon-endpoint/falcon-browser-extension) |
| Windows | AI applications, browsers | AIDR for Workforce + Falcon Insight XDR | Falcon Endpoint | [Network Inspection](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/falcon-endpoint/network-inspection) |
| Windows, macOS (Chrome, Edge, Firefox) | Web-based AI tools (ChatGPT, Claude, Gemini, etc.) | AIDR for Workforce | Browser | [Chrome](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/chrome), [Edge](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/edge), [Firefox](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/firefox) |
| Any (Python, JS, Go, cURL) | Any LLM provider | AIDR for Agents | Application | [SDK / API](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/application/) |
| Gateway infrastructure | LLM API traffic | AIDR for Agents | Gateway | [Apigee](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/gateway/apigee), [Azure APIM](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/gateway/azure-api-management), [Kong](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/gateway/kong), [LiteLLM](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/gateway/litellm), [Portkey](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/gateway/portkey), [TrueFoundry](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/gateway/truefoundry), [JetStream](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/gateway/jetstream) |
| Any OS running Claude Code | User prompts and tool calls | AIDR for Workforce | Agentic | [Claude Code](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/agentic/claude-code) |
| Microsoft Copilot Studio | Tool invocations by agents | AIDR for Agents | Agentic | [Copilot Studio](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/agentic/copilot-studio) |
| Any (Node.js); Claude Desktop, VS Code, Cursor, custom agents | Tool descriptions, inputs, and outputs | AIDR for Agents | Agentic | [MCP Proxy](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/agentic/) |
| AWS | Amazon Bedrock invocation logs | AIDR for Agents | Logging | [Cloud](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/cloud/) |
| Any OTLP source | AI-related telemetry (`gen_ai.*`) | AIDR for Agents | Logging | [OTel Collector](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/otel/) |

### Enforcement [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors\#enforcement "Direct link to Enforcement")

Some collectors block and redact data in real time. Others only log events for visibility.

#### LLM interactions [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors\#llm-interactions "Direct link to LLM interactions")

- **Input** \- The request payload sent to the LLM provider, which can include user prompts, tool definitions, tool call arguments, and tool results.
For tool-level enforcement outside the LLM call, see [Tool-level interactions](https://aidr-docs.crowdstrike.com/docs/aidr/collectors#tool-level-interactions).
- **Output** \- LLM-generated responses returned to users.

| Collector | Input | Output |
| --- | --- | --- |
| Monitor | Block | Redact | Monitor | Block | Redact |
| --- | --- | --- | --- | --- | --- |
| Falcon Endpoint (Falcon browser extension) [\*](https://aidr-docs.crowdstrike.com/docs/aidr/collectors#falcon-endpoint) | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ |
| Falcon Endpoint (Network Inspection) [\*](https://aidr-docs.crowdstrike.com/docs/aidr/collectors#falcon-endpoint) | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Browser (Chrome, Edge, Firefox) [\*](https://aidr-docs.crowdstrike.com/docs/aidr/collectors#browser-collectors) | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ |
| Application (SDK / API) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Gateway (all) [\*](https://aidr-docs.crowdstrike.com/docs/aidr/collectors#kong-gateway) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Claude Code [\*](https://aidr-docs.crowdstrike.com/docs/aidr/collectors#claude-code) | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ |
| Cloud (AWS) [\*](https://aidr-docs.crowdstrike.com/docs/aidr/collectors#cloud-and-otel) | ✅ | ❌ | ❌ | ✅ | ❌ | ❌ |
| OTel Collector [\*](https://aidr-docs.crowdstrike.com/docs/aidr/collectors#cloud-and-otel) | ✅ | ❌ | ❌ | ✅ | ❌ | ❌ |

#### Tool-level interactions [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors\#tool-level-interactions "Direct link to Tool-level interactions")

The following collectors enforce policies on tool-level interactions between MCP clients and servers or between agents and external tools.

| Collector | Tool Listing | Tool Input | Tool Output |
| --- | --- | --- | --- |
| Monitor | Block | Monitor | Block | Redact | Monitor | Block | Redact |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Claude Code [\*](https://aidr-docs.crowdstrike.com/docs/aidr/collectors#claude-code) | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Copilot Studio [\*](https://aidr-docs.crowdstrike.com/docs/aidr/collectors#copilot-studio) | ❌ | ❌ | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ |
| MCP Proxy [\*](https://aidr-docs.crowdstrike.com/docs/aidr/collectors#mcp-proxy) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

### Considerations [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors\#considerations "Direct link to Considerations")

#### Falcon Endpoint (Falcon browser extension) [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors\#falcon-endpoint "Direct link to Falcon Endpoint (Falcon browser extension)")

This collector runs output rules in report-only mode.
It logs detections but doesn't block or redact LLM responses.

#### Browser collectors [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors\#browser-collectors "Direct link to Browser collectors")

These collectors run output rules in report-only mode.
They log detections but don't block or redact LLM responses.

#### Copilot Studio [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors\#copilot-studio "Direct link to Copilot Studio")

This collector supports only allow/block decisions on entire tool invocations.
Transform actions run in report-only mode.
During enforcement, the collector analyzes only the tool name and parameters - not the user prompt or conversation history.

#### Kong Gateway [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors\#kong-gateway "Direct link to Kong Gateway")

This collector doesn't support streaming responses.

#### Claude Code [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors\#claude-code "Direct link to Claude Code")

- This collector doesn't monitor LLM responses, model configuration, token usage, extended thinking, system prompts, or subagent context.
It captures only data that passes through Claude Code hook events.
- This collector supports redaction on tool inputs and tool outputs, but not on user prompts.

#### MCP Proxy [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors\#mcp-proxy "Direct link to MCP Proxy")

This collector doesn't monitor client interactions with the LLM, such as prompts or model responses.
It enforces policies on tool descriptions, tool inputs, and tool outputs between the MCP client and server.

#### Cloud and OTel [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors\#cloud-and-otel "Direct link to Cloud and OTel")

These collectors provide passive telemetry only.
They forward historical or streamed data for analysis but don't enforce policies inline.
For real-time enforcement, deploy an application, gateway, or agentic collector.

- [Collectors Overview](https://aidr-docs.crowdstrike.com/docs/aidr/collectors#collectors-overview)
- [Collector categories and types](https://aidr-docs.crowdstrike.com/docs/aidr/collectors#collector-types)
- [Capabilities and limitations](https://aidr-docs.crowdstrike.com/docs/aidr/collectors#capabilities-and-limitations)
  - [Deployment scope](https://aidr-docs.crowdstrike.com/docs/aidr/collectors#deployment-scope)
  - [Enforcement](https://aidr-docs.crowdstrike.com/docs/aidr/collectors#enforcement)
    - [LLM interactions](https://aidr-docs.crowdstrike.com/docs/aidr/collectors#llm-interactions)
    - [Tool-level interactions](https://aidr-docs.crowdstrike.com/docs/aidr/collectors#tool-level-interactions)
  - [Considerations](https://aidr-docs.crowdstrike.com/docs/aidr/collectors#considerations)
    - [Falcon Endpoint (Falcon browser extension)](https://aidr-docs.crowdstrike.com/docs/aidr/collectors#falcon-endpoint)
    - [Browser collectors](https://aidr-docs.crowdstrike.com/docs/aidr/collectors#browser-collectors)
    - [Copilot Studio](https://aidr-docs.crowdstrike.com/docs/aidr/collectors#copilot-studio)
    - [Kong Gateway](https://aidr-docs.crowdstrike.com/docs/aidr/collectors#kong-gateway)
    - [Claude Code](https://aidr-docs.crowdstrike.com/docs/aidr/collectors#claude-code)
    - [MCP Proxy](https://aidr-docs.crowdstrike.com/docs/aidr/collectors#mcp-proxy)
    - [Cloud and OTel](https://aidr-docs.crowdstrike.com/docs/aidr/collectors#cloud-and-otel)
