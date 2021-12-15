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
      # if (x, y) in Q:
      neighbours.append((x, y))
  return neighbours

def get_dist(x):
  return x['dist']
  
import numpy as np

np_map = np.array(_map)
large_map = np.tile(np_map, (5,5))

for y in range(len(large_map)):
  for x in range(len(large_map[0])):
    risk = large_map[x, y]
    y_add = y // (len(_map))
    x_add = x // (len(_map[0]))
    risk += y_add + x_add 
    risk = (risk % 10) + 1 if risk > 9 else risk 
    large_map[x, y] = risk

    
_map = large_map

import math
def djikstra():
  Q = []
  dist = {}
  prev = {}

  # for y in range(len(_map)):
  #   for x in range(len(_map[0])):
  #     dist[(x,y)] = math.inf
  #     prev[(x,y)] = None
  #     Q.append((x,y))
  Q.append({'xy':(0,0), 'dist':0})
  dist[(0,0)] = 0

  i = 0
  while len(Q) > 0:
    i += 1
    if i % 1000 == 0:
      print(i, len(Q))

    current = min(Q, key=get_dist)
    Q.remove(current)
    u = current['xy']

    neighbours = get_neighbours(u, Q)

    for v in neighbours:

      (x,y) = v
      alt = dist.get(u, math.inf) + _map[y][x]
      if alt < dist.get(v, math.inf):
        Q.append({'xy':(x,y), 'dist':alt})
        dist[v] = alt
        prev[v] = u
  

        
      
  S = []
  u = (len(_map[0])-1, len(_map)-1)
  print(dist[u])

  # while u != (0,0):
  #   S.insert(0, u)
  #   u = prev[u]

  # print(S)




djikstra()