"""
Write the solutions for the following quizzes by using functional programming:
"""
from functools import reduce
import math


# 1
print("Ex 1:")
'''Sum all the natural numbers below one thousand that are multiples of 3 or 5.'''
print( 
   sum([ x for x in range(1000) if x % 3 == 0 or x % 5 == 0])
)

# 2
def divisible_by_1_to(n):
   '''Calculate the smallest number divisible by each of the numbers 1 to n (included).'''
   def gcd(a, b):
      '''Calculates the greatest common divisor of two numbers (Euclid's)'''
      return (not b and a) or gcd(b, a-b*(a//b))

   def lcm(a, b): 
      ''' Calculates the least common multiple of two numbers '''
      return (a*b) // gcd(a,b)

   acc = 2
   for i in range(2, n):
      acc = lcm(i, acc)

   return acc  
print("Ex 2:")
print(divisible_by_1_to(20))

# 3
def sum_of_figures(number):
   '''Calculate the sum of the figures of number '''
   return reduce(lambda s, c: int(s) + int(c), str(number))

print("Ex 3:")
print(sum_of_figures(2 ** 1000))
print(sum_of_figures(2 ** 15))

# 4 - using recursion won't work with such depth calculation, since tail recursion
# is not optimized
def first_fib_term_with_n_figures(n):
   '''Calculate the first term in the Fibonacci sequence to contain 1000 digits.'''

   def aux(a, b):
      return (len(str(b)) >= n and b) or aux(b, a+b)

   return aux(1, 1)

print("Ex 4:")
print(first_fib_term_with_n_figures(20))   

# import sys
#sys.setrecursionlimit(1500)
# ERROR: MAXIMUM RECURSION DEPTH print(first_fib_term_with_n_figures(1000))   

def first_fib_term_with_n_figures2(n):
   '''Calculate the first term in the Fibonacci sequence to contain 1000 digits using generators.'''

   def make_fibs(limit = 10000):
      a = 0
      b = 1
      while limit == None or b < limit:
         yield b
         a, b = b, a+b

   fibogen = make_fibs(None)
   for fibnum in fibogen:
      if ( len(str(fibnum)) >= n ):
         return fibnum

print("Ex 4 with generators:")
print(first_fib_term_with_n_figures2(1000))  