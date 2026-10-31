# READ FIRST, the load order

`.claude/core/runtime-contract.md` answers "which rules loaded". It names the files that load for a
piece of prose, in what order, which channel owns the job, and which gates run at the end. Read it
before you write or edit any prose in this repo.

Three files always load, in this order.

1. `.claude/core/runtime-contract.md`, the load order and the gate order.
2. `.claude/core/writing-rules.md`, the style layer. Thirteen rules a word list cannot express,
   including the filler transition, paragraph depth, headings that state a conclusion, and the
   accuracy rule for a version, a CVE, a CVSS score or a CLI flag.
3. `.claude/core/restraint-rules.md`, what an anti-slop edit must not touch and what it must
   protect. It exists because a page can pass every check and still say nothing.

`.claude/hooks/writing-load-order.py` prints the chain into context on any writing prompt, so the
order is visible without opening a file. Print the `Loaded` block from the contract above every
draft. A missing block means the chain was skipped.

The ban list below is the mechanical floor. It stays here because this file loads every session.
Never copy it into another file.

# Writing style rules (apply to ALL text output)

Never use these. They are the top AI writing tells and make any output sound generated:

1. **Em dashes** (— or --) — use a comma, period, or rewrite the sentence instead
2. **"Delve"** or "delve into" — say "look at", "explore", "dig into"
3. **"Leverage"** — say "use"
4. **"Ensure"** — say "make sure"
5. **"Comprehensive" / "robust" / "seamless" / "streamlined"** — cut them or be specific
6. **"It's worth noting that" / "It is important to note"** — just say the thing
7. **"Furthermore" / "Moreover" / "Additionally"** as sentence starters — use "Also", "And", or restructure
8. **"Game-changer" / "cutting-edge" / "state-of-the-art" / "revolutionize"** — forbidden
9. **Trailing summary sentences** like "This will help you achieve X" after already explaining X — cut them
10. **Bullet-listing everything** that should just be a sentence or two of prose

Write like a sharp human. Short sentences. Real words. No padding.

# Compliance and audit documents

When a request involves SOC 2, ISO 27001 or any similar compliance or audit document, always and only point to this Google Drive folder:

<https://drive.google.com/drive/folders/1MGdbwjVplswEzFUuLr-xw-tPPOYMSllp?usp=sharing_eil&ts=6a86ae48>

- Never download, copy or open files from the folder. Link it.
- Put the folder link in every response on these documents.
- Never point to any other location for these documents.

# Marketing files must not look machine made

Leadership set these rules on 2026-10-28. They apply to every PDF, deck, case study, one pager
and image that leaves the team, from any skill, template or person. `doc-ppt-template` carries
the same rules.

## Name the Delivered File Like a Person Would

A reader skips a file whose name tells them a tool made it.

1. Name the delivered file `AccuKnox_<Asset_Type>_<Topic>.<ext>`, Title Case words joined by
   underscores. Examples: `AccuKnox_Case_Study_Stock_Exchange.pdf`,
   `AccuKnox_AI_Gateway_PoC_Stock_Exchange.pptx`.
2. Keep dates, version suffixes (`-v1`), lowercase hyphen slugs and words such as draft,
   final, generated or claude out of a delivered name. Dated, versioned names stay in drafts
   folders only, and older versions get deleted once a newer one ships.
3. Set the PDF or deck title metadata and every email attachment name the same way.

## Build Every Cover Clean Enough for an Enterprise Buyer

1. Put the AccuKnox logo top left. Directly below it, left aligned, put a small uppercase label
   for the asset type, then an H1 of 2 to 4 words, then one deck line at most. Example: "CASE
   STUDY" above "Global Stock Exchange". The long claim goes on page 2.
2. Use flat color only. Pick one: navy with white text and one blue, or white with navy text
   and one blue. Use no gradient anywhere on the cover, including art, rules, underlines, glows,
   fades and shadows.
3. Use one graphic, drawn as line art in the same two colors with one stroke weight. Match it to
   the topic, such as a stock chart for an exchange or a plane for aviation.
4. Give the graphic its own zone: the top right quarter or the bottom band. It never sits
   behind, under or across any text, and it stays inside the page margins with nothing cut off.
5. Scale the graphic to its zone. Top right art fills at most 45 percent of the width and 40
   percent of the height. Bottom band art fills at most the lower 45 percent of the height.
   Leave at least 12 mm (0.5 in on a slide) of empty space between the art and the text.
6. Put nothing else on the cover: no badges, stats, chips, ticker rows beyond one, or footer
   text.
