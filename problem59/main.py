import time
import numpy as np
start = time.time()

data = np.loadtxt('cipher.txt',delimiter=',')

key = [ord('a'),ord('a'),ord('a')]
numW = [0]*26
numW = [numW[:] for e in [[0]*26]*3]
s = ''
for k in range(0,26):
  j=0
  for i in range(0,len(data)):
    char = chr((key[j]+k) ^ int(data[i]))
    if char =='<' or char == '+' or char =='='or char =='>' or char=='-' or char=='@' or char=='*' or char=='}' or char=='{' or char=='|' or char=='[' or char==']':
      numW[j][k]+=1
    
    j+=1
    if j==3:
      j=0

key = [ord('a')+numW[0].index(min(numW[0])),ord('a')+numW[1].index(min(numW[1])),ord('a')+numW[2].index(min(numW[2]))]
j=0
sum = 0
for i in range(0,len(data)):
  ascii = key[j] ^ int(data[i])
  sum+=ascii
  s+=chr(ascii)
  j+=1
  if j==3:
    j=0

end = time.time()
print s
print sum
print 'time elapsed: ' + str(end-start)
