"""Orchestrates the reference pipeline (see stats.py for the
standard entry point)."""
from csv_io import iter_batch_files
from words import meeting_totals
from speakers import roster


def run(root='data'):
    files = list(iter_batch_files(root))
    return {'batches': len(files)}


def describe(root='data'):
    """Human-readable one-liner for logs."""
    info = run(root)
    return f"corpus with {info['batches']} batches"
