import time
start = time.time()

num = 2**1000

sum = 0
word = str(num)
for i in range(0,len(word)):
  sum+=int(word[i])

end = time.time()
print sum
print 'time elapsed: ' + str(end-start)
