# Terms To Keep In Mind

# queue: implements multi-producer, multi-consumer queues

# deque: list-like container w/ fast appends + pops
from collections import deque, Counter

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

d = defaultdict(list)
for k, v in pairs:
    d[k].append(v)


d = {}  # regular dictionary
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('b', []).append(4)

d = {}
for k, v in pairs:
    if k not in d:
        d[k] = []
    d[k].append(v)




# OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4

for k in d:
    print(k, d[k])




prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75,
}

# zip: swaps k, v
min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))
sorted_prices = sorted(zip(prices.values(), prices.keys()))




a = {
    'x': 1,
    'y': 2,
    'z': 3,
}

b = {
    'w': 1,
    'x': 7,
    'y': 9,
}

# Find keys in common
a.keys() & b.keys()

# Find keys in a that are not in b
a.keys() - b.keys()

# Find (key, value) pairs in common
a.items() & b.items()

# Make a new dictionary with certain keys removed
c = {key:a[key] for key in a.keys() - {'z', 'w'}}




# Eliminate the duplicate values in a sequence, but preserve the order of the remaining items

def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = key(item) if key else item
        if val not in seen:
            yield item
            seen.add(val)

>>> a
[1, 5, 2, 1, 9, 5, 10]
>>> set(a)
{1, 2, 10, 5, 9}




# Clean up slice indices

record = '................100           ......    ............'
cost = int(record[20:32]) * float(record[40:48]) # ugly

SHARES = slice(20,32)
PRICE = slice(40, 48)
cost = int(record[SHARES]) * float(record[PRICE]) # better




# Determine the most frequently occuring items in a sequence.

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', 'dont', 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', 'youre', 'under'
]

word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(top_three)

morewords = ['why','are','you','not','looking','in','my','eyes']
for word in morewords:
    word_counts[word] += 1
# or word_counts.update(morewords)




# Sorting a dictionary according to one or more values.

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004},
]

from operator import itemgetter

rows_by_uid = sorted(rows, key=itemgetter('uid'))
rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_lfname = sorted(rows, key=itemgetter('lname','fname'))

rows_by_fname = sorted(rows, key=lambda r: r['fname'])
rows_by_lfname = sorted(rows, key=lambda r: (r['lname'],r['fname']))




# Sorting objects of the same Class

class User:
    def __init__(self, user_id):
        self.user_id = user_id
    def __repr__(self):
        return 'User({})'.format(self.user_id)

users = [User(23), User(3), User(99)]
sorted(users, key=lambda u: u.user_id)
# [User(3), User(23), User(99)]
from operator import attrgetter
sorted(users, key=attrgetter('user_id'))

by_name = sorted(users, key=attrgetter('last_name', 'first_name'))




# You have a sequence of dictionaries or instances and you want to iterate
# over the data in groups based on the value of a particular field, such
# as date.

rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 N 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 N ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 N GRANVILLE', 'date': '07/04/2012'},
]

from operator import itemgetter
from itertools import groupby

rows.sort(key=itemgetter('date'))

for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for item in items:
        print('    ', i)


from collections import defaultdict
rows_by_date = defaultdict(list)
for row in rows:
    rows_by_date[row['date']].append(row)

for row in rows_by_date['07/01/2012']:
    print(row)




# Extracting values from a sequence using some criteria.

mylist = [1, 4, -5, 10, -7, 2, 3, -1]
[n for n in mylist if n > 0]
# [1, 4, 10, 2, 3]
[n for n in mylist if n < 0]
# [-5, -7, -1]

pos = (n for n in mylist if n > 0)
for x in pos:
    print(x)

values = ['1', '2', '-3', '-', '4', 'N/A', '5']

def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False

intvalues = list(filter(is_int, values))
print(intvalues)


>>> mylist = [1, 4, -5, 10, -7, 2, 3, -1]
>>> import math
>>> [math.sqrt(n) for n in mylist if n > 0]
[1.0, 2.0, 3.1622776601683795, 1.4142135623730951, 1.7320508075688772]

>>> clip_neg = [n if n > 0 else 0 for n in mylist]
>>> clip_neg
[1, 4, 0, 10, 0, 2, 3, 0]
>>> clip_pos = [n if n < 0 else 0 for n in mylist]
>>> clip_pos
[0, 0, -5, 0, -7, 0, 0, -1]




addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 N 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 N ADDISON',
    '4801 N BROADWAY',
    '1039 N GRANVILLE',
]
counts = [0, 3, 10, 4, 1, 7, 6, 1]

>>> from itertools import compress
>>> more5 = [n > 5 for n in counts]
>>> more5
[False, False, True, False, False, True, True, False]
>>> list(compress(addresses, more5))
['5800 E 58TH', '4801 N BROADWAY', '1039 W GRANVILLE']




