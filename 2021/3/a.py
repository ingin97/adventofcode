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

count = [0 for i in range(12)]

for di in diagnostics:
  
  for i, b in enumerate(di):
    if b == '1':
      count[i] += 1


gamma = ''
epsilon = ''
print(count)
for c in count:
  if c > len(diagnostics)/2:
    gamma += '1'
    epsilon += '0'
  else:
    gamma += '0'
    epsilon += '1'
    

gamma = int(gamma, 2)
epsilon = int(epsilon, 2)

power_consumption = gamma * epsilon

print(power_consumption)