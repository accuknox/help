Scrape ID: 01a1361d-766b-725b-9176-a6ceb5cdec85
[Skip to main content](https://aidr-docs.crowdstrike.com/docs/aidr/policies/inspection-rules#__docusaurus_skipToContent_fallback)

AI Detection and Response reaches end of support on November 30, 2026. AIDR capabilities continue in [Falcon Guardian](https://docs.crowdstrike.com/access?ft:originId=dt55byd3) with expanded AI security.

On this page

## Inspection Rules [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/inspection-rules\#inspection-rules "Direct link to Inspection Rules")

Each inspection rule defines an event route - a set of conditions that determines which events the rule applies to.
When the event route matches, AIDR evaluates the

[Access Rules](https://aidr-docs.crowdstrike.com/docs/aidr/policies/access-rules) and [Prompt Rules](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules) configured in that inspection rule.

When you create a policy, AIDR generates default inspection rules based on the policy type.
These rules cover the standard event routes for each collector category.

You can delete, modify, or add inspection rules.

For example, a policy can include the following event routes:

| Name | Identifier | Rule key (including policy identifier) | Source | Conditions |
| --- | --- | --- | --- | --- |
| **Input** | `input_rule` | `k_t_boundary_input_policy` | Default | `app.event_type == input` |
| **Output** | `output_rule` | `k_t_boundary_output_policy` | Default | `app.event_type == output` |
| **My Tool Input** | `my_tool_input` | `k_t_boundary_my_tool_input_xt3ol` | Custom | `app.event_type == tool_input`<br>and `app.app_id == my-gateway` |

## Conditions [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/inspection-rules\#conditions "Direct link to Conditions")

Event route conditions determine which events the inspection rule applies to.
To preview a rule's conditions, hover over a condition on the rule page.

To edit conditions, click the pencil icon next to the conditions.

The condition editor works like the access rule condition editor.
You can create expressions based on request attributes, combine them with `AND` and `OR` logic, and group them into conditions.

note:

Event route conditions cannot reference the following attributes available in access rules:

- `rules.matched` \- Rule matches are unavailable because AIDR evaluates conditions before executing access rules.
- `prompt.detections` \- Detection results are unavailable because AIDR evaluates conditions before determining prompt rules.

Update the conditions in the editor and click **Save**.

## Order of execution [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/inspection-rules\#order-of-execution "Direct link to Order of execution")

AIDR evaluates inspection rules in the order they are displayed:

- The first rule whose event route conditions match applies its [Access Rules](https://aidr-docs.crowdstrike.com/docs/aidr/policies/access-rules) and [Prompt Rules](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules).
- If no event route matches, AIDR doesn't analyze the request but still logs the event with a `No Inspection` tag.

## Reorder inspection rules [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/inspection-rules\#reorder-inspection-rules "Direct link to Reorder inspection rules")

Because inspection rules follow first-match-wins evaluation, rule order matters.

To reorder rules:

1. Click the list icon at the top of the inspection rules panel.
2. In **Reorder Inspection Rules**, drag and drop rules to change their order.
3. Click **Save** to confirm the new order.

## Create inspection rule [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/inspection-rules\#create-inspection-rule "Direct link to Create inspection rule")

1. On the policy details page, in the **Inspection Rules** tab, click the plus icon ( **+**).
2. In **New Inspection Rule**, enter a **Name**.
3. Add one or more [conditions](https://aidr-docs.crowdstrike.com/docs/aidr/policies/inspection-rules#conditions).
4. Click **Save** to create the rule.

The new rule appears in the inspection rules list.
Each rule contains its own **Access Rules** and **Prompt Rules** sections where you configure detection and response behavior.

## Import rules [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/inspection-rules\#import-rules "Direct link to Import rules")

You can import access rules and prompt rules into an inspection rule from another policy.

1. Click the up-and-down-arrow import icon next to the event route conditions.
2. Select a source policy from the list.
3. Select an inspection rule whose rules you want to import.
4. In **Replace inspection rules in "<rule-name>"?**, click **Replace**.

Imported access rules and prompt rules appear in the destination inspection rule.
The source policy rules remain unchanged.

## View findings [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/inspection-rules\#view-findings "Direct link to View findings")

1. Click the search icon next to the import icon.
2. Select an inspection rule from the list.
The **Findings** page opens, filtered to events that matched the selected rule.

## Copy rule key [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/inspection-rules\#copy-rule-key "Direct link to Copy rule key")

1. Click the menu icon next to the search icon and select **Copy Key** to copy the rule's unique identifier.

This key corresponds to the `aiguard_config.rule_key` value in AIDR logs.

## Delete inspection rule [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/inspection-rules\#delete-inspection-rule "Direct link to Delete inspection rule")

Click the menu icon next to the search icon and select **Delete**.

caution:

Deleting an inspection rule removes all access rules and prompt rules configured within it.
This action cannot be undone.

## Report Only Mode [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/inspection-rules\#report-only-mode "Direct link to Report Only Mode")

When you enable **Report Only Mode** for an inspection rule, AIDR evaluates access rules and prompt rules and logs the results, but doesn't enforce actions or return policy decisions to the collector.

In **Report Only Mode**, you can test policies and collect data for analysis without affecting end users.
You can enable this mode per inspection rule to enforce some rules while testing others.

Common use cases for **Report Only Mode**:

- Test new policies in production without user impact.
- Tune detection rules before enforcement.
- Collect baseline data for policy development.

Example API 200 response in Report Only Mode

```output
{
  ...
  "status": "Success",
  "summary": "The payload has been accepted and will be processed asynchronously",
  "result": {}
}
```

note:

Browser and Falcon Endpoint policy inspection rules with `app.event_type == output` always run in **Report Only Mode**.

### How Report Only Mode works with existing rules [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/inspection-rules\#how-it-works-with-existing-rules "Direct link to How Report Only Mode works with existing rules")

When you enable **Report Only Mode**, action labels and color indicators change to reflect reporting-only behavior:

- `Block` becomes `Alert`, and the color indicator changes from red to orange.
AIDR logs the event, but the request proceeds.
Users aren't notified or interrupted.
AIDR sets the **Status** field in logs to `Alerted`.
- The color indicator for `Transform` actions, such as `Replacement`, `Mask`, and `Format Preserving Encryption`, changes from purple to blue.
Transformations apply only to logged content for analysis.
Users see the original, unmodified values.
AIDR sets the **Status** field in logs to `Reported`.

### Interpreting findings [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/inspection-rules\#interpreting-findings "Direct link to Interpreting findings")

In **Report Only Mode**, findings in **Prompt activity** and Next-Gen SIEM show what the policy _would_ have done if enforced, not what users experienced.
Examine the `Alerted` or `Reported` status to distinguish evaluated findings from enforced ones.

- [Inspection Rules](https://aidr-docs.crowdstrike.com/docs/aidr/policies/inspection-rules#inspection-rules)
- [Conditions](https://aidr-docs.crowdstrike.com/docs/aidr/policies/inspection-rules#conditions)
- [Order of execution](https://aidr-docs.crowdstrike.com/docs/aidr/policies/inspection-rules#order-of-execution)
- [Reorder inspection rules](https://aidr-docs.crowdstrike.com/docs/aidr/policies/inspection-rules#reorder-inspection-rules)
- [Create inspection rule](https://aidr-docs.crowdstrike.com/docs/aidr/policies/inspection-rules#create-inspection-rule)
- [Import rules](https://aidr-docs.crowdstrike.com/docs/aidr/policies/inspection-rules#import-rules)
- [View findings](https://aidr-docs.crowdstrike.com/docs/aidr/policies/inspection-rules#view-findings)
- [Copy rule key](https://aidr-docs.crowdstrike.com/docs/aidr/policies/inspection-rules#copy-rule-key)
- [Delete inspection rule](https://aidr-docs.crowdstrike.com/docs/aidr/policies/inspection-rules#delete-inspection-rule)
- [Report Only Mode](https://aidr-docs.crowdstrike.com/docs/aidr/policies/inspection-rules#report-only-mode)
  - [How Report Only Mode works with existing rules](https://aidr-docs.crowdstrike.com/docs/aidr/policies/inspection-rules#how-it-works-with-existing-rules)
  - [Interpreting findings](https://aidr-docs.crowdstrike.com/docs/aidr/policies/inspection-rules#interpreting-findings)
