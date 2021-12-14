lines = [
  '2199943210',
  '3987894921',
  '9856789892',
  '8767896789',
  '9899965678',
]

filename = '2021/9/input.txt'
with open(filename) as file:
  lines = file.readlines()
  lines = [line.strip() for line in lines]

_map = [[int(num) for num in line] for line in lines]

y_max = len(_map)
x_max = len(_map[0])

basins = []
for i in range(y_max):
  for j in range(x_max):
    current = _map[i][j]

    if i == 0:
      north = 9
    else:
      north = _map[i-1][j]
    
    if i == y_max-1:
      south = 9
    else:
      south = _map[i+1][j]

    if j == 0:
        west = 9
    else:
      west = _map[i][j-1]

    if j == x_max-1:
      east = 9
    else:
      east = _map[i][j+1]

    if current < north and current < south and current < west and current < east:
      basin = {}
      new_positions = {}
      new_positions[i,j] = True

      while len(new_positions) > 0:
        postitions = {**new_positions}
        new_positions = {}
        for pos in postitions.keys():
          y, x = pos

          if y != 0 and not basin.get((y-1,x), False):
            north = _map[y-1][x]
            if north != 9:
              new_positions[y-1,x] = True

          if y != y_max-1 and not basin.get((y+1,x), False):
            south = _map[y+1][x]
            if south != 9:
              new_positions[y+1,x] = True
          
          if x != 0 and not basin.get((y,x-1), False):
            west = _map[y][x-1]
            if west != 9:
              new_positions[y,x-1] = True

          if x != x_max-1 and not basin.get((y,x+1), False):
            east = _map[y][x+1]
            if east != 9:
              new_positions[y,x+1] = True

        basin = {**basin, **new_positions}

      basins.append(basin)

basins.sort(key=lambda s: -len(s))

result = len(basins[0]) * len(basins[1]) * len(basins[2])
print(result)

  