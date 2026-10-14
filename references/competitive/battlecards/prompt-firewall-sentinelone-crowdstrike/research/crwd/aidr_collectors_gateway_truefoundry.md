Scrape ID: 01a1361f-9ba9-72b2-99b3-8713f2efca89
[Skip to main content](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/gateway/truefoundry#__docusaurus_skipToContent_fallback)

AI Detection and Response reaches end of support on November 30, 2026. AIDR capabilities continue in [Falcon Guardian](https://docs.crowdstrike.com/access?ft:originId=dt55byd3) with expanded AI security.

On this page

## TrueFoundry AI Gateway Collector [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/gateway/truefoundry\#truefoundry-ai-gateway-collector "Direct link to TrueFoundry AI Gateway Collector")

[TrueFoundry](https://www.truefoundry.com/ai-gateway) is a platform for deploying, managing, and scaling AI applications and LLM workloads.

The TrueFoundry AI Gateway routes and governs API traffic to LLM providers.
You can monitor and protect AI traffic flowing through the TrueFoundry AI Gateway by deploying the AIDR collector as a TrueFoundry guardrail.

After you configure the collector, the gateway forwards API request and response data to AIDR for analysis.
You can define policy rules to evaluate content, report in AIDR logs, and enforce an action - allow, block, or redact.
The gateway applies the action before forwarding requests to the AI provider or returning responses to users.

Considerations:

- The gateway sends only prompts and completions to AIDR for analysis, not MCP tool content.
- Some metadata is not available through this collector, such as `source_ip`, `model_version`, and `app_id`. Use `span_id` to correlate with TrueFoundry logs for missing attributes.
- The collector doesn't support streaming responses. When streaming is enabled, TrueFoundry skips output guardrails because they require the complete response text to evaluate.

For more information, see the TrueFoundry article [CrowdStrike AIDR Integration](https://www.truefoundry.com/docs/ai-gateway/crowdstrike).

## Requirements [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/gateway/truefoundry\#requirements "Direct link to Requirements")

- **Subscription:** AIDR for Agents

- **Default roles:** AIDR Admin role explicitly assigned to your Falcon user for the current customer account

- **Permissions required for custom roles:**
  - Manage AIDR findings and agent collectors
  - Read AIDR data from LogScale
  - Read AIDR findings and agent collectors
- **CrowdStrike clouds:** Available in US-1, US-2, and EU-1

- **Network:** HTTP access to
[AIDR origins](https://aidr-docs.crowdstrike.com/docs/aidr#cloud-origins)


- **TrueFoundry:** [TrueFoundry](https://www.truefoundry.com/) account with AI Gateway access

## Register TrueFoundry collector [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/gateway/truefoundry\#register-truefoundry-collector "Direct link to Register TrueFoundry collector")

1. On the **Collectors** page, click **\+ Collector**.

2. Choose **Gateway** as the collector type, then select **TrueFoundry** and click **Next**.
3. On the **Add a Collector** screen:
   - **Collector Name:** Enter a descriptive name for the collector. This name appears in dashboards and reports.
   - **Logging:** Select whether to log prompt data and model responses, or only metadata sent to AIDR. You can also exclude prompt content in [access rule action settings](https://aidr-docs.crowdstrike.com/docs/aidr/policies/access-rules#exclude-prompt-content).
   - **Optional. Policy:** Assign a policy to analyze incoming data and model responses.

The assigned policy determines which detections run on data sent to AIDR.
Policies define rules for detecting malicious activity, sensitive data exposure, topic violations, and other risks in AI interactions.

     - Select an existing policy available for this collector type.

       The selected policy name appears under the drop-down list. After you save the collector registration, this label becomes a link to the corresponding policy page.

       You can create a policy on the **Policies** page.

     - You can select `No Policy, Log Only`. Without a policy, AIDR records activity for visibility and analysis without applying detection rules.

4. Click **Save** to complete collector registration.

This opens the collector details page, where you can:

- Update the collector name, logging preference, and policy assignment.
- Click the policy link to view the policy details.
- Copy credentials and AIDR base URL from the **Config** tab to call AIDR APIs.
- View installation instructions for the collector type on the **Install** tab.
- View the collector configuration activity logs.

To open the collector details later, select your collector from the list on the **Collectors** page.

## Deploy collector [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/gateway/truefoundry\#deploy-collector "Direct link to Deploy collector")

To install and configure the collector, see the TrueFoundry article [CrowdStrike AIDR Integration](https://www.truefoundry.com/docs/ai-gateway/crowdstrike).

On the collector details page, copy the AIDR API token and base URL from the **Config** tab.
You need these values to configure the CrowdStrike AIDR guardrail in TrueFoundry.

## How TrueFoundry handles AIDR responses [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/gateway/truefoundry\#how-truefoundry-handles-aidr-responses "Direct link to How TrueFoundry handles AIDR responses")

### Modes of operation [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/gateway/truefoundry\#modes-of-operation "Direct link to Modes of operation")

TrueFoundry guardrails run in one of two modes:

- **Mutate** \- Can modify data or block the user prompt or model response.
- **Validate** \- Can block the user prompt or model response.

The TrueFoundry AI Gateway executes guardrails in two phases:

1. Mutation guardrails run first, sequentially.
2. Validation guardrails run next.

This applies to both the input (user prompt before the LLM) and the output (LLM response before the caller).

For more information, see the TrueFoundry article [Guardrails and Security](https://www.truefoundry.com/docs/ai-gateway/guardrails-overview).

### Violations [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/gateway/truefoundry\#violations "Direct link to Violations")

By default, the gateway raises a violation and blocks when either of these conditions is true:

- Top-level result includes `"blocked": true` \- A policy rule blocked the request.

- Any detector returns `"detected": true` and the platform-level guardrail parameter `enforce_on_detection = true` (the default), even when AIDR returns `"blocked": false`.

In Mutate mode, this doesn't apply to the following detectors when they transform the content (`"transformed": true`):


  - [Confidential and PII Entity](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#confidential-and-pii) (`confidential_and_pii_entity`)
  - [Secret and Key Entity](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#secret-and-key-entity) (`secret_and_key_entity`)
  - [Custom Entity](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#custom-entity) (`custom_entity`)

All other detectors trigger a violation on `"detected": true` and `enforce_on_detection = true` regardless of AIDR's overall blocked status and mode of operation.
This includes [Malicious Entity](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#malicious-entity) (`malicious_entity`), even when it transforms (defangs) data.

For more information, see the TrueFoundry article [CrowdStrike AIDR Integration](https://www.truefoundry.com/docs/ai-gateway/crowdstrike#when-the-gateway-considers-the-call-a-%E2%80%9Cviolation%E2%80%9D).

## View collector data in AIDR [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/gateway/truefoundry\#view-collector-data-in-aidr "Direct link to View collector data in AIDR")

### TrueFoundry AI Gateway fields [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/gateway/truefoundry\#truefoundry-ai-gateway-fields "Direct link to TrueFoundry AI Gateway fields")

TrueFoundry gateway events include the following field values:

- `collector_type` \- `truefoundry_gateway`.
- `tenant_id` \- Your TrueFoundry organization identifier.
- `span_id` \- TrueFoundry `tfy.request.conversation_id`.
Use this to correlate an AIDR finding with the specific gateway request in TrueFoundry logs.
- `provider` \- The LLM provider.
For example, `openai`.
- `model_name` \- The model that TrueFoundry routed the request to.
For example, `gpt-4.1-mini`.
- `user_id` \- The TrueFoundry logged-in user's email.

### AIDR Findings [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/gateway/truefoundry\#aidr-findings "Direct link to AIDR Findings")

On the **Findings** page, you can identify TrueFoundry gateway events by filtering on **Collector Type**`truefoundry_gateway`:

JSON representation of an example TrueFoundry gateway event in Findings

```json
{
  ...
  "collector_type": "truefoundry_gateway",
  "collector_name": "My TrueFoundry collector",
  "model_name": "gpt-4.1-mini",
  "provider": "openai",
  "span_id": "019f3e3f-1084-7bb6-b630-94c199934b6a",
  "tenant_id": "my-truefoundry-org",
  "user_id": "user@example.com",
  ...
}
```

You can view collector event data in AIDR **Findings** and **Visibility**:

- [Findings](https://aidr-docs.crowdstrike.com/docs/aidr/visibility/logs-and-findings) \- View individual events, filter by collector type, and inspect detection details.
- [Visibility](https://aidr-docs.crowdstrike.com/docs/aidr/visibility/data-flows-and-dashboards) \- Explore relationships between logged data attributes and view metrics in AIDR dashboards.

### Next-Gen SIEM [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/gateway/truefoundry\#next-gen-siem "Direct link to Next-Gen SIEM")

TrueFoundry gateway events appear in Next-Gen SIEM with the following parsed fields:

- `Vendor.collector_type` \- `truefoundry_gateway`.
- `Vendor.tenant_id` \- Your TrueFoundry organization identifier.
- `Vendor.span_id` \- TrueFoundry `tfy.request.conversation_id`.
Use this to correlate an AIDR finding with the specific gateway request in TrueFoundry logs.
- `Vendor.provider` \- The LLM provider.
For example, `openai`.
- `Vendor.model_name` \- The model that TrueFoundry routed the request to.
For example, `gpt-4.1-mini`.
- `Vendor.user_id` \- The TrueFoundry logged-in user's email.

Example TrueFoundry gateway event in Next-Gen SIEM

```json
{
  ...
  "agent.type": "truefoundry_gateway",
  "agent.name": "My TrueFoundry collector",
  "user.id": "user@example.com",
  "Vendor.collector_type": "truefoundry_gateway",
  "Vendor.collector_name": "My TrueFoundry collector",
  "Vendor.tenant_id": "my-truefoundry-org",
  "Vendor.span_id": "019f3fa4-7406-7ffe-b305-baef3d6729d4",
  "Vendor.provider": "openai",
  "Vendor.model_name": "gpt-4.1-mini",
  "Vendor.user_id": "user@example.com",
  ...
}
```

To query TrueFoundry gateway events in the Falcon console, go to **Next-Gen SIEM** \> **Advanced event search**, select `All` as the source, and enter:

Next-Gen SIEM query - TrueFoundry gateway events

```logscale
#repo="aidr"
| event_type="AIDRPromptDataEvent"
| agent.type="truefoundry_gateway"
```

For more information, see [Next-Gen SIEM](https://aidr-docs.crowdstrike.com/docs/aidr/visibility/next-gen-siem).

## Next steps [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/gateway/truefoundry\#next-steps "Direct link to Next steps")

- View collected data on [Visibility](https://aidr-docs.crowdstrike.com/docs/aidr/visibility/data-flows-and-dashboards/) and [Findings](https://aidr-docs.crowdstrike.com/docs/aidr/visibility/logs-and-findings/) pages.
Analyze it in [Next-Gen SIEM](https://aidr-docs.crowdstrike.com/docs/aidr/visibility/next-gen-siem) to decide on further implementation steps.

- Determine which [policy](https://aidr-docs.crowdstrike.com/docs/aidr/policies/) to apply:
  - Start with monitoring policies and report actions.
  - Apply protection to identified risks by enforcing blocking and data transformation actions based on your organization’s AI usage guidelines.
- For more info, see [Collector Categories](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/).


- [TrueFoundry AI Gateway Collector](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/gateway/truefoundry#truefoundry-ai-gateway-collector)
- [Requirements](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/gateway/truefoundry#requirements)
- [Register TrueFoundry collector](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/gateway/truefoundry#register-truefoundry-collector)
- [Deploy collector](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/gateway/truefoundry#deploy-collector)
- [How TrueFoundry handles AIDR responses](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/gateway/truefoundry#how-truefoundry-handles-aidr-responses)
  - [Modes of operation](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/gateway/truefoundry#modes-of-operation)
  - [Violations](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/gateway/truefoundry#violations)
- [View collector data in AIDR](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/gateway/truefoundry#view-collector-data-in-aidr)
  - [TrueFoundry AI Gateway fields](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/gateway/truefoundry#truefoundry-ai-gateway-fields)
  - [AIDR Findings](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/gateway/truefoundry#aidr-findings)
  - [Next-Gen SIEM](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/gateway/truefoundry#next-gen-siem)
- [Next steps](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/gateway/truefoundry#next-steps)
