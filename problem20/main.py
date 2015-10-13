import time
start = time.time()

prod = 1
for i in range(1,101):
  prod=prod*i
word = str(prod)

sum=0
for i in range(0,len(word)):
  sum=sum+int(word[i])

end = time.time()
print sum
print 'time elapsed: ' + str(end-start)
