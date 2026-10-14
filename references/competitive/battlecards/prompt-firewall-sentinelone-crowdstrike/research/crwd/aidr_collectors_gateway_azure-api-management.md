Scrape ID: 01a1361f-3d8f-75d8-abf7-b802874f50ce
[Skip to main content](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/gateway/azure-api-management#__docusaurus_skipToContent_fallback)

AI Detection and Response reaches end of support on November 30, 2026. AIDR capabilities continue in [Falcon Guardian](https://docs.crowdstrike.com/access?ft:originId=dt55byd3) with expanded AI security.

On this page

## Azure API Management Collector [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/gateway/azure-api-management\#azure-api-management-collector "Direct link to Azure API Management Collector")

[Azure API Management](https://azure.microsoft.com/en-us/products/api-management) is a service for publishing, securing, and monitoring APIs. It serves as a gateway between backend services and client applications, providing capabilities such as rate limiting, authentication, request/response transformation, and comprehensive analytics.

You can use AIDR with Azure API Management through **custom policies** that inspect, validate, and secure traffic to and from upstream LLM providers using the

[AIDR APIs](https://aidr-docs.crowdstrike.com/docs/api/aidr#/v1/guard_chat_completions).

This gives you AI traffic visibility and enforcement of security controls - such as prompt injection detection, PII redaction, and malicious content blocking - without changes to your application code.

## Requirements [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/gateway/azure-api-management\#requirements "Direct link to Requirements")

- **Subscription:** AIDR for Agents

- **Default roles:** AIDR Admin role explicitly assigned to your Falcon user for the current customer account

- **Permissions required for custom roles:**
  - Manage AIDR findings and agent collectors
  - Read AIDR data from LogScale
  - Read AIDR findings and agent collectors
- **CrowdStrike clouds:** Available in US-1, US-2, and EU-1

- **Network:** HTTP access to [AIDR origins](https://aidr-docs.crowdstrike.com/docs/aidr#cloud-origins)


- **Microsoft Azure:** Azure API Management instance and basic familiarity with Azure policies. For detailed setup instructions, refer to the [Azure API Management documentation](https://learn.microsoft.com/en-us/azure/api-management/get-started-create-service-instance).

## Register Azure API Management collector [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/gateway/azure-api-management\#register-azure-api-management-collector "Direct link to Register Azure API Management collector")

1. On the **Collectors** page, click **\+ Collector**.

2. Choose **Gateway** as the collector type, then select **Azure API Management** and click **Next**.
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

## Deploy collector [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/gateway/azure-api-management\#deploy-collector "Direct link to Deploy collector")

On the collector details page in the AIDR console, you can switch to the **Install** tab for instructions to install and configure the AIDR policy in Azure API Management.

### Configure named values [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/gateway/azure-api-management\#configure-named-values "Direct link to Configure named values")

Before configuring the AIDR policy, set up named values in Azure API Management to securely store your AIDR credentials.

1. In the Azure portal, navigate to your API Management instance.
2. Under **APIs**, select **Named values**.
3. Click **\+ Add** to create a new named value.
4. Create the following named values:

| Name | Display Name | Type | Value | Description |
| --- | --- | --- | --- | --- |
| `ai-guard-url` | `ai-guard-url` | Plain | Your AIDR endpoint URL | Example: `https://api.crowdstrike.com/aidr/aiguard` |
| `ai-guard-token` | `ai-guard-token` | Secret | Your AIDR API token | Keep this secure by selecting "Secret" type |

You can copy both values from the collector's **Config** tab in the AIDR console.

note:

For more information on managing named values, see the [Azure API Management named values documentation](https://learn.microsoft.com/en-us/azure/api-management/api-management-howto-properties).

### Install and configure AIDR policy [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/gateway/azure-api-management\#install-and-configure-aidr-policy "Direct link to Install and configure AIDR policy")

After setting up the named values, you can install and configure the AIDR policy in your Azure API Management instance.

1. **Get the Policy XML**: Copy the policy XML from the [CrowdStrike AIDR Azure API Management repository](https://github.com/CrowdStrike/aidr-azure-api-management/blob/main/ai-guard-policy.xml).

2. **Navigate to Policy Configuration**:
   - In the Azure portal, go to your API Management instance.
   - Select **APIs** from the left menu.
   - Choose the API you want to protect.
   - Select **All operations** to apply to the entire API, or choose a specific operation.
   - In the **Inbound processing** section, select the **`</>`** (code editor) icon.
3. **Apply the Policy**:
   - Paste or merge the AIDR policy XML into your existing policy definition.
   - Ensure the named values (`{{ai-guard-url}}` and `{{ai-guard-token}}`) are correctly referenced.
   - Save the policy configuration.

### Policy structure and requirements [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/gateway/azure-api-management\#policy-structure-and-requirements "Direct link to Policy structure and requirements")

The AIDR policy uses the standard Azure API Management policy sections:

```xml
<policies>
    <inbound>
        <base />
        <!-- AIDR policy for request inspection -->
    </inbound>
    <backend>
        <base />
    </backend>
    <outbound>
        <base />
        <!-- AIDR policy for response inspection -->
    </outbound>
    <on-error>
        <base />
    </on-error>
</policies>
```

**Requirements:**

- Your API must handle requests and responses in [OpenAI Responses API format](https://developers.openai.com/api/reference/resources/responses/methods/create).
- Named values for `ai-guard-url` and `ai-guard-token` must be configured.
- The policy validates and optionally transforms content before it reaches the LLM or returns to the client.

note:

Policies are automatically associated with the collector's policy rules:

- **Inbound policy** \- **Input Rules**
- **Outbound policy** \- **Output Rules**

For detailed policy configuration options, refer to the [Azure API Management policy documentation](https://learn.microsoft.com/en-us/azure/api-management/set-edit-policies).

## Next steps [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/gateway/azure-api-management\#next-steps "Direct link to Next steps")

- View collected data on [Visibility](https://aidr-docs.crowdstrike.com/docs/aidr/visibility/data-flows-and-dashboards/) and [Findings](https://aidr-docs.crowdstrike.com/docs/aidr/visibility/logs-and-findings/) pages.
Analyze it in [Next-Gen SIEM](https://aidr-docs.crowdstrike.com/docs/aidr/visibility/next-gen-siem) to decide on further implementation steps.

- Determine which [policy](https://aidr-docs.crowdstrike.com/docs/aidr/policies/) to apply:
  - Start with monitoring policies and report actions.
  - Apply protection to identified risks by enforcing blocking and data transformation actions based on your organization’s AI usage guidelines.
- For more info, see [Collector Categories](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/).


- [Azure API Management Collector](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/gateway/azure-api-management#azure-api-management-collector)
- [Requirements](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/gateway/azure-api-management#requirements)
- [Register Azure API Management collector](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/gateway/azure-api-management#register-azure-api-management-collector)
- [Deploy collector](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/gateway/azure-api-management#deploy-collector)
  - [Configure named values](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/gateway/azure-api-management#configure-named-values)
  - [Install and configure AIDR policy](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/gateway/azure-api-management#install-and-configure-aidr-policy)
  - [Policy structure and requirements](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/gateway/azure-api-management#policy-structure-and-requirements)
- [Next steps](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/gateway/azure-api-management#next-steps)
