import time
import numpy as np
from tools import *
start = time.time()

#colomn 1+= column 0; then find the min of [i-1][j],[

data = np.loadtxt('matrix82.txt',delimiter=',')
#data = [[131,673,234,103,18],[201,96,342,965,150],[630,803,746,422,111],[537,699,497,121,956],[805,732,524,37,331]]
L = len(data)

path = [x[:] for x in [[0]*L]*L]

#propagate minimum sums from left to right
#might be able to reduce the final nested loop to make a little faster
for j in range(0,L-1):
  for i in range(0,L):
    if j==0:
      path[i][j]=data[i][j]
      continue
    low = data[i][j]+path[i][j-1]
    for k in range(0,L):
      if k==i:
        continue
      sum = path[k][j-1]+data[i][j]
      if k<i:
        for l in range(k,i):
          sum+=data[l][j]
      if k>i:
        for l in range(i+1,k+1):
          sum+=data[l][j]
      low = min(low,sum)
    path[i][j]=low

ans = path[0][L-2]+data[0][L-1]
for i in range(1,L):
  ans = min(ans,path[i][L-2]+data[i][L-1])

end = time.time()
print path
print data
print ans
print 'time elapsed: ' + str(end-start)
