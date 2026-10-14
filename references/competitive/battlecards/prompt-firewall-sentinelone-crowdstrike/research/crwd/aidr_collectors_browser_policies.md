Scrape ID: 01a1361d-7777-7388-ba23-c849c4dfb21e
[Skip to main content](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/policies#__docusaurus_skipToContent_fallback)

AI Detection and Response reaches end of support on November 30, 2026. AIDR capabilities continue in [Falcon Guardian](https://docs.crowdstrike.com/access?ft:originId=dt55byd3) with expanded AI security.

On this page

## Policy Evaluation and Detections [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/policies\#policy-evaluation-and-detections "Direct link to Policy Evaluation and Detections")

When a browser collector sends captured AI activity to AIDR, the service evaluates the data against rules defined in the collector policy.
The resulting detections are logged for visibility, investigation, and integration with other security workflows.

### Input Rules [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/policies\#input-rules "Direct link to Input Rules")

You can use browser collectors to enforce input rules that block or redact sensitive data before it reaches the AI provider.

### Output Rules [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/policies\#output-rules "Direct link to Output Rules")

You can use browser collectors to detect threats in AI responses, but they can't modify what users see.

Output rules automatically run in

[Report Only Mode](https://aidr-docs.crowdstrike.com/docs/aidr/policies/inspection-rules#report-only-mode), with only `Report` and `Alert` actions available.
AIDR logs detections without affecting the user experience.

### Format Preserving Encryption (FPE) in browser collectors [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/policies\#format-preserving-encryption-fpe-in-browser-collectors "Direct link to Format Preserving Encryption (FPE) in browser collectors")

Format Preserving Encryption (FPE) encrypts sensitive values while preserving their format (length, character types, delimiter positions).
This prevents sensitive data leakage while allowing users to submit meaningful prompts.
For example, a phone number like `(555) 123-4567` encrypts to `(842) 967-3201`.
The format stays recognizable while the original number is protected.

When you apply [FPE redaction](https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules#format-preserving-encryption-fpe) in input rules:

1. Browser collectors encrypt sensitive data before submitting it to the AI provider.
2. If the AI provider includes the encrypted data in its response, users see the encrypted version in the same format.

For example, if a user submits SSN `234-56-7890`, FPE encrypts it to `987-65-4321`.
When the AI responds with "Your SSN 987-65-4321 cannot be verified", the user sees the encrypted value instead of the original.

note:

Browser collectors can't unredact FPE-encrypted values that appear in AI provider responses.

tip:

Use other redaction methods (replacement or mask) to make it clear that values were redacted - for example, `<US_SSN>` or `***-**-7890`.

- [Policy Evaluation and Detections](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/policies#policy-evaluation-and-detections)
  - [Input Rules](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/policies#input-rules)
  - [Output Rules](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/policies#output-rules)
  - [Format Preserving Encryption (FPE) in browser collectors](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/policies#format-preserving-encryption-fpe-in-browser-collectors)
