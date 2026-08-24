---
name: accuknox-press-release-writer
description: >
  Write an AccuKnox press release. Use this skill whenever the user asks for a
  press release, an announcement, a partnership announcement, a customer win
  announcement, a product launch release, an award announcement, an executive
  hire announcement, or newswire copy for AccuKnox. Triggers include "write a
  press release for X", "announce our partnership with X", "X selected us,
  announce it", "we launched X at RSAC, write the release", "PR for the award",
  or pasting deal details and asking for an announcement. Carries the dateline
  format, the quote and boilerplate rules, the intake list of what the writer
  must supply, and the structural validator.
trigger: /ak-press
---

# AccuKnox press release writer

A press release is a legal-adjacent document that a journalist, a partner's
marketing team and a customer's communications office all read before it ships.
Every name, title and claim in it gets checked by somebody who was in the room.

Repo root: `D:\Atharva\AccuKnox\HelpDocs`.
Shared harness: `.claude/skills/accuknox-blog-writer/`, written below as
`<harness>/`.

## Load the writing chain first

1. `.claude/core/runtime-contract.md`
2. `.claude/core/writing-rules.md`, sections 8, 9 and 10 carry this channel
3. `.claude/core/restraint-rules.md`
4. `<harness>/references/house-style.md`
5. `references/press-release-layout.md` in this skill

Print the `Loaded` block above the draft.

**The accuracy rule bites hardest here.** A misspelled partner name, a wrong
job title or an invented quote is a retraction, not a typo. Every name, title,
organisation descriptor and award citation comes from what the user supplied.
Anything missing goes in visible brackets. Never guess a title from a name, and
never write a quote nobody said and label it as said.

## Ask for the intake before you write a word

Ask all of it in one message and wait. A press release is entirely supplied
facts, so a missing answer becomes a bracket, never an invention.

**The announcement**

1. **Release type.** One of `partnership`, `customer-win`, `product-launch`,
   `award`, `executive-hire`, `funding`, `certification`. The type decides the
   section order.
2. **The one-sentence news.** What happened, in the words you would use to a
   journalist.
3. **Dateline.** City, country, date, and the release time with its timezone.
   Live releases carry `11:00 AM IST` style times.
4. **Embargo**, if there is one.

**The organisations**

5. **Every organisation named in the headline**, with its legal name, a
   two-sentence descriptor for the `About` block, and its website. A three-party
   partnership needs three descriptors and three websites.
6. **The AccuKnox module or product** in scope, by canonical name. ASPM, CNAPP,
   CSPM, SIEM, AI-SPM, AI Security 2.0.
7. **Deal shape**, where relevant. Multi-year, distributor plus reseller,
   region, whether the scope can be published.

**The quotes**

8. **Two to five quotes**, one per organisation named in the headline. For each:
   the exact wording if approved, otherwise the points to make, plus the
   speaker's **full name, exact job title and organisation**. A quote with an
   unverified title is a bracket, not a guess.

**The contacts**

9. **Media contacts**, one per organisation: name, title, email.
10. **Awards or recognitions** to cite, with the awarding body and the year.

Ask once. Skip the ask when the user says to go with your recommendation, and
bracket what you do not have.

## Write it

**1. Check it has not already gone out.**

```bash
grep -i "<partner or customer>" <harness>/sources/press-release.md
```

**2. Read the layout.** `references/press-release-layout.md` carries the
dateline shape, the quote block format, the `About` rules and the contact block,
from the four most recent live releases.

**3. Read the nearest live release of the same type.**

```bash
python <harness>/scripts/fetch_md.py \
  press-release/fairfirst-insurance-accuknox-partnership
python <harness>/scripts/fetch_md.py \
  press-release/accuknox-launches-ai-security-2-0-at-rsac-2026
```

**4. Copy the template and fill it.**

```bash
cp .claude/skills/accuknox-press-release-writer/assets/press-release-template.md \
   references/press-release-drafts/<slug>.md
```

**5. Write pass 1, read it cold, fix, then gate.**

## The gates

```bash
cd .claude/skills/accuknox-blog-writer
python scripts/check_asset.py <draft.md> --channel press-release  # CRITICAL 0
python scripts/verify_links.py <draft.md> --fix-suggestions       # 0 broken
python scripts/slop.py <draft.md>                                 # adjusted CRIT 0
```

Then section 5 of `.claude/core/restraint-rules.md` by reading.

The validator checks the dateline opens the body, that every quote has an
attribution line, that each named organisation has an `About` block, and that
`Media Contacts` exists. It cannot check that a job title is correct. That is a
human step, and you say so in your reply.

## Output

Google Doc by default:

```bash
cd .claude/skills/accuknox-blog-writer
python scripts/to_gdoc_html.py <draft.md>
python scripts/to_gdoc_html.py <draft.md> --print-title
```

Then `create_file` with `contentMimeType: "text/html"`.

Reply with the Doc URL, the markdown path, the gate results, and a numbered list
of **every name, title and claim that needs sign-off before this ships**. That
list is the deliverable as much as the draft is.

## The one place this diverges from the live pages

Published releases open the dateline with an en dash: `**Colombo, Sri
Lanka**, 20 AUG 2026 – The collaboration brings...`. The house ban list
forbids the en dash, and the slop scorer fails on it.

Write the dateline as two sentences instead:

```markdown
**Colombo, Sri Lanka**, 20 AUG 2026. *The collaboration brings together
AccuKnox's application security technology, VS ONE's distribution capabilities,
and APTS's local implementation and support expertise.*
```

Same information, same italic summary line, no banned punctuation. Flag the
divergence in your reply so whoever pastes it into WordPress knows it was
deliberate.

## Files in this skill

| Path | What it holds |
| --- | --- |
| `references/press-release-layout.md` | The section order per release type, from the four newest live releases |
| `assets/press-release-template.md` | The file you copy to start a draft |

Everything else comes from `<harness>/`.

## Related

- `.claude/skills/accuknox-case-study-writer/`, the long-form version of a
  customer win
- `.claude/skills/accuknox-blog-writer/`, the shared harness
- `.claude/core/runtime-contract.md`, the accuracy and safety rules
