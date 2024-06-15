
def ints(line):
  return [int(i) for i in line.split()]

t = 0
with open("9.txt") as f:


  for a in f.read().splitlines():

    cur = ints(a)
    diff = 0
    tt = 0
    arr = []
    arr2 = []
    arr3 = []
    #ddd = []
    while not all(d == 0 for d in cur):
      s = []
      #diff = cur[1] // cur[0]
      #print(diff)
      la = 0
      cc = 0
      #arr = []
      arr.append(cur[0])
      arr2.append(cur[1])
      print(cur)
      
      for i in range(len(cur)-1):
        s.append(cur[i+1] - cur[i])
        #if cc == 0:
        #  cc = 1
        #  continue
        #if c//diff <= 0:
        #  continue
        #print(c-diff)
        #print(c//diff)
        #s.append(max(c//diff,0))
        #la = c
        #arr.append()
      #arr.append(s[0])
      #print('arr', arr)
      #tt += cur[1] - cur[0]#+= cur[0] - diff#- diff#- (cur[1] - cur[0])#cur[-1] #+ diff[i]
      #diff =  s[1] - s[0]
      #arr3.append(s[0])
      cur = s
    arr.append(0)
    res = []
    for i in range(len(arr)-2,-1,-1):
      arr[i] -= arr[i+1]
      #res.append(arr[i] - arr[i+1])
    #print(res)
    #print('final', arr[0])
    print('arr', arr)
    #print(res)
    #print('arr2 hello', arr2)
    #print(tt)
    #print(arr[0]-arr[1])
    #print(arr[0] - (sum(arr[1:]) - sum(arr[0:]) ) )
    #print()
    t += arr[0]#arr[0]-arr[1]

print(t)
