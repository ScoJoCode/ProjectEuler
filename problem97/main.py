import time
from tools import *

start = time.time()

#28433X2**7830457+1, multiply and cut off the leading digits, repeat
#or - find out what each digit is as a function of powers?

EXPO = 7830457
expo = 34
mult = 28433

ans=1
for i in range(0,EXPO/expo):
  ans=ans*(2**expo)
  ans = ans%(10**10)

ans=ans*(2**(EXPO%expo))*mult+1
ans=ans%(10**10)
end = time.time()
print ans
print 'time elapsed: ' + str(end-start)
