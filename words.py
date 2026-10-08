"""Word-count helpers for verbatim-style text."""


def count(text):
    return len(text.split())


def meeting_totals(rows):
    totals = {}
    for r in rows:
        totals[r["meeting_id"]] = totals.get(r["meeting_id"], 0) + count(r["text"])
    return totals


def speaker_totals(rows):
    totals = {}
    for r in rows:
        totals[r["speaker"]] = totals.get(r["speaker"], 0) + count(r["text"])
    return totals
