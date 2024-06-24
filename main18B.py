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

MP = {UU:U, DD:D, LL:L, RR:R}

#0 means R, 1 means D, 2 means L, and 3 means U
with open("1818.txt") as f:

  coor = []
  for a in f.read().splitlines():
    #blo.extend(  a.split(',') )
    #grid.append(a)
    l, r, bad = a.split(' ')
    bad = bad.split('(#')[1]
    bad = bad.split(')')[0]

    left, right = bad[:-1], bad[-1]
    left = int(left, 16) # hex()
    right = MP[int(right)]
    #print(bad)
    #print(l,r)
    #coor.append((l, int(r) ))
    coor.append((right,left))
    print(right, left)
  x, y  = 500000, 500000
  #x,y = 0,0
  v = set()

  #v.add((0,0))
  v.add((500000,500000))

  M = 0
  N = 0
  M, N = 1000000,1000000 #max(x, M) , max(y, N)

  

  edges = []
  
  for d, s in coor:

    if d == U:
      x0, y0, x1, y1 = x-s, y, x, y 
      edges.append((x0, y0, x1, y1))
      x -= s
      #for i in range(s):
      #  x -= 1
      #  v.add((x,y))
      #  M, N = max(x, M) , max(y, N)
    if d == D:
      x0, y0, x1, y1 = x, y, x+s, y 
      edges.append((x0, y0, x1, y1))
      x += s
      #for i in range(s):
      #  x += 1
      #  v.add((x,y))
      #  M, N = max(x, M) , max(y, N)
    if d == L:
      x0, y0, x1, y1 = x, y-s, x, y 
      edges.append((x0, y0, x1, y1))
      y -= s
      #for i in range(s):
      #  y -= 1
      #  v.add((x,y))
      #  M, N = max(x, M) , max(y, N) 
    if d == R:
      x0, y0, x1, y1 = x, y, x, y+s
      edges.append((x0, y0, x1, y1))
      y += s
      #for i in range(s):
      #  y += 1
      #  v.add((x,y))
      #  M, N = max(x, M) , max(y, N)

  print(len(v))

  print('vv finish')
  q = deque()

  #q.append((1,1))

  #v.add((1,1))

  vv = set()

  M += 1
  N += 1

  def test(x,y,q,v,vv):
    if (x,y) not in v:
      q.append((x,y))
      vv.add((x,y))

  '''
  for i in range(M):
    test(i,0,q,v,vv)
    test(i,N-1,q,v,vv)
    #q.append((i, N-1))

  for j in range(N):
    #q.append((0, j))
    #q.append((M-1, j))
    test(0,j,q,v,vv)
    test(M-1,j,q,v,vv)
  '''
  test(0,0,q,v,vv)
  print(M, N)

  for i in range(M):
    l = [ '.' if (i,j) not in v else '#' for j in range(N) ]
    #print(''.join(l))
  print()
  while q:
    cx, cy = q.popleft()

    for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
      nx = cx + dx
      ny = cy + dy
      if nx < 0 or ny < 0 or nx >= M or ny >= N:
        continue
      if (nx, ny) not in v and (nx, ny) not in vv :
        q.append((nx, ny))
        vv.add((nx, ny))

  for i in range(M):
    l = [ '.' if (i,j) not in v else '#' for j in range(N) ]
    #print(''.join(l))

  print(M, N, M * N)
  print(len(vv))
  print(len(v))
  print(M*N - len(vv))

  #print(  len(v) // 2 - 1)

  
  