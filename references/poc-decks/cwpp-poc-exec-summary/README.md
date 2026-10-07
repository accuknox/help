# CWPP POC Executive Summary, Anonymized Reference Deck

Use this deck as the model for every AccuKnox POC executive summary. It is the anonymized copy of a real
CSPM, KSPM and CWPP (VM and runtime) POC readout. The customer is called "ACME Corp".

## Files

| File | Use |
|---|---|
| `accuknox-cwpp-poc-exec-summary-anonymized-2026-09.pptx` | Editable master. 64 slides, 16:9, Arial. |
| `accuknox-cwpp-poc-exec-summary-anonymized-2026-09.pdf` | Read-only copy for review and sharing. |

## Slide Structure

The deck has 10 sections. Keep the order when you build a new POC deck.

| Section | Slides | Content |
|---|---|---|
| Opening | 1 to 4 | Title, agenda, executive summary, scope and coverage |
| 01 Platform Overview | 5 to 6 | CNAPP map: CSPM, KSPM, KIEM, CWPP, container security, compliance, Ask AI |
| 02 CSPM Assessment | 7 to 10 | Dashboard, top findings, asset inventory |
| 03 CSPM Key Findings | 11 to 18 | One evidence slide and one security graph slide per finding |
| 04 Compliance Insights | 19 to 21 | Framework scores, CIS deep dive |
| 05 KSPM and Key Findings | 22 to 38 | Clusters, risk posture, KIEM graphs, image CVEs, CIS control |
| 06 VM and Runtime Protection | 39 to 51 | App behavior, KubeArmor alert, policies, VM CVEs, toxic combinations |
| 07 Investigation Report | 52 to 54 | AI-correlated deep dives |
| 08 Risk Prioritization | 55 to 57 | Scanner output to action queue |
| 09 Assistive Remediation | 58 to 60 | Ask AI and Agent Z |
| 10 POC Summary and Next Steps | 61 to 64 | Outcomes, 90-day roadmap, call to action |

Every finding slide uses one pattern: four stat cards, a screenshot, a risk impact column and a
recommended fix box.

## What Was Anonymized

The source PDF copy only swapped the customer name. Account IDs, account names and resource names stayed
in the text and in the screenshots. This copy replaces them everywhere.

1. **Slide text.** Customer name, AWS account names and IDs, security group names and IDs, instance
   IDs, ECR repository names, hostnames, API names and finding IDs.
2. **Screenshots.** All 41 unique screenshots were read with OCR, and every sensitive string was
   repainted with a fake value in the same place. Each redacted image was read with OCR again, and
   the second pass found no match.
3. **Hidden data.** Alt text, file paths, author and title fields in the file properties.
4. **Kept on purpose.** Public product and tool names (ArgoCD, Datadog, Okta, Kyverno, vLLM and similar),
   CVE IDs, finding counts, dates and scores. They carry the evidence and do not identify the customer.

The real-to-fake map is not in this repo. A map file would defeat the anonymization.

## How to Reuse the Deck

1. Copy the PPTX. Never edit the master.
2. Replace "ACME Corp" and the numbers with the new customer's data.
3. Replace every screenshot with a new capture, then redact it before you share the deck outside AccuKnox.
4. Check each number against the platform. The master carries the numbers of the source POC.
5. Search the finished file for the customer's real name, account IDs and domain before you send it.

## Help Docs Linked From the Section Slides

| Slide | Link |
|---|---|
| 5 | `help.accuknox.com/getting-started/accuknox-arch/` |
| 7 | `help.accuknox.com/how-to/playbook-cspm/` |
| 19 | `help.accuknox.com/use-cases/compliance/` |
| 22 | `help.accuknox.com/use-cases/kspm/` |
| 39 | `help.accuknox.com/getting-started/runtime-sec-arch/` |
| 58 | `help.accuknox.com/agentz/` |
| 61 | `help.accuknox.com/getting-started/cwpp-prereq/` |

## Open Points in the Source Numbers

Slides 55 to 57 do not add up. A human must resolve them before the numbers go to a customer.

1. The "action queue" is 360 Critical/High findings on slides 3, 55, 56 and 57. The severity chart on slide 56
   shows 5 Critical and 373 High, which sum to 378. Slide 57 shows 366, 6 and 6, which also sum to 378.
2. Slide 56 shows 866 findings still Critical, High or Medium. The chart bars (5, 373, 525) sum to 903.
3. The title slide eyebrow reads "CSPM, KSPM, CWPP". The source deck read "CSPM, KSPM, VM".
