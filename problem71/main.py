import time
from tools import *

start = time.time()

lim = 3.0/7
max=0.
ans2=0
for i in range(2,1000001):
  num = 3*i/7
  att = num*1./i
  if att>max and att < lim: #wonder if this always work or if fp precision screws it up
    if i==7:
      continue
    max=att
    ans=i
    ans2=num
 

end = time.time()
print ans
print ans2
print 'time elapsed: ' + str(end-start)
