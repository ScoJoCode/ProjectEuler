import time
from tools import *

def getVal(a):
  wa = str(a)
  l = len(wa)
  suma = 0
  for i in range(0,l):
    suma+=l**int(wa[i])
  return suma

start = time.time()

ans=0
nPerm=5
i=2
cubes=[1]
cube=1
p = 1
notFound=True
while notFound:
  if 10**p<cube:
    #now have all the cubes with this number of digits
    dVal = {}
    dNum = {}
    for j in range(0,len(cubes)):
      val = getVal(cubes[j])
      if val in dVal:
        dVal[val]+=1
        if dVal[val]==nPerm:
          ans = dNum[val]
          notFound=False
          break
      else:
        dVal[val]=1
        dNum[val]=cubes[j]
    p+=1
    cubes=[]
  cube = i**3
  cubes.append(cube)
  i+=1

end = time.time()
print ans
print 'time elapsed: ' + str(end-start)
