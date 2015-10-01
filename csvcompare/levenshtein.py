from sys import hexversion
from collections import defaultdict, namedtuple

if hexversion < 0x03000000:
    range = xrange

infinity = float('inf')

Edit = namedtuple('Edit', 'old new cost data')

def one(old, new):
    return 1

def match_cost(old, new):
    return 0 if old == new else infinity

def alter_cost(old, new):
    return 1 if old != new else infinity

def remove_value(old, pos, new, loc):
    return (old[pos], None)

def insert_value(old, pos, new, loc):
    return (None, new[loc])

def change_value(old, pos, new, loc):
    return (old[pos], new[loc])

edits = {
    'remove': Edit(-1, 0, one, remove_value),
    'insert': Edit(0, -1, one, insert_value),
    'match': Edit(-1, -1, match_cost, change_value),
    'alter': Edit(-1, -1, alter_cost, change_value),
}

Score = namedtuple('Score', 'value how')

def diff(old, new, score_only=False, edits=edits):
    scores = defaultdict(dict)

    scores[-1][-1] = Score(-1, 'initial')

    for index, value in enumerate(new):
        scores[-1][index] = Score(index, 'insert')

    for index, value in enumerate(old):
        scores[index][-1] = Score(index, 'remove')

    def score(pos, loc, name):
        edit = edits[name]
        prev = scores[pos + edit.old][loc + edit.new].value
        cost = edit.cost(old[pos], new[loc])
        return Score(prev + cost, name)

    for pos in range(len(old)):
        for loc in range(len(new)):
            scores[pos][loc] = min(score(pos, loc, name) for name in edits)

    if score_only:
        return scores[pos][loc].value + 1

    result = []

    while scores[pos][loc].how != 'initial':
        _, name = scores[pos][loc]
        edit = edits[name]

        result.append((name, edit.data(old, pos, new, loc)))

        pos += edit.old
        loc += edit.new

    result.reverse()

    return result
