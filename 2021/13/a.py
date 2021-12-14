lines = [
  '6,10',
  '0,14',
  '9,10',
  '0,3',
  '10,4',
  '4,11',
  '6,0',
  '6,12',
  '4,1',
  '0,13',
  '10,12',
  '3,4',
  '3,0',
  '8,4',
  '1,10',
  '2,14',
  '8,10',
  '9,0',
  '',
  'fold along y=7',
  'fold along x=5',
]


filename = '2021/13/input.txt'
with open(filename) as file:
  lines = file.readlines()
  lines = [line.strip() for line in lines]

dots = []
folds = []

part_one = True
x_max = 0
y_max = 0
for line in lines:

  if line == '':
    part_one = False
    continue
  if part_one:
    [x, y] = line.split(',')
    x, y = int(x), int(y)
    if x > x_max:
      x_max = x
    if y > y_max:
      y_max = y
    dots.append([x, y])
  else:
    token = line.split(' ')[2]
    [direction, split] = token.split('=')
    folds.append([direction, int(split)])

x_max += 1
y_max += 1
paper = [[0 for i in range(x_max)] for j in range(y_max)]
for dot in dots:
  [x, y] = dot
  paper[y][x] = 1

for fold in folds[:1]:
  [direction, split] = fold

  if direction == 'y':
    part1 = paper[:split]
    part2 = paper[split+1:]
    paper = part1
    part2.reverse()
    for y, (row1, row2) in enumerate(zip(part1, part2)):
      for x, (pos1, pos2) in enumerate(zip(row1, row2)):
        paper[y][x] = pos1 or pos2


  if direction == 'x':
    part1 = []
    for row in paper:
      part1.append(row[:split])
    part2 = []
    for row in paper:
      part2.append(row[split+1:])

    paper = part1
    for row in part2:
      row.reverse()

    for y, (row1, row2) in enumerate(zip(part1, part2)):
      for x, (pos1, pos2) in enumerate(zip(row1, row2)):
        paper[y][x] = 1 if pos1 or pos2 else 0
  
dot_count = 0
for row in paper:
  print(' '.join(['#' if x==1 else '.' for x in row]))
  for pos in row:
    if pos == 1:
      dot_count += 1


print(dot_count)
