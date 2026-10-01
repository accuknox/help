"""Helpers an edit.py imports to write its edit decision list.

    from editkit import c, h, A

c(a, b, speed=1.0, view=FULL, ann=[...])   play source a..b seconds at `speed`
h(t, dur, view=FULL, ann=[...])            freeze source frame t for `dur` seconds
A(rect, text, pos, st, at)                 a highlight box, with an optional label

Views are (x, y, w) in SOURCE pixels. The height follows the output aspect ratio.
A view pair (FROM, TO) eases from one framing to the other over 0.8 s.
"""


def c(a, b, speed=1.0, view=None, ann=None):
    assert b > a, f"clip out {b} must be after in {a}"
    return dict(a=a, b=b, speed=speed, view=view, ann=ann or [])


def h(t, dur, view=None, ann=None):
    return dict(hold=t, dur=dur, view=view, ann=ann or [])


def A(rect, text=None, pos="below", st=(0, 99999), at=None):
    """rect=(x, y, w, h) source pixels. st=(from, to) source seconds the box is visible.

    pos places the label below, above, right or left of the box. at=(x, y) in source
    pixels pins the label instead, for when the automatic spot covers UI text.
    """
    return dict(rect=rect, text=text, pos=pos, st=st, at=at)
