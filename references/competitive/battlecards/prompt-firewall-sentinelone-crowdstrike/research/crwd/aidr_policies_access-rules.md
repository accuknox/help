Scrape ID: 01a1361d-74fb-7335-9d47-fd06f3c18514
[Skip to main content](https://aidr-docs.crowdstrike.com/docs/aidr/policies/access-rules#__docusaurus_skipToContent_fallback)

AI Detection and Response reaches end of support on November 30, 2026. AIDR capabilities continue in [Falcon Guardian](https://docs.crowdstrike.com/access?ft:originId=dt55byd3) with expanded AI security.

On this page

You can configure access rules in a policy to evaluate request attributes at runtime and allow, block, or report requests.

## Assistant [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/access-rules\#assistant "Direct link to Assistant")

In the **Assistant** tab, you can create access rules by describing conditions in natural language.
You can start with the Assistant for quick setup, then refine rules in the editor.

To submit a rule request:

1. Describe the rule you want in the Assistant input field.
2. Press Enter or click the arrow button to submit your request.

## Access rules editor [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/access-rules\#access-rules-editor "Direct link to Access rules editor")

In the access rules editor, you can create and update rules, including those created by the Assistant.

### Add access rule [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/access-rules\#add-access-rule "Direct link to Add access rule")

If you see the **No Access Rules Enabled** section in the inspection rule, click **\+ Create first access rule** to open the rule editor.

After you create the first rule, the section label changes to **Execute Access Rules**.
The rule appears as a movable card.

Click the pencil icon to open the rule editor and update the rule.

Click **\+ Access rule** to add more rules.

note:

AIDR evaluates access rules sequentially and independently, in top-down order.
Each rule produces its own result, and any rule with a `Stop` action halts execution.

### Edit access rule [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/access-rules\#edit-access-rule "Direct link to Edit access rule")

In the rule editor, you can create one or more conditions based on request attributes.
Combine conditions with `AND` and `OR` logic:

1. Enter a rule name.

2. Create a condition.
1. Create an expression (a single comparison):
      1. Click the attribute field to view available attributes.
      2. Select a comparison operator for:
         - Request metadata attributes:
           - `==` \- Value equals the specified string exactly.
             Use `@null` to match `null` or missing values, or `@empty` to match empty strings.
           - `!=` \- Value does not equal the specified string.
             Use `@null` to exclude `null` or missing values, or `@empty` to exclude empty strings.
           - `>` \- Value is greater than the specified number.
           - `>=` \- Value is greater than or equal to the specified number.
           - `<` \- Value is less than the specified number.
           - `<=` \- Value is less than or equal to the specified number.
           - `in` \- Value matches one of the values in a comma-separated list.
           - `contains` \- Value contains the specified text as a substring.
           - `not contains` \- Value does not contain the specified text as a substring.
           - `matches` \- Value matches the specified RE2 regular expression pattern.
             For syntax details, see the [Google RE2 GitHub repository](https://github.com/google/re2/wiki/Syntax).
           - `not matches` \- Value does not match the specified RE2 regular expression pattern.
             For syntax details, see the [Google RE2 GitHub repository](https://github.com/google/re2/wiki/Syntax).
         - Prompt content-based:
           - `has` \- Specified detector rule produces a finding.
             For detectors with multiple rules, such as the **Malicious Entity** or **Custom Entity** detectors, you can reference specific rules, like `custom_entity.<rule-name>`. For an example, see [Custom Entity rule reference](https://aidr-docs.crowdstrike.com/docs/aidr/policies/access-rules#custom-entity-specific-rule-reference).
           - `not has` \- Specified detector rule doesn't produce a finding.
             For detectors with multiple rules, such as the **Confidential and PII Entity** or **Language** detectors, you can reference specific rules.
             For example, `confidential_and_pii_entity.<rule-name>`.
           - `executes` \- Triggers prompt rule execution as part of this access rule evaluation.
         - Rules matched reference:
           - `includes` \- Specified rule appears in previously matched rules.
           - `excludes` \- Specified rule does not appear in previously matched rules.
         - Group membership:
           - `includes` \- Subject belongs to the selected group.
           - `excludes` \- Subject does not belong to the selected group.
         - Identity provider attributes (`user.idp.entra.<attribute>`, `user.idp.ad.<attribute>`):
           - Standard comparison operators (`==`, `!=`, `contains`, `not contains`, `matches`, `not matches`, `in`)
      3. Enter the comparison value.
         When you click the value field, the editor suggests values from your data.
         Suggested values include known user IDs and application names.
2. Add another expression to the condition:
      1. Click **Or +** or **And +** next to an existing expression.
      2. Select an `AND` or `OR` logical operator to combine expressions.
3. Change the execution order by dragging expressions with their six-dot handle.
3. Add another condition to the rule:
1. Click **Add Condition +**.
2. Select an `AND` or `OR` logical operator to combine conditions.
4. In the **Then** dropdown, select the action to execute when the rule matches.
You can also click the configuration icon next to the dropdown to [configure action settings](https://aidr-docs.crowdstrike.com/docs/aidr/policies/access-rules#action-settings).


   - `Continue` \- Proceed to the next rule without flagging this rule as a detection.

   - `Report and Continue` \- Flag this rule as a detection and continue to the next rule.

   - `Report and Stop` \- Flag this rule as a detection and stop policy execution.

   - `Block and Stop` \- Block the request, flag this rule as a detection, and stop policy execution.

     See [Block messages](https://aidr-docs.crowdstrike.com/docs/aidr/policies/access-rules#block-messages) for details on customizing a Block action response in browser collector policies.

   - `Ignore and Stop` \- Allow the request and stop policy execution without logging.

   - `Allow and Stop` \- Allow the request, log the event, and stop policy execution.


Each action produces these AIDR **Findings** event values and execution behavior:

| Action | Status | Summary | Rule `detected` | Rule `action` | Execution |
| --- | --- | --- | --- | --- | --- |
| `Continue` | `reported` | `The operation was completed successfully.` | `false` | `allowed` | Continues |
| `Report and Continue` | `reported` | `<rule-name> matched and reported.` | `true` | `reported` | Continues |
| `Report and Stop` | `reported` | `<rule-name> matched and reported then stopped.` | `true` | `reported` | Stops |
| `Block and Stop` | `blocked` | `<rule-name> matched and blocked.` | `true` | `blocked` | Stops |
| `Ignore and Stop` | N/A | N/A | N/A | N/A | Stops |
| `Allow and Stop` | `allowed` | `<rule-name> matched and allowed then stopped.` | `false` | `allowed` | Stops |

note:

The **Status** and **Summary** columns show the final event-level values when this is the last rule to execute.
If execution continues, subsequent rules or detectors override these values.

5. In the **Else** dropdown, select the action to execute when the rule doesn't match.
You can also click the configuration icon next to the dropdown to [configure action settings](https://aidr-docs.crowdstrike.com/docs/aidr/policies/access-rules#action-settings).

6. Click **\+ Access rule** to add another rule.

7. Change the execution order by dragging rules with their six-dot handle.

8. Click **Update** to apply changes to the policy.


note:

- If you define conditions based on prompt content (`prompt.detections`), you must also enable the corresponding detectors.
Configure referenced rules in the **Execute Prompt Rules** section.
For details, see [Prompt Rules](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules).
If you reference a detector in access rules without enabling it, the console prompts you to enable the detector.

- For detectors with multiple rules, you can reference individual rules in `prompt.detections`.

- The `rules.matched` attribute references other access rules by their identifier. AIDR populates this attribute as each rule executes.
A rule can reference only rules that appear earlier in the execution order.
For an example, see [Rules matched reference](https://aidr-docs.crowdstrike.com/docs/aidr/policies/access-rules#rules-matched-reference).

- The `user.groups`, `app.groups`, and `model.groups` attributes represent group membership.
Use these attributes with the `includes` or `excludes` operators to match requests by group.

For `user.groups`, group values include a prefix that identifies the source:


  - `custom:` \- Groups managed in AIDR (for example, `custom:patient_room_chatbot`)
  - `entra:` \- Groups synced from Microsoft Entra ID (for example, `entra:d753f19e-0dcc-4697-a878-8faecf5513f8`)
  - `ad:` \- Groups synced from Active Directory (for example, `ad:f369484c076c43ceab6fa1cc1e240a9f`)

Application and model groups are always custom and carry the `custom:` prefix.

For an example, see [Group membership](https://aidr-docs.crowdstrike.com/docs/aidr/policies/access-rules#group-membership).
To create and manage groups, see [Memberships](https://aidr-docs.crowdstrike.com/docs/aidr/administration/settings#memberships) in Settings.

### Configure action settings [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/access-rules\#action-settings "Direct link to Configure action settings")

In the rule editor, click the configuration icon next to the **Then** or **Else** action dropdown to open action settings.
You can tag events and exclude prompt content from logged events.

#### Tag events [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/access-rules\#tag-events "Direct link to Tag events")

You can tag events with custom labels to classify them for filtering and analysis.
Tags apply regardless of whether AIDR reports or blocks the event.
Use tags for severity levels, compliance exceptions, or custom workflows.

Under **Tag Event**, select from predefined tags or enter a custom tag name.

- Predefined tags:
  - `Critical`
  - `High`
  - `Medium`
  - `Low`
  - `Information`
- Custom tags:

Enter a custom tag name in the tag selector and click **+** or press **Enter**.
You must enter custom tags manually each time - they don't appear as selectable options even if previously used in event logs.


Tags appear in the AIDR **Findings** table under the **TAGS** column and in event logs under the **Tags** field.
You can filter events by tag values on the **Visibility** and **Findings** pages and in Next-Gen SIEM. For more information, see [Visibility and Monitoring](https://aidr-docs.crowdstrike.com/docs/aidr/visibility/).

When multiple rules match a request, AIDR combines their tags into a single, deduplicated list in the event log.

note:

When you select `Ignore and Stop`, tags and prompt content settings are unavailable because AIDR doesn't log the event.

#### Exclude prompt content [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/access-rules\#exclude-prompt-content "Direct link to Exclude prompt content")

You can exclude prompt content from the logged event while still recording event metadata.
Enable **Exclude Prompt Content** in action settings to omit user request and LLM response body data from the AIDR log.

note:

This setting overrides the collector-level logging configuration for matched events.

### Custom block messages [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/access-rules\#block-messages "Direct link to Custom block messages")

In browser collector policies, you can assign custom messages that end users see when AIDR blocks or transforms a request.
You can reuse custom messages across policies in the same account (CID).
Each detector supports one block message and one transform message.
These messages apply to all rules with the respective action in that detector.

You can manage custom messages in **Block Message** or **Transform Message**:

1. Hover over the message icon on the action label - **Block**, **Transform**, or **Defang** \- to preview the assigned message in a tooltip.
You can also open the dialog from the **Manage User Messaging** menu in the expanded rule.
2. Click the message icon to open the dialog.
3. Click the **Select message** dropdown to display existing messages and available controls.
A custom message assigned to the detector displays a **CURRENT** badge.
   - To assign a message, select one from the list, optionally edit it in the text area, and click **Update**.
   - To create a message, click **\+ Create New Message**, enter the message text, and click **\+ Save**.
   - To hide the browser extension popup while still performing the action, select `Do not show a message`.
   - To display the AIDR response [summary](https://aidr-docs.crowdstrike.com/docs/aidr/apis#summary-string---list-of-the-enabled-detectors-outcomes-and-actions-taken) instead, select `Use summary as message`.
   - To display a standard redaction message for transform actions, select `Use standard redaction message`.
   - To set the account-wide default for the message type, **Block** or **Transform**, click the star icon next to a message.
     A filled star indicates the current default.
   - To delete a message, click the trash icon next to it.
     You cannot delete an assigned message or one used as the account default.

When AIDR blocks or transforms a request, it determines which message to return:

1. If the detector has a message assigned, AIDR returns that message.
2. Otherwise, AIDR returns the default for that message type.

The [display\_message](https://aidr-docs.crowdstrike.com/docs/aidr/apis#display_message-string---message-text-to-communicate-to-the-end-user) field in the API response returns the resolved message text.

note:

Changes to custom messages or account defaults can take several minutes to propagate because of caching.

### Examples [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/access-rules\#examples "Direct link to Examples")

#### Request metadata [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/access-rules\#request-metadata "Direct link to Request metadata")

This rule matches requests from user `dennis.nedry` to the `security` application.
The rule also matches requests that specify the `DeepSeek` model.
When matched, it tags the event as `High` and reports the detection, then continues to the next rule.
If the rule doesn't match, execution continues to the next rule.

| Condition | Operator | Value |  |
| --- | --- | --- | --- |
| `Report suspicious activity` (rule name) |
| `user.id` | `== ▼` | `dennis.nedry` | `And ▼` (logical operator) `⊖` (remove expression) |
| `app.app_id` | `== ▼` | `security` | `And +` (add expression) `⊖` (remove expression) |
| `Or ▼` (logical operator) |
| `model.model_name` | `== ▼` | `DeepSeek` | `Or +` (add expression) `⊖` (remove expression) |
| `Add Condition +` |
| **Then**`≡ High``Report and Continue  ▼`<br>**Else**`≡``Continue  ▼` |
| `🗑️` \| `Cancel` \| `Update` |

`+ Access rule`

After you click **Update**, the rule editor closes and displays the rule definition in a structured format:

`if (`

`then` ≡ `High` \| `Report`

`user.id == dennis.nedry`

`and app.app_id == security`

`)`

`or model.model_name == deepseek`

#### Request metadata and prompt rules [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/access-rules\#request-metadata-and-prompt-rules "Direct link to Request metadata and prompt rules")

This rule executes the `US Social Security Number` prompt rule from the **Confidential and PII Entity** detector.
The access rule applies only to requests from the `ingen-chatbot` application.

- When the request matches the `ingen-chatbot` condition, AIDR applies the action configured for the `US Social Security Number` prompt rule.
The access rule then reports the detection and continues to the next rule.
- When the condition doesn't match, AIDR allows the request and stops policy execution without logging.

| Condition | Operator | Value |  |
| --- | --- | --- | --- |
| `Remove PII` (rule name) |
| `app.app_id` | `== ▼` | `ingen-chatbot` | `And ▼` (logical operator) `⊖` (remove expression) |
| `prompt.detections` | `executes ▼` | `confidential_and_pii_entity.us_ssn` | `And +` (add expression) `⊖` (remove expression) |
| `Add Condition +` |
| **Then**`≡``Report and Continue  ▼`<br>**Else**`≡``Ignore and Stop  ▼` |
| `🗑️` \| `Cancel` \| `Update` |

After you click **Update**, the rule editor displays the rule definition as:

`if (`

`then``Report``else``Ignore and Stop`

`app.app_id == ingen-chatbot`

`and prompt.detections executes confidential_and_pii_entity.us_ssn`

`)`

#### Custom Entity rule reference [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/access-rules\#custom-entity-specific-rule-reference "Direct link to Custom Entity rule reference")

This rule blocks requests that contain competitor references detected by a **Custom Entity** rule, except for a specific user.
The **Custom Entity** rule uses a regex pattern (`[Bb]io[-\s]?[Ss]yn`) to match variations of the competitor name, including common misspellings.

The `has` operator references a specific **Custom Entity** rule by its identifier (`custom_entity.biosyn`).

- When the prompt contains a match for the `biosyn` **Custom Entity** rule and the user is not `john.hammond`, the rule blocks the request.
- When the condition doesn't match, execution continues to the next rule.

| Condition | Operator | Value |  |
| --- | --- | --- | --- |
| `Block competitor references` (rule name) |
| `prompt.detections` | `has ▼` | `custom_entity.biosyn` | `And ▼` (logical operator) `⊖` (remove expression) |
| `user.id` | `!= ▼` | `john.hammond` | `And +` (add expression) `⊖` (remove expression) |
| `Add Condition +` |
| **Then**`≡``Block and Stop  ▼`<br>**Else**`≡``Continue  ▼` |
| `🗑️` \| `Cancel` \| `Update` |

After you click **Update**, the rule editor displays the rule definition as:

`if (`

`then``Block`

`prompt.detections has custom_entity.biosyn`

`and user.id != john.hammond`

`)`

#### Rules matched reference [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/access-rules\#rules-matched-reference "Direct link to Rules matched reference")

This example (configured under an output inspection rule) demonstrates three access rules.
The first two rules detect independent risk signals.
The third rule evaluates the `rules.matched` condition to determine whether both earlier rules matched.
When both match, the third rule blocks the request.

Neither signal alone warrants blocking.
Contractors legitimately access the HR chatbot, and some PII may be allowed for permanent employees.
The combination of both signals - a contractor account and exposed PII in the same request - warrants blocking.

- Rule 1 - `Contractors access HR` (`contractors_access_hr`):

This rule matches when contractor accounts access the HR chatbot.
When matched, it reports the detection and continues to the next rule.



`if (`



`then``Report`





`user.id matches ^contractor`





`and app.app_id == hr-chatbot`





`)`

- Rule 2 - `PII exposed` (`pii_exposed`):

This rule matches when the model response contains PII entities, such as email addresses, phone numbers, or person names.
When matched, it reports the detection and continues to the next rule.



`if (`



`then``Report`





`prompt.detections has confidential_and_pii_entity.email_address`





`or prompt.detections has confidential_and_pii_entity.phone_number`





`or prompt.detections has confidential_and_pii_entity.person`





`)`

- Rule 3 - `PII exposed to Contractors` (`pii_exposed_to_contractors`):

This rule matches when both earlier rules matched - indicating a contractor receives a response containing PII through the HR chatbot.
When matched, it blocks the request.



| Condition | Operator | Value |  |
| --- | --- | --- | --- |
| `PII exposed to Contractors` (rule name) |
| `rules.matched` | `includes ▼` | `contractors_access_hr` | `And ▼` (logical operator) `⊖` (remove expression) |
| `rules.matched` | `includes ▼` | `pii_exposed` | `And +` (add expression) `⊖` (remove expression) |
| `Add Condition +` |
| **Then**`≡``Block and Stop  ▼`<br>**Else**`≡``Continue  ▼` |
| `🗑️` \| `Cancel` \| `Update` |


After you click **Update**, the rule editor displays the rule definition as:



`if (`



`then``Block`





`rules.matched includes contractors_access_hr`





`and rules.matched includes pii_exposed`





`)`


Example response from AIDR APIs

```json
{
  ...
  "status": "Success",
  "summary": "PII exposed to Contractors matched and blocked.  Contractors access HR matched and reported.  PII exposed matched and reported.  Confidential and PII Entity was detected and reported.",
  "result": {
    "blocked": true,
    "transformed": false,
    "policy": "k_t_boundary_output_policy",
    "detectors": {
      "confidential_and_pii_entity": {
        "detected": true,
        "data": {
          "entities": [\
            {\
              "action": "reported",\
              "type": "PHONE_NUMBER",\
              "value": "555-555-5555"\
            },\
            {\
              "action": "reported",\
              "type": "EMAIL_ADDRESS",\
              "value": "ed.regis@ingen.com"\
            },\
            {\
              "action": "reported",\
              "type": "PERSON",\
              "value": "Ed Regis"\
            }\
          ]
        }
      }
    },
    "access_rules": {
      "contractors_access_hr": {
        "detected": true,
        "matched": true,
        "action": "reported",
        "name": "Contractors access HR",
        "attributes": {
          "app": {
            "app_id": "hr-chatbot"
          },
          "user": {
            "id": "contractor.dennis.nedry"
          }
        }
      },
      "pii_exposed": {
        "detected": true,
        "matched": true,
        "action": "reported",
        "name": "PII exposed",
        "attributes": {
          "app": {
            "app_id": "hr-chatbot"
          },
          "user": {
            "id": "contractor.dennis.nedry"
          }
        }
      },
      "pii_exposed_to_contractors": {
        "detected": true,
        "matched": true,
        "action": "blocked",
        "name": "PII exposed to Contractors",
        "attributes": {
          "app": {
            "app_id": "hr-chatbot"
          },
          "user": {
            "id": "contractor.dennis.nedry"
          }
        }
      }
    }
  }
}
```

#### Group membership [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/access-rules\#group-membership "Direct link to Group membership")

The following examples show group membership conditions for custom and external identity provider groups.

##### Custom groups [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/access-rules\#custom-groups "Direct link to Custom groups")

AIDR matches group members against the following request parameters.
A match on either field satisfies the condition:

- **User** groups - `user_id` and `extra_info.user_name`
- **Application** groups - `app_id` and `extra_info.app_name`
- **Model** groups - `model` and `llm_provider`

AIDR normalizes request values before matching.
Spaces become underscores.
For example, `Jeffrey Goines` matches `Jeffrey_Goines`.

This rule blocks requests from users who belong to the `patient_room_chatbot` group.
It uses the `user.groups` attribute with the `includes` operator to check group membership.

| Condition | Operator | Value |  |
| --- | --- | --- | --- |
| `Block patient room chatbot users` (rule name) |
| `user.groups` | `includes ▼` | `custom:patient_room_chatbot` | `And +` (add expression) `⊖` (remove expression) |
| `Add Condition +` |
| **Then**`≡``Block and Stop  ▼`<br>**Else**`≡``Continue  ▼` |
| `🗑️` \| `Cancel` \| `Update` |

After you click **Update**, the rule editor displays the rule definition as:

`if (`

`then``Block`

`user.groups includes custom:patient_room_chatbot`

`)`

When this rule matches, the API response includes the access rule result:

Example response from AIDR APIs

```json
{
  ...
  "summary": "Patient room Chatbot matched and blocked.",
  "result": {
    "blocked": true,
    "access_rules": {
      "patient_room_chatbot": {
        "detected": true,
        "matched": true,
        "action": "blocked",
        "name": "Patient room Chatbot"
      }
    }
  }
}
```

When you click the value field for a group membership expression, the editor opens a group browser.
The group browser shows tabs for each available source:

- **Custom** \- Click **Browse Custom Groups** to select a group managed in AIDR.
- **Entra ID** \- Click **Browse Entra ID Groups** to select a group synced from Microsoft Entra ID.
- **Active Directory** \- Click **Browse Active Directory Groups** to select a group synced from Active Directory.

For `app.groups` and `model.groups`, the only available option is **Browse Custom Groups**.

**Browse Custom Groups** opens **Manage Memberships**, where you can create groups or manage group members directly, using the **\+ Create Group** and **Manage Members** buttons.

For more information, see [Memberships](https://aidr-docs.crowdstrike.com/docs/aidr/administration/settings#memberships) in Settings.

##### External identity provider groups [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/access-rules\#external-identity-provider-groups "Direct link to External identity provider groups")

For Entra ID and Active Directory users synced through Falcon Identity Protection, AIDR resolves group membership by matching request `user_id` and `extra_info.user_name` values against the synced user's email, user principal name, and user ID.
AIDR applies the first match.

This rule blocks requests from users who do not belong to a specific Entra ID group.
It uses the `user.groups` attribute with the `excludes` operator to check external group membership.

| Condition | Operator | Value |  |
| --- | --- | --- | --- |
| `Block non-DNS Admins` (rule name) |
| `user.groups` | `excludes ▼` | `entra:d753f19e-0dcc-4697-a878-8faecf5513f8` | `And +` (add expression) `⊖` (remove expression) |
| `Add Condition +` |
| **Then**`≡``Block and Stop  ▼`<br>**Else**`≡``Continue  ▼` |
| `🗑️` \| `Cancel` \| `Update` |

After you click **Update**, the rule editor displays the rule definition as:

`if (`

`then``Block`

`user.groups excludes entra:d753f19e-0dcc-4697-a878-8faecf5513f8`

`)`

When this rule matches, the API response includes the access rule result:

Example response from AIDR APIs

```json
{
  ...
  "summary": "Block non-DNS Admins matched and blocked.",
  "result": {
    "blocked": true,
    "access_rules": {
      "block_non_dns_admins": {
        "detected": true,
        "matched": true,
        "action": "blocked",
        "name": "Block non-DNS Admins"
      }
    }
  }
}
```

#### Identity provider attributes [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/access-rules\#idp-attributes "Direct link to Identity provider attributes")

You can create access rule conditions based on user attributes synced from external identity providers.
AIDR resolves the user's identity provider record by matching the request `user_id` and `extra_info.user_name` values against the synced user's email, user principal name, and user ID.
AIDR applies the first match.

To create a condition based on an identity provider attribute:

1. Click the attribute field and select `User` \> `idp attributes`.
2. Select `entra id` or `active directory`.
3. Select a specific attribute (for example, `department`).
4. Select a comparison operator.
5. Enter the comparison value.

The attribute path in the rule expression is `user.idp.entra.<attribute>` for Entra ID or `user.idp.ad.<attribute>` for Active Directory.

The following rule blocks requests from users whose Entra ID `department` attribute equals `Users`.

| Condition | Operator | Value |  |
| --- | --- | --- | --- |
| `Block regular users` (rule name) |
| `user.idp.entra.department` | `== ▼` | `Users` | `And +` (add expression) `⊖` (remove expression) |
| `Add Condition +` |
| **Then**`≡``Block and Stop  ▼`<br>**Else**`≡``Continue  ▼` |
| `🗑️` \| `Cancel` \| `Update` |

After you click **Update**, the rule editor displays the rule definition as:

`if (`

`then``Block`

`user.idp.entra.department == Users`

`)`

When this rule matches, the API response includes the access rule result:

Example response from AIDR APIs

```json
{
  ...
  "summary": "Block regular users matched and blocked.",
  "result": {
    "blocked": true,
    "access_rules": {
      "block_regular_users": {
        "detected": true,
        "matched": true,
        "action": "blocked",
        "name": "Block regular users"
      }
    }
  }
}
```

For more information, see [Users](https://aidr-docs.crowdstrike.com/docs/aidr/administration/settings#users) in Settings.

### Rule execution order [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/access-rules\#rule-execution-order "Direct link to Rule execution order")

AIDR evaluates rules in the order they appear.

You can change the order by dragging rules with their six-dot handle.

### Save policy changes [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/access-rules\#save-policy-changes "Direct link to Save policy changes")

After you change a policy, click **Save Changes** in the action bar to apply your changes.
If you navigate away without saving, AIDR prompts you to save or discard your changes.

## Default action [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/access-rules\#default-action "Direct link to Default action")

If no access rules match, AIDR evaluates configured prompt rules.

tip:

Test access rules in the [Sandbox](https://aidr-docs.crowdstrike.com/docs/aidr/policies/testing#sandbox) on the policy page, or in the [Playground](https://aidr-docs.crowdstrike.com/docs/aidr/policies/testing#playground) on the **Application** collector page.

- [Assistant](https://aidr-docs.crowdstrike.com/docs/aidr/policies/access-rules#assistant)
- [Access rules editor](https://aidr-docs.crowdstrike.com/docs/aidr/policies/access-rules#access-rules-editor)
  - [Add access rule](https://aidr-docs.crowdstrike.com/docs/aidr/policies/access-rules#add-access-rule)
  - [Edit access rule](https://aidr-docs.crowdstrike.com/docs/aidr/policies/access-rules#edit-access-rule)
  - [Configure action settings](https://aidr-docs.crowdstrike.com/docs/aidr/policies/access-rules#action-settings)
    - [Tag events](https://aidr-docs.crowdstrike.com/docs/aidr/policies/access-rules#tag-events)
    - [Exclude prompt content](https://aidr-docs.crowdstrike.com/docs/aidr/policies/access-rules#exclude-prompt-content)
  - [Custom block messages](https://aidr-docs.crowdstrike.com/docs/aidr/policies/access-rules#block-messages)
  - [Examples](https://aidr-docs.crowdstrike.com/docs/aidr/policies/access-rules#examples)
    - [Request metadata](https://aidr-docs.crowdstrike.com/docs/aidr/policies/access-rules#request-metadata)
    - [Request metadata and prompt rules](https://aidr-docs.crowdstrike.com/docs/aidr/policies/access-rules#request-metadata-and-prompt-rules)
    - [Custom Entity rule reference](https://aidr-docs.crowdstrike.com/docs/aidr/policies/access-rules#custom-entity-specific-rule-reference)
    - [Rules matched reference](https://aidr-docs.crowdstrike.com/docs/aidr/policies/access-rules#rules-matched-reference)
    - [Group membership](https://aidr-docs.crowdstrike.com/docs/aidr/policies/access-rules#group-membership)
      - [Custom groups](https://aidr-docs.crowdstrike.com/docs/aidr/policies/access-rules#custom-groups)
      - [External identity provider groups](https://aidr-docs.crowdstrike.com/docs/aidr/policies/access-rules#external-identity-provider-groups)
    - [Identity provider attributes](https://aidr-docs.crowdstrike.com/docs/aidr/policies/access-rules#idp-attributes)
  - [Rule execution order](https://aidr-docs.crowdstrike.com/docs/aidr/policies/access-rules#rule-execution-order)
  - [Save policy changes](https://aidr-docs.crowdstrike.com/docs/aidr/policies/access-rules#save-policy-changes)
- [Default action](https://aidr-docs.crowdstrike.com/docs/aidr/policies/access-rules#default-action)
