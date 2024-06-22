from functools import cache
from collections import defaultdict, deque
import math

def ints(s, split=' '):
    return [int(x) for x in s.split(split) if x]

def colon(s):
    return s.split(': ')[1]

def merge(l):
    return ''.join([str(x) for x in l])

def pp(g):
  for gg in g:
    print(gg)

def tp(g):
  return tuple(sum(g, []))

digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

digmap = {}

for i, x in enumerate(digits):
    digmap[x] = i

grid = []

with open("14.txt") as f:
  blo = []
  for a in f.read().splitlines():
    grid.append(a)

  M = len(grid)
  N = len(grid[0])

  def cal(grid):
    r = 0
    for j in range(N):
      #pf = -1 
      s = M
      for i in range(M):
        if grid[i][j] == 'O':
          r += s
          s -= 1 
        elif grid[i][j] == '#':
          #s = M - i - 1 
          s -= 1
        elif grid[i][j] == '.':
          #continue 
          s -= 1
    return r

  og = grid

  def rock_and_roll(old_grid,new_grid, direction):

    if direction == "N":
      for j in range(len(old_grid[0])):
        p = 0
        for i in range(len(old_grid)):
          if old_grid[i][j] == 'O':
            new_grid[p][j] = 'O'
            p+=1
          elif old_grid[i][j] == '#':
            new_grid[i][j] = '#'
            p = i + 1
    elif direction == "E":
        for i in range(len(old_grid)):
          p = len(old_grid[0])-1
          for j in range(len(old_grid[0])-1,-1,-1):
              if old_grid[i][j] == 'O':
                new_grid[i][p] = 'O'
                p-=1
              elif old_grid[i][j] == '#':
                new_grid[i][j] = '#'
                p = j - 1
    elif direction == "S":
      for j in range(len(old_grid[0])):
        p = len(old_grid) -1 
        for i in range(len(old_grid) -1,-1,-1):
          if old_grid[i][j] == 'O':
            new_grid[p][j] = 'O'
            p-=1
          elif old_grid[i][j] == '#':
            new_grid[i][j] = '#'
            p = i - 1
    elif direction == "W":
      for i in range(len(old_grid)):
        p = 0
        for j in range(len(old_grid[0])):
            if old_grid[i][j] == 'O':
              new_grid[i][p] = 'O'
              p+=1
            elif old_grid[i][j] == '#':
              new_grid[i][j] = '#'
              p = j + 1
  
  s = {}
  
  #print(cal(og))
  ng = [['.']*N for _ in range(M)]
  rock_and_roll(og,ng,'N')
  print(cal(ng))

  sv = {}
  si = {}
  for i in range(1,1_000_000_001):

    for D in 'NWSE':
      ng = [['.']*N for _ in range(M)]
      rock_and_roll(og,ng,D)
      #pp(ng)
      #print(cal(ng))
      og = ng

    #pp(og)

    r = cal(ng)
    #print(r)
    tt = tp(og)
    #print(tt)
    if tt in s:
      diff = i - s[tt]
      print('diff', diff)
      print('id', (1_000_000_000 - i) % diff)
      print( si[ i - diff + (1_000_000_000 - i) % diff ])
      #print()
      print('found', si[ i - diff + (1_000_000_000 - i) % diff ])
      print(si)
      break

    s[tt] = i
    sv[tt] = cal(ng)
    si[i] = cal(ng)
    #s.add(tt)

    ng = og
