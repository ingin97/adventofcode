lines = [
  '[({(<(())[]>[[{[]{<()<>>',
  '[(()[<>])]({[<{<<[]>>(',
  '{([(<{}[<>[]}>{[]{[(<()>',
  '(((({<>}<{<{<>}{[]{[]{}',
  '[[<[([]))<([[{}[[()]]]',
  '[{[{({}]{}}([{[{{{}}([]',
  '{<[[]]>}<{[{[{[]{()[[[]',
  '[<(<(<(<{}))><([]([]()',
  '<{([([[(<>()){}]>(<<{{',
  '<{([{{}}[<[[[<>{}]]]>[]]',
]

filename = '2021/10/input.txt'
with open(filename) as file:
  lines = file.readlines()
  lines = [line.strip() for line in lines]


opening = ['(', '[', '{', '<']
closing = [')', ']', '}', '>']

opening_to_closing = {'(':')', '[':']', '{':'}', '<':'>'}


l_to_scores = {')':1, ']':2, '}':3, '>':4}


scores = []
for line in lines:
  opens = []
  corrupted = False
  for l in line:
    if l in opening:
      opens.append(l)
    elif l in closing:
      open = opens.pop()
      if l != opening_to_closing[open]:
        corrupted = True
        break
  if corrupted:
    continue
  
  opens = []
  for l in line:
    if l in opening:
      opens.append(l)
    elif l in closing:
      open = opens.pop()

  add = []
  for i in range(len(opens)):
    open = opens.pop()
    add.append(opening_to_closing[open])

  print(add)
  

  score = 0
  for l in add:
    score *= 5
    score += l_to_scores[l]
  scores.append(score)
  

scores.sort()

print(scores[int(len(scores)/2)])
