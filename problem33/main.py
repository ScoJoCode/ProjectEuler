import time
start = time.time()


proda = 1
prodb = 1


for i in range(11,99):
  for j in range(10,i):
    f = 1.0*j/i

    wordI = str(i)
    wordJ = str(j)

    if wordI[1]=='0' and wordJ[1]=='0':
      continue

    for k in range(0,2):
      for l in range(0,2):
        if wordI[1+-1*k]==wordJ[1+-1*l]:
          if int(wordI[k])>0:
            newF=1.0*int(wordJ[l])/int(wordI[k])
            if abs(newF-f)<.0001:
              proda*=int(wordJ[l])
              prodb*=int(wordI[k])

for i in range(2,800):
  while proda%i==0 and prodb%i==0:
    proda=proda/i
    prodb=prodb/i


end = time.time()
print prodb
print 'time elapsed: ' + str(end-start)
