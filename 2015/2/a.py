filename = '2015/2/input.txt'
with open(filename) as file:
  lines = file.readlines()
  presents = [line.strip() for line in lines]

floor = 0

for i, char in enumerate(y):
  if char == '(':
    floor += 1
  elif char == ')':
    floor -= 1

print(floor)