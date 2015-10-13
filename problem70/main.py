import time
from tools import *

def tot(n,ps,min):
  prod = 1.
  dum = n
  for e in ps:
    if e>dum:
      break
    if dum%e==0:
      prod*= (1-1./e)
      if 1./prod>min:
        return 1 #just return a small number
      while dum%e==0:
        dum=dum/e
  return int(round(n*prod))

start = time.time()

up = 10**7

primes = getPrimes(m.sqrt(up)*2) #the factors of the number should not be *much* higher than the sqrt of the limit

min = 2.
num=2

#just check multiples of two primes; could make a lot faster by narrowing the range of primes checked to be near sqrt(10**7)
for i in range(1,len(primes)):
  if primes[i]*primes[i]>up:
    break
  for j in range(i,len(primes)):
    n = primes[i]*primes[j]
    if n>up:
      break
    t = tot(n,primes,min)
    r=1.*n/t
    if r>min:
      continue
    if isPerm(t,n):
      min=r
      num=n

end = time.time()
print num
print tot(num,primes,9.)
print 'time elapsed: ' + str(end-start)
