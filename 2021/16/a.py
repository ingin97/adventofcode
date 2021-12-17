

line = 'A0016C880162017C3686B18A3D4780'

filename = '2021/16/input.txt'
with open(filename) as file:
  line = file.read()
  line = line.strip()

bits = bin(int(line, 16))[2:].zfill(len(line)*4)

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

r = Reader()

class Packet:

  sub_packets = []
  sum = 0
  def __init__(self):
    self.start = r.p
    self.version = r.read_int(3)
    self.sum += self.version

    self.type = r.read_int(3)

    self.num = ''
    if self.type == 4:
      while r.read(1) == '1':
        self.num += r.read(4)
      self.num += r.read(4)

      self.num = int(self.num, 2)
    
    else:
      length_type = r.read(1)

      if length_type == '0':
        length = r.read_int(15)
        current = r.p

        while (r.p - current) < length:
          p = Packet()
          self.sum += p.sum
          self.sub_packets.append(p)
        
      elif length_type == '1':
        packet_count = r.read_int(11)

        for i in range(packet_count):
          p = Packet()
          self.sum += p.sum
          self.sub_packets.append(p)

  

p = Packet()
print(p.sum)





