# scripts/

Repo tooling for the help docs.

| File | What it does |
|---|---|
| [gen_docs_readmes.py](gen_docs_readmes.py) | Writes a small set of folder index READMEs under `docs/`: a master `docs/README.md` plus one `README.md` in each top-level folder that directly holds markdown pages (how-to, use-cases, etc.). Each lists that folder's pages with a description from each page's front matter. It deliberately skips image and asset folders and does not descend into nested subfolders. It is self-cleaning: any index it previously wrote that now falls out of scope is removed. |
| [install-git-hooks.sh](install-git-hooks.sh) | Points this clone's git hooks at `.githooks/` (`git config core.hooksPath .githooks`). Run once after cloning. |

## Folder index READMEs

The generated READMEs exist only for humans and tools reading the repo (an LLM
can read one folder index instead of opening every file). They are **not
published** to the live site: `exclude_docs: README.md` in `mkdocs.yml` drops
them from the build, and `hooks/copy_md_source.py` skips them too.

Regenerate manually:

```sh
python scripts/gen_docs_readmes.py
```

The generator is idempotent, it only rewrites a README when its content changes.

## Keeping them current

`.githooks/pre-commit` runs the generator on every commit that touches `docs/`
and stages any README it updated. Enable it once per clone:

```sh
sh scripts/install-git-hooks.sh
```
