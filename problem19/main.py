import time
start = time.time()

def isLastDay(day,year,month):
  if day==31 and (month==1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
    return True
  if day==30 and (month ==4 or month == 6 or month == 9 or month == 11):
    return True
  if month == 2 and day==28:
    if year%4!=0 or (year%4==0 and year%100==0 and year%400!=0):
      return True
  if month == 2 and day==29:
    return True
  return False

sum = 0

year = 1900
weekday = 2
monthDay = 1
month = 1

while year<2001:
  if monthDay==1 and weekday==1 and year >1900:
    sum+=1
  #if monthDay>27
  if isLastDay(monthDay,year,month):
    if month==12:
      month = 1
      year+=1
    else:
      month+=1
    monthDay=1
  else:
    monthDay+=1
  if weekday==7:
    weekday=1
  else:
    weekday+=1


end = time.time()
print sum
print 'time elapsed: ' + str(end-start)
