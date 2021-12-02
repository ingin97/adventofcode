from hashlib import md5

x1 = 'abcdef'
x2 = 'pqrstuv'
x = 'bgvyzdsv'

i = 0

while True:
  if i % 1000 == 0:
    print(i)
  
  val = x + str(i)
  hash = md5(val.encode('utf-8')).hexdigest()

  if hash[0:5] == '00000':
    print(i, hash)
    break
  i += 1
