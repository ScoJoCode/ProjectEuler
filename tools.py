import math as m
from tree import *

def isSquare(n):
  sq=m.sqrt(n)
  return sq==int(sq)

#add isTriang, isPenta etc

#returns the prime factors of n - can make more efficient?
def factor(n,primes):
  ps = []
  for e in primes:
    if n%e==0:
      ps.append(e)
    while n%e==0:
      n=n/e
    if e>n:
      break
  return ps

#def factor(n):
#  primes = getPrimes(n/2)
#  return factor(n,primes)

#returns all the primes up to n
def getPrimes(n):
  if n<2:
    return []
  primes=[2]
  i=3
  while i<n+1:
    for e in primes:
      if i%e==0:
        break
      if m.sqrt(i)<e:
        primes.append(i)
        break
    i+=1
  return primes

#is prime
#def isPrime(n,ps):

#is prime
#def isPrime(n):

#euler's totient function, calculates the number of primes relative to n given the prime factors ps
def _totient(n,ps):
  prod = n
  for e in ps:
    prod*= (1-1./e)
  return int(round(prod))

#euler's totient function without ps argument
def totient(n,ps=None):
  if ps==None:
    ps = factor(n)
    return _totient(n,ps)
  else:
    return _totient(n,ps)


#sort an array: should average o(nlog(n))
def sort(a):
  t = Tree()
  for i in range(0,len(a)):
    t.add(a[i])
  return t.getArray()

#determine if permutation without sorting - i think it is o(n)
def isPerm(a,b):
  wa = str(a)
  l = len(wa)
  wb = str(b)
  if not (l == len(wb)):
    return False
  suma = 0
  sumb = 0
  for i in range(0,l):
    suma+=l**int(wa[i])
    sumb+=l**int(wb[i])
  if sumb==suma:
    return True
  return False
