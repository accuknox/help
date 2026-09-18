# Zernio scheduling for the AccuKnox LinkedIn page

One command turns a campaign markdown file into a scheduled queue on the
AccuKnox LinkedIn company page. This is the standard path. Do not use the
FavStash MCP and do not schedule through the Zernio web UI, because only
`li.py` writes the `_sent.tsv` ledger.

The FavStash MCP server exposes Instagram, YouTube and TikTok only. It cannot
reach LinkedIn. That is why this script exists.

`post.py` in `../accuknox-social-campaign/` is the X equivalent. The two scripts
share their plumbing and differ in three ways: LinkedIn posts carry their own
date rather than filling auto-assigned slots, they carry a first comment, and
they carry resolved `@mentions`.

## Three Commands Take a File From Draft to Scheduled

```bash
py -3.11 .claude/skills/accuknox-linkedin-post/li.py plan campaigns/<file>.md
```

`plan` prints the full schedule with character counts, image flags, first
comment flags and tag counts. It sends nothing. Then check the tags:

```bash
py -3.11 .claude/skills/accuknox-linkedin-post/li.py tags campaigns/<file>.md
```

`tags` resolves every `tag:` line against LinkedIn and prints what will render
as a real mention and what will not. Read both outputs, get Atharva's
go-ahead, then send:

```bash
py -3.11 .claude/skills/accuknox-linkedin-post/li.py send campaigns/<file>.md --live
```

Dry run is the default on every command. Nothing leaves the machine without
`--live`. Nothing publishes immediately either: every post in the run is
scheduled for the `when:` it states.

## Six Commands, and Only Two of Them Write

| Command | What it does |
|---|---|
| `plan <file>` | Print the schedule, character counts, image and comment flags. Sends nothing. |
| `tags <file>` | Resolve every `tag:` to a LinkedIn mention. Read-only. |
| `send <file> --live` | Schedule every post, append to `_sent.tsv`. |
| `sync-media <file> --live` | Re-upload images onto posts that are already scheduled. |
| `list` | Print the AccuKnox LinkedIn queue with status, time, image and comment flags. |
| `cancel <post_id> --live` | Delete one scheduled post. |

## One Block per Post, Each Carrying Its Own Date

Frontmatter, then posts separated by a line of three dashes. Every post states
its own date and time in IST.

```markdown
---
campaign: Sep to Oct 2026
---

Some frontier models rewrite the shutdown script you gave them.

Palisade Research ran 100,000 trials across thirteen models. Grok 4, GPT-5 and
Gemini 2.5 Pro all subverted a shutdown mechanism to finish a task, up to 97%
of the time even when told not to.

They overwrote a file they had permission to overwrite.

That makes it a permissions failure, not an alignment failure.

Read the full breakdown via the link in the comments.

#AIsecurity #ZeroTrust #AgenticAI

when: 2026-09-22 19:30
comment: Full post here: https://accuknox.com/blog/ai-kill-switch-agentic-ai
media: references/li-images/2026-09-22-post-03.jpg
alt: Diagram of an internal versus an external AI kill switch
tag: Atharva Shah | https://www.linkedin.com/in/...

---

Second post goes here.

when: 2026-09-23 19:30
comment: Download it here: https://accuknox.com/ebooks/ai-security-buyers-guide-2026
media: references/li-images/2026-09-23-post-04.png
```

### The keys

| Key | Required | Notes |
|---|---|---|
| `when:` | yes | `YYYY-MM-DD HH:MM` in IST. A past date or a collision is an error. |
| `comment:` | no, but warned | The auto first comment. This is where the link goes. |
| `media:` | no, but warned | A public URL or a repo-relative path. |
| `alt:` | no | Accessibility text on the image. |
| `tag:` | no, repeats | `Display Name \| https://www.linkedin.com/in/handle`. An extra tag, placed above the roster. |
| `roster:` | no | `no` drops the standard 15-name roster line. Defaults to yes. |

Every key line is stripped out of the body before the post goes out.

## A Link in the Body Is Refused, Because It Suppresses Reach

`li.py` refuses to schedule a post whose body contains `http://` or `https://`.
A link in the caption suppresses reach, so the link lives in `comment:` and the
body ends on a line pointing at it.

## The Same Key Reaches a Personal Profile, so the Account Is Pinned

One `ZERNIO_API_KEY` reaches two profiles under one user.

| Profile | ID | Accounts |
|---|---|---|
| AccuKnox | `6a7ebc0ab7c6776815670114` | LinkedIn `AccuKnox`, X `AccuKnox`, YouTube `accuknox` |
| Personal | `6a7e14d1ea845ffef005528b` | X `cultist_dev`, YouTube `cozy-console` |

`li.py` hard-pins the LinkedIn account to `6a80942677555aae01131b68` and
re-checks its platform, profile, username and enabled flag on every run. A
mismatch stops the run rather than posting somewhere wrong.

The key lives in `D:\Atharva\NOTES\.env` and is never copied into this repo.

## The Roster Is Automatic, so Never Type It Into the Body

Fourteen names close every post, in fixed order, as their own paragraph
between the body and the hashtags. `ROSTER` in `li.py` holds it pre-resolved.

`plan` prints the roster size and both character counts, and the `R` column
shows which posts carry it. Set `roster: no` on a post to drop it.

**Barun Acharya is never tagged.** He is in the two posts of 2026-09-16 and was
removed on 2026-09-18. Do not copy the roster line out of those older posts.

Rahul Jadhav is first and is plain text, not a link. LinkedIn refuses to
resolve `in.linkedin.com/in/rahul-jadhav-a0485310`, which is his real profile.
Two other Rahul Jadhav profiles do resolve and neither is the CTO, so never
swap one in to make the tag clickable.

## A Company Page Always Resolves, a Non-Follower Never Does

`tags` calls `GET /accounts/{id}/linkedin-mentions` for every `tag:` line.
These are the extra tags, a partner company or a speaker, and they land on
their own line above the roster.

A **company page always resolves.** A **person resolves only when the AccuKnox
page can see them.** A non-follower comes back with no `mentionFormat`, and
`send` ships that name as plain text and prints a note saying which ones.

Verified not to resolve: Mehlam Shakir, Rahul Jadhav. SecuVerse.ai has no
findable company page at all.

## Uploaded Media Dies After 7 Days, a Site URL Never Does

A `media:` value is either a public URL or a repo-relative path. This matters
more than it looks.

Zernio-hosted media auto-deletes after 7 days, silently. A post scheduled
further out than that publishes with a dead image. A public `accuknox.com` or
`help.accuknox.com` URL skips the upload entirely and never expires, so prefer
one whenever the image already lives on a site.

`plan` prints `UPLOAD!` against every local image that fires after the TTL. For
a campaign longer than 7 days, run `sync-media --live` a few days before the
far-out posts fire.

## Five Checks Run Before Anything Reaches the Company Page

1. `plan` and read every line.
2. `tags` and confirm the mention list.
3. Show Atharva the final copy, the destination and the schedule.
4. Wait for an explicit go-ahead. A live write to the company page is never assumed.
5. `send --live`, then `list` to verify status, image and first comment landed.
