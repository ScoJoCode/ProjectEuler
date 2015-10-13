import time
start = time.time()

nTimes=0

n=1
d=1
for i in range(1,1000):
  dTemp = d
  d=n+d
  n=dTemp+d
  if len(str(n))>len(str(d)):
    nTimes+=1


end = time.time()
print nTimes
print 'time elapsed: ' + str(end-start)
