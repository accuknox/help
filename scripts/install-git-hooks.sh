#!/bin/sh
# Point this clone's git hooks at the version-controlled .githooks directory.
# Run once after cloning:  sh scripts/install-git-hooks.sh
git config core.hooksPath .githooks
chmod +x .githooks/* 2>/dev/null || true
echo "core.hooksPath set to .githooks (pre-commit will keep docs READMEs current)."
