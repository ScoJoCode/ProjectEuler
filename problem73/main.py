import time
from tools import *

def isReducible(a,b,ps):
  #are a and b relatively prime?
  for e in ps:
    if a<e:
      return False
    if a%e==0:
      if b%e==0:
        return True
      while a%e==0:
        a=a/e
  return False

start = time.time()


#this method words but takes 180s. Maybe it could work under a min with some optimization
#ps = getPrimes(12000)

#ans=0
#for i in range(2,12001):
#  down = i/3+1
#  up = int((i-.00000001)/2)
#  for j in range(down,up+1):
#    if not isReducible(j,i,ps):
#      ans+=1
      #print ' '
      #Eprint j
      #print i

#farey sequences:

#initialize
x1=1
y1=3
x2=4000
y2=11999
#x2=3
#y2=8
xEnd=1
yEnd=2
lim=12000
#lim=8


ans=0

while not(x2==1) and not(y2==2):
  ans+=1
  k = (lim+y1)/y2
  x3=k*x2-x1
  y3=k*y2-y1
  #print str(x1) + '/' + str(y1)
  #print str(x2) + '/' + str(y2)
  #print str(x3) + '/' + str(y3)
  #print k
  #print ' '
  x1=x2
  y1=y2
  x2=x3
  y2=y3


#there are some facter algorithms that run in nlog(n) time..

end = time.time()
print ans
print 'time elapsed: ' + str(end-start)
