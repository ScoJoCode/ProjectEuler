import time
from tools import *

start = time.time()

length = {}
chain = {}

def foundLoop(n,m,l):
  p = getNext(m)
  if p==n:
    length[m]=l
    return l
  length[m]=foundLoop(n,p,l+1)
  return length[m]

def getDistance(n):
  if n in length:
    return length[n]
  else:
    if n in chain:
      foundLoop(n,n,1)
      return length[n]
    else:
      chain[n]=getNext(n)
      Len=getDistance(getNext(n))+1
      if n in length:
        return length[n]
      else:
        length[n]=Len
        return Len


def getNext(n):
  w = str(n)
  next=0
  for c in w:
    next+=m.factorial(int(c))
  return next

ans=0
up=1000000
for i in range(1,up):
  l = getDistance(i)
  if l==60:
    ans+=1

end = time.time()
print ans
print 'time elapsed: ' + str(end-start)
