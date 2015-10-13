import time
import math
import numpy as np

start = time.time()

def isPent(p):
  n = (1./2+math.sqrt(1./4+2*3*1.0*p))/(3./2)
  if math.ceil(n)==math.floor(n):
    return True
  return False

i=1
j=1
found = False
while not found:
  pentI = i*(3*i-1)/2
  j=1
  while j < i:
    pentJ = j*(3*j-1)/2
    if isPent(pentI-pentJ) and isPent(pentI+pentJ):
      ans = pentI-pentJ
      found=True
      break
    j+=1
  i+=1

#print isPent(1)
#print isPent(2)
#print isPent(5)



end = time.time()
print ans
print 'time elapsed: ' + str(end-start)
