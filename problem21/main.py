import time
import math
start = time.time()

def getD(num):
  sum = 0
  for i in range(2,int(math.sqrt(num))+1):
    if num%i==0:
      sum+=i
      if i!=num/i:
        sum+=num/i
  sum+=1
  return sum

dict = {}
sum = 0

for i in range(1,10000):
  d = getD(i)
  dict[i]=d
for i in range(1,10000):
  if dict[i] in dict and dict[dict[i]]==i and dict[i]!=i:
    sum+=i



end = time.time()
print sum
print 'time elapsed: ' + str(end-start)
