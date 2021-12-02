route1 = '^v'
route2 = '^>v<'
route3 = '^v^v^v^v^v'

filename = '2015/3/input.txt'
with open(filename) as file:
    route = file.read()

s_x = 0
s_y = 0
r_x = 0
r_y = 0
houses = dict()
houses[s_x, s_y] = True

for i, c in enumerate(route):
  x, y = 0, 0
  if c == '>':
    x += 1
  elif c == '<':
    x -= 1
  elif c == '^':
    y += 1
  elif c == 'v':
    y -= 1

  if i % 2 == 0:
    s_x += x
    s_y += y
    houses[s_x, s_y] = True
  else:
    r_x += x
    r_y += y
    houses[r_x, r_y] = True


print(len(houses))
