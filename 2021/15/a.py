lines = [
  '1163751742',
  '1381373672',
  '2136511328',
  '3694931569',
  '7463417111',
  '1319128137',
  '1359912421',
  '3125421639',
  '1293138521',
  '2311944581',
]


filename = '2021/15/input.txt'
with open(filename) as file:
  lines = file.readlines()
  lines = [line.strip() for line in lines]


_map = [[int(x) for x in row] for row in lines]

def get_neighbours(u, Q):
  (x,y) = u
  neighbours = []
  for (x, y) in [(x-1, y), (x, y-1), (x+1, y), (x, y+1)]:
    if x >= 0 and x < len(_map[0]) and y >= 0 and y < len(_map):
      if (x, y) in Q:
        neighbours.append((x, y))
  return neighbours
  
def get_risk(x):
  return x['risk']

def at_end(x,y):
  return y == len(_map) - 1 and x == len(_map[0]) - 1

import math
def djikstra():
  Q = []
  dist = {}
  prev = {}

  for y, row in enumerate(_map):
    for x, risk in enumerate(row):
      dist[(x,y)] = math.inf
      prev[(x,y)] = None
      Q.append((x,y))

  dist[(0,0)] = 0

  while len(Q) > 0:
    low = math.inf 
    u = Q[0]  
    for v in Q:
      if dist[v] < low:
        u = v
        low = dist[v]

    Q.remove(u)

    neighbours = get_neighbours(u, Q)

    for v in neighbours:
      (x,y) = v
      alt = dist[u] + _map[y][x]
      if alt < dist[v]:
        dist[v] = alt
        prev[v] = u
  

        
      
  S = []
  u = (len(_map[0])-1, len(_map)-1)
  print(dist[u])

  while u != (0,0):
    S.insert(0, u)
    u = prev[u]

  print(S)




djikstra()