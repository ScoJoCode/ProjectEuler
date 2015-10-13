import time
start = time.time()

side = 18

def move(i,j):
  sum = 0
  #if i==side-2:
  #  return (side-j+1)*(side-j+2)/2
  #if i==side-3:
  #  return (side-j+1)*(side-j+2)*(side-j+3)/(2*3)
  if i==side-4:
    return (side-j+1)*(side-j+2)*(side-j+3)*(side-j+4)/(2*3*4)
  if i<side and i==j:
    sum = sum+2*move(i+1,j)
    return sum
  if i<side:
    sum = sum+move(i+1,j)
  if j<side:
    sum = sum+move(i,j+1)
  return sum

answer = move(0,0)

end = time.time()
print answer
print 'time elapsed: ' + str(end-start)
