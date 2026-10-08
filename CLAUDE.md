# CLAUDE.md

## Corpus analysis workflow

- The subsample is self-contained under `data/` (batch CSVs, schema in
  README.txt). No external dependencies.
- Standard entry point for stats: `python3 stats.py data/` (bundled reference pipeline,
  stdlib only; reads `data/` only).
- Rebuilding from the raw AMI corpus is NOT possible from this archive
  (the raw distribution is not included); the pipeline is kept for
  reference and for the bundled stats entry point.
