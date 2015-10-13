import math as m

#slow
def getNDiv(n,primes):
  nDiv=0
  for i in range(2,n):
    for e in primes:
      if i%e==0:
        nDiv+=1
        break
  return nDiv

#faster?
def getRec(n,frac,i,ps):
  if i==len(ps)-1:
    return int((n-1)*frac/ps[i])
  else:
    sum=getRec(n,frac,i+1,ps)
    frac/=ps[i]
    sum+=int((n-1)*frac)+getRec(n,-1*frac,i+1,ps)
    return sum

def getRes(n,primes):
  nDiv = getRec(n,1.0,0,primes)
  return 1.0*(n-1-nDiv)/(n-1)
