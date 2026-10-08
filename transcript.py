"""Segment row model helpers."""


def duration_ms(row):
    return int(row["end_ms"]) - int(row["start_ms"])


def is_overlap(row_a, row_b):
    return not (int(row_a["end_ms"]) <= int(row_b["start_ms"]) or int(row_b["end_ms"]) <= int(row_a["start_ms"]))


def overlaps(rows):
    """Count overlapping segment pairs (ihm mics overlap a lot)."""
    n = 0
    for i, a in enumerate(rows):
        for b in rows[i + 1:]:
            if int(b["start_ms"]) > int(a["end_ms"]):
                break
            if is_overlap(a, b):
                n += 1
    return n
