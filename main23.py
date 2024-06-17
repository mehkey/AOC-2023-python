from functools import cache
from collections import defaultdict, deque
from heapq import heappop, heappush
import math
import time
from types import GeneratorType


def ints(s, split=' '):
  return [int(x) for x in s.split(split) if x]


def colon(s):
  return s.split(': ')[1]


def merge(l):
  return ''.join([str(x) for x in l])


#def pp(g):
#  for gg in g:
#    print(gg)


def tp(g):
  return tuple(sum(g, []))


#vv = set()
def pp(vv):
  #nonlocal vv
  for i in range(M):
    l = ['#' if (i, j) in vv else '.' for j in range(N)]
    print(l)


digits = [
    'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
    'nine'
]

digmap = {}
for i, x in enumerate(digits):
  digmap[x] = i

grid = []


def dijkstra(graph, start):

  n = len(graph)
  dist, parents = defaultdict(lambda: 0), defaultdict(
      lambda: -1)  # [float("inf")] * n, [-1] * n
  dist[start] = 0

  queue = [(0, start)]
  vv  = set()
  while queue:
    path_len, v = heappop(queue)

    if path_len == dist[v]:
      for w, edge_len in graph[v]:

        if edge_len + path_len > dist[w]:

        #if w not in vv:
       #   vv.add(w)

          dist[w], parents[w] = max(dist[w],edge_len + path_len), v
          heappush(queue, (edge_len + path_len, w))

  return dist, parents
 
U,D,L,R = 'U', 'D', 'L', 'R'
UU = 3
DD = 1
LL = 2
RR = 0

MP = {UU:U, DD:D, LL:L, RR:R}

grid = []

#0 means R, 1 means D, 2 means L, and 3 means U
with open("2323.txt") as f:

  coor = []
  for a in f.read().splitlines():
    #blo.extend(  a.split(',') )
    #grid.append(a)
    #for a in f.read().splitlines():
      #blo.extend(  a.split(',') )
    grid.append(a)

  dirs = [[1,0],[0,1],[-1,0],[0,-1]]
  G = defaultdict(list)
  X = len(grid)
  Y = len(grid[0])
  for i in range(X):
    for j in range(Y):
      for dx,dy in dirs:
        nx = i + dx
        ny = j + dy
        if nx < 0 or nx >= X or ny < 0 or ny >= Y or grid[nx][ny] == '#':
          continue
        G[(i,j)].append( ((nx,ny),1) ) #((nx,ny),int(grid[nx][ny])))
  print(G)
  d, p = dijkstra(G, (0,1))
  print(d)
  m = 0
  for dd in d.values():
    m = max(m, dd)
  print(m)