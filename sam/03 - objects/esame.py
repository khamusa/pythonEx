from functools import *
from math import *
def myfact(n):
   fact = 1
   for i in range(1,n+1):
      fact *= i
      if i%2 !=0: yield fact
def mysin(x,n):
   g=myfact(n)
   return sum([(x**i)/next(g) for i in range(1, n//2+1)])

if __name__ == "__main__":
   for x in range(30,360,90):
      for i in range(1,1000):
         print("*** The error with {0:4} addends in {1:3} is {2}".format(i, x, sin(x)-mysin(x,i)))
   for i in range(361):
      print("### sin({0:3}) :- {1:15} mysin({0:3}) :- {2:15}".format(i, sin(i), mysin(i,10000)))
