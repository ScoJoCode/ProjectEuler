import time
import math as m
from tools import *
start = time.time()



lim = 1.0*15499/94744
#lim = 4.0/10

#some primes
primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59]
ans=1
ps = []

#largest jumps in resilience seem to come by multiplying the number by new primes
#as a first attempt, assume the limit breaks at one of these numbers
for e in primes:
  ans*=e
  ps.append(e)
  res = getRes(ans,ps)
  print ps[len(ps)-1]
  if res<lim:
    break
#getting to 29 breaks the limit, so then I checked prod(primes[1 to 23])*(2, 2*2, 3)
#could write up some code to do this automatically, but it's not worth
# turns out my little tool for calculating the number of reducible fractions could be replaced by Euler's totient function: prod(1-1/p)*n where p are the prime factors of n


end = time.time()
print ans

print 'time elapsed: ' + str(end-start)
