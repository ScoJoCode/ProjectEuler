import time
start = time.time()

def isPal(a):
  for i in range(0,len(a)/2):
    if not (a[i]==a[len(a)-1-i]):
      return False
  return True

sum=0
for i in range(1,1000000):
  if not isPal(str(i)):
    continue
  b = ''
  n=i
  j=2
  while n>0:
    if n%j>0:
      b='1'+b
      n = n-j/2
    else:
      b='0'+b
    j=j*2
  if not isPal(b):
    continue
  sum+=i

end = time.time()
print sum
print 'time elapsed: ' + str(end-start)
