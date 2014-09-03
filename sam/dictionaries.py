mydict = { "sam": 123, "tha": 456 }
otherdict = {"gab" : 333 }

print(mydict)
my2 = mydict.copy()
mydict.update(otherdict)
print(mydict)
print(my2)

sam = mydict.pop("sam")
print(sam)
print(mydict)

sam2 = mydict.pop("sam", "The key sam is not present")
print(sam2)

dict_as_tuples = mydict.items()
print(dict_as_tuples)
print(mydict.values())

"""Calling d.keys() will return a dictionary view object. It supports operations
like membership test and iteration, but its contents are not independent of the
original dictionary – it is only a view.
"""
keys = mydict.keys()
print(keys) # gab will be present
mydict.pop("gab")
print(keys) # Gab will not be present

def new_dict(**keywords):
   return { key: value for key, value in keywords.items() }

print(new_dict(samu=123, gab="legal", mon="ca"))
