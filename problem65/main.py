import time
start = time.time()

#initialize to the 100th terms
num=1
den=1

#do terms 2 through 99
for i in range(99,1,-1):
  new = 1
  if i%3==0:
    new=i/3*2
  num=new*den+num
  temp = num
  num = den
  den = temp

#i==1
num = 2*den+num

sum=0
word=str(num)
for i in range(0,len(word)):
  sum+=int(word[i])

end = time.time()
print sum
print 'time elapsed: ' + str(end-start)
