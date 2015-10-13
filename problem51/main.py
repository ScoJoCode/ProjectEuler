import time
from tools import *

start = time.time()

fam = 8
ans=0
found=False
ps = getPrimes(10**6)

#need to replace 3 digits; can show this with divisible by 3 rule
#should somehow program this better...
for p in ps:
  if p < 1000:
    continue
  wa = str(p)
  for i in range(0,len(wa)-3):
    if int(wa[i])>10-fam:
      continue
    for j in range(i+1,len(wa)-2):
      if not wa[i]==wa[j]:
        continue
      for k in range(j+1,len(wa)-1):
        if not wa[i]==wa[k]:
          continue
        nPrimes = 1
        for n in range(int(wa[i])+1,10):
          if fam-nPrimes>10-n: 
            break
          newPrime = int(wa[0:i]+str(n)+wa[i+1:j]+str(n)+wa[j+1:k]+str(n)+wa[k+1:len(wa)])
          if newPrime in ps: #slow?
            nPrimes+=1
          if nPrimes==fam:
            found=True
            ans=p
            break
        if found==True:  #not so elegant i know
          break
      if found==True:
        break
    if found==True:
      break
  if found==True:
    break
 


  


end = time.time()
print ans
print 'time elapsed: ' + str(end-start)
