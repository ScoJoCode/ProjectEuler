import time
import math
import numpy as np

start = time.time()
f = open('problem42.txt','r')


words = (f.readline()).replace('"','').split(',')

max = 0
ans=0

for w in words:
  sum = 0
  for i in range(0,len(w)):
    sum+=ord(w[i])-ord('A')+1
  a = 1.0*(-1+math.sqrt(1+4*2*sum))/2
  if math.ceil(a)==math.floor(a):
    ans+=1

end = time.time()
print ans
print 'time elapsed: ' + str(end-start)
