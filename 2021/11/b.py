lines = [
  '5483143223',
  '2745854711',
  '5264556173',
  '6141336146',
  '6357385478',
  '4167524645',
  '2176841721',
  '6882881134',
  '4846848554',
  '5283751526',
]

filename = '2021/11/input.txt'
with open(filename) as file:
  lines = file.readlines()
  lines = [line.strip() for line in lines]

octopuses = [[int(x) for x in line] for line in lines]

def pretty():
  for row in octopuses:
    print(row)

total_flashes = 0
for step in range(1000):
  # Increment
  for y in range(10):
    for x in range(10):
      octopuses[y][x] += 1

  # Flashes
  new_flashes = True
  while new_flashes:
    new_flashes = False
    for y in range(10):
      for x in range(10):
        if octopuses[y][x] > 9:
          octopuses[y][x] = -1000000
          new_flashes = True
          total_flashes += 1
          if x != 0 and y != 0:
            octopuses[y-1][x-1] += 1
          if y != 0:
            octopuses[y-1][x] += 1
          if y != 0 and x != 9:
            octopuses[y-1][x+1] += 1
          if x != 9:
            octopuses[y][x+1] += 1
          if x != 9 and y != 9:
            octopuses[y+1][x+1] += 1
          if y != 9:
            octopuses[y+1][x] += 1
          if x != 0 and y != 9:
            octopuses[y+1][x-1] += 1
          if x != 0:
            octopuses[y][x-1] += 1
    


  # Reset
  flashes = 0
  for y in range(10):
    for x in range(10):
      if octopuses[y][x] < 0:
        flashes += 1
        octopuses[y][x] = 0

  print(flashes)
  if flashes == 100:
    print(step+1)
    break
  


print(total_flashes)