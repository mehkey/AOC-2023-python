def ints(line):
  return [int(i) for i in line.split()]

from collections import deque

start ='S'
x0 = y0 = 0

'''
| is a vertical pipe connecting north and south.
- is a horizontal pipe connecting east and west.
L is a 90-degree bend connecting north and east.
J is a 90-degree bend connecting north and west.
7 is a 90-degree bend connecting south and west.
F is a 90-degree bend connecting south and east.
. is ground; there is no pipe in this tile.
S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
'''
S,E,N,W='S','E','N','W'

avail = {'F': {S:E,E:S}, 'L': {N:E,E:N}, 'J': {N:W,W:N}, '7': {S:W,W:S}, '|': {N:S,S:N}, '-':{E:W,W:E}}

exp = []

with open("10.txt") as f:

  mat = []
  ct = 0
  tc = 0
  tot = 0
  for a in f.read().splitlines():

    exp.append([[] for _ in range(len(a))])
    if 'S' in a:
      x0 = ct
      y0 = a.index('S')
    for j in range(len(a)):
      tot += 1
      if a[j] == '.':
        tc+= 1
      if a[j] == 'F':
        exp[ct][j].append((ct,j+1))
        exp[ct][j].append((ct+1,j))
      if a[j] == '7':
        exp[ct][j].append((ct,j-1))
        exp[ct][j].append((ct+1,j))
      if a[j] == 'J':
        exp[ct][j].append((ct-1,j))
        exp[ct][j].append((ct,j-1))
      if a[j] == 'L':
        exp[ct][j].append((ct-1,j))
        exp[ct][j].append((ct,j+1))
      if a[j] == '-':
        exp[ct][j].append((ct,j-1))
        exp[ct][j].append((ct,j+1))
      if a[j] == '|':
        exp[ct][j].append((ct-1,j))
        exp[ct][j].append((ct+1,j))
        
    mat.append(a)
    ct += 1
  M = len(mat)
  NN = len(mat[0])

  #print(exp)

  s = x0,y0
  d = 0
  p = set()
  p.add((x0,y0))
  ttt = 0
  ttt += 1

  q = deque()
  s = set()

  t = 


  for dx,dy,DI in [(1,0,N),(-1,0,S),(0,1,W),(0,-1,E)]:
    nx = x0+dx
    ny = y0+dy

    if (x0,y0) in exp[nx][ny]:
      d = 1
      px, py = x0,y0
      cx, cy = nx, ny
      
      while (cx,cy) != (x0,y0):
        #print(cx,cy)
        #print(d)

        if mat[cx][cy] == 'F':
          #s.add((cx+1,cy+1))
          q.append((cx+1,cy+1))
          #exp[ct][j].append((ct,j+1))
          #exp[ct][j].append((ct+1,j))
        if mat[cx][cy] == '7':
          #s.add((cx+1,cy-1))
          q.append((cx+1,cy-1))
          #exp[ct][j].append((ct,j-1))
          #exp[ct][j].append((ct+1,j))
        if mat[cx][cy] == 'J':
          #s.add((cx-1,cy-1))
          q.append((cx-1,cy-1))
          #exp[ct][j].append((ct-1,j))
          #exp[ct][j].append((ct,j-1))
        if mat[cx][cy] == 'L':
          #s.add((cx-1,cy+1))
          q.append((cx-1,cy+1))
          #exp[ct][j].append((ct-1,j))
          #exp[ct][j].append((ct,j+1))
        
        ttt += 1
        p.add((cx,cy))
        exp[cx][cy].remove((px,py))

        px, py = cx, cy
        cx, cy = exp[cx][cy][0]

        d += 1
    break
  print(d//2)

  q = deque()
  s = set()
  sx = 0
  sy = 0
  for i in range(M):
    q.append((i,0))
    q.append((i,NN-1))
  for j in range(NN):
    q.append((0,j))
    q.append((M-1,j))
  #s.add((0,0))
  #s.add((0,NN-1))
  #s.add((M-1,0))
  #s.add((M-1,NN-1))
  #q.append((sx,sy))

  #q.append((0,0))
  #q.append((0,NN-1))
  #q.append((M-1,0))
  #q.append((M-1,NN-1))

  re = 0
  while q:
    cx,cy = q.popleft()
    #print(cx,cy)
    #if mat[cx][cy]== '.':
    if cx < 0 or cx >= M or cy < 0 or cy >= NN:
      continue
    if (cx,cy) in p or (cx,cy) in s:
      continue
    s.add((cx,cy))
    re += 1
    for dx,dy,DI in [(1,0,N),(-1,0,S),(0,1,W),(0,-1,E)]:
      nx = cx+dx
      ny = cy+dy
      if nx < 0 or nx >= M or ny < 0 or ny >= NN:
        continue
      if (nx,ny) not in p and (nx,ny) not in s:
        #s.add((nx,ny))
        q.append((nx,ny))

  print(tot)
  print(ttt)
  #print(tc)
  print(re)
  print(tot-ttt-re)

  '''
  print(x0,y0)
  q = deque()
  q.append((x0,y0,0))
  d = -1
  #M = len(mat)
  #NN = len(mat[0])
  v = set()
  while q:
    d+=1
    ql = len(q)
    for _ in range(ql):

      x,y,F = q.popleft()

      if (x,y) in v:
        q = []
        break
      v.add((x,y))
      print(x,y)
      cur=mat[x][y]
      print(cur)
      print(F,  avail)
      if cur == 'S':
        for dx,dy,DI in [(1,0,N),(-1,0,S),(0,1,W),(0,-1,E)]:
            nx = x+dx
            ny = y+dy
          if nx < 0 or nx >= M or ny < 0 or ny >= NN:
            continue
          newcur = mat[nx][ny]
          if newcur == '.':
            continue
          #if DI in avail[newcur].keys() :
          q.append((nx,ny,DI))
 
      elif cur in avail.keys(): #and F in avail[cur].keys():
        print('from',F)
        other = avail[cur][F]
        print('other',other)
        if other == N:
          q.append((x+1,y,S))
        elif other == S:
          q.append((x-1,y,N))
        elif other == E:
          q.append((x,y+1,W))
        elif other == W:
          q.append((x,y-1,E))
        nx,ny = q[-1][0],q[-1][1]
        if nx < 0 or nx >= M or ny < 0 or ny >= NN or mat[nx][ny] == '.':
          q.pop()
  '''
  #print(d)  
  #print(mat)