lines = [
  '123 -> x',
  '456 -> y',
  'x AND y -> d',
  'x OR y -> e',
  'x LSHIFT 2 -> f',
  'y RSHIFT 2 -> g',
  'NOT x -> h',
  'NOT y -> i',
]

filename = '2015/7/input.txt'
with open(filename) as file:
  lines = file.readlines()
  lines = [line.strip() for line in lines]


variables = dict()

for i, line in enumerate(lines):
  print(line)
  [l, var] = line.split('->')
  l, var = l.strip(), var.strip()

  tokens = l.split()

  if len(tokens) == 1:
    val = int(tokens[0])
  elif len(tokens) == 2:
    x = variables[tokens[1]] or 0
    val = ~x 
  elif len(tokens) == 3:
    x = variables[tokens[0]] or 0
    op = tokens[1]
    if op == 'AND':
      y = variables[tokens[2]] or 0
      val = x & y
    elif op == 'OR':
      y = variables[tokens[2]] or 0
      val = x | y
    elif op == 'LSHIFT':
      y = int(tokens[2])
      val = x << y
    elif op == 'RSHIFT':
      y = int(tokens[2])
      val = x >> y

  if val < 0:
    val = val & 0xffff

  variables[var] = val

print(variables['h'])