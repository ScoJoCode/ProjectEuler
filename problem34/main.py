import time
import math
start = time.time()

sum = 0
for i in range(3,2540160):
  s = 0
  word = str(i)
  for j in range(0,len(word)):
    s+=math.factorial(int(word[j]))
  if s==i:
    sum+=i
    print i
end = time.time()
print sum
print 'time elapsed: ' + str(end-start)
