lines = [
'NNCB',
'',
'CH -> B',
'HH -> N',
'CB -> H',
'NH -> C',
'HB -> C',
'HC -> B',
'HN -> C',
'NN -> C',
'BH -> H',
'NC -> B',
'NB -> B',
'BN -> B',
'BB -> N',
'BC -> B',
'CC -> N',
'CN -> C',
]


# filename = '2021/14/input.txt'
# with open(filename) as file:
#   lines = file.readlines()
#   lines = [line.strip() for line in lines]


template = list(lines[0])
pairs = {}

for line in lines[2:]:
  [pair, insert] = line.split(' -> ')
  pairs[pair] = insert


from collections import defaultdict
pair_counts = defaultdict(int)

last = ''
for current in template:
  if last+current in pairs.keys():
    pair_counts[last+current] += 1
  last = current

print(pair_counts)

for step in range(1):
  temp = {**pair_counts}
  pair_counts = defaultdict(int)
  for pair, value in temp.items():
    print(pair_counts)
    if pair in pairs.keys():
      insert = pairs[pair]
      [first, second] = pair
      pair_counts[first+insert] += value
      pair_counts[insert+second] += value


print(pair_counts)


letter_counts = defaultdict(int)
for pair, value in pair_counts.items():
  [first, second] = pair

  letter_counts[first] += value
  letter_counts[second] += value

print(letter_counts)
# values = list(counts.values())
# values.sort()
# print(values[-1] - values[0])
