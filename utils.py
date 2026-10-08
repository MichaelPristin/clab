"""Small shared utilities."""


def human_ms(ms):
    seconds = ms // 1000
    return f"{seconds // 60}m{seconds % 60:02d}s"


def clamp(value, lo, hi):
    return max(lo, min(hi, value))


def meeting_series(meeting_id):
    """ES2002a -> ES."""
    return meeting_id[:2]


def batch_label(index):
    """1-based batch index -> filename stem."""
    return f"batch_{index:02d}"
