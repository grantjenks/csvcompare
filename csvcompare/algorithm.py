from functools import partial

from .levenshtein import Edit, diff, match_cost

def old_row_len(old, new):
    return len(old)

def new_row_len(old, new):
    return len(new)

def alter_cost(old, new):
    return diff(old, new, score_only=True) + 0.001

def remove_value(old, pos, new, loc):
    return [('remove', (value, None)) for value in old[pos]]

def insert_value(old, pos, new, loc):
    return [('insert', (None, value)) for value in new[loc]]

def match_value(old, pos, new, loc):
    return [('match', (value, value)) for value in new[loc]]

def alter_value(old, pos, new, loc):
    return diff(old[pos], new[loc])

row_edits = {
    'remove': Edit(-1, 0, old_row_len, remove_value),
    'insert': Edit(0, -1, new_row_len, insert_value),
    'match': Edit(-1, -1, match_cost, match_value),
    'alter': Edit(-1, -1, alter_cost, alter_value),
}

csv_file_diff = partial(diff, edits=row_edits)
