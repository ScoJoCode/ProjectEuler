import time
from tools import *

def isInc(w):
 for i in range(1,len(w)):
   if int(w[i])<int(w[i-1]):
    return False
 return True

def isDec(w):
 for i in range(1,len(w)):
   if int(w[i])>int(w[i-1]):
    return False
 return True

def isBouncy(a):
 w =str(a)
 return (not isInc(w)) and (not isDec(w))


start = time.time()

nBounce=0.
per=.99

i=1
while True:
  if isBouncy(i):
    nBounce+=1
  if nBounce/i==per:
    break
  i+=1


end = time.time()
print i
print 'time elapsed: ' + str(end-start)
