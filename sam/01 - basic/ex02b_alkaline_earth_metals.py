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

from operator import itemgetter
alkaline_earth_metals = [
   12, 20, 4, 38, 56, 88
]

alkaline_dict = {    "beryllium": 4, "magnesium": 12, "calcium" : 20, "strontium" : 38,
            "barium": 56, "radium" : 88
            } 

noble_gases = {  "helium": 2, "neon": 10, "argon": 18, 
            "krypton": 36, "xenon": 54, "radon": 86
            }

# If this MODULE have been executed by calling python3 modulename <args>, the
# variable __name__ will have value '__main__'. Instead, if this module was imported
# by another script, __name__ will equal the name of this imported module.
if __name__ == '__main__':
   # Highest atomic number
   print(sorted(alkaline_earth_metals)[-1])
   alkaline_earth_metals.sort()
   print(alkaline_earth_metals)

   alkaline_dict.update(noble_gases)
   names = list(alkaline_dict.items())
   names.sort(key = itemgetter(1) )
   print(names)





