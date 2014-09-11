
class PositiveValue():
   value = None

   def __get__(self, instance, owner = None):
      print("Getting value {} inst: {} owner: {}".format(self.value, instance, owner))
      return self.value or None

   def __set__(self, instance, value):
      print("Setting value to {}, inst: {}".format(value, instance))
      if(value < 0):
         raise ValueError("Product value cannot be negative")

      self.value = value
      return value

class Product():
   price = PositiveValue()


p = Product()
print(p.price)
p.price = 123
print(p.price)

try:
   p.price = -123
except ValueError:
   print("You cannot assign a negative value!")

# problem:
p2 = Product()
print(p2.price)
print(p2.price == p.price) # True

# Solution:
from weakref import WeakKeyDictionary
class PositiveValue2():
   data = WeakKeyDictionary()

   def __get__(self, instance, owner = None):
      print("Getting value {} inst: {} owner: {}".format(self.data[instance], instance, owner))
      return self.data.get(instance)

   def __set__(self, instance, value):
      print("Setting value to {}, inst: {}".format(value, instance))
      if(value < 0):
         raise ValueError("Product value cannot be negative")

      self.data[instance] = value
      return value

class Product2():
   price = PositiveValue2()

p_fix = Product2()
p_fix.price = 123
p_fix2 = Product2()
print(p_fix2.price == p_fix.price)
print(p_fix2.price)
print(p_fix.price)


