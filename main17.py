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
    l = ['#' if (i,j) in vv else '.' for j in range(N)]
    print(l)

digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

digmap = {}
for i, x in enumerate(digits):
    digmap[x] = i

grid = []

def dijkstra(graph, start):

  n = len(graph)
  dist, parents = defaultdict(lambda: math.inf), defaultdict(lambda: -1) # [float("inf")] * n, [-1] * n
  dist[start] = 0

  queue = [(0, start, 0,0,0,0)]
  while queue:
      path_len, v, cx, cxx,cy,cyy = heappop(queue)

      if path_len == dist[v]:
          for w, edge_len, dx, dy in graph[v]:
            
            if edge_len + path_len < dist[w]:
                
                if dx > 0:
                  x,xx,y,yy = cx + dx, 0,0,0
                if dy > 0:
                  x,xx,y,yy = 0, 0,cy + dy,0
                if dx < 0:
                  x,xx,y,yy = 0, cx - dx,0,0
                if dy < 0:
                  x,xx,y,yy = 0, 0,0,cy - dy
                if 4 == x or 4 == xx or 4 == y or 4 == yy:
                  continue
                dist[w], parents[w] = edge_len + path_len, v
                heappush(queue, (edge_len + path_len, w, x, xx , y , yy ))

  return dist, parents

with open("1717.txt") as f:
  #blo = []

  #h = []
  for a in f.read().splitlines():
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
        if nx < 0 or nx >= X or ny < 0 or ny >= Y:
          continue
        G[(i,j)].append(((nx,ny),int(grid[nx][ny]), dx, dy))
  d, p = dijkstra(G, (0,0))

  print(d[(X-1,Y-1)] )#len(d))
  dd = set()
  cur = (X-1,Y-1)
  while cur != (0,0):
    dd.add(cur)
    cur = p[cur]
  for i in range(X):
    l = ['X' if (i,j) in dd else '.' for j in range(Y)]
    print(l)
  '''h = []
  dirs = [[1,0],[0,1],[-1,0],[0,-1]]
  while h:
    cx,cy,t = heappop(h)

    for dx,dy in dirs:
      nx = cx + dx
      ny = 
  '''
  