lines = [
  'turn on 0,0 through 999,999',
  'toggle 0,0 through 999,0',
  'turn off 499,499 through 500,500',
]

filename = '2015/6/input.txt'
with open(filename) as file:
  lines = file.readlines()
  lines = [line.strip() for line in lines]


lights = [ [0 for i in range(1000)] for i in range(1000)]


for line in lines:
  turn_on = False
  turn_off = False
  toggle = False

  tokens = line.split()
  if tokens[0] == 'toggle':
    toggle = True
  else: 
    if tokens[1] == 'on':
      turn_on = True
    else:
      turn_off = True

  x_0, y_0 = tokens[-3].split(',')
  x_1, y_1 = tokens[-1].split(',')

  for i in range(int(x_0), int(x_1)+1):
    for j in range(int(y_0),int(y_1)+1):
      if turn_on:
        lights[i][j] = True
      elif turn_off:
        lights[i][j] = False
      elif toggle:
        lights[i][j] = not lights[i][j]


on_count = 0

for row in lights:
  for col in row:
    if col:
      on_count += 1

print(on_count)