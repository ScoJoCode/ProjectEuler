import time
from tools import *

start = time.time()

up=1001
#up=8
D=0
max=0
for i in range(2,up):
  if isSquare(i):
    continue
  j=2
  while True:
    #x2=1+j*j*i
    Dy2=j*j-1
    if Dy2%i!=0:
      j+=1
      continue
    y2=Dy2/i
    
    if isSquare(y2):
      print ' '
      print i
      y=m.sqrt(y2)
      print j
      if j>max:
        max=j
        D=i
      break
    j+=1

end = time.time()
print D
print 'time elapsed: ' + str(end-start)
