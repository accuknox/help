---
name: newsletter-clicks
description: Monthly click-level analysis of the AccuKnox newsletter from the email platform's statistics export. Checks that every email list and every file is present, finds security-scanner clicks that inflate the numbers, and reports what is working, what is not, what to do next, the top 5 and worst 5 links and companies. Use for "Newsletter Clicks", "analyze the newsletter", "newsletter stats", "click analysis", "how did the newsletter do", "AccuKnox_Newsletter_Statistics", or any zip or folder with bounce_, unsubscribe_, open_click_ and click_details_ Excel files.
---

# Newsletter Clicks

Raw newsletter clicks are not people. Security scanners at the reader's company open every link in a message before the reader does. This skill removes those clicks, checks the export for gaps, and says what the real readers did.

First run: October 2026. In that month 97.9% of NAT CRM clickers were scanners.

## Four Inputs Make a Full Run

1. The statistics export, as a `.zip` or a folder. It holds one subfolder per list, such as `NAT CRM` and `TGACRM`.
2. Four Excel files in each list folder: `bounce_`, `unsubscribe_`, `open_click_` and `click_details_`.
3. The sent count for each list. The export does not hold it. Ask the user once. Without it, rates stay empty.
4. The month label, such as `October 2026`.

## One Command Builds the Report

```bash
python3 -I .claude/skills/newsletter-clicks/scripts/analyze.py \
  --input "<zip or folder>" \
  --month "October 2026" \
  --sent "NAT CRM=<sent>,TGACRM=<sent>"
```

1. Add `--expect "List A,List B,List C"` when the user sends more or other lists. The default is `NAT CRM,TGACRM`.
2. Leave `--sent` out when the user does not know the counts. The report says rates are missing.
3. The script needs only `openpyxl`. Run it with `-I`, and never from inside the unzipped folder.

The script writes four files to `~/Atharva/AccuKnox/newsletter-reports/<month>/`.

| File | Holds |
|---|---|
| `report.md` | The full report |
| `summary.json` | The same facts for scripts |
| `link_table.csv` | Every link with human, scanner and raw clicks |
| `human_clickers.csv` | People who clicked and are not scanners, for sales |

The output holds customer emails. Never copy it into this repo or any other git repo.

## What the Report Covers

1. **Data sanity check.** FAIL, WARN or OK for each check below.
2. **What is working, what is not, what we recommend.** Each line carries a number.
3. **Top 5 and worst 5 links** by human clickers.
4. **Top 5 companies** by human clickers, **worst 5 companies** by bounces, and the most scanner-heavy companies.
5. **Numbers by list**, with the sent count and rates when you gave them.

### The Sanity Checks

- Every expected list folder exists.
- Each list has all four files, with the right column headers and at least one row.
- File names carry the same list tag as the folder. The October export had `TGACRM` folders with `TGACTM` file names.
- File names carry a month.
- No campaign id repeats across lists.
- The bounce file matches the Bounce rows in `open_click`. The unsubscribe file matches the Unsubscribe rows.
- Clickers in `click_details` also appear in `open_click`, and the reverse.
- The same address does not sit on two lists.
- A sent count exists for each list.

## How Scanners Are Found

1. A newsletter link is any link clicked by at least 50% of a list's clickers.
2. A scanner is a clicker who hit at least 80% of the newsletter links.
3. A human is every other clicker.

The export has no click timestamps, so click speed cannot be tested. Say "strong estimate" when you quote the scanner count. The script switches the filter off when a list has fewer than 3 newsletter links.

## Judge the Result, Then Add Your Own Read

The script writes the verdicts from fixed rules. Read `report.md` before you answer, then add what the rules cannot see.

1. Open the top 5 links. Name the topic that won, and say why it fits the audience.
2. Open the worst 5 links. Check whether a zero-click link is there on purpose, such as a webinar the sales team needs.
3. Open the scanner-heavy companies. Tell sales to ignore their clicks.
4. Send `human_clickers.csv` to sales. Sort by `beyond_newsletter_links`, highest first.
5. Quote any list that has no `click_details` file as unchecked. Do not call its clicks real.

## Six Limits Change How You Read the Numbers

- The worst 5 links often tie at 0 human clickers. The report says how many tie. Ties break on raw clicks.
- A list without `click_details` gets only an estimate of its scanner share, copied from the other lists.
- Bounce and unsubscribe rates need the sent count. Without it the report shows counts only.
- Tracked records are people with any event. They are not the sent count.
- Apple Mail Privacy Protection inflates opens in the same way. Trust clicks and human clicks over opens.

## Report to the User

1. Lead with the human click count and the scanner share.
2. State every FAIL from the sanity check, with the missing file name.
3. Give the top 5 and worst 5 links as a short list.
4. End with the 3 most useful recommendations and the path to the output folder.
