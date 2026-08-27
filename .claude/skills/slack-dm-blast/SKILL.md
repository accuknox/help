---
name: slack-dm-blast
description: Send a custom 1:1 DM to every member (or a filtered subset) of the AccuKnox Slack workspace via the connected Slack account. Supports text messages with optional images. Always asks for confirmation before sending. Invoke with /slack-dm-blast.
---

# Slack DM Blast

Send a formatted 1:1 direct message to every human member of the AccuKnox Slack workspace, or to a filtered subset.

## Prerequisites

The session must have a connected Slack MCP server (`mcp__eabb2725-5759-46aa-81a0-30b8d4fee4a1`). Load the following tools via ToolSearch before starting:

- `slack_list_channel_members`
- `slack_search_channels`
- `slack_search_users`
- `slack_send_message`
- `slack_send_message_draft`

## Workflow

### Step 1: Collect the message

Ask the user for:

1. **Message text** (Slack markdown). If the user already provided it in the prompt, use that.
2. **Image** (optional). The user can provide a URL or a local file path. If a local file, upload it to Slack via the available tools. If no image tool exists, tell the user to paste the image URL directly into the message.
3. **Audience filter** (optional). The user can specify:
   - `all` (default): every human member of `#general` (channel ID `CM1PV8YPQ`).
   - `exclude: [list of names]`: everyone except the listed names.
   - `only: [list of names]`: send only to the listed names.
   - `test: [list of names]`: send to a small test group first.

### Step 2: Build the recipient list

1. Paginate through `#general` members using `slack_list_channel_members` with `response_format: "concise"` and `limit: 30`. The channel ID for `#general` is `CM1PV8YPQ`.
2. Collect all pages. Exclude bots (`include_bots: false`).
3. Apply the audience filter from Step 1.
4. If the user gave names to exclude or include, match by display name (case-insensitive partial match). If ambiguous, ask.
5. Remove the sender's own user ID (`U059Q8ULCU8`) from the list. Nobody DMs themselves.

### Step 3: Confirm before sending

Present the user with:

- The exact message that will be sent (rendered).
- The total recipient count.
- The list of recipient names (if under 30, show all; if over 30, show count and a sample of 10).

Use `AskUserQuestion` with two options:
- **Send now**: proceed.
- **Cancel**: abort.

Do NOT send a single message until the user confirms. This is a hard rule.

### Step 4: Send DMs

1. Loop through the recipient list.
2. For each recipient, call `slack_send_message` with `channel_id` set to the user's Slack user ID. Slack opens a DM channel automatically when you message a user ID.
3. Collect successes and failures.
4. Report the final tally: `X sent, Y failed` with the list of failures if any.

### Step 5: Report

Print a summary table:

| Status | Count |
|--------|-------|
| Sent | X |
| Failed | Y |
| Total | Z |

If any failed, list the names and error reasons so the user can retry.

## Rules

- Never send without explicit user confirmation.
- Never include bots or deactivated accounts.
- Never DM the sender (your own connected account).
- If the Slack connection drops mid-send, stop and report progress. Do not retry automatically.
- Rate limit: Slack may throttle. If you hit a rate limit error, wait 3 seconds and retry that one message up to 2 times before marking it failed.
- Keep the message under 5000 characters (Slack limit per message).

## Example invocations

```
/slack-dm-blast
Message: <paste your message>
Audience: all
```

```
/slack-dm-blast
Message: <paste your message>
Audience: only Likhitha, Kavitha
```

```
/slack-dm-blast
Message: <paste your message>
Audience: exclude Nat, Rahul, Gaurav, Emre, Brian, Jim Watts
```

```
/slack-dm-blast
Message: <paste your message>
Image: https://example.com/banner.png
Audience: test Likhitha, Kavitha
```
