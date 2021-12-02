presents = [
    '2x3x4',
    '1x1x10'
]

filename = '2015/2/input.txt'
with open(filename) as file:
    lines = file.readlines()
    presents = [line.strip() for line in lines]


def ribbon(l, w, h):
    l, w, h = int(l), int(w), int(h)
    lwh = l*w*h
    dimensions = [l, w, h] 
    dimensions.sort()
    m1, m2 = dimensions.pop(0), dimensions.pop(0)
    return m1*2 + m2*2 + lwh 


sum = 0
for p in presents:
    [l, w, h] = p.split('x')
    sum += ribbon(l, w, h)

print(sum)
