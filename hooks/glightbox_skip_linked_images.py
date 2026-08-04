"""Keep the lightbox off any image that already sits inside something clickable.

mkdocs-glightbox decides whether to wrap an image by looking at its *direct*
parent only. Every Neoteroi card puts its icon a few levels deeper than the
card's own anchor:

    <a href="/use-cases/cspm/">
      <div><div class="nt-card-image tags"><img src="CSPM.svg"></div>...</div>
    </a>

so the plugin wraps the icon in a second anchor. Nested anchors are illegal
HTML, the browser splits them apart, the card's link is destroyed, and clicking
an icon opens the lightbox instead of navigating to the page.

The same thing happens on the homepage, where the carousel cards and the module
picker rows are plain divs carrying an onclick handler. Wrapping their images
means the lightbox eats the click and the carousel never rotates.

This patches the plugin's skip check to walk the whole ancestor chain and leave
an image alone if anything above it is a link or has an onclick handler, no
matter how deeply it is nested. Screenshots in page bodies are untouched and
still open in the lightbox.

It also skips images that declare a width or height of 64px or less. Those are
inline glyphs sitting next to a line of text, and enlarging an 18px icon to fill
the viewport is never what the reader wanted. Anything larger is treated as a
screenshot. The `{: .off-glb }` opt-out still works for the rest.
"""

# Declared px size at or below which an image counts as an inline glyph.
MAX_INLINE_ICON_PX = 64

from mkdocs_glightbox.plugin import LightboxPlugin

_original_should_skip_img = LightboxPlugin._should_skip_img


def _inside_clickable(node):
    parent = node.parent
    while parent is not None:
        if parent.tag == "a" or "onclick" in parent.attributes:
            return True
        parent = parent.parent
    return False


def _is_inline_icon(img):
    for attr in ("width", "height"):
        raw = (img.attributes.get(attr) or "").strip().rstrip("px").strip()
        if raw.isdigit() and int(raw) <= MAX_INLINE_ICON_PX:
            return True
    return False


def _should_skip_img(self, img, skip_classes, plugin_config, meta):
    if _inside_clickable(img) or _is_inline_icon(img):
        return True
    return _original_should_skip_img(self, img, skip_classes, plugin_config, meta)


LightboxPlugin._should_skip_img = _should_skip_img
