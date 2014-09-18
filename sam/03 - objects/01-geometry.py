""" Exercise 1: Playing around with Geometry. To implement the classes
representing: equilateral triangles, circles, rectangles, squares and pentagons
with the following characteristics/properties/capabilities.

- they should understand the calculate_area() and calculate_perimeter() messages
   with the obvious meaning 
- the state must be private 
- a list of geometric shapes must be sortable by area and by perimeter 
   (not at the same time, of course) 
- to add an hexagon class should maintain all the capabilities of the existing
   classes and correctly interact with them 
- to write a iterator that permits to return the elements of a list of geometric
shapes sorted by increasing areas.
"""
import unittest, math
from collections import deque

def create_shape(name, area_lambda, perimeter_lambda):
   class shape_class:
      def __init__(self, side_radius):
         self._side_radius = side_radius

      def calculate_area(self):
         return area_lambda(self._side_radius)

      def calculate_perimeter(self):
         return perimeter_lambda(self._side_radius)

      def __str__(self):
         return "{}({}), with area {} and perimeter {}".format(name, \
                        self._side_radius, \
                        self.calculate_area(), self.calculate_perimeter())

      def __repr__(self):
         return str(self)

      def __lt__(self, other):
         return self.lessthan(other)

      def lessthan(self, other):
         return self.calculate_area() < other.calculate_area()


   return shape_class


circle = create_shape("Circle", \
                  area_lambda = lambda side_radius: math.pi * side_radius ** 2, \
                  perimeter_lambda = lambda side_radius: 2 * math.pi * side_radius)

square = create_shape("Square", \
                  area_lambda = lambda side_radius: side_radius ** 2, \
                  perimeter_lambda = lambda side_radius: 4 * side_radius)

class TestCircle(unittest.TestCase):
   area_lambda = lambda side_radius: math.pi * side_radius ** 2
   perimeter_lambda = lambda side_radius: 2 * math.pi * side_radius

   def test_area(self):
      for i in range(100):
         c = circle(i)
         self.assertIn("Circle", str(c))
         self.assertEqual(c.calculate_area(), TestCircle.area_lambda(i) )

   def test_perimeter(self):
      for i in range(100):
         c = circle(i)
         self.assertEqual(c.calculate_perimeter(), TestCircle.perimeter_lambda(i) )

class TestSquare(unittest.TestCase):
   area_lambda = lambda side_radius: side_radius ** 2
   perimeter_lambda = lambda side_radius: side_radius * 4

   def test_area(self):
      for i in range(100):
         c = square(i)
         self.assertIn("Square", str(c))
         self.assertEqual(c.calculate_area(), TestSquare.area_lambda(i) )

   def test_perimeter(self):
      for i in range(100):
         c = square(i)
         self.assertEqual(c.calculate_perimeter(), TestSquare.perimeter_lambda(i) )


class ShapesList:

   def __init__(self, ls = []):
      self._ls = sorted(ls)

   def __str__(self):
      return "\n".join([str(shape) for shape in self._ls])

   def add(self, shape):

      def sorted_insert(ls, el):
         if len(ls) == 0:
            return [el]
         else:
            h, *t = ls
            if(el.calculate_area() < h.calculate_area()):
               return [el] + ls
            else:
               return [h] + sorted_insert(t, el)

      self._ls = sorted_insert(self._ls, shape)

import random

if __name__ == '__main__': 

   ls = [ random.choice([square, circle])(i) for i in range(20) ]  
   ls.sort()
   print(ls)

   def less_perimeter(self, other): 
      return self.calculate_perimeter() < other.calculate_perimeter()

   for sh in ls:
      sh.lessthan = less_perimeter.__get__(sh)

   input("Type anything to see ordering by perimeter")
   ls.sort()
   print(ls)

   sl = ShapesList(ls)
   print(sl)

   sl.add(circle(22))
   sl.add(circle(19.5))
   sl.add(circle(17.5))

   print(sl)


   unittest.main()