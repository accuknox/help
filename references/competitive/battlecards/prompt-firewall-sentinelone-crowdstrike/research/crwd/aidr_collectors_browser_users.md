Scrape ID: 01a1361d-77ed-732e-bdc5-629c6574da39
[Skip to main content](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/users#__docusaurus_skipToContent_fallback)

AI Detection and Response reaches end of support on November 30, 2026. AIDR capabilities continue in [Falcon Guardian](https://docs.crowdstrike.com/access?ft:originId=dt55byd3) with expanded AI security.

On this page

## User experience [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/users\#user-experience "Direct link to User experience")

### When prompts are blocked [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/users\#when-prompts-are-blocked "Direct link to When prompts are blocked")

When the browser collector blocks a user prompt, the user sees a banner that includes:

- Message indicating that the prompt was blocked
- Request ID that users can copy and provide to Support

For example:

> Malicious Prompt was detected and blocked.
>
> Request ID: prq\_b6m7di4yao3lc4q75j5lddx5y7licu5v **⧉**

### When data is transformed [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/users\#when-data-is-transformed "Direct link to When data is transformed")

When the browser collector transforms data, the AI provider receives redacted sensitive values and defanged malicious URLs, IP addresses, and domains.
Some sites might show the original user input in the chat history.

Users see a banner message that includes:

- Message indicating that sensitive data was redacted or malicious references were defanged
- Request ID that users can copy and provide to Support

For example:

> Your organization's security policy modified sensitive or malicious content before sending it to the AI provider.
>
> Request ID: prq\_b6m7di4yao3lc4q75j5lddx5y7licu5v **⧉**

Users see transformed values in AI responses when the model repeats those values in its output.

### Custom messages [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/users\#custom-messages "Direct link to Custom messages")

By default, the banner displays a standard message in a popup.
You can replace this with a custom message to provide context relevant to your organization.
For example, include a link to an internal acceptable-use policy or instructions for requesting an exception.
You can also disable the popup.

To configure custom block and transform messages, see the following documentation:

- [Access Rules - Custom block messages](https://aidr-docs.crowdstrike.com/docs/aidr/policies/access-rules#block-messages)
- [Prompt Rules - Custom block messages](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#block-messages)
- [Prompt Rules - Custom defang messages](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#custom-defang-messages)
- [Prompt Rules - Custom redact messages](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#custom-redact-messages)

### Inconsistent behavior across AI provider sites [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/users\#inconsistent-behavior-across-ai-provider-sites "Direct link to Inconsistent behavior across AI provider sites")

AI provider sites handle AIDR security interventions differently based on their client-side web processing.
These implementations can change at any time, are outside AIDR's control, and might result in inconsistent user experiences across platforms.

#### Example [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/users\#example "Direct link to Example")

The ChatGPT conversation interface captures user input and updates chat history based on what the AI model processed.
Depending on how AIDR processes user input, the displayed conversation might not match what the user originally entered:

- When AIDR transforms data in a user prompt:


1. The user enters a prompt containing sensitive data.
2. ChatGPT adds the user input to the chat interface.
     The input briefly appears unchanged until ChatGPT updates it based on the model's response.
3. The AIDR browser collector intercepts the prompt, processes it, and sends the transformed version to the AI model.
4. ChatGPT receives the model response and:
     - Updates the user prompt displayed in the chat interface with the actual prompt received by the model.
     - Adds the model response to the chat history.

Example exchange:

  - The user enters: "Do you know the Muffin Man?"
  - The user's input is added to the chat history unmodified: "Do you know the Muffin Man?"
  - AIDR's **Confidential and PII Entity** detector replaces the person name with a placeholder before sending the prompt to the AI model.
  - When the model responds:
    - The AIDR browser extension shows a [banner message](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/users#when-data-is-transformed).
    - The user input in the chat history becomes "Do you know <PERSON>".
    - The model response is added to the chat history and might read: "I do not know who <PERSON> is from that message..."

- When AIDR blocks a user prompt, the behavior differs because no content reaches the AI model:
1. The user enters a prompt that AIDR blocks - for example, a prompt with harmful intent detected by the **Malicious Prompt** detector.
2. ChatGPT adds the user input to the chat interface.
3. The AIDR browser collector intercepts the prompt, processes it, and blocks it from being sent to the model.
4. The AIDR browser extension shows a [banner message](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/users#when-prompts-are-blocked).
5. Because no model response arrives, ChatGPT doesn't update the conversation. The user prompt remains in the chat history and can't be removed or modified.

Other AI providers, such as Claude, Gemini, and enterprise platforms, might handle these scenarios differently due to variations in their client-side implementations.

For example, Claude AI currently behaves like ChatGPT when AIDR transforms a user prompt.
However, when AIDR blocks a prompt, Claude AI doesn't add it to the conversation.

### Report Only Mode [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/users\#report-only-mode "Direct link to Report Only Mode")

If browser collector policy input rules are set to `Report`, or the policy is in [Report Only Mode](https://aidr-docs.crowdstrike.com/docs/aidr/policies/inspection-rules#report-only-mode), the user experience is unaffected.
AIDR logs detections without blocking prompts or modifying data.

note:

[Output rules](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/policies#output-rules) in browser collector policies always run in Report Only Mode.

- [User experience](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/users#user-experience)
  - [When prompts are blocked](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/users#when-prompts-are-blocked)
  - [When data is transformed](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/users#when-data-is-transformed)
  - [Custom messages](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/users#custom-messages)
  - [Inconsistent behavior across AI provider sites](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/users#inconsistent-behavior-across-ai-provider-sites)
    - [Example](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/users#example)
  - [Report Only Mode](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/users#report-only-mode)
