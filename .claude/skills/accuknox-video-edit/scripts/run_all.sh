#!/usr/bin/env bash
# Regenerate every AccuKnox video edit: voice, render, then the read-back checks.
# Run from the repo root. Each project logs to references/video-edits/<slug>/output/_run.log.
S=.claude/skills/accuknox-video-edit/scripts
for p in "$@"; do
  d=references/video-edits/$p
  log=$d/output/_run.log
  mkdir -p "$d/output"
  {
    echo "=== $p tts"
    python $S/vedit.py $d tts || { echo "RESULT $p FAIL tts"; continue; }
    echo "=== $p render"
    python $S/vedit.py $d render || { echo "RESULT $p FAIL render"; continue; }
    echo "=== $p hook"
    python $S/qc.py $d hook && h=PASS || h=FAIL
    echo "=== $p voice"
    python $S/qc.py $d voice
    echo "=== $p full"
    python $S/qc.py $d full
    echo "RESULT $p hook=$h"
  } > "$log" 2>&1
  grep "^RESULT" "$log"
done
echo "ALL DONE"
