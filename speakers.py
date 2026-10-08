"""Speaker roster utilities."""


def roster(rows):
    seen = []
    for r in rows:
        if r["speaker"] not in seen:
            seen.append(r["speaker"])
    return seen


def per_speaker(rows):
    counts = {}
    for r in rows:
        counts[r["speaker"]] = counts.get(r["speaker"], 0) + 1
    return counts


def per_meeting_roster(rows):
    """Meetings -> ordered list of distinct speakers."""
    out = {}
    for r in rows:
        m = r["meeting_id"]
        if m not in out:
            out[m] = []
        if r["speaker"] not in out[m]:
            out[m].append(r["speaker"])
    return out
