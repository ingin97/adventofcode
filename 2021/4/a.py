lines = [
  '7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1',
  '',
  '22 13 17 11  0',
  ' 8  2 23  4 24',
  '21  9 14 16  7',
  ' 6 10  3 18  5',
  ' 1 12 20 15 19',
  '',
  ' 3 15  0  2 22',
  ' 9 18 13 17  5',
  '19  8  7 25 23',
  '20 11 10 24  4',
  '14 21 16 12  6',
  '',
  '14 21 17 24  4',
  '10 16 15  9 19',
  '18  8 23 26 20',
  '22 11 13  6  5',
  ' 2  0 12  3  7',
]

filename = '2021/4/input.txt'
with open(filename) as file:
  lines = file.readlines()
  lines = [line.strip() for line in lines]
import numpy as np
numbers = [int(x) for x in lines[0].split(',')]
board_lines = lines[2:]

boards = []
board = []
for line in board_lines:
  if line == '':
    boards.append(board)
    board = []
    continue

  nums = [int(x) for x in line.split()]
  board.append(nums)
boards.append(board)

pos = 5
winner = False

while not winner:
  nums = numbers[:pos]

  for board in boards:
    for row in board:
      correct = 0
      for num in row:
        if num in nums:
          correct += 1
      if correct == 5:
        winner = board
    

    board_transpose = np.transpose(board)
    for col in board_transpose:
      correct = 0
      for num in col:
        if num in nums:
          correct += 1
      if correct == 5:
        winner = board
  pos += 1

sum = 0
for row in winner:
  for num in row:
    if num not in nums:
      sum += num

result = sum * nums[-1]
print(result)