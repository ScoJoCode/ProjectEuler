#this is the same as the coin problem
import time
start = time.time()

up = 100
coins = range(1,up)

def getCs(pence,c):
  sum = 0
  if c==up-1:
    return 1+pence/200
  for i in range(0,pence+1,coins[c]):
    sum+=getCs(pence-i,c+1)
  return sum

sum = getCs(up,1)
end = time.time()
print sum
print 'time elapsed: ' + str(end-start)
