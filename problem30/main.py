import time
start = time.time()
sum = 0
for i in range(2,5*9**5):
  word = str(i)
  s = 0
  for j in range(0,len(word)):
    n = int(word[j])
    s+=n**5
  if i == s:
    sum+=i
end = time.time()
print sum
print 'time elapsed: ' + str(end-start)
