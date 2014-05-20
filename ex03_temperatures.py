"""
Beyond the well-known Celsius and Fahrenheit, there are other six temperature scales: 
Kelvin, Rankine, Delisle, Newton, Réaumur, and Romer 
(Look at http://en.wikipedia.org/wiki/Comparison_of_temperature_scales to read about them).

Write a function that given a pure number(???) prints a conversion table for it among any of the 8 
scales (remember that functions are objects as well).

Write a function that given a temperature in a specified scale returns a list of all the 
corresponding temperatures in the other scales, the list must be sorted on the temperature 
and the scale must be specified (hint: use a tuple).
"""

id = lambda s: s
to_kelvin_from = {
               "Celsius": lambda s: s + 273.15,
               "Fahrenheit": lambda s: (s + 459.67) * (5/9.0),
               "Kelvin": id #,
              #"Rankine": id,
              #"Delisle": id,
              #"Newton": id,
              #"Réaumur": id,
              #"Romer": id 
               }
from_kelvin_to = {
               "Celsius": lambda s: s - 273.15,
               "Fahrenheit": lambda s: s * (9/5.0) - 459.67,
               "Kelvin": id #,
               #"Rankine": id,
               #"Delisle": id,
               #"Newton": id,
               #"Réaumur": id,
               #"Romer": id
               }

def conversions(grades, scale):
   ls = []
   for key in from_kelvin_to.keys():
      in_kelvin = to_kelvin_from[scale](grades)
      ls.append(( from_kelvin_to[key](in_kelvin), key))
   return sorted(ls, key = lambda s: s[0])
      
   
print(conversions(20, "Celsius"))
