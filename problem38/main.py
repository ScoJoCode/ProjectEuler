import time
start = time.time()

def isPandigital(word):
  if not (len(word)==9):
    return False
  for i in range(1,len(word)+1):
    if not (str(i) in word):
      return False
  return True

big = 0

for i in range(1,10000):
  word = ''
  for j in range(1,9):
    num = i*j
    word+=str(num)
    if len(word)==9:
      if isPandigital(word):
        if int(word)>big:
          big = int(word)
    elif len(word)>9:
      continue


end = time.time()
print big
print 'time elapsed: ' + str(end-start)
