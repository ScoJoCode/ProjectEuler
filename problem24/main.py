import time
import math
start = time.time()

a=[0,1,2,3,4,5,6,7,8,9]
b=[]

#nPerms = 1000000
nPerms = 999999
for i in range(0,10):
  num = nPerms/math.factorial(9-i)
  b.append(a[num])
  nPerms-=num*math.factorial(9-i)
  print a[num]
  a.remove(a[num])


end = time.time()
print 'time elapsed: ' + str(end-start)
