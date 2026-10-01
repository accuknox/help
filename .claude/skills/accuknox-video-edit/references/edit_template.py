"""Edit decision list for: __TITLE__

The render input and the edit map in one file. Every time is a SOURCE second, every
rect and view is in SOURCE pixels. Re-render with:

    python .claude/skills/accuknox-video-edit/scripts/vedit.py <this folder> render
"""
from editkit import A, c, h  # noqa: F401  (the skill's scripts folder is on sys.path)

SOURCE = "__SOURCE__"
VTT = __VTT__

# The shared-screen area: (x, y, w, h). Everything outside it, such as a webcam
# column or a participant strip, is never read. Measure it on a grabbed frame.
SHARE = (0, 0, __W__, __H__)

OUTPUT = dict(
    name="__SLUG__.mp4",
    title="__TITLE__",
    width=__OUTW__,          # never above SHARE width: no upscaling
    height=__OUTH__,
)

PACE = dict(base=1.15, vo_tempo=1.10)   # vo_tempo above 1.10 starts to sound rushed

# Jev, the TypeSafe judgment model. "narration" checks every voiceover line for customer
# identifiers and hard-to-voice words before ElevenLabs sees it. "all" also triages the
# caption cues, which sends the call transcript to TypeSafe. "off" keeps code checks only.
# A brief that allows no outside service except ElevenLabs means "off".
JEV = "narration"

VOICE = dict(voice_id="nPczCjzI2devNBz1zQrb", model="eleven_v3",
             settings={"stability": 0.5, "similarity_boost": 0.75})

# Opening card over a blurred frame of the recording. Set INTRO = None to skip it.
INTRO = dict(
    kicker="Internal review  ·  __DATE__",
    title="__TITLE__",
    subtitle="[one line: what the viewer will see]",
    footer="Confidential. Contains customer environment details. Not for external distribution.",
    backdrop_t=0.0,                      # a source second with a clean, representative screen
    line="[intro narration, one sentence]",
)

# Views: (x, y, w). Height follows the output aspect ratio. Name every view you reuse,
# because the edit map prints these names.
FULL = (0, 0, __W__)                     # [crop the browser chrome: set y to the app's top edge]

SECTIONS = {
    1: "[Section name]",
}

BEATS = [
    dict(id="B01", section=1, clips=[
        c(0.0, 5.0, ann=[A((100, 100, 200, 40), "[label the UI supports]", "below", (0.5, 5.0))]),
        h(4.96, 1.0),
    ], lines=[(0.5, "[narration: what the viewer is seeing, verifiable from the frame]")]),
]
