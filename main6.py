from types import TracebackType


def ints(line):
  return [int(i) for i in line.split()]


ct = 0
dis = []
tra = []

D = 0
T = 0

with open("6.txt") as f:

  for a in f.read().splitlines():
    if ct == 0:
      tra = ints(a)
    else:
      dis = ints(a)
    ct += 1

D = int(''.join([str(v) for v in dis]))
T = int(''.join([str(v) for v in tra]))

print(T,D)
res = 1
for i,t in enumerate(tra):

  count = 0
  for j in range(1,t+1):
    dd = dis[i]
    tt = t - j

    if j * tt > dd:
      count += 1

  print(count)
  res*= count

print('res',res)

count = 0
for j in range(1,T+1):
  dd = D
  tt = T - j

  if j * tt > dd:
    count += 1

print('final', count)
  