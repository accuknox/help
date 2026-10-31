---
name: competitor-tool-signal
description: Weekly lead hunt for accounts that run a rival security tool. Finds job posts from the last 7 days that name Wiz, Orca, Lacework, Aqua, Sysdig, Prisma Cloud, Veracode or Checkmarx, then returns verified security buyers at those companies in one sheet. Use for "find accounts that use Wiz", "competitor displacement leads", "crawl job posts for tools", or when Nat asks which companies run a rival tool.
---

# Competitor Tool Signal

A company that hires for a rival tool runs that tool today. That is a displacement account, and the job post is the reason to write. Nat asked for this on 2026-10-29 after seeing Uniphore post a role that names Wiz.

## One Command Builds the Weekly Sheet

```bash
python .claude/skills/competitor-tool-signal/scripts/run.py --target 25 --cap 0.60
```

Add `--window m` on the first run to look back a month. The sheet lands in `drafts/competitor-signal/AccuKnox_Competitor_Tool_Leads_<date>.xlsx`. One run costs about $0.05 in treg and Jev spend and about 75 Firecrawl credits. The first sample run on 2026-10-30 found 43 job pages, 10 confirmed posts, 4 companies and 6 verified leads. The routine runs it every Monday at 09:00 IST, and its spec lives in `D:\Atharva\NOTES\.claude\routines\competitor-tool-signal-weekly.md`.

## Six Steps Turn a Job Post Into a Verified Buyer

1. **Find.** Firecrawl searches the open web for job pages from the last 7 days, one query per tool, and reads each page.
2. **Confirm.** Jev checks that the page is one job post and that the team uses the tool. This drops "Orca" the whale and the vendor hiring for itself.
3. **Company.** treg enriches the company. Jev checks the name matches and the employer is not a security vendor or an agency. The size gate is 1,000+ staff.
4. **Buyers.** treg finds security people. Jev runs five checks: buyer role, fit, not a competitor, can buy, title evidence.
5. **Email.** treg finds the work email, tries the next provider on a miss, then verifies it. Only a `valid` email on the company's own domain counts.
6. **Sheet.** One tab, nine columns, with an opening line per lead. A company and tool pair already reported never shows twice.

## Eight Rival Tools Are Watched

| Tool | Why it matters |
|---|---|
| Wiz, Orca, Lacework, Aqua, Sysdig, Prisma Cloud | Cloud and container security rivals |
| Veracode, Checkmarx | Application security rivals |

To watch another tool, add one line to `TOOLS` in `scripts/run.py`. To change the opening line, edit `OPENER` in the same file.

## Five Rules Keep the Run Safe and Cheap

1. Send nothing. The routine only builds the sheet, and a person reviews it first.
2. LinkedIn job pages stay out of step 1 because Firecrawl refuses linkedin.com. A LinkedIn job title that names a tool can still be added through treg.
3. The sheet holds personal emails, so keep it internal and out of git. `drafts/` is untracked.
4. Check the Firecrawl balance with `firecrawl credit-usage` before a manual run. The free plan gives 1,000 credits a month.
5. The script imports `common.py` from `D:\Atharva\NOTES\SCRIPTS\gtm`. Restore the vault first on a new PC.

## Sources

Tool list from Nat Natraj, 2026-10-29. Discovery and scraping with Firecrawl. Company, people and email data with treg. Judgements with Jev (TypeSafe System One).
