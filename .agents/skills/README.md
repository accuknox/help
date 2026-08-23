# Skills live under `.claude/skills/`

This folder used to mirror one skill for the Codex runtime. The mirror drifted
from its `.claude/` twin by two lines and nobody noticed, so the copy is gone.

Four writing skills now live in one place:

| Skill | Job |
| --- | --- |
| `.claude/skills/accuknox-blog-writer/` | A blog post, plus the shared harness the other three read |
| `.claude/skills/accuknox-press-release-writer/` | An announcement |
| `.claude/skills/accuknox-case-study-writer/` | A customer outcome |
| `.claude/skills/accuknox-comparison-writer/` | A versus, alternatives or stack-ranking page |

Read the `SKILL.md` in whichever one matches the job. All four follow the
load-order contract in `.claude/core/runtime-contract.md`, and `AGENTS.md` at the
repo root carries the same ban list as `CLAUDE.md`.
