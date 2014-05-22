import functools
def sum1():
  """ Sum all the natural numbers below one thousand that are multiples of 3 or 5 """
  return sum([ x for x in range(1000) if(x%3==0 or x%5==0) ])

def sum2():
  """ Sum all the natural numbers below one thousand that are multiples of 3 or 5 """
  return functools.reduce( lambda x,y: x+y , [x for x in range(1000) if(x%3==0 or x%5==0) ] )

def smallest(n):
  """ Calculate the smallest number divisible by each of the numbers 1 to 20 """
  is_divisible_for = lambda x,y : (x%y)==0
  divisible = functools.reduce( lambda acc,i : is_divisible_for(n,i) & acc , [ x for x in range(1,9) ] , True )

  if( divisible ):
    return n
  else:
    return smallest(n+1)

def figures():
  """ Calculate the sum of the figures of 2^1000 """
  return sum( [int(x) for x in str(2**1000)] )

def fib():
  """Calculate the first term in the Fibonacci sequence to contain 1000 digits"""


print(sum1())
print(sum2())
print(figures())
print(smallest(1))
