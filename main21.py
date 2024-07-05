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
  dist, parents = defaultdict(lambda: math.inf), defaultdict(
      lambda: -1)  # [float("inf")] * n, [-1] * n
  dist[start] = 0

  queue = [(0, start, 0, 0, 0, 0)]
  while queue:
    path_len, v, cx, cxx, cy, cyy = heappop(queue)

    if path_len == dist[v]:
      for w, edge_len, dx, dy in graph[v]:

        if edge_len + path_len < dist[w]:

          if dx > 0:
            x, xx, y, yy = cx + dx, 0, 0, 0
          if dy > 0:
            x, xx, y, yy = 0, 0, cy + dy, 0
          if dx < 0:
            x, xx, y, yy = 0, cx - dx, 0, 0
          if dy < 0:
            x, xx, y, yy = 0, 0, 0, cy - dy
          if 4 == x or 4 == xx or 4 == y or 4 == yy:
            continue
          dist[w], parents[w] = edge_len + path_len, v
          heappush(queue, (edge_len + path_len, w, x, xx, y, yy))

  return dist, parents

U,D,L,R = 'U', 'D', 'L', 'R'
UU = 3
DD = 1
LL = 2
RR = 0

grid = []

with open("2121.txt") as f:
#blo = []

  #h = []
  sx, sy = 0,0
  ct = 0
  for a in f.read().splitlines():
    #blo.extend(  a.split(',') )
    if 'S' in a:
      sx = ct
      sy = a.index('S')
    grid.append(a)
    ct += 1
  print(sx,sy)
  dirs = [[1,0],[0,1],[-1,0],[0,-1]]
  # G = defaultdict(list)
  X = len(grid)
  Y = len(grid[0])

  q = deque()
  q.append((sx,sy,0))
  v = set()
  v.add((sx,sy,0))
  r = set()
  res = 0
  while q:
    i,j, d = q.popleft()

    if d == 10_000: #26501365: 
      r.add((i,j))
      continue

    for dx,dy in dirs:
      nx = i + dx
      ny = j + dy
      if nx < 0: 
        nx = X -1
      if ny < 0:
        ny = Y -1
      if nx >= X:
        nx = 0
      if ny >= Y:
        ny = 0
      if grid[nx][ny] == '#':
        continue

      if (nx,ny,d+1) not in v:
        v.add((nx,ny,d+1))
        q.append((nx,ny,d+1))

  print(len(r))
