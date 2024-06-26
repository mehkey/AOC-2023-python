with open("3.txt") as f:
  '''s = 0

  res = 0
  res2 = 0
  g = 0
  m = []
  for x in f.read().splitlines():
    m.append(x)

  #for i in range()
  #print(m)
  N = len(m)
  M = len(m[0])

  dirs = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]

  valid = '123456789.'
  valid1 = '123456789'

  for i in range(N):
    curr = []
    for j in range(M):
      cur = m[i][j]
      if ord('0') <= ord(cur) <= ord('9'):
        curr.append(cur)

      if  j == M - 1 or m[i][j+1] not in valid1:
        if len(curr) > 0:
          #print(curr)
          num = int(''.join(curr))

          found = False
          for jj in range(j, j - len(curr) - 1, -1):
            for d in dirs:
              nx = i + d[0]
              ny = jj + d[1]

              if 0 <= nx < N and 0 <= ny < M:
                if m[nx][ny] in '@#$%^&*()_+=/':
                  print('found', num)
                  res += num
                  found = True
                  break

            if found:
              break
          curr = []

  print(res)
  '''
  l = []
  for a in f.read().splitlines():
    l.append(a)
  #print(l)
  R, C = len(l), len(l[0])
  print(R, C)
  safe = set()
  for i in range(R):
    for j in range(C):
      c = l[i][j]
      if not ('0' <= c <= '9') and c != '.':
        for dx in range(-1, 2):
          for dy in range(-1, 2):
            safe.add((i + dx, j + dy))
  #print(safe)
  ret = 0
  for i in range(R):
    q = 0
    en = False
    sf = False
    for j in range(C):
      try:
        v = int(l[i][j])
        q = 10 * q + v
        if (i, j) in safe:
          sf = True
      except:
        en = True
      if en:
        if sf:
          ret += q
        q = 0
        sf = False
        en = False
    if sf:
      ret += q

  print(ret)
