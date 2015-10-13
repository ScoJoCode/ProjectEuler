import time
import numpy as np
import math as m
start = time.time()

data = np.loadtxt('base_exp.txt',delimiter=',')

BASE=519432
POW=525806
line=0
for i in range(1,len(data)):
  if(BASE<pow(data[i][0],1.0*data[i][1]/POW)):
    line=i
    BASE=data[i][0]
    POW=data[i][1]


end = time.time()
print line+1
print 'time elapsed: ' + str(end-start)
