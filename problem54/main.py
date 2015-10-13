import time
from tools import *

#poker hands - boring, this one was pretty annoying - I did a pretty messy job but i don't care to make it nicer
start = time.time()

wins=0
for line in open('poker.txt'):
  words = line.strip().split()
  nums1=[]
  suits1=[]
  nums2=[]
  suits2=[]
  for w in words[0:5]:
    n1 = 0
    if w[0]=='J':
      n1=11
    elif w[0]=='Q':
      n1=12
    elif w[0]=='K':
      n1=13
    elif w[0]=='A':
      n1=14
    elif w[0]=='T':
      n1=10
    else:
      n1=int(w[0])
    suits1.append(w[1])
    if len(nums1)==0:
      nums1.append(n1)
    else:
      for i in range(0,len(nums1)):
        if nums1[i]>n1:
          nums1.insert(i,n1)
          break
        if i==len(nums1)-1:
          nums1.append(n1)
  for w in words[5:10]:
    if w[0]=='J':
      n2=11
    elif w[0]=='Q':
      n2=12
    elif w[0]=='K':
      n2=13
    elif w[0]=='A':
      n2=14
    elif w[0]=='T':
      n2=10
    else:
      n2=int(w[0])
    suits2.append(w[1])
    if len(nums2)==0:
      nums2.append(n2)
    else:
      for i in range(0,len(nums2)):
        if nums2[i]>n2:
          nums2.insert(i,n2)
          break
        if i==len(nums2)-1:
          nums2.append(n2)
  points1=0
  points2=0
  isFlush1 = True
  isFlush2 = True
  isStraight1 =True
  isStraight2 = True
  pair1=[0]*2
  pair1Val=[0]*2
  p1=0
  pair2=[0]*2
  pair2Val=[0]*2
  p2=0
  for i in range(1,5):
    if not nums1[i]==nums1[0]+i:
      isStraight1=False
    if not nums2[i]==nums2[0]+i:
      isStraight2=False
    if not suits1[i]==suits1[0]:
      isFlush1=False
    if not suits2[i]==suits2[0]:
      isFlush2=False
    if nums1[i]==nums1[i-1]:
      pair1[p1]+=1
      pair1Val[p1]=nums1[i]
    else:
      if pair1[0]>0:
        p1=1
    if nums2[i]==nums2[i-1]:
      pair2[p2]+=1
      pair2Val[p2]=nums2[i]
    else:
      if pair2[0]>0:
        p2=1

  comp1 = [0]*2
  comp2 = [0]*2
  if pair1[0]==1:
    if pair1[1]==1:
      points1=2
      comp1[0]=max(pair1Val[0],pair1Val[1])
      comp1[1]=min(pair1Val[0],pair1Val[1])
    elif pair1[1]==2:
      points1=6
      comp1[0]=pair1Val[1]
      comp1[1]=pair1Val[0]
    else:
      points1=1
      comp1[0]=pair1Val[0]
  elif pair1[0]==2:
    comp1[0]=pair1Val[0]
    comp1[1]=pair1Val[1]
    if pair1[1]==0:
      points1=3
    else:
      points1=6
  elif pair1[0]==3:
    comp1[0]=pair1Val[0]
    points1=7
  if pair2[0]==1:
    if pair2[1]==1:
      points2=2
      comp2[0]=max(pair2Val[0],pair2Val[1])
      comp2[1]=min(pair2Val[0],pair2Val[1])
    elif pair2[1]==2:
      points2=6
      comp2[0]=pair2Val[1]
      comp2[1]=pair2Val[0]
    else:
      points2=1
      comp2[0]=pair2Val[0]
  elif pair2[0]==2:
    comp2[0]=pair2Val[0]
    comp2[1]=pair2Val[1]
    if pair2[1]==0:
      points2=3
    else:
      points2=6
  elif pair2[0]==3:
    comp2[0]=pair2Val[0]
    points2=7

  if isStraight1:
    if isFlush1:
      points1 = 8
    else:
      points1 = 4
  elif isFlush1:
    points1=5
  if isStraight2:
    if isFlush2:
      points2 = 8
    else:
      points2 = 4
  elif isFlush2:
    points2=5

  if points1>points2:
    wins+=1
    continue
  elif points1<points2:
    continue

  over = False
  for i in range(0,len(comp1)):
    if comp1[i]>comp2[i]:
      wins+=1
      over=True
      break
    elif comp1[i]<comp2[i]:
      over=True
      break
  if over:
    continue

  for i in range(4,-1,-1):
    if nums1[i]==nums2[i]:
      continue
    if nums1[i]>nums2[i]:
      wins+=1
      break
    else:
      break

end = time.time()
print wins
print 'time elapsed: ' + str(end-start)
