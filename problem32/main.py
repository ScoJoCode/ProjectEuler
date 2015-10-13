import time
start = time.time()

def isPandigital(a,b,c):
  word=str(a)+str(b)+str(c)
  if not (len(word)==9):
    return False
  for i in range(1,len(word)+1):
    if not (str(i) in word):
      return False
  return True

pans = []

for i in range(1,10000):
  for j in range(1,1000):
    num = i*j
    if isPandigital(i,j,num):
      if not (num in pans):
        pans.append(num)

ans = 0
for num in pans:
  ans+=num

end = time.time()
print ans
print pans
print 'time elapsed: ' + str(end-start)
