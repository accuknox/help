Scrape ID: 01a1361d-72b2-75eb-aecd-55e948ae6208
[Skip to main content](https://aidr-docs.crowdstrike.com/docs/aidr/policies#__docusaurus_skipToContent_fallback)

AI Detection and Response reaches end of support on November 30, 2026. AIDR capabilities continue in [Falcon Guardian](https://docs.crowdstrike.com/access?ft:originId=dt55byd3) with expanded AI security.

On this page

## Policy Overview [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies\#policy-overview "Direct link to Policy Overview")

On the **Policies** page, you can define how AIDR inspects and controls AI traffic.

Each policy type corresponds to a collector category, such as **Browser**, **Falcon Endpoint**, **Application**, **Gateway**, **Agentic**, or **Logging**.
You can assign a policy to any

[collector](https://aidr-docs.crowdstrike.com/docs/aidr/collectors) registered in your account that matches the policy type.
Policy rules report, block, or transform data at different stages of the AI workflow.

Policies determine which detections apply to data flowing through the collector and what actions to enforce.

You can reuse policies across multiple collectors of the same type.
When you update a policy, changes apply to all collectors assigned that policy.

You can omit policy assignment entirely and use collectors for logging only.

## Pre-configured policies [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies\#pre-configured-policies "Direct link to Pre-configured policies")

Pre-configured policies on the **Policies** page cover common use cases.
These policies serve as examples and starting points for your configurations.

To match your security requirements, edit policies or create additional ones.

## Create policy [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies\#create-policy "Direct link to Create policy")

1. On the **Policies** page, click **\+ Policy**.
2. In **Create a Policy**:
1. Select a policy type corresponding to a collector category.
2. Enter a **Display name** that appears in collector policy selectors.
3. Review the **Policy Key**, a unique identifier automatically generated from the display name.
      AIDR reports the policy key in API responses.
3. Click **Save**.

AIDR creates the policy and opens its details page.

To return to the policy details page later, click the policy name in the **Policies** list.

## Policy rules [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies\#configure-policy-rules "Direct link to Policy rules")

On the policy details page, configure rules across the following tabs.

### Site Access [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies\#site-access "Direct link to Site Access")

Site access rules are available only in browser collector policies.

Site access rules control what happens when a user visits a monitored website.

AIDR evaluates site access rules first.
If AIDR triggers a terminal action, such as `Block`, `Redirect`, or `Ignore`, it stops rule execution and skips further inspection for that site.

For more information, see [Site Access Rules](https://aidr-docs.crowdstrike.com/docs/aidr/policies/site-access).

### Inspection Rules [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies\#inspection-rules "Direct link to Inspection Rules")

Every policy contains one or more inspection rules.
Each inspection rule specifies an event route defined by request attribute conditions.
AIDR evaluates inspection rules sequentially and executes the first rule whose event route matches.
If no inspection rule matches, AIDR doesn't analyze the request but still logs it.

For each inspection rule, you can configure **Access Rules** and **Prompt Rules**.

For more information, see [Inspection Rules](https://aidr-docs.crowdstrike.com/docs/aidr/policies/inspection-rules).

#### Access Rules [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies\#access-rules "Direct link to Access Rules")

Access rules evaluate request attributes at runtime to allow, block, or report requests.
Within a matched inspection rule, AIDR evaluates access rules sequentially.
Each rule produces its own result:

- `Continue` actions proceed to the next rule.
- `Stop` actions, such as `Report and Stop`, `Block and Stop`, and `Ignore and Stop`, halt rule execution.
AIDR doesn't evaluate prompt rules.

tip:

Access rules can execute prompt rules or reference their detection results.

For more information, see [Access Rules](https://aidr-docs.crowdstrike.com/docs/aidr/policies/access-rules).

#### Prompt Rules [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies\#prompt-rules "Direct link to Prompt Rules")

Prompt rules apply detectors to content exchanged with the AI system.
If no access rule stops execution, AIDR applies enabled prompt rules within the matched inspection rule:

- AIDR runs configured detectors on the content.
- AIDR applies actions defined in the detectors: block, report, or detector rule-specific actions.

For more information, see [Prompt Rules](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules).

## View policy audit log [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies\#view-policy-audit-log "Direct link to View policy audit log")

On the policy details page, you can view policy configuration changes in the **Audit Log** tab.
For more information, see [Audit Log](https://aidr-docs.crowdstrike.com/docs/aidr/policies/configuration-activity).

## Manage policy options [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies\#manage-policy-options "Direct link to Manage policy options")

Click the menu icon in the policy list or on the policy details page to access the following options:

- **Clone** \- Create a copy of the policy.
- **Rename** \- Edit the policy name.
Available for custom policies and modified pre-configured policies.
- **Delete**\- Remove or reset policies:
  - For a policy you created - Delete the policy.
  - For a pre-configured policy - Reset the policy to its default configuration.

- [Policy Overview](https://aidr-docs.crowdstrike.com/docs/aidr/policies#policy-overview)
- [Pre-configured policies](https://aidr-docs.crowdstrike.com/docs/aidr/policies#pre-configured-policies)
- [Create policy](https://aidr-docs.crowdstrike.com/docs/aidr/policies#create-policy)
- [Policy rules](https://aidr-docs.crowdstrike.com/docs/aidr/policies#configure-policy-rules)
  - [Site Access](https://aidr-docs.crowdstrike.com/docs/aidr/policies#site-access)
  - [Inspection Rules](https://aidr-docs.crowdstrike.com/docs/aidr/policies#inspection-rules)
    - [Access Rules](https://aidr-docs.crowdstrike.com/docs/aidr/policies#access-rules)
    - [Prompt Rules](https://aidr-docs.crowdstrike.com/docs/aidr/policies#prompt-rules)
- [View policy audit log](https://aidr-docs.crowdstrike.com/docs/aidr/policies#view-policy-audit-log)
- [Manage policy options](https://aidr-docs.crowdstrike.com/docs/aidr/policies#manage-policy-options)
