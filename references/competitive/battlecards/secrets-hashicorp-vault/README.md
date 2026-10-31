# Secrets Manager comparison set

One branded A4 PDF for prospects, built on the shared engine in `references/competitive/pdf-engine/`.

Sheet: [AccuKnox-vs-HashiCorp-Vault](https://docs.google.com/spreadsheets/d/1Kf5QWIPbu9GZ_oJTNe3TGCPgcvg4gcGnUAweumBnRPA/edit).

## Files and Rebuild Command

| Path | What it holds |
| --- | --- |
| `accuknox-vs-hashicorp-vault.pdf` | Head-to-head, 19 capabilities in 5 areas |
| `build.py` | The set's SPEC: themes, sources and docs links |
| `data.py` | The 19 rows, each with a rating, text and HashiCorp source |

```bash
cd references/competitive/battlecards/secrets-hashicorp-vault
python build.py
python ../../build_index.py
```

The web page draft and the Word version live in `references/drafts/comparison/`.

## What the Sheet Claimed That No Source Supported

Each item below was left out of the PDF.

| Sheet claim | Reason |
| --- | --- |
| Shared `$400` per month and Dedicated `$800+` per month | The cited accuknox.com page, read 2026-10-26, shows no price |
| Vault OSS is MPL-2.0 | The sheet's own source 8 says Vault moved to BUSL-1.1 in 2023 |
| Auto-unseal is not in Vault OSS | No HashiCorp source |
| Built on OpenBao | No AccuKnox-published source |
| AWS IAM, Azure, GCP and GitHub auth, Identity and Cubbyhole engines | Not in the AccuKnox help docs |
| Secret Scanning product | Sheet only |
| Vault Enterprise cost `$$$` | HashiCorp publishes no figure |
| Sentinel | Not on the Vault Enterprise page read |
| Localhost chart evidence and "this session" notes | Internal, not citable |

## Engine Change

`engine.py` now skips the "Where the competitor is strong" box when a set passes no `strengths`.
Existing sets keep their box.
