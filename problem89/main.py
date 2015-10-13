import time
import math as m
start = time.time()

nums = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

#returns the minimum length for a roman numeral sequence of a given value
def getMin(v): 
  n=v/1000
  v = v%1000
  for i in range(2,-1,-1):
    if v/(9*pow(10,i))==1:
      n+=2
      v = v%(9*pow(10,i))
    if v/(5*pow(10,i))==1:
      n+=1
      v=v%(5*pow(10,i))
    if v/(4*pow(10,i))==1:
      n+=2
      v=v%(4*pow(10,i))
    n+=v/pow(10,i)
    v=v%pow(10,i)
  return n

#returns the value of a roman numeral string
def getVal(s):
  v=0
  for i in range(0,len(s)):
    val = nums[s[i]]
    if i+1<len(s):
      if nums[s[i+1]]>val:
        v-=val
      else:
        v+=val
    else:
      v+=val
  return v  

sum=0
f = open('roman.txt')
for l in f:
  word =l.split()[0]
  val = getVal(word)
  sum+= len(word)-getMin(val)

end = time.time()
print sum
print 'time elapsed: ' + str(end-start)
