import time
start = time.time()
#I actually did this one by hand, but just going through the numbers and putting them in the sequence when you know something goes between some other ones

#One way to code it. If you assume no repeating numbers, you can find the number (7) which does not follow any other numbers. Then find the next etc. This is probably the simplest way

#Could assign the numbers values based on where they appear
#eg: 3:1,1:2,9:3    6:1,8:2,0:3
#as you go through more numbres you can move the numbers ie 8:2.5, but then what does 9 get? this might be complicated
#This gets even more complicated if you don't assume no repeating numbers, but maybe there is a way to modify it for such a case
end = time.time()
print '73162890'
print 'time elapsed: ' + str(end-start)
