from math import factorial,pi
import math
from decimal import * 
#Calculate sin using first n terms of the Taylor series...
#input expected in radians
def sin_rad(x,n):
    sum = 0.0;

    def gen_sins(mx):
       for n in range(mx):
           a1 = Decimal((-1)**n)
           a2 = Decimal(factorial(2*n+1))
           a3 = Decimal(x**(2*n+1))
           #print( "{} / ({}) * x^{}".format(a1, a2, 2*n+1) )
           yield (a1 / a2) * a3
 
    return math.fsum(gen_sins(n))
 
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
      print("Precision {:>4}: {} {} = {}".format(precision, math.sin(angle), \
         sin_rad(angle, precision), math.sin(angle) - sin_rad(angle, precision)))

   
   print_result(angle, 10)
   print_result(angle, 50)
   print_result(angle, 1000)

   
print("Took", time.clock() - st)