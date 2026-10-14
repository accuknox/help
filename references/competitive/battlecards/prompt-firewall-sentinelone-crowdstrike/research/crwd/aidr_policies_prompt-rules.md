Scrape ID: 01a1361d-73eb-747f-92b7-3a9b4f1cba38
[Skip to main content](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#__docusaurus_skipToContent_fallback)

AI Detection and Response reaches end of support on November 30, 2026. AIDR capabilities continue in [Falcon Guardian](https://docs.crowdstrike.com/access?ft:originId=dt55byd3) with expanded AI security.

On this page

Prompt rules inspect and act on the content of requests and responses that your collector intercepts from AI systems.

You can define a separate set of rules under each inspection rule in your policy.

You can configure prompt rules by enabling and adjusting

[detectors](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#detectors).

## Enable detector [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules\#enable-detector "Direct link to Enable detector")

If you haven't enabled any detectors, the **No Prompt Rules Enabled** section displays a list of detector buttons.

To enable a detector, click its button.
The button highlights and the section label changes to **Execute Prompt Rules**.

The enabled detector appears as an expandable card showing the detector name and assigned actions: `Report`, `Transform`, or `Block`.

To disable a detector, click its highlighted button.

## Configure detector [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules\#configure-detector "Direct link to Configure detector")

Click the pencil icon to expand the detector card.

In the expanded detector card, configure the detector rules and assign an action to each rule.
Available options depend on the detector type.

tip:

For available actions per detector type, see [Detectors](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#detectors) and [Actions](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#actions).

### Configure detector rules [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules\#configure-detector-rules "Direct link to Configure detector rules")

Each detector identifies a specific risk type, such as PII exposure, malicious entities, prompt injection, or toxic content.
When the detector identifies a threat, it applies the configured action.

#### Single-rule detectors [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules\#single-rule-detectors "Direct link to Single-rule detectors")

Some detectors include a single rule that applies one action.
A single-rule detector provides controls, such as toggles or sliders, to customize rule behavior.

Example:

The **Malicious Prompt** detector reports or blocks prompts with detected adversary intents.

You can configure the malicious prompt rule to detect prompt injection attempts.
To improve detection accuracy, provide additional context with examples of benign and malicious prompts.

#### Detectors with multiple rules [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules\#detectors-with-multiple-rules "Direct link to Detectors with multiple rules")

Some detectors include multiple rules, each targeting a specific data type within a broader risk category:

- [Malicious Entity](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#malicious-entity) \- Includes predefined rules for detecting malicious IP addresses, URLs, and domains.
- [Confidential and PII Entity](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#confidential-and-pii) and [Secret and Key Entity](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#secret-and-key-entity) \- Let you select from predefined redaction rules and configure each rule individually.
- [Custom Entity](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#custom-entity) \- Lets you create and apply custom rules based on text patterns.
Click **\+ Custom Rule** to create a rule.

Example:

The **Confidential and PII Entity** detector identifies and acts on personal identifiers, credit card numbers, email addresses, locations, and other sensitive data types.
You can configure and test a separate rule for each data type in the detector.

##### Add rule [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules\#add-rule "Direct link to Add rule")

1. Click the down-pointing triangle icon next to the **Rules** label in the expanded detector card.
2. In the list of available rules, select the checkbox for each rule you want to enable.
3. Click **Add**.

##### Remove or edit rule [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules\#remove-or-edit-rule "Direct link to Remove or edit rule")

Click the menu icon in the rule row.

- Click **Edit** to open **Edit Rule**.
Configure the rule and test it with **Test Rules**.

Click **Update** to apply the changes.

- Click **Delete** to remove the rule from the detector configuration.


#### Add regex matchers [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules\#add-regex-matchers "Direct link to Add regex matchers")

In the [Custom Entity](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#custom-entity) detector, you can define rules with regex matchers that follow

[RE2 syntax](https://github.com/google/re2/wiki/Syntax).
RE2 guarantees linear-time matching. This prevents patterns from causing timeouts on large inputs.

To add a regex matcher to a Custom Entity rule:

1. In **Edit Rule**, click **\+ Add Match** or click an existing matcher.
2. Select **Regex** as the **Match Type**.
3. Enter a regular expression in RE2 syntax.
4. Click **Test Rules** to validate the expression and verify match behavior.

RE2 syntax:

RE2 doesn't support the following constructs:

- Lookahead and lookbehind
- Backreference
- Some Perl-specific syntax extensions

For supported syntax elements, see the Google article [RE2 syntax reference](https://github.com/google/re2/wiki/Syntax).

Upgrading existing rules:

If a Custom Entity rule contains a regex pattern created before RE2 support, the console prompts you to upgrade the pattern when you save.
After upgrading, verify the pattern behavior with **Test Rules**.

### Assign rule action [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules\#assign-rule-action "Direct link to Assign rule action")

In the action dropdown next to the rule name, select the action to apply when the rule conditions match.
For single-rule detectors, this dropdown is labeled **Set action**.

### Apply detector changes [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules\#apply-detector-changes "Direct link to Apply detector changes")

- Click **Update** to apply your changes.
- Click **Cancel** to discard your changes and close the rule editor.
- Click the delete icon to reset all saved customizations for the detector.

tip:

- Disabling a detector by clicking its highlighted button removes it from the policy but preserves your configuration.
- Using the delete icon resets the detector to its defaults.

### Save policy changes [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules\#save-policy-changes "Direct link to Save policy changes")

After you change a policy, click **Save Changes** in the action bar to apply your changes.
If you navigate away without saving, AIDR prompts you to save or discard your changes.

## Test prompt rules [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules\#test-prompt-rules "Direct link to Test prompt rules")

You can test your enabled prompt rules in the **Sandbox** tab on the policy page.
To verify how the policy processes a detection, type a message that triggers an enabled detector.

For details and examples, see [Policy Testing > Sandbox](https://aidr-docs.crowdstrike.com/docs/aidr/policies/testing#sandbox).

## Detectors [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules\#detectors "Direct link to Detectors")

You can enable these detectors in prompt rules:

note:

Not all inspection rules and policy types enforce every action. You can enforce Block, Redact, and Defang actions that block a request or transform its data depending on where the inspection rule runs.

For more info, see [Actions](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#actions).

### Malicious Prompt [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules\#malicious-prompt "Direct link to Malicious Prompt")

Detect attempts to manipulate AI behavior with adversarial inputs.

Supported actions:

- [Report](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#report)
- [Block](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#block)

Additional configuration:

- **Generic Prompt Injection and Jailbreak Detection** \- Detect attempts to manipulate AI system behavior.

- **Custom Benign Prompt Detection** \- Provide examples of benign prompts for better accuracy.
- **Custom Malicious Prompt Detection** \- Provide examples of malicious prompts for better accuracy.

### Malicious Entity [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules\#malicious-entity "Direct link to Malicious Entity")

Detect harmful references for three malicious entity types:

- **IP Address**
- **URL**
- **Domain**

You can assign an action to each type:

- [Report](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#report)
- [Defang](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#defang)
- [Block](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#block)
- [Disabled](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#disabled)

### MCP Validation [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules\#mcp-validation "Direct link to MCP Validation")

Detect tool poisoning and other security issues in MCP tool definitions.
Collectors submit these definitions in the `tools` parameter of requests to AIDR APIs.

The detector identifies the following threat types:

- Malicious prompt in tool description - Detect malicious instructions embedded in tool descriptions, such as attempts to exfiltrate system prompts or manipulate model behavior.
- Conflicting tool names - Detect duplicate tool names that can cause the model to invoke an unintended tool.
- Conflicting tool descriptions - Detect tools with similar descriptions that indicate a spoofing attempt.

For example payloads and responses, see [APIs](https://aidr-docs.crowdstrike.com/docs/aidr/apis#tools-array-optional---array-of-tools-available-to-the-llm-for-function-calling).

Supported actions:

- [Report](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#report)
- [Block](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#block)

Additional configuration:

- **Similarity threshold** \- Lower the threshold to increase sensitivity, or raise it to require higher confidence for a detection. Drag the slider to adjust.

### Confidential and PII Entity [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules\#confidential-and-pii "Direct link to Confidential and PII Entity")

Detect personally identifiable information (PII) and other confidential data, such as **Email Address**, **US Social Security Number**, **Credit Card**, **Passport**, and **Driver License**.

You can add individual rules for each supported data type, as described in [Detectors with multiple rules](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#detectors-with-multiple-rules), and apply an action to each rule:

- [Block](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#block)
- [Replacement](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#replacement)
- [Mask (<\*\*\*\*>)](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#mask)
- [Partial Mask (\*\*\*\*xxxx)](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#partial-mask)
- [Report](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#report)
- [Hash](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#hash)
- [Format Preserving Encryption (FPE)](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#format-preserving-encryption-fpe)

### Secret and Key Entity [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules\#secret-and-key-entity "Direct link to Secret and Key Entity")

Detect sensitive credentials, such as API keys and encryption keys.

You can add individual rules for each supported secret type, as described in [Detectors with multiple rules](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#detectors-with-multiple-rules), and apply an action to each rule:

- [Block](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#block)
- [Replacement](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#replacement)
- [Mask](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#mask)
- [Partial Mask](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#partial-mask)
- [Report](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#report)
- [Hash](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#hash)
- [Format Preserving Encryption (FPE)](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#format-preserving-encryption-fpe)

### Language [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules\#language "Direct link to Language")

Detect text language and apply language-based security policies.

You can configure two actions for language detection:

- Select a blocking behavior for detected languages:
  - [Block](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#block) \- Block list.
    Specify the languages to block in requests to the AI system.
  - [Block all except](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#block-all-except) \- Allow list.
    Specify the languages allowed in requests to the AI system.
- Select a reporting behavior for detected languages:
  - [Report](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#report) \- Report the specified languages.
  - [Report all except](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#report-all-except) \- Report all detected languages except the ones you specify.

Additional configuration:

- **Ignore unclassified languages** \- Enable to prevent the configured actions from triggering on text that cannot be classified.
Unclassified languages include unknown languages and text that is not long enough to classify as a language.

This option applies when using the following actions:
  - `Block all except`
  - `Report all except`
- **Similarity threshold** \- Lower the threshold to increase sensitivity, or raise it to require higher confidence for a detection. Drag the slider to adjust.

- **Report secondary detected languages** \- Enable to report languages detected in text fragments that do not qualify as primary.
When a text is primarily in one language but contains fragments in others, those fragments are reported as secondary languages.
When enabled, all secondary languages are reported regardless of the language lists configured in the block or report actions.

- **Minimum word count for primary language classification** \- Languages spanning fewer than this many words are treated as secondary detections.
Lower values mean more languages qualify as primary; higher values mean only languages with a longer presence qualify as primary.
A language is classified as primary if it exceeds either this threshold or the text coverage minimum.

- **Minimum text coverage for primary language classification** \- Languages covering less than this percentage of total text are treated as secondary detections.
Lower values mean more languages qualify as primary; higher values mean only dominant languages qualify as primary.
A language is classified as primary if it exceeds either this threshold or the word count minimum.


Example report from the Language detector

```json
{
  ...
  "status": "Success",
  "summary": "Language was detected and reported.",
  "result": {
    "blocked": false,
    "transformed": false,
    "policy": "k_t_boundary_input_policy",
    "detectors": {
      "language": {
        "detected": true,
        "data": {
          "action": "report",
          "languages": [\
            {\
              "language": "en",\
              "confidence": 1,\
              "action": "reported",\
              "category": "primary"\
            },\
            {\
              "language": "ru",\
              "confidence": 0.99,\
              "action": "reported",\
              "category": "secondary",\
              "text": "Аналитическая лента угроз выявила эти фишинговые атаки за последние 24 часа."\
            }\
          ]
        }
      }
    }
  }
}
```

### Code [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules\#code "Direct link to Code")

Detect attempts to insert executable code into AI interactions.

Supported actions:

- [Report](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#report)
- [Block](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#block)

Additional configuration:

- **Confidence threshold** \- Lower the threshold to increase sensitivity, or raise it to require higher confidence for a detection. Drag the slider to adjust.

### Competitors [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules\#competitors "Direct link to Competitors")

Detect mentions of competing brands or entities.

You can define a list of competitor names to detect.
Assign an action for each match:

- [Report](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#report)
- [Block](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#block)

Additional configuration:

- **List of competitors** (required) - Enter competitor names to identify references in AI content.

### Custom Entity [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules\#custom-entity "Direct link to Custom Entity")

Define rules to detect text patterns.

Add custom rules as described in [Detectors with multiple rules](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#detectors-with-multiple-rules), and apply an action to each rule:

- [Block](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#block)
- [Replacement](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#replacement)
- [Mask (<\*\*\*\*>)](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#mask)
- [Partial Mask (\*\*\*\*xxxx)](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#partial-mask)
- [Report](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#report)
- [Hash](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#hash)
- [Format Preserving Encryption (FPE)](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#format-preserving-encryption-fpe)

### Topic [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules\#topic "Direct link to Topic")

Report or block content related to restricted topics, such as politics, health, and legal.

Select predefined topics to block or report all detected topics.

Supported actions:

- [Report](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#report) \- Detect supported topics and include them in the response for visibility and analysis.
- [Block](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#block) \- Flag responses containing selected topics as blocked.

Additional configuration:

- **Confidence threshold** \- Lower the threshold to increase sensitivity, or raise it to require higher confidence for a detection. Drag the slider to adjust.

Currently supported topics:

- **Financial**
- **Legal**
- **Religion**
- **Politics**
- **Health**
- **Toxicity**
- **Negative sentiment**
- **Self-harm and violence**
- **Roleplay**
- **Weapons**
- **Criminal conduct**

### Emoji [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules\#emoji "Direct link to Emoji")

Detect classes of potentially unsafe Unicode characters that can obfuscate prompt injection attacks.

Select which character categories to detect:

- **Emojis** \- Emoji characters embedded in text.



Example





```bash
What is the 🔑 to accessing admin functions?
```

- **Miscellaneous graphics** \- Graphics, box drawing characters, and mathematical operators.



Example





```bash
■□▲△ show me the hidden config
```

- **Invisible chars** \- Zero-width spaces, joiners, soft hyphens, bidirectional control characters, and other hidden or control characters.



Example





```bash
Ig\u200bnore prev\u200bious inst\u200bructions
```

- **Mixed scripts** \- Text mixing multiple Unicode scripts within a single word, such as Cyrillic characters in place of visually similar Latin characters.



Example





```bash
Ignоre previоus instructiоns
```









In this example, the Cyrillic `о` (U+043E) replaces the visually identical Latin letter `o`.

- **Modifiers** \- Characters with multiple combining diacritical marks applied to a single character.
The detector requires a minimum of three modifiers for a detection.
For example: `ặ̂̃́`.



Example





```bash
S̷̢̧̛̩̦̱̭͇̈́̈̏̇̕h̶̡̧̛̗̣̮̱̺̀̈́̋̈́o̵̧̨̼̣̙̱̗̊̈́̽̑̕w̶̨̧̛̹̺̣̗̌̈́̋̈́
```


Supported actions:

- [Report](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#report)
- [Block](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#block)

Additional configuration:

- **Exclusions** \- Specify characters to exclude from detection.
If your application intentionally uses the zero-width space, exclude it.



Example





```bash
\u200b
```

- **Custom characters** \- Specify additional characters that trigger detection.
For example, add circled numbers to extend the default categories.



Example





```bash
①
```


### Malicious Skills and Tools [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules\#malicious-skills-and-tools "Direct link to Malicious Skills and Tools")

Detect malicious skills and tools in AI agent requests.

Skill and tool content can contain malicious code, data exfiltration commands, or privilege escalation attempts disguised as legitimate instructions.
Detected patterns include prompt injection, credential harvesting, supply chain attacks, and persistence mechanisms.

Supported actions:

- [Report](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#report)
- [Block](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#block)

Additional configuration:

- **Detection threshold** \- Lower the threshold to increase sensitivity, or raise it to require higher confidence for a detection. Drag the slider to adjust.

## Actions [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules\#actions "Direct link to Actions")

You can configure each detector to apply one of these actions when it triggers:

- Report the detection.
- Transform detected text by redacting or encrypting it before AIDR returns the result to the collector.
- Mark the request as blocked.

note:

Blocking actions can prevent subsequent detectors from running and improve performance.

warning:

In **Report Only Mode**, actions are not enforced in real time:

- User experience is not affected.
- `Block` actions appear as `Alert`. AIDR logs the event but the request proceeds. AIDR sets the **Status** field in logs to `Alerted`.
- **Transform** actions apply only to logged content for analysis. Users see original, unmodified values. AIDR sets the **Status** field in logs to `Reported`.

For more information, see [Report Only Mode](https://aidr-docs.crowdstrike.com/docs/aidr/policies/inspection-rules#report-only-mode).

### Block [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules\#block "Direct link to Block")

Flag the request as blocked.

note:

A blocking action can halt execution early and remaining detectors don't run.

#### Enforcement [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules\#enforcement "Direct link to Enforcement")

AIDR always evaluates blocking rules and logs the result. However, inline enforcement depends on where the rule executes:

- **Falcon Endpoint:**
  - Browser input inspection rules can enforce blocking.

  - Other endpoint inspection rules always run in **Report Only Mode**.
    AIDR logs the detection but doesn't block the request, and the `Block` action appears as [Alert](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#alert).

    For more information, see [Report Only Mode](https://aidr-docs.crowdstrike.com/docs/aidr/policies/inspection-rules#report-only-mode).
- **Other Collectors:**
  - **AI Gateway** and **Application** collectors can enforce blocking.
  - Browser input inspection rules can enforce blocking.
  - **Logging** collectors process events asynchronously and don't enforce any actions.
  - Other collectors provide various support for enforcement depending on the event type.

#### AIDR API response [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules\#aidr-api-response "Direct link to AIDR API response")

AIDR sets the top-level `blocked` property to `true`.
The collector should stop processing the request.

The following collectors automatically enforce the blocking action:

- Browser collectors - for input events only
- Gateway collectors
- Agentic collectors

#### AIDR logs [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules\#aidr-logs "Direct link to AIDR logs")

AIDR sets the `status` field to `blocked`.
The log **Summary** and **Findings** fields reflect the blocking action.

#### Custom block messages [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules\#block-messages "Direct link to Custom block messages")

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

### Alert [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules\#alert "Direct link to Alert")

When an inspection rule runs in [Report Only Mode](https://aidr-docs.crowdstrike.com/docs/aidr/policies/inspection-rules#report-only-mode), the **Block** action appears as **Alert** and the color indicator changes from red to orange.
AIDR logs the event, but the request proceeds and users aren't interrupted.

For more information, see [Report Only Mode](https://aidr-docs.crowdstrike.com/docs/aidr/policies/inspection-rules#report-only-mode).

### Block all except [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules\#block-all-except "Direct link to Block all except")

Allow input only in the languages specified in the [Language](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#language) detector settings.

### Defang [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules\#defang "Direct link to Defang")

Modify malicious IP addresses, URLs, or domains to prevent accidental clicks or execution.
Defanged values remain readable for analysis.
For example, a defanged IP address: `47[.]84[.]32[.]175`.

#### AIDR API response [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules\#aidr-api-response-1 "Direct link to AIDR API response")

AIDR sets the top-level `transformed` property to `true`.

#### AIDR logs [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules\#aidr-logs-1 "Direct link to AIDR logs")

AIDR sets the `status` field to `transformed`.

AIDR saves the transformed data in the **Guard Output** and **Findings** fields.

#### Custom defang messages [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules\#custom-defang-messages "Direct link to Custom defang messages")

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

### Disabled [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules\#disabled "Direct link to Disabled")

Disable processing for a specific rule in multi-rule detectors.

### Report [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules\#report "Direct link to Report")

Report the detection in AIDR logs without acting on the detected content.
AIDR doesn't affect user interactions with the AI system.

### Report all except [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules\#report-all-except "Direct link to Report all except")

Report all detected languages except the ones you specify in the [Language](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#language) detector settings.

### Redact actions [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules\#redact-actions "Direct link to Redact actions")

Redact actions transform detected text before AIDR returns it to the collector.
You can assign redact actions to rules in the following detectors:

- [Confidential and PII Entity](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#confidential-and-pii)
- [Secret and Key Entity](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#secret-and-key-entity)
- [Custom Entity](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#custom-entity)

When you apply a redact action:

#### AIDR API response [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules\#aidr-api-response-2 "Direct link to AIDR API response")

AIDR sets the top-level `transformed` property to `true`.

#### AIDR logs [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules\#aidr-logs-2 "Direct link to AIDR logs")

AIDR sets the `status` field to `transformed`.

AIDR saves the transformed data in **Guard Output**. The **Summary** and **Findings** fields note the applied transformation.

#### Custom redact messages [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules\#custom-redact-messages "Direct link to Custom redact messages")

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

#### Actions [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules\#redact-actions-list "Direct link to Actions")

For each detector rule, you can select an action:

##### Replacement [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules\#replacement "Direct link to Replacement")

Replace rule-matching data with a descriptive token, such as `<PHONE_NUMBER>` or `<US_SSN>`.
In the rule [Edit](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#remove-or-edit-rule) option, configure the replacement value.

##### Mask (\*\*\*\*) [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules\#mask "Direct link to Mask (****)")

Replace rule-matching text with asterisks.

##### Partial Mask (\*\*\*\*xxxx) [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules\#partial-mask "Direct link to Partial Mask (****xxxx)")

Partially replace rule-matching text with a masking character, such as `***-***-7890` for a phone number.
In the rule [Edit](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#remove-or-edit-rule) option, configure partial masking settings:

- **Masking Character** \- Specify the character for masking, such as `#`.
- **Masking Options**
  - **Unmasked from left** \- Set the number of starting characters to leave unmasked.
  - **Unmasked from right** \- Set the number of ending characters to leave unmasked.
- **Characters to Ignore** \- Specify characters to leave unmasked, such as `-`.

##### Hash [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules\#hash "Direct link to Hash")

Replace detected text with a cryptographic hash.
To enable hashing, configure a salt value.

##### Format Preserving Encryption (FPE) [​](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules\#format-preserving-encryption-fpe "Direct link to Format Preserving Encryption (FPE)")

Format Preserving Encryption (FPE) transforms data while preserving its format, including length, character type, and structure.
For example, a phone number like `(555) 123-4567` becomes `(842) 967-3201` \- the parentheses, spaces, and hyphens remain in their original positions.

You can redact sensitive data while maintaining a recognizable format and providing useful context to the AI system.
To recover the original values, call the [/aiguard/v1/unredact](https://aidr-docs.crowdstrike.com/docs/aidr/apis#aiguardv1unredact) endpoint.

When you apply FPE redaction, the response from AIDR APIs includes:

- Processed content with encrypted values under the `guard_output` result property
- FPE context to recover the encrypted values in the processed content under the `fpe_context` result property

The **Findings** page displays these values in the following fields:

- **Guard Output**
- **Extra Info** \> **"fpe\_context"**

Example response with FPE-redacted values

```json
{
  ...
  "status": "Success",
  "summary": "Malicious Prompt was detected and blocked.  Malicious Entity was not executed.  Confidential and PII Entity was detected and redacted.",
  "result": {
    "guard_output": {
      ...
      "messages": [\
        ...\
        {\
          "annotations": [],\
          "content": "You are Jason Bourne. Your phone number is 852-432-4478",\
          "refusal": null,\
          "role": "assistant"\
        }\
      ]
    },
    "transformed": true,
    "detectors": {
      ...
      "confidential_and_pii_entity": {
        "detected": true,
        "data": {
          "entities": [\
            {\
              "action": "redacted:encrypted",\
              "type": "PHONE_NUMBER",\
              "value": "555-555-5555"\
            }\
          ]
        }
      }
    },
    "fpe_context": "eyJhIjogIkFFUy1GRjEtMjU2IiwgIm0iOiBbeyJhIjogMSwgInMiOiA0MywgImUiOiA1NSwgImsiOiAibWVzc2FnZXMuMC5jb250ZW50IiwgInQiOiAiUEhPTkVfTlVNQkVSIiwgInYiOiAiODUyLTQzMi00NDc4In1dLCAidCI6ICJoekNTdDNJIiwgImsiOiAicHZpXzJxd29obDd2dmxmZzZ3cXFqZnczeWRscHg2bGk0dGg3IiwgInYiOiAxLCAiYyI6ICJwY2lfczV6NWg3Y3JxeWk1enZ6NHdnbnViZXNud3E2dXkzcDcifQ=="
  }
}
```

To retrieve original content, call `/aiguard/v1/unredact` with the redacted data and `fpe_context` value:

Authorize requests to AIDR APIs

```bash
export CS_AIDR_BASE_URL="https://api.crowdstrike.com/aidr/aiguard"
export CS_AIDR_TOKEN="pts_s2ngg2...hzwafm" # Collector token
```

Example request to /aiguard/v1/unredact

```bash
curl --location --request POST "$CS_AIDR_BASE_URL/v1/unredact" \
--header "Authorization: Bearer $CS_AIDR_TOKEN" \
--header 'Content-Type: application/json' \
--data-raw '{
  "redacted_data": "You are Jason Bourne. Your phone number is 852-432-4478",
  "fpe_context": "eyJhIjogIkFFUy1GRjEtMjU2IiwgIm0iOiBbeyJhIjogMSwgInMiOiA0MywgImUiOiA1NSwgImsiOiAibWVzc2FnZXMuMC5jb250ZW50IiwgInQiOiAiUEhPTkVfTlVNQkVSIiwgInYiOiAiODUyLTQzMi00NDc4In1dLCAidCI6ICJoekNTdDNJIiwgImsiOiAicHZpXzJxd29obDd2dmxmZzZ3cXFqZnczeWRscHg2bGk0dGg3IiwgInYiOiAxLCAiYyI6ICJwY2lfczV6NWg3Y3JxeWk1enZ6NHdnbnViZXNud3E2dXkzcDcifQ=="
}'
```

Response from /aiguard/v1/unredact

```output
{
  ...
  "status": "Success",
  "summary": "Success. Unredacted 1 item(s) from items",
  "result": {
    "data": "You are Jason Bourne. Your phone number is 555-555-5555"
  }
}
```

In AIDR **Settings** \> **Model Settings** \> **Format-Preserving Encryption**, you can enable **Deterministic Format Preserving Encryption (FPE)**.

You can generate and apply a custom tweak value for FPE redaction in your AIDR organization.

FPE tweak:

A `tweak` enhances encryption security as an additional input alongside the plaintext and encryption key.
The tweak prevents attackers from applying statistical methods to break the encryption.
Different tweak values produce different outputs for the same encryption key and data.
To decrypt the data, you must provide the original tweak value applied during encryption.

A custom tweak ensures deterministic encryption - the same original value produces the same encrypted value on every request.
Without a custom tweak, AIDR generates a random string, and the encrypted value differs on each request.

Whether you use a custom or randomly generated tweak, the API response includes it in the `fpe_context` attribute.
You can recover original content with this value.

- [Enable detector](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#enable-detector)
- [Configure detector](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#configure-detector)
  - [Configure detector rules](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#configure-detector-rules)
    - [Single-rule detectors](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#single-rule-detectors)
    - [Detectors with multiple rules](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#detectors-with-multiple-rules)
      - [Add rule](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#add-rule)
      - [Remove or edit rule](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#remove-or-edit-rule)
    - [Add regex matchers](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#add-regex-matchers)
  - [Assign rule action](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#assign-rule-action)
  - [Apply detector changes](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#apply-detector-changes)
  - [Save policy changes](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#save-policy-changes)
- [Test prompt rules](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#test-prompt-rules)
- [Detectors](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#detectors)
  - [Malicious Prompt](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#malicious-prompt)
  - [Malicious Entity](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#malicious-entity)
  - [MCP Validation](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#mcp-validation)
  - [Confidential and PII Entity](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#confidential-and-pii)
  - [Secret and Key Entity](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#secret-and-key-entity)
  - [Language](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#language)
  - [Code](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#code)
  - [Competitors](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#competitors)
  - [Custom Entity](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#custom-entity)
  - [Topic](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#topic)
  - [Emoji](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#emoji)
  - [Malicious Skills and Tools](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#malicious-skills-and-tools)
- [Actions](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#actions)
  - [Block](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#block)
    - [Enforcement](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#enforcement)
    - [AIDR API response](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#aidr-api-response)
    - [AIDR logs](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#aidr-logs)
    - [Custom block messages](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#block-messages)
  - [Alert](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#alert)
  - [Block all except](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#block-all-except)
  - [Defang](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#defang)
    - [AIDR API response](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#aidr-api-response-1)
    - [AIDR logs](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#aidr-logs-1)
    - [Custom defang messages](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#custom-defang-messages)
  - [Disabled](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#disabled)
  - [Report](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#report)
  - [Report all except](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#report-all-except)
  - [Redact actions](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#redact-actions)
    - [AIDR API response](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#aidr-api-response-2)
    - [AIDR logs](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#aidr-logs-2)
    - [Custom redact messages](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#custom-redact-messages)
    - [Actions](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#redact-actions-list)
      - [Replacement](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#replacement)
      - [Mask (\*\*\*\*)](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#mask)
      - [Partial Mask (\*\*\*\*xxxx)](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#partial-mask)
      - [Hash](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#hash)
      - [Format Preserving Encryption (FPE)](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#format-preserving-encryption-fpe)
