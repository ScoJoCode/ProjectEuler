import numpy as np
import time
start = time.time()

data = np.loadtxt('data.txt')
prod = 1

#horizontal
for i in range(0,16):
  for j in range(0,20):
    prodHor = 1
    for k in range(0,4):
      prodHor=prodHor*data[i+k][j]
    if prodHor>prod:
      prod=prodHor

#hvertical
for i in range(0,16):
  for j in range(0,20):
    prodVert = 1
    for k in range(0,4):
      prodVert=prodVert*data[j][i+k]
    if prodVert>prod:
      prod=prodVert

#diag down
for i in range(0,16):
  for j in range(0,16):
    prodDiag = 1
    for k in range(0,4):
      prodDiag = prodDiag*data[i+k][j+k]
    if prodDiag>prod:
      prod = prodDiag

#diag up
for i in range(0,16):
  for j in range(4,20):
    prodDiag = 1
    for k in range(0,4):
      prodDiag = prodDiag*data[i+k][j-k]
    if prodDiag>prod:
      prod = prodDiag
print prod

end = time.time()
print 'time elapsed: ' + str(end-start)
