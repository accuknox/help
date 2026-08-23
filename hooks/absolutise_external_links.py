"""Point relative links inside injected upstream markdown at their real home.

`docs/support-matrix/kubearmor-support-matrix.md` pulls two sections out of
`kubearmor/KubeArmor` with `external_markdown()`. That upstream file ends with
reference-style link definitions written for the KubeArmor docs tree:

    [Observability]: workload_visibility.md
    [Network-Segmentation]: network_segmentation.md

Neither page exists in this repo, so `mkdocs build --strict` fails on two
warnings nobody here can fix by editing a local file. The targets are real, they
just live in the other repository.

This rewrites a bare `*.md` reference definition into the matching URL on
GitHub, for pages built from external markdown only. Links that resolve inside
this repo are untouched, and a genuinely broken local link still fails the
build, which is the whole point of running strict mode.

Registered in `mkdocs.yml` under `hooks:`.
"""

from __future__ import annotations

import re

# Pages that inject markdown from another repository, and the raw base each
# one's relative links should resolve against. Add a row when a new page starts
# using external_markdown().
EXTERNAL_SOURCES: dict[str, str] = {
    "support-matrix/kubearmor-support-matrix.md":
        "https://github.com/kubearmor/KubeArmor/blob/main/getting-started/",
}

# A reference-style definition whose target is a bare relative markdown file.
# `[Observability]: workload_visibility.md` matches. An absolute URL, an anchor
# and a path that climbs out of the directory all do not.
REF_DEFINITION = re.compile(
    r"^(?P<indent>[ \t]*)"
    r"\[(?P<label>[^\]^\n]+)\]:[ \t]+"
    r"(?P<target>(?!https?://|/|#|\.\./)[A-Za-z0-9._-]+\.md)"
    r"(?P<rest>[ \t]+[\"'(].*)?$",
    re.M,
)


def on_page_markdown(markdown: str, page, config, files):  # noqa: ANN001
    """Absolutise relative reference definitions on external-markdown pages."""
    base = EXTERNAL_SOURCES.get(page.file.src_uri)
    if not base:
        return markdown

    def repl(m: re.Match[str]) -> str:
        return (f"{m.group('indent')}[{m.group('label')}]: "
                f"{base}{m.group('target')}{m.group('rest') or ''}")

    return REF_DEFINITION.sub(repl, markdown)
