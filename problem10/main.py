import math
import time

start = time.time()

primes=[]

sum = 0

iPrime = 0
i = 1
while i<2000000:
  i+=1
  for e in primes:
    if i%e==0:
      break
    if math.sqrt(i)<e:
      iPrime+=1
      sum+=i
      primes.append(i)
      #print 'i: ' + str(i)
      #print 'iPrime: ' + str(iPrime)
      break
  else:
    iPrime+=1
    sum+=i
    primes.append(i)
    #print 'i: ' + str(i)
    #print 'iPrime: ' + str(iPrime)

print sum
end = time.time()
print 'time elapsed: ' + str(end-start)
