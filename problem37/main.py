import math
import time
def trunL(word):
  new = ''
  for i in range(1,len(word)):
    new+=word[i]
  return new

def trunR(word):
  new = ''
  for i in range(0,len(word)-1):
    new+=word[i]
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

sum = 0

for p in primes:
  if p<10:
    continue
  wordR = str(p)
  wordL = str(p)
  isTruncatable = 1
  for i in range(1,len(wordR)):
    wordR=trunR(wordR)
    numR = int(wordR)
    wordL=trunL(wordL)
    numL = int(wordL)
    if not isPrime[numR]:
      isTruncatable=0
      break
    if not isPrime[numL]:
      isTruncatable=0
      break

  if isTruncatable:
    print p
    sum+=p


end = time.time()
print sum
print 'time elapsed: ' + str(end-start)
