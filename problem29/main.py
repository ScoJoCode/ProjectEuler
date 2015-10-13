import time
start = time.time()

nums = []

dis=0

for a in range(2,101):
  for b in range(2,101):
    new = a**b
    if not new in nums:
      dis+=1
      nums.append(new)

end = time.time()
print dis
print 'time elapsed: ' + str(end-start)
