import time
import math as m
start = time.time()

primes = [2]
i=3
while i < 1000000:
  for e in primes:
    if i%e==0:
      break
    if m.sqrt(i)<e:
      primes.append(i)
      break
  i+=1

sum = 0
largest=0

for f in primes:
  sum = 0
  if f > 100:
    break
  for e in primes:
    if e < f:
      continue
    sum+=e
    if sum > 1000000:
      continue
    if sum > largest:
      if sum in primes:
        largest=sum

end = time.time()
print largest
print 'time elapsed: ' + str(end-start)

