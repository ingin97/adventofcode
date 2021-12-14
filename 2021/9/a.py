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

risk = 0
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
      risk += 1 + current

print(risk)

  