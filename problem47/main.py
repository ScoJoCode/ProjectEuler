import time
import math
start = time.time()

i=3
num=4
primes = [2]
nums = []
while True:
  isPrime=1
  nPrimes=0
  new = i
  for e in primes:
    if e>new:
      break
    if new%e==0:
      isPrime=0
      nPrimes+=1
      if nPrimes>num:
        break
      while new%e==0:
        new = new/e
  if isPrime:
    primes.append(i)
  if nPrimes==num:
    nCon+=1
    nums.append(i)
  else:
    nCon=0
    nums = []
  if nCon==num:
    break
  i+=1

end = time.time()
print nums[0]
print 'time elapsed: ' + str(end-start)

#there are no 9 or 8 digit pandigital primes (they are all divisible by 3: sum(1:8)=27)
