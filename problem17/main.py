import time
start = time.time()

def getCount(n):
  if n==1 or n==2 or n==6 or n==10:
    return 3
  if n==3 or n==7 or n==8 or n==40 or n==50 or n==60:
    return 5
  if n==4 or n==5 or n==9:
    return 4
  if n==11 or n==12 or n==20 or n==30 or n==80 or n==90:
    return 6
  if n==13 or n==14 or n==18 or n==19:
    return 8
  if n==15 or n==16 or n==70:
    return 7
  if n==17:
    return 9
  return 0

sum = 0
for i in range(1,1000):
  num = i
  if num%100!=0:
    if num%100<20:
      sum+=getCount(num%100)
    else:
      sum+=getCount((num-num%10)%100)+getCount((num%10)%100)
    if num>100:
      sum+=3 #for "and"
  if num>=100:
    sum+=getCount(num/100)+7
sum+=11 #for 1000

end = time.time()
print sum
print 'time elapsed: ' + str(end-start)
