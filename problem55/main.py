import time
start = time.time()

def pal(word):
  drow = ''
  for k in range(0,len(word)):
    drow+=word[len(word)-k-1]
  return drow


nNums = 0
for i in range(1,10000):
  isL = True
  num = i
  num = int(pal(str(num)))+num
  for j in range(1,50):
    mun = int(pal(str(num)))
    if mun==num:
      isL=False
      break
    num=num+mun
  if isL:
    nNums+=1
end = time.time()
print nNums
print 'time elapsed: ' + str(end-start)
