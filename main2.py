ma = {'red': 12, 'blue': 14, 'green': 13}

#print('hi')
with open("2.txt") as f:
  s = 0

  res = 0
  res2 = 0
  g = 0
  for x in f.read().splitlines():
    g += 1

    x = x.split(': ')[1]
    pairs = x.split('; ')

    mr = 0
    mg = 0
    mb = 0

    gp = True
    for p in pairs:

      count = {'red': 0, 'blue': 0, 'green': 0}

      cur = p.split(', ')

      for bead in cur:

        bead = bead.split(' ')
        #print(bead)
        val = int(bead[0])
        count[bead[1]] += val
        if bead[1] == 'green':
          mg = max(mg, val)
        if bead[1] == 'blue':
          mb = max(mb, val)
        if bead[1] == 'red':
          mr = max(mr, val)
      if count['red'] > ma['red'] or count['blue'] > ma['blue'] or count[
          'green'] > ma['green']:
        gp = False

    res2 += mg * mb * mr
    if gp:
      #print('good', g)
      #print(g)
      res += g

  print(res)
  print(res2)
#print('end')
