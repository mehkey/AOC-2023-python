
from functools import cache
from collections import defaultdict, deque
import math
from numpy import inf

def ints(line):
  return [int(i) for i in line.split(',')]


with open("1212.txt") as f:

  mat = []
  pla = []
  dbr = set()
  dbc = set()
  pos, l = [],''
  


  res = 0
  for a in f.read().splitlines():
    l, r = a.split(' ')

    @cache
    def dp(i,j, cur):

      print(M,N,0)

      if i >= M and j >= N:
        return 1

      if i >= M:
        return 1

      if j >= N:
        return 0

      if cur > pos[i]:
        return 0

      if cur == pos[i]:
        if i+1 == M or l[i] == '.'  or l[i] == '?':
          return dp(i+2,j+1, 0, hm)
        else:
          return 0
      if l[j] == '.':
        return inf
      v = 0

      if l[j] == '?':
        v =  dp(i, j+1, cur,hm) + dp(i, j+1, cur+1,hm)
      elif l[j] == '#':
        v =  dp(i, j+1, cur+1,hm)

      return v

    pos = ints(r)
    hm = {}
    M = len(l)
    N = len(pos)
    v = dp(0,0,0, hm)
    print(l,pos)
    print(v)

    res += v
    
  print(res)