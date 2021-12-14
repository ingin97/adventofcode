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


scores = {')':3, ']':57, '}':1197, '>':25137}



sum = 0
for line in lines:
  opens = []
  for l in line:
    if l in opening:
      opens.append(l)
    elif l in closing:
      open = opens.pop()
      if l != opening_to_closing[open]:
        sum += scores[l]
        break
print(sum)
