import time
start = time.time()

i = 1
d=0
prod = 1
while d<100000:
  word = str(i)
  for j in range(0,len(word)):
    d+=1
    if d==1 or d==10 or d==100 or d==1000 or d==10000 or d==100000:
      prod=prod*int(word[j])
  i+=1

end = time.time()
print prod
print 'time elapsed: ' + str(end-start)
