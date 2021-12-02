route1 = '>'
route2 = '^>v<'
route3 = '^v^v^v^v^v'

filename = '2015/3/input.txt'
with open(filename) as file:
    route = file.read()

x = 0
y = 0
houses = dict()
houses[x, y] = True

for c in route:
  if c == '>':
    x += 1
  elif c == '<':
    x -= 1
  elif c == '^':
    y += 1
  elif c == 'v':
    y -= 1
    
  houses[x, y] = True


print(len(houses))
