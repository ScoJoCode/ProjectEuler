
def isPrime(num):
  for i in range(2,num):
    if num%i==0:
      return False
  return True


num = 1
up = 20
i = 2

for i in range(2,up+1):
  dummyNum = num
  dummyI = i
  j = 2
  while j <= dummyI:
    if dummyI%j==0:
      dummyI=dummyI/j
      if dummyNum%j==0:
        dummyNum = dummyNum/j
      else:
        num=num*j
    else:
      j+=1
print num
