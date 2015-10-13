import time
import math as m
start = time.time()

def isPrime(n):
  for i in range(2,int(m.sqrt(n))+1):
    if n%i==0:
      return False
  return True

#primes = [2]
#j=3
#while j < 1000000:
#  for e in primes:
#    if j%e==0:
#      break
#    if m.sqrt(j)<e:
#      primes.append(j)
#      break
#  j+=1

nDiag=1
nPrime=0
i=3
while True:
  nDiag+=4
  n1=i*i
  n2=i*i-(i-1)
  n3=i*i-2*(i-1)
  n4=i*i-3*(i-1)
  #if n2 in primes:
  #  nPrime+=1
  #if n3 in primes:
  #  nPrime+=1
  #if n4 in primes:
  #  nPrime+=1
  #if 1.0*nPrime/nDiag<.1:
  #  break
  #i+=2
  if isPrime(n2):
    nPrime+=1
  if isPrime(n3):
    nPrime+=1
  if isPrime(n4):
    nPrime+=1
  if 1.0*nPrime/nDiag<.1:
    break
  i+=2



end = time.time()
print i
print 'time elapsed: ' + str(end-start)
