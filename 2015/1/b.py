filename = '2015/1/input.txt'
with open(filename) as file:
  y = file.read()

floor = 0

for i, char in enumerate(y):
  if char == '(':
    floor += 1
  elif char == ')':
    floor -= 1
  if floor == -1:
    print(i+1)
    break
print(floor)