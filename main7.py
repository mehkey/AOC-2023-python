import collections
from collections.abc import MappingView


def ints(line):
  return [int(i) for i in line.split()]


ct = 0
dis = []
tra = []

D = 0
T = 0

res = []
r = 0
cds = 'J23456789TQKA'

ci = {v: i for i, v in enumerate(cds)}


def cal(x):
  rrr = [0, 0, 0, 0, 0]
  print('x', x)
  for i, v in enumerate(x):
    rrr[i] = ci[str(v)]
  return tuple(rrr)


hm = {}

with open("7.txt") as f:

  for a in f.read().splitlines():
    f, s = a.split(' ')
    s = int(s)
    res.append([f, s])

  for f, s in res:
    c = {}
    rr = 0
    for l in f:
      if l == 'J':
        continue
      c[l] = c.get(l, 0) + 1
      if c[l] == 2:
        rr += 1
      if c[l] == 3:
        rr += 3
      if c[l] == 4:
        rr += 6
      if c[l] == 5:
        rr += 7
    print(c)
    if c:
      mv = max(c.values())
    else:
      mv = 0
    for i in range(f.count('J')):
      #if mv == 0:
        #rr += 1
      if mv == 1:
        rr += 1
      if mv == 2:
        rr += 3
      if mv == 3:
        rr += 6
      if mv == 4:
        rr += 7
      mv += 1
    #if rr == 0:
    #  rr = 0.1*max(cal(f))
    hm[f] = rr

  res.sort(key=lambda x: (hm[x[0]], cal(x[0])))

  rank = 1
  for f, s in res:
    print('rank', rank, f, s, hm[f], cal(f))
    r += rank * s
    rank += 1

  print(res)
  print(r)
