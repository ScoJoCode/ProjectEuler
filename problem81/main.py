import time
import numpy as np
start = time.time()

#this is similar to the triangular sum:
#now I will instead collapse from the top left corner to the middle and then from the middle to the bottom right corner
#Okay, it would be nice to have a min(a,b) definition to replace the if statements

data = np.loadtxt('matrix.txt',delimiter=',')

#propagate sums from top left to the middle diagonal
for i in range(0,len(data)):
  for j in range(0,len(data)-i):
    if j==0 and i==0:
      continue
    if j==0:
      data[i][j]=data[i][j]+data[i-1][j]
    elif i==0:
      data[i][j]=data[i][j]+data[i][j-1]
    elif data[i][j-1]>data[i-1][j]:
      data[i][j]=data[i][j]+data[i-1][j]
    else:
      data[i][j]=data[i][j]+data[i][j-1]

#propagate sums from the middle diagonal to the bottom right
for i in range(1,len(data)):
  for j in range(len(data)-i,len(data)):
    if data[i-1][j]>data[i][j-1]:
      data[i][j]=data[i][j]+data[i][j-1]
    else:
      data[i][j]=data[i-1][j]+data[i][j]

end = time.time()
print data
print data[len(data)-1][len(data)-1]
print 'time elapsed: ' + str(end-start)
