lines = [
  '0,9 -> 5,9',
  '8,0 -> 0,8',
  '9,4 -> 3,4',
  '2,2 -> 2,1',
  '7,0 -> 7,4',
  '6,4 -> 2,0',
  '0,9 -> 2,9',
  '3,4 -> 1,4',
  '0,0 -> 8,8',
  '5,5 -> 8,2',
]

filename = '2021/5/input.txt'
with open(filename) as file:
  lines = file.readlines()
  lines = [line.strip() for line in lines]

_map = [[0 for i in range(1000)] for i in range(1000)]


for vent in lines:
  [_from, _to] = vent.split(' -> ')

  [x1, y1] = _from.split(',')
  [x2, y2] = _to.split(',')
  x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)

  if x1 == x2 or y1 == y2:
    y_min = min(y1,y2)
    y_max = max(y1,y2)
    for i in range(y_min, y_max+1):
      x_min = min(x1,x2)
      x_max = max(x1,x2)
      for j in range(x_min, x_max+1):
        _map[i][j] += 1
  else:
    if x1 > x2:
        x1, y1, x2, y2 = x2, y2, x1, y1

    slope = (y2 - y1) // (x2 - x1)
    for i, j in zip(range(x1, x2), range(y1, y2, slope)):
        _map[j][i] += 1
    _map[y2][x2] += 1


danger = 0
for row in _map:
  for vc in row:
    if vc >= 2:
      danger += 1
  
print(danger)