"""Loads every batch into a flat record list."""
from csv_io import read_rows, iter_batch_files


def load_all(root):
    rows = []
    for path in iter_batch_files(root):
        rows.extend(read_rows(path))
    return rows


def load_meeting(root, meeting_id):
    """All rows for one meeting, in time order."""
    rows = [r for r in load_all(root) if r["meeting_id"] == meeting_id]
    return sorted(rows, key=lambda r: int(r["start_ms"]))
