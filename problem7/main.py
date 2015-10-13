def isPrime(num):
  if num<2:
    return False
  for i in range(2,num):
    if num%i==0:
      return False
  return True

iPrime = 1
i=1
while iPrime <10002:
  i+=1
  if isPrime(i):
    iPrime+=1
    print 'i: ' + str(i)
    print 'iPrime: ' + str(iPrime)
print i
