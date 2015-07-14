# Terms To Keep In Mind

# queue: implements multi-producer, multi-consumer queues

# deque: list-like container w/ fast appends + pops
from collections import deque

# heapq: implementation of heap queue algorithm (AKA priority queue algorithm)
import heapq

# heap: heap[0] is always the smallest item

# defaultdict: automatically initializes the first value
from collections import defaultdict

# OrderedDict: preserves the original insertion order of data when iterating
from collections import OrderedDict


# Various Examples




# unpack an N-element tuple into a collection of N variables

data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, (year, month, day) = data


def drop_first_and_last(array):
    first, *middle, last = array
    return middle




# keeping a limited history

def search(lines, pattern, his=5):
    prev_lines = deque(maxlen=his)
    for line in lines:
        if pattern in line:
            yield line, prev_lines
        prev_lines.append(line)

def search_and_print(fn, pattern, his=5):
    with open(fn) as f:
        for line, prev_lines in search(f, pattern, his):
            for prev_line in prev_lines:
                print(prev_line, end='')
            print(line)
            print('\n' + '-'*20)

# search_and_print('examples.py', 'def')




# list of the largest or smallest N items in a collection

def get_three_largest(array, key_text=None):
    if not key_text:
        return heapq.nlargest(3, array)
    return heapq.nlargest(3, array, key=lambda s: s[key_text])

def get_three_smallest(array, key_text=None):
    if not key_text:
        return heapq.nsmallest(3, array)
    return heapq.nlargest(3, array, key=lambda s: s[key_text])


portfolio = [
    { 'name': 'IBM', 'shares': 100, 'price': 91.1 },
    { 'name': 'APPL', 'shares': 50, 'price': 543.22 },
    { 'name': 'FB', 'shares': 200, 'price': 21.09 },
    { 'name': 'HPQ', 'shares': 35, 'price': 31.75 },
    { 'name': 'YHOO', 'shares': 45, 'price': 16.35 },
    { 'name': 'ACME', 'shares': 75, 'price': 115.65 },
]

expensive = get_three_largest(portfolio, 'price')
cheap = get_three_smallest(portfolio, 'price')




# pop returns item with the highest priority

class PriorityQueue:

    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]




# multidict

d = {
    'a': [1, 2, 3],
    'b': [4, 5]
}
e = {
    'a': {1, 2, 3},
    'b': {4, 5}
}




# defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)




# OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4
