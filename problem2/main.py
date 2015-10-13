sum = 0

i = 1
k = 0

while i < 4e6:
  if i%2==0:
    sum+=i
  l=i
  i+=k
  k=l


print sum
