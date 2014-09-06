

# Mode 1: making a iterable from a class
class Reverser:

   def __init__(self, data = []):
      self._data = data
      self._index = len(data)


   # The __iter__ metho must setup an iterator and return it
   # an iterator is whatever object that defines a __next__ method
   # in this case, is the object itself, but it could be another one
   def __iter__(self):
      self._index = len(self._data)
      return self

   # The next method must return one element at a time on each call
   # and save the state in order to proceed through the sequence
   # When it's finished, it must raise StopIteration
   def __next__(self):
      if self._index == 0:
         raise StopIteration
      self._index = self._index - 1
      return self._data[self._index]

test = Reverser([1, 2, 3, 4, 5])
it = iter(test) # calls __iter__

try:
   while True:
      print(next(it))
except StopIteration:
   print("Finished Class Reverser")

# The for i in iterator syntax will automatically call iter, next and
# handle the StopIteration exception. This is powerful, bitch!
for i in Reverser([1, 2, 3, 4, 5]):
   print(i)
   
# Mode 2, with a generator function
# we don't have to write the next nor the iter functions
# At each call of next on the generator, it remembers automatically the 
# context. The idea is to write a loop that, with a print instead of a yield
# would print the whole sequence we're interested in.
def myreverse(iterable):
   for i in range(len(iterable) -1, -1, -1):
      yield iterable[i]

for c in myreverse("samuel"):
   print(c)

s = myreverse("leumas123")
try:
   while True:
      print(next(s))
except StopIteration:
   print("Finished manual myreverse")
else:
   print("This will never be executed")
finally:
   print("Anyway, the generator works!")

# generator expression
sum_squares = sum(i*i for i in range(10))
print(sum_squares) 