# Make a dictionary that is a subset of another dictionary

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75,
}
# p1 = { k:v for k,v in prices.items() if v > 200 }
p1 = dict((k,v) for k,v in prices.items() if v > 200)

tech_names = { 'AAPL', 'IBM', 'HPQ', 'MSFT' }
p2 = { k:v for k,v in prices.items() if k in tech_names }
# p2 = { k:prices[k] for k in prices.keys() & tech_names }


>>> from collections import namedtuple
>>> Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
>>> sub = Subscriber('jonesy@example.com', '2012-10-19')
>>> sub
Subscriber(addr='jonesy@example.com', joined='2012-10-19')
>>> sub.addr
'jonesy@example.com'
>>> sub.joined
'2012-10-19'
>>> len(sub)
2
>>> addr, joined = sub
>>> addr
'jonesy@example.com'
>>> joined
'2012-10-19'


def compute_cost(records):
    total = 0.0
    for record in records:
        total += record[1] * record[2]
    return total


from collections import namedtuple

Stock = namedtuple('Stock', ['name', 'shares', 'price'])

def compute_cost(records):
    total = 0.0
    for record in records:
        s = Stock(*record)
        total += s.shares * s.price
    return total




>>> s = Stock('ACME', 100, 123.45)
>>> s
Stock(name='ACME', shares=100, price=123.45)
>>> s.shares = 75
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: cant set attribute

>>> s = s._replace(shares=75)
>>> s
Stock(name='ACME', shares=75, price=123.45)




from collections import namedtuple

Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])

stock_prototype = Stock('', 0, 0.0, None, None)

def dict2stock(s):
    return stock_prototype._replace(**s)

>>> a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
>>> dict2stock(a)
Stock(name='ACME', shares=100, price=123.45, date=None, time=None)
>>> b = {'name': 'ACME', 'shares': 100, 'price': 123.45, 'date': '12/17/2012'}
>>> dict2stock(b)
Stock(name='ACME', shares=100, price=123.45, date='12/17/2012', time=None)




# transform/filter data and then execute reduction function

nums = [1, 2, 3, 4, 5]
s = sum(n * n for n in nums)


import os
files = os.listdir('dirname')
if any(fn.endswith('.py') for fn in files):
    print('There be python!')
else:
    print('Sorry, no python.')

# Output a tuple as CSV
s = ('ACME', 50, 123.45)
print(','.join(str(x) for x in s))

# Data reduction across fields of a data structure
portfolio = [
    {'name':'GOOG', 'shares':50},
    {'name':'YHOO', 'shares':75},
    {'name':'AOL', 'shares':20},
    {'name':'SCOX', 'shares':65},
]
min_shares = min(s['shares'] for s in portfolio)
min_shares = min(portfolio, key=lambda s: s['shares'])




# Combining Multiple Mappings into a Single Mapping

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}

from collections import ChainMap
c = ChainMap(a,b)
print(c['x'])
print(c['y'])
print(c['z'])

>>> values = ChainMap()
>>> values['x'] = 1
>>> values = values.new_child()
>>> values['x'] = 2
>>> values = values.new_child()
>>> values['x'] = 3
>>> values
ChainMap({'x': 3}, {'x': 2}, {'x': 1})
>>> values['x']
3
>>> values = values.parents
>>> values['x']
2
>>> values = values.parents
>>> values['x']
1
>>> values
ChainMap({'x': 1})


>>> a = {'x': 1, 'z': 3}
>>> b = {'y': 2, 'z': 4}
>>> merged = dict(b)
>>> merged.update(a)
>>> merged['x']
1
>>> merged['y']
2
>>> merged['z']
3
>>> a['x'] = 13
>>> merged['x']
1
>>> a = {'x': 1, 'z': 3}
>>> b = {'y': 2, 'z': 4}
>>> merged = ChainMap(a, b)
>>> merged['x']
1
>>> a['x'] = 42
>>> merged['x']
42




from urllib.request import urlopen

def read_data(name):
    if name.startswith(('http:','https:','ftp:')):
        return urlopen(name).read()
    return open(name).read()



from calendar import month_abbr
def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(
        m.group(2),
        mon_name,
        m.group(3)
    )



def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        return word
    return replace



def combine(src, maxsize):
    parts = []
    size = 0
    for part in src:
        parts.append(part)
        size += len(part)
        if size > maxsize:
            yield ''.join(parts)
            parts = []
            size = 0
    yield ''.join(parts)


for part in combine(sample(), 32768):
    f.write(part)




from collections import namedtuple

Token = namedtuple('Token', ['type','value'])

def generate_tokens(pat, text):
    scanner = pat.scanner(text)
    for m in iter(scanner.match, None):
        yield Token(m.lastgroup, m.group())

for token in generate_tokens(master_pat, 'foo = 42'):
    print(tok)



tokens = (tok for tok in generate_tokens(master_pat, text) if tok.type != 'WS')

for token in tokens:
    print(token)
