
num = 600851475143
factor = 1
i=2

while i<=num:
  if num%i==0:
    num=num/i
    factor=i
  else:
    i+=1

print factor
