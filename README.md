# clab -- AMI corpus lab

Text-and-timing subsample of the AMI Meeting Corpus (Carletta et al., 2006)
for lightweight experiments: 20 meetings,
72 speakers, 1900 segment rows,
14227 transcript words (13 - 1967
per meeting). No audio -- text and segment timings only.

## Usage

Batch CSVs live under `data/` (schema in `README.txt`). The bundled
reference pipeline prints the corpus statistics:

    python3 stats.py data/

The table below was generated with that command.

| meetings | speakers | segments | words |
| --- | --- | --- | --- |
| 20 | 72 | 1900 | 14227 |

A legacy `.seg` binary index ships as `data/index.bin` (fixed-width
records; see `stats.py:load_index`).

## Source & licence

Redistributed under CC BY 4.0, following the AMI release terms. Cite:
Carletta, J. et al. (2006). The AMI Meeting Corpus: A Pre-announcement.
MLMI'06.
