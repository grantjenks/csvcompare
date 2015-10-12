from .algorithm import csv_file_diff

try:
    from .display import html
except ImportError:
    pass

__title__ = 'csvcompare'
__version__ = '0.1.2'
__build__ = 0x000102
__author__ = 'Grant Jenks'
__license__ = 'Apache 2.0'
__copyright__ = 'Copyright 2015 Grant Jenks'
