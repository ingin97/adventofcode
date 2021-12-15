# lines = [
# 'fs-end',
# 'he-DX',
# 'fs-he',
# 'start-DX',
# 'pj-DX',
# 'end-zg',
# 'zg-sl',
# 'zg-pj',
# 'pj-he',
# 'RW-he',
# 'fs-DX',
# 'pj-RW',
# 'zg-RW',
# 'start-pj',
# 'he-WI',
# 'zg-he',
# 'pj-fs',
# 'start-RW',
# ]
# lines = [
#   'dc-end',
#   'HN-start',
#   'start-kj',
#   'dc-start',
#   'dc-HN',
#   'LN-dc',
#   'HN-end',
#   'kj-sa',
#   'kj-HN',
#   'kj-dc',
# ]
lines = [
  'start-A',
  'start-b',
  'A-c',
  'A-b',
  'b-d',
  'A-end',
  'b-end',
]



from collections import defaultdict
from random import randint

filename = '2021/12/input.txt'
with open(filename) as file:
  lines = file.readlines()
  lines = [line.strip() for line in lines]

adjacent_caves = defaultdict(list)

for line in lines:
  [_from, _to] = line.split('-')
  if _to != 'start':
    adjacent_caves[_from].append(_to)
  if _from != 'start':
    adjacent_caves[_to].append(_from)

paths = []
def search(path): 
  current = path[-1]

  if current == 'end':
    paths.append(path)
    return

  neighbours = adjacent_caves[current]

  for cave in neighbours:
    if cave.islower() and not isValid(cave, path):
      # Dead end
      continue
    else:
      search([*path, cave])

from collections import defaultdict
def isValid(cave, path):
  if cave not in path:
    return True
  
  counts = defaultdict(int)
  for c in path:
    if c.islower():
      counts[c] += 1
  
  for count in counts.values():
    if count >= 2:
      return False

  return True
    

search(['start'])


print(len(paths))

# paths = [list(x) for x in set(tuple(x) for x in paths)]
# for path in paths:
#   print(path)
# print(len(paths))