
# Lists:

print("Evens list: ", [ x for x in range(5) if x % 2 == 0 ])

# Sets
print("Set: ", { x for x in "abecedário" if x in "samuel" })

# Dictionaries:
words = [ "samuel", "samba", "leumas", "words" ]
canonic = lambda w: "".join(sorted(w)) 
print("Dict: ", { canonic(x): True for x in words } )

print("From key/values dict: ", dict([("sam", 123), ("José", 145)]))