import time
import numpy as np
from tree import *

start = time.time()

def letterScore(a):
  return  ord(a)-ord('A')+1

f = open('data.txt','r')

words = (f.readline()).replace('"','').split(',')

tree = Tree()

for i in range(0,len(words)):
  tree.add(words[i])

a = []
tree.makeArray(a)

sum=0
for i in range(0,len(a)):
  word = a[i]
  sumWord=0
  for j in range(0,len(word)):
    sumWord+=letterScore(word[j])
  sum+=(i+1)*sumWord

end = time.time()
print sum
print 'time elapsed: ' + str(end-start)
