import math
import time

start = time.time()

primes=[]

for i in range (2,50000):
  i+=1
  for e in primes:
    if i%e==0:
      break
    if math.sqrt(i)<e:
      primes.append(i)
      break
  else:
    primes.append(i)

nPrimes = 0
prod = 0

isPrime = [0]*2000000
for i in primes:
  isPrime[i]=1

print 'calculated primes'

for a in range(-999,1000):
  if not(isPrime[abs(a)]) and (abs(a) != 1):
    continue
  for b in range(-999,1000):
    i = 0
    if not(isPrime[abs(b)]) and (abs(b) != 1):
      continue
    while True:
      num = i*i+b*i+a
      if num>2000000:
        print 'need more primes'
        break
      if not(isPrime[num]):
        if i > nPrimes:
          nPrimes=i
          prod = a*b
        break
      i+=1
    #print 'a b i ' + str(a) + ' ' + str(b) + ' ' + str(i)
     


end = time.time()
print prod
print 'time elapsed: ' + str(end-start)
