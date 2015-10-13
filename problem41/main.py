import time
import math
start = time.time()

def isPandigital(word):
  for i in range(1,len(word)+1):
    if not (str(i) in word):
      return False
  return True

big = 0

primes = [2]
for i in range (3,2767):
  for e in primes:
    if i%e==0:
      break
    if math.sqrt(i)<e:
      primes.append(i)
      break
    else:
      primes.append(i)

for i in range(7654321,1,-1):
  if not isPandigital(str(i)):
    continue
  isPrime = True
  for e in primes:
    if math.sqrt(i)<e:
      break
    if i%e==0:
      isPrime=False
      break
  if isPrime:
    big = i
    break

end = time.time()
print big
print 'time elapsed: ' + str(end-start)

#there are no 9 or 8 digit pandigital primes (they are all divisible by 3: sum(1:8)=27)
