

line = '9C0141080250320F1802104A08'

filename = '2021/16/input.txt'
with open(filename) as file:
  line = file.read()
  line = line.strip()

bits = bin(int(line, 16))[2:].zfill(len(line)*4)
print(bits)

class Reader:
  p = 0

  def read(self, move):
    result = bits[self.p:self.p+move]
    self.p += move
    return result

  def read_int(self, move):
    result = self.read(move)
    return int(result, 2)

  def look(self, move=1):
    result = bits[self.p:self.p+move]
    return result

  def eof(self):
    return self.look() == ''

r = Reader()

class Packet:

  
  def __init__(self):
    self.value = 0
    self.sub_values = []
    self.start = r.p
    print(f'===== NEW PACKET ======')
    self.version = r.read_int(3)
    print(f'Version {self.version}')


    self.type = r.read_int(3)
    print(f'Type {self.type}')

    if self.type == 4:
      num = ''
      while r.read(1) == '1':
        num += r.read(4)
      num += r.read(4)

      num = int(num, 2)
      print(f'num {num}')
      self.value = num
    
    else:
      length_type = r.read(1)
      print(f'length_type {length_type}')


      if length_type == '0':
        length = r.read_int(15)
        current = r.p
        print(f'length {length}')

        while (r.p - current) < length:
          print(r.p, current, length)
          p = Packet()
          self.sub_values.append(p.value)
          if (self.type == 7):
            print(self.sub_values)
        
          
        
      elif length_type == '1':
        packet_count = r.read_int(11)
        print(f'packet_count {packet_count}')


        for i in range(packet_count):
          p = Packet()
          self.sub_values.append(p.value)
        

      if self.type == 0:
        sum = 0
        for value in self.sub_values:
          sum += value
        self.value = sum

      elif self.type == 1:
        product = 1
        for value in self.sub_values:
          product *= value
          print('product', product)
        self.value = product

      elif self.type == 2:
        self.value = min(self.sub_values)
      
      elif self.type == 3:
        self.value = max(self.sub_values)

      elif self.type == 5:
        self.value = 1 if self.sub_values[0] > self.sub_values[1] else 0
      
      elif self.type == 6:
        self.value = 1 if self.sub_values[0] < self.sub_values[1] else 0
      
      elif self.type == 7:
        self.value = 1 if self.sub_values[0] == self.sub_values[1] else 0



  
  
p = Packet()
print(p.value)




