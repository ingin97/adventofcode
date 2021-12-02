instructions = [
  'forward 5',
  'down 5',
  'forward 8',
  'up 3',
  'down 8',
  'forward 2',
]

filename = '2021/2/input.txt'
with open(filename) as file:
  lines = file.readlines()
  instructions = [line.strip() for line in lines]

y_pos = 0
x_pos = 0
aim = 0

for ins in instructions:
  [direction, value] = ins.split()
  value = int(value)
  if direction == 'forward':
    x_pos += value
    y_pos += aim * value
  elif direction == 'down':
    aim += value
  elif direction == 'up':
    aim -= value


print(f'y_pos: {y_pos}')
print(f'x_pos: {x_pos}')
print(f'Answer: {y_pos*x_pos}')