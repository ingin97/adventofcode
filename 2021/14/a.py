lines = [
'NNCB',
'',
'CH -> B',
'HH -> N',
'CB -> H',
'NH -> C',
'HB -> C',
'HC -> B',
'HN -> C',
'NN -> C',
'BH -> H',
'NC -> B',
'NB -> B',
'BN -> B',
'BB -> N',
'BC -> B',
'CC -> N',
'CN -> C',
]


# filename = '2021/14/input.txt'
# with open(filename) as file:
#   lines = file.readlines()
#   lines = [line.strip() for line in lines]


template = list(lines[0])
pairs = {}

for line in lines[2:]:
  [pair, insert] = line.split(' -> ')
  pairs[pair] = insert


for step in range(10):
  temp = list(template)
  last = ''
  i = 0
  for current in temp:
    if last+current in pairs.keys():
      template.insert(i, pairs[last+current])
      i += 1
    last = current
    i += 1

from collections import defaultdict
counts = defaultdict(int)
for x in template:
  counts[x] += 1

values = list(counts.values())
values.sort()
print(values[-1] - values[0])
