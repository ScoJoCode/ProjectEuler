import time
import math as m
start = time.time()

sum=0
for i in range(1,1000):
  prod = 1
  for j in range(1,i+1):
    prod*=i
    prod=prod%10e11
  sum+=prod
  sum=sum%10e11

end = time.time()
print sum
print 'time elapsed: ' + str(end-start)
