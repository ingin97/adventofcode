lines = [
  'ugknbfddgicrmopn',
  'aaa',
  'jchzalrnumimnmhp',
  'haegwjzuvuyypxyu',
  'dvszwmarrgswjxmb',
]

filename = '2015/5/input.txt'
with open(filename) as file:
  lines = file.readlines()
  lines = [line.strip() for line in lines]


nice_count = 0
for line in lines:
  vowel_count = 0
  twice = False
  forbidden = False

  last_c = ''
  for c in line:
    if c in 'aeiou':
      vowel_count += 1
    if c == last_c:
      twice = True
    if last_c+c in ['ab', 'cd', 'pq', 'xy']:
      forbidden = True
    last_c = c

  if vowel_count >= 3 and twice and not forbidden:
    nice_count += 1

print(nice_count)
