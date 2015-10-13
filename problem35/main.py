import math
import time
def permute(word):
  new = word[len(word)-1]
  for i in range(1,len(word)):
    new+=word[i-1]
  return new


start = time.time()

primes=[2]

for i in range (2,1000000):
  i+=1
  for e in primes:
    if i%e==0:
      break
    if math.sqrt(i)<e:
      primes.append(i)
      break
  else:
    primes.append(i)
isPrime = [0]*1000000
for i in primes:
  isPrime[i]=1
nPrimes=0
for p in primes:
  word = str(p)
  isCircular=1
  for i in range(1,len(word)):
    word=permute(word)
    num = int(word)
    if not isPrime[num]:
      isCircular=0
      break

  if isCircular:
    nPrimes+=1


end = time.time()
print nPrimes
print 'time elapsed: ' + str(end-start)
