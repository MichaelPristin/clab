"""Fixed-size batching of the combined segment table."""
from pathlib import Path


def batch_files(batch_dir):
    return sorted(Path(batch_dir).glob("batch_*.csv"))


def expected_rows(n_files, batch_size):
    """Rows per batch is fixed; the remainder joins the last batch."""
    return n_files * batch_size


def batch_index(path):
    """batch_07.csv -> 7 (sort order helper)."""
    return int(Path(path).stem.split("_")[1])
