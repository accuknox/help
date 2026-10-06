# Video Edit Playbook

The detail behind each step in `SKILL.md`. Every rule here came from a real edit of a
customer onboarding review in October 2026. That project stays on the local machine and out
of git, because it holds customer data.

## The First 5 Seconds Decide Whether Anyone Watches

The old cuts opened on a title card and a 25-word intro line, so the product appeared at
0:15. Viewers leave before that. Every video now opens on `HOOK`, and `qc.py hook` fails the
render when it does not hold.

1. Open on product, never on black or a title. Shot 1 starts at 0.0 s on a flash.
2. Use 2 or 3 shots of about 1.2 s each. Each floats the product screen in 3D, pushes the
   camera toward one fact, and punches that fact in as a 2 to 3 word headline.
3. Pick the most striking proof in the recording: a big number, a blocked attack, a success
   toast, a synced value. The headline names what the frame shows. "637 roles" sat over a
   ROLE node with a 637 badge. Never put a claim in a headline that the frame does not prove.
4. Zoom past the 1.5x body limit when the fact needs it. A shot lasts about a second, so 2.6x
   on a badge reads. Keep the fact clear of the lower-left third, where the headline sits.
5. Keep the hook line to about 10 words, so it ends by 4.5 s. A 15-word CIEM line ran 6.6 s
   and pushed the walkthrough to 7 s. Open it with a v4 tag such as `[intrigued]`.
6. End on the logo slam with the product name and a 3 to 5 word tagline. That replaces the
   old intro card, so set `INTRO = None`. Put any legal footer in `HOOK["footer"]`.
7. The walkthrough starts by 6.5 s, on a white flash out of the logo.

`OUTRO` adds the end card: the logo, a one-line title, a call-to-action pill and the closing
voice line. `BRAND = dict(watermark="br")` puts the colour logo on a white pill in the corner
of every product frame. The speed badge moves beside it.

The sound design is synthesized in `brand.py`: a low pad, a sub hit on the first frame,
whooshes on cuts, a riser and a hit on the logo. It sits about 9 dB under the voice. At
5 dB under, it masked the hook line.

| Test | Pass when |
|---|---|
| H1 opens bright | The first frame has mean luma above 40 |
| H2 product by 0.5 s | A hook shot or a product frame is on screen by 0.5 s |
| H3 motion | The median frame-to-frame change in the first 5 s is above 3, with 2 or more cuts |
| H4 voice by 0.8 s | Speech-band energy starts by 0.8 s |
| H5 body by 6.5 s | The walkthrough starts by 6.5 s |
| H6 logo in the hook | The white logo matches above 0.5 in the hook's last second |
| H7 watermark | The logo inside the pill matches on 90% or more of product frames |
| H8 logo on the end card | The logo matches above 0.5 on the end card |

## A Timestamp From the Brief Is a Hint, the Frame Is the Fact

The person who asks for the edit remembers the call, not the file. In the first brief,
"cut at about 2:46" pointed at a click that happened at 2:48.6, and "remove the API view at
4:19" was right to within 0.4 s. Treat every time in a brief as a place to start looking.

1. Find the moment in `work/events.txt`. A page change scores above 0.3. A click, a
   dropdown or a scroll scores 0.01 to 0.1.
2. Grab the frames on both sides with `survey.py <project> grid T-1 T T+0.4 T+1`.
3. Put the cut on the last clean frame before the unwanted action, never on the brief's
   number.

## The Shared Screen Hides Four Things That Must Never Ship

Each one turned up in the first source and had to be cut.

| What appears | Where it hides | How to find it |
|---|---|---|
| A webcam tile or a full-screen participant | The first seconds, and any column beside the shared screen | Contact sheet 1. Set `SHARE` so the column is never read |
| The macOS app switcher, with the presenter's apps and an unread-message badge | The half second before a window switch | A change event of about 0.1 right before a jump to another app. End the clip 0.5 s earlier |
| The dock | Window switching | The same event pattern. Cut it |
| An "empty" or "Not Available" view | After a click the brief said to skip | Grab the frame after the click |

A cut that lands near a window switch needs one extra check. `vedit.py plan` extends a
beat by freezing its last frame when the narration runs long. A frozen frame 0.1 s into
the app switcher shows the switcher for seconds. Grab the hold frame itself.

## Framing Rules Keep Small UI Text Readable

- Crop the browser chrome. `FULL = (0, 88, 1440)` removed the tab strip and the URL bar in a
  1440 x 900 share and gave a clean 16:9 frame at 1:1.
- Keep zoom at 1.5x or less. Above that, H.264 smears 12 px text. The engine adds a light unsharp
  mask above 1.15x.
- Reframe on a detail drawer, a terminal or a YAML panel rather than the whole page.
- A `(FROM, TO)` view pair eases over 0.8 s. Use it when a drawer opens, so the motion follows
  the UI.
- Never upscale the source. The output is never wider than `SHARE`.

## Speed Rules Separate Waiting From Content

| Footage | Speed |
|---|---|
| A loading spinner, a sidebar open, a menu search | 3x to 4x |
| Slow scrolling through a list | 1.5x to 2.5x |
| A click the viewer must follow | 1x |
| A result the viewer must read: a finding, a blocked command, an alert | 1x, then a 1 to 2 s freeze |
| A view on screen for less time than its narration | 0.6x, then a freeze |

`PACE.base` multiplies every clip. 1.15 suits a demo where the presenter moved slowly. A
badge reading "2.3x speed" appears at `badge_from` (1.6x by default), so a viewer never
mistakes a fast-forward for real time.

## Callouts Name What the UI Already Says

