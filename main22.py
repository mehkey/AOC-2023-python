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


U,D,L,R = 'U', 'D', 'L', 'R'
UU = 3
DD = 1
LL = 2
RR = 0

coor = []

with open("2222.txt") as f:

  sx, sy = 0,0
  ct = 0
  mx=0
  my=0
  mz=0
  
  for a in f.read().splitlines():

    #if 'S' in a:
    #  sx = ct
    #  sy = a.index('S')
    left, right = a.split('~')
    
    #grid.append(a)
    coor.append( (ints(left, split=','), ints(right, split=',')) )
    mx=max(mx,coor[-1][0][0],coor[-1][1][0])
    my=max(my,coor[-1][0][1],coor[-1][1][1])
    mz=max(mz,coor[-1][0][2],coor[-1][1][2])
    ct += 1

  print(mx,my,mz)
  print(coor)

  ct = 0
  g = [[['.' for _ in range(mz+1)] for _ in range(my+1)] for _ in range(mx+1)]
  
  for left, right in coor:
    x0,y0,z0 = left
    x1,y1,z1 = right
    if x0 > x1:
      x0, x1 = x1, x0
    if y0 > y1:
      y0, y1 = y1, y0
    if z0 > z1:
      z0, z1 = z1, z0

    for i in range(x0,x1+1):
      for j in range(y0,y1+1):
        for k in range(z0,z1+1):
          g[i][j][k] = chr(ct+ord('A'))
          
    ct += 1
  mx += 1
  my += 1
  mz += 1

  G = defaultdict(list)
  
  for i in range(mx-1,-1,-1):
    s = []
    for j in range(my):
      for k in range(0,mz):
        
        if g[i][j][k] != '.':
          cur = g[i][j][k]
          for zz in range(k+1,mz):
            if g[i][j][zz] != '.':
              #G[cur].append(g[i][j][zz])
              G[g[i][j][zz]].append(cur)
      s.append( [g[i][j][k] for k in range(mz)] )
    print(s)

  # fall down
  #GG = defaultdict(list)
  for c in G:
    if c in G[c]:
      G[c].remove(c)
    #for cc in G[c]:
    #  GG[cc].append(c)
  #G = {}
  res = 0
  for c in range(ct):
    ch = chr(c+ord('A'))
    if len(G[ch]) > 1:
      res += 1
  print( res ) ,

  