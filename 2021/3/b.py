import math
diagnostics = [
  '00100',
  '11110',
  '10110',
  '10111',
  '10101',
  '01111',
  '00111',
  '11100',
  '10000',
  '11001',
  '00010',
  '01010',
]

filename = '2021/3/input.txt'
with open(filename) as file:
  lines = file.readlines()
  diagnostics = [line.strip() for line in lines]

def get_count(dias, pos):
  count = 0
  for di in dias:
    if di[pos] == '1':
      count += 1
  return count

def find_rating(more, less):
  pos = 0
  dias = diagnostics
  while len(dias) > 1:
    keep = []
    c = get_count(dias, pos)
    criteria = more if c >= len(dias)/2 else less

    for di in dias:
      if di[pos] == criteria:
        keep.append(di)
    
    dias = keep
    pos += 1
  return dias[0]

ox = find_rating('1', '0')
print(ox)

co2 = find_rating('0', '1')
print(co2)

ox = int(ox, 2)
co2 = int(co2, 2)

life  = ox * co2

print(life)