import math
import time
start = time.time()

phi = (1+math.sqrt(5.0))/2

n = (.5*math.log10(5)+999)/math.log10(phi)

end = time.time()
print n
print 'time elapsed: ' + str(end-start)
