#!/usr/bin/env python3
import sys

print("The name of the program is {}".format(sys.argv[0]))

if len(sys.argv) > 1:
   print("The following args were supplied:")
   for arg in sys.argv[1:]:
      print(arg)
else:
   print ("No arguments supplied")
