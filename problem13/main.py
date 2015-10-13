import numpy as np
import time
start = time.time()

data = np.loadtxt('data.txt')
sum = 0;

for i in range(0,100):
  sum = sum+data[i]
print sum

#code
end = time.time()
print 'time elapsed: ' + str(end-start)
