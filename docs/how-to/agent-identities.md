---
title: Set Up Agent Identities for Coding Agents
description: Give each coding agent on your machine its own identity in AgentZ. Add Claude Code or Codex as an external agent, choose its models, sign in, and see its activity in Lens traces.
---

# Set Up Agent Identities for Coding Agents

Add your coding agent as an **external agent** in AgentZ. The agent gets its own named identity, uses only the models you approve, and writes its activity to Lens traces. You set it up on one machine at a time.

This guide covers two coding agents: **Claude Code** and **Codex**. The screens below show Codex.

<video controls preload="none" style="display: block; width: 100%; max-width: 100%; height: auto; margin: 1em 0; border-radius: 4px;" poster="../images/agent-identities/AccuKnox_Agent_Identities_Walkthrough.jpg">
  <source src="../videos/AccuKnox_Agent_Identities_Walkthrough.mp4" type="video/mp4">
  Your browser does not support embedded video. <a href="../videos/AccuKnox_Agent_Identities_Walkthrough.mp4">Download the Agent Identities walkthrough video</a> instead.
</video>

The video above walks through the same steps in about 2 minutes. The steps below follow it.

## Why Give a Coding Agent Its Own Identity

Coding agents run on a laptop with the developer's own login. That setup has three gaps.

- **No name.** Nobody can tell which agent made a call.
- **No limit.** The agent uses whatever model and credentials its owner has.
- **No record.** There is no trace of what the agent did.

An agent identity closes each gap.

- **Named.** Each agent has its own name, such as `work-laptop`.
- **Scoped.** You pick the models the agent may use when you approve its sign-in. You can disconnect it at any time.
- **Traced.** Its activity appears in **Lens > Traces**.

## Prepare One Machine and One Workspace

- An AgentZ workspace where you can open **Workspace settings**.
- Claude Code or Codex installed on the machine you want to connect. Codex must be version 0.162.1 or later.
- A terminal on that machine.

Install on one endpoint first. Add more machines after the first one works.

## Add the Agent in Five Steps

### 1. Open External Agents

In your workspace, go to **Workspace settings > External agents**, then click **Add agent**. The left side of the image in step 2 marks this menu item.

### 2. Pick the Agent and Name It

1. Open the **Agent** list and select **Claude Code** or **Codex**.
2. Enter a **Name**. Use something that tells you which machine it is, such as `work-laptop`.
3. Click **Add agent**.

A setup panel opens with the steps for the agent you picked.

![External agents menu item on the left, and the Add external agent panel with the agent type, name and Add agent button marked on the right](images/agent-identities/step-1-2-add-agent.png)

### 3. Install the AgentZ CLI

The image below covers steps 3 to 5. On the left is the **Setup** tab. On the right are the release assets, the config file and the launch command.

![Setup tab on the left. On the right, the GitHub release assets, the pasted config file and the terminal after the launch command](images/agent-identities/step-3-5-setup-install-config-launch.png)

In the **Setup** tab, click **Download CLI**. This opens the latest AgentZ release on GitHub.

Under **Assets**, download the archive for your system. There is one for macOS, Linux and Windows, each in amd64 and arm64.

Unpack the archive and put the `agentz` binary on your `PATH`. Then check it:

```bash
which agentz
```

The command prints the path to the binary.

### 4. Save the Configuration

Setup step 2 shows a config block for your agent. Pick your system tab (**Linux**, **macOS** or **Windows**) to see where the file goes. On Linux the path is `~/.config/agentz/config.yaml`.

1. Create the folder and open the file:

    ```bash
    mkdir -p ~/.config/agentz
    vi ~/.config/agentz/config.yaml
    ```

2. Click the copy icon next to the config block and paste it into the file.
3. Save the file.

The entry looks like this. Your panel fills in the real values.

```yaml
externalAgents:
  - "<agent-name>":
      provider: codex
      serverUrl: https://agentzharness.ai
      clientID: <client-id>
```

If the file already has an `externalAgents` list, add the new entry to it. Keep your existing profiles.

### 5. Sign In and Choose Models

Setup step 3 gives you the launch command. Copy it and run it:

```bash
agentz launch codex --profile '<agent-name>' --
```

For Claude Code, run the command shown in your **Setup** tab.

The terminal prints a sign-in link. Open it in your browser.

1. Open the **Models** list and tick the models this agent may use.
2. Click **Authorize**.

The page lists what the agent can read: your name, profile image and email. It also says you can disconnect the agent at any time in **Workspace settings > External agents**.

After you authorize, the agent starts in your terminal. Send it a short message such as `Hi` to confirm it answers.

## Switch to a Workspace Model

The agent starts on its default model. To use a model you approved:

1. Type `/model` in Codex.
2. Pick one of the approved models and a reasoning level.

Codex confirms the change, and the status line shows the new model.

![Authorize page with the Models list and Authorize button on the left, and Codex confirming the model change on the right](images/agent-identities/step-5-authorize-and-model.png)

## Add MCP Tools (Optional)

Setup step 4 in the panel connects MCP tools. Run the command it shows, then choose the tools, prompts and resources in the browser. For Codex the command is:

```bash
agentz launch codex --profile '<agent-name>' -- mcp login agentz
```

Skip this step if you only need models.

## See the Agent's Activity

1. Open your workspace.
2. Go to **Lens > Traces**.
3. Open the dropdown and select the external agent.

The traces list shows what that agent did.

## Disconnect an Agent at Any Time

Go to **Workspace settings > External agents** and open the agent. Its **Access** tab shows what the agent can use. The authorize page confirms you can disconnect an agent from this page at any time.
