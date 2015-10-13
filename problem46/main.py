import time
import math as m
start = time.time()

primes = [2]
i=3
while True:
  isComp=False
  for e in primes:
    if i%e==0:
      isComp=True
      break
    if m.sqrt(i)<e:
      primes.append(i)
      break
  if isComp and i%2==1:
    found = False
    for e in primes[0:len(primes)]:
      new = 1.*(i-e)/2
      if m.ceil(m.sqrt(new))==m.floor(m.sqrt(new)):
        found=True
        break
    if not found:
      break
  i+=1


end = time.time()
print i
print 'time elapsed: ' + str(end-start)

#there are no 9 or 8 digit pandigital primes (they are all divisible by 3: sum(1:8)=27)
