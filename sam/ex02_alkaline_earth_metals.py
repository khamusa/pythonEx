"""
Assign a list that contains the atomic numbers of the six alkaline earth metals -- beryllium (4), 
magnesium (12), calcium (20), strontium (38), barium (56), and radium (88) -- 
to a variable called alkaline_earth_metals.

Write code that returns the highest atomic number in alkaline_earth_metals.
Using one of the list methods, sort alkaline_earth_metals in ascending order (from the lightest to 
the heaviest).
Transform the alkaline_earth_metals into a dictionary using the name of the metals as the 
dictionary's key.
Create a second dictionary containing the noble gases -- helium (2), neon (10), argon (18), 
krypton (36), xenon (54), and radon (86) -- and stored in the variable noble_gases.

Merge the two dictionaries and print the result as couples (name, atomic number) sorted in 
ascending order on the element names.

Note that Python's dictionaries do not preserve the insertion order neither it is sorted in 
some way.
"""

import functools
alkaline_earth_metals = [ 
                           ("beryllium", 4), 
                           ("magnesium", 12), 
                           ("calcium", 20), 
                           ("strontium", 38), 
                           ("barium", 56), 
                           ("radium", 88)
                        ]

my_dict = dict(alkaline_earth_metals)

noble_gases = { "helium": 2, "neon": 10, "argon": 18, 
"krypton": 36, "xenon": 54, "radon": 86 }

full_dict = dict(list(my_dict.items()) + list(noble_gases.items()))


def highest_alkaline():
   bigger = 0
   for _, number in alkaline_earth_metals:
      if(number > bigger):
         bigger = number
   return bigger


def sort_metals(ls):
   def extract(tuple):
      return tuple[1]
   return sorted(ls, key=extract)

print(highest_alkaline())

print(sort_metals(alkaline_earth_metals))

print(sort_metals(full_dict.items()))


