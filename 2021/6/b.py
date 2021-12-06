fishes = [3,4,3,1,2]

filename = '2021/6/input.txt'
with open(filename) as file:
  line = file.read()
  fishes = [int(num) for num in line.split(',')]

#       0  1  2  3  4  5  6  7  8
days = [0, 0, 0, 0, 0, 0, 0, 0, 0]

for fish in fishes:
  days[fish] += 1
  
for n in range(256):
  print(n+1, days)
  move = 0
  for i in range(len(days)-1, -1, -1):
    temp = days[i] 
    days[i] = move
    move = temp

  days[6] += move
  days[8] += move

sum = 0
for fish in days:
  sum += fish

print(sum)