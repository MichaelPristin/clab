AMI MEETING TRANSCRIPTS - subsample text set
Version 2.0  (packaged 2026-08-31)

WHAT THIS IS
------------
A text-and-timing subsample of the AMI Meeting Corpus (Carletta et al.,
2006), individual headset microphone (ihm) segment rows:
20 meetings, 72 speakers,
1900 segment rows, 14227 transcript words
(13 - 1967 per meeting).
This archive carries NO audio -- text and segment timings only.

FILES
-----
  data/batch_01.csv .. data/batch_19.csv   19 files,
                     fixed-size 100-row batches (the
                     remainder joins the last batch)
  *.py               the pipeline that produced the CSVs, for reference.
                     Rebuilding requires the raw AMI distribution, which is
                     NOT included here.

SCHEMA
------
  meeting_id   AMI meeting ID (e.g. ES2002a)
  speaker      AMI speaker ID
  start_ms     segment start, milliseconds from meeting start
  end_ms       segment end
  text         verbatim segment text (AMI transcripts are uppercase,
               disfluent spontaneous speech)

SOURCE & LICENCE
----------------
  Carletta, J. et al. (2006). The AMI Meeting Corpus: A
  Pre-announcement. MLMI'06. The public AMI releases are distributed
  by the AMI consortium under CC BY 4.0; this subsample carries text
  and segment timings only (no audio) and follows the same terms.
  Cite the original corpus in any derived work.
