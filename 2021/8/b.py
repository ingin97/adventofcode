lines = [
  # 'acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf',
  'be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe',
  'edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc',
  'fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg',
  'fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb',
  'aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea',
  'fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb',
  'dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe',
  'bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef',
  'egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb',
  'gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce',
]

filename = '2021/8/input.txt'
with open(filename) as file:
  lines = file.readlines()
  lines = [line.strip() for line in lines]

number_to_pos = {
    0: ['a', 'b', 'c', 'e', 'f', 'g'], 
    1: ['c', 'f'], 
    2: ['a', 'c', 'd', 'e', 'g'], 
    3: ['a', 'c', 'd', 'f', 'g'], 
    4: ['b', 'c', 'd', 'f'], 
    5: ['a', 'b', 'd', 'f', 'g'], 
    6: ['a', 'b', 'd', 'e', 'f', 'g'],
    7: ['a', 'c', 'f'],
    8: ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
    9: ['a', 'b', 'c', 'd', 'f', 'g']
}



sum = 0
for line in lines:
  mapping = {'a': [], 'b': [], 'c': [], 'd': [], 'e': [], 'f': [], 'g': []}
  [uniques, outputs] = line.split('|')
  uniques = uniques.split()
  outputs = outputs.split()

  for val in uniques:
    if len(val) == 2:
      for letter in val:
        mapping['c'].append(letter)
        mapping['f'].append(letter)

  for val in uniques:
    if len(val) == 3:
      for letter in val:
        if letter not in mapping['c'] and letter not in mapping['f']:
            mapping['a'].append(letter)

  for val in uniques:
    if len(val) == 4:
      for letter in val:
        if letter not in mapping['c'] and letter not in mapping['f']:
            mapping['b'].append(letter)
            mapping['d'].append(letter)

  for val in uniques:
    if len(val) == 7:
      for letter in val:
        if letter not in mapping['c'] and letter not in mapping['f'] and letter not in mapping['a'] and letter not in mapping['b'] and letter not in mapping['d']:
            mapping['e'].append(letter)
            mapping['g'].append(letter)
  

  for val in uniques:
    if len(val) == 5:
      match = True
      d = ''
      b = ''
      for letter in mapping['d']:
        if letter not in val:
          match = False
          b = letter
        else:
          d = letter

      if not match:
        mapping['d'] = [d]
        mapping['b'] = [b]
        break


  for val in uniques:
    if len(val) == 6:
      match = True
      f = ''
      c = ''
      for letter in mapping['f']:
        if letter not in val:
          match = False
          c = letter
        else:
          f = letter

      if not match:
        mapping['f'] = [f]
        mapping['c'] = [c]
        break

  for val in uniques:
    if len(val) == 6:
      match = True
      e = ''
      g = ''
      for letter in mapping['g']:
        if letter not in val:
          match = False
          e = letter
        else:
          g = letter

      if not match:
        mapping['g'] = [g]
        mapping['e'] = [e]
        break
        

  output_number = ''
  for output in outputs:
    for num, letters in number_to_pos.items():
      if len(output) != len(letters):
        continue
      match = True
      for letter in letters:
        if mapping[letter][0] not in output:
          match = False
      
      if match:
        output_number += str(num)
        break
  sum += int(output_number)
  print(output_number)


print(sum)






  