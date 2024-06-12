
#mport zip

def ints(line):
  return [int(i) for i in line.split()]



with open("11.txt") as f:

  mat = []
  ct = 0
  pla = []
  dbr = set()
  dbc = set()
  
  for a in f.read().splitlines():
    for j in range(len(a)):
      if a[j] =='#':
        pla.append((ct,j))
    #else:
    #dbr.add(ct)
    mat.append([c for c in a])
    if '#' not in mat[-1] :
      dbr.add(ct)
    mat.append([c for c in a])

    ct+=1
  #print(mat)
  matt = list(zip(*mat))
  for i in range(len(matt)):
    if '#' not in matt[i] :
      dbc.add(i)

  print(dbr, dbc)
  
  d = 0
  pla.sort()

  print(pla)
  for i in range(len(pla)):
    for j in range(i+1,len(pla)):
      x0,y0, x1,y1 = pla[i][0],pla[i][1],pla[j][0],pla[j][1]
      if x0 > x1:
        x0 , x1 = x1, x0
      if y0 > y1:
        y0,  y1 = y1, y0
      s1 = sum(1 for x in dbr if x in range(x0,x1+1))
      s2 = sum(1 for x in dbc if x in range(y0,y1+1))
      d += abs(pla[i][0] - pla[j][0]) + abs(pla[i][1] - pla[j][1]) + 999_999 * (s1+s2) 
  #print(pla)
  #print(len(pla))
  print(d)
