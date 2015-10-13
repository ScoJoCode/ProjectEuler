import time
import math as m
start = time.time()

def getPer(n):
  t = m.sqrt(n)
  if pow(int(t),2)==n:
    return 0
  F = int(t)
  botF=n-pow(F,2)
  topF=F
  bot = botF
  top = topF
  next = F
  
  i = 0
  while True:
    last = next
    next = int((m.sqrt(n)+top)/bot)
    top = next*bot-top
    bot = (n-pow(top,2))/bot
    i+=1
    if bot == botF and top == topF:
      break
  return i



nP=0
for i in range(1,10001):
  p=getPer(i)
  if p%2==1:
    nP+=1

end = time.time()
print nP
print 'time elapsed: ' + str(end-start)
