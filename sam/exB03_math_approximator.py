"""
sin(x) can be approximate by the Taylor's series:

x - x^3/3! + x^5/5! ...

Let's write a library to implement sin(x, n) by using the Taylor's series (where n is the level 
of approximation, i.e., 1 only one item, 2 two items, 3 three items and so on).

Let's compare your function with the one implemented in the math module at the growing of the 
approximation level.

Hint. Use a generator for the factorial and a comprehension for the series.
"""
import math, functools, inspect
class MathApproximator:

   def __init__(self, approx = 3):
      self.target_precision = approx
	
   def step_two_factorial(self, index = 1):
      if index not in [1, 2]:
         raise ValueError("You may only initialize the stepping factorial with 1 or 2")

      last_result       = index

      while True:
         yield (index, last_result)
         index          += 2
         last_result    = last_result * (index - 1) * (index)

   # PERCHÉ NON FUNZIONA?
   def sin_lambda_generator(self):
      sign_for_sin             = lambda index: -1 if index % 2 == 0 else 1
      fact_generator           = self.step_two_factorial(1)

      for i in range(1, self.target_precision + 1):
         index, fact    = next(fact_generator)
         sign           = sign_for_sin(i)

         yield lambda x: (sign * x ** index) / fact

   def gimme_sin2(self, num):
      generator                = self.sin_lambda_generator()


      # con la list comprehention non funziona
      # senza, usando il generatore direttamente al loop for sotto,
      # funziona
      # con la comprehention tutti gli oggetti della lista calcolano la STESSA cosa
      lambdass = [ i for i in generator ]

      print(type(lambdass))
      print( lambdass[0] is lambdass[1] )
      print( lambdass[0](1) == lambdass[0](2) )

      res = 0
      for f in lambdass:
         print(f(num))
         res += f(num)

      return res

   def gimme_sin(self, num):
      generator         = self.step_two_factorial(1)
      sign_for_sin             = lambda index: -1 if index % 2 == 0 else 1

      res = 0
      for i in range(1, self.target_precision + 1):
         e, f = next(generator)
         res += (sign_for_sin(i) * num ** e) / f
      return res

      #return functools.reduce( lambda x, y: , x + y(num), lambdass, 0 )

if __name__ == '__main__':
   ma = MathApproximator()
   gen = ma.step_two_factorial(1)
   for i in range(1, 10, 2):
      _, value = next(gen)
      expect = math.factorial(i)
      assert value == expect, "Expected {} but received {} from fact({})".format(expect, value, i)

   ma       = MathApproximator(3)
   sin      = ma.gimme_sin(30)
   print("The sin of {}, approximated by {} terms is {}. Math.sin = {}".format(30, 3, sin, math.sin(30)))

   ma       = MathApproximator(3)
   sin      = ma.gimme_sin2(30)
   print("The sin2 of {}, approximated by {} terms is {}. Math.sin = {}".format(30, 3, sin, math.sin(30)))
