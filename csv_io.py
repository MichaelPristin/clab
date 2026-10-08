"""CSV readers/writers for the batch files."""
import csv
from pathlib import Path


def read_rows(path):
    with open(path, newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def iter_batch_files(root):
    return sorted(Path(root).glob("batch_*.csv"))


def row_count(path):
    with open(path, newline="", encoding="utf-8") as fh:
        return sum(1 for _ in fh) - 1
