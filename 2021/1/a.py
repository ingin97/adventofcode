depths = [
  199,
  200,
  208,
  210,
  200,
  207,
  240,
  269,
  260,
  263,
]

filename = '2021/1/input.txt'
with open(filename) as file:
  lines = file.readlines()
  depths = [int(line.strip()) for line in lines]

increase = 0
last = None

for depth in depths:
  if last is not None and depth > last:
    increase += 1
  last = depth

print(increase)