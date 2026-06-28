"""
MkDocs hook: publish each page's raw Markdown alongside its built HTML.

For every documentation page (e.g. docs/foo/bar.md), this hook writes a copy
of the original markdown to the built site at the URL path the page is served
from, suffixed with `index.md`. Example:

    docs/foo/bar.md   ->   site/foo/bar/index.html  (rendered page)
                      ->   site/foo/bar/index.md    (raw source, fetchable)

Client-side JS can then fetch `<page-url>index.md` to get the original markdown
for "Copy page", "View as Markdown", and LLM-prefill buttons. No plugins, no
external deps, just a native MkDocs hook.
"""

import os
import shutil


def on_post_build(config, **kwargs):
    docs_dir = config["docs_dir"]
    site_dir = config["site_dir"]
    use_dir_urls = config.get("use_directory_urls", True)

    for root, _dirs, files in os.walk(docs_dir):
        for fname in files:
            if not fname.endswith(".md"):
                continue
            # Auto-generated folder index files are repo-only; never publish them.
            if fname == "README.md":
                continue

            src_path = os.path.join(root, fname)
            rel = os.path.relpath(src_path, docs_dir).replace(os.sep, "/")

            if use_dir_urls:
                if rel.endswith("/index.md") or rel == "index.md":
                    dest_rel = rel
                else:
                    dest_rel = rel[:-3] + "/index.md"
            else:
                dest_rel = rel

            dest_path = os.path.join(site_dir, dest_rel.replace("/", os.sep))
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)
            shutil.copyfile(src_path, dest_path)
