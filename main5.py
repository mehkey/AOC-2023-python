import math

maps = []

ct = 0

ret = []

r = []
seeds = []
seedss = []


def ints(line):
  return [int(i) for i in line.split()]


with open("5.txt") as f:

  #f.read().readLines()

  ct = 1

  for a in f.read().splitlines():
    #print(a)

    if ct == 1:
      seeds = ints(a)

      seedss = [[a, b] for i, (a, b) in enumerate(zip(seeds, seeds[1:]))
                if i % 2 == 0]

      #print(seeds)
      #print(seedss)
    elif a == ':':
      r.sort()
      maps.append(r)
      r = []
    elif ':' not in a:
      #print("a", a)
      x, y, z = ints(a)
      r.append([y, y + z - 1, x])

    ct += 1
  r.sort()
  maps.append(r)

  mm = math.inf
  mmm = math.inf
  for seed in seeds:
    cur = seed
    for m in maps:
      #print(m)
      for y, y2, x in m:
        if y <= cur <= y2:
          cur = x + (cur - y)
          break
    mm = min(cur, mm)

  mmm = math.inf

  #sd = [[s,e]]

  print(seedss)
  for i, (s, e) in enumerate(seedss):
    seedss[i] = [s, s + e]
  print(seedss)
  seedss.sort(key = lambda x: x[0])
  for m in maps:
    ns = []
    #print('map', m)
    for s, e in seedss:

      #print(s,e)

      #for i in range(s,s+e):
      curs = s
      cure = e
      #print(s,e)
      #for k,v in m.items():
      for y, y2, x in m:
        if y <= curs <= y2:
          #cur = x + (cur - y)
          #mmm = min(cur, mmm)
          diff = curs - y
          diff2 = cure - y
          #diff3 =
          marg = y2 - y
          extra = cure - y2

          if cure <= y2:

            ns.append([x + diff, x + diff2])

          else:
            ns.append([x + diff, x + marg])
            ns.append([y2, cure])
    nss = []

    ps, pe = ns[0][0], ns[0][1]
    for i, (s, e) in enumerate(ns, 1):

      ss, ee = ps, pe
      if ss <= e <= ee or s <= ee <= e:
        ps = min(s, ss)
        pe = max(e, ee)
        #ns.remove(j)
        #tr.append(j)
    #for ind in tr:
    #ns.remove(ind)
      else:
        nss.append([ps, pe])
        ps, pe = s, e

    nss.sort(key=lambda x: x[0])
    seedss = nss[:]
    #print(nss)
  #print(min(seedss))
  #print(mmm)
  print(seedss)
  print(min([x0 for x0, x1 in seedss]))
