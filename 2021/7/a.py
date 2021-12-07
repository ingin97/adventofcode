positions = [16,1,2,0,4,2,7,1,2,14]

filename = '2021/7/input.txt'
with open(filename) as file:
  line = file.read()
  positions = [int(num) for num in line.split(',')]


fuels = []


for i in range(max(positions)+1):
  fuel = 0
  for pos in positions:
    fuel += abs(pos - i)
  fuels.append(fuel)

print(fuels)
print(min(fuels))


  