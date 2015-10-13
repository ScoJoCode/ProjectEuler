import time
import math
start = time.time()

def isAbundant(num):
  sum = 0
  for i in range(2,int(math.sqrt(num))+1):
    if num%i==0:
      sum+=i
      if i!=num/i:
        sum+=num/i
  sum+=1
  if sum>num:
    return True
  return False

aNums = []
aSums = [0]*28123

for i in range(1,28123):
  if isAbundant(i):
    aNums.append(i)

for i in range(0,len(aNums)):
  for j in range(i,len(aNums)):
    if aNums[i]+aNums[j] < 28123:
      aSums[aNums[i]+aNums[j]]=1

sum = 0
for i in range(0,len(aSums)):
  if aSums[i]==0:
    sum+=i

end = time.time()
print sum
print 'time elapsed: ' + str(end-start)
