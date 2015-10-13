import time
import math as m
start = time.time()

SUM = 0

for i in range(1,100):
  for j in range(1,100):
    num = pow(i,j)
    word = str(num)
    sum = 0
    for n in range(0,len(word)):
      sum+=int(word[n]) 
    if sum>SUM:
      SUM=sum

end = time.time()
print SUM
print 'time elapsed: ' + str(end-start)
