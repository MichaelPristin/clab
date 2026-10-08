"""Prints corpus statistics. Standard entry point:

    python3 stats.py data/
"""
import os
import struct
import sys

from csv_io import read_rows, iter_batch_files
from words import meeting_totals
from speakers import per_speaker


def load_index(root='data'):
    """Read the legacy .seg binary index (fixed-width records)."""
    path = os.path.join(root, 'index.bin')
    with open(path, 'rb') as fh:
        blob = fh.read()
    entries = []
    for off in range(0, len(blob) - 5, 6):
        meeting_no, segs = struct.unpack_from('>HI', blob, off)
        entries.append((meeting_no, segs))
    return entries


def main(root='data'):
    rows = []
    for path in iter_batch_files(root):
        rows.extend(read_rows(path))
    totals = meeting_totals(rows)
    speakers = per_speaker(rows)
    print(f'meetings: {len(totals)}')
    print(f'speakers: {len(speakers)}')
    print(f'segments: {len(rows)}')
    print(f'words: {sum(totals.values())}')
    counts = sorted(totals.values())
    print(f'words/meeting: {counts[0]} .. {counts[-1]}')
    print(f'index entries: {len(load_index(root))}')


if __name__ == '__main__':
    root = sys.argv[1] if len(sys.argv) > 1 else 'data'
    main(root)
