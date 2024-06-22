from functools import cache
from collections import defaultdict, deque
import math
import time

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

with open("16.txt") as f:
  #blo = []

  for a in f.read().splitlines():
    #blo.extend(  a.split(',') )
    grid.append(a)
  s = 0
  print('\\')
  M = len(grid)
  N = len(grid[0])
  ext = [ [defaultdict(list) for j in range( N)]for i in range(M)]
  (L,R,U,D) = 'LRUD'
  print(L,R,U,D)
  for i in range(M):
    for j in range(N):
      #if j == 3 and i == 7:
      #  print(grid[i][j], "HH")
      if grid[i][j] == '-':
        #for d in L+R+U+D:
        ext[i][j][L].append((i,j+1,L))
        ext[i][j][R].append((i,j-1,R))
        #if j == 3 and i == 7:
        #  print(grid[i][j], "HERE")
        for d in U+D:
          #print(d)
          ext[i][j][d].append((i,j+1,L))
          ext[i][j][d].append((i,j-1,R))

      if grid[i][j] == '\\':
        #for d in L+D:
          ext[i][j][D].append((i,j-1,R))
          #ext[i][j][D].append((i,j-1,R))
          ext[i][j][L].append((i+1,j,U))
        #for d in U+R:
          ext[i][j][R].append((i-1,j,D))
          ext[i][j][U].append((i,j+1,L))

      if grid[i][j] == '/':
          ext[i][j][U].append((i,j-1,R))
          ext[i][j][L].append((i-1,j,D))
          ext[i][j][R].append((i+1,j,U))
          ext[i][j][D].append((i,j+1,L))
      if grid[i][j] == '|':
        for d in L+R:
          ext[i][j][d].append((i+1,j,U))
          ext[i][j][d].append((i-1,j,D))
        ext[i][j][U].append((i+1,j,U))
        ext[i][j][D].append((i-1,j,D))

      '''
      if grid[i][j] == '-':
        for d in L+R+U+D:
          ext[i][j][d].append((i,j+1,L))
          ext[i][j][d].append((i,j-1,R))
  
      if grid[i][j] == '\\':
        for d in L+D:
          ext[i][j][d].append((i,j-1,R))
          ext[i][j][d].append((i+1,j,U))
        for d in U+R:
          ext[i][j][d].append((i-1,j,D))
          ext[i][j][d].append((i,j+1,L))

      if grid[i][j] == '/':
        for d in L+U:
          ext[i][j][d].append((i,j-1,R))
          ext[i][j][d].append((i-1,j,D))
        for d in D+R:
          ext[i][j][d].append((i+1,j,U))
          ext[i][j][d].append((i,j+1,L))
      if grid[i][j] == '|':
        for d in L+R+U+D:
          ext[i][j][d].append((i+1,j,U))
          ext[i][j][d].append((i-1,j,D))
      '''
  q = deque()
  v = set()
  vv = set()
  mm = 0

  def dfs(q,v,vv):
    #nonlocal q, v, vv

    while q :
      #k+=1
      cx, cy, cd = q.popleft()
      
      
      #print(cx,cy,cd)
      #for i in range(M):
      #  l = ['#' if (i,j) in vv else '.' for j in range(N)]
      #  print(l)
      # time.sleep(0.2)
      #if (cx,cy) in v:
      #  continue
      #if cx == 6 and cy == 6:
        #print(grid[cx][cy])
        #print('here')
        #print(cd, ext[cx][cy][cd])
      g = grid[cx][cy]
      if grid[cx][cy] == '.':
        nx, ny = cx, cy
        if cd == L:
          ny += 1
        if cd == R:
          ny -= 1
        if cd == U:
          nx += 1
        if cd == D:
          nx -= 1

        if not( nx < 0 or nx >= M or ny < 0 or ny >= N):
          
          if (nx,ny,cd) not in v:
            v.add((nx,ny,cd))
            vv.add((nx,ny))
            q.append((nx,ny,cd))

      if grid[cx][cy] in '-|/\\':
        #if  cy == 3:
        #  print(grid[cx][cy])
        #  print(ext[cx][cy][cd])
        for nx, ny, nd in ext[cx][cy][cd]:
          if nx < 0 or nx >= M or ny < 0 or ny >= N:
            continue
  
          if (nx,ny,nd) not in v:
            v.add((nx,ny,nd))
            vv.add((nx,ny))
            q.append((nx,ny,nd))

  
  for j in range(N):
    q.append((0,j,U))
    v.add((0,j,U))
    vv.add((0,j))
    dfs(q,v,vv)
    mm=max(mm,len(vv))
    if len(vv) == 61:
      pp(vv)
    q = deque()
    v = set()
    vv = set()
    
    q.append((M-1,j,D))
    v.add((M-1,j,D))
    vv.add((M-1,j))
    dfs(q,v,vv)
    mm=max(mm,len(vv))
    if len(vv) == 61:
      pp(vv)
    q = deque()
    v = set()
    vv = set()

  for i in range(M):
    q.append((i,0,L))
    v.add((i,0,L))
    vv.add((i,0))
    dfs(q,v,vv)
    mm=max(mm,len(vv))
    if len(v) == 61:
      pp(vv)
    q = deque()
    v = set()
    vv = set()

    q.append((i,N-1,R))
    v.add((i,N-1,R))
    vv.add((i,N-1))
    dfs(q,v,vv)
    mm=max(mm,len(vv))
    if len(v) == 61:
      pp(vv)
    q = deque()
    v = set()
    vv = set()
  q.append((0,3,U))
  v.add((0,3,U))
  vv.add((0,3))
  dfs(q,v,vv)
  print(mm)
  #print(len(vv))

  #print(ext[6][3])
  #print(ext[7][3])
  #print(grid)
  #boxes = defaultdict(list)
  #boxset = defaultdict(set)