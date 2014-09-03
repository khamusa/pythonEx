
"""
Format: "{" [field_name] ["!" conversion] [":" format_spec] "}"

   - conversions: !a, !s, !r (the methods ascii, str and repr are applied)
   - format_specs:
      :.Nf -> prints a number as a float with N decimals
      :X.Nf -> prints an number as a floating point with N decimals, right-aligned
               - in a column of width X

            - the f actually represents the type conversion, which can be one of:
               "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X" | "%"
"""

print("An integer as a float with 2 decimals: {0:.2f}".format(-123))
print("An integer as a float with 2 decimals, right-align in a column of width 10:\n {0:10.2f}".format(-123))
print("Same, with x's filling the empty spaces:\n {0:x>10.2f}".format(-123))
print("Same, with x's filling the empty spaces, align center:\n {0:x^10.2f}".format(-123))
print("Same, filling with 0's and forcing the sign to be placed before them:\n {0:0=10.2f}".format(-123))
print("Same, just filling with 0's (LOL):\n {0:0>10.2f}".format(-123))
print("Same, just filling with 0's (LOL), left aligned:\n {0:0<10.2f}".format(-123))

print("An integer as binary:\n {0:b}".format(123))
print("An integer in exponential notation:\n {0:e}".format(123))


print("Calling ascii() as conversion method: {0!a}".format('Samus ®'))
print("Calling repr() as conversion method: {0!r}".format(('Samuel', 'è', 'Legal')))
print("Calling str() as conversion method: {0!s}".format(('Samuel', 'è', 'Legal')))

""" Using keywords """
phrase = "{sam} is a {adj} {noumn}"

print(phrase.format(sam= "Samuel", adj= "nice", noumn= "guy"))
kdict = { "sam": "Someone", "adj": "baddass", "noumn": "killer" }
print(phrase.format(**kdict)) # dictionary unpacking

# alternative dictionary usage (using [] syntax for accessing key values):
print("{0[sam]} is a {0[adj]} {0[noumn]}!".format(kdict))

#  Finally, we can also use the % operator
print('The value of PI is approximately %5.3f.' % math.pi)