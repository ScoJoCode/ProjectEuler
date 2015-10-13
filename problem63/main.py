import time
import math as m
start = time.time()

n=0
for i in range(1,10):
  p=1
  while True:
    if len(str(pow(i,p)))==p:
      n+=1
      p+=1
    else:
      break

end = time.time()
print n
print 'time elapsed: ' + str(end-start)
