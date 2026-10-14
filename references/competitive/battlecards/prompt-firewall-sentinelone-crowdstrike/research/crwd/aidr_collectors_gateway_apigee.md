Scrape ID: 01a1361f-22b7-74a8-9b41-0bc879e96927
[Skip to main content](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/gateway/apigee#__docusaurus_skipToContent_fallback)

AI Detection and Response reaches end of support on November 30, 2026. AIDR capabilities continue in [Falcon Guardian](https://docs.crowdstrike.com/access?ft:originId=dt55byd3) with expanded AI security.

On this page

## Apigee Collector [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/gateway/apigee\#apigee-collector "Direct link to Apigee Collector")

[Google Cloud Apigee](https://cloud.google.com/apigee) is a fully managed API management platform that enables organizations to design, secure, analyze, and scale APIs.

You can integrate AIDR with Apigee through the open-source [CrowdStrike AIDR shared flow bundle](https://github.com/CrowdStrike/aidr-apigee). The shared flow inspects both user prompts and LLM responses using the

[AIDR APIs](https://aidr-docs.crowdstrike.com/docs/api/aidr#/v1/guard_chat_completions), enforcing security controls such as threat detection, PII redaction, and policy-based blocking, without changes to your application code.

You can deploy the shared flow to an Apigee environment and invoke it from your API proxy using [FlowCallout policies](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/shared-flows).

## Requirements [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/gateway/apigee\#requirements "Direct link to Requirements")

- **Subscription:** AIDR for Agents

- **Default roles:** AIDR Admin role explicitly assigned to your Falcon user for the current customer account

- **Permissions required for custom roles:**
  - Manage AIDR findings and agent collectors
  - Read AIDR data from LogScale
  - Read AIDR findings and agent collectors
- **CrowdStrike clouds:** Available in US-1, US-2, and EU-1

- **Network:** HTTP access to [AIDR origins](https://aidr-docs.crowdstrike.com/docs/aidr#cloud-origins)


- **Google Cloud:**
  - Project with [Apigee provisioned](https://cloud.google.com/apigee/docs/api-platform/get-started/overview)
  - Apigee API proxy that serves LLM traffic in the [Vertex AI generateContent format](https://cloud.google.com/vertex-ai/generative-ai/docs/reference/rest/v1/projects.locations.endpoints/generateContent)

## Register Apigee collector [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/gateway/apigee\#register-apigee-collector "Direct link to Register Apigee collector")

1. On the **Collectors** page, click **\+ Collector**.

2. Choose **Gateway** as the collector type, then select **Apigee** and click **Next**.
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

## Deploy collector [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/gateway/apigee\#deploy-collector "Direct link to Deploy collector")

### Download and import shared flow [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/gateway/apigee\#download-and-import-shared-flow "Direct link to Download and import shared flow")

1. Download the latest release of the CrowdStrike AIDR shared flow from the [GitHub releases page](https://github.com/CrowdStrike/aidr-apigee/releases).
2. In the Google Cloud console, go to [Apigee Shared flows](https://console.cloud.google.com/apigee/sharedflows).
3. Click **Upload bundle** and upload the downloaded shared flow archive.
4. Name the shared flow `cs-aidr-guard`.
5. Deploy the shared flow to the same Apigee environment as the API proxy you want to protect.

### Create policies in your API proxy [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/gateway/apigee\#create-policies-in-your-api-proxy "Direct link to Create policies in your API proxy")

In your API proxy, create the following three policies.

#### 1\. AssignMessage - Set AIDR configuration [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/gateway/apigee\#1-assignmessage---set-aidr-configuration "Direct link to 1. AssignMessage - Set AIDR configuration")

The `AM-SetAIDRConfig` policy sets the AIDR API token and base URL as flow variables that the shared flow uses to call AIDR APIs.

You can copy both values from the collector's **Config** tab in the AIDR console.

Example AM-SetAIDRConfig.xml

```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<AssignMessage async="false" continueOnError="false" enabled="true" name="AM-SetAIDRConfig">
  <DisplayName>AM-SetAIDRConfig</DisplayName>
  <Properties/>
  <AssignVariable>
    <Name>cs_aidr_token</Name>
    <Value>pts_lj3nqp...6ssc3k</Value>
  </AssignVariable>
  <AssignVariable>
    <Name>aiguard_base_url</Name>
    <Value>api.crowdstrike.com/aidr/aiguard</Value>
  </AssignVariable>
  <IgnoreUnresolvedVariables>true</IgnoreUnresolvedVariables>
</AssignMessage>
```

- **cs\_aidr\_token** \- Your AIDR API token
- **aiguard\_base\_url** \- AIDR API endpoint for your region (without the `https://` protocol prefix)

#### 2\. FlowCallout - Guard LLM input [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/gateway/apigee\#2-flowcallout---guard-llm-input "Direct link to 2. FlowCallout - Guard LLM input")

The `FC-LLMGuardInput` policy invokes the shared flow to inspect the request before it reaches the LLM provider.

FC-LLMGuardInput.xml

```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<FlowCallout async="false" continueOnError="false" enabled="true" name="FC-LLMGuardInput">
  <DisplayName>FC-LLMGuardInput</DisplayName>
  <Properties/>
  <SharedFlowBundle>cs-aidr-guard</SharedFlowBundle>
</FlowCallout>
```

#### 3\. FlowCallout - Guard LLM output [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/gateway/apigee\#3-flowcallout---guard-llm-output "Direct link to 3. FlowCallout - Guard LLM output")

The `FC-LLMGuardOutput` policy invokes the shared flow to inspect the response from the LLM provider before it is returned to the client.

FC-LLMGuardOutput.xml

```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<FlowCallout async="false" continueOnError="false" enabled="true" name="FC-LLMGuardOutput">
  <DisplayName>FC-LLMGuardOutput</DisplayName>
  <Properties/>
  <SharedFlowBundle>cs-aidr-guard</SharedFlowBundle>
</FlowCallout>
```

### Attach policies to proxy flow [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/gateway/apigee\#attach-policies-to-proxy-flow "Direct link to Attach policies to proxy flow")

After creating the policies, attach them to your API proxy's flow:

1. Add `AM-SetAIDRConfig` and `FC-LLMGuardInput` to the **request PreFlow** \- this runs AIDR input checks before forwarding the request to the LLM provider.
2. Add `FC-LLMGuardOutput` to the **response PostFlow** \- this runs AIDR output checks on the LLM response before returning it to the client.

You can also use [flow hooks](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/flow-hooks) to attach the shared flow at the environment level, applying it to all API proxies in that environment without modifying individual proxy configurations.

note:

Policies are automatically associated with the collector's policy rules:

- **Request PreFlow** policies - **Input Rules**
- **Response PostFlow** policies - **Output Rules**

## Request schema [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/gateway/apigee\#request-schema "Direct link to Request schema")

The shared flow expects API proxy requests and responses to follow the [Vertex AI generateContent schema](https://cloud.google.com/vertex-ai/generative-ai/docs/reference/rest/v1/projects.locations.endpoints/generateContent).

Make sure your API proxy handles requests in this format so the shared flow can correctly parse and inspect the content.

## Next steps [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/gateway/apigee\#next-steps "Direct link to Next steps")

- View collected data on [Visibility](https://aidr-docs.crowdstrike.com/docs/aidr/visibility/data-flows-and-dashboards/) and [Findings](https://aidr-docs.crowdstrike.com/docs/aidr/visibility/logs-and-findings/) pages.
Analyze it in [Next-Gen SIEM](https://aidr-docs.crowdstrike.com/docs/aidr/visibility/next-gen-siem) to decide on further implementation steps.

- Determine which [policy](https://aidr-docs.crowdstrike.com/docs/aidr/policies/) to apply:
  - Start with monitoring policies and report actions.
  - Apply protection to identified risks by enforcing blocking and data transformation actions based on your organization’s AI usage guidelines.
- For more info, see [Collector Categories](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/).


- [Apigee Collector](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/gateway/apigee#apigee-collector)
- [Requirements](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/gateway/apigee#requirements)
- [Register Apigee collector](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/gateway/apigee#register-apigee-collector)
- [Deploy collector](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/gateway/apigee#deploy-collector)
  - [Download and import shared flow](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/gateway/apigee#download-and-import-shared-flow)
  - [Create policies in your API proxy](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/gateway/apigee#create-policies-in-your-api-proxy)
    - [1\. AssignMessage - Set AIDR configuration](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/gateway/apigee#1-assignmessage---set-aidr-configuration)
    - [2\. FlowCallout - Guard LLM input](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/gateway/apigee#2-flowcallout---guard-llm-input)
    - [3\. FlowCallout - Guard LLM output](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/gateway/apigee#3-flowcallout---guard-llm-output)
  - [Attach policies to proxy flow](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/gateway/apigee#attach-policies-to-proxy-flow)
- [Request schema](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/gateway/apigee#request-schema)
- [Next steps](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/gateway/apigee#next-steps)
