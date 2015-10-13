import time
import math as m
start = time.time()

def getValue(a):
  w = str(a)
  s=0
  for i in range(0,len(w)):
    s+=m.pow(len(w),int(str(a)[i]))
  return s

i = 10
yay = False
while yay is False:
  if len(str(i*6))>len(str(i)):
    i+=1
    continue
  
  v = getValue(i)
  yay = True
  for j in range(2,7):
    ix = i*j
    if not v==getValue(ix):
      yay = False
      i+=1
      break

end = time.time()
print i
print 'time elapsed: ' + str(end-start)

