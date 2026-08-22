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
