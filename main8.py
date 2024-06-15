import collections
import math

def ints(line):
  return [int(i) for i in line.split()]

ct = 1

dir = ''
edges= []
ed = {}

start = []
end = set()

with open("8.txt") as f:

  for a in f.read().splitlines():
    #f, s = a.split(' ')
    if ct == 1:
      dir = a
      print(a)
    else:
      l,r = a.split("=")
      l = l.strip()
      r = r.strip()
      r = r[1:-1]
      s,e = r.split(", ")
      #a.remove('(')
      #a.remove(')')
      #edges.append(a)
      print(l,s,e)
      ed[l] = (s,e)
      if l[-1] == 'A':
        start.append(l)
      if l[-1] == 'Z':
        end.add(l)
    ct += 1

res = 0
#for v in start:
cres = 1
ind = 0
cur = start #v#'AAA'
#print(len(start))
ress = []
for c in start:
  ccc = 0
  print(c,'start')
  while True:
    #print(cur )
    #print(cres)
    #if all(c in end for c in cur):# 'ZZZ':
    if c in end :# 'ZZZ'
      print(c, ccc)
      ress.append(ccc)
      cres = math.lcm(cres,ccc )
      #res = max(res, cres)
      #res = 
      break
  
    if dir[ind] == 'R':
      '''cc = []
      for c in cur:
        #cur = ed[cur][1]
        cc.append(ed[c][1])
      cur = cc
      '''
      c = ed[c][1]
    if dir[ind] == 'L':
      
      '''cc = []
      for c in cur:
        #cur = ed[cur][1]
        cc.append(ed[c][0])
      cur = cc
      #cur = ed[cur][0]
      '''
      c = ed[c][0]
    ccc += 1
    ind += 1
    if ind == len(dir):
      ind = 0

print(cres)
#print(res)
#print(res)