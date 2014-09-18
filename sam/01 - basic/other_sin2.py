from math import factorial,pi
import math, itertools
from decimal import * 

def sinfact():
      fact = 1
      for i in itertools.count(start=1):
        fact *= i
        if i % 2 != 0: 
          yield fact

fct = sinfact()
next(fct)
for i in range(3, 50, 2):
   f = next(fct)
   print(math.factorial(i), f)
   assert math.factorial(i) == f

def gen_sins(x, mx):
 f = sinfact()
 for n in range(0, mx):
     a1 = Decimal((-1)**n)
     a2 = Decimal(next(f))
     a3 = Decimal(x**(2*n+1))
     yield (a1 / a2) * a3

#Calculate sin using first n terms of the Taylor series...
#input expected in radians
def sin_rad(x,n):
    sum = 0.0;    
 
    return math.fsum(gen_sins(x, n))
 
#calculate sin
#input in degrees
def sin(x, n = 10):
    a = x*(pi)/180.0
    return sin_rad(a, n)
 
 
 
import time
getcontext().prec = 200
st = time.clock()
for angle in range(1, 30, 3):
   print("Angle", angle)
   def print_result(angle, precision):
      myres = sin_rad(angle, precision)
      print("Precision {:>4}: {} {} = {}".format(precision, math.sin(angle), \
         myres, math.sin(angle) - myres))

   
   print_result(angle, 10)
   print_result(angle, 50)
   print_result(angle, 1000)

print("Took", time.clock() - st)
   #print_result(angle, 1000)
exit()
from math import *
def myfact(n):
   fact = 1
   for i in range(1,n+1):
      fact *= i
      if i%2 !=0: yield fact
def mysin(x,n):
   g=myfact(n)
   return sum([(x**i)/next(g) for i in range(1, n//2+1)])

   for x in range(30,360,90):
      for i in range(1,1000):
         print("*** The error with {0:4} addends in {1:3} is {2}".format(i, x, sin(x)-mysin(x,i)))
   for i in range(361):
      print("### sin({0:3}) :- {1:15} mysin({0:3}) :- {2:15}".format(i, sin(i), mysin(i,10000)))
