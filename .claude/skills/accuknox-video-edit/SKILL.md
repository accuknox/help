---
name: accuknox-video-edit
description: >
  Edit an AccuKnox screen recording into a short, narrated, readable video. Use this skill
  whenever the user wants a Zoom, Teams, Meet or Loom recording, a customer call, a demo
  walkthrough, an onboarding review, a POC readout or an internal meeting cut down, cleaned
  up, voiced over, annotated, zoomed, chaptered or sped up. Triggers include "edit this
  recording", "cut this demo", "make a video from this call", "remove the webcam", "add a
  voiceover", "speed up the slow parts", "skip the part where", or a path to an .mp4 with a
  .vtt beside it. Works from frame inspection plus the caption file, renders with ffmpeg and
  OpenCV, voices the script with ElevenLabs v3, and checks the output by reading it back.
trigger: /ak-video
---

# AccuKnox video edit

The skill turns one raw recording into one MP4. It verifies each cut against frames, crops
the people out, and speeds up the waiting. Then it adds zooms, callouts, chapter titles and
an AI voiceover. The platform footage stays the subject, so the skill adds no slides or
marketing graphics.

The skill lives in `.claude/skills/accuknox-video-edit/` inside the repo at `D:\AccuKnox\help`.
Read `references/playbook.md` before step 3. It holds the rules each step below relies on.

## A Recording of a Customer Call Is Customer Data

Treat every source as confidential unless the user says it is public.

1. Keep the project under `references/video-edits/<slug>/`. `scaffold.py` writes a
   `.gitignore` of `*` there, so nothing in the folder reaches git.
2. Set `JEV` in `edit.py` from the brief before anything leaves the machine. The default,
   `"narration"`, sends the voiceover lines to Jev and ElevenLabs only. `"all"` also sends the
   caption cues to Jev, so use it only when the brief allows it. A brief that names
   ElevenLabs as the only outside service means `"off"`.
3. Never upload a frame, the source or the output anywhere. Never publish the MP4 as an
   artifact. Speech-to-text QC runs locally.
4. Do not print, log or store the ElevenLabs key. `eleven.py` reads it at run time.
5. Never hide an error or an empty view to imply a feature works. Cut it, or show it as it is.

## Eight Steps Take a Recording to a Checked MP4

Run every command from the repo root.

1. **Check the tools.** `ffmpeg -version` must report 5 or newer. The scripts prefer
   `C:\ProgramData\chocolatey\bin\ffmpeg.exe` over ImageMagick's old copy. Install a missing
   one with `choco install ffmpeg`. Python needs `opencv-python`, `numpy`, `pillow`,
   `faster-whisper` and `typesafe-sdk`. Jev reads `TYPESAFE_API_KEY` from the environment or
   from `D:\Atharva\NOTES\.env`. For a YouTube or web source, download it with `yt-dlp` first.

2. **Scaffold the project.**

    ```bash
    python .claude/skills/accuknox-video-edit/scripts/scaffold.py <slug> "<recording.mp4>" --vtt "<captions.vtt>" --title "<title>"
    ```

3. **Survey the whole source.** The command below writes 1 fps frames, contact sheets, a
   change-event list and the cleaned transcript to `work/`.

    ```bash
    python .claude/skills/accuknox-video-edit/scripts/survey.py references/video-edits/<slug>
    ```

    With `JEV = "all"`, Jev also labels every caption cue as setup, navigation, content,
    off-track or wrap-up in `work/cues.txt`. Each off-track, setup and wrap-up cue is a lead
    for a cut, and the frame still decides. Read every contact sheet in `work/sheets/` in
    order, beside `work/transcript.txt`. Note
    each section, each webcam tile, each wrong click and each dead stretch. Measure the
    shared-screen rectangle on a grabbed frame and set `SHARE` and `FULL` in `edit.py`.

4. **Verify every cut against frames.** For each time the brief names, run
   `survey.py <project> events A B` and `survey.py <project> grid T1 T2 T3 T4`. Read the
   grid. The cut goes on the last clean frame, whatever the brief said.

5. **Write `edit.py`.** It holds the config, the sections and the beats. A beat is one idea
   with its clips, holds, callouts and narration lines. Follow the speed, framing, callout and
   narration rules in the playbook. Then run `vedit.py <project> map` and **report the edit
   map and every ambiguity to the user before the render**. Flag what the footage cannot
   settle. Do not guess it.

6. **Voice the script.** `vedit.py <project> tts` first runs the narration gate. Jev scores
   each new line for a customer identifier and for a word a voice may spell out, and code
   patterns catch IPs, hostnames, IDs and paths. A blocked line stops the run before
   ElevenLabs sees any text. Rewrite it, then rerun. `vedit.py <project> check` runs the gate
   alone. The surviving lines are voiced and cached by text.
   `qc.py <project> voice` transcribes each line locally. Rewrite any line that comes back
   with a wrong word.

7. **Check the stills, then render.** `vedit.py <project> plan` prints the timeline.
   `vedit.py <project> qc B05:3 B12:7 ...` renders chosen frames into
   `output/qc_grid_N.jpg`. Read every grid for a label that covers UI text, a box that misses
   its target, or a frozen frame with an overlay in it. Then render, which takes about 1.5 min
   per output minute.

    ```bash
    python .claude/skills/accuknox-video-edit/scripts/vedit.py references/video-edits/<slug> render
    ```

8. **Watch the whole output.** `qc.py <project> full` writes a contact sheet of every second,
   a transcript of the final mix, and every silence over 4 s. Read all the sheets. Compare
   the transcript to the script. Fix, re-render, and check again.

## Every Requirement Gets Evidence in the Final Report

Report the output path, the duration and the resolution, then one row per requirement from
the brief with the check that proved it. A typical set:

| Check | Evidence |
|---|---|
| Section order | The chapter list in the MP4, and the contact sheets |
| A view the brief excluded is absent | The contact sheets around the cut |
| A result is visible long enough to read | The freeze length in the edit map, and a `qc` still |
| Every spoken claim matches the frame | The final-mix transcript beside the stills |
| No person, webcam, app switcher or dock | The contact sheets, every second |
| Voice timing | The silence list, and the transcript timestamps |

Write "not checked" for any row that did not run.

## Seven Scripts and Two References Do the Work

| File | Job |
|---|---|
| `scripts/scaffold.py` | Creates the project folder, `edit.py` and the `.gitignore` |
| `scripts/survey.py` | Frames, contact sheets, change events, transcript, frame grabs |
| `scripts/editkit.py` | `c`, `h` and `A`, the three helpers an `edit.py` is written with |
| `scripts/vedit.py` | Plans, voices, previews and renders. The edit lives only in `edit.py` |
| `scripts/jev.py` | Jev judgments: the narration gate and the caption-cue triage, with code fallbacks |
| `scripts/eleven.py` | ElevenLabs client. Key from the environment or `keys.py`, never printed |
| `scripts/qc.py` | Reads the output back: line transcripts, contact sheets, silences |
| `references/edit_template.py` | The `edit.py` that `scaffold.py` fills in |
| `references/playbook.md` | Rules for cuts, framing, speed, callouts, narration and reports |

The user's own changes after delivery go in `edit.py` only. The intro card, the base pace
and the voice are config keys at the top of that file. Re-run `render` and `qc.py full`
after every change.
