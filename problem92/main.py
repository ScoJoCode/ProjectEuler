import time
start = time.time()

#really desperate to save time; converting to int apparently expensive
sqs={'0':0,'1':1,'2':4,'3':9,'4':16,'5':25,'6':36,'7':49,'8':64,'9':81}
def square(n):
  w = str(n)
  sq = 0
  for i in range(0,len(w)):
    sq+=sqs[w[i]]
  return sq


dict = [0]*600
dict[1-1]=1
dict[89-1]=89
sum=0
for i in range(1,10000000):
  nums=[]
  num = i
  if num>567:
    num=square(num)
    if dict[num-1]==89:
      sum+=1
      continue

  end=0
  while True:
    if dict[num-1]==89:
      end=89
      break
    elif dict[num-1]==1:
      end=1
      break
    nums.append(num)
    num=square(num)
  for e in nums:
    if end==89:
      dict[e-1]=89
    else:
      dict[e-1]=1
  if end==89:
    sum+=1

end = time.time()
print sum
print 'time elapsed: ' + str(end-start)
