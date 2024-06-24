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

with open("15.txt") as f:
  blo = []
  
  for a in f.read().splitlines():
    blo.extend(  a.split(',') )
  s = 0

  boxes = defaultdict(list)
  #boxset = defaultdict(set)

  for b in blo:
    cur = 0
    for c in b:
      if c == '=' or c == '-':
        break
      cur += ord(c)
      cur *= 17
      cur %= 256
    #print('cur',cur)
    hv = cur

    if b[-1] == '-':
      label = b[:-1]
      #print(boxes[hv])
      for i,  (curl, curr) in enumerate(boxes[hv]):
        if curl == label:
          #del boxes[hv][i]
          #print()
          boxes[hv].pop(i)

    else:
      left,right = b.split('=')
      found = False
      for i, (curl, curr) in enumerate(boxes[hv]):
        if curl == left:
          #boxes[hv].remove((curl, curr))
          #boxes[hv].append((right, curr))
          boxes[hv][i][1] = right
          found = True
          break
      if not found:
        boxes[hv].append([left,right])

    

  rr = 0 
  for i in range(256):
    for j,(l,r) in enumerate(boxes[i]):
      val = (i+1) * (j+1) * int(r)
      print(val, i+1, j+1, int(r))
      rr += val
  print('rr',rr)
  print('s',s)
  print(blo)
