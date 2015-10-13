sumOfSq = 0
sum = 0
for i in range(1,101):
  sumOfSq+=i*i
  sum+=i
sqOfSum=sum*sum

print sqOfSum-sumOfSq

