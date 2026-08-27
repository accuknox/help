# Zernio scheduling for AccuKnox

One command turns a campaign markdown file into a scheduled queue on the AccuKnox X account.
This is the standard path. Do not use the FavStash MCP tools and do not schedule through the web
UI, because only `post.py` writes the `_sent.tsv` ledger.

The FavStash MCP server exposes Instagram, YouTube and TikTok only. It cannot reach X at all.
That is why this script exists.

## Run it

```bash
py -3.11 .claude/skills/accuknox-social-campaign/post.py plan <campaign.md> --start 2026-08-27
```

`plan` prints the full schedule and sends nothing. Read every line, then send:

```bash
py -3.11 .claude/skills/accuknox-social-campaign/post.py send <campaign.md> --start 2026-08-27 --live
```

Dry run is the default on every command. Nothing leaves the machine without `--live`.

Nothing publishes immediately. Every post in the run is scheduled, starting on `--start`, or on
tomorrow when `--start` is omitted. Two slots a day at 07:30 and 19:30 IST, which is a 12 hour gap
that lands on the APAC morning and the US morning.

## Commands

| Command | What it does |
|---|---|
| `plan <file>` | Print the schedule, character counts and image flags. Sends nothing. |
| `send <file> --live` | Schedule every post, append to `_sent.tsv`. |
| `sync-media <file> --live` | Re-upload images onto posts that are **already scheduled**, matched on exact text. |
| `list` | Print the AccuKnox queue with status, time and image flag. |
| `cancel <post_id> --live` | Delete one scheduled post. |

## The two-account trap

The API key reaches two X accounts: `AccuKnox` and `cultist_dev`, which is Atharva's personal
account. They sit in two Zernio profiles under one user.

| Profile | ID | Accounts |
|---|---|---|
| AccuKnox | `6a7ebc0ab7c6776815670114` | X `AccuKnox`, LinkedIn, YouTube |
| Personal | `6a7e14d1ea845ffef005528b` | X `cultist_dev`, Instagram, YouTube |

The vault copy of this script at `D:\Atharva\NOTES\SCRIPTS\zernio\post.py` selects the first
enabled account of a platform. Run that one from this repo and it posts to `cultist_dev`.

This copy pins every lookup to `PROFILE_ID` and then matches the username, so both filters have to
pass. A wrong account is an error, not a silent mis-send. `list` is scoped the same way, so it
never shows personal posts.

## Attaching an image

Add a `media:` line at the end of a post block. An `alt:` line is optional and becomes the
accessibility text on X. Both lines are stripped before the post goes out.

A `media:` value is either a public URL or a local path. This matters more than it looks.

```markdown
Security Graph maps the assets around a finding.

media: https://help.accuknox.com/getting-started/images/release-notes/v3.6/security-graph-finding-s3.png
alt: AccuKnox Security Graph mapping an S3 finding to connected assets
```

A public `https://` URL passes straight through to Zernio with no upload. A local path is uploaded
first. Local paths are absolute, or relative to the repo root.

## The 7 day limit on uploaded images

Uploaded media lands in Zernio's temporary storage and **auto-deletes after 7 days**. A post
scheduled further out publishes with a dead image link and no warning.

A public URL never expires. So prefer a `help.accuknox.com` URL over a local file whenever the
image is already published on the docs site. `plan` marks a local upload that fires past the TTL
with `UPLOAD!` and prints a count at the bottom.

For a run longer than 7 days with local images, send the posts first, then re-run `sync-media` a
few days before the far-out ones fire. It matches each post by its exact text, so an edit to the
wording breaks the match and the post reports `skip (not scheduled)`.

## Before you send

1. Run the slop scorer on the campaign file. CRIT must reach 0.
2. Run `plan` and read every line. This is the last point where a mistake is free.
3. Check the `profile:` and `account:` header in the `plan` output says AccuKnox.
4. Confirm the schedule with Atharva. A live send always needs his explicit go-ahead.

`check()` refuses a post that carries a link, because these campaigns are link-free by default.
Delete that guard deliberately if a campaign needs links, rather than working around it.

## Character limits

The AccuKnox X account is X Premium, so the free-tier 280 cap does not apply and the real ceiling
is 25,000. `LIMITS` sets a 4,000 sanity ceiling instead. The personal account is not Premium, so a
campaign aimed there needs the 280 limit back.

## What cannot be undone

A scheduled post is deletable with `cancel`. A published post is not. Removing a published post
needs `POST /v1/posts/{id}/unpublish`, which deletes it from X itself, and `post.py` deliberately
does not wrap that. Do it by hand so it stays a decision rather than a flag.

## How it talks to Zernio

The key is `ZERNIO_API_KEY` in `D:\Atharva\NOTES\.env`, the machine-wide key file. It is not
duplicated into this repo. Never paste it into a file, a commit or chat output.

Every call shells out to `curl`, because this machine's Python has an expired CA root and `urllib`
fails on the Zernio host.

Every request carries a unique `x-request-id`. Zernio dedupes on that header for 5 minutes, which
makes a retry after a network blip safe instead of a double post.

One API shape gotcha: `/accounts` returns `accountId` and `profileId` as strings or as populated
objects depending on the endpoint. `/posts` populates them. Both shapes are handled.

## Campaigns

Each campaign gets a folder under `campaigns/<id>/` holding `tweets.md` and an `images/` folder.
The markdown is the single source of truth, so edit it and re-run rather than clicking through a
dashboard.
