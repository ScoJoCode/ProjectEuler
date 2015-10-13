import time
import math
start = time.time()



def calcDig(i):
  num = 10
  a = []
  rs = []
  nDig=0
  #print 'calculating for: ' + str(i)
  for j in range(0,i+1):
    re = num%i
    if re is 0:
      return 0
    dig = num/i
    a.append(dig)
    if re in rs:
      nDig=len(rs)-rs.index(re)
      return nDig
    rs.append(re)
    #print str(dig) + ' ' + str(re)
    num=re*10

  return nDig

big = 0
n = 0

for i in range(1,1000):
  nDig = calcDig(i)
  #print nDig
  if nDig>big:
    big = nDig
    n = i


end = time.time()
print n
print 'time elapsed: ' + str(end-start)
