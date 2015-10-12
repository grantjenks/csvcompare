import argparse, csv

from .algorithm import csv_file_diff
from .display import html

parser = argparse.ArgumentParser(
    prog='csvcompare',
    description='CSV file comparison.',
    epilog='Copyright 2015 Grant Jenks'
)

parser.add_argument(
    'old_file',
    type=argparse.FileType('r'),
    help='Path to old CSV file',
)
parser.add_argument(
    'new_file',
    type=argparse.FileType('r'),
    help='Path to new CSV file'
)

args = parser.parse_args()

old_cells = list(csv.reader(args.old_file))
new_cells = list(csv.reader(args.new_file))

import tempfile, webbrowser

with tempfile.NamedTemporaryFile(suffix='.html') as writer:
    writer.write(html(csv_file_diff(old_cells, new_cells)))
    writer.flush()
    webbrowser.open('file://' + writer.name)
    raw_input('press Enter to exit')
