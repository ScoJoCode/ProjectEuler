import time
start = time.time()
sum = 1
for i in range(3,1002,2):
  sum+=i*i+i*i-(i-1)+i*i-2*(i-1)+i*i-3*(i-1)

end = time.time()
print sum
print 'time elapsed: ' + str(end-start)
