"""Per-meeting one-line summaries."""
from words import meeting_totals


def summarize(rows):
    totals = meeting_totals(rows)
    return {m: f"{m}: {n} words" for m, n in sorted(totals.items())}


def top_speakers(rows, k=5):
    from speakers import per_speaker

    counts = per_speaker(rows)
    ranked = sorted(counts.items(), key=lambda kv: -kv[1])
    return ranked[:k]
