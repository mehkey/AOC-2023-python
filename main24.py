from functools import cache
from collections import defaultdict, deque
from heapq import heappop, heappush
import math
import time
from types import GeneratorType
import numpy as np

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

MP = {UU:U, DD:D, LL:L, RR:R}

grid = []

#0 means R, 1 means D, 2 means L, and 3 means U
def find_intersection(line1, line2):
  # Extracting start points and velocities of the lines
  x1, y1, z1, vx1, vy1, vz1 = line1
  x2, y2, z2, vx2, vy2, vz2 = line2

  if (vx1 * vy2 - vx2 * vy1) == 0:
    return -1,-1,-1
  if  (vx2 * vy1 - vx1 * vy2) == 0:
    return -1,-1,-1

  # Solving for t1 and t2
  t1 = (vy2 * (x2 - x1) + vx2 * (y1 - y2)) / (vx1 * vy2 - vx2 * vy1)
  t2 = (vy1 * (x2 - x1) + vx1 * (y1 - y2)) / (vx2 * vy1 - vx1 * vy2)
  
  if t1 < 0 :
    return -1,-1,-1

  if t2 > 0:
    return -1,-1,-1

  xi = x1 + vx1 * t1
  yi = y1 + vy1 * t1
  zi = z1 + vz1 * t1

  return xi, yi, zi
  
  # Calculating intersection point
  xi = x1 + vx1 * t1
  yi = y1 + vy1 * t1

  return xi, yi

  # Solving for t1 and t2
  t1 = (vx2 * (y2 - y1) + vy2 * (x1 - x2)) / (vx1 * vy2 - vx2 * vy1)
  
  t2 = (vx1 * (y2 - y1) + vy1 * (x1 - x2)) / (vx2 * vy1 - vx1 * vy2)

  # Calculating intersection point
  xi = x1 + vx1 * t1
  yi = y1 + vy1 * t1
  zi = z1 + vz1 * t1

  return xi, yi, zi

#print line_intersection((A, B), (C, D))

with open("2424.txt") as f:

  coor = []
  for a in f.read().splitlines():
    #blo.extend(  a.split(',') )
    #grid.append(a)
    #for a in f.read().splitlines():
      #blo.extend(  a.split(',') )
    #grid.append(a)
    l,r = a.split(' @ ')
    coor.append( (ints(l, ',')+ints(r, ',') ) )

  print(coor)

  N = len(coor)

  res = 0
  s = set()
  rr = []
  for i in range(N):
    for j in range(i+1,N):
      line1 = coor[i]
      line2 = coor[j]
      MI = 7#200000000000000 #7
      MA = 27#400000000000000 #27
      x,y,z = find_intersection(line1, line2)
      if x != -1 and x > MI and x < MA and y > MI and y < MA:
        rr.append((x,y,z))
        #rr.append((x,y,z))
  print(rr) 
  print(sum(rr[0]), sum(rr[1]))

  '''
  res = 0
  for i in range(N):
    for j in range(i+1,N):

      # Given these endpoints
      #line 1
      #A = [X, Y]
      #B = [X, Y]

      line1 = coor[i]
      line2 = coor[j]

      #line 2
      #C = [X, Y]
      #D = [X, Y]
      MI = 200000000000000 #7
      MA = 400000000000000 #27
      x,y = find_intersection(line1, line2)
      if x != -1 and x > MI and x < MA and y > MI and y < MA:

        res += 1

  A = np.empty((0,3))#np.array([[]]) #np.empty((0,2))#np.array([])
  b = np.array([])
  i = 0
  for c in coor:
    #print(A,b)
    x1, y1, z1, vx1, vy1, vz1 = c
    #
    #A = np.array([[8, 3, -2], [-4, 7, 5], [3, 4, -12]])
    #b = np.array([9, 15, 35])
    A = np.concatenate( (A, [ [vx1, vy1, vz1]] ), axis=0 )
    #A.append([vx1, vy1, vz1])
    b = np.append( b, [-x1 - y1 - z1], axis=0 )
    #print(A,b)
    #b.append(x1 + y1 + z1)
    i+=1
    if i == 3:
      break
  print(A,b)
  print(len(A),len(b))
  x = np.linalg.solve(A, b)
  print(x)
  #y = np.linalg.svd(A,b)
  #print(y)
  #x
  #print(res)
  '''
  #for c in coor[:2]:


  #for c in coor[2:4]:
    
      #coor.append(grid)