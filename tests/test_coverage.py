import csv
import os.path as path
from csvcompare import csv_file_diff

BASE_DIR = path.dirname(path.realpath(__file__))

def test_001():
    with open(path.join(BASE_DIR, 'old-001.csv'), 'r') as reader:
        old_cells = tuple(csv.reader(reader))
    with open(path.join(BASE_DIR, 'new-001.csv'), 'r') as reader:
        new_cells = tuple(csv.reader(reader))
    assert csv_file_diff(old_cells, new_cells) == [
        ('remove', [('remove', ('', None)), ('remove', ('', None)), ('remove', ('', None))]),
        ('alter', [('remove', ('', None)), ('match', ('foo', 'foo')), ('match', ('bar', 'bar'))]),
        ('alter', [('remove', ('', None)), ('match', ('0', '0')), ('match', ('1', '1'))]),
        ('insert', [('insert', (None, '8')), ('insert', (None, '9'))]),
        ('alter', [('remove', ('', None)), ('match', ('2', '2')), ('alter', ('5', '3'))]),
        ('alter', [('remove', ('', None)), ('match', ('4', '4')), ('match', ('5', '5'))]),
    ]
