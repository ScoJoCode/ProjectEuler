import time
import numpy as np
start = time.time()

arrays = [np.array(map(int,line.split())) for line in open('data.txt')]

length= len(arrays)
data = []
for i in range(0,length):
  data.append([])
  for j in range(0,len(arrays[i])):
    data[i].append(arrays[i][j])

for i in range(length-1,0,-1):
  for j in range(0,i):
    if data[i][j]>data[i][j+1]:
      data[i-1][j]=data[i-1][j]+data[i][j]
    else:
      data[i-1][j]=data[i-1][j]+data[i][j+1]
end = time.time()
print data[0][0]
print 'time elapsed: ' + str(end-start)
