import time
import math as m
start = time.time()

nWays=0

for n in range(1,101):
  for r in range(1,n+1):
    ways = m.factorial(n)/(m.factorial(r)*m.factorial(n-r))
    if ways>10e5:
      nWays+=1

end = time.time()
print nWays
print 'time elapsed: ' + str(end-start)
