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

#0 means R, 1 means D, 2 means L, and 3 means U
with open("1919.txt") as f:

  coor = []
  r = True
  rl = defaultdict()
  ord = []
  for a in f.read().splitlines():
    #rule = 
    if not a:
      r = False
      continue

    if r:
      # px{a<2006:qkq,m>2090:A,rfg}

      rule, list = a.split('{')
      list = list[:-1]
      ord.append(rule)
      print(rule, list)
      rl[rule] = list
      list = list.split(',')
      cur_lis = []
      for i in range(len(list)-1):
        ru = list[i]
        label, sign, limit , dest = 0,0,0,0
        if '>' in ru:
          sign = '>'
          label, rest = ru.split('>')
        if '<' in ru:
          sign = '<'
          label, rest = ru.split('<')

        limit, dest = rest.split(':')
        #rl[rule]
        cur_lis.append((label,sign,limit,dest))

      cur_lis.append(list[-1])

      rl[rule] = cur_lis
        
    else:

      a = a[1:-1]

      a = a.split(',')
      print(a)
      x = int(a[0][2:])
      m = int(a[1][2:])
      aa = int(a[2][2:])
      s = int(a[3][2:])

      coor.append((x,m,aa,s))

  #print(len(coor))
  #print(len(rl))
  #print(coor)
  print(coor)
  print(len(coor))
  print(rl)
  rl['A'] = 'A'
  rl['R'] = 'R'
  rtot = 0
  for x,m,a,s in coor:
    #fr = ''
    
    cr = rl['in']
    cv = 'in'
    while True:
      print( cv)
      if cr == 'A':
        print('A res', x,m,a,s, x+m+a+s)
        rtot+= x+m+a+s
        break
      elif cr == 'R':
        print('R res', x,m,a,s)
        break
      for cur in cr:
        if type(cur) != tuple:
          cr = rl[cur]
          cv = cur
          break
        else:
          print(cur)
          label, sign, limit , dest = cur[0], cur[1], cur[2], cur[3]

          val = 0
          if label == 'a':
            val = a
          if label == 'm':
            val = m
          if label == 's':
            val = s
          if label == 'x':
            val = x
  
          if sign == '>':
            if val > int(limit):
              cr = rl[dest]
              cv = dest
              break
          elif sign == '<':
            if val < int(limit):
              cr = rl[dest]
              cv = dest
              break
  print(rtot)