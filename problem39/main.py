import time
import math
start = time.time()

most = 0
per = 0

for p in range(9,1001):
  nWays = 0
  for c in range(p/3,p/2):
    for a in range(1,c/2):
      b2 = c*c-a*a
      b = p-c-a
      if b<0:
        continue
      if a*a+b*b==c*c:
        nWays+=1
  if nWays>most:
    most=nWays
    per=p

end = time.time()
print per
print 'time elapsed: ' + str(end-start)
