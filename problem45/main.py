import time
import math
import numpy as np

start = time.time()

def isPent(p):
  n = (1./2+math.sqrt(1./4+2*3*1.0*p))/(3./2)
  if math.ceil(n)==math.floor(n):
    return True
  return False

def isHex(h):
  n = (1+math.sqrt(1+4.*2*h))/4
  if math.ceil(n)==math.floor(n):
    return True
  return False

howMany = 0
i=1
ans=0
while True:
  triI = i*(i+1)/2
  if isPent(triI) and isHex(triI):
    howMany+=1
    if howMany==3:
      ans=triI
      break
  i+=1


end = time.time()
print ans
print 'time elapsed: ' + str(end-start)
