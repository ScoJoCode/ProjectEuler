import time
start = time.time()

#I actually did this by hand - this code illustrates how I did it; might be interesting to check to see if this works for all n

primes = [2,3,5,7,11,13,17,19,23] 

prod = 1
for e in primes:
  if prod*e>1000000:
    break
  prod*=e

end = time.time()
print prod
print 'time elapsed: ' + str(end-start)
