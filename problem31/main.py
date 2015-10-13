import time
start = time.time()

coins = [1,2,5,10,20,50,100,200]

def getCs(pence,c):
  sum = 0
  if c==7:
    return 1+pence/200
  for i in range(0,pence+1,coins[c]):
    sum+=getCs(pence-i,c+1)
  return sum

sum = getCs(200,1)
end = time.time()
print sum
print 'time elapsed: ' + str(end-start)
