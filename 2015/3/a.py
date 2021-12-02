presents = [
  '2x3x4',
  '1x1x10'
]

filename = '2015/2/input.txt'
with open(filename) as file:
  lines = file.readlines()
  presents = [line.strip() for line in lines]

def wrapping_paper(l, w, h):
  l, w, h = int(l), int(w), int(h)
  lw = l*w
  wh = w*h
  hl = h*l
  return 2*lw + 2*wh + 2*hl + min(lw, wh, hl)

sum = 0
for p in presents:
  [l, w, h] = p.split('x')
  sum += wrapping_paper(l, w, h)

print(sum)