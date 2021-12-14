lines = [
'fs-end',
'he-DX',
'fs-he',
'start-DX',
'pj-DX',
'end-zg',
'zg-sl',
'zg-pj',
'pj-he',
'RW-he',
'fs-DX',
'pj-RW',
'zg-RW',
'start-pj',
'he-WI',
'zg-he',
'pj-fs',
'start-RW',
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

  adjacent_caves[_from].append(_to)
  adjacent_caves[_to].append(_from)

print(adjacent_caves)

paths = []
for i in range(1000000):
  path = []
  current = 'start'
  path.append(current)
  visited = []
  visited.append(current)

  skip = False
  while current != 'end':
    temp = adjacent_caves[current][randint(0, len(adjacent_caves[current])-1)]
    if temp in visited:
      # Skip dead ends
      all_visited = True
      for cave in adjacent_caves[current]:
        if cave not in visited:
          all_visited = False
      if all_visited:
        skip = True
        break

      continue
    current = temp
    if current.islower():
      visited.append(current)
    path.append(current)
  if skip:
    continue
  paths.append(path)
  


paths = [list(x) for x in set(tuple(x) for x in paths)]
for path in paths:
  print(path)
print(len(paths))