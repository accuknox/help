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

PACE = dict(base=1.15, vo_tempo=1.0)    # Alice on v4 sets her own pace. Above 1.05 sounds rushed

# Jev, the TypeSafe judgment model. "narration" checks every voiceover line for customer
# identifiers and hard-to-voice words before ElevenLabs sees it. "all" also triages the
# caption cues, which sends the call transcript to TypeSafe. "off" keeps code checks only.
# A brief that allows no outside service except ElevenLabs means "off".
JEV = "narration"

# Voice: Alice, British female, on eleven_v4, the skill default. Set VOICE = dict(...) only
# to change it.

# The first 5 s. 2 or 3 shots of the strongest proof in the recording, then the logo slam.
# Each shot: t= a still second, or a= b= a range played across the shot. view= one view or a
# (FROM, TO) pair the camera pushes through. The headline names what that frame shows.
HOOK = dict(
    line="[intrigued] [about ten words that end by 4.5 s]",
    shots=[
        dict(t=0.0, view=None, kicker="[where we are]", text="[2 to 3 word fact]"),
        dict(t=0.0, view=None, kicker="[where we are]", text="[2 to 3 word fact]"),
    ],
    product="[product name]",
    tagline="[3 to 5 word promise]",
    footer="Confidential. Contains customer environment details. Not for external distribution.",
)
INTRO = None                             # the hook replaces the old title card

# The end card: logo, one line, a call to action and the closing voice line.
OUTRO = dict(
    title="[one line the viewer should remember]",
    cta="help.accuknox.com",
    sub="accuknox.com",
    backdrop_t=0.0,                      # a source second with a clean, representative screen
    line="[closing narration, one sentence]",
)
BRAND = dict(watermark="br")             # the logo corner on every product frame, or None

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
