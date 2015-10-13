import time
start = time.time()

side = 20

prod=1

for i in range(1,side+1):
  prod=prod*(side+i)/i

end = time.time()
print prod
print 'time elapsed: ' + str(end-start)
