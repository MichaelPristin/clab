"""Shared constants for the AMI subsample pipeline."""
from pathlib import Path

BATCH_DIR = Path("data")
BATCH_SIZE = 100
CSV_HEADER = ["meeting_id", "speaker", "start_ms", "end_ms", "text"]
AMI_PREFIXES = ("ES", "IS", "TS", "PS", "MS", "EN", "IN")


def is_meeting_id(value):
    """ES2002a-style IDs: 2-letter series, 4 digits, one letter."""
    return (
        len(value) == 7
        and value[:2] in AMI_PREFIXES
        and value[2:6].isdigit()
        and value[6].isalpha()
    )
