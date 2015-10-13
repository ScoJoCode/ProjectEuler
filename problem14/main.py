import time
start = time.time()

most = 0
start = 0

for i in range(1,1000000):
  num = i
  count = 0
  while num!=1:
    count+=1
    if num%2==0:
      num = num/2
    else:
      num=num*3+1
  if count>most:
    most = count
    start = i

print start

end = time.time()
print 'time elapsed: ' + str(end-start)
