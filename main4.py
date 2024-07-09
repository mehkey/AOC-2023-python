def ints(line):
  return [int(i) for i in line.split()]

res =0
r2 = 0

with open("4.txt") as f:

  #f.read().readLines()

  ct = 1
  hm = {}
  c ={}
  for a in f.read().splitlines():
    
    left,right = a.split('|')

    bad, left = left.split(':')
    print(left)
    print(right)
    s = set(ints(right))
    ss = set(ints(left))
    hm[ct] = 0
    
    #if not len(s&ss):
    #  continue
    #for v in s & ss:
    print(len(s&ss))
    print(2**(len(s&ss)-1))
    res += (2**(len(s&ss)-1))
    hm[ct] = len(s&ss) 
    c[ct] = 1
    ct += 1
    

  print(ct)
  for i in range(1,ct):
    for j in range(i+1, min(i+hm[i]+1,ct)):

      c[j] += c[i] 
    r2 += c[i]
    print(i,c[i],hm[i])
    #hm[i]+=1

print(res)
print(sum(hm))
print(r2)