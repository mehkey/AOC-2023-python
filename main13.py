from functools import cache
from collections import defaultdict, deque
import math

def ints(s, split=' '):
    return [int(x) for x in s.split(split) if x]

def colon(s):
    return s.split(': ')[1]

def merge(l):
    return ''.join([str(x) for x in l])

digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
digmap = {}
for i, x in enumerate(digits):
    digmap[x] = i

lines = []
lll = []
with open("13.txt") as f:
    blo = []
    for a in f.read().splitlines():
      lines.append(a)
      if not a:
        lll.append(blo)
        blo = []
        
        continue
      blo.append(a)

    lll.append(blo)
ln = len(lines)

print(ln)
print(lines)
print(lll)

a1, a2 = 0,0
for blo in lll:
  for b in blo:
    print(b)
  M = len(blo)
  N = len(blo[0])

  def match_col(j,k):
    for i in range(M):
      if blo[i][k] != blo[i][j]:
        return False
    return True

  def match_row(j,k):
    for i in range(N):
      if blo[j][i] != blo[k][i]:
        return False
    return True

  def match_col2(j,k):
    count = 0
    for i in range(M):
      if blo[i][k] != blo[i][j]:
        count += 1
        if count > 2:
          break
    return count

  def match_row2(j,k):
    count = 0
    for i in range(N):
      if blo[j][i] != blo[k][i]:
        count += 1
        if count > 2:
          break
    return count

  for i in range(1,M):
    #print(i,min(i, M - i + 2) -1 )
    if 1 == sum( match_row2(i-k-1,i+k) for k in range(0,min(i, M - i ))):
      print('found', i, i-1, i)
      a1 += i 

  for i in range(1,N):
    #print(i,min(i, N - i+2) -1 )
    #print(sum( match_col2(i-k-1,i+k) for k in range(0,min(i, N - i))))
    if 1 == sum( match_col2(i-k-1,i+k) for k in range(0,min(i, N - i))):
      print('foundC', i, i-1, i)
      a2 +=  i 

print( a1 , a2 )

print(a1*100 +a2)
