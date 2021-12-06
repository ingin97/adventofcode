fishes = [3,4,3,1,2]

filename = '2021/6/input.txt'
with open(filename) as file:
  line = file.read()
  fishes = [int(num) for num in line.split(',')]


for i in range(18):
  print(i)
  for i, fish in enumerate(fishes):
    if fish == 0:
      fishes.append(9)
      fishes[i] = 6
    else:
      fishes[i] = fish - 1
    

print(len(fishes))