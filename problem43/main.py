import time
import math as m
start = time.time()

def hasProp(a):
  if not int(a[7:10])%17==0:
    return False
  if not int(a[6:9])%13==0:
    return False
  if not int(a[5:8])%11==0:
    return False
  if not int(a[4:7])%7==0:
    return False
  if not int(a[3:6])%5==0:
    return False
  if not int(a[2:5])%3==0:
    return False
  if not int(a[1:4])%2==0:
    return False
  return True

n = m.factorial(10)
ans = 0

for i in range(0,n):
  pan = ''
  nums = ['0','1','2','3','4','5','6','7','8','9']
  num = i
  skip = False
  for j in range(9,0,-1):
    ind = num/m.factorial(j)
    pan+=nums[ind]
    if j ==6:
      if not int(nums[ind])%2==0:
        skip = True
        break
    nums.remove(nums[ind])
    num = num%m.factorial(j)
    #could start testing for property here to save time...
  if skip:
    continue
  pan+=nums[0]
  if hasProp(pan):
    ans+=int(pan)


end = time.time()
print ans
print 'time elapsed: ' + str(end-start)
