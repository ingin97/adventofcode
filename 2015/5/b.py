lines = [
  'qjhvhtzxzqqjkmpb',
  'xxyxx',
  'uurcxstgmygtbstg',
  'ieodomkazucvgmuy',
  'aaa',
]

filename = '2015/5/input.txt'
with open(filename) as file:
  lines = file.readlines()
  lines = [line.strip() for line in lines]


nice_count = 0
for line in lines:
  pair_twice = ''
  repeat = ''

  last_c = ''
  last_last_c = ''
  pairs = dict()
  for c in line:
    if last_c+c in pairs and not(c == last_c and c == last_last_c):
      pair_twice = last_c+c

    pairs[last_c+c] = 1

    if c == last_last_c:
      repeat = c+last_c+last_last_c

    last_last_c = last_c
    last_c = c
  print(pairs)

  print(f'Line: {line} | {pair_twice} | {repeat} |')

  if pair_twice and repeat:
    nice_count += 1

print(nice_count)
