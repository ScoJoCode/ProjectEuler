import time
import math

start = time.time()

i=1
while True:
  tri =0
  for j in range(1,i):
    tri=tri+j
  nDiv=0
  for j in range(1,int(math.sqrt(tri))+1):
    if tri%j==0:
      nDiv+=1
      if tri/j != j:
        nDiv+=1
  if nDiv>500:
    print tri
    break
  i+=1

end = time.time()
print 'time elapsed: ' + str(end-start)
