import time
from tools import *

start = time.time()

up = 1000000
#up = 100000
#up = 8
#primes = getPrimes(up)

#ans=1
#x1=1
#y1=up
#x2=1
#y2=up-1
#xEnd=1
#EyEnd=2

factors=[[]for x in [[]]*(up+1)]#can store factors and then 
#eg factors[2]=[2]
#   factors[3]=[3]
#   factors[4]=[2]
#   factors[6]=[2,3]

primes=[2]
factors[2]=[2]
ans=1
i=3
while i<=up:
  num=i
  tot=num
  isPrime=True
  for e in primes:
    if num%e==0:
      isPrime=False
      tot*=(1-1./e)
      num=num/e
      factors[i].append(e)
      for f in factors[num]:
        if f==e:
          continue
        factors[i].append(f)
        tot*=(1-1./f)
      break
    if m.sqrt(i)<e and isPrime:
      tot*=(1-1./i)
      primes.append(i)
      factors[i].append(i)
      break
  ans+=tot
  i+=1

#while not(x2==xEnd and y2==yEnd):
#  ans+=1
#  k=(up+y1)/y2
#  x3=k*x2-x1
#  y3=k*y2-y1
#  x1=x2
#  y1=y2
#  x2=x3
#  y2=y3
#ans=ans*2+1

#last = 1
#for e in primes:
#  ans+=(e-1)
#  for f in range(last+1,e):
#    if f>=up:
#      break
#    ps=factor(f,primes)
#    ans+=totient(f,ps)
#  last = e
#for f in range(last+1,up):
#  ps=factor(f,primes)
#  ans+=totient(f,ps)

#for i in range(2,up):
#  ps = factor(i,primes)
#  ans+=totient(i,ps)





end = time.time()
print ans
print 'time elapsed: ' + str(end-start)
