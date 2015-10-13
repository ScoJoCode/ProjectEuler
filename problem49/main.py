import time
import math as m
start = time.time()

primes = [2]
i=3
while i < 10000:
  for e in primes:
    if i%e==0:
      break
    if m.sqrt(i)<e:
      primes.append(i)
      break
  i+=1
ans = ''
for i in range(1110,10000-2*3300):
  i2 = i+3330
  i3 = i2+3330
  a = 0
  a2 = 0
  a3 = 0
  if i==1487:
    continue
  for j in range(0,4):
    a+=m.pow(4,int(str(i)[j]))
    a2+=m.pow(4,int(str(i2)[j]))
    a3+=m.pow(4,int(str(i3)[j]))
  if not (a==a2 and a2==a3):
    continue
  if not i in primes:
    continue
  if not i2 in primes:
    continue
  if not i3 in primes:
    continue

  ans= ans+str(i)+str(i2)+str(i3)

end = time.time()
print ans
print 'time elapsed: ' + str(end-start)

