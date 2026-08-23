# The AccuKnox case study layout

Read on 2026-08-23 from the four most recently modified pages on
accuknox.com, through their `.md` twins:

| Page | Shape |
| --- | --- |
| `case-studies/sbom-india-bank` | Anonymised bank, air-gapped SBOM, bold lead-in bullets |
| `case-studies/enterprise-islamic-bank` | Anonymised bank, Azure compliance, plain bullets |
| `case-studies/yoma-fleet` | Named customer, SIEM displacement, plain bullets |
| `case-studies/humata-health` | Named customer, HIPAA and GenAI pipelines |

Refresh with
`python <harness>/scripts/fetch_md.py case-studies/<slug>`.

## What you write and what WordPress adds

Three stat tiles appear on every page, identical every time:

| Tile | Value |
| --- | --- |
| Native Integrations | 37+ |
| Fewer False Positives | 89% |
| Reduced Remediation Time | 91% |

They are platform constants injected by the template. They are **not** the
customer's numbers. Do not write them, and never let a sentence imply the
customer measured 89% fewer false positives unless they actually did and said so.

The **More Case Studies** block at the foot is injected too. Write nothing
after Outcomes.

## The section order

1. **YAML front matter.** Fields listed in `assets/case-study-template.md`.
2. **H1.** `<Customer descriptor> <verb>s <outcome>`. Present tense, active.
   `UAE Islamic Bank Achieves Continuous Cloud Compliance on Azure`.
3. **H2 subtitle.** The quantified version of the same claim.
   `Achieves 300+ Vulnerabilities Detected Across 6 Azure Subscriptions`.
4. **An at-a-glance label row**, optional. Two to four labels with values:
   `Environment`, `Registry`, `Deployment`, `Supported Cloud`, `Integrations`.
5. **DOWNLOAD PDF link**, where marketing produced one.
6. **An intro paragraph**, optional but common. One line of AccuKnox
   positioning, then the customer's situation in two sentences.
7. **H2 Challenges.** Four to six bullets.
8. **H2 Solutions.** Four to six bullets, one per module or workstream.
9. **The quote.** Then the attribution role, then the organisation.
10. **H2 Outcomes.** Four to six bullets, at least three carrying a figure.

Nothing after Outcomes.

## The H1 and subtitle carry the whole page

A buyer scanning the case-studies index reads these two lines and nothing else.
They have to hold the sector, the outcome and ideally the number.

| Weak | Strong |
| --- | --- |
| `Banking Customer Success Story` | `Top #3 Indian Public Sector Bank Operationalises SBOM in an Air-Gapped Environment` |
| `Improved Cloud Security` | `Achieves End-to-End Software Supply Chain Visibility in 1 Week with Zero Internet Connectivity` |
| `Fleet Company Uses AccuKnox` | `Fleet and Leasing Leader Achieves $1B+ in Secured Operations on AWS` |

Title Case for the H1 and the H2 subtitle. This is the one channel that breaks
the sentence-case rule, because every live page does.

## Bullets, two shapes

Pick one shape per page and hold it across all three sections.

**Bold lead-in.** The lead-in names the problem, the sentence carries the fact.
Used by the SBOM page.

```markdown
- **Air-Gapped Infrastructure Constraints.** Banking-grade security policies
  prohibit internet connectivity, ruling out SaaS-based scanning and most
  cloud-native SBOM tools.
```

**Plain sentence.** No lead-in, used where the bullets are already specific.
Used by the Azure and Yoma pages.

```markdown
- No unified visibility across 6 Azure subscriptions to continuously validate
  posture against Azure CIS, PCI, and SOC 2 Type II.
```

Either way, every bullet is a complete sentence. A noun fragment is not a
bullet. Twelve to thirty words each.

## Challenges name the consequence, not only the gap

A challenge bullet that stops at the technical gap has done half the job. Say
what the gap cost the business.

- Gap only: `Container images in ACR were not scanned.`
- Full: `Container images in ACR were not scanned, allowing vulnerable images
  into production without any CVE assessment.`

Four to six of them. Fewer reads thin, more reads like a list of everything
wrong with the customer.

## Solutions name the module and what it did

Use the canonical module name on first mention, then reuse it exactly. CSPM,
KSPM, CWPP, ASPM, CIEM, KIEM, CDR, SIEM, CTEM, DSPM, AI-SPM, AI-DR, Prompt
Firewall, AI Red Teaming, KubeArmor, KnoxGuard.

```markdown
- Deployed CSPM across all 6 Azure subscriptions for continuous benchmarking
  against Azure CIS, PCI, and SOC 2 Type II controls.
```

Verb first, module named, scope stated, purpose stated. Never `leveraged the
platform to improve posture`.

One solution bullet should name the displacement where there was one.
`Deployed AccuKnox SIEM to ingest AWS CloudTrail, VPC Flow Logs, and GuardDuty
events, replacing Wazuh`. That sentence sells harder than any adjective.

## Outcomes carry numbers

At least three of the four to six bullets carry a figure with a unit. The
validator fails the draft otherwise, because a case study without figures is a
testimonial.

```markdown
- **7-day end-to-end deployment** completed in a fully air-gapped, on-premise
  environment.
- **10 projects** scanned with full vulnerability, transitive dependency, and
  license-compliance reporting.
- **5+ BOM types covered** (SBOM, CBOM, AI-BOM, HBOM, OBOM).
- **Regulatory coverage validated** against CERT-In, RBI IT Framework, SSDF,
  and EO 14028.
```

Bold the metric, then finish the sentence. A non-numeric outcome is allowed for
compliance coverage and for the qualitative win, but never for more than two of
them.

## The quote

One quote, two or three sentences, in the customer's voice. It names what
changed, not how great the vendor is.

```markdown
“AccuKnox gave us a complete picture of our software supply chain inside a
fully air-gapped environment, in a week. CERT-In evidence that previously took
manual effort is now generated automatically across every project.”

Security Leadership

Top #3 Indian Public Sector Bank
```

Attribution runs on two lines: the role, then the organisation. Where the
customer cleared a name, use `Srimal Silva, AGM - IT` style on the role line.
Where they did not, `Security Leadership`, `Cloud Security Team` and
`Spokesperson` all appear on live pages.

## Anonymisation

Half the live pages are anonymised, and the descriptor does the work a name
would.

| Pattern | Example |
| --- | --- |
| Rank plus sector plus country | `Top #3 Indian Public Sector Bank` |
| Region plus sector | `UAE Islamic Bank` |
| Segment plus category | `AI Healthcare Innovator` |
| Scale plus sector | `Fleet and Leasing Leader` |

Set `anonymized: true` in the front matter and the validator will fail the
draft if the body still names the customer. It cannot read a screenshot, so
check every image by eye for a tenant name, a domain, an IP or an account id.

## Length and images

300 to 900 prose words. These pages are short by design, because the reader is
comparing four of them.

At most two images, each captioned. Never a console screenshot containing the
customer's own data. A redacted architecture diagram or a generic product view
is the safe choice, and `<harness>/references/asset-kit.md` names where both
live.

## Related

- `assets/case-study-template.md`, the file you copy
- `<harness>/references/house-style.md`, tables, bullets, callouts, watermarks
- `<harness>/scripts/check_asset.py`, the validator for this channel