- A label repeats or summarises text the frame shows. "Command blocked" sat beside
  `bash: /usr/bin/apt: Permission denied`. A label never asserts what the UI does not show.
- Keep labels to four words. Number a set: "1 of 3: file activity".
- A box without text is enough to point at a tab the narration names.
- The automatic label spot covers UI text about one time in five. Pin it with `at=(x, y)` in
  source pixels, then render a `qc` still to check.
- Fade timing comes from `st=(from, to)` in source seconds. Start the box on the frame where
  the thing appears, not when the beat starts.

## Narration Says What the Viewer Sees and Nothing Else

1. One or two short sentences per beat. Explain what the screen means, do not read every label.
2. Spell numbers as words when they matter ("ninety four workloads"), so the voice cannot
   misread them.
3. Do not voice an acronym the voice may spell wrong or that you have not confirmed. The
   first script said "identity findings" for KIEM and "Kubernetes benchmark findings" for
   K8s CIS. The on-screen label carries the acronym.
4. Name no person, hostname, account ID, IP address or image registry. Text sent to
   ElevenLabs leaves the machine.
5. For a before-and-after demo, give each state its own sentence. The first script had
   four: the command runs, the policy activates, the same command is blocked, the alert
   appears.
6. Claim only what the frame proves. The alerts list held older blocks from the same day, so
   the script claimed only "a new alert at the top".
7. Write in plain American English for a listener. "This time it is blocked, with permission
   denied" beats "the execution is subsequently prevented".
8. Tell it as a story, not a feature list. Open a section on the problem or the source of
   truth, then the reveal. "Start with one list. Every user, group and role across your cloud
   accounts" beats "The identity list shows every user, group and role".

## Jev Judges the Narration Before It Leaves the Machine

A regex cannot tell the product name "KubeArmor" from a hostname, or "a Kubernetes cluster"
from a real cluster name. Jev can. In a test on synthetic lines, Jev scored a line naming a
pod, a namespace and a company at 0.98 for a customer identifier, and the regex missed it.
Plain product lines scored under 0.1.

| Judgment | Primitive | Policy in code |
|---|---|---|
| The line names a person, company, host, IP, ID, image path, or a named cluster, pod or namespace | Noul per line | Block the voice run at 0.7 or above. Plain lines scored 0.51 to 0.57 at the old 0.5 |
| A voice may mispronounce or spell out a term in the line | Noul per line | Warn at 0.6 or above |
| A caption cue is setup, navigation, content, off-track or wrap-up | Choice per cue | Mark setup, off-track and wrap-up as cut leads |

Every question goes in one request, so Jev reads the state once. The thresholds sit in
`jev.py`, so changing one needs no new call. When Jev is off or a call fails, the code
patterns still run, so the gate never fails open on IPs, hostnames or long IDs.

Keep these jobs in code, where Jev adds nothing: cut times, change-event scores, crop
rectangles, speeds and every frame decision.

## The Voice Settings That Worked

The house voice is Alice (`Xb7hH8MSUJpSbSDYk0k2`), British female, on `eleven_v4`, with
stability 0.45, similarity 0.8, style 0.35 and speed 1.0. It reads about 148 words a minute,
so `PACE.vo_tempo` stays at 1.0. The old Brian voice on v3 needed 1.08 and still sounded slow.
v4 accepts audio tags such as `[intrigued]`, `[confident]` and `[excited]` at the start of a
line, and does not speak them. Run `python scripts/eleven.py sample "<neutral sentence>"` to
hear the shortlist. Use a sentence with no customer detail.

The Jev gate needs the product's generic words in `PRODUCT_TERMS` in `jev.py`. Without them,
"copies it into a Kubernetes secret" scored 0.69 as a customer identifier. Add words for one
project with `JEV_TERMS = [...]` in its `edit.py`. A resource name such as "mysql pass" still
scores above 0.5, so describe the thing instead of naming it.

The `qc.py voice` command transcribes each line locally. A mismatch on a word means rewrite the line:
"Policies lists the policies" was heard as "Policies list", so the line became "The policies
tab lists". A mismatch on digits ("94" for "ninety four") is the transcriber, not the voice.

## Tool Pitfalls on This Machine

- `ffmpeg` on PATH is ImageMagick's 4.2 build. The scripts pick the chocolatey 7.x build
  first. Set `FFMPEG` and `FFPROBE` to override.
- The ElevenLabs keys cannot read models or voices (`models_read`, `voices_read` missing).
  Synthesis works. Use premade voice IDs. `eleven_v4` exists, which was confirmed by a test call on
  2026-10-05.
- `keys.py elevenlabs` can return a slot with 2 credits left, because its 1-character probe
  still fits. `eleven.py` reads slots 1 to 6 from the `.env` itself and moves to the next slot
  on `quota_exceeded`, so a run never stops on a nearly empty slot.
- `faster-whisper` on this machine has no CUDA `cublas64_12.dll`. Pass `device="cpu"`.
- The free plan blocks `mp3_44100_192`. `eleven.py` falls back to 128 kbps on its own.
- A Bash heredoc that holds a Python script with nested quotes can fail to parse. Write the
  patch to a `.py` file and run it.
- `faster-whisper` downloads `small.en` once, then runs offline.

## Two Reports Bracket Every Render

Before the render, report the edit map: one table per section with source in and out, speed,
framing, callouts and the voiceover line, then a numbered list of ambiguities. `vedit.py map`
writes the table.

After the render, report the output path, the duration, the resolution and a QC table. Each
row is a requirement from the brief and the evidence that it passed. Say which checks ran
and which did not. Never claim a check that never ran.
